"""Click on the Hōrai case button and record the scroll glide, one rAF per sample.

    python click_scroll_probe.py URL [--scenario wait|fast] [--runs N] [--trace OUT.json]

wait: jump to #exempelcase, wait 1.5 s, click (the lead's original scenario).
fast: jump to #exempelcase, click 250 ms after the picker is reached (R7b).
Pass = arrived (within 2 px of the glide's end) inside 2.0 s, largest step
<= 60 px, and no frame longer than 100 ms during the first 2 s after the click.
--trace OUT.json writes one CDP trace per run (OUT-1.json, ...) from the jump on.
Always headless.
"""
import sys, json, argparse
sys.path.insert(0, r"C:/Users/Anton L/anti-slop-design/tests/alunix-r8")
from showcase_probe import single_flight
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("url")
ap.add_argument("--scenario", choices=["wait", "fast"], default="wait")
ap.add_argument("--runs", type=int, default=1)
ap.add_argument("--trace")
a = ap.parse_args()
WAIT_MS = {"wait": 1500, "fast": 250}[a.scenario]
CATS = ["devtools.timeline", "disabled-by-default-devtools.timeline", "toplevel", "blink.user_timing",
        "v8.execute", "disabled-by-default-devtools.timeline.frame", "loading",
        "gpu", "disabled-by-default-gpu.service", "skia.gpu", "disabled-by-default-skia.gpu", "viz"]

single_flight()


def one(p, trace):
    b = p.chromium.launch(headless=True, channel="chromium", args=["--enable-gpu", "--ignore-gpu-blocklist", "--use-angle=d3d11"])
    try:
        pg = b.new_page(viewport={"width": 1440, "height": 900}); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)[:120])); pg.on("console", lambda m: m.type == "error" and not m.text.startswith("Failed to load resource") and errs.append(m.text[:120]))
        pg.on("response", lambda r: r.status >= 400 and errs.append("%d %s" % (r.status, r.url[-80:])))
        pg.goto(a.url, wait_until="load"); pg.wait_for_timeout(2000)
        pg.evaluate("""(()=>{window.__ev=[];const C=window.__CASES;for(const k in C){C[k].iframe.addEventListener('load',()=>__ev.push([k+':load',Math.round(performance.now())]));
          new MutationObserver(()=>__ev.push([k+':src',Math.round(performance.now())])).observe(C[k].iframe,{attributes:true,attributeFilter:['src']});}})()""")
        if trace: b.start_tracing(page=pg, categories=CATS)
        pg.evaluate("window.__jumpAt=performance.now();window.__lenis.scrollTo('#exempelcase',{immediate:true})"); pg.wait_for_timeout(WAIT_MS)
        tgt = pg.evaluate("(()=>{const r=document.getElementById('showcase').getBoundingClientRect();return Math.round(r.top+scrollY-(parseFloat(getComputedStyle(document.getElementById('showcase')).scrollMarginTop)||0))})()")
        pg.evaluate("""window.__ys=[];let t0=performance.now();window.__clickAt=t0;(function f(){window.__ys.push([Math.round(performance.now()-t0),Math.round(scrollY)]); if(performance.now()-t0<3000) requestAnimationFrame(f)})()""")
        pg.evaluate("performance.mark('probe-click');document.querySelector('button.case-choice[data-case=horai]').click()")
        pg.wait_for_timeout(3200)
        ys, ev, t0, jump = pg.evaluate("[window.__ys, window.__ev, window.__clickAt, window.__jumpAt]")
        if trace:
            open(trace, "wb").write(b.stop_tracing())
    finally:
        b.close()
    ev = [(n, round(t - t0)) for n, t in ev]
    return ys, tgt, ev, round(t0 - jump), errs


res = []
with sync_playwright() as p:
    for r in range(a.runs):
        ys, tgt, ev, lag, errs = one(p, a.trace.replace(".json", "-%d.json" % (r+1)) if a.trace else None)
        d = [ys[i+1][1]-ys[i][1] for i in range(len(ys)-1)]
        dt = [(ys[i+1][0], ys[i+1][0]-ys[i][0]) for i in range(len(ys)-1)]
        end = ys[-1][1]
        arrive = next((t for t, y in ys if abs(y - tgt) <= 2), None)
        maxstep = max(d) if d else 0
        maxframe = max((x for t, x in dt if t <= 2000), default=0)
        after = max((x for t, x in dt if t > 2000), default=0)  # reported, not gated
        ok = arrive is not None and arrive <= 2000 and maxstep <= 60 and maxframe <= 100 and not errs
        res.append(ok)
        print("run %d [%s, click %d ms after jump] %s | arrive %s ms | max step %d px | max frame %d ms (first 2 s), %d ms (2-3.2 s) | y at 0/300/700/1400/2000 ms: %s | last y %d (glide target %d) | events: %s" % (
            r+1, a.scenario, lag, "PASS" if ok else "FAIL", arrive, maxstep, maxframe, after,
            [next((y for t, y in ys if t >= m), ys[-1][1]) for m in (0, 300, 700, 1400, 2000)], end, tgt, ev) + (" | ERRORS: %s" % errs if errs else ""))
print("%s: %d/%d pass" % (a.scenario, sum(res), len(res)))
sys.exit(0 if all(res) else 1)
