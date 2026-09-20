import asyncio,json
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':390,'height':844})
    await pg.goto('http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=case-horai-03'); await pg.wait_for_timeout(5000)
    r=await pg.evaluate("""()=>{const f=document.querySelector('#case-horai iframe');const d=f.contentDocument;const q=s=>{const e=d.querySelector(s);if(!e)return null;const r=e.getBoundingClientRect();return [Math.round(r.top),Math.round(r.bottom),Math.round(r.left),Math.round(r.right)]};
      return {iw:f.contentWindow.innerWidth,ih:f.contentWindow.innerHeight,nav:q('nav')||q('header'),kicker:q('#quote-kicker'),jp:q('#quote-jp'),text:q('#quote-text'),sticky:q('#quote-section .sticky'),col:q('#quote-section .sticky > div'),sec:q('#quote-section')}}""")
    print(json.dumps(r)); await b.close()
asyncio.run(m())
