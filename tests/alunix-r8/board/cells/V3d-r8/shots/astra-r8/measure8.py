"""astra-r8: mått för r7-fixarna 2, 4, 5, 6, 7, 8."""
import asyncio, json
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
R="""e=>{if(!e)return null;const r=e.getBoundingClientRect();return {x:Math.round(r.left),y:Math.round(r.top),w:Math.round(r.width),h:Math.round(r.height),r:Math.round(r.right)}}"""
async def main():
  out={}
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(1440,900),(768,1024),(390,844)]:
      pg=await (await b.new_context(viewport={'width':w,'height':h})).new_page()
      o=out[w]={}
      for n in range(1,6):
        await pg.goto(URL+f'?preview=thesis-0{n}');await pg.wait_for_timeout(2500)
        o[f'thesis-0{n}']=await pg.evaluate(f"""()=>{{const q={R};const ts=[...document.querySelectorAll('.ts')].find(e=>getComputedStyle(e).clipPath.startsWith('inset(0%'));
          return {{photo:q(document.querySelector('.thesis-photo-box')),lines:q(document.querySelector('.thesis-lines')),ts:q(ts),ticks:q(document.querySelector('.thesis-ticks')),stage:q(document.querySelector('.thesis-stage'))}}}}""")
      await pg.goto(URL+'?preview=case-calyx-03');await pg.wait_for_timeout(3500)
      o['calyx']=await pg.evaluate(f"""()=>{{const q={R};const s=document.querySelector('#case-calyx .case-stage');const c=getComputedStyle(s);
        return {{bg:c.backgroundColor,ink:c.color,wrap:q(document.querySelector('#case-calyx .case-wrap')),fig:q(document.querySelector('#case-calyx .case-fig')),text:q(document.querySelector('#case-calyx .case-text'))}}}}""")
      await pg.goto(URL+'?preview=case-horai-03');await pg.wait_for_timeout(5000)
      o['horai3']=await pg.evaluate(f"""()=>{{const q={R};const f=document.querySelector('#case-horai iframe');const d=f.contentDocument;const jp=d.querySelector('#quote-jp'),tx=d.querySelector('#quote-text');
        const fr=f.getBoundingClientRect();const jr=jp&&jp.getBoundingClientRect();
        return {{wrap:q(document.querySelector('#case-horai .case-wrap')),jpOp:jp&&getComputedStyle(jp).opacity,txFilter:tx&&getComputedStyle(tx).filter,txOp:tx&&getComputedStyle(tx).opacity,
          jpInFrame:jr?{{top:Math.round(jr.top),bot:Math.round(jr.bottom),ih:f.contentWindow.innerHeight}}:null,fy:f.contentWindow.scrollY}}}}""")
      await pg.goto(URL+'?preview=chapter');await pg.wait_for_timeout(3000)
      o['chapter']=await pg.evaluate(f"""()=>{{const q={R};const li=document.querySelector('.process-steps li[data-step="01"]');return {{y:scrollY,li01:q(li),vh:innerHeight}}}}""")
    await b.close()
  print(json.dumps(out,indent=1))
asyncio.run(main())
