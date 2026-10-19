"""pricefix_ab.py <out.json>: hypothesis test. .price{content-visibility:auto;
contain-intrinsic-size:auto 760px} (index.html ~731) reserves 760 px while the block is
off-screen; its real content is ~463 px at 1440 / ~450 px at 390, so the page loses
297 / 262 px the first time the block renders, and the engine's cached act tops for
#process, #principer and footer.close stay stale until a real resize.
A: as built. B: the two declarations neutralised by an injected style at load.
Read: docH at load vs in band, engine top vs real top for #process, #process --sc-p at
scrollY 4800 (1440) without any resize, and ?preview=process-01/02 at 390, 3 loads each."""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
FIX = ".price{content-visibility:visible!important;contain-intrinsic-size:none!important;}"
JS = """() => {
  const p = document.getElementById('process'); const cs = getComputedStyle(p);
  const inst = (window.ScrollCraft && window.ScrollCraft.instances && window.ScrollCraft.instances[0]) || null;
  let engTop = null; try { engTop = Math.round(inst.acts.filter(a => a.el === p)[0].top); } catch(e) {}
  const price = document.querySelector('.price').getBoundingClientRect();
  return {scrollY: scrollY, docH: document.documentElement.scrollHeight, realTop: Math.round(p.getBoundingClientRect().top + scrollY), engTop: engTop,
    procP: parseFloat(p.style.getPropertyValue('--sc-p')), ps: parseFloat(cs.getPropertyValue('--sc-ps')), priceH: Math.round(price.height),
    e1: parseFloat(cs.getPropertyValue('--e1')), e2: parseFloat(cs.getPropertyValue('--e2'))};
}"""
def page(b, w, h, fix, url=URL):
    pg = b.new_page(viewport={"width": w, "height": h})
    if fix: pg.add_init_script("addEventListener('DOMContentLoaded', () => { const s = document.createElement('style'); s.textContent = %r; document.head.appendChild(s); });" % FIX)
    pg.goto(url, wait_until="load"); pg.wait_for_timeout(2000)
    return pg
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for fix in (False, True):
        tag = "B_fix" if fix else "A_asbuilt"
        r = {}
        for w, h, y in ((1440, 900, 4800), (390, 844, 4900)):
            pg = page(b, w, h, fix)
            r[f"{w}_load"] = pg.evaluate(JS)
            pg.mouse.move(w // 2, h // 2); cur = 0
            while cur < y:
                pg.mouse.wheel(0, 100); pg.wait_for_timeout(40); cur = pg.evaluate("scrollY")
            pg.wait_for_timeout(3000)
            r[f"{w}_in_band_wheel"] = pg.evaluate(JS)
            pg.close()
        for n in (1, 2):
            for rep in range(3):
                pg = page(b, 390, 844, fix, URL + f"?preview=process-0{n}")
                pg.wait_for_timeout(1000)
                d = pg.evaluate(JS); r[f"390_preview0{n}_{rep}"] = {"ps": d["ps"], "e": d[f"e{n}"], "formed": d["ps"] >= d[f"e{n}"] - 0.0005, "engTop": d["engTop"], "realTop": d["realTop"]}
                pg.close()
        out[tag] = r
        for k, v in r.items(): print(tag, k, json.dumps(v))
    b.close()
json.dump(out, open(sys.argv[1], "w"), indent=1)
