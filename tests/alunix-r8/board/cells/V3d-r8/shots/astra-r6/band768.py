import asyncio, json
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=process-07"
JS=r"""(()=>{const lis=[...document.querySelectorAll('.process-steps > li')];return lis.map(li=>{const b=li.querySelector('.step-band');const R=s=>{const e=b.querySelector(s);const r=e.getBoundingClientRect();return [Math.round(r.left),Math.round(r.top-b.getBoundingClientRect().top),Math.round(r.right),Math.round(r.bottom-b.getBoundingClientRect().top)]};const n=R('.ledger-num'),p=R('.process-p'),t=R('.process-step-title'),no=R('.process-note');const ov=(a,c)=>a[0]<c[2]&&c[0]<a[2]&&a[1]<c[3]&&c[1]<a[3];return {step:li.dataset.step,num:n,title:t,note:no,p:p,numXp:ov(n,p),noteXp:ov(no,p),titleXp:ov(t,p),pRow:getComputedStyle(b.querySelector('.process-p')).gridRow}})})()"""
async def main():
  async with async_playwright() as pw:
    b=await pw.chromium.launch()
    for w in [768,900,1023,1024]:
      pg=await b.new_page(viewport={"width":w,"height":1024}); await pg.goto(URL,wait_until="load"); await pg.wait_for_timeout(2000)
      r=await pg.evaluate(JS); print(w,json.dumps([x for x in r if x['step'] in ('01','04','07')])); await pg.close()
    await b.close()
asyncio.run(main())
