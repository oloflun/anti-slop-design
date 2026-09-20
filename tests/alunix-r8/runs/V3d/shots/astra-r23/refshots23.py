"""astra-r23: referensbilder ur hyperborea/horai - hur de gar in i ett nytt kapitel."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
OUT = Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3d\shots\astra-r23")
SITES = {"hyp":"http://localhost:3090/sites/hyperborea.html",
         "hor":"http://localhost:3090/sites/horai.html"}
async def main():
    async with async_playwright() as p:
        br = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for tag,url in SITES.items():
            for w,h in ((1920,930),(390,844)):
                ctx = await br.new_context(viewport={"width":w,"height":h})
                pg = await ctx.new_page()
                await pg.goto(url, wait_until="load", timeout=40000)
                await pg.wait_for_timeout(2500)
                dh = await pg.evaluate("document.documentElement.scrollHeight")
                await pg.mouse.move(w/2,h/2)
                n = 9
                for i in range(n):
                    tgt = int((dh-h)*i/(n-1))
                    for _ in range(2000):
                        cur = await pg.evaluate("scrollY")
                        d = tgt-cur
                        if abs(d)<3: break
                        await pg.mouse.wheel(0, max(-200,min(200,d)))
                        await pg.wait_for_timeout(16)
                    await pg.wait_for_timeout(1400)
                    await pg.screenshot(path=str(OUT/f"REF-{tag}-{w}-{i}.png"))
                    print(tag,w,i,tgt,flush=True)
                await ctx.close()
        await br.close()
asyncio.run(main())
