"""synth3.py: targeted write-cost tests (cpu 1, 120 writes, one per rAF) for the plan:
 (1) --sc-p registered inherits:false: write cost on hero / giant / process
 (2) hero: the two 2 kB glyph paths given a short d (is path re-parse the cost?)
 (3) giant: .is-scrubbed removed (are the 60 var()-spans the cost?)
 (4) process: #p-glyph short d; sheet text hidden
Then whole-segment scroll runs at cpu 4 with --sc-p inherits:false (hero, band, process)
and the giant word-fit at 901/1024/1280/1440 for the candidate clamp."""
import json, sys, statistics
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"

WRITE = """([sel, prop, n]) => new Promise(res => {
  const el = sel === ':root' ? document.documentElement : document.querySelector(sel);
  let i = 0;
  const step = () => {
    el.style.setProperty(prop, (0.1 + (i % 50) * 0.01).toFixed(4));
    void getComputedStyle(el).opacity;
    if (++i < n) requestAnimationFrame(step); else res(i);
  };
  requestAnimationFrame(step);
})"""
REG_SCP = "CSS.registerProperty({name:'--sc-p',syntax:'<number>',inherits:false,initialValue:'0'})"
SHORT_D = ".logo-dock path,.card-glyph path{d:path('M0 0 H10 V10 Z') !important}"

def metrics(cdp):
    return {x["name"]: x["value"] for x in cdp.send("Performance.getMetrics")["metrics"]}

def measure(p, label, sel, prop, css=None, js=None):
    b = p.chromium.launch(executable_path=CHROME)
    ctx = b.new_context(viewport={"width": 1440, "height": 900}); pg = ctx.new_page()
    pg.route("**/sites/**", lambda r: r.abort())
    cdp = ctx.new_cdp_session(pg); cdp.send("Performance.enable")
    pg.goto(BASE, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(1200)
    if css: pg.add_style_tag(content=css)
    if js: pg.evaluate(js)
    pg.wait_for_timeout(200)
    n = 120
    before = metrics(cdp); pg.evaluate(WRITE, [sel, prop, n]); after = metrics(cdp)
    rd = (after["RecalcStyleDuration"] - before["RecalcStyleDuration"]) * 1000
    rc = after["RecalcStyleCount"] - before["RecalcStyleCount"]
    print(f"{label:58s} {rd/max(rc,1):6.2f} ms per recalc ({rc:.0f})")
    b.close()

RAF_START = """() => { window.__ft = []; window.__ftOn = true; let last = performance.now();
  const loop = t => { if (!window.__ftOn) return; window.__ft.push(t - last); last = t; requestAnimationFrame(loop); };
  requestAnimationFrame(loop); }"""
RAF_STOP = "() => { window.__ftOn = false; return window.__ft.slice(1); }"

def scroll_run(p, name, start_y, ticks, css=None, init=None):
    b = p.chromium.launch(executable_path=CHROME)
    ctx = b.new_context(viewport={"width": 1440, "height": 900}); pg = ctx.new_page()
    if init: pg.add_init_script(init)
    pg.route("**/sites/**", lambda r: r.abort())
    cdp = ctx.new_cdp_session(pg); cdp.send("Performance.enable"); cdp.send("Emulation.setCPUThrottlingRate", {"rate": 4})
    pg.goto(BASE, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(1500)
    if css: pg.add_style_tag(content=css)
    pg.evaluate(f"window.scrollTo(0,{start_y})"); pg.wait_for_timeout(1200); pg.mouse.move(1000, 450)
    before = metrics(cdp); pg.evaluate(RAF_START)
    for _ in range(ticks):
        pg.mouse.wheel(0, 100); pg.wait_for_timeout(60)
    pg.wait_for_timeout(300)
    ft = pg.evaluate(RAF_STOP); after = metrics(cdp)
    s = sorted(ft); p95 = s[min(len(s) - 1, int(round(0.95 * len(s))) - 1)]
    rd = after["RecalcStyleDuration"] - before["RecalcStyleDuration"]; rc = after["RecalcStyleCount"] - before["RecalcStyleCount"]
    print(f"{name:40s} n {len(ft):>3} p95 {p95:6.1f} >33 {sum(1 for x in ft if x > 33):>3} mean {statistics.mean(ft):5.1f} | recalc {rd:.2f}s / {rc:.0f} = {rd*1000/max(rc,1):.1f} ms each")
    b.close()

def main():
    with sync_playwright() as p:
        measure(p, "hero --sc-p, as built", "section.hero", "--sc-p")
        measure(p, "hero --sc-p, registered inherits:false", "section.hero", "--sc-p", js=REG_SCP)
        measure(p, "giant --sc-p, registered inherits:false", "#giant-section", "--sc-p", js=REG_SCP)
        measure(p, "process --sc-p, registered inherits:false", "#process", "--sc-p", js=REG_SCP)
        measure(p, "hero --sc-ps, as built", "section.hero", "--sc-ps")
        measure(p, "hero --sc-ps, glyph paths short d", "section.hero", "--sc-ps", css=SHORT_D)
        measure(p, "hero --sc-ps, glyph svgs display:none", "section.hero", "--sc-ps", css=".logo-dock,.card-glyph{display:none !important}")
        measure(p, "giant --sc-ps, as built", "#giant-section", "--sc-ps")
        measure(p, "giant --sc-ps, is-scrubbed removed", "#giant-section", "--sc-ps", js="document.getElementById('giant-section').classList.remove('is-scrubbed')")
        measure(p, "giant --sc-ps, spans unwrapped to text", "#giant-section", "--sc-ps",
                js="document.querySelectorAll('#giant-section .scrub-text h3, #giant-section .scrub-text p').forEach(e => { e.textContent = e.textContent; })")
        measure(p, "process --sc-ps, as built", "#process", "--sc-ps")
        measure(p, "process --sc-ps, #p-glyph short d", "#process", "--sc-ps", css="#p-glyph{d:path('M0 0 H10 V10 Z') !important}")
        measure(p, "process --sc-ps, sheet <text> hidden", "#process", "--sc-ps", css=".process-sheet text{display:none !important}")
        measure(p, "process --sc-ps, .measure static fill/transform", "#process", "--sc-ps", css=".process-sheet .measure{fill:#1e5e9c !important;transform:none !important;opacity:1 !important}")
        # whole-segment runs with --sc-p inherits:false (registered before the engine mounts)
        b = p.chromium.launch(executable_path=CHROME); pg = b.new_page(viewport={"width": 1440, "height": 900})
        pg.goto(BASE, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(1000)
        g = pg.evaluate("() => { const r = s => Math.round(document.querySelector(s).getBoundingClientRect().top + scrollY); return {stagger: r('.stagger'), process: r('#process')}; }")
        b.close()
        INIT = "try{CSS.registerProperty({name:'--sc-p',syntax:'<number>',inherits:false,initialValue:'0'})}catch(e){}"
        for name, y, t in (("hero", 0, 30), ("band", g["stagger"] - 600, 28), ("process", g["process"] - 900, 45)):
            scroll_run(p, name + " as built", y, t)
            scroll_run(p, name + " --sc-p inherits:false", y, t, init=INIT)
            scroll_run(p, name + " inherits:false + short d + no spans", y, t, init=INIT + ";addEventListener('DOMContentLoaded',()=>{setTimeout(()=>{document.querySelectorAll('#giant-section .scrub-text h3, #giant-section .scrub-text p').forEach(e=>{e.textContent=e.textContent;});},400)})",
                       css=SHORT_D + "#p-glyph{d:path('M0 0 H10 V10 Z') !important}")
        # giant word fit for the candidate clamp at four widths
        b = p.chromium.launch(executable_path=CHROME)
        for w in (901, 1024, 1280, 1440):
            pg = b.new_page(viewport={"width": w, "height": 900})
            pg.goto(BASE, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(800)
            r = pg.evaluate("""() => { const g = document.querySelector('.giant'); const head = g.parentNode;
              const colW = head.getBoundingClientRect().width;
              g.style.fontSize = 'clamp(2.1rem, 7.4vw - 18px, 5.5rem)'; g.style.letterSpacing = '-0.04em'; g.style.hyphens = 'manual';
              const fs = parseFloat(getComputedStyle(g).fontSize);
              const probe = document.createElement('span'); probe.textContent = 'VARUMÄRKE.';
              probe.style.cssText = 'position:absolute;white-space:nowrap;visibility:hidden;font-family:' + getComputedStyle(g).fontFamily + ';font-weight:700;text-transform:uppercase;font-size:' + fs + 'px;letter-spacing:-0.04em';
              document.body.appendChild(probe); const ww = probe.getBoundingClientRect().width; probe.remove();
              const range = document.createRange(); const tn = g.firstChild; const txt = tn.textContent; const i = txt.indexOf('VARUM'); range.setStart(tn, i); range.setEnd(tn, i + 10);
              const lines = Math.round(g.getBoundingClientRect().height / (fs * 0.96));
              return {w: innerWidth, colW: +colW.toFixed(1), fs: +fs.toFixed(1), wordW: +ww.toFixed(1), fits: ww <= colW, wordRects: range.getClientRects().length, lines, overflow: g.scrollWidth > g.clientWidth + 1}; }""")
            print("giant fit", json.dumps(r, ensure_ascii=False))
            pg.close()
        b.close()

main()
