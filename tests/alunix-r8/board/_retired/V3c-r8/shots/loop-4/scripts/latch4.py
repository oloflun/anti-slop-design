"""latch4.py <out.json>: H-27 on the R9 state. Four ways to reach the same scrollY
(Horai act --sc-ps ~0.58): wheel 100/60, PageDown, scrollTo, smooth scrollTo; read
--rv on both wrappers 2.5 s after the last input, plus a resize-before-band run
(Astra loop 3 fix 1) and the writes-after-landing count (035 step 3)."""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
READ = """() => {
  const w = document.querySelector('.horai-wrap'), c = document.querySelector('.calyx-wrap');
  const fig = document.querySelector('.horai-fig');
  const a = (window.__scSmooth.acts||[]).filter(x => x.el === fig)[0];
  return {scrollY: window.scrollY,
    horai_rv: parseFloat(w.style.getPropertyValue('--rv')), calyx_rv: parseFloat(c.style.getPropertyValue('--rv')),
    horai_ps: parseFloat(getComputedStyle(fig).getPropertyValue('--sc-ps')), horai_cur: a ? a.cur : null,
    turning: document.querySelector('section.hero').classList.contains('is-turning'),
    backInert: document.querySelector('.face--back') ? document.querySelector('.face--back').inert : null};
}"""
COUNTER = """() => { window.__rvWrites = 0; const w = document.querySelector('.horai-wrap'); const c = document.querySelector('.calyx-wrap');
  for (const el of [w, c]) { const orig = el.style.setProperty.bind(el.style); el.style.setProperty = function(k, v){ if (k === '--rv') window.__rvWrites++; return orig(k, v); }; } }"""
def target_y(page):
    return page.evaluate("""() => { const fig = document.querySelector('.horai-fig'); const r = fig.getBoundingClientRect();
      const top = r.top + window.scrollY, h = r.height, vh = innerHeight; return Math.round(0.58*(h+vh) - vh + top); }""")
def run(pw, method, resize=False):
    b = pw.chromium.launch(executable_path=CHROME)
    page = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    page.goto(URL, wait_until="load"); page.wait_for_timeout(1500)
    if resize:
        page.evaluate("scrollTo(0, 1000)"); page.wait_for_timeout(800)
        page.set_viewport_size({"width": 1280, "height": 800}); page.wait_for_timeout(800)
    y = target_y(page)
    if method == "wheel":
        page.mouse.move(640, 400); cur = page.evaluate("scrollY")
        while cur < y:
            page.mouse.wheel(0, 100); page.wait_for_timeout(60); cur = page.evaluate("scrollY")
    elif method == "pagedown":
        page.evaluate("document.body.focus()"); cur = page.evaluate("scrollY"); n = 0
        while cur < y and n < 40:
            page.keyboard.press("PageDown"); page.wait_for_timeout(450); cur = page.evaluate("scrollY"); n += 1
    elif method == "scrollTo":
        page.evaluate("y => scrollTo(0, y)", y)
    elif method == "smooth":
        page.evaluate("y => scrollTo({top: y, behavior: 'smooth'})", y)
    page.wait_for_timeout(2500)
    r = page.evaluate(READ)
    page.evaluate(COUNTER); page.wait_for_timeout(3000)
    r["rv_writes_after_landing_3s"] = page.evaluate("window.__rvWrites")
    r.update(method=method, resize=resize, target_y=y)
    b.close(); return r
out = []
with sync_playwright() as pw:
    for m in ("wheel", "pagedown", "scrollTo", "smooth"):
        r = run(pw, m); out.append(r); print(json.dumps(r))
    r = run(pw, "wheel", resize=True); out.append(r); print(json.dumps(r))
json.dump(out, open(sys.argv[1], "w"), indent=1)
