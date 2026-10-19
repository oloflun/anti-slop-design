"""p01check.py: ?preview=process-01 at 390, eight loads. Is the one load that settled at
ps 0.2400 instead of 0.2451 (k1 0.971) visible as an unclosed contour?"""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html?preview=process-01"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
JS = """() => {
  const p = document.getElementById('process'); const cs = getComputedStyle(p);
  const off = id => { const e = document.getElementById(id); return e ? getComputedStyle(e).strokeDashoffset : null; };
  return {ps: parseFloat(cs.getPropertyValue('--sc-ps')), e1: parseFloat(cs.getPropertyValue('--e1')),
    k1: parseFloat(cs.getPropertyValue('--k1')), outline: off('p-outline'), glyph: off('p-glyph')};
}"""
rows = []
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for i in range(8):
        pg = b.new_page(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
        pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2500)
        r = pg.evaluate(JS); rows.append(r); print(i, r)
        if r["ps"] < r["e1"] - 0.0005: pg.screenshot(path=sys.argv[1] + f"/p01-short-{i}.png")
        pg.close()
    b.close()
json.dump(rows, open(sys.argv[1] + "/p01check.json", "w"), indent=1)
short = [r for r in rows if r["ps"] < r["e1"] - 0.0005]
print("short:", len(short), "of", len(rows))
