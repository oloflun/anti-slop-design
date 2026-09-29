# GPU new-headless, CPU throttle, trace a wheel window and attribute main-thread time. Headless only.
import sys, json, time, collections, os
from playwright.sync_api import sync_playwright
url, cpu, w, h, start_sel, ticks, px, gap = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8])
INIT = "window.__f=[];(function L(n){window.__f.push([n,scrollY]);requestAnimationFrame(L)})(performance.now());"
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, channel="chromium", args=["--enable-gpu","--ignore-gpu-blocklist","--use-angle=d3d11"])
    try:
        ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg = ctx.new_page(); pg.add_init_script(INIT)
        import os
        mode = os.environ.get("AB", "")
        if "nowc" in mode:
            pg.add_init_script("document.addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');s.textContent='.tile-grid>span,.case-choice-frame img{will-change:auto!important}';document.head.appendChild(s)})")
        if "nograin" in mode:
            pg.add_init_script("if(location.pathname.indexOf('/sites/')===0)document.addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');s.textContent='.grain::before{display:none!important}';document.head.appendChild(s)})")
        if "noiframe" in mode:
            pg.route("**/sites/*.html", lambda r: r.fulfill(status=200, content_type="text/html", body="<html><body style='height:5000px'></body></html>"))
        cdp = ctx.new_cdp_session(pg)
        pg.goto(url, wait_until="load", timeout=90000); pg.wait_for_timeout(4000)
        gpu = pg.evaluate("(()=>{const c=document.createElement('canvas').getContext('webgl');const e=c&&c.getExtension('WEBGL_debug_renderer_info');return e?c.getParameter(e.UNMASKED_RENDERER_WEBGL):'none'})()")
        if start_sel != "top":
            pg.evaluate("s => window.__lenis.scrollTo(s,{immediate:true})", start_sel); pg.wait_for_timeout(1500)
        cdp.send("LayerTree.enable")
        layers = {"n": 0}
        cdp.on("LayerTree.layerTreeDidChange", lambda e: layers.__setitem__("n", len(e.get("layers") or [])) )
        pg.wait_for_timeout(300)
        if cpu > 1: cdp.send("Emulation.setCPUThrottlingRate", {"rate": cpu})
        pg.mouse.move(w//2, h//2)
        chunks = []
        cdp.on("Tracing.dataCollected", lambda e: chunks.extend(e["value"]))
        cdp.send("Tracing.start", {"categories": "devtools.timeline,disabled-by-default-devtools.timeline,blink,cc,viz", "transferMode": "ReportEvents"})
        i0 = pg.evaluate("__f.length"); y0 = pg.evaluate("scrollY")
        for _ in range(ticks):
            pg.mouse.wheel(0, px); pg.wait_for_timeout(gap)
        pg.wait_for_timeout(600)
        i1 = pg.evaluate("__f.length")
        done = {"v": False}
        cdp.on("Tracing.tracingComplete", lambda e: done.__setitem__("v", True))
        cdp.send("Tracing.end")
        t = time.time()
        while not done["v"] and time.time() - t < 60: pg.wait_for_timeout(200)
        f = pg.evaluate("__f")[i0:i1]; y1 = pg.evaluate("scrollY")
        heap = pg.evaluate("performance.memory.usedJSHeapSize")
        m = {x["name"]: x["value"] for x in (cdp.send("Performance.enable") or cdp.send("Performance.getMetrics"))["metrics"]}
    finally:
        b.close()
d = sorted(b2[0]-a[0] for a, b2 in zip(f, f[1:]))
p95 = d[int(0.95*len(d))] if d else 0
# attribute: main renderer thread = thread with most 'RunTask' dur
ev = [e for e in chunks if e.get("ph") == "X"]
bytid = collections.Counter()
for e in ev:
    if e["name"] == "RunTask": bytid[(e["pid"], e["tid"])] += e.get("dur", 0)
main = None
for e in chunks:
    if e.get("name") == "thread_name" and e.get("args", {}).get("name") == "CrRendererMain":
        k=(e["pid"], e["tid"])
        if main is None or bytid[k] > bytid[main]: main = k
agg = collections.Counter(); cnt = collections.Counter()
for e in ev:
    if (e["pid"], e["tid"]) == main:
        agg[e["name"]] += e.get("dur", 0); cnt[e["name"]] += 1
longs = sorted([e.get("dur",0)/1000 for e in ev if (e["pid"],e["tid"])==main and e["name"]=="RunTask"], reverse=True)[:10]
fn = collections.Counter()
for e in ev:
    if (e["pid"],e["tid"])==main and e["name"] in ("FunctionCall","EvaluateScript","FireAnimationFrame","TimerFire","EventDispatch"):
        a = e.get("args",{}).get("data",{})
        fn[(e["name"], (a.get("url") or "")[-40:] + ":" + str(a.get("functionName","")) + ":" + str(a.get("lineNumber","")) + " " + str(a.get("type","")))] += e.get("dur",0)
out = {"mode": os.environ.get("AB",""), "per_frame_ms": {k: round(agg[k]/1000/max(1,cnt["ProxyMain::BeginMainFrame"]),1) for k in ["ProxyMain::BeginMainFrame","LocalFrameView::RunPaintLifecyclePhase","Paint","PrePaint","Commit","Layerize","FireAnimationFrame","UpdateLayoutTree","Layout","Document::UpdateStyleAndLayout","LocalFrameView::RunStyleAndLayoutLifecyclePhases"] if k in agg}, "gpu": gpu, "cpu": cpu, "window": [start_sel, ticks, px, gap], "scroll": [y0, y1], "frames": len(d), "p95_ms": round(p95,1),
       "over33": sum(1 for x in d if x > 33.4), "over20": sum(1 for x in d if x > 20), "median": round(d[len(d)//2],1) if d else 0,
       "layers": layers["n"], "heap_MB": round(heap/1e6,1), "nodes": m.get("Nodes"),
       "main_ms": {k: round(v/1000) for k, v in agg.most_common(22)}, "counts": {k: cnt[k] for k,_ in agg.most_common(22)},
       "top_runtasks_ms": [round(x) for x in longs],
       "top_fn_ms": [[k[0], k[1], round(v/1000)] for k, v in fn.most_common(10)]}
print(json.dumps(out, indent=1))
