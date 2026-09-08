#!/usr/bin/env python
"""Generic scroll-page verification harness -- walks a page top to bottom in
steps of viewport/3, screenshots each stop, and reports dead scroll, cues
that never reach full opacity, unrevealed elements, and contrast over media.
Generic counterpart to scroll-craft's shoot.mjs: understands [data-sc-cue]
when present, does not require it.

  python scroll_verify.py <url> [--width 1440] [--height 900]
                           [--out DIR]

Prints one JSON report, exits 0. Needs playwright (python); Pillow is
optional (diff + contact sheet skip with a note if missing). contrast_over_
media.py next door is not import-safe (module-level Playwright, no __main__
guard) so its luminance formula is reimplemented inline instead of imported.
"""
import argparse, io, json, os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
try:
    from PIL import Image
    HAVE_PIL = True
except ImportError:
    HAVE_PIL = False

CANDIDATE_SEL = "h1,h2,h3,h4,p,a,button,[data-sc-in],[class*='reveal']"
TEXT_SEL = "h1,h2,h3,p,a,button"
CHROME_CANDIDATES = [  # a real Chrome: the bundled "headless shell" has crashed outright mid-screenshot
    os.environ.get("SCROLLCRAFT_CHROME"), "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe", "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable", "/usr/bin/chromium",
]
def find_chrome():
    return next((p for p in CHROME_CANDIDATES if p and Path(p).exists()), None)
def lum_srgb(r, g, b):
    ch = lambda v: (v / 255) / 12.92 if v <= 10.0164 else ((v / 255 + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)
def contrast_ratio(a, b):
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)
def downsample_gray(png_bytes, w=64, h=36):
    if not HAVE_PIL:
        return None
    return list(Image.open(io.BytesIO(png_bytes)).convert("L").resize((w, h)).getdata())
def mean_abs_diff(a, b):
    if a is None or b is None or len(a) != len(b):
        return None
    return sum(abs(x - y) for x, y in zip(a, b)) / (len(a) * 255.0)

TAG_JS = """(sel) => { window.__scvN = window.__scvN || 0;
  const full = sel.split(',').map(s => s.trim() + ':not([data-scv-media])').join(',');
  document.querySelectorAll(full).forEach(el => {
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    if ((parseFloat(cs.fontSize) || 0) < 14 || r.width < 8 || r.height < 8) return;
    if (r.bottom <= 0 || r.top >= innerHeight || r.right <= 0 || r.left >= innerWidth) return;
    const cx = Math.min(Math.max(r.left + r.width / 2, 0), innerWidth - 1);
    const cy = Math.min(Math.max(r.top + r.height / 2, 0), innerHeight - 1);
    const over = (document.elementsFromPoint(cx, cy) || []).some(s => {
      if (s === el || el.contains(s)) return false;
      if (['IMG', 'VIDEO', 'CANVAS'].includes(s.tagName)) return true;
      const bg = getComputedStyle(s).backgroundImage;
      return bg && bg !== 'none' && s !== document.body && s !== document.documentElement;
    });
    if (over) el.setAttribute('data-scv-media', String(window.__scvN++));
  }); }"""
STATE_JS = """(sel) => { const out = [], seen = new Set();
  document.querySelectorAll(sel).forEach(el => {
    const r = el.getBoundingClientRect();
    if (!(r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth)) return;
    const cs = getComputedStyle(el);
    const t = (el.tagName + '.' + (el.className || '').toString().split(' ')[0] + ':' +
               (el.textContent || '').trim().slice(0, 30)).replace(/\\s+/g, ' ');
    if (seen.has(t)) return;
    seen.add(t); out.push({key: t, op: parseFloat(cs.opacity), vis: cs.visibility});
  }); return out; }"""
MEDIA_JS = """() => { const out = [], cvs = document.createElement('canvas');
  cvs.width = cvs.height = 1;
  const g2 = cvs.getContext('2d');
  document.querySelectorAll('[data-scv-media]').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.bottom <= 0 || r.top >= innerHeight || r.width < 8 || r.height < 8) return;
    const cs = getComputedStyle(el);
    g2.fillStyle = cs.color; g2.fillRect(0, 0, 1, 1);
    const px = g2.getImageData(0, 0, 1, 1).data;
    out.push({ id: el.getAttribute('data-scv-media'),
      x: Math.max(0, r.left), y: Math.max(0, r.top),
      w: Math.min(innerWidth, r.right) - Math.max(0, r.left),
      h: Math.min(innerHeight, r.bottom) - Math.max(0, r.top),
      rgb: [px[0], px[1], px[2]], size: parseFloat(cs.fontSize),
      text: (el.textContent || '').trim().slice(0, 40) });
  }); return out; }"""
HIDE_JS = """() => document.querySelectorAll('[data-scv-media]').forEach(el => {
  el.setAttribute('data-scv-prevvis', el.style.visibility || '');
  el.style.setProperty('visibility', 'hidden', 'important'); })"""
RESTORE_JS = """() => document.querySelectorAll('[data-scv-media]').forEach(el => {
  el.style.visibility = el.getAttribute('data-scv-prevvis') || '';
  el.removeAttribute('data-scv-prevvis'); })"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--out", default="scroll_verify_out")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    report = {"url": args.url, "positions": [], "deadScroll": [], "cuesNeverFull": [], "unrevealed": [],
              "contrastUnderMedia": [], "contactSheet": None, "notes": []}
    media_track = {}
    with sync_playwright() as pw:
        chrome = find_chrome()
        browser = pw.chromium.launch(executable_path=chrome) if chrome else pw.chromium.launch()
        if not chrome:
            report["notes"].append("No installed Chrome found; used Playwright's bundled headless shell, known to crash on some pages. Set SCROLLCRAFT_CHROME.")
        ctx = browser.new_context(viewport={"width": args.width, "height": args.height}, device_scale_factor=1)  # F-011: motion always plays; no reduced-motion mode to verify
        page = ctx.new_page()
        page.goto(args.url, wait_until="load", timeout=30000)
        page.wait_for_timeout(400)
        doc_h = page.evaluate("document.documentElement.scrollHeight")
        step, max_y = max(1, args.height // 3), max(0, doc_h - args.height)
        positions = sorted(set(list(range(0, max_y, step)) + [max_y]))
        gray_frames, cue_track = [], {}
        for i, y in enumerate(positions):
            page.evaluate("(y) => scrollTo(0, y)", y)
            page.wait_for_timeout(250)
            gray_frames.append(downsample_gray(page.screenshot(path=str(out / f"{i:02d}.png"))))
            page.evaluate(TAG_JS, TEXT_SEL)
            for e in page.evaluate(STATE_JS, CANDIDATE_SEL):
                rec = cue_track.setdefault(e["key"], {"peak": 0.0})
                rec["peak"] = max(rec["peak"], 0.0 if e["vis"] == "hidden" else e["op"])
            media = page.evaluate(MEDIA_JS)
            if media and HAVE_PIL:
                page.evaluate(HIDE_JS)
                plate = Image.open(io.BytesIO(page.screenshot())).convert("RGB")
                page.evaluate(RESTORE_JS)
                for m in media:
                    x0, y0 = int(m["x"]), int(m["y"])
                    x1, y1 = max(int(m["x"] + m["w"]), x0 + 1), max(int(m["y"] + m["h"]), y0 + 1)
                    px = list(plate.crop((x0, y0, min(x1, plate.width), min(y1, plate.height))).getdata())
                    if not px:
                        continue
                    lums = sorted(lum_srgb(*p[:3]) for p in px)
                    ratio = contrast_ratio(lum_srgb(*m["rgb"]), lums[int(len(lums) * 0.95)])
                    key, floor = m["id"] + ":" + m["text"], (3.0 if m["size"] >= 24 else 4.5)
                    slot = media_track.setdefault(key, {"worst": ratio, "text": m["text"], "floor": floor})
                    slot["worst"] = min(slot["worst"], ratio)
            report["positions"].append(y)
        if HAVE_PIL:  # dead scroll: <1.5% mean-abs-diff on a coarse grayscale downsample, y advancing >= vh/3
            for i in range(1, len(positions)):
                d = mean_abs_diff(gray_frames[i - 1], gray_frames[i])
                if d is not None and d < 0.015 and positions[i] - positions[i - 1] >= step - 1:
                    report["deadScroll"].append({"from": positions[i - 1], "to": positions[i], "diff": round(d, 4)})
        else:
            report["notes"].append("Pillow not installed: deadScroll / contact sheet skipped.")
        for key, rec in cue_track.items():
            if rec["peak"] <= 0.02:
                report["unrevealed"].append(key)
            elif rec["peak"] < 0.98:
                report["cuesNeverFull"].append({"el": key, "peakOpacity": round(rec["peak"], 3)})
        for slot in media_track.values():
            if slot["worst"] < slot["floor"]:
                report["contrastUnderMedia"].append({"text": slot["text"], "worst": round(slot["worst"], 2), "floor": slot["floor"]})
        if HAVE_PIL and positions:
            cols, rows = min(5, len(positions)), -(-len(positions) // min(5, len(positions)))
            tw, first = 260, Image.open(out / "00.png")
            th = int(tw * first.height / first.width)
            sheet = Image.new("RGB", (cols * tw, rows * th), (30, 30, 30))
            for i in range(len(positions)):
                sheet.paste(Image.open(out / f"{i:02d}.png").resize((tw, th)), ((i % cols) * tw, (i // cols) * th))
            sheet.save(out / "sheet.png")
            report["contactSheet"] = str(out / "sheet.png")
        elif not HAVE_PIL:
            report["notes"].append("Pillow not installed: sheet.png skipped.")
        # blankBands: a full-page capture (no scroll) with a near-uniform vertical band taller
        # than 60% of a viewport is a pinned act with sparse content, or a reveal that never
        # fired. Reads as a broken page in every static view (AB06, T17 on 2026-09-03).
        report["blankBands"] = []
        if HAVE_PIL:
            try:
                page.evaluate("window.scrollTo(0,0)"); page.wait_for_timeout(300)
                page.screenshot(path=str(out / "full.png"), full_page=True)
                im = Image.open(out / "full.png").convert("L")
                w, h = im.size
                small = im.resize((max(1, w // 8), h))
                px = small.load(); sw = small.size[0]
                flat = []
                for y in range(h):
                    row = [px[x, y] for x in range(sw)]
                    m = sum(row) / sw
                    var = sum((v - m) ** 2 for v in row) / sw
                    flat.append(var < 16)
                start = None
                for y, f in enumerate(flat + [False]):
                    if f and start is None: start = y
                    if not f and start is not None:
                        if y - start >= 0.6 * args.height:
                            report["blankBands"].append({"from": start, "to": y, "px": y - start})
                        start = None
            except Exception as e:
                report["notes"].append(f"blankBands skipped: {e}")
        browser.close()
    print(json.dumps(report, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
