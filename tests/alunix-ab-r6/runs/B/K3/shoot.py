# ponytail: one script, all captures. python shoot.py [round]
import sys, os, json
from playwright.sync_api import sync_playwright
URL = "http://127.0.0.1:3103/tests/alunix-ab-r6/runs/B/K3/index.html"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shots")
os.makedirs(OUT, exist_ok=True)
rnd = sys.argv[1] if len(sys.argv) > 1 else "r1"
def P(n): return os.path.join(OUT, f"{rnd}-{n}.png")

OVERFLOW_JS = """() => { const w = document.documentElement.clientWidth; const bad=[];
  for (const el of document.querySelectorAll('body *')) { const r = el.getBoundingClientRect(); if (r.width && (r.right > w + 1 || r.left < -1)) bad.push(el.tagName.toLowerCase()+(el.id?'#'+el.id:'')+(el.className&&typeof el.className==='string'?'.'+el.className.split(' ')[0]:'')+' '+Math.round(r.left)+'..'+Math.round(r.right)); }
  return {w, sw: document.documentElement.scrollWidth, bad: bad.slice(0,12)}; }"""

with sync_playwright() as pw:
    b = pw.chromium.launch()
    logs = []
    def ctx(w, h, reduced=False):
        c = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1, reduced_motion="reduce" if reduced else "no-preference")
        pg = c.new_page()
        pg.on("console", lambda m: logs.append(f"[{m.type}] {m.text}") if m.type in ("error","warning") else None)
        pg.on("pageerror", lambda e: logs.append(f"[pageerror] {e}"))
        return c, pg

    # 1440 fold + step-through + full
    c, pg = ctx(1440, 900)
    pg.goto(URL); pg.wait_for_timeout(2500)
    pg.screenshot(path=P("1440-fold"))
    total = pg.evaluate("document.documentElement.scrollHeight")
    y = 0
    while y < total:
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(60); y += 300
        total = pg.evaluate("document.documentElement.scrollHeight")
    pg.wait_for_timeout(600)
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(400)
    pg.screenshot(path=P("1440-full"), full_page=True)
    print("1440 height", total, "overflow", pg.evaluate(OVERFLOW_JS))
    # frame titles
    titles = pg.evaluate("Array.from(document.querySelectorAll('iframe')).map(f=>[f.title, f.contentDocument && f.contentDocument.title])")
    print("frames", titles)
    # mid-scene frames via preview hook
    for f in ("0.15", "0.5", "0.85"):
        pg.goto(URL + "?preview=" + f); pg.wait_for_timeout(2500)
        pg.screenshot(path=P(f"1440-scene-{f}"))
        print("scene", f, pg.evaluate("[scrollY, document.querySelector('#c-sec').textContent, document.querySelector('#c-pct').textContent]"))
    # after release: chip state
    pg.goto(URL + "?preview=1"); pg.wait_for_timeout(2000)
    pg.evaluate("window.scrollBy(0, innerHeight*0.3)"); pg.wait_for_timeout(900)
    pg.screenshot(path=P("1440-release"))
    print("release", pg.evaluate("[scrollY, document.querySelector('#chip').className, document.querySelector('#chip-sec').textContent]"))
    c.close()

    # 390 full page
    c, pg = ctx(390, 844)
    pg.goto(URL); pg.wait_for_timeout(2500)
    pg.screenshot(path=P("390-fold"))
    total = pg.evaluate("document.documentElement.scrollHeight"); y = 0
    while y < total:
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(50); y += 300
        total = pg.evaluate("document.documentElement.scrollHeight")
    pg.wait_for_timeout(500); pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300)
    pg.screenshot(path=P("390-full"), full_page=True)
    print("390 height", total)
    c.close()

    # overflow sweep
    for w in (320, 390, 768, 1440):
        for red in (False, True):
            c, pg = ctx(w, 800, red)
            pg.goto(URL); pg.wait_for_timeout(1500)
            r1 = pg.evaluate(OVERFLOW_JS)
            pg.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)"); pg.wait_for_timeout(600)
            r2 = pg.evaluate(OVERFLOW_JS)
            print("overflow", w, "reduced" if red else "motion", r1["sw"], r1["bad"], r2["bad"])
            c.close()

    # reduced motion, full page
    c, pg = ctx(1440, 900, True)
    pg.goto(URL); pg.wait_for_timeout(2000)
    pg.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)"); pg.wait_for_timeout(600)
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300)
    pg.screenshot(path=P("1440-reduced-full"), full_page=True)
    hidden = pg.evaluate("Array.from(document.querySelectorAll('[data-reveal],[data-clip],[data-line]')).filter(e=>getComputedStyle(e).opacity!=='1').length")
    print("reduced: un-revealed", hidden, "height", pg.evaluate("document.documentElement.scrollHeight"))
    c.close()

    # JS disabled
    c = b.new_context(viewport={"width": 1440, "height": 900}, java_script_enabled=False)
    pg = c.new_page(); pg.goto(URL); pg.wait_for_timeout(1500)
    hidden = pg.evaluate("Array.from(document.querySelectorAll('[data-reveal],[data-clip],[data-line]')).filter(e=>getComputedStyle(e).opacity!=='1').length")
    print("nojs: un-revealed", hidden, "height", pg.evaluate("document.documentElement.scrollHeight"))
    c.close()
    b.close()
    print("CONSOLE:", "\n".join(logs) if logs else "clean")
