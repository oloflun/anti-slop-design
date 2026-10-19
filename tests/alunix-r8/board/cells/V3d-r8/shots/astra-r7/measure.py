import asyncio, json
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
JS="""()=>{const q=s=>{const e=document.querySelector(s);if(!e)return null;const r=e.getBoundingClientRect();return {x:Math.round(r.left),y:Math.round(r.top),w:Math.round(r.width),h:Math.round(r.height),fs:getComputedStyle(e).fontSize}};
return {vw:innerWidth,vh:innerHeight,stage:q('.thesis-stage'),photo:q('.thesis-photo-box'),lines:q('.thesis-lines'),ts3:q('.ts[style*="--i:3"]'),ticks:q('.thesis-ticks')}}"""
JS2="""(sel)=>{const s=document.querySelector(sel);const q=e=>{const r=e.getBoundingClientRect();return {x:Math.round(r.left),y:Math.round(r.top),w:Math.round(r.width),h:Math.round(r.height),fs:getComputedStyle(e).fontSize}};
return {wrap:q(s.querySelector('.case-wrap')),title:q(s.querySelector('.case-title')),text:q(s.querySelector('.case-text')),h3:q(s.querySelector('.cs h3')),p:q(s.querySelector('.cs p')),steps:q(s.querySelector('.case-steps'))}}"""
async def main():
  out={}
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(1440,900),(768,1024),(390,844)]:
      pg=await (await b.new_context(viewport={'width':w,'height':h})).new_page()
      await pg.goto(URL+'?preview=thesis-04');await pg.wait_for_timeout(3000)
      out[f't{w}']=await pg.evaluate(JS)
      for m,sel in [('case-calyx-03','#case-calyx'),('case-horai-03','#case-horai')]:
        await pg.goto(URL+'?preview='+m);await pg.wait_for_timeout(3500)
        out[f'{m}-{w}']=await pg.evaluate(JS2,sel)
      await pg.goto(URL+'?preview=cases');await pg.wait_for_timeout(2500)
      out[f'cases-{w}']=await pg.evaluate("()=>{const r=document.querySelector('.cases-title').getBoundingClientRect();return {fs:getComputedStyle(document.querySelector('.cases-title')).fontSize,y:r.top,h:r.height}}")
      await pg.goto(URL+'?preview=bridge');await pg.wait_for_timeout(2500)
      out[f'bridge-{w}']=await pg.evaluate("()=>getComputedStyle(document.querySelector('.bridge-title')).fontSize")
    await b.close()
  print(json.dumps(out,indent=0))
asyncio.run(main())
