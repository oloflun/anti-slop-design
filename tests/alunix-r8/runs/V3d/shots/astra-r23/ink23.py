"""Exakt glyfyta for rubrikerna: Range.getClientRects pa textnoden, inte elementets box."""
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT=Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3d\shots\astra-r23")
JS=r"""(() => {
  function ink(sel){
    const el=document.querySelector(sel); if(!el) return null;
    const rg=document.createRange(); rg.selectNodeContents(el);
    const rs=[...rg.getClientRects()]; if(!rs.length) return null;
    const l=Math.min(...rs.map(r=>r.left)), r=Math.max(...rs.map(r=>r.right));
    const t=Math.min(...rs.map(r=>r.top)), b=Math.max(...rs.map(r=>r.bottom));
    const cs=getComputedStyle(el);
    return {w:+(r-l).toFixed(1),h:+(b-t).toFixed(1),lines:rs.length,fs:cs.fontSize,
            ff:cs.fontFamily.split(',')[0],fw:cs.fontWeight};
  }
  const sec=document.querySelector('#case');
  const st=document.querySelector('.cases-title'), ld=document.querySelector('.cases-lead');
  const sr=sec.getBoundingClientRect(), tr=st.getBoundingClientRect(), lr=ld.getBoundingClientRect();
  return {
    exempelcase: ink('.cases-title'),
    calyxName: ink('.case--calyx .case-name'),
    horaiName: ink('.case--horai .case-name'),
    prisTitle: ink('#pris-title'),
    processTitle: ink('.process-title'),
    heroLine: ink('.thesis-lines .ts'),
    caseAir: {sectionH:+sr.height.toFixed(1),
      above:+(tr.top-sr.top).toFixed(1),
      titleToLead:+(lr.top-tr.bottom).toFixed(1),
      below:+(sr.bottom-lr.bottom).toFixed(1),
      inkBlock:+(lr.bottom-tr.top).toFixed(1)},
    vw:innerWidth, vh:innerHeight
  };
})()"""
async def main():
    res={}
    async with async_playwright() as p:
        br=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w,h in ((1920,930),(1440,900),(390,844)):
            ctx=await br.new_context(viewport={"width":w,"height":h}); pg=await ctx.new_page()
            await pg.goto(URL,wait_until="load",timeout=40000); await pg.wait_for_timeout(2600)
            res[w]=await pg.evaluate(JS)
            await ctx.close()
        await br.close()
    (OUT/"ink23.json").write_text(json.dumps(res,indent=1,ensure_ascii=False))
    print(json.dumps(res,indent=1,ensure_ascii=False))
asyncio.run(main())
