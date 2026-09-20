import asyncio,json
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':390,'height':844})
    await pg.goto('http://localhost:3090/sites/horai.html'); await pg.set_viewport_size({'width':390,'height':450}); await pg.wait_for_timeout(2500)
    for s in [0,100,200,272,320]:
      r=await pg.evaluate("""async(s)=>{const sec=document.getElementById('quote-section');const top=sec.offsetTop;const y=top+(sec.offsetHeight-innerHeight)/2 - s;scrollTo(0,y);await new Promise(r=>setTimeout(r,800));
        const g=id=>{const e=document.getElementById(id),c=getComputedStyle(e),r=e.getBoundingClientRect();return [c.opacity,c.filter,Math.round(r.top),Math.round(r.bottom)]};return {s,jp:g('quote-jp'),tx:g('quote-text')}}""",s)
      print(json.dumps(r))
    await b.close()
asyncio.run(m())
