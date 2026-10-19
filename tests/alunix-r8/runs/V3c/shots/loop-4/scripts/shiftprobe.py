"""shiftprobe.py <out.json>: which element and which property make the band 297 px
(1440) / 262 px (390) shorter once the frames are awake? Toggle content-visibility,
is-asleep and mounting at scrollY 0 and read the row."""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
READ = """() => {
  const q = s => document.querySelector(s);
  const h = s => { const e = q(s); return e ? Math.round(e.getBoundingClientRect().height) : null; };
  const cv = s => getComputedStyle(q(s)).contentVisibility;
  return {stagger: h('.stagger'), thesis: h('.panel-thesis'), calyxFig: h('.calyx-fig'), calyxWrap: h('.calyx-wrap'), giant: h('.panel-giant'), horaiFig: h('.horai-fig'), horaiWrap: h('.horai-wrap'), price: h('.price'), priceInner: h('.price > *'),
    calyxCV: cv('.calyx-wrap'), horaiCV: cv('.horai-wrap'), calyxAsleep: q('.calyx-wrap').classList.contains('is-asleep'), horaiAsleep: q('.horai-wrap').classList.contains('is-asleep'),
    horaiSrc: !!q('.horai-wrap iframe').src, calyxSrc: !!q('.calyx-wrap iframe').src,
    staggerDisplay: getComputedStyle(q('.stagger')).display, staggerRows: getComputedStyle(q('.stagger')).gridTemplateRows, staggerCols: getComputedStyle(q('.stagger')).gridTemplateColumns,
    horaiFigParent: q('.horai-fig').parentElement.className, horaiWrapMinH: getComputedStyle(q('.horai-wrap')).minHeight, calyxWrapMinH: getComputedStyle(q('.calyx-wrap')).minHeight,
    horaiIframeH: h('.horai-wrap iframe'), horaiRvH: h('.horai-wrap .rv'), horaiRvPos: getComputedStyle(q('.horai-wrap .rv')).position, horaiIframePos: getComputedStyle(q('.horai-wrap iframe')).position};
}"""
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for w, hgt in ((1440, 900), (390, 844)):
        pg = b.new_page(viewport={"width": w, "height": hgt})
        pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2500)
        r = {}
        r["load"] = pg.evaluate(READ)
        pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.style.contentVisibility = 'visible')"); pg.wait_for_timeout(300)
        r["cv_visible_unmounted"] = pg.evaluate(READ)
        pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.style.contentVisibility = '')"); pg.wait_for_timeout(300)
        pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.classList.add('is-asleep'))"); pg.wait_for_timeout(300)
        r["asleep_unmounted"] = pg.evaluate(READ)
        pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.classList.remove('is-asleep'))"); pg.wait_for_timeout(300)
        pg.evaluate("document.querySelectorAll('iframe[data-src]').forEach(f => { if (!f.src) f.src = f.getAttribute('data-src'); })"); pg.wait_for_timeout(4000)
        r["mounted_scrollY0"] = pg.evaluate(READ)
        pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.style.contentVisibility = 'visible')"); pg.wait_for_timeout(500)
        r["mounted_cv_visible"] = pg.evaluate(READ)
        pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.style.contentVisibility = '')"); pg.wait_for_timeout(300)
        pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.classList.add('is-asleep'))"); pg.wait_for_timeout(500)
        r["mounted_asleep"] = pg.evaluate(READ)
        pg.evaluate("document.querySelectorAll('.frame-wrap').forEach(w => w.classList.remove('is-asleep'))"); pg.wait_for_timeout(300)
        pg.evaluate("scrollTo(0, document.querySelector('.horai-fig').getBoundingClientRect().top + scrollY - 200)"); pg.wait_for_timeout(3000)
        r["mounted_in_band"] = pg.evaluate(READ)
        out[str(w)] = r
        for k, v in r.items():
            print(w, k, json.dumps({kk: vv for kk, vv in v.items() if kk in ('stagger', 'calyxFig', 'calyxWrap', 'horaiFig', 'horaiWrap', 'price', 'priceInner', 'calyxCV', 'horaiCV', 'calyxAsleep', 'horaiAsleep', 'horaiSrc', 'horaiIframeH', 'horaiRvH')}))
        print(w, "static:", json.dumps({kk: vv for kk, vv in r["load"].items() if kk in ('staggerDisplay', 'staggerRows', 'staggerCols', 'horaiFigParent', 'horaiWrapMinH', 'calyxWrapMinH', 'horaiRvPos', 'horaiIframePos')}))
        pg.close()
    b.close()
json.dump(out, open(sys.argv[1], "w"), indent=1)
