"""astra-r23: hjulsvep genom tes -> ritning. Matt per bildruta: hur mycket LEVANDE
text som syns, var den ligger, planets synliga rektangel, tx. Inga skarmbilder har."""
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT = Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3d\shots\astra-r23")

JS = r"""(() => {
  const vw = innerWidth, vh = innerHeight, VA = vw*vh;
  function clipAnc(el, r){
    let n = el, out = {l:r.left,t:r.top,rr:r.right,b:r.bottom};
    while (n && n.nodeType === 1){
      const cs = getComputedStyle(n);
      if (cs.clipPath && cs.clipPath.indexOf('inset(') === 0){
        const nums = cs.clipPath.slice(6,-1).split(/\s+/).map(parseFloat);
        const nb = n.getBoundingClientRect();
        const t = nums[0];
        const rt = nums.length>1?nums[1]:nums[0];
        const b = nums.length>2?nums[2]:nums[0];
        const l = nums.length>3?nums[3]:rt;
        out.l = Math.max(out.l, nb.left+l); out.t = Math.max(out.t, nb.top+t);
        out.rr = Math.min(out.rr, nb.right-rt); out.b = Math.min(out.b, nb.bottom-b);
      }
      if (cs.overflow !== 'visible'){
        const nb = n.getBoundingClientRect();
        out.l=Math.max(out.l,nb.left); out.t=Math.max(out.t,nb.top);
        out.rr=Math.min(out.rr,nb.right); out.b=Math.min(out.b,nb.bottom);
      }
      n = n.parentElement;
    }
    return out;
  }
  let area = 0, minT = 1e9, maxB = -1e9, n = 0;
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let node;
  while ((node = tw.nextNode())){
    if (!node.nodeValue.trim()) continue;
    const el = node.parentElement; if (!el) continue;
    const cs = getComputedStyle(el);
    if (cs.display==='none'||cs.visibility==='hidden'||parseFloat(cs.opacity)===0) continue;
    const transparent = cs.color === 'rgba(0, 0, 0, 0)';
    const clipText = (cs.webkitBackgroundClip||cs.backgroundClip)==='text';
    if (transparent && !clipText) continue;
    const rg = document.createRange(); rg.selectNodeContents(node);
    const rects = rg.getClientRects();
    for (let i=0;i<rects.length;i++){
      const b = rects[i];
      if (b.width<=0||b.height<=0) continue;
      const c = clipAnc(el, b);
      const l=Math.max(0,c.l), t=Math.max(0,c.t), r=Math.min(vw,c.rr), bo=Math.min(vh,c.b);
      if (r<=l||bo<=t) continue;
      area += (r-l)*(bo-t); n++;
      if (t<minT) minT=t; if (bo>maxB) maxB=bo;
    }
  }
  const pl = document.querySelector('.tes-plane');
  let plane = null;
  if (pl){
    const b = pl.getBoundingClientRect(); const c = clipAnc(pl, b);
    const l=Math.max(0,c.l),t=Math.max(0,c.t),r=Math.min(vw,c.rr),bo=Math.min(vh,c.b);
    if (r>l&&bo>t) plane={x:Math.round(l),y:Math.round(t),w:Math.round(r-l),h:Math.round(bo-t),
                          frac:+(((r-l)*(bo-t))/VA).toFixed(3),
                          bg:getComputedStyle(pl).backgroundColor};
  }
  const ch = document.querySelector('.process-chapter');
  return {y:scrollY, vh, vw,
    tx: ch? +(parseFloat(getComputedStyle(ch).getPropertyValue('--tx'))||0).toFixed(3):null,
    ps: ch? +(parseFloat(getComputedStyle(ch).getPropertyValue('--sc-ps'))||0).toFixed(3):null,
    inkFrac:+(area/VA).toFixed(4), inkRuns:n,
    inkTop: minT<1e9?Math.round(minT):null, inkBot: maxB>-1e9?Math.round(maxB):null,
    plane};
})()"""

async def main():
    res = {}
    async with async_playwright() as p:
        br = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w,h,lo,hi in ((1920,930,5700,9300),(390,844,5100,7900)):
            ctx = await br.new_context(viewport={"width":w,"height":h})
            pg = await ctx.new_page()
            await pg.goto(URL, wait_until="load", timeout=40000)
            await pg.wait_for_timeout(2500)
            await pg.mouse.move(w/2, h/2)
            while (await pg.evaluate("scrollY")) < lo-100:
                await pg.mouse.wheel(0, 200)
                await pg.wait_for_timeout(16)
            await pg.wait_for_timeout(900)
            frames = []
            while (await pg.evaluate("scrollY")) < hi:
                frames.append(await pg.evaluate(JS))
                await pg.mouse.wheel(0, 40)
                await pg.wait_for_timeout(28)
            res[w] = frames
            print(w, "frames", len(frames), flush=True)
            await ctx.close()
        await br.close()
    (OUT/"sweep23.json").write_text(json.dumps(res))
    for w in res:
        print("===", w)
        for f in res[w][::10]:
            print("  y", f["y"], "tx", f["tx"], "ink", f["inkFrac"], "runs", f["inkRuns"], "top", f["inkTop"], "plane", f["plane"])

asyncio.run(main())
