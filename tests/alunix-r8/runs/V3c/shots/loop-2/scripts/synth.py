"""synth.py: cost of ONE custom-property write, isolated. No scrolling. For each target
element and property, write 120 distinct values one per rAF and read the CDP
RecalcStyleDuration / RecalcStyleCount delta (cpu 1 = raw machine time)."""
import json, sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CTRL = "http://localhost:3090/tests/motion/smooth.html"

WRITE = """([sel, prop, n]) => new Promise(res => {
  const el = sel === ':root' ? document.documentElement : document.querySelector(sel);
  let i = 0; const t0 = performance.now();
  const step = () => {
    el.style.setProperty(prop, (0.1 + (i % 50) * 0.01).toFixed(4));
    // force style resolution this frame
    void getComputedStyle(el).opacity;
    if (++i < n) requestAnimationFrame(step); else res(performance.now() - t0);
  };
  requestAnimationFrame(step);
})"""

def metrics(cdp):
    return {x["name"]: x["value"] for x in cdp.send("Performance.getMetrics")["metrics"]}

def main():
    with sync_playwright() as p:
        for url, targets in ((BASE, [("section.hero", "--sc-ps"), ("section.hero", "--sc-p"), ("section.hero", "--zz-unused"),
                                      ("#process", "--sc-ps"), ("#giant-section", "--sc-ps"), ("footer.close", "--sc-ps"),
                                      (".hero-sub", "--sc-ps"), (".hero-sub", "--zz-unused"), (":root", "--sc-ps"), (":root", "--sc-canvas")]),
                             (CTRL, [("#act", "--sc-ps"), ("#act", "--sc-p")])):
            for sel, prop in targets:
                b = p.chromium.launch(executable_path=CHROME)
                ctx = b.new_context(viewport={"width": 1440, "height": 900})
                pg = ctx.new_page()
                pg.route("**/sites/**", lambda r: r.abort())
                cdp = ctx.new_cdp_session(pg); cdp.send("Performance.enable")
                pg.goto(url, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(1200)
                n = 120
                before = metrics(cdp)
                ms = pg.evaluate(WRITE, [sel, prop, n])
                after = metrics(cdp)
                rd = after["RecalcStyleDuration"] - before["RecalcStyleDuration"]
                rc = after["RecalcStyleCount"] - before["RecalcStyleCount"]
                ld = after["LayoutDuration"] - before["LayoutDuration"]
                lc = after["LayoutCount"] - before["LayoutCount"]
                print(f"{url.split('/')[-1]:12s} {sel:16s} {prop:12s} writes {n}: recalc {rd*1000:7.1f} ms over {rc:4.0f} recalcs = {rd*1000/max(rc,1):5.2f} ms each | layout {ld*1000:6.1f} ms / {lc:.0f} | wall {ms:.0f} ms")
                b.close()

main()
