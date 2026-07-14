#!/usr/bin/env python3
"""Synchronize or verify the public German against edition/german-reading.md."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "edition/german-reading.md"
OUTPUT = ROOT / "index.html"
NOTE_1 = '<sup class="fn"><a href="#note-1">1</a></sup>'


def source_paragraphs() -> dict[int, str]:
    text = SOURCE.read_text(encoding="utf-8")
    matches = list(
        re.finditer(r"^## ¶(\d+)\n\n(.*?)(?=\n\n## ¶|\n\n\[\^1\]:)", text, re.M | re.S)
    )
    result = {int(m.group(1)): m.group(2).strip().replace("[^1]", NOTE_1) for m in matches}
    if set(result) != set(range(1, 27)):
        raise SystemExit(f"expected paragraphs 1–26, found {sorted(result)}")
    return result


SECTION = re.compile(
    r'(<section class="para" id="p(?P<n>\d+)".*?'
    r'<div class="de"><p>)(?P<de>.*?)(</p></div></section>)'
)


def displayed_paragraphs(html: str) -> dict[int, str]:
    result = {int(m.group("n")): m.group("de") for m in SECTION.finditer(html)}
    if set(result) != set(range(1, 27)):
        raise SystemExit(f"expected 26 displayed paragraphs, found {sorted(result)}")
    return result


def synchronized_html(html: str, source: dict[int, str]) -> str:
    def replacement(match: re.Match[str]) -> str:
        n = int(match.group("n"))
        return f"{match.group(1)}{source[n]}{match.group(4)}"

    result, count = SECTION.subn(replacement, html)
    if count != 26:
        raise SystemExit(f"expected to replace 26 paragraphs, replaced {count}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="update index.html")
    args = parser.parse_args()

    source = source_paragraphs()
    html = OUTPUT.read_text(encoding="utf-8")
    displayed = displayed_paragraphs(html)

    if args.write:
        updated = synchronized_html(html, source)
        OUTPUT.write_text(updated, encoding="utf-8")
        print("synchronized 26 German paragraphs")
        return 0

    mismatches = [n for n in range(1, 27) if source[n] != displayed[n]]
    if mismatches:
        print("German source/output mismatch at: " + ", ".join(f"¶{n}" for n in mismatches))
        return 1
    print("German source/output match: 26 paragraphs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
