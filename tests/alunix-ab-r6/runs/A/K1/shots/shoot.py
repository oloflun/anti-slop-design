"""Skjuter skärmbilder av K1. Körs från repo-roten med servern igång på 3101."""
import sys, json, asyncio
from playwright.sync_api import sync_playwright
URL="http://127.0.0.1:3101/tests/alunix-ab-r6/runs/A/K1/index.html"
import os, mimetypes, urllib.parse
ROOT=os.getcwd()
mimetypes.add_type('image/webp','.webp'); mimetypes.add_type('image/svg+xml','.svg'); mimetypes.add_type('text/javascript','.js')
def from_disk(route, request):
    """python -m http.server tappar anslutningar under parallell last; samma filer, samma URL:er, men lasta fran disk."""
    path=urllib.parse.unquote(urllib.parse.urlparse(request.url).path).lstrip('/').split('?')[0]
    fp=os.path.join(ROOT, *path.split('/'))
    if os.path.isfile(fp):
        route.fulfill(path=fp, content_type=mimetypes.guess_type(fp)[0] or 'application/octet-stream')
    else:
        route.fulfill(status=404, body='not found')
OUT="tests/alunix-ab-r6/runs/A/K1/shots/"
what=sys.argv[1:] or ['all']
def overflow(page):
    return page.evaluate("""() => {
      const vw=document.documentElement.clientWidth; const bad=[];
      const clipped=(el)=>{ for(let a=el.parentElement;a;a=a.parentElement){ const o=getComputedStyle(a).overflow; if(o.includes('hidden')||o.includes('clip')) return true; } return false; };
      for (const el of document.querySelectorAll('body *')) {
        const r=el.getBoundingClientRect();
        if (r.width===0) continue;
        if (clipped(el)) continue;
        if (r.right>vw+1 || r.left<-1) bad.push(el.tagName+'.'+el.className+' '+Math.round(r.left)+'..'+Math.round(r.right));
      }
      return {sw:document.documentElement.scrollWidth, vw, bad:bad.slice(0,20)};
    }""")
with sync_playwright() as p:
    b=p.chromium.launch()
    def ctx(w,h,reduced=False):
        c=b.new_context(viewport={'width':w,'height':h}, device_scale_factor=1, reduced_motion='reduce' if reduced else 'no-preference')
        pg=c.new_page(); errs=[]
        pg.route('http://127.0.0.1:3101/**', from_disk)
        pg.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type in ('error','warning') else None)
        pg.on('pageerror', lambda e: errs.append('pageerror: '+str(e)))
        pg.on('requestfailed', lambda r: errs.append('reqfail: '+r.url+' '+str(r.failure)))
        pg.goto(URL, wait_until='networkidle'); pg.wait_for_timeout(1200)
        return c,pg,errs
    if 'all' in what or 'desk' in what:
        c,pg,errs=ctx(1440,900)
        pg.screenshot(path=OUT+'d-00-fold.png')
        info=pg.evaluate("()=>({h:document.documentElement.scrollHeight, cut: document.getElementById('hero').offsetHeight - innerHeight, title: document.getElementById('frame').contentDocument && document.getElementById('frame').contentDocument.title})")
        print('desk', info)
        # genomscroll i 300 px-steg
        H=info['h']; y=0
        while y<H:
            pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(40); y+=300
        pg.wait_for_timeout(600)
        pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300)
        # signaturrörelsen: tre punkter mitt i
        vh=900; track=2.6*vh
        for i,fr in enumerate([0.22,0.5,0.72,0.9,1.0]):
            pg.evaluate(f"window.scrollTo(0,{int(track*fr)})"); pg.wait_for_timeout(250)
            pg.screenshot(path=OUT+f'd-zoom-{i}-p{int(fr*100)}.png')
        pg.wait_for_timeout(1500); pg.screenshot(path=OUT+'d-hold-late.png')
        # klippet och vitt
        cut=info['cut']
        for name,yy in [('cut-1',cut-1),('cut',cut+2),('cut+400',cut+400)]:
            pg.evaluate(f"window.scrollTo(0,{yy})"); pg.wait_for_timeout(900)
            pg.screenshot(path=OUT+f'd-{name}.png')
        # hela sidan efter genomscroll (full_page)
        pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300)
        y=0
        while y<H:
            pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(60); y+=300
        pg.wait_for_timeout(1500)
        pg.screenshot(path=OUT+'d-full.png', full_page=True)
        # folds through the white part
        for k,yy in enumerate(range(cut, H-vh+1, 700)):
            pg.evaluate(f"window.scrollTo(0,{yy})"); pg.wait_for_timeout(700)
            pg.screenshot(path=OUT+f'd-white-{k}.png')
        pg.evaluate("window.scrollTo(0,document.documentElement.scrollHeight)"); pg.wait_for_timeout(900)
        pg.screenshot(path=OUT+'d-end.png')
        print('images', pg.evaluate("Array.from(document.images).map(i=>[i.currentSrc.split('/').pop(), i.complete && i.naturalWidth>0])"))
        print('overflow desk', overflow(pg)); print('errs', errs); c.close()
    if 'all' in what or 'mob' in what:
        for w in (390,320,768):
            c,pg,errs=ctx(w,844 if w<700 else 1024)
            H=pg.evaluate("document.documentElement.scrollHeight"); y=0
            pg.screenshot(path=OUT+f'm{w}-fold.png')
            while y<H:
                pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(50); y+=300
            pg.wait_for_timeout(1200)
            if w==390:
                vh=844; track=2.6*vh
                for i,fr in enumerate([0.5,0.9]):
                    pg.evaluate(f"window.scrollTo(0,{int(track*fr)})"); pg.wait_for_timeout(250)
                    pg.screenshot(path=OUT+f'm390-zoom-p{int(fr*100)}.png')
                pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(200); y=0
                while y<H:
                    pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(50); y+=300
                pg.wait_for_timeout(1200)
            pg.screenshot(path=OUT+f'm{w}-full.png', full_page=True)
            if w==390:
                cut=pg.evaluate("document.getElementById('hero').offsetHeight - innerHeight")
                for k,yy in enumerate(range(cut, H-844+1, 800)):
                    pg.evaluate(f"window.scrollTo(0,{yy})"); pg.wait_for_timeout(700)
                    pg.screenshot(path=OUT+f'm390-white-{k}.png')
            print(w,'overflow', overflow(pg), 'errs', errs); c.close()
    if 'all' in what or 'rm' in what:
        c,pg,errs=ctx(1440,900,reduced=True)
        pg.screenshot(path=OUT+'rm-fold.png')
        H=pg.evaluate("document.documentElement.scrollHeight"); y=0
        while y<H:
            pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(50); y+=300
        pg.wait_for_timeout(1200); pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300)
        pg.screenshot(path=OUT+'rm-full.png', full_page=True)
        pg.evaluate("window.scrollTo(0, innerHeight*1.3)"); pg.wait_for_timeout(400)
        pg.screenshot(path=OUT+'rm-frame.png')
        print('rm images', pg.evaluate("Array.from(document.images).map(i=>[i.currentSrc.split('/').pop(), i.complete && i.naturalWidth>0])"))
        print('rm overflow', overflow(pg), 'errs', errs, pg.evaluate("document.documentElement.className"))
        c.close()
    b.close()
