import asyncio
from playwright.async_api import async_playwright
URL="http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for w,h in [(1440,900),(390,844)]:
      ctx=await b.new_context(viewport={"width":w,"height":h}); pg=await ctx.new_page()
      await pg.goto(URL,wait_until="domcontentloaded"); await pg.wait_for_timeout(600); await pg.mouse.move(w/2,h/2)
      for i in range(7):
        await pg.mouse.wheel(0,800); await pg.wait_for_timeout(150)
      await pg.wait_for_timeout(300)
      y=await pg.evaluate("scrollY"); await pg.screenshot(path=f"fast-{w}-{y}.png"); print(w,y)
      await ctx.close()
    await b.close()
asyncio.run(main())
