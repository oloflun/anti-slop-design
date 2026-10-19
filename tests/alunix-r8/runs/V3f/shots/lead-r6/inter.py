import asyncio
from playwright.async_api import async_playwright
U="http://127.0.0.1:4626/cells/V3f-r8/index.html"
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1440,'height':900})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto(U); await pg.wait_for_timeout(800)
        await pg.evaluate("__lenis.scrollTo('#exempelcase',{immediate:true})"); await pg.wait_for_timeout(1200)
        await pg.evaluate("__lenis.scrollTo(document.querySelector('#exempelcase').offsetTop+300,{immediate:true})"); await pg.wait_for_timeout(900)
        btns=pg.locator('#exempelcase button'); print('buttons',await btns.count())
        await btns.nth(1).hover(); await pg.wait_for_timeout(900); await pg.screenshot(path='i-hover-horai.png')
        await btns.nth(1).click(); await pg.wait_for_timeout(2200)
        st=await pg.evaluate("[scrollY, document.querySelector('#showcase').getBoundingClientRect().top, [...document.querySelectorAll('#showcase iframe')].map(f=>[f.src.split('/').pop(), f.offsetParent!==null])]"); print('after click',st)
        await pg.screenshot(path='i-horai-start.png')
        for k in range(3):
            for _ in range(6): await pg.mouse.wheel(0,120); await pg.wait_for_timeout(40)
            await pg.wait_for_timeout(700); await pg.screenshot(path=f'i-horai-{k}.png')
        iy=await pg.evaluate("[...document.querySelectorAll('#showcase iframe')].filter(f=>f.offsetParent).map(f=>f.contentWindow.scrollY)"); print('inner scrollY',iy)
        # kontakt front before flip
        await pg.evaluate("__lenis.scrollTo('#kontakt',{immediate:true,offset:-700})"); await pg.wait_for_timeout(1200); await pg.screenshot(path='i-kontakt-pre.png')
        await pg.evaluate("__lenis.scrollTo('#kontakt',{immediate:true,offset:-250})"); await pg.wait_for_timeout(1200); await pg.screenshot(path='i-kontakt-front.png')
        card=pg.locator('#kontakt button').first; await card.hover(); await pg.wait_for_timeout(500); await card.click(); await pg.wait_for_timeout(250); await pg.screenshot(path='i-kontakt-midflip.png'); await pg.wait_for_timeout(1200); await pg.screenshot(path='i-kontakt-back.png')
        print('errors',errs); await b.close()
asyncio.run(m())
