"""profile.py <out-dir>: CDP attribution of frame time per page segment and per
ablation, at 4x CPU, scripted wheel 100 px / 60 ms (same cadence as motion_probe).

Segments (1440x900): hero pin, band (frames awake / frames blocked / frames forced
asleep = R7 broken state), process life, tail (principles + footer).
Ablations on the band: .ground::after (mix-blend tone) off; on process: sheet hidden,
#process removed from the shim's act list (no --sc-ps writes on #process).

Metrics: CDP Performance.getMetrics deltas (TaskDuration, ScriptDuration,
LayoutDuration, RecalcStyleDuration, LayoutCount, RecalcStyleCount) plus an in-page
rAF frame-time log (p95, frames > 33 ms, n).
"""
import json, sys, statistics
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CPU = 4
PX, MS = 100, 60

RAF_START = """() => { window.__ft = []; window.__ftOn = true; let last = performance.now();
  const loop = t => { if (!window.__ftOn) return; window.__ft.push(t - last); last = t; requestAnimationFrame(loop); };
  requestAnimationFrame(loop); }"""
RAF_STOP = "() => { window.__ftOn = false; return window.__ft.slice(1); }"

KEYS = ["TaskDuration", "ScriptDuration", "LayoutDuration", "RecalcStyleDuration", "LayoutCount", "RecalcStyleCount", "StyleRecalcDuration"]

def metrics(cdp):
    m = cdp.send("Performance.getMetrics")["metrics"]
    return {x["name"]: x["value"] for x in m}

def frame_stats(ft):
    if not ft:
        return {}
    s = sorted(ft)
    p95 = s[min(len(s) - 1, int(round(0.95 * len(s))) - 1)]
    return {"n": len(ft), "p95_ms": round(p95, 1), "over33": sum(1 for x in ft if x > 33), "mean_ms": round(statistics.mean(ft), 1)}

def run(p, name, start_y, ticks, css=None, block_sites=False, drop_process_act=False, warm=None, url=None):
    url = url or BASE
    b = p.chromium.launch(executable_path=CHROME)
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    pg = ctx.new_page()
    if block_sites:
        pg.route("**/sites/**", lambda r: r.abort())
    cdp = ctx.new_cdp_session(pg)
    cdp.send("Performance.enable")
    cdp.send("Emulation.setCPUThrottlingRate", {"rate": CPU})
    pg.goto(url, wait_until="networkidle", timeout=60000)
    pg.wait_for_timeout(1500)
    if css:
        pg.add_style_tag(content=css)
    if drop_process_act:
        pg.evaluate("() => { const a = window.__scSmooth.acts; const i = a.findIndex(x => x.el.id === 'process'); if (i >= 0) a.splice(i, 1); window.__dropped = i; }")
    if warm:  # pre-scroll through a region so frames are mounted and awake before measuring
        for y in warm:
            pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(400)
        pg.wait_for_timeout(2500)
    pg.evaluate(f"window.scrollTo(0,{start_y})")
    pg.wait_for_timeout(1200)
    pg.mouse.move(1000, 450)
    before = metrics(cdp)
    pg.evaluate(RAF_START)
    for _ in range(ticks):
        pg.mouse.wheel(0, PX)
        pg.wait_for_timeout(MS)
    pg.wait_for_timeout(300)
    ft = pg.evaluate(RAF_STOP)
    after = metrics(cdp)
    state = pg.evaluate("() => [...document.querySelectorAll('.frame-wrap')].map(w => w.className + '|' + getComputedStyle(w).contentVisibility + '|src=' + !!w.querySelector('iframe').getAttribute('src'))")
    end_y = pg.evaluate("scrollY")
    d = {k: round(after.get(k, 0) - before.get(k, 0), 3) for k in KEYS if k in after}
    out = {"name": name, "start": start_y, "end": end_y, "ticks": ticks, "delta": d, "frames": frame_stats(ft), "frameState": state}
    b.close()
    print(json.dumps(out))
    return out

def main(out_dir):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    res = []
    with sync_playwright() as p:
        # geometry
        b = p.chromium.launch(executable_path=CHROME); pg = b.new_page(viewport={"width": 1440, "height": 900})
        pg.goto(BASE, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(1000)
        g = pg.evaluate("() => { const r = s => Math.round(document.querySelector(s).getBoundingClientRect().top + scrollY); return {stagger: r('.stagger'), process: r('#process'), principles: r('#principer'), close: r('footer.close'), docH: document.documentElement.scrollHeight}; }")
        b.close()
        print("geom", g)
        band0 = g["stagger"] - 600
        proc0 = g["process"] - 900
        tail0 = g["principles"] - 900
        # hero pin: 0 -> 3000
        res.append(run(p, "hero-pin", 0, 30))
        # band, frames as R7 leaves them (asleep = broken state), scrolling through
        res.append(run(p, "band-r7-asleep", band0, 28))
        # band, frames blocked (no live sites at all)
        res.append(run(p, "band-frames-blocked", band0, 28, block_sites=True))
        # band, frames awake and live: force wrappers awake
        res.append(run(p, "band-frames-awake", band0, 28, css=".frame-wrap.is-asleep{content-visibility:auto !important}", warm=[band0 + 300, band0 + 900, band0 + 1500]))
        # band, frames blocked and ground tone off (attribution of the mix-blend layer)
        res.append(run(p, "band-blocked-noTone", band0, 28, block_sites=True, css=".ground::after{display:none !important}"))
        # band, frames blocked and giant scale off
        res.append(run(p, "band-blocked-noGiantScale", band0, 28, block_sites=True, css=".js .giant{transform:none !important}"))
        # process life
        res.append(run(p, "process", proc0, 45, block_sites=True))
        res.append(run(p, "process-noSheet", proc0, 45, block_sites=True, css=".process-sheet{display:none !important}"))
        res.append(run(p, "process-noAct", proc0, 45, block_sites=True, drop_process_act=True))
        res.append(run(p, "process-noGroundTone", proc0, 45, block_sites=True, css=".ground::after{display:none !important}"))
        res.append(run(p, "process-noGround", proc0, 45, block_sites=True, css=".ground{display:none !important}"))
        # tail
        res.append(run(p, "tail", tail0, 20, block_sites=True))
        # control fixture
        res.append(run(p, "control-smooth", 0, 30, url="http://localhost:3090/tests/motion/smooth.html"))
    (out / "profile.json").write_text(json.dumps({"geom": g, "runs": res}, indent=1), encoding="utf-8")
    print("PROFILE-DONE")

if __name__ == "__main__":
    main(sys.argv[1])
