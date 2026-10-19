# Load-phase check at a given CPU rate: iframe loads, ST refreshes, page errors, showcase-stage visibility at scrollY 0. Headless GPU.
import sys, json
from playwright.sync_api import sync_playwright
url, cpu, w, h = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
INIT = r"""
window.__lc = {ev:[], vis:[]};
document.addEventListener('DOMContentLoaded', () => {
  __lc.ev.push(['dcl','',Math.round(performance.now())]);
  document.querySelectorAll('iframe').forEach(f => f.addEventListener('load', () => __lc.ev.push(['load', f.id, Math.round(performance.now())])));
  const hook = () => window.ScrollTrigger ? (ScrollTrigger.addEventListener('refresh', () => __lc.ev.push(['refresh','',Math.round(performance.now())])), ScrollTrigger.addEventListener('refreshInit', () => __lc.ev.push(['refreshInit','',Math.round(performance.now())]))) : setTimeout(hook, 20);
  hook();
  (function L(){ const s=document.querySelector('.showcase-stage'); if(s){const r=s.getBoundingClientRect(); if(r.top<innerHeight && r.bottom>0 && scrollY<10) __lc.vis.push([Math.round(performance.now()), Math.round(r.top), Math.round(r.height), getComputedStyle(s).position]);} if(performance.now()<30000) requestAnimationFrame(L); })();
});
"""
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, channel="chromium", args=["--enable-gpu","--ignore-gpu-blocklist","--use-angle=d3d11"])
    try:
        ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg = ctx.new_page(); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
        pg.on("console", lambda m: m.type in ("error","warning") and errs.append(m.type+": "+m.text[:160]))
        if cpu > 1: ctx.new_cdp_session(pg).send("Emulation.setCPUThrottlingRate", {"rate": cpu})
        pg.add_init_script(INIT)
        pg.goto(url, wait_until="load", timeout=90000); pg.wait_for_timeout(8000)
        r = pg.evaluate("__lc")
        r["calyx_y"] = pg.evaluate("window.__CASES && window.__CASES.calyx.y")
        r["iframes"] = pg.evaluate("[...document.querySelectorAll('iframe')].map(f=>[f.id,f.getAttribute('src'),getComputedStyle(f).opacity])")
    finally:
        b.close()
vis = r.pop("vis")
r["showcase_visible_frames_at_top"] = len(vis); r["vis_sample"] = vis[:6]; r["errors"] = errs[:12]
print(json.dumps(r, indent=1))
