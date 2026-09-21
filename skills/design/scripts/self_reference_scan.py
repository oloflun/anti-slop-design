#!/usr/bin/env python3
"""self_reference_scan.py - the mechanical test for F-018 (chain-discipline.md R2).

FEEDBACK.md F-018: the page never narrates itself. The rule was written into
five files on 2026-09-20 and broken by the very next sentence the chain
delivered, because it was written as prose and prose loses to fluency. This is
the test that was missing.

The test is the *subject of the sentence*, not its vocabulary. A sentence whose
subject is the page, the section, the example or the selection is the page
talking about itself, however elegant the words are:

    "Vi har ingen husstil. Formen kommer ur verksamheten, och därför valde vi
     de två projekt som ligger längst ifrån varandra."

New words, same posture - it explains the page's own selection to a reader who
never asked. Four categories are reported, because they fail differently:

  page-as-subject           the sentence's subject is the page/section/chapter
  selection-justification   it explains why the page contains what it contains
  narration-of-disposition  it announces what the page is about to do
  meta-label                it names the artefact (exempel, demo, placeholder)

Like microtext_scan.py this finds *candidates*; a reviewer judges the
exception. A site's own genre apparatus that is stylistic AND functional is not
the same fault - say so in the report rather than widening this list.

    python self_reference_scan.py --file runs/V3d/index.html
    python self_reference_scan.py --text "Vi går igenom vad vi valde."
    python self_reference_scan.py --selftest

Exit 0 = clean, 1 = candidates found. The selftest must pass first: it asserts
the F-018 sentence IS flagged and that genuine service copy is NOT. A version of
this check that flags everything, or nothing, measures nothing (M3).
"""
from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass

# --- categories -----------------------------------------------------------
# Each is a list of regexes matched against a single lowercased sentence.

# Deictic only. "sidan" on its own is the *customer's* page - the deliverable,
# and the legitimate subject of most of the copy ("vad sidan ska göra för er",
# "vi bygger sidan i kod"). The fault is the page pointing at *itself*, which
# needs a demonstrative or a spatial pointer, or a disposition verb that makes
# the page the thing being described. The selftest caught the broad version.
PAGE_AS_SUBJECT = [
    r"\b(den här|denna|det här|detta) (sidan|sida|webbplats|webbplatsen|sektionen|sektion|avsnittet|avsnitt|kapitlet|kapitel|rutan|blocket)\b",
    r"\bsidan (slutar|inleds|börjar|fortsätter|består|är uppdelad|delas)\b",
    # Standalone "ovan"/"nedan" only. "ovanför" is an ordinary spatial
    # preposition ("ett tecken ovanför") and flagging it is noise.
    r"\b(här nedan|här ovan|nedan följer|som ni ser (ovan|nedan)|ovan|nedan)\b",
    r"\bthis (page|section|chapter|site|one)\b",
    r"\bthe (page|section) (below|above|that follows)\b",
]

SELECTION_JUSTIFICATION = [
    r"\bdärför valde vi\b", r"\bdärför valde\b", r"\bvi har valt ut\b",
    r"\bvi valde (de|dessa|två|tre)\b", r"\bvårt urval\b", r"\burvalet\b",
    r"\bhandplockat\b", r"\bvi har handplockat\b",
    r"\bthat'?s why we (chose|picked)\b", r"\bwe (chose|picked) (these|those|the two)\b",
    r"\bour selection\b", r"\bhand-?picked\b",
]

# "vi" + a verb that announces the page's own agenda. Not every "vi" sentence -
# "vi bearbetar texter", "vi bygger sidan", "vi börjar med ett samtal" are the
# work, and they are the copy. These verbs narrate instead of doing.
NARRATION_OF_DISPOSITION = [
    r"\bvi (går|gar) igenom\b", r"\bvi berättar\b", r"\bvi presenterar\b",
    r"\bvi (tar|tittar) upp\b", r"\bvi tittar på\b", r"\bvi förklarar\b",
    r"\bhär går vi igenom\b",
    r"\bwe'?ll walk (you )?through\b", r"\bwe go through\b", r"\bwe'?ll show you\b",
    r"\blet'?s (look|dive)\b",
]

# Narrow on purpose. "mall" and "skiss" are how this trade talks about the work
# ("utan färdig mall", "en enkel skiss") and flagging them is noise - the first
# draft did, and the selftest caught it.
META_LABEL = [
    r"\bexempelsida\b", r"\bexempel på\b", r"\bexempelcase:", r"\bplatshållare\b",
    r"\bexample page\b", r"\bsample page\b", r"\bplaceholder\b", r"\bmock-?up\b",
]

CATEGORIES = (
    ("page-as-subject", PAGE_AS_SUBJECT),
    ("selection-justification", SELECTION_JUSTIFICATION),
    ("narration-of-disposition", NARRATION_OF_DISPOSITION),
    ("meta-label", META_LABEL),
)

_COMPILED = tuple(
    (name, tuple(re.compile(p, re.IGNORECASE) for p in pats))
    for name, pats in CATEGORIES
)

# A sentence this short is usually a heading or a label already caught by its
# own category; flagging it as "narration" adds noise, not signal.
MIN_WORDS = 4


class _Text(HTMLParser):
    """Visible text only. Skips script/style/noscript/svg and the alt text of
    images (an alt is metadata, not page copy)."""

    SKIP = {"script", "style", "noscript", "template", "svg", "head"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._depth += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._depth:
            self._depth -= 1

    def handle_data(self, data):
        if not self._depth and data.strip():
            self.parts.append(data)

    def text(self) -> str:
        return " ".join(self.parts)


def sentences(text: str) -> list[str]:
    """Split on sentence enders, keeping it crude on purpose - a copy rule does
    not need a parser, it needs to survive a fluent paragraph.

    NOT on ':' - a colon starts a label's value, it does not end the sentence,
    and splitting there cuts "Exempelsida: Horai, Asian fusion-koncept" in half
    and hides it under MIN_WORDS. The selftest caught exactly that."""
    flat = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", flat) if s.strip()]


def scan(text: str) -> list[tuple[str, str]]:
    """-> [(category, sentence)] for every sentence that trips a category."""
    hits: list[tuple[str, str]] = []
    for s in sentences(text):
        if len(s.split()) < MIN_WORDS:
            continue
        for name, pats in _COMPILED:
            if any(p.search(s) for p in pats):
                hits.append((name, s))
                break
    return hits


def report(text: str, label: str) -> int:
    hits = scan(text)
    print(f"-- self-reference scan: {label}")
    if not hits:
        print("0 candidates.")
        return 0
    by_cat: dict[str, list[str]] = {}
    for name, s in hits:
        by_cat.setdefault(name, []).append(s)
    for name, _ in CATEGORIES:
        for s in by_cat.get(name, []):
            print(f"  [{name}] {s}")
    print(f"{len(hits)} candidate(s), {len(sentences(text))} sentence(s) scanned.")
    print("Candidates, not verdicts - a functional genre label may be an exception (F-016).")
    return 1


# --- selftest: the check must fail against the known-broken case first (M3) --

F018_SENTENCE = (
    "Vi har ingen husstil. Formen kommer ur verksamheten, och därför valde vi "
    "de två projekt som ligger längst ifrån varandra."
)
DISPOSITION_SENTENCE = (
    "Calyx är en florist i Stockholm och Hōrai en restaurang. Vi går igenom vad "
    "vi valde i dem och varför."
)
META_LABEL_LINE = "Exempelsida: Hōrai, Asian fusion-koncept"

# Genuine service copy, deliberately including the lines that look like the
# fault and are not. "sidan" here is the customer's page - the deliverable, and
# the subject the copy is supposed to have. If this fixture trips, the scanner
# has become noise and the selftest must fail.
CLEAN = (
    "Vi börjar med ett samtal om er verksamhet och vad sidan ska göra för er. "
    "Ni behöver inte ha något färdigt när vi börjar. Vi bearbetar texter och "
    "bilder ni har och säger till om något saknas. "
    "Vi bygger sidan i kod från grunden, utan färdig mall, så att den laddar snabbt. "
    "Sidan är er att bygga vidare på när ni vill lägga till mer. "
    "Mobilen planerar vi från början, i samma skiss som datorn. "
    "Calyx fick bli ett vårnummer."
)


def selftest() -> int:
    bad = {s for _, s in scan(F018_SENTENCE)}
    assert any("därför valde vi" in s for s in bad), (
        f"selftest FAILED: F-018 sentence not flagged. got={bad}"
    )
    disp = {s for _, s in scan(DISPOSITION_SENTENCE)}
    assert any("går igenom" in s for s in disp), (
        f"selftest FAILED: disposition sentence not flagged. got={disp}"
    )
    meta = scan(META_LABEL_LINE)
    assert meta, "selftest FAILED: meta label not flagged"

    clean = scan(CLEAN)
    assert not clean, f"selftest FAILED: clean service copy flagged: {clean}"

    print("selftest OK - F-018 sentence flagged, genuine service copy clean.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file")
    ap.add_argument("--text")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if a.text:
        return report(a.text, "text")
    if a.file:
        raw = open(a.file, encoding="utf-8", errors="replace").read()
        if a.file.lower().endswith((".html", ".htm")):
            p = _Text()
            p.feed(raw)
            raw = p.text()
        return report(raw, a.file)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
