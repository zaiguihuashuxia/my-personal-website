"""MkDocs hooks for metadata-driven learning-series navigation."""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, DefaultDict, Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.site import collect_documents  # noqa: E402


SERIES: DefaultDict[str, List[Tuple[int, str]]] = defaultdict(list)


def on_config(config: Dict[str, Any]) -> Dict[str, Any]:
    SERIES.clear()
    docs_dir = Path(config["docs_dir"])
    for document in collect_documents(docs_dir):
        series = document.metadata.get("series")
        order = document.metadata.get("order")
        if isinstance(series, str) and isinstance(order, int) and not isinstance(order, bool):
            SERIES[series].append((order, document.relative_path))
    for entries in SERIES.values():
        entries.sort()
    return config


def on_nav(nav: Any, config: Dict[str, Any], files: Any) -> Any:
    pages_by_source = {page.file.src_uri: page for page in nav.pages}
    for page in nav.pages:
        page.previous_page = None
        page.next_page = None

    for entries in SERIES.values():
        pages = [pages_by_source[path] for _, path in entries if path in pages_by_source]
        for index, page in enumerate(pages):
            page.previous_page = pages[index - 1] if index > 0 else None
            page.next_page = pages[index + 1] if index + 1 < len(pages) else None
    return nav
