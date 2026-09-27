import sys, json
sys.path.insert(0, r"C:/Users/Anton L/anti-slop-design/tests/alunix-r8")
from showcase_probe import single_flight
from playwright.sync_api import sync_playwright
single_flight()
url = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, channel="chromium", args=["--enable-gpu","--ignore-gpu-blocklist","--use-angle=d3d11"])
    try:
        pg = b.new_page(viewport={"width":1440,"height":900}); pg.goto(url, wait_until="load"); pg.wait_for_timeout(2000)
        pg.evaluate("window.__lenis.scrollTo('#exempelcase',{immediate:true})"); pg.wait_for_timeout(1500)
        tgt = pg.evaluate("(()=>{const r=document.getElementById('showcase').getBoundingClientRect();return Math.round(r.top+scrollY)})()")
        pg.evaluate("""window.__ys=[];let t0=performance.now();(function f(){window.__ys.push([Math.round(performance.now()-t0),Math.round(scrollY)]); if(performance.now()-t0<3000) requestAnimationFrame(f)})()""")
        pg.evaluate("document.querySelector('button.case-choice[data-case=horai]').click()")
        pg.wait_for_timeout(3200)
        ys = pg.evaluate("window.__ys")
    finally: b.close()
d = [ys[i+1][1]-ys[i][1] for i in range(len(ys)-1)]
i=max(range(len(d)),key=lambda k:d[k]) if d else 0
print("max step at t=%sms dt=%sms y %s->%s" % (ys[i+1][0], ys[i+1][0]-ys[i][0], ys[i][1], ys[i+1][1]))
print("showcase top", tgt, "| y at 0/300/700/1400/2500 ms:", [next((y for t,y in ys if t>=m), ys[-1][1]) for m in (0,300,700,1400,2500)], "| max step", max(d) if d else 0)
