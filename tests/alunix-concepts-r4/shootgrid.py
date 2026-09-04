# -*- coding: utf-8 -*-
"""Eight viewport frames through a cell after a scripted scroll-through, tiled 4x2. Usage: python shootgrid.py M2"""
import sys
from playwright.sync_api import sync_playwright
from PIL import Image
cell=sys.argv[1]
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':900})
    msgs=[]; pg.on('console', lambda m: msgs.append(m.type+': '+m.text))
    pg.goto(f'http://127.0.0.1:3090/tests/alunix-concepts-r4/cells/{cell}-chain/index.html', wait_until='networkidle'); pg.wait_for_timeout(2000)
    H=pg.evaluate('document.documentElement.scrollHeight'); print('H',H)
    for y in range(0,H,300): pg.evaluate(f'window.scrollTo(0,{y})'); pg.wait_for_timeout(120)
    ys=[int((H-900)*f) for f in (0,0.12,0.24,0.36,0.5,0.65,0.8,1)]
    for i,y in enumerate(ys):
        pg.evaluate(f'window.scrollTo(0,{y})'); pg.wait_for_timeout(700); pg.screenshot(path=f'my-{cell}-{i}.png')
    print('console:',[m for m in msgs if 'scrollcraft' in m or 'error' in m.lower()][:5])
    b.close()
ims=[Image.open(f'my-{cell}-{i}.png').resize((480,300)) for i in range(8)]
out=Image.new('RGB',(4*480+30,2*300+10),(90,90,90))
for i,im in enumerate(ims): out.paste(im,((i%4)*490,(i//4)*310))
out.save(f'my-{cell}-grid.png'); print(out.size, ys)
