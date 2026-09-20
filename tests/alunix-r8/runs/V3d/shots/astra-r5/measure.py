import asyncio, json
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
JS="""(()=>{const q=s=>document.querySelector(s);const r=s=>{const e=q(s);if(!e)return null;const b=e.getBoundingClientRect();return [Math.round(b.left),Math.round(b.top),Math.round(b.width),Math.round(b.height)]};const cs=(s,p)=>{const e=q(s);return e?getComputedStyle(e)[p]:null};
const back=[...document.querySelectorAll('.hero-plate *, .card *')].filter(e=>e.textContent.trim()==='ALUNIX'&&e.children.length==0).map(e=>[getComputedStyle(e).fontSize,Math.round(e.getBoundingClientRect().width)]);
return {y:scrollY,back,card:r('.hero-plate')||r('.card'),thesisH:cs('.thesis-headline','fontSize'),thesis:r('.panel-thesis'),thesisFig:r('.thesis-figure'),giant:r('.panel-giant'),giantH:cs('.panel-giant h2','fontSize'),giantHr:r('.panel-giant h2'),chapter:r('.process-chapter'),ptitle:cs('.process-title','fontSize'),ptitleR:r('.process-title'),chapterBg:cs('#process','backgroundColor'),sheet:r('.process-sheet'),live:r('.process-sheet .p-live'),liveImg:r('#p-live-img'),rev:r('#p-rev'),revOp:cs('#p-rev','opacity'),ledOp:cs('#p-ledgers','opacity'),hatchOp:cs('#p-hatch','opacity'),crow:r('#p-c-row'),
horai:(()=>{const f=q('.horai-wrap iframe');if(!f)return null;try{const D=f.contentDocument;return [Math.round(f.getBoundingClientRect().width),D.documentElement.scrollWidth]}catch(e){return String(e)}})(),docW:document.documentElement.scrollWidth}})()"""
async def main():
  out={}
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(1440,900),(390,844)]:
      for m in ["","?preview=back","?preview=ledger","?preview=process-04","?preview=process-05","?preview=process-06","?preview=process-07"]:
        pg=await b.new_page(viewport={"width":w,"height":h}); await pg.goto(URL+m,wait_until="load"); await pg.wait_for_timeout(3000)
        out[f"{w}{m or 'top'}"]=await pg.evaluate(JS); await pg.close()
    await b.close()
  print(json.dumps(out,indent=0))
asyncio.run(main())
