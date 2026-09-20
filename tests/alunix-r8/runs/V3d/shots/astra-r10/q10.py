import asyncio
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for run in range(3):
      pg=await (await b.new_context(viewport={'width':390,'height':844})).new_page()
      await pg.goto('http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=case-horai-03')
      for t in (3000,3000,4000):
        await pg.wait_for_timeout(t)
        r=await pg.evaluate("""()=>{const f=document.querySelector('#case-horai iframe'),w=f.contentWindow,d=f.contentDocument,e=d.querySelector('#quote-text'),r=e.getBoundingClientRect();return [scrollY,Math.round(w.scrollY),w.innerHeight,Math.round(r.top),getComputedStyle(e).opacity,getComputedStyle(e).filter,d.readyState]}""")
        print(run,t,r)
      await pg.screenshot(path=f'fix-case-horai-03-390-preview-{run}.png')
    # thesis: why does ticks move 01/02 vs 03?
    pg=await (await b.new_context(viewport={'width':390,'height':844})).new_page()
    for n in (1,2,3):
      await pg.goto(f'http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=thesis-0{n}'); await pg.wait_for_timeout(2500)
      print(n, await pg.evaluate("""()=>{const L=document.querySelector('.thesis-lines'),r=L.getBoundingClientRect();return {lines:[Math.round(r.top),Math.round(r.height),getComputedStyle(L).minHeight],ts:[...document.querySelectorAll('.ts')].map(e=>{const q=e.getBoundingClientRect();return [Math.round(q.top),Math.round(q.height),getComputedStyle(e).position,getComputedStyle(e).clipPath.slice(0,22)]}),nPhoto:document.querySelectorAll('.thesis-photo-box').length}}"""))
    await b.close()
asyncio.run(m())
