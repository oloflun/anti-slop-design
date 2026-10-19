"""profile2.py <out-dir>: second attribution pass. Same harness as profile.py (4x CPU,
100 px / 60 ms), plus (a) a setProperty counter per (element, property) during the run,
and (b) subtree ablations: the two big SVG paths in the hero, the glyph path / live image /
step text in the process act, and the ground layer in the hero."""
import json, sys, statistics
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CPU = 4
PX, MS = 100, 60

COUNTER_INIT = r"""
(() => {
  window.__sp = {};
  const orig = CSSStyleDeclaration.prototype.setProperty;
  CSSStyleDeclaration.prototype.setProperty = function(name, value, prio){
    if (window.__spOn){
      const el = this.__el || (this.parentRule ? 'rule' : 'inline');
      const key = name + ' @ ' + (this.__owner || '?');
      window.__sp[key] = (window.__sp[key] || 0) + 1;
    }
    return orig.call(this, name, value, prio);
  };
  // tag inline style declarations with their owner once
  const styleDesc = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'style') || Object.getOwnPropertyDescriptor(Element.prototype, 'style');
  if (styleDesc && styleDesc.get){
    const g = styleDesc.get;
    Object.defineProperty(Element.prototype, 'style', { get: function(){ const s = g.call(this); if (!s.__owner) s.__owner = this.tagName.toLowerCase() + (this.id ? '#' + this.id : '') + (this.className && typeof this.className === 'string' ? '.' + this.className.split(' ')[0] : ''); return s; }, configurable: true });
  }
})();
"""
RAF_START = """() => { window.__ft = []; window.__ftOn = true; window.__spOn = true; window.__sp = {}; let last = performance.now();
  const loop = t => { if (!window.__ftOn) return; window.__ft.push(t - last); last = t; requestAnimationFrame(loop); };
  requestAnimationFrame(loop); }"""
RAF_STOP = "() => { window.__ftOn = false; window.__spOn = false; return {ft: window.__ft.slice(1), sp: window.__sp}; }"
KEYS = ["TaskDuration", "ScriptDuration", "LayoutDuration", "RecalcStyleDuration", "LayoutCount", "RecalcStyleCount"]

def metrics(cdp):
    return {x["name"]: x["value"] for x in cdp.send("Performance.getMetrics")["metrics"]}

def frame_stats(ft):
    if not ft: return {}
    s = sorted(ft); p95 = s[min(len(s) - 1, int(round(0.95 * len(s))) - 1)]
    return {"n": len(ft), "p95_ms": round(p95, 1), "over33": sum(1 for x in ft if x > 33), "mean_ms": round(statistics.mean(ft), 1)}

def run(p, name, start_y, ticks, css=None, block_sites=True, count=False, url=None):
    url = url or BASE
    b = p.chromium.launch(executable_path=CHROME)
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    pg = ctx.new_page()
    if count:
        pg.add_init_script(COUNTER_INIT)
    if block_sites:
        pg.route("**/sites/**", lambda r: r.abort())
    cdp = ctx.new_cdp_session(pg)
    cdp.send("Performance.enable")
    cdp.send("Emulation.setCPUThrottlingRate", {"rate": CPU})
    pg.goto(url, wait_until="networkidle", timeout=60000)
    pg.wait_for_timeout(1500)
    if css:
        pg.add_style_tag(content=css)
    pg.evaluate(f"window.scrollTo(0,{start_y})")
    pg.wait_for_timeout(1200)
    pg.mouse.move(1000, 450)
    before = metrics(cdp)
    pg.evaluate(RAF_START)
    for _ in range(ticks):
        pg.mouse.wheel(0, PX); pg.wait_for_timeout(MS)
    pg.wait_for_timeout(300)
    r = pg.evaluate(RAF_STOP)
    after = metrics(cdp)
    d = {k: round(after.get(k, 0) - before.get(k, 0), 3) for k in KEYS if k in after}
    sp = dict(sorted(r["sp"].items(), key=lambda kv: -kv[1])[:14]) if count else {}
    out = {"name": name, "start": start_y, "ticks": ticks, "delta": d, "frames": frame_stats(r["ft"]), "writes": sp}
    b.close()
    f = out["frames"]
    print(f"{name:28s} n {f.get('n',0):>3} p95 {f.get('p95_ms',0):>6} >33 {f.get('over33',0):>3} mean {f.get('mean_ms',0):>5} | task {d.get('TaskDuration',0):.2f}s recalc {d.get('RecalcStyleDuration',0):.2f} rec# {d.get('RecalcStyleCount',0):.0f} layout {d.get('LayoutDuration',0):.2f} lay# {d.get('LayoutCount',0):.0f}")
    if count:
        for k, v in sp.items(): print("    ", v, k)
    return out

def main(out_dir):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    res = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME); pg = b.new_page(viewport={"width": 1440, "height": 900})
        pg.goto(BASE, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(1000)
        g = pg.evaluate("() => { const r = s => Math.round(document.querySelector(s).getBoundingClientRect().top + scrollY); return {stagger: r('.stagger'), process: r('#process'), principles: r('#principer')}; }")
        b.close()
        proc0 = g["process"] - 900; band0 = g["stagger"] - 600
        HIDE_HERO_SVG = ".logo-dock,.card-glyph{display:none !important}"
        res.append(run(p, "hero-count", 0, 30, count=True))
        res.append(run(p, "hero-noSvgPaths", 0, 30, css=HIDE_HERO_SVG))
        res.append(run(p, "hero-noGround", 0, 30, css=".ground{display:none !important}"))
        res.append(run(p, "hero-noSvg-noGround", 0, 30, css=HIDE_HERO_SVG + ".ground{display:none !important}"))
        res.append(run(p, "band-count", band0, 28, count=True))
        res.append(run(p, "band-noHeroSvg", band0, 28, css=HIDE_HERO_SVG))
        res.append(run(p, "band-noHeroSvg-noPGlyph", band0, 28, css=HIDE_HERO_SVG + "#p-glyph{display:none !important}"))
        res.append(run(p, "process-count", proc0, 45, count=True))
        res.append(run(p, "process-noPGlyph", proc0, 45, css="#p-glyph{display:none !important}"))
        res.append(run(p, "process-noLiveImg", proc0, 45, css="#p-live-img{display:none !important}"))
        res.append(run(p, "process-noSteps", proc0, 45, css=".process-steps{visibility:hidden !important}"))
        res.append(run(p, "process-noPGlyph-noHeroSvg", proc0, 45, css="#p-glyph{display:none !important}" + HIDE_HERO_SVG))
        res.append(run(p, "process-allPathsOff", proc0, 45, css="#p-glyph{display:none !important}" + HIDE_HERO_SVG + ".process-sheet{display:none !important}"))
        res.append(run(p, "control-smooth", 0, 30, url="http://localhost:3090/tests/motion/smooth.html", count=True))
    (out / "profile2.json").write_text(json.dumps({"geom": g, "runs": res}, indent=1), encoding="utf-8")
    print("PROFILE2-DONE")

if __name__ == "__main__":
    main(sys.argv[1])
