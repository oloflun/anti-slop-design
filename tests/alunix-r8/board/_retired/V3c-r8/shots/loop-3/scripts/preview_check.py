"""preview_check.py: does ?preview=process-0N land on --eN after load and fonts? Reads --kN,
--sN/--eN, #process --sc-ps and the dash offsets of the step's paths, at 1440 and 390,
right after load and again 2 s later (fonts/relayout)."""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
JS = """(n) => {
  const p = document.getElementById('process'); const cs = getComputedStyle(p);
  const g = k => cs.getPropertyValue(k).trim();
  const off = id => { const e = document.getElementById(id); return e ? getComputedStyle(e).strokeDashoffset : null; };
  const li = document.querySelectorAll('.process-steps li')[n-1]; const r = li.getBoundingClientRect();
  return {scrollY: scrollY, ps: g('--sc-ps'), k: g('--k'+n), s: g('--s'+n), e: g('--e'+n),
    liTop: Math.round(r.top), liCenter: Math.round(r.top + r.height/2), vh: innerHeight,
    outline: off('p-outline'), glyph: off('p-glyph'), guides: off('p-guides'), dimw: off('p-dim-width'), stations: off('p-stations'),
    ids: [...p.querySelectorAll('.process-sheet [id]')].map(e => e.id).join(','),
    on: [...p.querySelectorAll('g[data-step][data-on]')].map(e => e.getAttribute('data-step')).join(',')};
}"""
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for w, h in ((1440, 900), (390, 844)):
        for n in (1, 2):
            pg = b.new_page(viewport={"width": w, "height": h}, reduced_motion="reduce")
            pg.goto(f"{URL}?preview=process-0{n}", wait_until="load")
            a = pg.evaluate(JS, n); pg.wait_for_timeout(2000); c = pg.evaluate(JS, n)
            out[f"{w}-0{n}"] = {"at_load": a, "after_2s": c}
            print(w, n, "load:", {k: a[k] for k in ("scrollY","ps","k","s","e","liCenter","vh","outline","glyph")})
            print(w, n, "2s:  ", {k: c[k] for k in ("scrollY","ps","k","s","e","liCenter","vh","outline","glyph","dimw","stations","on")})
            if n == 1: print("   ids:", c["ids"])
            pg.close()
    b.close()
json.dump(out, open(sys.argv[1], "w"), indent=1)
