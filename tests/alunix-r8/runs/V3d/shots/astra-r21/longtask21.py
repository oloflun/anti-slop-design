"""astra-r18: long tasks (>50ms) under ett helt hjulsvep, 120 px/steg, med scrollY och sektion vid uppgiften."""
import asyncio, json, sys
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
INIT = r"""
window.__lt=[];window.__ys=[];
(function tick(t){window.__ys.push([performance.now(),scrollY]);requestAnimationFrame(tick)})();
new PerformanceObserver(l=>{for(const e of l.getEntries())window.__lt.push({s:e.startTime,d:e.duration,a:(e.attribution||[]).map(a=>a.containerSrc||a.containerName||a.name)})}).observe({type:'longtask',buffered:true});
"""
SECT = r"""(y)=>{const ids=[...document.querySelectorAll('body > *, main > section, section[id], header, footer')].filter(e=>e.id);
 let best=null;for(const e of ids){const t=e.getBoundingClientRect().top+scrollY;if(t<=y+innerHeight/2&&(!best||t>best[1]))best=[e.id,t];}return best?best[0]:'?'}"""


async def main():
    w, h = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1440, 900)
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.add_init_script(INIT)
        await pg.goto(URL); await pg.wait_for_timeout(4000)
        await pg.evaluate("window.__lt=[]")
        t0 = await pg.evaluate("performance.now()")
        await pg.mouse.move(w / 2, h / 2)
        H = await pg.evaluate("document.documentElement.scrollHeight-innerHeight")
        while await pg.evaluate("scrollY") < H - 2:
            await pg.mouse.wheel(0, 120); await pg.wait_for_timeout(50)
        await pg.wait_for_timeout(1500)
        lt = await pg.evaluate("window.__lt"); ys = await pg.evaluate("window.__ys")
        res = []
        for e in lt:
            if e['s'] < t0: continue
            y = min(ys, key=lambda r: abs(r[0] - e['s']))[1]
            res.append({'start': round(e['s'] - t0), 'dur': round(e['d']), 'y': y, 'sect': await pg.evaluate(SECT, y), 'attr': e['a']})
        print(json.dumps({'vp': [w, h], 'n': len(res), 'tasks': res}, ensure_ascii=False, indent=1))
        await b.close()

asyncio.run(main())
