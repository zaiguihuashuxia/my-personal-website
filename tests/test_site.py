from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import markdown

from scripts.site import (
    ContentValidationError,
    build_navigation,
    collect_documents,
    inspect_site,
    read_document,
    validate_content,
)


class SiteToolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative_path: str, content: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_title_is_required(self) -> None:
        self.write("index.md", "# Missing title\n")
        with self.assertRaisesRegex(ContentValidationError, "required frontmatter field 'title'"):
            validate_content(self.root)

    def test_series_requires_integer_order(self) -> None:
        self.write(
            "index.md",
            "---\ntitle: Series page\nseries: demo\n---\n\n# Series page\n",
        )
        with self.assertRaisesRegex(ContentValidationError, "requires an integer 'order'"):
            validate_content(self.root)

    def test_broken_link_identifies_source(self) -> None:
        self.write(
            "guide/index.md",
            "---\ntitle: Guide\n---\n\n[Missing](missing.md)\n",
        )
        with self.assertRaisesRegex(
            ContentValidationError, "guide/index.md: unresolved link or asset 'missing.md'"
        ):
            validate_content(self.root)

    def test_obsidian_only_syntax_is_rejected(self) -> None:
        self.write(
            "index.md",
            "---\ntitle: Obsidian\n---\n\n[[Private note]]\n",
        )
        with self.assertRaisesRegex(ContentValidationError, "wikilinks/transclusions"):
            validate_content(self.root)

    def test_navigation_uses_order_without_changing_paths(self) -> None:
        self.write("index.md", "---\ntitle: Home\norder: 0\n---\n")
        self.write(
            "java/index.md",
            "---\ntitle: Java\nnav_title: Java\norder: 10\n---\n",
        )
        self.write(
            "java/second.md",
            "---\ntitle: Second\nseries: demo\norder: 20\n---\n",
        )
        self.write(
            "java/first.md",
            "---\ntitle: First\nseries: demo\norder: 10\n---\n",
        )
        documents = validate_content(self.root)
        nav = build_navigation(documents, self.root)
        java_items = nav[1]["Java"]
        self.assertEqual(java_items[1], {"First": "java/first.md"})
        self.assertEqual(java_items[2], {"Second": "java/second.md"})

    def test_artifact_inspection_rejects_private_sentinel(self) -> None:
        self.write("index.html", "PRIVATE_ONLY_SENTINEL")
        search_dir = self.root / "search"
        search_dir.mkdir()
        (search_dir / "search_index.json").write_text(
            json.dumps({"docs": [{"text": "Java 面向对象 Spring Boot IoC"}]}),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ContentValidationError, "private sentinel"):
            inspect_site(self.root)

    def test_github_pages_deploy_depends_on_successful_build(self) -> None:
        workflow = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "site.yml"
        text = workflow.read_text(encoding="utf-8")
        self.assertIn("needs: build", text)
        self.assertIn("uv run python scripts/site.py check", text)
        self.assertIn("path: site", text)
        self.assertIn("actions/deploy-pages@v4", text)

    def test_concept_template_renders_supported_structure(self) -> None:
        template = Path(__file__).resolve().parents[1] / "templates" / "concept-note.md"
        document = read_document(template, template.parent)
        rendered = markdown.markdown(
            document.body,
            extensions=["admonition", "tables", "pymdownx.superfences"],
        )
        for heading in ("为什么重要", "核心原理", "最小示例", "常见误区", "自测问题", "相关知识"):
            self.assertIn(heading, rendered)
        self.assertIn("<code", rendered)


if __name__ == "__main__":
    unittest.main()
