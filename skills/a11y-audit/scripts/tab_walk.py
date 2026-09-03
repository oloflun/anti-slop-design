"""Walk the page with the keyboard (Tab) and record what happens at each stop.

    python tab_walk.py <url|file> [--max 200] [--out f]

Detects: focus traps (same element repeats >3 times), stops with an empty
accessible name, stops that land offscreen, and DOM-order vs visual-order
mismatches (a stop whose top is >200px above the previous stop's).

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
# accessible names on the page. Force UTF-8 so a print() never blows up.
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

STOP_JS = """() => {
  const el = document.activeElement;
  if (!el || el === document.body) return null;
  if (!el.dataset.a11yWalkId) { window.__a11yIdx = (window.__a11yIdx || 0) + 1; el.dataset.a11yWalkId = String(window.__a11yIdx); }
  const focusedStyle = getComputedStyle(el);
  const focusedOutlineStyle = focusedStyle.outlineStyle;
  const focusedOutlineWidth = focusedStyle.outlineWidth;
  const focusedBoxShadow = focusedStyle.boxShadow;
  el.blur();
  const unfocusedBoxShadow = getComputedStyle(el).boxShadow;
  el.focus();
  const hasOutline = focusedOutlineStyle !== 'none' && focusedOutlineWidth !== '0px';
  const hasShadowChange = focusedBoxShadow !== 'none' && focusedBoxShadow !== unfocusedBoxShadow;
  const rect = el.getBoundingClientRect();
  const byIds = (el.getAttribute('aria-labelledby') || '').split(/\s+/).filter(Boolean).map(id => (document.getElementById(id) || {}).innerText || '').join(' ').trim();
  const byLabels = (el.labels && el.labels.length) ? [...el.labels].map(l => (l.innerText || '').trim()).join(' ').trim() : '';
  const name = byIds || el.getAttribute('aria-label') || byLabels || (el.innerText || '').trim().slice(0, 60) || el.getAttribute('title') || el.alt || el.getAttribute('placeholder') && '' || '';
  const inViewport = rect.bottom > 0 && rect.right > 0 && rect.top < window.innerHeight && rect.left < window.innerWidth;
  return {
    walkId: el.dataset.a11yWalkId,
    tag: el.tagName.toLowerCase(),
    name,
    hasFocusIndicator: hasOutline || hasShadowChange,
    rect: {top: Math.round(rect.top), left: Math.round(rect.left), width: Math.round(rect.width), height: Math.round(rect.height)},
    inViewport,
    tabIndex: el.tabIndex
  };
}"""


def to_url(arg):
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://", arg):
        return arg
    return Path(arg).resolve().as_uri()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--max", type=int, default=200)
    ap.add_argument("--out")
    args = ap.parse_args()

    try:
        url = to_url(args.target)
        stops = []
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.goto(url, wait_until="networkidle", timeout=60000)
            page.wait_for_timeout(500)
            page.evaluate("document.body.focus && document.body.focus()")

            consecutive_same = 0
            last_walk_id = None
            for _ in range(args.max):
                page.keyboard.press("Tab")
                info = page.evaluate(STOP_JS)
                if info is None:
                    break  # focus left the document (reached the end)
                stops.append(info)
                if info["walkId"] == last_walk_id:
                    consecutive_same += 1
                    if consecutive_same >= 6:
                        break  # clearly stuck, stop wasting tab presses
                else:
                    consecutive_same = 0
                last_walk_id = info["walkId"]

            # Elements that look clickable (onclick handler, cursor:pointer)
            # but are not natively focusable and never received a tab stop
            # at all -- e.g. a <div onclick> with no role/tabindex. These
            # can't show up as an "issue at index N" since they never got a
            # stop; report them separately.
            unreachable = page.evaluate("""() => {
                const focusableTags = new Set(['A','BUTTON','INPUT','SELECT','TEXTAREA','SUMMARY']);
                const out = [];
                document.querySelectorAll('[onclick]').forEach(el => {
                    if (focusableTags.has(el.tagName)) return;
                    if (el.tabIndex >= 0) return;
                    if (el.dataset.a11yWalkId) return;
                    out.push({tag: el.tagName.toLowerCase(), text: (el.innerText || '').trim().slice(0, 60)});
                });
                return out;
            }""")
            browser.close()
    except Exception as e:
        sys.stderr.write(f"tab_walk tool failure: {e}\n")
        sys.exit(2)

    issues = []
    counts = {}
    prev_top = None
    for i, s in enumerate(stops):
        counts[s["walkId"]] = counts.get(s["walkId"], 0) + 1
        if not s["name"]:
            issues.append({"kind": "empty_name", "index": i, "detail": f"<{s['tag']}> has no accessible name"})
        if not s["inViewport"]:
            issues.append({"kind": "offscreen", "index": i, "detail": f"<{s['tag']}> stop lands outside the viewport"})
        if prev_top is not None and (prev_top - s["rect"]["top"]) > 200:
            issues.append({
                "kind": "order_mismatch", "index": i,
                "detail": f"stop {i} top={s['rect']['top']} is >200px above previous stop's top={prev_top}",
            })
        if not s["hasFocusIndicator"]:
            issues.append({"kind": "no_focus_indicator", "index": i, "detail": f"<{s['tag']}> {s['name']!r} has no visible focus indicator"})
        if s["tabIndex"] and s["tabIndex"] > 0:
            issues.append({"kind": "positive_tabindex", "index": i, "detail": f"<{s['tag']}> has tabindex={s['tabIndex']}"})
        prev_top = s["rect"]["top"]

    for walk_id, n in counts.items():
        if n > 3:
            issues.append({"kind": "focus_trap", "index": None, "detail": f"element walkId={walk_id} received focus {n} times"})

    for u in unreachable:
        issues.append({
            "kind": "unreachable_interactive", "index": None,
            "detail": f"<{u['tag']} onclick> {u['text']!r} has a click handler but is never keyboard-focusable (no role/tabindex)",
        })

    out = {"stops": stops, "issues": issues}
    text = json.dumps(out, indent=2, ensure_ascii=False)
    print(text)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    sys.exit(0)


if __name__ == "__main__":
    main()
