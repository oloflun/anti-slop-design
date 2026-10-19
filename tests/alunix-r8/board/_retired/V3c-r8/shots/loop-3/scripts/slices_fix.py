"""slices_fix.py <out-dir> <url> <slug> <w> <h> <first> <last>
Slices like slices.py, but with plan 035's latch loop (sample the shim's lerped value
every frame while a reveal is unfinished) injected after load, so a scrollTo capture
shows what a wheel reader sees. Frames get 3 s to load once in view."""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
FIX = """() => {
  const R = [
    {el: document.querySelector('.calyx-wrap'), fig: document.querySelector('.calyx-fig'), from:0.02, to:0.30, v:0},
    {el: document.querySelector('.horai-wrap'), fig: document.querySelector('.horai-fig'), from:0.10, to:0.55, v:0}
  ];
  let raf = null;
  function tick(){
    raf = null; let again = false;
    for (const r of R){
      const a = (window.__scSmooth.acts||[]).filter(x => x.el === r.fig)[0];
      if (!a || isNaN(a.cur)) { again = true; continue; }
      let t = Math.min(1, Math.max(0, (a.cur - r.from)/(r.to - r.from)));
      t = t*t*(3-2*t);
      if (t > r.v + 0.002){ r.v = t; r.el.style.setProperty('--rv', t.toFixed(4)); }
      const target = parseFloat(a.el.style.getPropertyValue('--sc-p'));
      if (r.v < 1 && !isNaN(target) && Math.abs(target - a.cur) > 0.0005) again = true;
    }
    if (again) raf = requestAnimationFrame(tick);
  }
  function kick(){ if (!raf) raf = requestAnimationFrame(tick); }
  addEventListener('scroll', kick, {passive:true});
  kick();
}"""
async def main(out_dir, url, slug, w, h, first, last):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        page = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1, reduced_motion="reduce")
        await page.goto(url, wait_until="load", timeout=60000)
        await page.wait_for_timeout(1500)
        await page.evaluate(FIX)
        for i in range(first, last + 1):
            await page.evaluate(f"window.scrollTo(0, {i*h})")
            await page.wait_for_timeout(3000)
            rv = await page.evaluate("[document.querySelector('.calyx-wrap').style.getPropertyValue('--rv'), document.querySelector('.horai-wrap').style.getPropertyValue('--rv')]")
            await page.screenshot(path=str(out / f"{slug}--s{i:02d}.png"))
            print(f"{slug}--s{i:02d}.png rv calyx={rv[0]} horai={rv[1]}")
        await b.close()
a = sys.argv
asyncio.run(main(a[1], a[2], a[3], int(a[4]), int(a[5]), int(a[6]), int(a[7])))
