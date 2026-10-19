"""latch_diag.py: is plan 031's --rv latch path dependent, and why?

Four ways to reach the same scrollY (Horai act --sc-ps ~ 0.58): wheel 100 px / 60 ms,
PageDown, scrollTo (instant), scrollTo smooth (scrollbar-like: many events).
Per frame we log scrollY, the shim's lerped cur for .horai-fig, the inline --rv on
.horai-wrap, and the raw --sc-p, for 2.5 s after the last input. Then the same four
with an in-page emulation of the proposed fix (a rAF loop that samples the shim's
cur every frame while any reveal < 1 and its act is still lerping).
"""
import json, sys, time
from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUT = sys.argv[2] if len(sys.argv) > 2 else "latch_diag.json"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"

LOGGER = """
() => {
  window.__log = [];
  const w = document.querySelector('.horai-wrap');
  const c = document.querySelector('.calyx-wrap');
  const fig = document.querySelector('.horai-fig');
  const act = () => (window.__scSmooth.acts||[]).filter(a => a.el === fig)[0];
  const t0 = performance.now();
  function f(){
    const a = act();
    window.__log.push([Math.round(performance.now()-t0), window.scrollY,
      a ? +a.cur.toFixed(4) : null,
      parseFloat(fig.style.getPropertyValue('--sc-p')),
      parseFloat(w.style.getPropertyValue('--rv')),
      parseFloat(c.style.getPropertyValue('--rv'))]);
    window.__logRaf = requestAnimationFrame(f);
  }
  f();
}
"""

# Emulation of the proposed fix: sample the shim's lerped value every frame while a
# reveal is unfinished and its act is still moving toward its target.
FIX = """
() => {
  const R = [
    {el: document.querySelector('.calyx-wrap'), fig: document.querySelector('.calyx-fig'), from:0.02, to:0.30, v:0},
    {el: document.querySelector('.horai-wrap'), fig: document.querySelector('.horai-fig'), from:0.10, to:0.55, v:0}
  ];
  R.forEach(r => r.el.style.setProperty('--rv','0'));
  let raf = null;
  function tick(){
    raf = null; let again = false;
    for (const r of R){
      const a = (window.__scSmooth.acts||[]).filter(x => x.el === r.fig)[0];
      if (!a || isNaN(a.cur)) { again = true; continue; }
      let t = Math.min(1, Math.max(0, (a.cur - r.from)/(r.to - r.from)));
      t = t*t*(3-2*t);
      if (t > r.v + 0.002){ r.v = t; r.el.style.setProperty('--rv', t.toFixed(4)); }
      const target = parseFloat(a.el.style.getPropertyValue('--sc-p'));
      if (r.v < 1 && !isNaN(target) && Math.abs(target - a.cur) > 0.0005) again = true;
    }
    if (again) raf = requestAnimationFrame(tick);
  }
  function kick(){ if (!raf) raf = requestAnimationFrame(tick); }
  addEventListener('scroll', kick, {passive:true});
  kick();
  window.__fixOn = true;
}
"""

def settle(page, ms=2500):
    page.wait_for_timeout(ms)

def read(page):
    return page.evaluate("""() => {
      const w = document.querySelector('.horai-wrap'), c = document.querySelector('.calyx-wrap');
      const fig = document.querySelector('.horai-fig');
      const a = (window.__scSmooth.acts||[]).filter(x => x.el === fig)[0];
      return {scrollY: window.scrollY,
        horai_rv: parseFloat(w.style.getPropertyValue('--rv')),
        calyx_rv: parseFloat(c.style.getPropertyValue('--rv')),
        horai_ps: parseFloat(getComputedStyle(fig).getPropertyValue('--sc-ps')),
        horai_p: parseFloat(fig.style.getPropertyValue('--sc-p')),
        horai_cur: a ? a.cur : null,
        clip: getComputedStyle(w).clipPath};
    }""")

def target_y(page):
    # scrollY where .horai-fig raw p = 0.58 (flow: (y + vh - top)/(h + vh))
    return page.evaluate("""() => {
      const fig = document.querySelector('.horai-fig'); const r = fig.getBoundingClientRect();
      const top = r.top + window.scrollY, h = r.height, vh = innerHeight;
      return Math.round(0.58*(h+vh) - vh + top);
    }""")

def run(pw, method, fix):
    b = pw.chromium.launch(executable_path=CHROME, headless=True)
    ctx = b.new_context(viewport={"width":1440,"height":900}, device_scale_factor=1)
    page = ctx.new_page()
    page.goto(URL, wait_until="load"); page.wait_for_timeout(1500)
    if fix: page.evaluate(FIX)
    y = target_y(page)
    page.evaluate(LOGGER)
    if method == "wheel":
        page.mouse.move(720, 450)
        cur = 0
        while cur < y:
            page.mouse.wheel(0, 100); page.wait_for_timeout(60)
            cur = page.evaluate("window.scrollY")
    elif method == "pagedown":
        page.evaluate("document.body.focus()")
        cur = 0; n = 0
        while cur < y and n < 40:
            page.keyboard.press("PageDown"); page.wait_for_timeout(450)
            cur = page.evaluate("window.scrollY"); n += 1
    elif method == "scrollTo":
        page.evaluate("y => window.scrollTo(0, y)", y)
    elif method == "smooth":
        page.evaluate("y => window.scrollTo({top:y, behavior:'smooth'})", y)
    settle(page)
    res = read(page)
    log = page.evaluate("window.__log")
    # number of frames in which --rv changed, and the last frame index where it changed
    changes = [i for i in range(1, len(log)) if log[i][4] != log[i-1][4]]
    res.update(method=method, fix=fix, target_y=y, frames=len(log),
               rv_change_frames=len(changes),
               last_rv_change_frame=(changes[-1] if changes else None),
               last_cur_move_frame=max([i for i in range(1,len(log)) if log[i][2] != log[i-1][2]] or [None]),
               tail=log[-3:], head=log[:3])
    b.close()
    return res

out = []
with sync_playwright() as pw:
    for fix in (False, True):
        for m in ("wheel", "pagedown", "scrollTo", "smooth"):
            r = run(pw, m, fix); out.append(r)
            print(json.dumps({k: r[k] for k in ("method","fix","target_y","scrollY","horai_ps","horai_cur","horai_rv","calyx_rv","rv_change_frames","last_rv_change_frame","last_cur_move_frame","frames")}))
            sys.stdout.flush()
json.dump(out, open(OUT, "w"), indent=1)
