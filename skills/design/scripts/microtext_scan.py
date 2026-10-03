#!/usr/bin/env python3
"""microtext_scan.py - finds descriptive microtext (FEEDBACK.md F-016).

Anton's ban, 2026-09-19: small "descriptive" AI-style text - kickers/eyebrows
that describe the page instead of naming a chapter, captions that explain
what an example is, side-rails of step headings in small grey type, small
explainer lines under a heading. The test (his words): does the line exist to
fill space, explain the obvious, or look designed - or does it do a job the
reader needs? Is it smaller than the body text and about the page rather than
about the subject? See anti-patterns.md § Descriptive microtext, gate 99.

Exception: a site's own genre apparatus that is stylistic AND functional
(Calyx's edition/plate numbers, Hoerai's deliberate labels) is not flagged by
name here - this script finds candidates, a human/reviewer judges the
exception. It never sees inside an <iframe> (page.evaluate only walks the
main frame's DOM; iframe documents are separate and untouched by design).

    python microtext_scan.py --url http://localhost:3090/sites/calyx.html
    python microtext_scan.py --file some/page.html
    python microtext_scan.py --url URL --price-ledger
    python microtext_scan.py --selftest
    python microtext_scan.py --names sites/calyx.html sites/horai.html   (no browser)

--names (Anton, 2026-10-03): example and demo pages never name real places or people;
the city may stand (Stockholm). Flags street names, districts, regions, other cities,
"Hotel X", postcodes and "Firstname X." signatures in the visible text. Candidates,
like the rest of this script: a reviewer judges, the scan only finds.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Windows consoles default to cp1252; page text carries em-dashes/arrows/etc.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass

WIDTHS = (1440, 390)

# Walks the main-frame DOM only (see module docstring re: iframes).
SCAN_JS = r"""
() => {
  const BLOCK = new Set(['SCRIPT','STYLE','NOSCRIPT','TEMPLATE','IFRAME','svg','path']);
  const KICKER_RE = /kicker|eyebrow|caption|rail|label|meta|overline/i;

  function visible(el) {
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) return false;
    const cs = getComputedStyle(el);
    return cs.display !== 'none' && cs.visibility !== 'hidden' && cs.opacity !== '0';
  }
  function hasDirectText(el) {
    for (const n of el.childNodes) {
      if (n.nodeType === 3 && n.textContent.trim()) return true;
    }
    return false;
  }
  function isGrey(colorStr) {
    const m = colorStr.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)/);
    if (!m) return false;
    const [r, g, b] = m.slice(1).map(Number);
    const max = Math.max(r, g, b), min = Math.min(r, g, b);
    const sat = max === 0 ? 0 : (max - min) / max;
    return sat < 0.15;
  }
  function nearHeading(el) {
    const cands = [el.previousElementSibling, el.nextElementSibling,
      el.parentElement && el.parentElement.previousElementSibling,
      el.parentElement && el.parentElement.nextElementSibling];
    return cands.some(s => s && /^H[1-6]$/.test(s.tagName));
  }
  function selectorOf(el) {
    const cls = el.className && typeof el.className === 'string'
      ? '.' + el.className.trim().split(/\s+/)[0] : '';
    const id = el.id ? '#' + el.id : '';
    return el.tagName.toLowerCase() + id + cls;
  }

  // Body text baseline: median font-size of visible <p> elements.
  const ps = [...document.querySelectorAll('p')].filter(visible);
  const sizes = ps.map(p => parseFloat(getComputedStyle(p).fontSize)).sort((a, b) => a - b);
  const bodySize = sizes.length ? sizes[Math.floor(sizes.length / 2)]
    : parseFloat(getComputedStyle(document.body).fontSize);

  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    if (BLOCK.has(el.tagName)) continue;
    if (!visible(el) || !hasDirectText(el)) continue;
    const text = el.textContent.trim().replace(/\s+/g, ' ');
    if (!text) continue;
    const cs = getComputedStyle(el);
    const px = parseFloat(cs.fontSize);
    if (px >= bodySize - 0.5) continue; // must be smaller than body text

    const reasons = [];
    if (el.tagName === 'FIGCAPTION') reasons.push('figcaption');
    if (KICKER_RE.test(el.className || '')) reasons.push('class:kicker-like');
    const lsPx = cs.letterSpacing === 'normal' ? 0 : parseFloat(cs.letterSpacing) || 0;
    if (cs.textTransform === 'uppercase' && (lsPx / px) > 0.08) reasons.push('uppercase+tracking');
    const wordCount = text.split(' ').length;
    if (wordCount <= 8 && isGrey(cs.color) && nearHeading(el)) reasons.push('short-grey-line-near-heading');

    if (reasons.length) {
      out.push({ selector: selectorOf(el), text: text.slice(0, 70), px: Math.round(px * 10) / 10,
        reason: reasons.join('+'), bodySize: Math.round(bodySize * 10) / 10 });
    }
  }
  return out;
}
"""

# Heuristic ledger check: a text cell sized like the digit cells beside it.
PRICE_JS = r"""
() => {
  const NUM_RE = /^[\d\s.,]+(\s*(kr|sek|:-|\$|€))?$/i;
  const cells = [...document.querySelectorAll('body *')].filter(el => {
    const t = el.textContent.trim();
    return t && el.children.length === 0 && t.length < 24;
  });
  const numeric = cells.filter(el => NUM_RE.test(el.textContent.trim()) && /\d/.test(el.textContent));
  const out = [];
  for (const num of numeric) {
    const parent = num.parentElement;
    if (!parent) continue;
    const numPx = parseFloat(getComputedStyle(num).fontSize);
    for (const sib of parent.children) {
      if (sib === num || numeric.includes(sib)) continue;
      const text = sib.textContent.trim();
      if (!text || NUM_RE.test(text)) continue;
      const sibPx = parseFloat(getComputedStyle(sib).fontSize);
      if (Math.abs(sibPx - numPx) < 0.5) {
        out.push({ selector: sib.tagName.toLowerCase(), text: text.slice(0, 60),
          px: Math.round(sibPx * 10) / 10, reason: 'text-cell = digit-cell font-size (' + numPx + 'px)' });
      }
    }
  }
  return out;
}
"""


def scan(url: str, price_ledger: bool) -> dict[int, list[dict]]:
    findings: dict[int, list[dict]] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width in WIDTHS:
            page = browser.new_page(viewport={"width": width, "height": 900})
            page.goto(url, wait_until="networkidle")
            rows = page.evaluate(SCAN_JS)
            if price_ledger:
                rows += page.evaluate(PRICE_JS)
            findings[width] = rows
            page.close()
        browser.close()
    return findings


def report(url: str, findings: dict[int, list[dict]]) -> int:
    total = 0
    print(f"\n=== {url} ===")
    for width, rows in findings.items():
        print(f"-- viewport {width}px --")
        if not rows:
            print("  (none)")
            continue
        for r in rows:
            print(f"  {r['selector']:<28} {r['px']:>5}px  {r['reason']:<32} {r['text']!r}")
        total += len(rows)
    print(f"Total findings: {total}")
    return 1 if total else 0


def to_file_url(path: str) -> str:
    return Path(path).resolve().as_uri()


SELFTEST_HTML = """
<html><body>
<p>This is ordinary body copy, set at a normal reading size for the page.</p>
<h2>Om oss</h2>
<span style="font-size:11px;color:#666">Ett kort stycke som bara förklarar rubriken ovan.</span>
<p style="font-size:10px;text-transform:uppercase;letter-spacing:0.2em">EXEMPELCASE</p>
<figcaption style="font-size:10px">Exempelsida: Hoerai, Asian fusion-koncept</figcaption>
<div class="ledger-row">
  <span class="price">2480</span>
  <span class="price-note" style="font-size:16px">Pris vid foerfraagan</span>
</div>
</body></html>
"""


ALLOWED_PLACES = {"Stockholm"}
NAME_PATTERNS = [
    ("street", re.compile(r"\b[A-ZÅÄÖ][a-zåäöé]+(?:gatan|vägen|torget|gränd|backen|stigen|allén|kajen|stranden)\b(?:\s+\d+\w?)?")),
    ("street", re.compile(r"\b[A-ZÅÄÖ]+(?:GATAN|VÄGEN|TORGET|GRÄND)\b")),
    ("hotel", re.compile(r"\bHotell?\s+[A-ZÅÄÖ][\wåäö]+")),
    ("postcode", re.compile(r"\b\d{3}[\s ]\d{2}[\s ]+[A-ZÅÄÖ]")),
    ("signature", re.compile(r"\b[A-ZÅÄÖ][a-zåäöé]+\s[A-ZÅÄÖ]\.(?=\s|$|,)")),
    # R9 walk found what the first version missed: "IDUN & MARIT LINDSTRÖM", "by Bodil Sjöö"
    ("surname", re.compile(r"\b[A-ZÅÄÖ][A-Za-zÅÄÖåäöé]+(?:ström|berg|gren|qvist|kvist|sson|son|lund|holm|dahl|STRÖM|BERG|GREN|QVIST|SSON|LUND|HOLM|DAHL)\b")),
    ("credit", re.compile(r"\bby\s+[A-ZÅÄÖ][a-zåäöé]+\s+[A-ZÅÄÖ][a-zåäöé]+")),
    ("place", re.compile(r"\b(?:Östermalm|Södermalm|Söder|Vasastan|Kungsholmen|Djurgården|Norrmalm|Gamla stan|Hornstull|"
                         r"Hammarby|Lidingö|Solna|Nacka|Bromma|Söderåsen|Visby|Tyresta|Smögen|Grebbestad|Riddarfjärden|[Gg]amla [Ss]tan|Skåne|Småland|Göteborg|Malmö|Uppsala|Lund|Kyoto|Bangkok|Tokyo|Paris|London)\b")),
]


def scan_names(html: str) -> list[tuple[str, str]]:
    text = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", html)
    text = re.sub(r"<[^>]+>", " ", text).replace("&nbsp;", " ").replace("&apos;", "'")
    text = re.sub(r"\s+", " ", text)
    return [(kind, m.group(0)) for kind, rx in NAME_PATTERNS for m in rx.finditer(text)
            if m.group(0).lower() not in {p.lower() for p in ALLOWED_PLACES}]


def selftest_names() -> None:
    bad = scan_names("<p>Cmsn. 0211 — Hotel Pigalle, Drottninggatan</p><p>Strandvägen 7B, Vasastan</p>"
                     "<p>HORNSGATAN&nbsp;58 · 118&nbsp;49&nbsp;STOCKHOLM</p><p>Magnus K. — Aira</p>"
                     "<p>IDUN &amp; MARIT LINDSTRÖM</p><p>hand-thrown by Bodil Sjöö</p>")
    kinds = {k for k, _ in bad}
    assert {"hotel", "street", "place", "postcode", "signature", "surname", "credit"} <= kinds, kinds
    assert not scan_names("<p>Ateljé i Stockholm. Hotel lobby. Private home.</p>"), "false positive"
    print("SELFTEST names: PASS")


def selftest() -> None:
    selftest_names()
    tmp = Path(__file__).parent / "_microtext_selftest.html"
    tmp.write_text(SELFTEST_HTML, encoding="utf-8")
    try:
        findings = scan(to_file_url(str(tmp)), price_ledger=True)
        rows = findings[1440]
        reasons = {r["reason"] for r in rows}
        assert any("uppercase+tracking" in r for r in reasons), "eyebrow not caught"
        assert any(r == "figcaption" for r in reasons), "caption not caught"
        assert any("short-grey-line-near-heading" in r for r in reasons), "grey explainer line not caught"
        price_rows = [r for r in rows if "digit-cell" in r["reason"]]
        assert price_rows, "price-ledger same-size text cell not caught"
        body_texts = [r["text"] for r in rows]
        assert not any("ordinary body copy" in t for t in body_texts), "false positive on body copy"
        print("SELFTEST: PASS")
    finally:
        tmp.unlink(missing_ok=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--url")
    ap.add_argument("--file")
    ap.add_argument("--price-ledger", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--names", nargs="+", metavar="FILE")
    args = ap.parse_args()

    if args.names:
        hits = [(f, k, t) for f in args.names for k, t in scan_names(Path(f).read_text(encoding="utf-8"))]
        for f, k, t in hits:
            print(f"{f}: {k}: {t}")
        print(f"names: {len(hits)} candidate(s)")
        return 1 if hits else 0

    if args.selftest:
        selftest()
        return 0

    if not args.url and not args.file:
        ap.error("pass --url or --file (or --selftest)")
    target = args.url or to_file_url(args.file)
    findings = scan(target, args.price_ledger)
    return report(target, findings)


if __name__ == "__main__":
    sys.exit(main())
