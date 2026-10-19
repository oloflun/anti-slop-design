"""walkproc5.py <out.json>: the gap R10 named and Astra repeated - the 1440 process walk in
BOTH directions. Wheel down through #process in 100 px ticks, then wheel back up, reading
--sc-ps, the --kN of every step and the four drawn paths' stroke-dashoffset at each tick.
The question H-30 asks: does every step own a window and reach its formed state, and is the
sequence the same going up as going down (no step that only forms downward)?"""
import json, sys
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
READ = """() => {
  const p = document.getElementById('process'); const cs = getComputedStyle(p);
  const num = k => parseFloat(cs.getPropertyValue(k));
  const off = id => { const e = document.getElementById(id); return e ? parseFloat(getComputedStyle(e).strokeDashoffset) : null; };
  const k = {}; for (let i = 1; i <= 7; i++) k[i] = num('--k' + i);
  return {y: Math.round(scrollY), ps: num('--sc-ps'),
    k: k, on: [...p.querySelectorAll('g[data-step][data-on]')].map(e => e.getAttribute('data-step')).sort().join(','),
    paths: {outline: off('p-outline'), glyph: off('p-glyph'), dimw: off('p-dim-width'), stations: off('p-stations')}};
}"""
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(1500)
    pg.evaluate("scrollTo(0, 4400)"); pg.wait_for_timeout(2500)
    pg.mouse.move(720, 450)
    for label, sign, ticks in (("down", 1, 50), ("up", -1, 50)):
        rows = []
        for i in range(ticks):
            pg.mouse.wheel(0, 100 * sign); pg.wait_for_timeout(70)
            rows.append(pg.evaluate(READ))
        pg.wait_for_timeout(1500)
        rows.append(pg.evaluate(READ))
        out[label] = rows
        # per step: did kN reach 1, and was the order monotone?
        maxk = {n: max(r["k"][str(n)] if str(n) in r["k"] else r["k"][n] for r in rows) for n in range(1, 8)}
        print(label, "y", rows[0]["y"], "to", rows[-1]["y"],
              "| kN max:", {n: round(v, 3) for n, v in maxk.items()},
              "| paths at end:", rows[-1]["paths"], "| on:", rows[-1]["on"])
    b.close()
json.dump(out, open(sys.argv[1], "w"), indent=1)
