import time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(headless=True); pg=b.new_page(viewport={"width":1440,"height":900})
    pg.goto("http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"); time.sleep(4.5)
    for y in [9900, 9900.5, 9900.3, 6200]:
        pg.evaluate(f"window.__v4.lenis.scrollTo({y}, {{immediate:true, force:true}})"); time.sleep(0.6)
        r=pg.evaluate("""() => { const c=document.createElement('canvas'); return [scrollY, window.__v4.lenis.scroll] }""")
        pg.screenshot(path="tests/alunix-r8/runs/V4/shots/top-probe.png", clip={"x":0,"y":0,"width":1440,"height":6})
        from PIL import Image
        im=Image.open("tests/alunix-r8/runs/V4/shots/top-probe.png").convert('RGB')
        print(y, r, [im.getpixel((700,k)) for k in range(4)])
    b.close()
