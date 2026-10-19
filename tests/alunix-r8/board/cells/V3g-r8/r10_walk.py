#!/usr/bin/env python3
"""R10 wheel walk: real mouse.wheel through one page region, both directions, frames to disk.

    python tests/alunix-r8/browser_lock.py -- python r10_walk.py URL OUT W H FROM TO [--notch 100] [--every 2] [--sheet]

FROM / TO: CSS selectors (the walk starts with FROM's top at the viewport top and ends when
TO's top reaches the viewport top), or plain numbers (scrollY). The walk goes down and then
back up over the same range with the same notch, capturing a frame every `--every` notches
after the scroll has settled (Lenis at rest). Writes down-NN.png / up-NN.png plus a JSON log
of scrollY per frame, and with --sheet a contact sheet per direction.
Headless only; the browser always closes.
"""
import json, os, sys, time
from playwright.sync_api import sync_playwright

URL, OUT, W, H, FROM, TO = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
def opt(name, d):
    return type(d)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else d
NOTCH, EVERY, SHEET = opt("--notch", 100), opt("--every", 2), "--sheet" in sys.argv
os.makedirs(OUT, exist_ok=True)

Y_OF = """(s)=>{ if(/^-?\\d+(\\.\\d+)?$/.test(s)) return +s;
  if(s.startsWith('js:')) return Math.round(eval(s.slice(3)));
  const el=document.querySelector(s); if(!el) return null;
  return Math.round(el.getBoundingClientRect().top + scrollY); }"""
SETTLE = """async ()=>{ const L=window.__lenis; let still=0, last=-1;
  for(let i=0;i<240 && still<6;i++){ await new Promise(r=>requestAnimationFrame(r));
    const y=L?L.animatedScroll:scrollY; still = (Math.abs(y-last)<0.3 && !(L&&L.isScrolling)) ? still+1 : 0; last=y; }
  return scrollY; }"""


def sheet(paths, out, cols=6):
    from PIL import Image
    ims = [Image.open(p) for p in paths]
    if not ims:
        return
    tw = 300
    th = int(ims[0].height * tw / ims[0].width)
    rows = (len(ims) + cols - 1) // cols
    S = Image.new("RGB", (cols * tw + (cols - 1) * 4, rows * th + (rows - 1) * 4), (230, 0, 60))
    for i, im in enumerate(ims):
        S.paste(im.convert("RGB").resize((tw, th)), ((i % cols) * (tw + 4), (i // cols) * (th + 4)))
    S.save(out)


with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    try:
        pg = b.new_page(viewport={"width": W, "height": H})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.goto(URL, wait_until="load")
        pg.wait_for_timeout(1800)
        y0, y1 = pg.evaluate(Y_OF, FROM), pg.evaluate(Y_OF, TO)
        if y0 is None or y1 is None:
            sys.exit(f"selector not found: {FROM} -> {y0}, {TO} -> {y1}")
        y0 = max(0, y0 - (48 if not (FROM.lstrip('-').isdigit() or FROM.startswith('js:')) else 0))
        if TO.startswith('js:'):
            y1 += 48  # the walk stops 48 px before TO for selectors (topline); expressions are exact
        pg.evaluate("(y)=>window.__lenis.scrollTo(y,{immediate:true,force:true})", y0)
        pg.wait_for_timeout(900)
        pg.evaluate(SETTLE)
        pg.mouse.move(W * 0.5, H * 0.6)
        log = {"down": [], "up": [], "from": y0, "to": y1, "errors": errs}
        for direction, sign in (("down", 1), ("up", -1)):
            n, k, paths = 0, 0, []
            guard = 0
            while guard < 2000:
                guard += 1
                y = pg.evaluate("scrollY")
                if sign > 0 and y >= y1 - 48:
                    break
                if sign < 0 and y <= y0 + 2:
                    break
                pg.mouse.wheel(0, sign * NOTCH)
                pg.wait_for_timeout(16)
                n += 1
                if n % EVERY == 0:
                    y = pg.evaluate(SETTLE)
                    path = os.path.join(OUT, f"{direction}-{k:03d}.png")
                    pg.screenshot(path=path)
                    paths.append(path)
                    log[direction].append({"i": k, "y": y})
                    k += 1
            if SHEET:
                sheet(paths, os.path.join(OUT, f"sheet-{direction}.png"))
        json.dump(log, open(os.path.join(OUT, "walk.json"), "w"), indent=1)
        print(json.dumps({"from": y0, "to": y1, "down": len(log["down"]), "up": len(log["up"]), "errors": errs[:5]}))
    finally:
        b.close()
