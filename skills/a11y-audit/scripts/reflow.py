"""Reflow checks: 320px overflow, 200% zoom overflow, reduced-motion hiding.

    python reflow.py <url|file> [--out f]

(a) At 320px width: elements whose right edge exceeds the viewport.
(b) At 200% zoom emulation (720x450, deviceScaleFactor 2): same overflow check.
(c) With prefers-reduced-motion: reduce, elements still at opacity:0 after
    2s at three scroll positions (0%, 50%, 100%) -- content a reveal system
    never shows because it depended on a scroll/observer event that never fired.

Exit 0 with findings in the JSON. Exit 2 only on tool failure.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Windows consoles/pipes often default stdout/stderr to cp1252, which
# crashes on ordinary Unicode (arrows, curly quotes, etc.) picked up from
# selectors built from page content. Force UTF-8 so a print() never blows up.
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

SELECTOR_FN = """
  function selOf(el) {
    if (el.id) return '#' + el.id;
    if (typeof el.className === 'string' && el.className.trim()) {
      return el.tagName.toLowerCase() + '.' + el.className.trim().split(/\\s+/).join('.');
    }
    return el.tagName.toLowerCase();
  }
"""

OVERFLOW_JS = """() => {
""" + SELECTOR_FN + """
  const out = [];
  document.querySelectorAll('body *').forEach(el => {
    const tag = el.tagName;
    if (tag === 'HTML' || tag === 'BODY') return;
    const s = getComputedStyle(el);
    if (s.position === 'fixed') return;
    if (s.visibility === 'hidden' || s.display === 'none') return;
    // Closed dialogs, inert regions and aria-hidden trees are not user-reachable overflow.
    if (el.closest('[aria-hidden="true"], [inert], dialog:not([open])')) return;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) return;
    // A panel translated fully off-canvas (a closed drawer) is not overflow the user can hit.
    if (r.left >= window.innerWidth - 1) return;
    if (r.right > window.innerWidth + 1) out.push(selOf(el));
  });
  return [...new Set(out)].slice(0, 20);
}
"""

HIDDEN_JS = """() => {
""" + SELECTOR_FN + """
  const out = [];
  document.querySelectorAll('body *').forEach(el => {
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return;
    if (el.closest('[aria-hidden="true"], [inert], dialog:not([open])')) return;
    const r = el.getBoundingClientRect();
    // Visually-hidden form controls behind a label (custom switches) and off-canvas panels are by design.
    if (r.width <= 2 || r.height <= 2) return;
    if (r.left >= window.innerWidth - 1 || r.right <= 1) return;
    if ((el.tagName === 'INPUT' && (el.type === 'checkbox' || el.type === 'radio')) && el.labels && el.labels.length) return;
    if (parseFloat(s.opacity) === 0) out.push(selOf(el));
  });
  return out;
}
"""


def to_url(arg):
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://", arg):
        return arg
    return Path(arg).resolve().as_uri()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--out")
    args = ap.parse_args()

    try:
        url = to_url(args.target)
        with sync_playwright() as p:
            browser = p.chromium.launch()

            # (a) 320px width
            page = browser.new_page(viewport={"width": 320, "height": 800})
            page.goto(url, wait_until="networkidle", timeout=60000)
            page.wait_for_timeout(500)
            overflow_320 = page.evaluate(OVERFLOW_JS)
            page.close()

            # (b) 200% zoom emulation
            page = browser.new_page(viewport={"width": 720, "height": 450}, device_scale_factor=2)
            page.goto(url, wait_until="networkidle", timeout=60000)
            page.wait_for_timeout(500)
            overflow_zoom = page.evaluate(OVERFLOW_JS)
            page.close()

            # (c) reduced motion, three scroll positions
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.emulate_media(reduced_motion="reduce")
            page.goto(url, wait_until="networkidle", timeout=60000)
            page.wait_for_timeout(500)
            hidden_selectors = set()
            for frac in (0.0, 0.5, 1.0):
                page.evaluate(f"window.scrollTo(0, Math.round(document.documentElement.scrollHeight * {frac}))")
                page.wait_for_timeout(2000)
                for sel in page.evaluate(HIDDEN_JS):
                    hidden_selectors.add(sel)
            page.close()
            browser.close()
    except Exception as e:
        sys.stderr.write(f"reflow tool failure: {e}\n")
        sys.exit(2)

    out = {
        "overflow320": overflow_320,
        "overflowZoom200": overflow_zoom,
        "hiddenUnderReducedMotion": len(hidden_selectors),
        "hiddenSelectors": sorted(hidden_selectors),
    }
    text = json.dumps(out, indent=2, ensure_ascii=False)
    print(text)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    sys.exit(0)


if __name__ == "__main__":
    main()
