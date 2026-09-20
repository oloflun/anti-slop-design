"""Konturens fyra kanter mot planets KLIPPTA rektangel och mot .seam-linjerna, per tx-lage och bredd."""
import asyncio, json
from playwright.async_api import async_playwright
BASE="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=tes-till-ritning-"
async def main():
    out={}
    async with async_playwright() as p:
        b=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w,h in ((1920,930),(1440,900),(390,844)):
            for k in (2,3,4):
                pg=await b.new_page(viewport={'width':w,'height':h})
                await pg.goto(BASE+str(k)); await pg.wait_for_timeout(3500)
                g=await pg.evaluate("""()=>{
                  const e=document.querySelector('.tes-plane');const r=e.getBoundingClientRect();
                  const cs=getComputedStyle(e);
                  const m=/inset\(([^)]+)\)/.exec(cs.clipPath);
                  const v=m?m[1].trim().split(/\s+/).map(parseFloat):[0,0,0,0];
                  const ls=[...document.querySelectorAll('.seam i')].filter(i=>i.className.includes('seam-up')||i.className.includes('seam-dn'))
                    .map(i=>{const q=i.getBoundingClientRect();return {c:i.className,l:i.dataset.l,x:Math.round(q.left),w:Math.round(q.width)}});
                  const sh=document.querySelector('.process-sheet');
                  return {elem:[r.left,r.top,r.right,r.bottom], ins:v,
                          clipped:[r.left+v[3], r.top+v[0], r.right-v[1], r.bottom-v[2]],
                          shadowAt:[r.left,r.top,r.right,r.bottom],
                          lines:ls.filter(o=>o.l==='1'||o.l==='4'),
                          sheet: sh? [sh.getBoundingClientRect().left, sh.getBoundingClientRect().right]:null};
                }""")
                cl=g['clipped']
                l1=[o['x'] for o in g['lines'] if o['l']=='1']
                l4=[o['x'] for o in g['lines'] if o['l']=='4']
                out[f"{w}-t{k}"]={'clippedLeft':round(cl[0],1),'clippedRight':round(cl[2],1),
                                  'x1':l1[0] if l1 else None,'x4':(l4[0]+2) if l4 else None,
                                  'shadowLeftAt':round(g['elem'][0],1),'shadowRightAt':round(g['elem'][2],1),
                                  'sideGapLeft':round((l1[0]-cl[0]),1) if l1 else None,
                                  'sideGapRight':round((cl[2]-(l4[0]+2)),1) if l4 else None}
                print(f"{w}-t{k}", out[f"{w}-t{k}"], flush=True)
                await pg.close()
        await b.close()
    open('contour2.json','w').write(json.dumps(out,indent=1))
asyncio.run(main())
