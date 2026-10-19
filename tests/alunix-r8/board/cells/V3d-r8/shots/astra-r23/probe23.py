"""Vilka element bidrar med synlig text vid ett givet scrollY."""
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT=Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3d\shots\astra-r23")
JS=r"""(() => {
  const vw=innerWidth, vh=innerHeight, out=[];
  const tw=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT); let node;
  while((node=tw.nextNode())){
    if(!node.nodeValue.trim()) continue;
    const el=node.parentElement; if(!el) continue;
    const cs=getComputedStyle(el);
    if(cs.display==='none'||cs.visibility==='hidden'||parseFloat(cs.opacity)===0) continue;
    if(cs.color==='rgba(0, 0, 0, 0)' && (cs.webkitBackgroundClip||cs.backgroundClip)!=='text') continue;
    const b=el.getBoundingClientRect();
    if(b.bottom<=0||b.top>=vh||b.width<=0) continue;
    out.push({sel:el.tagName.toLowerCase()+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\s+/).join('.'):''),
      txt:node.nodeValue.trim().slice(0,34), top:Math.round(b.top), bot:Math.round(b.bottom),
      fs:cs.fontSize});
  }
  return {y:scrollY,out};
})()"""
POS={1920:[6640,6720,6800,6880,6960,7040,7200],390:[5880,5960,6040,6120,6200,6300]}
async def main():
    res={}
    async with async_playwright() as p:
        br=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w,h in ((1920,930),(390,844)):
            ctx=await br.new_context(viewport={"width":w,"height":h}); pg=await ctx.new_page()
            await pg.goto(URL,wait_until="load",timeout=40000); await pg.wait_for_timeout(2200)
            await pg.mouse.move(w/2,h/2); res[w]=[]
            for tgt in POS[w]:
                for _ in range(2000):
                    cur=await pg.evaluate("scrollY"); d=tgt-cur
                    if abs(d)<2: break
                    await pg.mouse.wheel(0,max(-120,min(120,d))); await pg.wait_for_timeout(18)
                await pg.wait_for_timeout(700)
                res[w].append(await pg.evaluate(JS))
            await ctx.close()
        await br.close()
    (OUT/"probe23.json").write_text(json.dumps(res,ensure_ascii=False,indent=1))
    for w in res:
        print("===",w)
        for f in res[w]:
            print(" y",f["y"])
            for o in f["out"]: print("   ",o["top"],o["bot"],o["fs"],o["sel"][:48],"|",o["txt"])
asyncio.run(main())
