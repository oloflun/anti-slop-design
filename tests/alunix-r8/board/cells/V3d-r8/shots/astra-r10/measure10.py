"""astra-r10: r8-fixarna 1-3 vid 390 och 375, i preview och med mouse.wheel från toppen. Plus hscroll 320-1920."""
import asyncio, json
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
R = "e=>{if(!e)return null;const r=e.getBoundingClientRect();return {t:Math.round(r.top),b:Math.round(r.bottom),l:Math.round(r.left),r:Math.round(r.right),h:Math.round(r.height)}}"
THESIS = f"""()=>{{const q={R};const ts=[...document.querySelectorAll('.ts')].find(e=>getComputedStyle(e).clipPath.startsWith('inset(0%'));
 return {{y:scrollY,photo:q(document.querySelector('.thesis-photo-box')),img:q(document.querySelector('.thesis-photo-box img')),objpos:getComputedStyle(document.querySelector('.thesis-photo-box img')).objectPosition,
  ticks:q(document.querySelector('.thesis-ticks')),ts:q(ts),cap:q(document.querySelector('.thesis-caption')),stage:q(document.querySelector('.thesis-stage')),hs:document.documentElement.scrollWidth-innerWidth}}}}"""
FRAME = f"""(sel)=>{{const q={R};const f=document.querySelector(sel+' iframe');const d=f.contentDocument,w=f.contentWindow;
 const g=e=>e?{{...q(e),op:getComputedStyle(e).opacity,filter:getComputedStyle(e).filter}}:null;
 const fig=d.querySelector('#studio + section figure');
 return {{y:scrollY,frame:q(f),ih:w.innerHeight,fy:Math.round(w.scrollY),header:q(d.querySelector('header')),
  quoteText:g(d.querySelector('#quote-text')),quoteJp:g(d.querySelector('#quote-jp')),author:g(d.querySelector('#quote-author')),
  fig1:q(fig),cap1:q(fig&&fig.querySelector('figcaption')),hs:document.documentElement.scrollWidth-innerWidth}}}}"""
async def wheel_to(pg, y):
    await pg.mouse.move(pg.viewport_size['width']/2, pg.viewport_size['height']/2)
    for _ in range(1500):
        d = y - await pg.evaluate("scrollY")
        if abs(d) < 2: break
        await pg.mouse.wheel(0, max(-120, min(120, d))); await pg.wait_for_timeout(40)
    await pg.wait_for_timeout(4000)
async def main():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w, h in [(390, 844), (375, 812)]:
            o = out[w] = {}
            for name, fn, arg in [(f"thesis-0{n}", THESIS, None) for n in range(1, 6)] + [("case-horai-03", FRAME, "#case-horai"), ("case-calyx-03", FRAME, "#case-calyx")]:
                ctx = await b.new_context(viewport={'width': w, 'height': h}); pg = await ctx.new_page()
                await pg.goto(URL + "?preview=" + name); await pg.wait_for_timeout(5000)
                pv = await (pg.evaluate(fn, arg) if arg else pg.evaluate(fn))
                ty = pv['y']
                await pg.goto(URL); await pg.wait_for_timeout(2000)
                await wheel_to(pg, ty)
                wh = await (pg.evaluate(fn, arg) if arg else pg.evaluate(fn))
                await pg.screenshot(path=f"fix-{name}-{w}-wheel.png")
                o[name] = {"preview": pv, "wheel": wh}
                await ctx.close()
        hs = {}
        for w in (320, 375, 390, 414, 768, 1024, 1280, 1440, 1920):
            ctx = await b.new_context(viewport={'width': w, 'height': 900}); pg = await ctx.new_page()
            await pg.goto(URL); await pg.wait_for_timeout(1500)
            H = await pg.evaluate("document.documentElement.scrollHeight")
            mx = 0
            for y in range(0, H, 900):
                await pg.evaluate(f"scrollTo(0,{y})"); await pg.wait_for_timeout(60)
                mx = max(mx, await pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth"))
            hs[w] = mx; await ctx.close()
        out['hscroll'] = hs
        await b.close()
    open('measure10.json', 'w').write(json.dumps(out, indent=1))
    print(json.dumps(out['hscroll']))
asyncio.run(main())
