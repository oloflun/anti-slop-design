import asyncio
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
async def wheel(pg,y):
  for _ in range(400):
    d=y-await pg.evaluate("scrollY")
    if abs(d)<2: break
    await pg.mouse.wheel(0,max(-120,min(120,d))); await pg.wait_for_timeout(40)
  await pg.wait_for_timeout(2000)
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    pg=await b.new_page(viewport={"width":1440,"height":900}); await pg.goto(URL,wait_until="load"); await pg.wait_for_timeout(1500); await pg.mouse.move(720,450)
    for y in [3700,4000,4330,4600]:
      await wheel(pg,y)
      r=await pg.evaluate("(()=>{const g=document.querySelector('.panel-giant').getBoundingClientRect();const t=document.querySelector('.panel-thesis').getBoundingClientRect();const c=document.querySelector('.calyx-wrap').getBoundingClientRect();return {y:scrollY,giant:[g.left|0,g.top|0,g.width|0,g.height|0],thesis:[t.top|0,t.bottom|0],calyx:[c.left|0,c.top|0,c.bottom|0]}})()")
      print(r); await pg.screenshot(path=f"giant-wheel-{y}.png")
    await pg.close()
    pg=await b.new_page(viewport={"width":390,"height":844}); await pg.goto(URL,wait_until="load"); await pg.wait_for_timeout(1500); await pg.mouse.move(195,400)
    await wheel(pg,4819); await pg.wait_for_timeout(4000)
    print(await pg.evaluate("(()=>{const f=document.querySelector('.horai-wrap iframe');let d=null;try{const D=f.contentDocument;d={ready:D.readyState,sw:D.documentElement.scrollWidth,cw:D.documentElement.clientWidth}}catch(e){d=String(e)};return {src:f.getAttribute('src')||f.dataset.src,w:f.getBoundingClientRect().width,d}})()"))
    await pg.screenshot(path="P05-390-settled.png")
    await b.close()
asyncio.run(main())
