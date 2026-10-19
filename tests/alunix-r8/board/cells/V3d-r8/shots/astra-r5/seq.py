import asyncio
from PIL import Image
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
async def wheel(pg,y):
  for _ in range(600):
    d=y-await pg.evaluate("scrollY")
    if abs(d)<2: break
    await pg.mouse.wheel(0,max(-120,min(120,d))); await pg.wait_for_timeout(40)
  await pg.wait_for_timeout(1200)
async def run(b,w,h,ys,tag):
  pg=await b.new_page(viewport={"width":w,"height":h}); await pg.goto(URL,wait_until="load"); await pg.wait_for_timeout(1500); await pg.mouse.move(w/2,h/2)
  ims=[]
  for y in ys:
    await wheel(pg,y); f=f"seq-{tag}-{y}.png"; await pg.screenshot(path=f); ims.append(Image.open(f))
  sc=0.3 if w>800 else 0.45; tw,th=int(w*sc),int(h*sc); cols=5
  S=Image.new('RGB',(cols*(tw+6),((len(ims)+cols-1)//cols)*(th+6)),'white')
  for k,im in enumerate(ims): S.paste(im.convert('RGB').resize((tw,th)),((k%cols)*(tw+6),(k//cols)*(th+6)))
  S.save(f"strip-{tag}.png"); await pg.close()
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    await run(b,1440,900,list(range(13500,14300,80)),"d-exit")
    await run(b,390,844,list(range(9300,10900,160)),"m-0607")
    await b.close()
asyncio.run(main())
