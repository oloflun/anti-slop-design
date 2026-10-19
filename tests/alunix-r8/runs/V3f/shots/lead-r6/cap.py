import sys, asyncio
# Leadens pixelgranskning: riktig hjulscroll, bild per steg, kontaktark. Kör: python lead_motion_capture.py 1440|390 (servern på 4626 med boardcellen).
from playwright.async_api import async_playwright
from PIL import Image
URL="http://127.0.0.1:4626/cells/V3f-r8/index.html"; W=int(sys.argv[1]); H=844 if W<500 else 900; tag=f"m6-{W}"
async def shot(pg,path):
    for i in range(3):
        try: return await pg.screenshot(path=path,timeout=10000)
        except Exception as e: print('retry',path,str(e)[:40]); await pg.wait_for_timeout(300)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':W,'height':H})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: m.type=='error' and errs.append(m.text))
        await pg.goto(URL); shots=[]
        await pg.wait_for_timeout(300); await shot(pg,f"{tag}-i300.png"); shots.append(f"{tag}-i300.png")
        await pg.wait_for_timeout(1300); await shot(pg,f"{tag}-i1600.png"); shots.append(f"{tag}-i1600.png")
        await pg.mouse.move(W//2,H//2)
        n=0; last=-1
        while True:
            for _ in range(4): await pg.mouse.wheel(0,120); await pg.wait_for_timeout(40)
            await pg.wait_for_timeout(250)
            y=await pg.evaluate("scrollY")
            f=f"{tag}-{n:02d}.png"; await shot(pg,f); shots.append(f); n+=1
            if y==last: break
            last=y
        print('frames',len(shots),'errors',errs[:5])
        cols=6; tw=W//3 if W>500 else W//2; th=int(tw*H/W)
        rows=(len(shots)+cols-1)//cols; s=Image.new('RGB',(cols*(tw+4),rows*(th+4)),'red')
        for i,f in enumerate(shots): s.paste(Image.open(f).resize((tw,th)),((i%cols)*(tw+4),(i//cols)*(th+4)))
        s.save(f"{tag}-sheet.png"); print(s.size)
        await b.close()
asyncio.run(main())
