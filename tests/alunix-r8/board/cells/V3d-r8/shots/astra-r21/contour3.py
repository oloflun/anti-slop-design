import asyncio, json
from playwright.async_api import async_playwright
BASE="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=tes-till-ritning-"
JS=r"""()=>{
  function ins(cs,w,h){const m=/inset\(([^)]+)\)/.exec(cs.clipPath);if(!m)return[0,0,0,0];
    const r=m[1].trim().split(/\s+/);const v=t=>t.endsWith('%')?parseFloat(t)/100:parseFloat(t);
    let a=r.map(parseFloat);
    if(r.length===1)a=[a[0],a[0],a[0],a[0]];
    else if(r.length===2)a=[a[0],a[1],a[0],a[1]];
    else if(r.length===3)a=[a[0],a[1],a[2],a[1]];
    // procent
    const p=r.map(t=>t.endsWith('%'));
    return a.map((x,i)=>p[Math.min(i,p.length-1)]? x/100*(i%2?w:h) : x);
  }
  const e=document.querySelector('.tes-plane'); const r=e.getBoundingClientRect();
  const v=ins(getComputedStyle(e), r.width, r.height);
  const P={l:r.left+v[3],t:r.top+v[0],r:r.right-v[1],b:r.bottom-v[2]};
  const lines=[...document.querySelectorAll('.seam i')].map(i=>{
    const q=i.getBoundingClientRect(); const w2=ins(getComputedStyle(i), q.width, q.height);
    return {c:i.className,l:i.dataset.l||'', t:Math.round(q.top+w2[0]), b:Math.round(q.bottom-w2[2]),
            x:Math.round(q.left+w2[3]), r:Math.round(q.right-w2[1])};
  }).filter(o=>o.b-o.t>1||o.r-o.x>1);
  const ups=lines.filter(o=>o.c.includes('seam-up')), dns=lines.filter(o=>o.c.includes('seam-dn'));
  return {plane:{l:Math.round(P.l),t:Math.round(P.t),r:Math.round(P.r),b:Math.round(P.b)},
          upTop: ups.length?Math.min(...ups.map(o=>o.t)):null,
          dnBot: dns.length?Math.max(...dns.map(o=>o.b)):null,
          lines};
}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w,h in ((390,844),(1920,930)):
            for k in (1,2,3,4):
                pg=await b.new_page(viewport={'width':w,'height':h})
                await pg.goto(BASE+str(k)); await pg.wait_for_timeout(3000)
                g=await pg.evaluate(JS); await pg.close()
                pl=g['plane']
                print(w,'t'+str(k),'plan',pl,'linjernas topp',g['upTop'],'linjernas botten',g['dnBot'],
                      '| plan.t - linjetopp', (pl['t']-g['upTop']) if g['upTop'] is not None else None,
                      '| plan.b - linjebotten', (pl['b']-g['dnBot']) if g['dnBot'] is not None else None, flush=True)
        await b.close()
asyncio.run(main())
