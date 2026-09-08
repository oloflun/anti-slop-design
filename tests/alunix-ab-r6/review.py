"""Orchestrator's own capture for the r6/r7 pixel review. Stdlib + Playwright + Pillow.

    python tests/alunix-ab-r6/review.py <arm> <K> [--port 3110] [--root tests/alunix-ab-r7] [--url URL]

Writes <root>/review/<arm>-<K>/ (root defaults to tests/alunix-ab-r6):
  fold-1440.png          first screen, 1440x900, motion on (reduced_motion="no-preference")
  d-25/50/75/100.png     1440 at 25/50/75/100 % of the scroll, after a 300 px scroll-through
  sp-0/5/10/15/20/25/30/40.png
                         the set-piece region: 1440 at 0/5/10/15/20/25/30/40 % of the
                         scroll -- the first 40 % is where scroll-linked set-piece motion
                         (scrub/pin) lives, so it gets denser sampling than the rest
  full-1440.png          full page after scroll-through
  grid-motion.png        fold + sp-* + d-* composed into one image to read instead of many
  grid.png               copy of grid-motion.png, kept for callers expecting the old name
  rm-fold.png             1440, reduced motion, first screen
  rm-25/50/75/100.png    1440, reduced motion, at 25/50/75/100 % of the scroll
  grid-reduced.png       rm-fold + rm-* composed into one image
  report.json            console errors, iframe titles, per-element overflow at 320/390/768/1440
"""
import json, sys, argparse, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("arm"); ap.add_argument("key"); ap.add_argument("--port", type=int, default=3110)
ap.add_argument("--root", default="tests/alunix-ab-r6", help="repo-relative root; controls the URL path prefix and the output dir")
ap.add_argument("--url", default=None, help="override the constructed URL")
a = ap.parse_args()
root = (REPO / a.root).resolve()
root_rel = root.relative_to(REPO).as_posix()
url = a.url or f"http://127.0.0.1:{a.port}/{root_rel}/runs/{a.arm}/{a.key}/index.html"
out = root / "review" / f"{a.arm}-{a.key}"
out.mkdir(parents=True, exist_ok=True)
report = {"url": url, "console": [], "overflow": {}, "iframes": []}

SET_PIECE_PCTS = (0, 5, 10, 15, 20, 25, 30, 40)

OVERFLOW_JS = """() => {
  const w = document.documentElement.clientWidth, bad = [];
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    let p = el.parentElement, clipped = false;
    while (p) { const o = getComputedStyle(p).overflowX; if (o === 'hidden' || o === 'clip') { clipped = true; break; } p = p.parentElement; }
    if (clipped) continue;
    if (r.right > w + 1 || r.left < -1) bad.push(el.tagName + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : '') + ' ' + Math.round(r.left) + '..' + Math.round(r.right));
  }
  return {clientWidth: w, scrollWidth: document.documentElement.scrollWidth, bad: bad.slice(0, 12)};
}"""

def scroll_through(page, step=300):
    h = page.evaluate("document.documentElement.scrollHeight")
    y = 0
    while y < h:
        page.evaluate(f"window.scrollTo(0,{y})"); page.wait_for_timeout(120); y += step
        h = page.evaluate("document.documentElement.scrollHeight")
    page.evaluate("window.scrollTo(0,0)"); page.wait_for_timeout(600)

def at(page, frac):
    h = page.evaluate("document.documentElement.scrollHeight - innerHeight")
    page.evaluate(f"window.scrollTo(0,{int(h*frac)})"); page.wait_for_timeout(900)

def grid_of(tiles, path):
    cell_w = 480
    thumbs = []
    for p, label in tiles:
        im = Image.open(p); im.thumbnail((cell_w, 900)); thumbs.append((im, label))
    row_h = max(t.height for t, _ in thumbs) + 22
    cols = 4; rows = (len(thumbs) + cols - 1) // cols
    grid = Image.new("RGB", (cols * (cell_w + 8) + 8, rows * (row_h + 8) + 8), "#222")
    d = ImageDraw.Draw(grid)
    for i, (im, label) in enumerate(thumbs):
        x = 8 + (i % cols) * (cell_w + 8); y = 8 + (i // cols) * (row_h + 8)
        d.text((x, y), label, fill="#ddd"); grid.paste(im, (x, y + 18))
    grid.save(path)

motion_frames = []
reduced_frames = []
with sync_playwright() as pw:
    b = pw.chromium.launch()
    # desktop, motion forced ON
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    page.on("console", lambda m: report["console"].append(f"{m.type}: {m.text[:160]}") if m.type in ("error", "warning") else None)
    page.on("pageerror", lambda e: report["console"].append(f"pageerror: {str(e)[:160]}"))
    page.goto(url, wait_until="load"); page.wait_for_timeout(2500)
    fold_p = out / "fold-1440.png"; page.screenshot(path=str(fold_p)); motion_frames.append((fold_p, "1440 · fold"))
    scroll_through(page)
    for pct in SET_PIECE_PCTS:
        at(page, pct / 100); p = out / f"sp-{pct}.png"; page.screenshot(path=str(p))
        motion_frames.append((p, f"1440 · set-piece {pct} %"))
    for f in (0.25, 0.5, 0.75, 1.0):
        at(page, f); p = out / f"d-{int(f*100)}.png"; page.screenshot(path=str(p))
        motion_frames.append((p, f"1440 · {int(f*100)} %"))
    page.evaluate("window.scrollTo(0,0)"); page.wait_for_timeout(500)
    page.screenshot(path=str(out / "full-1440.png"), full_page=True)
    report["iframes"] = page.evaluate("Array.from(document.querySelectorAll('iframe')).map(f => { try { return {src: f.getAttribute('src'), title: f.contentDocument && f.contentDocument.title} } catch(e) { return {src: f.getAttribute('src'), title: 'cross-origin'} } })")
    report["scrollHeight"] = page.evaluate("document.documentElement.scrollHeight")
    ctx.close()
    # overflow sweep
    for w in (320, 390, 768, 1440):
        ctx = b.new_context(viewport={"width": w, "height": 844 if w < 800 else 900})
        pg = ctx.new_page(); pg.goto(url, wait_until="load"); pg.wait_for_timeout(1500)
        scroll_through(pg, 600)
        worst = {"bad": []}
        for f in (0, 0.33, 0.66, 1.0):
            at(pg, f); r = pg.evaluate(OVERFLOW_JS)
            if len(r["bad"]) > len(worst["bad"]): worst = r
            worst.setdefault("scrollWidth", r["scrollWidth"]); worst.setdefault("clientWidth", r["clientWidth"])
            worst["scrollWidth"] = max(worst["scrollWidth"], r["scrollWidth"])
        report["overflow"][w] = worst
        ctx.close()
    # reduced motion
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    pg = ctx.new_page(); pg.goto(url, wait_until="load"); pg.wait_for_timeout(1500)
    p = out / "rm-fold.png"; pg.screenshot(path=str(p)); reduced_frames.append((p, "1440 · reduced motion · fold"))
    scroll_through(pg, 600)
    for f in (0.25, 0.5, 0.75, 1.0):
        at(pg, f); p = out / f"rm-{int(f*100)}.png"; pg.screenshot(path=str(p))
        reduced_frames.append((p, f"1440 · reduced motion · {int(f*100)} %"))
    ctx.close(); b.close()

grid_of(motion_frames, out / "grid-motion.png")
grid_of(reduced_frames, out / "grid-reduced.png")
(out / "grid.png").write_bytes((out / "grid-motion.png").read_bytes())  # old name, compat

(out / "report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps({k: report[k] for k in ("console", "iframes", "scrollHeight")}, ensure_ascii=False)[:1500])
for w, r in report["overflow"].items():
    print(f"overflow {w}: scrollWidth={r.get('scrollWidth')} client={r.get('clientWidth')} bad={r['bad'][:4]}")
