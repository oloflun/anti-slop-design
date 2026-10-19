"""Storsta tomma vagrata bandet per bildruta, 120px-hjul over hela sidan, 1920x930.
Tomt = en rad dar ALLA pixlar ligger inom 3 enheter fran radens median (ingen text,
ingen bild, ingen linje). Rapporterar det hogsta sammanhangande blocket i % av vh."""
import asyncio, sys
from playwright.async_api import async_playwright
from PIL import Image
import io
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
async def main():
    w,h=int(sys.argv[1]),int(sys.argv[2])
    worst=[]
    async with async_playwright() as p:
        b=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg=await b.new_page(viewport={'width':w,'height':h})
        await pg.goto(URL); await pg.wait_for_timeout(3500)
        await pg.mouse.move(w/2,h/2)
        H=await pg.evaluate("document.documentElement.scrollHeight-innerHeight")
        while True:
            y=await pg.evaluate("scrollY")
            png=await pg.screenshot()
            im=Image.open(io.BytesIO(png)).convert('L').resize((160, h))
            run=0; best=0; bstart=0; bs=0
            for yy in range(h):
                row=[im.getpixel((x,yy)) for x in range(160)]
                flat = (max(row)-min(row))<=6
                if flat:
                    if run==0: bs=yy
                    run+=1
                    if run>best: best=run; bstart=bs
                else: run=0
            worst.append((y, best, round(100*best/h,1), bstart))
            if y>=H-2: break
            await pg.mouse.wheel(0,120); await pg.wait_for_timeout(60)
        await b.close()
    worst.sort(key=lambda t:-t[1])
    print('storsta tomma band, topp 8:')
    for t in worst[:8]: print('  scrollY',t[0],'  ',t[1],'px =',t[2],'% vh, start y',t[3])
asyncio.run(main())
