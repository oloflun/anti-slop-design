#!/usr/bin/env python3
"""contrast_over_media.py - contrast for text over media, measured from rendered pixels.

Computed style cannot answer this: the ground is a photograph or a video frame.
So the text is hidden, the fold is screenshotted, and the luminance of the exact
rectangle each string occupied is sampled from that plate. Worst case uses the
brightest 5 % of the ground under the string, not the mean, because one blown
highlight is where the text actually disappears.

    python contrast_over_media.py --url URL [--width 1440 --height 900]
        [--selectors "h1, header a, section p"] [--wait 2500] [--scroll N] [--json]

History: until 2026-09-10 this was a one-off with the URL hard-coded to
localhost:3055 and white text assumed; r8 R3 could not run it at all. The
foreground colour is now read from computed style per element.
"""
from __future__ import annotations

import argparse
import io
import json
import re
import sys

DEFAULT_TARGETS = ("h1, h2, h3, header nav a, header a, section p, section a, "
                   "figcaption, .kicker, .lede")


def lum_srgb(px):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = px[:3]
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def parse_color(css: str):
    """rgb()/rgba() from computed style -> (r, g, b, a). Anything else -> None."""
    m = re.match(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:[,\s/]+([\d.]+))?", css or "")
    if not m:
        return None
    r, g, b = (float(m.group(i)) for i in (1, 2, 3))
    a = float(m.group(4)) if m.group(4) else 1.0
    return (r, g, b, a)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--selectors", default=DEFAULT_TARGETS)
    ap.add_argument("--wait", type=int, default=2500, help="ms to let media/fonts settle")
    ap.add_argument("--scroll", type=int, default=0, help="scroll px before measuring")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    try:
        from PIL import Image
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print("contrast_over_media: beroende saknas (" + str(e) + ")", file=sys.stderr)
        return 2

    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": args.width, "height": args.height},
                        device_scale_factor=1)
        try:
            pg.goto(args.url, wait_until="networkidle", timeout=45000)
        except Exception:
            pg.goto(args.url, wait_until="load", timeout=45000)
        if args.scroll:
            pg.evaluate("y => window.scrollTo(0, y)", args.scroll)
        pg.wait_for_timeout(args.wait)

        boxes = pg.evaluate("""(sel) => {
          const out = [];
          document.querySelectorAll(sel).forEach(el => {
            const r = el.getBoundingClientRect();
            if (r.width < 4 || r.height < 4 || r.top > innerHeight || r.bottom < 0) return;
            const t = (el.innerText || '').trim();
            if (!t) return;
            const cs = getComputedStyle(el);
            if (cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) return;
            out.push({t: t.slice(0, 32).replace(/\\s+/g, ' '),
                      sel: el.tagName.toLowerCase() + (el.className && typeof el.className === 'string'
                            ? '.' + el.className.trim().split(/\\s+/).join('.') : ''),
                      x: Math.max(0, r.left), y: Math.max(0, r.top),
                      w: Math.min(r.width, innerWidth - Math.max(0, r.left)),
                      h: Math.min(r.height, innerHeight - Math.max(0, r.top)),
                      color: cs.color, size: parseFloat(cs.fontSize),
                      weight: parseInt(cs.fontWeight) || 400});
          });
          return out;
        }""", args.selectors)

        # hide every text node, then plate the ground alone
        pg.add_style_tag(content="*{color:transparent!important;text-shadow:none!important;"
                                 "-webkit-text-stroke:0!important;caret-color:transparent!important}"
                                 "svg,img.logo,[data-logo]{opacity:0!important}")
        pg.wait_for_timeout(300)
        plate = Image.open(io.BytesIO(pg.screenshot())).convert("RGB")
        b.close()

    rows = []
    for bx in boxes:
        x0, y0 = int(bx["x"]), int(bx["y"])
        x1, y1 = int(bx["x"] + bx["w"]), int(bx["y"] + bx["h"])
        crop = plate.crop((x0, y0, min(x1, plate.width), min(y1, plate.height)))
        px = list(crop.getdata())
        if not px:
            continue
        col = parse_color(bx["color"])
        if not col:
            continue
        fg = lum_srgb(col)
        lums = sorted(lum_srgb(q) for q in px)
        # the text disappears against the ground closest to its own luminance
        # in the worst 5 % of the patch: brightest for dark text, darkest for light
        worst = lums[int(len(lums) * 0.95)] if fg < 0.5 else lums[int(len(lums) * 0.05)]
        mean = sum(lums) / len(lums)
        ratio_worst = (max(fg, worst) + 0.05) / (min(fg, worst) + 0.05)
        ratio_mean = (max(fg, mean) + 0.05) / (min(fg, mean) + 0.05)
        large = bx["size"] >= 24 or (bx["size"] >= 18.66 and bx["weight"] >= 700)
        floor = 3.0 if large else 4.5
        rows.append({"text": bx["t"], "sel": bx["sel"], "size_px": round(bx["size"], 1),
                     "color": bx["color"], "ratio_worst": round(ratio_worst, 2),
                     "ratio_mean": round(ratio_mean, 2), "floor": floor,
                     "pass": ratio_worst >= floor})

    out = {"url": args.url, "viewport": [args.width, args.height], "scroll": args.scroll,
           "rows": rows, "pass": all(r["pass"] for r in rows), "measured": len(rows)}
    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print("contrast_over_media " + ("PASS" if out["pass"] else "FAIL") + "  " + args.url
              + "  (%d strangar i folden)" % len(rows))
        for r in rows:
            mark = "ok  " if r["pass"] else "FAIL"
            print("  %s varsta %5.2f:1  medel %5.2f:1  (golv %.1f)  %4.0fpx  %-28s %r"
                  % (mark, r["ratio_worst"], r["ratio_mean"], r["floor"], r["size_px"],
                     r["sel"][:28], r["text"]))
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
