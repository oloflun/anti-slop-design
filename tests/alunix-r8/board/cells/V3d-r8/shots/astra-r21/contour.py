"""Vad ritar de tva ljusa 2px-raderna vid det klippta planets over- och underkant?
Kor samma preview-lage tva ganger: en gang orort, en gang med box-shadow:none."""
import asyncio, sys
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=tes-till-ritning-3"
async def shot(p,w,h,css,path):
    b=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
    pg=await b.new_page(viewport={'width':w,'height':h})
    await pg.goto(URL); await pg.wait_for_timeout(3500)
    if css: await pg.add_style_tag(content=css); await pg.wait_for_timeout(400)
    g=await pg.evaluate("""()=>{const e=document.querySelector('.tes-plane');const r=e.getBoundingClientRect();
      const cs=getComputedStyle(e);return {rect:[r.left,r.top,r.right,r.bottom],clip:cs.clipPath,shadow:cs.boxShadow}}""")
    await pg.screenshot(path=path)
    print(path,g)
    await b.close()
async def main():
    async with async_playwright() as p:
        await shot(p,1920,930,None,'contour-on.png')
        await shot(p,1920,930,'.tes-plane{box-shadow:none!important;}','contour-off.png')
asyncio.run(main())
