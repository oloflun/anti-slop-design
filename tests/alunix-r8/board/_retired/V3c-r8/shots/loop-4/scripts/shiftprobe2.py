"""shiftprobe2.py: children heights of .price, .horai-wrap, .col-left, .col-right at
scrollY 0 (mounted) vs in the band, 1440; and which single --sc-ps / --rv toggle at
scrollY 0 reproduces the shrink."""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
READ = """() => {
  const q = s => document.querySelector(s);
  const kids = s => [...q(s).children].map(c => [c.tagName.toLowerCase() + (c.className ? '.' + String(c.className).split(' ').join('.') : ''), Math.round(c.getBoundingClientRect().height), getComputedStyle(c).position]);
  const h = s => Math.round(q(s).getBoundingClientRect().height);
  return {stagger: h('.stagger'), colL: h('.col-left'), colR: h('.col-right'), price: h('.price'), priceKids: kids('.price'), horaiWrap: h('.horai-wrap'), horaiWrapKids: kids('.horai-wrap'), horaiFig: h('.horai-fig'), horaiFigKids: kids('.horai-fig'),
    colLkids: kids('.col-left'), colRkids: kids('.col-right'),
    priceCS: (c => ({minH: c.minHeight, h: c.height, flex: c.flex, alignSelf: c.alignSelf}))(getComputedStyle(q('.price'))),
    horaiFigCS: (c => ({minH: c.minHeight, h: c.height, flex: c.flex}))(getComputedStyle(q('.horai-fig'))),
    ps: {thesis: getComputedStyle(q('.panel-thesis')).getPropertyValue('--sc-ps'), giant: getComputedStyle(q('#giant-section')).getPropertyValue('--sc-ps'), price: getComputedStyle(q('.price')).getPropertyValue('--sc-ps'), horai: getComputedStyle(q('.horai-fig')).getPropertyValue('--sc-ps')},
    rv: [q('.calyx-wrap').style.getPropertyValue('--rv'), q('.horai-wrap').style.getPropertyValue('--rv')]};
}"""
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2500)
    pg.evaluate("document.querySelectorAll('iframe[data-src]').forEach(f => { if (!f.src) f.src = f.getAttribute('data-src'); })"); pg.wait_for_timeout(4000)
    out["mounted_y0"] = pg.evaluate(READ)
    # toggle candidates at scrollY 0
    pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.style.setProperty('--rv', '1'))"); pg.wait_for_timeout(400)
    out["rv1_y0"] = pg.evaluate(READ)
    pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.style.setProperty('--rv', '0'))"); pg.wait_for_timeout(400)
    pg.evaluate("['.panel-thesis','#giant-section','.price','.horai-fig','.calyx-fig'].forEach(s => document.querySelector(s).style.setProperty('--sc-ps', '0.6'))"); pg.wait_for_timeout(400)
    out["ps06_y0"] = pg.evaluate(READ)
    pg.evaluate("['.panel-thesis','#giant-section','.price','.horai-fig','.calyx-fig'].forEach(s => document.querySelector(s).style.removeProperty('--sc-ps'))"); pg.wait_for_timeout(400)
    pg.evaluate("scrollTo(0, 4800)"); pg.wait_for_timeout(3000)
    out["in_band"] = pg.evaluate(READ)
    pg.evaluate("scrollTo(0, 0)"); pg.wait_for_timeout(3000)
    out["back_to_y0"] = pg.evaluate(READ)
    b.close()
for k, v in out.items():
    print(k, "stagger", v["stagger"], "colL", v["colL"], "colR", v["colR"], "price", v["price"], "horaiWrap", v["horaiWrap"], "ps", v["ps"], "rv", v["rv"])
    print("   priceKids", v["priceKids"]); print("   horaiWrapKids", v["horaiWrapKids"]); print("   horaiFigKids", v["horaiFigKids"]); print("   colL", v["colLkids"]); print("   colR", v["colRkids"]); print("   priceCS", v["priceCS"], "horaiFigCS", v["horaiFigCS"])
json.dump(out, open(sys.argv[1], "w"), indent=1)
