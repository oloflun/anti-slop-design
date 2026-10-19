import asyncio, json, sys
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
JS="""(sel)=>[...document.querySelectorAll(sel+' .cs')].slice(0,2).map(li=>{const h=li.querySelector('h3'),p=li.querySelector('p');const cs=getComputedStyle(li),hs=getComputedStyle(h);const r=h.getBoundingClientRect(),pr=p.getBoundingClientRect();
return {i:li.style.cssText,clip:cs.clipPath,tf:cs.transform,in_:cs.getPropertyValue('--in'),out:cs.getPropertyValue('--out'),ps:getComputedStyle(li.closest('section')||li).getPropertyValue('--sc-ps'),h3:{t:r.top,b:r.bottom,h:r.height,color:hs.color,op:hs.opacity,vis:hs.visibility,disp:hs.display,fs:hs.fontSize},p:{t:pr.top,b:pr.bottom},li:li.getBoundingClientRect().top,
hit:(document.elementFromPoint(r.left+10,r.top+r.height/2)||{}).className}})"""
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(390,844),(1440,900)]:
      for m,sel in [("case-horai-01","#case-horai"),("case-calyx-01","#case-calyx")]:
        pg=await b.new_page(viewport={'width':w,'height':h})
        await pg.goto(URL+"?preview="+m); await pg.wait_for_timeout(5000)
        print(w,m,json.dumps(await pg.evaluate(JS,sel),indent=0))
        await pg.close()
    await b.close()
asyncio.run(main())
