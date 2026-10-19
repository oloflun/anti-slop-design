"""profile3.py <out-dir>: third attribution pass (4x CPU, 100 px / 60 ms).
Ablations: (a) container-type off on .hero-plate/.panel-giant; (b) dedup of the engine's
per-frame --sc-p writes (in-page monkeypatch, measurement only); (e) content-visibility:auto
on the big off-screen sections so a document-wide recalc skips them; combinations."""
import json, sys, statistics
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CPU = 4
PX, MS = 100, 60

DEDUP_INIT = r"""
(() => {
  const orig = CSSStyleDeclaration.prototype.setProperty;
  const memo = new WeakMap();
  window.__skipped = 0;
  CSSStyleDeclaration.prototype.setProperty = function(n, v, p){
    if (n === '--sc-p' || n === '--sc-canvas'){
      let m = memo.get(this); if (!m){ m = {}; memo.set(this, m); }
      if (m[n] === v){ window.__skipped++; return; }
      m[n] = v;
    }
    return orig.call(this, n, v, p);
  };
})();
"""
RAF_START = """() => { window.__ft = []; window.__ftOn = true; let last = performance.now();
  const loop = t => { if (!window.__ftOn) return; window.__ft.push(t - last); last = t; requestAnimationFrame(loop); };
  requestAnimationFrame(loop); }"""
RAF_STOP = "() => { window.__ftOn = false; return window.__ft.slice(1); }"
KEYS = ["TaskDuration", "ScriptDuration", "LayoutDuration", "RecalcStyleDuration", "LayoutCount", "RecalcStyleCount"]

def metrics(cdp):
    return {x["name"]: x["value"] for x in cdp.send("Performance.getMetrics")["metrics"]}

def frame_stats(ft):
    if not ft: return {}
    s = sorted(ft); p95 = s[min(len(s) - 1, int(round(0.95 * len(s))) - 1)]
    return {"n": len(ft), "p95_ms": round(p95, 1), "over33": sum(1 for x in ft if x > 33), "mean_ms": round(statistics.mean(ft), 1)}

def run(p, name, start_y, ticks, css=None, dedup=False, url=None):
    url = url or BASE
    b = p.chromium.launch(executable_path=CHROME)
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    pg = ctx.new_page()
    if dedup:
        pg.add_init_script(DEDUP_INIT)
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
    ft = pg.evaluate(RAF_STOP)
    after = metrics(cdp)
    skipped = pg.evaluate("window.__skipped || 0")
    d = {k: round(after.get(k, 0) - before.get(k, 0), 3) for k in KEYS if k in after}
    out = {"name": name, "start": start_y, "ticks": ticks, "delta": d, "frames": frame_stats(ft), "skipped": skipped}
    b.close()
    f = out["frames"]
    print(f"{name:30s} n {f.get('n',0):>3} p95 {f.get('p95_ms',0):>6} >33 {f.get('over33',0):>3} mean {f.get('mean_ms',0):>5} | task {d.get('TaskDuration',0):.2f}s recalc {d.get('RecalcStyleDuration',0):.2f} rec# {d.get('RecalcStyleCount',0):.0f} layout {d.get('LayoutDuration',0):.2f} lay# {d.get('LayoutCount',0):.0f} skipped {skipped}")
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
        NOCQ = ".hero-plate,.panel-giant{container-type:normal !important}"
        CV_PROCESS = ".process{content-visibility:auto;contain-intrinsic-size:auto 3800px}.principles{content-visibility:auto;contain-intrinsic-size:auto 550px}"
        CV_BAND = ".panel-thesis,.panel-giant,.price{content-visibility:auto;contain-intrinsic-size:auto 800px}"
        CV_ALL = CV_PROCESS + CV_BAND
        res.append(run(p, "hero", 0, 30))
        res.append(run(p, "hero-noCQ", 0, 30, css=NOCQ))
        res.append(run(p, "hero-dedup", 0, 30, dedup=True))
        res.append(run(p, "hero-cvProcess", 0, 30, css=CV_PROCESS))
        res.append(run(p, "hero-cvAll", 0, 30, css=CV_ALL))
        res.append(run(p, "hero-cvAll-dedup-noCQ", 0, 30, css=CV_ALL + NOCQ, dedup=True))
        res.append(run(p, "band", band0, 28))
        res.append(run(p, "band-noCQ", band0, 28, css=NOCQ))
        res.append(run(p, "band-dedup", band0, 28, dedup=True))
        res.append(run(p, "band-cvProcess", band0, 28, css=CV_PROCESS))
        res.append(run(p, "band-cvProcess-dedup", band0, 28, css=CV_PROCESS, dedup=True))
        res.append(run(p, "band-cvProcess-dedup-noCQ", band0, 28, css=CV_PROCESS + NOCQ, dedup=True))
        res.append(run(p, "process", proc0, 45))
        res.append(run(p, "process-dedup", proc0, 45, dedup=True))
        res.append(run(p, "process-cvBand", proc0, 45, css=CV_BAND))
        res.append(run(p, "process-cvBand-dedup", proc0, 45, css=CV_BAND, dedup=True))
        res.append(run(p, "process-cvBand-dedup-noCQ", proc0, 45, css=CV_BAND + NOCQ, dedup=True))
        res.append(run(p, "control-smooth", 0, 30, url="http://localhost:3090/tests/motion/smooth.html"))
    (out / "profile3.json").write_text(json.dumps({"geom": g, "runs": res}, indent=1), encoding="utf-8")
    print("PROFILE3-DONE")

if __name__ == "__main__":
    main(sys.argv[1])
