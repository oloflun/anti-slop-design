"""Glappet mellan de tva arken: scrollintervall dar VARKEN .tes-plane (synlig del)
eller .process-sheet syns i viewporten, plus vad som da star pa skarmen."""
import asyncio, sys
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
JS=r"""()=>{
  function ins(cs,w,h){const m=/inset\(([^)]+)\)/.exec(cs.clipPath);if(!m)return[0,0,0,0];
    const r=m[1].trim().split(/\s+/);let a=r.map(parseFloat);
    if(r.length===1)a=[a[0],a[0],a[0],a[0]];else if(r.length===2)a=[a[0],a[1],a[0],a[1]];
    else if(r.length===3)a=[a[0],a[1],a[2],a[1]];
    const p=r.map(t=>t.endsWith('%'));
    return a.map((x,i)=>p[Math.min(i,p.length-1)]? x/100*(i%2?w:h):x);}
  const vh=innerHeight;
  const e=document.querySelector('.tes-plane'); const r=e.getBoundingClientRect();
  const v=ins(getComputedStyle(e),r.width,r.height);
  const P={t:r.top+v[0],b:r.bottom-v[2]};
  const s=document.querySelector('.process-sheet'); const sr=s.getBoundingClientRect();
  const seam=[...document.querySelectorAll('.seam i')].map(i=>{const q=i.getBoundingClientRect();
    const w2=ins(getComputedStyle(i),q.width,q.height);return {t:q.top+w2[0],b:q.bottom-w2[2]};})
    .filter(o=>o.b-o.t>1 && o.b>0 && o.t<vh);
  const planeVis = P.b>0 && P.t<vh && (P.b-P.t)>8;
  const sheetVis = sr.bottom>0 && sr.top<vh && sr.height>8;
  return {y:scrollY, planeVis, sheetVis, seamVis:seam.length>0,
          planeH: Math.round(Math.min(vh,P.b)-Math.max(0,P.t)),
          sheetH: Math.round(Math.min(vh,sr.bottom)-Math.max(0,sr.top))};
}"""
async def main():
    w,h=int(sys.argv[1]),int(sys.argv[2])
    async with async_playwright() as p:
        b=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg=await b.new_page(viewport={'width':w,'height':h})
        await pg.goto(URL); await pg.wait_for_timeout(3000)
        await pg.mouse.move(w/2,h/2)
        y0=await pg.evaluate("(()=>{const t=document.getElementById('process');return t.getBoundingClientRect().top+scrollY-innerHeight})()")
        while await pg.evaluate("scrollY")<y0-2:
            await pg.mouse.wheel(0,240); await pg.wait_for_timeout(18)
        await pg.wait_for_timeout(600)
        rows=[]
        for _ in range(260):
            rows.append(await pg.evaluate(JS))
            await pg.mouse.wheel(0,40); await pg.wait_for_timeout(30)
        gap=[r for r in rows if not r['planeVis'] and not r['sheetVis'] and not r['seamVis']]
        if gap:
            print('glapp (varken ark eller linje syns): scrollY',gap[0]['y'],'till',gap[-1]['y'],
                  '=',round((gap[-1]['y']-gap[0]['y'])/h,2),'skarmhojder')
        else: print('inget glapp')
        both=[r for r in rows if r['planeVis'] and r['sheetVis']]
        print('bildrutor med bada arken synliga:',len(both), both[:3])
        await b.close()
asyncio.run(main())
