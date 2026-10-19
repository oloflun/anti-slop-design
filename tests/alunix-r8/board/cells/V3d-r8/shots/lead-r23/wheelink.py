"""Lead R23: riktig hjulscroll genom tes -> ritning. Matt textyta per bildruta, inte preview.

Previews siktar pa det gamla tx-fonstret efter plan 067 C3, sa de ar inte langre
sanning om aktens lagen. Detta matt ar det planen faktiskt kraver: >= 18 % textyta
i VARJE bildruta vid 1920/1440, aldrig noll vid 390.
"""
import asyncio, json, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"

INK = """() => {
  let ink=0, runs=0; const vw=innerWidth, vh=innerHeight;
  const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT); let n;
  while((n=w.nextNode())){
    if(!n.nodeValue.trim()) continue;
    const rg=document.createRange(); rg.selectNodeContents(n);
    for(const r of rg.getClientRects()){
      const ww=Math.max(0,Math.min(r.right,vw)-Math.max(r.left,0));
      const hh=Math.max(0,Math.min(r.bottom,vh)-Math.max(r.top,0));
      if(ww>0&&hh>0){ ink+=ww*hh; runs++; }
    }
  }
  const ch=document.querySelector('.process-chapter');
  const tx=ch?parseFloat(getComputedStyle(ch).getPropertyValue('--tx'))||0:0;
  return {ink:+(100*ink/(vw*vh)).toFixed(1), runs, tx:+tx.toFixed(3)};
}"""


async def main():
    w, h, start, end, tag = (int(sys.argv[1]), int(sys.argv[2]),
                             int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
    rows = []
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.goto(URL); await pg.wait_for_timeout(3000)
        await pg.mouse.move(w // 2, h // 2)
        cur = 0
        while cur < start:
            step = min(60, start - cur)
            await pg.mouse.wheel(0, step); cur += step
            await pg.wait_for_timeout(2)
        await pg.wait_for_timeout(600)
        shots = 0
        while cur <= end:
            g = await pg.evaluate(INK)
            g['y'] = cur
            rows.append(g)
            # spara en bild vid varje fjardedel av draget
            if g['tx'] > 0 and shots < 5 and g['tx'] >= shots * 0.25:
                await pg.screenshot(path=f"wtx{shots}-{tag}.png")
                shots += 1
            await pg.mouse.wheel(0, 20); cur += 20
            await pg.wait_for_timeout(3)
        await b.close()

    worst = min(rows, key=lambda r: r['ink'])
    zero = [r for r in rows if r['runs'] == 0]
    print(f"{tag}: {len(rows)} bildrutor, lagst textyta {worst['ink']}% vid y{worst['y']} "
          f"(tx {worst['tx']}), bildrutor utan text: {len(zero)}")
    under = [r for r in rows if r['ink'] < 18]
    print(f"  under 18%: {len(under)} bildrutor")
    open(f"wheelink-{tag}.json", 'w').write(json.dumps(rows, indent=1))


asyncio.run(main())
