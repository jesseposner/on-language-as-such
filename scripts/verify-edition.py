#!/usr/bin/env python3
"""Verify the accountable reading text and its reader-visible dependents."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"
READING_PATH = ROOT / "edition/german-reading.md"
GS_PATH = ROOT / "edition/german-gs.md"
APPARATUS_PATH = ROOT / "edition/textual-apparatus.yml"


def fail(message: str) -> None:
    raise AssertionError(message)


def source_paragraphs(path: Path) -> dict[int, str]:
    text = path.read_text(encoding="utf-8")
    matches = re.finditer(
        r"^## ¶(\d+)\n\n(.*?)(?=\n\n## ¶|\n\n\[\^1\]:|\Z)", text, re.M | re.S
    )
    result = {int(match.group(1)): match.group(2).strip() for match in matches}
    if set(result) != set(range(1, 27)):
        fail(f"{path}: expected paragraphs 1–26, found {sorted(result)}")
    return result


def plain(fragment: str) -> str:
    fragment = re.sub(r"<sup\b.*?</sup>", "", fragment, flags=re.S)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = fragment.replace("[^1]", "")
    return re.sub(r"\s+", " ", fragment).strip()


class EditionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int | None]] = []
        self.current_comm: int | None = None
        self.capture: tuple[str, int] | None = None
        self.buffer: list[str] = []
        self.german_quotes: list[tuple[int, str]] = []
        self.english_quotes: list[tuple[int, str]] = []
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs_list)
        if attrs.get("id"):
            self.ids.append(attrs["id"] or "")

        if tag not in {"div", "span", "blockquote"}:
            return

        previous_comm = self.current_comm
        if tag == "div" and "comm" in (attrs.get("class") or "").split():
            self.current_comm = int(attrs["data-n"] or "0")
        self.stack.append((tag, previous_comm))

        classes = (attrs.get("class") or "").split()
        if self.current_comm and tag == "blockquote" and "deq" in classes:
            self.capture = ("de", self.current_comm)
            self.buffer = []
        elif self.current_comm and tag == "span" and {"uquote", "ours"} <= set(classes):
            self.capture = ("en", self.current_comm)
            self.buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag not in {"div", "span", "blockquote"}:
            return

        if self.capture and ((self.capture[0] == "de" and tag == "blockquote") or (self.capture[0] == "en" and tag == "span")):
            kind, paragraph = self.capture
            value = "".join(self.buffer)
            target = self.german_quotes if kind == "de" else self.english_quotes
            target.append((paragraph, value))
            self.capture = None
            self.buffer = []

        if not self.stack:
            fail(f"unexpected closing tag </{tag}>")
        start_tag, previous_comm = self.stack.pop()
        if start_tag != tag:
            # HTML permits a few implicit closures; none occur in the edition's
            # div/span/blockquote structures that matter to this verifier.
            if {start_tag, tag} & {"div", "span", "blockquote"}:
                fail(f"mismatched tags: <{start_tag}> closed by </{tag}>")
        self.current_comm = previous_comm

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.buffer.append(data)


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("\u00a0", " ")
    value = value.translate(str.maketrans("", "", "“”„»«›‹\"'’"))
    return re.sub(r"\s+", " ", value).strip()


def quote_chunks(value: str, kind: str) -> list[str]:
    value = normalized(value)
    if kind == "de":
        value = re.sub(r"^DE:\s*", "", value)
    value = value.strip("“”„»«\" ")
    chunks = re.split(r"(?:…|\.\.\.)", value)
    cleaned: list[str] = []
    for chunk in chunks:
        chunk = normalized(chunk).strip("“”„»«\" ")
        chunk = re.sub(r"^[—–-]\s*|\s*[—–-]$", "", chunk)
        if len(chunk) >= 5:
            cleaned.append(chunk)
    return cleaned


def assert_quotes(
    quotes: list[tuple[int, str]], sources: dict[int, str], kind: str
) -> None:
    failures: list[str] = []
    for paragraph, quote in quotes:
        source = normalized(plain(sources[paragraph]))
        position = 0
        for chunk in quote_chunks(quote, kind):
            found = source.find(chunk, position)
            if found < 0:
                # Commentary headings occasionally supply terminal punctuation
                # outside the excerpt's exact source boundary.
                relaxed = chunk.rstrip(".:;!?—–- ")
                found = source.find(relaxed, position)
            if found < 0:
                failures.append(f"¶{paragraph}: {chunk!r}")
                break
            position = found + len(chunk)
    if failures:
        fail(f"{kind} quotation mismatch(es): " + "; ".join(failures[:8]))


def main() -> int:
    sync = subprocess.run(
        [sys.executable, str(ROOT / "scripts/sync-german.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if sync.returncode:
        fail(sync.stdout.strip() or sync.stderr.strip())

    html = HTML_PATH.read_text(encoding="utf-8")
    reading = source_paragraphs(READING_PATH)
    gs = source_paragraphs(GS_PATH)

    differences = {n for n in reading if plain(reading[n]) != plain(gs[n])}
    if differences != {3, 14}:
        fail(f"GS/reading differences should be ¶3 and ¶14, found {differences}")

    if len(re.findall(r'<section class="para" id="p\d+"', html)) != 26:
        fail("expected 26 reading-text paragraph sections")
    if len(re.findall(r'<div class="en ours"><p>', html)) != 26:
        fail("expected 26 English reading-text paragraphs")
    if len(re.findall(r'<div class="de"><p>', html)) != 26:
        fail("expected 26 German reading-text paragraphs")

    parser = EditionParser()
    parser.feed(html)
    parser.close()
    duplicates = sorted({identifier for identifier in parser.ids if parser.ids.count(identifier) > 1})
    if duplicates:
        fail(f"duplicate HTML ids: {duplicates}")
    if len(parser.german_quotes) != 125 or len(parser.english_quotes) != 125:
        fail(
            "expected 125 German and English commentary excerpts, found "
            f"{len(parser.german_quotes)} and {len(parser.english_quotes)}"
        )

    english_sections = re.findall(
        r'<div class="en ours"><p>(.*?)</p></div><div class="de">', html, re.S
    )
    english_plain = " ".join(plain(section) for section in english_sections)
    if english_plain.lower().count("quintess") != 62:
        fail("expected 62 quintessence-family occurrences in the English reading text")

    if 'id="textual-apparatus"' not in html:
        fail("public textual apparatus is missing")
    apparatus = APPARATUS_PATH.read_text(encoding="utf-8")
    departure_block = apparatus.split("reader_notes:", 1)[0]
    if len(re.findall(r"^  - id:", departure_block, re.M)) != 2:
        fail("machine-readable apparatus must contain exactly two departures")

    stale = {
        "GS collation pending": r"GS (?:II[.-]?1|II\.1).{0,80}(?:pending|awaits)",
        "GS will settle": r"GS II-?1 will settle",
        "old defect count": r"(?:fourteen transcription defects|fifteen editorial corrections|99\.7%)",
        "old quintessence count": r"sixty-one repetitions",
        "nonexistent frontmatter": r"German file's frontmatter",
    }
    for label, pattern in stale.items():
        if re.search(pattern, html, re.I | re.S):
            fail(f"stale claim remains in index.html: {label}")

    # Quote checks run last so failures report a concrete editorial locus.
    assert_quotes(parser.german_quotes, reading, "de")

    english_by_paragraph: dict[int, str] = {}
    for match in re.finditer(
        r'<section class="para" id="p(?P<n>\d+)".*?<div class="en ours"><p>(?P<en>.*?)</p></div><div class="de">',
        html,
        re.S,
    ):
        english_by_paragraph[int(match.group("n"))] = match.group("en")
    assert_quotes(parser.english_quotes, english_by_paragraph, "en")

    print(sync.stdout.strip())
    print("GS/reading departures: ¶3, ¶14")
    print("Commentary excerpts verified: 125 German, 125 English")
    print("English quintessence-family count: 62")
    print("Edition verification passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as error:
        print(f"verification failed: {error}", file=sys.stderr)
        sys.exit(1)
