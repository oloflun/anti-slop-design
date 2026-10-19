"""mountshift.py <out.json>: the band's height before and after the frames mount, at 1440
and 390, with the engine's cached act tops and the page's own processTop-derived
--s1/--e1 read alongside, driven by a real wheel (not scrollTo). Which element shrinks?"""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
JS = """() => {
  const q = s => document.querySelector(s);
  const box = s => { const e = q(s); if (!e) return null; const r = e.getBoundingClientRect(); return [Math.round(r.top + scrollY), Math.round(r.height)]; };
  const o = {scrollY: scrollY, docH: document.documentElement.scrollHeight};
  for (const s of ['section.hero', '.stagger', '.calyx-fig', '.calyx-wrap', '.calyx-wrap .rv', '.calyx-wrap iframe', '.horai-fig', '.horai-wrap', '.horai-wrap .rv', '.horai-wrap iframe', '.price', '#process', '#principer', 'footer.close']) o[s] = box(s);
  o.calyxSrc = !!q('.calyx-wrap iframe').src; o.horaiSrc = !!q('.horai-wrap iframe').src;
  o.horaiWrapCS = (c => ({minH: c.minHeight, h: c.height, display: c.display, cv: c.contentVisibility}))(getComputedStyle(q('.horai-wrap')));
  o.horaiIframeCS = (c => ({pos: c.position, h: c.height, w: c.width, display: c.display}))(getComputedStyle(q('.horai-wrap iframe')));
  o.calyxIframeCS = (c => ({pos: c.position, h: c.height, w: c.width, display: c.display}))(getComputedStyle(q('.calyx-wrap iframe')));
  const inst = (window.ScrollCraft && window.ScrollCraft.instances && window.ScrollCraft.instances[0]) || null;
  try { o.engine = inst.acts.map(a => [a.el.id || a.el.className.split(' ')[0], Math.round(a.top)]); } catch(e) { o.engine = String(e); }
  const p = q('#process'); const cs = getComputedStyle(p); o.s1 = cs.getPropertyValue('--s1'); o.e1 = cs.getPropertyValue('--e1'); o.procP = p.style.getPropertyValue('--sc-p');
  return o;
}"""
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for w, h in ((1440, 900), (390, 844)):
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2500)
        rows = {"load": pg.evaluate(JS)}
        pg.mouse.move(w // 2, h // 2)
        y = 0
        for target, label in ((1500, "before_mount"), (2400, "after_mount"), (4800, "in_band")):
            while y < target:
                pg.mouse.wheel(0, 100); pg.wait_for_timeout(60); y = pg.evaluate("scrollY")
            pg.wait_for_timeout(3000)
            rows[label] = pg.evaluate(JS)
        pg.set_viewport_size({"width": w, "height": h - 1}); pg.wait_for_timeout(500)
        pg.set_viewport_size({"width": w, "height": h}); pg.wait_for_timeout(1500)
        rows["after_real_resize"] = pg.evaluate(JS)
        out[str(w)] = rows
        for k, v in rows.items():
            print(w, k, json.dumps({kk: vv for kk, vv in v.items() if kk in ('scrollY', 'docH', '.stagger', '.horai-fig', '.horai-wrap', '.horai-wrap iframe', '.price', '#process', 'calyxSrc', 'horaiSrc', 'horaiIframeCS', 'e1', 'procP')}))
            print("     engine", v.get("engine"))
        pg.close()
    b.close()
json.dump(out, open(sys.argv[1], "w"), indent=1)
