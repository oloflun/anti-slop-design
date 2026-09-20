"""Nar far Horai-ramen sin src (fix 3, R19), och var ligger den langa uppgiften?"""
import asyncio, json, sys
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
INIT = r"""
window.__ev=[];
new PerformanceObserver(l=>{for(const e of l.getEntries())if(e.duration>50)window.__ev.push({t:'lt',s:e.startTime,d:e.duration,a:(e.attribution||[]).map(a=>a.containerSrc||a.containerName||a.name),y:scrollY})}).observe({type:'longtask',buffered:true});
addEventListener('DOMContentLoaded',()=>{
  const f=document.querySelector('#case-horai iframe');
  if(!f) return;
  new MutationObserver(ms=>{for(const m of ms) if(m.attributeName==='src'||m.attributeName==='data-src')
    window.__ev.push({t:'attr',n:m.attributeName,s:performance.now(),y:scrollY,
      cur:(window.__scSmooth&&window.__scSmooth.acts||[]).filter(a=>a.el&&a.el.id==='case-calyx').map(a=>a.cur)[0]});
  }).observe(f,{attributes:true,attributeFilter:['src','data-src']});
});
"""
async def main():
    w,h=int(sys.argv[1]),int(sys.argv[2])
    async with async_playwright() as p:
        b=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg=await b.new_page(viewport={'width':w,'height':h})
        await pg.add_init_script(INIT)
        await pg.goto(URL); await pg.wait_for_timeout(4000)
        await pg.mouse.move(w/2,h/2)
        H=await pg.evaluate("document.documentElement.scrollHeight-innerHeight")
        while await pg.evaluate("scrollY")<H-2:
            await pg.mouse.wheel(0,120); await pg.wait_for_timeout(50)
        await pg.wait_for_timeout(1500)
        print(json.dumps(await pg.evaluate("window.__ev"),indent=1))
        await b.close()
asyncio.run(main())
