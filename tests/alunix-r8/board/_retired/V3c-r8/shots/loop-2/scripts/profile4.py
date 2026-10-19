"""profile4.py <out-dir>: measure plan 028's shim (batched reads/writes, --sc-p
inherits:false) by route-substituting scroll/sc-smooth.js. Same harness as
profile.py (cpu 4 and cpu 1, 100 px / 60 ms). Also verifies the smoothing contract
survives (staircase on --sc-ps via the same logic as motion_probe: max step and
monotonicity of the value sampled per frame)."""
import json, sys, statistics
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
SHIM = Path(__file__).with_name("sc-smooth-batched.js").read_text(encoding="utf-8")

RAF_START = """(sel) => { window.__ft = []; window.__vals = []; window.__ftOn = true; let last = performance.now();
  const el = document.querySelector(sel);
  const loop = t => { if (!window.__ftOn) return; window.__ft.push(t - last); last = t;
    window.__vals.push(parseFloat(el.style.getPropertyValue('--sc-ps')) || 0); requestAnimationFrame(loop); };
  requestAnimationFrame(loop); }"""
RAF_STOP = "() => { window.__ftOn = false; return {ft: window.__ft.slice(1), vals: window.__vals}; }"
KEYS = ["TaskDuration", "RecalcStyleDuration", "RecalcStyleCount", "LayoutDuration", "LayoutCount"]

def metrics(cdp):
    return {x["name"]: x["value"] for x in cdp.send("Performance.getMetrics")["metrics"]}

def run(p, name, start_y, ticks, sel, cpu=4, shim=False, noinherit=True, block=True):
    b = p.chromium.launch(executable_path=CHROME)
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1); pg = ctx.new_page()
    if shim:
        body = SHIM if noinherit else SHIM.replace("window.__scpNoInherit !== false", "false")
        pg.route("**/scroll/sc-smooth.js", lambda r: r.fulfill(status=200, content_type="application/javascript", body=body))
    if block: pg.route("**/sites/**", lambda r: r.abort())
    cdp = ctx.new_cdp_session(pg); cdp.send("Performance.enable"); cdp.send("Emulation.setCPUThrottlingRate", {"rate": cpu})
    pg.goto(BASE, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(1500)
    pg.evaluate(f"window.scrollTo(0,{start_y})"); pg.wait_for_timeout(1200); pg.mouse.move(1000, 450)
    before = metrics(cdp); pg.evaluate(RAF_START, sel)
    for _ in range(ticks):
        pg.mouse.wheel(0, 100); pg.wait_for_timeout(60)
    pg.wait_for_timeout(400)
    r = pg.evaluate(RAF_STOP); after = metrics(cdp)
    ft, vals = r["ft"], r["vals"]
    s = sorted(ft); p95 = s[min(len(s) - 1, int(round(0.95 * len(s))) - 1)]
    steps = [abs(vals[i] - vals[i - 1]) for i in range(1, len(vals))]
    max_step = max(steps) * 100 if steps else 0
    # staircase: a run of >=3 identical values followed by a jump > 1.5 % while scrolling
    stair = 0; run_len = 0
    for i in range(1, len(vals)):
        if vals[i] == vals[i - 1]: run_len += 1
        else:
            if run_len >= 3 and abs(vals[i] - vals[i - 1]) > 0.015: stair += 1
            run_len = 0
    d = {k: round(after.get(k, 0) - before.get(k, 0), 3) for k in KEYS if k in after}
    out = {"name": name, "cpu": cpu, "shim": shim, "n": len(ft), "p95": round(p95, 1), "over33": sum(1 for x in ft if x > 33), "mean": round(statistics.mean(ft), 1),
           "recalcs": d["RecalcStyleCount"], "recalc_s": d["RecalcStyleDuration"], "task_s": d["TaskDuration"], "max_step_pct": round(max_step, 2), "staircase": stair}
    print(f"{name:34s} cpu {cpu} shim {str(shim):5s} n {len(ft):>3} p95 {p95:6.1f} >33 {out['over33']:>3} mean {out['mean']:5.1f} | recalcs {d['RecalcStyleCount']:.0f} ({d['RecalcStyleCount']/max(len(ft),1):.2f}/frame) {d['RecalcStyleDuration']:.2f}s task {d['TaskDuration']:.2f}s | max_step {max_step:.2f}% stair {stair}")
    b.close(); return out

def main(out_dir):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True); res = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME); pg = b.new_page(viewport={"width": 1440, "height": 900})
        pg.goto(BASE, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(1000)
        g = pg.evaluate("() => { const r = s => Math.round(document.querySelector(s).getBoundingClientRect().top + scrollY); return {stagger: r('.stagger'), process: r('#process')}; }")
        b.close()
        segs = (("hero", 0, 30, "section.hero"), ("band", g["stagger"] - 600, 28, "#giant-section"), ("process", g["process"] - 900, 45, "#process"))
        for cpu in (4, 1):
            for name, y, t, sel in segs:
                res.append(run(p, name + " as built", y, t, sel, cpu=cpu))
                res.append(run(p, name + " shim batched+noinherit", y, t, sel, cpu=cpu, shim=True))
                if cpu == 4:
                    res.append(run(p, name + " shim batched only", y, t, sel, cpu=cpu, shim=True, noinherit=False))
        res.append(run(p, "control smooth.html", 0, 30, "#act", cpu=4, block=False))
    (out / "profile4.json").write_text(json.dumps({"geom": g, "runs": res}, indent=1), encoding="utf-8")
    print("PROFILE4-DONE")

if __name__ == "__main__":
    main(sys.argv[1])
