import sys, json
from playwright.sync_api import sync_playwright
URL='http://127.0.0.1:3101/tests/alunix-ab-r6/runs/B/K1/index.html'
OUT='shots/'
OVF="""() => { const vw=document.documentElement.clientWidth; const bad=[];
 for (const el of document.querySelectorAll('body *')) { const r=el.getBoundingClientRect();
  if (r.width>0 && (r.right>vw+1 || r.left<-1)) { const cs=getComputedStyle(el); if(cs.visibility==='hidden'||cs.display==='none') continue;
   if (el.closest('#plate')) continue; bad.push(el.tagName+'.'+el.className+' '+Math.round(r.left)+'..'+Math.round(r.right)); } }
 return {sw:document.documentElement.scrollWidth, vw, bad: bad.slice(0,12)}; }"""
what = sys.argv[1] if len(sys.argv)>1 else 'all'
with sync_playwright() as p:
    b=p.chromium.launch()
    def ctx(w,h,reduce=False):
        c=b.new_context(viewport={'width':w,'height':h},reduced_motion='reduce' if reduce else 'no-preference',device_scale_factor=1)
        pg=c.new_page(); errs=[]
        pg.on('console',lambda m: errs.append(m.type+': '+m.text) if m.type in('error','warning') else None)
        pg.on('pageerror',lambda e: errs.append('pageerror: '+str(e)))
        return pg,errs
    if what in('all','desk'):
        pg,errs=ctx(1440,900); pg.goto(URL,wait_until='domcontentloaded',timeout=60000); pg.wait_for_timeout(1800)
        pg.screenshot(path=OUT+'desk-fold.png')
        print('iframe title:', pg.evaluate("document.getElementById('horai').contentDocument && document.getElementById('horai').contentDocument.title"))
        # signature frames
        for f in ['0.35','0.7','0.92']:
            pg.evaluate(f"scrollTo(0, innerHeight*2.6*{f})"); pg.wait_for_timeout(900)
            pg.screenshot(path=OUT+f'desk-zoom-{f}.png')
        pg.evaluate("scrollTo(0, innerHeight*2.6+innerHeight*0.3)"); pg.wait_for_timeout(900); pg.screenshot(path=OUT+'desk-hold.png')
        print('overflow at hold', pg.evaluate(OVF))
        # scroll through in 300px steps, then full page
        H=pg.evaluate('document.documentElement.scrollHeight'); y=0
        while y<H:
            pg.evaluate(f'scrollTo(0,{y})'); pg.wait_for_timeout(70); y+=300
        pg.wait_for_timeout(1500)
        print('overflow at end', pg.evaluate(OVF))
        print('unrevealed', pg.evaluate("document.querySelectorAll('.rv:not(.in)').length"))
        pg.screenshot(path=OUT+'desk-full.png',full_page=True)
        pg.evaluate("scrollTo(0, innerHeight*3.2)"); pg.wait_for_timeout(700); pg.screenshot(path=OUT+'desk-cut.png')
        pg.evaluate("scrollTo(0, innerHeight*3.2-2)"); pg.wait_for_timeout(700); pg.screenshot(path=OUT+'desk-precut.png')
        pg.evaluate("document.getElementById('ledger').scrollIntoView({block:'center'})"); pg.wait_for_timeout(1200); pg.screenshot(path=OUT+'desk-ledger.png')
        pg.evaluate("scrollTo(0, document.documentElement.scrollHeight)"); pg.wait_for_timeout(1200); pg.screenshot(path=OUT+'desk-close.png')
        print('desk console:', errs)
    if what in('all','mob'):
        for w,h,name in [(390,844,'mob390'),(320,700,'mob320'),(768,1024,'tab768')]:
            pg,errs=ctx(w,h); pg.goto(URL,wait_until='domcontentloaded',timeout=60000); pg.wait_for_timeout(1500)
            pg.screenshot(path=OUT+f'{name}-fold.png')
            H=pg.evaluate('document.documentElement.scrollHeight'); y=0
            while y<H:
                pg.evaluate(f'scrollTo(0,{y})'); pg.wait_for_timeout(50); y+=300
            pg.wait_for_timeout(1400)
            print(name,'overflow', pg.evaluate(OVF), 'unrevealed', pg.evaluate("document.querySelectorAll('.rv:not(.in)').length"))
            pg.screenshot(path=OUT+f'{name}-full.png',full_page=True)
            print(name,'console:',errs)
    if what in('all','rm'):
        pg,errs=ctx(1440,900,True); pg.goto(URL,wait_until='domcontentloaded',timeout=60000); pg.wait_for_timeout(1500)
        print('reduced overflow', pg.evaluate(OVF), 'motion class', pg.evaluate("document.documentElement.className"))
        pg.screenshot(path=OUT+'desk-reduced-full.png',full_page=True)
        pg.evaluate("scrollTo(0, innerHeight)"); pg.wait_for_timeout(600); pg.screenshot(path=OUT+'desk-reduced-frame.png')
        print('reduced console:',errs)
        pg,errs=ctx(1440,900); pg.goto(URL,wait_until='domcontentloaded',timeout=60000); pg.wait_for_timeout(1000)
        pg.evaluate("[...document.querySelectorAll('.rv')].forEach(e=>e.classList.remove('in'))")
        # simulate JS never running: static state = no .motion class
        pg.evaluate("document.documentElement.classList.remove('motion')"); pg.wait_for_timeout(300)
        print('no-motion hidden count', pg.evaluate("[...document.querySelectorAll('.rv')].filter(e=>getComputedStyle(e).opacity==='0').length"))
    b.close()
