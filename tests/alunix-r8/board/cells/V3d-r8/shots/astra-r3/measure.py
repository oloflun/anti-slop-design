import asyncio
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
JS="""(()=>{const q=s=>document.querySelector(s);const r=s=>{const e=q(s);if(!e)return null;const b=e.getBoundingClientRect();return [b.left|0,b.top|0,b.width|0,b.height|0]};const fs=s=>{const e=q(s);return e?getComputedStyle(e).fontSize:null};
return {y:scrollY,hero:fs('.hero-headline'),thesisH:fs('.panel-thesis h2')||fs('.panel-thesis h3'),thesisFig:r('.thesis-figure'),backWord:(()=>{const c=[...document.querySelectorAll('.hero-plate *')].filter(e=>e.textContent.trim()==='ALUNIX'&&e.children.length==0);return c.map(e=>getComputedStyle(e).fontSize)})(),giant:r('.panel-giant'),giantH:fs('.panel-giant h2'),principlesP:fs('.principles .ledger-body p'),kicker:fs('.principles > .kicker-sans'),lead:r('.process-lead'),leadMB:q('.process-lead')&&getComputedStyle(q('.process-lead')).marginBottom,sheet:r('.process-sheet'),live:r('.process-sheet .p-live'),liveFilter:q('.process-sheet .p-live')&&getComputedStyle(q('.process-sheet .p-live')).filter,title:r('#p-title'),horai:r('.horai-wrap'),horaiIframe:(()=>{const f=q('.horai-wrap iframe');return f?[f.getBoundingClientRect().width|0,f.style.transform||getComputedStyle(f).transform]:null})()}})()"""
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(1440,900),(390,844)]:
      for m in ["", "?preview=back","?preview=ledger","?preview=process-04","?preview=process-06","?preview=process-07"]:
        pg=await b.new_page(viewport={"width":w,"height":h}); await pg.goto(URL+m,wait_until="load"); await pg.wait_for_timeout(2500)
        print(w,m or 'top',await pg.evaluate(JS)); await pg.close()
    await b.close()
asyncio.run(main())
