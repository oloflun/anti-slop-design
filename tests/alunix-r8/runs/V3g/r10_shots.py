#!/usr/bin/env python3
"""R10 stills: jump to named scroll positions (Lenis, immediate) and screenshot each, plus a probe.

    python tests/alunix-r8/browser_lock.py -- python r10_shots.py URL OUT W H name=JSEXPR [name=JSEXPR ...] [--roundtrip]

JSEXPR is evaluated in the page and must give a scrollY (e.g. `0`, `__R10.t1.end`,
`document.querySelector('#pris').getBoundingClientRect().top+scrollY-48`).
--roundtrip: before the shots, wheel down past the hero (40 notches) and back up to 0, then
report the hero's state (the R9 check: clipPath inset(0%), whole h1 lines).
Headless only; the browser always closes.
"""
import json, os, sys
from playwright.sync_api import sync_playwright

URL, OUT, W, H = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
SPECS = [a.split("=", 1) for a in sys.argv[5:] if "=" in a and not a.startswith("--")]
os.makedirs(OUT, exist_ok=True)
SETTLE = """async ()=>{ const L=window.__lenis; let still=0, last=-1;
  for(let i=0;i<300 && still<8;i++){ await new Promise(r=>requestAnimationFrame(r));
    const y=L?L.animatedScroll:scrollY; still = (Math.abs(y-last)<0.3 && !(L&&L.isScrolling)) ? still+1 : 0; last=y; }
  return scrollY; }"""
HERO = """()=>{ const nh=document.querySelector('.hero-nh'); const cs=getComputedStyle(nh);
  const lines=[...document.querySelectorAll('.hero-h1 > div > div, .hero-offer > div > div')].map(l=>{
    const r=l.getBoundingClientRect(), m=l.parentElement.getBoundingClientRect();
    return {text:l.textContent.trim(), visible:+((Math.min(r.bottom,m.bottom)-Math.max(r.top,m.top))/r.height).toFixed(3)}; });
  return {scrollY, nhClip: cs.clipPath, nhTop: Math.round(nh.getBoundingClientRect().top), lines}; }"""

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    try:
        pg = b.new_page(viewport={"width": W, "height": H})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.goto(URL, wait_until="load")
        pg.wait_for_timeout(2000)
        out = {"errors": errs, "shots": {}}
        if "--roundtrip" in sys.argv:
            pg.mouse.move(W / 2, H / 2)
            for _ in range(40):
                pg.mouse.wheel(0, 100); pg.wait_for_timeout(30)
            pg.evaluate(SETTLE)
            for _ in range(60):
                pg.mouse.wheel(0, -100); pg.wait_for_timeout(30)
            pg.evaluate(SETTLE)
            pg.wait_for_timeout(400)
            out["hero_after_roundtrip"] = pg.evaluate(HERO)
            pg.screenshot(path=os.path.join(OUT, "hero-roundtrip.png"))
        for name, expr in SPECS:
            y = pg.evaluate(f"()=>Math.round({expr})")
            pg.evaluate("(y)=>window.__lenis.scrollTo(y,{immediate:true,force:true})", y)
            pg.wait_for_timeout(250)
            pg.evaluate(SETTLE)
            pg.wait_for_timeout(250)
            pg.screenshot(path=os.path.join(OUT, f"{name}.png"))
            out["shots"][name] = y
        json.dump(out, open(os.path.join(OUT, "shots.json"), "w"), indent=1)
        print(json.dumps(out, indent=1)[:3000])
    finally:
        b.close()
