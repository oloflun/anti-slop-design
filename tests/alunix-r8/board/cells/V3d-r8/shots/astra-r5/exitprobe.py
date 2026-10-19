import asyncio
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1440,"height":900}); await pg.goto(URL,wait_until="load"); await pg.wait_for_timeout(1500); await pg.mouse.move(720,450)
    for y in range(13980,14240,20):
      for _ in range(400):
        d=y-await pg.evaluate("scrollY")
        if abs(d)<2: break
        await pg.mouse.wheel(0,max(-120,min(120,d))); await pg.wait_for_timeout(40)
      await pg.wait_for_timeout(900)
      print(await pg.evaluate("""(()=>{const li=document.querySelector('.process-steps li[data-step="07"]');const band=li.querySelector('.step-band')||li;const cs=getComputedStyle(band);const r=band.getBoundingClientRect();const st=document.querySelector('.process-stick').getBoundingClientRect();const ps=getComputedStyle(document.querySelector('#process')).getPropertyValue('--sc-ps');return {y:scrollY,ps,band:[Math.round(r.top),Math.round(r.height)],clip:cs.clipPath,stick:Math.round(st.top),slit:cs.getPropertyValue('--slit-p')}})()"""))
    await b.close()
asyncio.run(main())
