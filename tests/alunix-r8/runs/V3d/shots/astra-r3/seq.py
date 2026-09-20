import asyncio,sys
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
w,h,y0,y1,st,tag=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),sys.argv[6]
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":w,"height":h})
    await pg.goto(URL,wait_until="load"); await pg.wait_for_timeout(1500)
    await pg.mouse.move(w/2,h/2)
    y=y0
    while True:
      for _ in range(300):
        d=y-await pg.evaluate("scrollY")
        if abs(d)<2: break
        await pg.mouse.wheel(0,max(-120,min(120,d))); await pg.wait_for_timeout(40)
      await pg.wait_for_timeout(1200)
      info=await pg.evaluate("""(()=>{const s=document.querySelector('.process-sheet'),t=document.getElementById('p-title');const r=s&&s.getBoundingClientRect(),q=t&&t.getBoundingClientRect();const cs=getComputedStyle(document.querySelector('#process'));return {y:scrollY,ps:cs.getPropertyValue('--sc-ps'),sheet:r&&[r.left|0,r.top|0,r.right|0,r.bottom|0],title:q&&[q.left|0,q.top|0,q.right|0,q.bottom|0],k7:cs.getPropertyValue('--k7')}})()""")
      print(info,flush=True)
      await pg.screenshot(path=f"seq-{tag}-{int(info['y'])}.png")
      if y>=y1: break
      y+=st
    await b.close()
asyncio.run(main())
