"""synth2.py: (1) what in the hero subtree makes one --sc-ps write cost 1.9 ms: ablate
parts with display:none and re-measure; (2) --sc-canvas on :root registered with
inherits:false (page-level CSS.registerProperty) vs today; (3) --sc-ps write on a
process act whose subtree excludes the steps text; (4) which acts have no consumer."""
import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"

WRITE = """([sel, prop, n]) => new Promise(res => {
  const el = sel === ':root' ? document.documentElement : document.querySelector(sel);
  let i = 0;
  const step = () => {
    el.style.setProperty(prop, prop === '--sc-canvas' ? ('rgb(' + (10 + i % 40) + ',30,60)') : (0.1 + (i % 50) * 0.01).toFixed(4));
    void getComputedStyle(el).opacity;
    if (++i < n) requestAnimationFrame(step); else res(i);
  };
  requestAnimationFrame(step);
})"""

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
    print(f"{label:52s} {rd/max(rc,1):6.2f} ms per recalc ({rc:.0f} recalcs, {rd:.0f} ms)")
    b.close()

def main():
    with sync_playwright() as p:
        measure(p, "hero --sc-ps, as built", "section.hero", "--sc-ps")
        measure(p, "hero, .face--back display:none", "section.hero", "--sc-ps", css=".face--back{display:none !important}")
        measure(p, "hero, .logo-dock display:none", "section.hero", "--sc-ps", css=".logo-dock{display:none !important}")
        measure(p, "hero, both svgs display:none", "section.hero", "--sc-ps", css=".logo-dock,.card-glyph{display:none !important}")
        measure(p, "hero, img display:none", "section.hero", "--sc-ps", css="#heroPoolImg{display:none !important}")
        measure(p, "hero, .hero-head display:none", "section.hero", "--sc-ps", css=".hero-head{display:none !important}")
        measure(p, "hero, .plate-card display:none", "section.hero", "--sc-ps", css=".plate-card{display:none !important}")
        measure(p, "hero, .hero-plate container-type:normal", "section.hero", "--sc-ps", css=".hero-plate{container-type:normal !important}")
        measure(p, ":root --sc-canvas, as built (unregistered)", ":root", "--sc-canvas")
        measure(p, ":root --sc-canvas, registered inherits:false", ":root", "--sc-canvas",
                js="CSS.registerProperty({name:'--sc-canvas',syntax:'<color>',inherits:false,initialValue:'#0b0c0e'})")
        measure(p, ":root --sc-canvas, registered inherits:true", ":root", "--sc-canvas",
                js="CSS.registerProperty({name:'--sc-canvas',syntax:'<color>',inherits:true,initialValue:'#0b0c0e'})")
        measure(p, ".ground --sc-canvas (write on the consumer)", ".ground", "--sc-canvas")
        measure(p, "#process --sc-ps, as built", "#process", "--sc-ps")
        measure(p, "#process, .process-steps display:none", "#process", "--sc-ps", css=".process-steps{display:none !important}")
        measure(p, "#process, .process-sheet display:none", "#process", "--sc-ps", css=".process-sheet{display:none !important}")
        measure(p, "#giant-section --sc-ps, as built", "#giant-section", "--sc-ps")
        measure(p, "#giant-section, .ledger display:none", "#giant-section", "--sc-ps", css=".ledger{display:none !important}")
        measure(p, ".price --sc-ps", ".price", "--sc-ps")
        measure(p, "#principer --sc-ps", "#principer", "--sc-ps")
        measure(p, ".panel-thesis --sc-ps", ".panel-thesis", "--sc-ps")
        measure(p, ".calyx-fig --sc-ps (asleep)", ".calyx-fig", "--sc-ps")
main()
