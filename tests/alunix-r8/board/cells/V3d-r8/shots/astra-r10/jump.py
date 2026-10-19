"""Fotots överkant per hjulsteg (20 px) genom tesbandet vid 390/375, ner och upp. Variant B: injicerad letter-spacing-låsning (bara mätning, filen orörd)."""
import asyncio, json, sys
from playwright.async_api import async_playwright
URL='http://localhost:3090/tests/alunix-r8/runs/V3d/index.html'
async def run(b,w,h,inject):
    pg=await (await b.new_context(viewport={'width':w,'height':h})).new_page()
    await pg.goto(URL); await pg.wait_for_timeout(1500)
    if inject: await pg.add_style_tag(content='@media (max-width:767px){.js .ts{letter-spacing:-.02em}}')
    await pg.mouse.move(w/2,h/2)
    top=await pg.evaluate("scrollY+document.querySelector('#tes').getBoundingClientRect().top")
    end=await pg.evaluate("(()=>{const e=document.querySelector('#tes');return scrollY+e.getBoundingClientRect().top+e.offsetHeight-innerHeight})()")
    while await pg.evaluate('scrollY')<top-2:
        await pg.mouse.wheel(0,min(150,top-await pg.evaluate('scrollY'))); await pg.wait_for_timeout(30)
    await pg.wait_for_timeout(1200)
    rows=[]; prev=None; shot=0
    for sgn in (1,-1):
        for i in range(600):
            y=await pg.evaluate('scrollY')
            if (sgn>0 and y>=end) or (sgn<0 and y<=top): break
            await pg.mouse.wheel(0,20*sgn); await pg.wait_for_timeout(90)
            t=await pg.evaluate("(()=>{const r=document.querySelector('.thesis-photo-box').getBoundingClientRect(),k=document.querySelector('.thesis-ticks').getBoundingClientRect();return [scrollY,Math.round(r.top),Math.round(r.height),Math.round(k.bottom)]})()")
            if prev and abs(t[1]-prev[1])>2 and not inject and shot<4:
                await pg.screenshot(path=f'jump-{w}-{"down" if sgn>0 else "up"}-{t[0]}.png'); shot+=1
            rows.append(t); prev=t
    tops=sorted(set(r[1] for r in rows)); jumps=[(a,b) for a,b in zip(rows,rows[1:]) if abs(b[1]-a[1])>2]
    print(w,'inject' if inject else 'as-is','frames',len(rows),'distinct photo tops',tops,'jumps',[(a[0],a[1],b[0],b[1]) for a,b in jumps])
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for w,h in ((390,844),(375,812)):
            for inj in (False,True): await run(b,w,h,inj)
        await b.close()
asyncio.run(m())
