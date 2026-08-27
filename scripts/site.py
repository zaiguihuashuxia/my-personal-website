#!/usr/bin/env python3
"""Validate, configure, build, inspect, and serve the public knowledge site."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = ROOT / "public"
BASE_CONFIG = ROOT / "mkdocs.yml"
GENERATED_DIR = ROOT / ".generated"
GENERATED_CONFIG = GENERATED_DIR / "mkdocs.yml"
SITE_DIR = ROOT / "site"

FRONTMATTER_DELIMITER = "---"
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
OBSIDIAN_LINK = re.compile(r"!?\[\[[^\]]+\]\]")
OBSIDIAN_BLOCK_ID = re.compile(r"(?m)(?:^|\s)\^[A-Za-z0-9-]+\s*$")
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:")
PRIVATE_SENTINELS = (
    "PRIVATE_ONLY_SENTINEL",
    "DRAFT_ONLY_SENTINEL",
    "PRIVATE_ASSET_SENTINEL",
    ".obsidian/workspace",
)
SEARCH_TERMS = ("Java", "面向对象", "Spring Boot", "IoC")


class ContentValidationError(RuntimeError):
    """Raised when public content violates the publication contract."""


@dataclass(frozen=True)
class Document:
    path: Path
    relative_path: str
    metadata: Dict[str, Any]
    body: str

    @property
    def title(self) -> str:
        return str(self.metadata["title"])

    @property
    def nav_title(self) -> str:
        return str(self.metadata.get("nav_title", self.title))

    @property
    def order(self) -> int:
        value = self.metadata.get("order", 10_000)
        return value if isinstance(value, int) and not isinstance(value, bool) else 10_000


def read_document(path: Path, public_dir: Path = PUBLIC_DIR) -> Document:
    text = path.read_text(encoding="utf-8")
    metadata: Dict[str, Any] = {}
    body = text
    if text.startswith(f"{FRONTMATTER_DELIMITER}\n"):
        parts = text.split(f"\n{FRONTMATTER_DELIMITER}\n", 1)
        if len(parts) != 2:
            raise ContentValidationError(f"{path}: frontmatter is not terminated with ---")
        raw_metadata = parts[0][len(FRONTMATTER_DELIMITER) + 1 :]
        parsed = yaml.safe_load(raw_metadata) or {}
        if not isinstance(parsed, dict):
            raise ContentValidationError(f"{path}: frontmatter must be a YAML mapping")
        metadata = parsed
        body = parts[1]
    try:
        relative_path = path.relative_to(public_dir).as_posix()
    except ValueError:
        relative_path = path.name
    return Document(path, relative_path, metadata, body)


def collect_documents(public_dir: Path = PUBLIC_DIR) -> List[Document]:
    if not public_dir.is_dir():
        raise ContentValidationError(f"Public source directory does not exist: {public_dir}")
    return [read_document(path, public_dir) for path in sorted(public_dir.rglob("*.md"))]


def _link_destination(raw_target: str) -> str:
    target = raw_target.strip()
    if " " in target and not target.startswith("<"):
        target = target.split(" ", 1)[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return unquote(target.split("#", 1)[0])


def _candidate_paths(source: Path, destination: str, public_dir: Path) -> Iterable[Path]:
    base = public_dir if destination.startswith("/") else source.parent
    target = base / destination.lstrip("/")
    yield target
    if destination.endswith("/"):
        yield target / "index.md"
    elif not target.suffix:
        yield target.with_suffix(".md")
        yield target / "index.md"


def validate_content(public_dir: Path = PUBLIC_DIR) -> List[Document]:
    documents = collect_documents(public_dir)
    errors: List[str] = []
    series_orders: Dict[Tuple[str, int], str] = {}

    for document in documents:
        title = document.metadata.get("title")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{document.relative_path}: required frontmatter field 'title' is missing")

        series = document.metadata.get("series")
        order = document.metadata.get("order")
        if series is not None:
            if not isinstance(series, str) or not series.strip():
                errors.append(f"{document.relative_path}: 'series' must be a non-empty string")
            if not isinstance(order, int) or isinstance(order, bool):
                errors.append(
                    f"{document.relative_path}: ordered series article requires an integer 'order'"
                )
            else:
                key = (str(series), order)
                if key in series_orders:
                    errors.append(
                        f"{document.relative_path}: duplicate order {order} in series '{series}' "
                        f"(also used by {series_orders[key]})"
                    )
                series_orders[key] = document.relative_path

        if OBSIDIAN_LINK.search(document.body):
            errors.append(
                f"{document.relative_path}: Obsidian wikilinks/transclusions are not supported"
            )
        if OBSIDIAN_BLOCK_ID.search(document.body):
            errors.append(f"{document.relative_path}: Obsidian block IDs are not supported")

        for match in MARKDOWN_LINK.finditer(document.body):
            destination = _link_destination(match.group(1))
            if not destination or destination.startswith("#") or destination.startswith(EXTERNAL_SCHEMES):
                continue
            if any(candidate.exists() for candidate in _candidate_paths(document.path, destination, public_dir)):
                continue
            errors.append(
                f"{document.relative_path}: unresolved link or asset '{destination}'"
            )

    if errors:
        raise ContentValidationError("\n".join(errors))
    return documents


def _sort_key(document: Document) -> Tuple[int, str]:
    return document.order, document.nav_title.casefold()


def _build_directory_nav(directory: Path, by_path: Dict[Path, Document]) -> List[Any]:
    items: List[Any] = []
    index_path = directory / "index.md"
    if index_path in by_path:
        index = by_path[index_path]
        items.append(index.relative_path)

    child_entries: List[Tuple[Tuple[int, str], Any]] = []
    for child_dir in sorted(path for path in directory.iterdir() if path.is_dir()):
        child_index_path = child_dir / "index.md"
        if child_index_path not in by_path:
            continue
        child_index = by_path[child_index_path]
        child_entries.append(
            (_sort_key(child_index), {child_index.nav_title: _build_directory_nav(child_dir, by_path)})
        )

    for child_file in sorted(directory.glob("*.md")):
        if child_file.name == "index.md" or child_file not in by_path:
            continue
        document = by_path[child_file]
        child_entries.append((_sort_key(document), {document.nav_title: document.relative_path}))

    items.extend(value for _, value in sorted(child_entries, key=lambda item: item[0]))
    return items


def build_navigation(documents: Sequence[Document], public_dir: Path = PUBLIC_DIR) -> List[Any]:
    by_path = {document.path: document for document in documents}
    nav: List[Any] = []
    root_index = public_dir / "index.md"
    if root_index in by_path:
        nav.append({by_path[root_index].nav_title: by_path[root_index].relative_path})

    child_dirs = [path for path in public_dir.iterdir() if path.is_dir() and (path / "index.md") in by_path]
    child_dirs.sort(key=lambda path: _sort_key(by_path[path / "index.md"]))
    for child_dir in child_dirs:
        index = by_path[child_dir / "index.md"]
        nav.append({index.nav_title: _build_directory_nav(child_dir, by_path)})
    return nav


def generate_config(documents: Sequence[Document]) -> Path:
    config = yaml.safe_load(BASE_CONFIG.read_text(encoding="utf-8"))
    config["docs_dir"] = str(PUBLIC_DIR)
    config["site_dir"] = str(SITE_DIR)
    config["nav"] = build_navigation(documents)
    config["hooks"] = [str(ROOT / "hooks" / "knowledge_library.py")]
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_CONFIG.write_text(
        yaml.safe_dump(config, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    return GENERATED_CONFIG


def _mkdocs_executable() -> str:
    candidate = Path(sys.executable).with_name("mkdocs")
    return str(candidate) if candidate.exists() else "mkdocs"


def run_mkdocs(arguments: Sequence[str]) -> None:
    subprocess.run([_mkdocs_executable(), *arguments], cwd=ROOT, check=True)


def inspect_site(site_dir: Path = SITE_DIR) -> None:
    if not site_dir.is_dir():
        raise ContentValidationError(f"Generated site does not exist: {site_dir}")
    text_files = [
        path
        for path in site_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in {".html", ".json", ".js", ".css", ".xml", ".txt"}
    ]
    forbidden_path_parts = {"private", "drafts", "private-assets", ".obsidian"}
    leaked_paths = [
        str(path.relative_to(site_dir))
        for path in site_dir.rglob("*")
        if path.is_file() and forbidden_path_parts.intersection(path.relative_to(site_dir).parts)
    ]
    if leaked_paths:
        raise ContentValidationError(
            f"Generated artifact contains local-only path(s): {', '.join(leaked_paths)}"
        )
    combined = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in text_files)
    leaks = [token for token in PRIVATE_SENTINELS if token in combined]
    if leaks:
        raise ContentValidationError(f"Generated artifact contains private sentinel(s): {', '.join(leaks)}")

    search_index = site_dir / "search" / "search_index.json"
    if not search_index.is_file():
        raise ContentValidationError("Generated site is missing local search index")
    search_data = json.loads(search_index.read_text(encoding="utf-8"))
    search_text = json.dumps(search_data, ensure_ascii=False).replace("\u200b", "")
    missing_terms = [term for term in SEARCH_TERMS if term not in search_text]
    if missing_terms:
        raise ContentValidationError(
            f"Search index is missing representative term(s): {', '.join(missing_terms)}"
        )

    search_locations = [str(item.get("location", "")) for item in search_data.get("docs", [])]
    if not any(location.startswith("programming/java/oop/") for location in search_locations):
        raise ContentValidationError("Search index is missing Java module hierarchy context")

    oop_page = site_dir / "programming" / "java" / "oop" / "index.html"
    fundamentals_page = site_dir / "programming" / "java" / "fundamentals" / "index.html"
    standalone_page = site_dir / "programming" / "index.html"
    for required_page in (oop_page, fundamentals_page, standalone_page):
        if not required_page.is_file():
            raise ContentValidationError(f"Generated site is missing required page: {required_page}")
    oop_html = oop_page.read_text(encoding="utf-8")
    fundamentals_html = fundamentals_page.read_text(encoding="utf-8")
    standalone_html = standalone_page.read_text(encoding="utf-8")
    required_fragments = (
        'class="md-path"',
        'md-sidebar--secondary',
        'data-md-color-scheme="default"',
        'data-md-color-scheme="slate"',
        'aria-label="上一页: Java 基础"',
        'aria-label="下一页: Java Web"',
    )
    missing_fragments = [fragment for fragment in required_fragments if fragment not in oop_html]
    if missing_fragments:
        raise ContentValidationError(
            f"Java article is missing navigation/theme fragment(s): {', '.join(missing_fragments)}"
        )
    if "md-footer__link" in standalone_html:
        raise ContentValidationError("Standalone article received artificial previous/next navigation")

    rendering_fragments = (
        'class="highlight"',
        'class="kd"',
        'class="arithmatex"',
        'class="admonition warning"',
        "knowledge-flow.svg",
        "<table>",
    )
    missing_rendering = [
        fragment for fragment in rendering_fragments if fragment not in fundamentals_html
    ]
    if missing_rendering:
        raise ContentValidationError(
            f"Technical fixture is missing rendered element(s): {', '.join(missing_rendering)}"
        )


def run_unit_tests() -> None:
    suite = unittest.defaultTestLoader.discover(
        str(ROOT / "tests"), top_level_dir=str(ROOT)
    )
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)


def build(strict: bool = True) -> None:
    documents = validate_content()
    config_path = generate_config(documents)
    arguments = ["build", "--config-file", str(config_path)]
    if strict:
        arguments.append("--strict")
    run_mkdocs(arguments)


def main(argv: Optional[Sequence[str]] = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "build", "inspect", "check", "serve"))
    args = parser.parse_args(argv)

    try:
        if args.command == "validate":
            documents = validate_content()
            generate_config(documents)
            print(f"Validated {len(documents)} public Markdown files")
        elif args.command == "build":
            build(strict=True)
            print(f"Built static site at {SITE_DIR}")
        elif args.command == "inspect":
            inspect_site()
            print("Generated artifact passed privacy and search inspection")
        elif args.command == "check":
            run_unit_tests()
            build(strict=True)
            inspect_site()
            print("All knowledge-site checks passed")
        elif args.command == "serve":
            documents = validate_content()
            config_path = generate_config(documents)
            try:
                run_mkdocs(("serve", "--config-file", str(config_path)))
            except KeyboardInterrupt:
                print("Preview stopped")
    except (ContentValidationError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
