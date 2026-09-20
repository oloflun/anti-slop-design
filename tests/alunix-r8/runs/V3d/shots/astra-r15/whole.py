import asyncio, os
from playwright.async_api import async_playwright
from PIL import Image
async def main():
    os.makedirs('whole-1920', exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg=await b.new_page(viewport={'width':1920,'height':930})
        await pg.goto("http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"); await pg.wait_for_timeout(2500)
        await pg.mouse.move(960,465)
        H=await pg.evaluate("document.documentElement.scrollHeight"); i=0; y=0
        while True:
            await pg.screenshot(path=f'whole-1920/{i:02d}.png'); i+=1
            if y>=H-930: break
            for _ in range(8): await pg.mouse.wheel(0,116); await pg.wait_for_timeout(40)
            await pg.wait_for_timeout(900); y=await pg.evaluate("scrollY")
        await b.close()
    fs=sorted(os.listdir('whole-1920')); cols=6; tw,th=320,155
    sheet=Image.new('RGB',(cols*tw,((len(fs)+cols-1)//cols)*th),'white')
    for k,f in enumerate(fs): sheet.paste(Image.open('whole-1920/'+f).convert('RGB').resize((tw-4,th-4)),((k%cols)*tw,(k//cols)*th))
    sheet.save('sheet-1920.png'); print(len(fs))
asyncio.run(main())
