# LCP / CLS / long-task attribution diagnostics. Headless only.
import sys, json
from playwright.sync_api import sync_playwright
url, cpu, w, h, gpu = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5] == "gpu"
INIT = r"""
window.__d = {lcp:[], ls:[], lt:[], t0: performance.now()};
const desc = n => { if(!n) return null; if(n.nodeType!==1) n=n.parentElement; if(!n) return null;
  return n.tagName.toLowerCase()+(n.id?'#'+n.id:'')+(n.className&&typeof n.className==='string'?'.'+n.className.trim().split(/\s+/).slice(0,2).join('.'):'') + (n.src? ' '+n.src.slice(-50):''); };
new PerformanceObserver(l => l.getEntries().forEach(e => __d.lcp.push({t: Math.round(e.startTime), size: e.size, el: desc(e.element), url: (e.url||'').slice(-60), rt: Math.round(e.renderTime), lt: Math.round(e.loadTime)}))).observe({type:'largest-contentful-paint', buffered:true});
new PerformanceObserver(l => l.getEntries().forEach(e => __d.ls.push({t: Math.round(e.startTime), v: +e.value.toFixed(4), input: e.hadRecentInput, scrollY: scrollY, src: (e.sources||[]).map(s => desc(s.node)+' '+JSON.stringify([Math.round(s.previousRect.y),Math.round(s.currentRect.y),Math.round(s.previousRect.height),Math.round(s.currentRect.height)]))}))).observe({type:'layout-shift', buffered:true});
new PerformanceObserver(l => l.getEntries().forEach(e => __d.lt.push({t: Math.round(e.startTime), d: Math.round(e.duration), scrollY: scrollY, attr: (e.attribution||[]).map(a => a.containerType+':'+(a.containerSrc||a.containerName||''))}))).observe({type:'longtask', buffered:true});
"""
args = ["--enable-gpu", "--ignore-gpu-blocklist", "--use-angle=d3d11"] if gpu else []
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, channel="chromium" if gpu else None, args=args)
    try:
        ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg = ctx.new_page()
        if cpu > 1:
            ctx.new_cdp_session(pg).send("Emulation.setCPUThrottlingRate", {"rate": cpu})
        pg.add_init_script(INIT)
        reqs = []
        pg.on("requestfinished", lambda r: reqs.append((r.url[-70:], r.timing.get("responseEnd"), r.frame == pg.main_frame)))
        pg.goto(url, wait_until="load", timeout=60000)
        load_t = pg.evaluate("performance.now()")
        pg.wait_for_timeout(4000)
        pre = pg.evaluate("JSON.parse(JSON.stringify(window.__d))")
        mem = pg.evaluate("performance.memory ? {used: performance.memory.usedJSHeapSize, total: performance.memory.totalJSHeapSize} : null")
        nav = pg.evaluate("(()=>{const n=performance.getEntriesByType('navigation')[0];return {dcl:Math.round(n.domContentLoadedEventEnd), load:Math.round(n.loadEventEnd)}})()")
        fcp = pg.evaluate("(performance.getEntriesByName('first-contentful-paint')[0]||{}).startTime")
        cdp = ctx.new_cdp_session(pg)
        cdp.send("Performance.enable")
        m = {x["name"]: x["value"] for x in cdp.send("Performance.getMetrics")["metrics"]}
        # scroll pass
        pg.mouse.move(w//2, h//2)
        maxy = pg.evaluate("document.documentElement.scrollHeight - innerHeight")
        n0 = len(pre["ls"]); lt0 = len(pre["lt"])
        import time; t=time.time()
        while pg.evaluate("scrollY") < maxy - 2 and time.time()-t < 120:
            pg.mouse.wheel(0, 100); pg.wait_for_timeout(30)
        pg.wait_for_timeout(1500)
        post = pg.evaluate("JSON.parse(JSON.stringify(window.__d))")
        m2 = {x["name"]: x["value"] for x in cdp.send("Performance.getMetrics")["metrics"]}
        layers = None
    finally:
        b.close()
out = {"nav": nav, "fcp": fcp, "load_t": round(load_t), "lcp": pre["lcp"], "mem_after_load": mem,
       "cls_load": round(sum(x["v"] for x in pre["ls"] if not x["input"]), 4),
       "ls_load": pre["ls"][:15],
       "cls_scroll": round(sum(x["v"] for x in post["ls"][n0:] if not x["input"]), 4),
       "ls_scroll_top": sorted(post["ls"][n0:], key=lambda x: -x["v"])[:10],
       "lt_load": pre["lt"], "lt_scroll": post["lt"][lt0:],
       "metrics_load": {k: m.get(k) for k in ["Nodes","JSHeapUsedSize","LayoutCount","RecalcStyleCount","LayoutDuration","RecalcStyleDuration","ScriptDuration","TaskDuration","Frames","Documents"]},
       "metrics_after_scroll": {k: m2.get(k) for k in ["Nodes","JSHeapUsedSize","LayoutCount","RecalcStyleCount","LayoutDuration","RecalcStyleDuration","ScriptDuration","TaskDuration","Documents"]},
       "late_requests": sorted([r for r in reqs if r[1]], key=lambda r: -r[1])[:8]}
print(json.dumps(out, indent=1, ensure_ascii=False))
