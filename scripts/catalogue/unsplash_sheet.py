#!/usr/bin/env python3
"""unsplash_sheet.py <out-dir> "<phrase>" ["<phrase>" ...]

No-API Unsplash sourcing, the AB14 method: load unsplash.com/s/photos/<phrase>
with Playwright, pull photo IDs out of the page, render a contact sheet of
images.unsplash.com/photo-<id>?w=600 thumbnails, verify each loads, and write
  <out-dir>/ids.json            [{id, phrase, loaded}]
  <out-dir>/contact-sheet.html  the sheet to LOOK at (shoot it, read it)
The judgement (pick, then re-judge under the real scrim) stays with the reader.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote
from playwright.sync_api import sync_playwright

PER_PHRASE = 12


def scrape_ids(page, phrase: str) -> list[str]:
    page.goto(f"https://unsplash.com/s/photos/{quote(phrase)}", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(2500)
    for _ in range(3):
        page.mouse.wheel(0, 1800)
        page.wait_for_timeout(700)
    html = page.content()
    ids = []
    for m in re.finditer(r"images\.unsplash\.com/photo-([0-9]{13}-[0-9a-f]{12})", html):
        if m.group(1) not in ids:
            ids.append(m.group(1))
    return ids[:PER_PHRASE]


def main():
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    # ponytail: unsplash.com returns 401/403 to headless Chromium (2026-09-04). The working path is
    # the in-app Browser pane: open the search page there, pull IDs with one JS line, and pass them
    # in as `--ids-file <json>` ({"phrase": ["id", ...]}); headless is then only used to verify loads.
    rows = []
    if sys.argv[2] == "--ids-file":
        data = json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
        phrases = list(data)
        for ph, ids in data.items():
            for pid in ids[:PER_PHRASE]:
                rows.append({"id": pid.replace("photo-", ""), "phrase": ph, "loaded": None})
    else:
        phrases = sys.argv[2:]
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        for ph in ([] if rows else phrases):
            for pid in scrape_ids(page, ph):
                rows.append({"id": pid, "phrase": ph, "loaded": None})
        # verify each thumbnail actually loads (grey box = dead ID)
        for r in rows:
            resp = page.request.get(f"https://images.unsplash.com/photo-{r['id']}?auto=format&fit=crop&w=600&q=70")
            r["loaded"] = resp.ok
        browser.close()
    (out / "ids.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    figs = "\n".join(
        f'<figure><img src="https://images.unsplash.com/photo-{r["id"]}?auto=format&fit=crop&w=600&q=70" alt="">'
        f'<figcaption>{r["id"]}<br>{r["phrase"]}{"" if r["loaded"] else " · FAILED"}</figcaption></figure>'
        for r in rows)
    html = ("<!doctype html><meta charset='utf-8'><title>contact sheet</title><style>"
            "body{margin:0;padding:24px;background:#111;color:#eee;font:12px system-ui}"
            ".grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}"
            "figure{margin:0;background:#1c1c1c;border:1px solid #333}"
            "figure img{display:block;width:100%;height:220px;object-fit:cover;background:#444}"
            "figcaption{padding:6px 8px;font:11px ui-monospace,Consolas,monospace;color:#aaa}"
            f"</style><h1>{' · '.join(phrases)} ({len(rows)} candidates)</h1><div class='grid'>{figs}</div>")
    (out / "contact-sheet.html").write_text(html, encoding="utf-8")
    ok = sum(1 for r in rows if r["loaded"])
    print(f"{len(rows)} candidates, {ok} load -> {out / 'contact-sheet.html'}")


if __name__ == "__main__":
    main()
