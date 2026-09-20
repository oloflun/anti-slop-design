import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':390,'height':844})
        await pg.goto("http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=case-horai-03"); await pg.wait_for_timeout(4000)
        print(await pg.evaluate("""(()=>{const c=document.querySelector('#case-horai .case-line');const cs=getComputedStyle(c);return {gtr:cs.gridTemplateRows,op:cs.opacity,mt:cs.marginTop,h:c.getBoundingClientRect().height,out:cs.getPropertyValue('--out'),supports:CSS.supports('grid-template-rows','calc(0.5 * 1fr)')}})()"""))
        await b.close()
asyncio.run(main())
