import asyncio
from playwright.async_api import async_playwright
U="http://127.0.0.1:4626/cells/V3f-r8/index.html"
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':900})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto(U); await pg.wait_for_timeout(800)
        k=await pg.evaluate("document.querySelector('#kontakt').offsetTop")
        await pg.evaluate(f"__lenis.scrollTo({k}-500,{{immediate:true}})"); await pg.wait_for_timeout(1300)
        await pg.screenshot(path='i-kontakt-front.png')
        st=lambda: pg.evaluate("[document.getElementById('kontaktCardFront').inert, document.getElementById('kontaktCardBack').inert]")
        print('front state (frontInert, backInert)', await st())
        await pg.mouse.move(900,600); await pg.wait_for_timeout(300)
        box=await pg.locator('#kontaktCardFront').bounding_box(); print('card box',box)
        await pg.mouse.move(box['x']+box['width']*0.85, box['y']+box['height']*0.2); await pg.wait_for_timeout(600); await pg.screenshot(path='i-kontakt-tilt.png')
        await pg.locator('#kontaktCardFront').click(); await pg.wait_for_timeout(260); await pg.screenshot(path='i-kontakt-midflip.png')
        await pg.wait_for_timeout(1200); await pg.screenshot(path='i-kontakt-back.png'); print('after click', await st())
        await pg.keyboard.press('Tab'); f=await pg.evaluate("document.activeElement.outerHTML.slice(0,90)"); print('tab ->',f)
        print('errors',errs); await b.close()
asyncio.run(m())
