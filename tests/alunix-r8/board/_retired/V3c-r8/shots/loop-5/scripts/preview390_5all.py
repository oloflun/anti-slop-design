"""preview390.py <out.json>: is ?preview=process-01/02 at 390 a race or a floor? Each mode
loaded 3 times; --sc-ps vs --eN read at 1, 2, 4 and 8 s after load, plus the engine's own
cached top for #process against the real one. Also the #process top at scrollY 5400 (1440)
for the s05/s06 seam question."""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
JS = """(n) => {
  const p = document.getElementById('process'); const cs = getComputedStyle(p);
  const g = k => parseFloat(cs.getPropertyValue(k));
  const inst = (window.ScrollCraft && window.ScrollCraft.instances && window.ScrollCraft.instances[0]) || null;
  let engTop = null; try { const a = inst.acts.filter(a => a.el === p)[0]; engTop = a ? Math.round(a.top) : null; } catch(e) {}
  return {scrollY: scrollY, ps: g('--sc-ps'), p: parseFloat(p.style.getPropertyValue('--sc-p')), e: g('--e'+n), s: g('--s'+n),
    realTop: Math.round(p.getBoundingClientRect().top + scrollY), engTop: engTop, docH: document.documentElement.scrollHeight};
}"""
out = {"previews": [], "seam": None}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for n in (1, 2, 3, 4, 5, 6, 7):
        for rep in range(3):
            pg = b.new_page(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
            pg.goto(f"{URL}?preview=process-0{n}", wait_until="load")
            row = {"n": n, "rep": rep}
            t = 0
            for wait in (1000, 1000, 2000, 4000):
                pg.wait_for_timeout(wait); t += wait
                r = pg.evaluate(JS, n); row[f"t{t}"] = r
            out["previews"].append(row)
            print(n, rep, {k: (v["ps"], v["e"], v["scrollY"], v["realTop"], v["engTop"]) for k, v in row.items() if k.startswith("t")})
            pg.close()
    pg = b.new_page(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(1500)
    pg.evaluate("scrollTo(0, 5400)"); pg.wait_for_timeout(3000)
    out["seam"] = pg.evaluate("""() => { const b = s => { const r = document.querySelector(s).getBoundingClientRect(); return {top: Math.round(r.top + scrollY), bottom: Math.round(r.bottom + scrollY), h: Math.round(r.height)}; };
      return {stagger: b('.stagger'), price: b('.price'), priceInner: b('.price > *'), horai: b('.horai-fig'), horaiWrap: b('.horai-wrap'), process: b('#process'), kicker: b('#process .kicker, #process [class*=kick]'), docH: document.documentElement.scrollHeight,
        priceBg: getComputedStyle(document.querySelector('.price')).backgroundColor, staggerBg: getComputedStyle(document.querySelector('.stagger')).backgroundColor, canvas: getComputedStyle(document.querySelector('.ground')).getPropertyValue('--sc-canvas')}; }""")
    print("seam", json.dumps(out["seam"]))
    pg.close(); b.close()
json.dump(out, open(sys.argv[1], "w"), indent=1)
