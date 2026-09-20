"""astra-r22: kostar det nya ::after nagot per bildruta? Det interpolerar inset()
med --tx, alltsa en layout av pseudoelementet varje bildruta genom hela akten.
A/B: samma svep genom tes -> ritning med och utan .tes-plane::after.
Matt: langa uppgifter (>50ms) och rAF-deltan under svepet. Argument: bredd hojd.
"""
import asyncio, json, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"

HOOK = """() => {
  window.__lt = []; window.__d = [];
  new PerformanceObserver(l => { for (const e of l.getEntries()) window.__lt.push(Math.round(e.duration)); })
    .observe({entryTypes:['longtask']});
  let prev = performance.now();
  (function tick(t){ window.__d.push(t - prev); prev = t; requestAnimationFrame(tick); })(prev);
}"""


async def run(b, w, h, off):
    pg = await b.new_page(viewport={'width': w, 'height': h})
    await pg.goto(URL, wait_until='load')
    await pg.wait_for_timeout(3000)
    if off:
        await pg.add_style_tag(content='.tes-plane::after{display:none!important;}')
    await pg.mouse.move(w/2, h/2)
    y0 = await pg.evaluate("(()=>{const t=document.getElementById('tes');return t.getBoundingClientRect().top+scrollY+t.offsetHeight-2.2*innerHeight})()")
    y1 = await pg.evaluate("(()=>{const t=document.getElementById('process');return t.getBoundingClientRect().top+scrollY+1.2*innerHeight})()")
    while await pg.evaluate("scrollY") < y0 - 2:
        await pg.mouse.wheel(0, 240)
        await pg.wait_for_timeout(18)
    await pg.wait_for_timeout(900)
    await pg.evaluate(HOOK)
    n = 0
    while n < 400 and await pg.evaluate("scrollY") < y1:
        await pg.mouse.wheel(0, 20)
        await pg.wait_for_timeout(16)
        n += 1
    await pg.wait_for_timeout(600)
    d = await pg.evaluate("({lt:window.__lt, d:window.__d.slice(1)})")
    await pg.close()
    ds = sorted(d['d'])
    p = lambda q: round(ds[min(len(ds)-1, int(len(ds)*q))], 2) if ds else None
    return {'frames': n, 'rafs': len(ds), 'long': d['lt'], 'longN': len(d['lt']),
            'p50': p(.5), 'p90': p(.9), 'p99': p(.99), 'max': round(ds[-1], 2) if ds else None,
            'over25ms': sum(1 for x in ds if x > 25)}


async def main():
    w, h = int(sys.argv[1]), int(sys.argv[2])
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for label, off in (('real', False), ('nocontour', True)):
            out[label] = await run(b, w, h, off)
            print(w, label, out[label], flush=True)
        await b.close()
    open('cost22-%d.json' % w, 'w').write(json.dumps(out, indent=1))

asyncio.run(main())
