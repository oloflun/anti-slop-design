import sys, json, asyncio, os
from playwright.sync_api import sync_playwright
URL="http://127.0.0.1:3101/tests/alunix-ab-r6/runs/B/K1/index.html"
OUT="C:/Users/Anton L/anti-slop-design/tests/alunix-ab-r6/runs/B/K1/shots"
os.makedirs(OUT,exist_ok=True)
tag=sys.argv[1] if len(sys.argv)>1 else "r1"
OVERFLOW_JS="""() => {
 const vw=document.documentElement.clientWidth; const bad=[];
 for(const el of document.querySelectorAll('body *')){
   const r=el.getBoundingClientRect(); if(r.width===0) continue;
   let clipped=false; for(let a=el.parentElement;a&&a!==document.body;a=a.parentElement){const o=getComputedStyle(a).overflowX; if(o==='hidden'||o==='clip'){clipped=true;break}}
   if(clipped) continue;
   if(r.right>vw+1||r.left<-1){ const cs=getComputedStyle(el); bad.push({tag:el.tagName,cls:el.className&&el.className.baseVal!==undefined?'':String(el.className).slice(0,40),l:Math.round(r.left),r:Math.round(r.right),tr:cs.transform!=='none'}); }
 }
 return {sw:document.documentElement.scrollWidth, vw, bad:bad.slice(0,12)};
}"""
with sync_playwright() as pw:
    b=pw.chromium.launch()
    def run(w,h,name,steps=True,reduced=False,mid=False):
        ctx=b.new_context(viewport={'width':w,'height':h},device_scale_factor=1,reduced_motion='reduce' if reduced else 'no-preference')
        pg=ctx.new_page(); errs=[]
        pg.on('console',lambda m: errs.append((m.type,m.text)) if m.type in('error','warning') else None)
        ASSETS="C:/Users/Anton L/anti-slop-design/tests/alunix-ab-r6/runs/B/K1/assets/"
        def serve(route):
            name=route.request.url.split('/assets/')[1].split('?')[0]
            ct='image/svg+xml' if name.endswith('.svg') else 'image/webp'
            route.fulfill(path=ASSETS+name,content_type=ct)
        pg.route('**/runs/B/K1/assets/*',serve)
        pg.on('requestfailed',lambda r: errs.append(('reqfail',r.url,r.failure)))
        pg.on('pageerror',lambda e: errs.append(('pageerror',str(e))))
        pg.goto(URL,wait_until='networkidle'); pg.wait_for_timeout(600)
        pg.screenshot(path=f"{OUT}/{tag}-{name}-fold.png")
        if mid:
            end=pg.evaluate("document.getElementById('skyTrack').offsetHeight-innerHeight")
            for i,p in enumerate([0.25,0.5,0.72,0.9,1.0]):
                pg.evaluate(f"scrollTo(0,{end*p})"); pg.wait_for_timeout(250)
                pg.screenshot(path=f"{OUT}/{tag}-{name}-zoom{i}-p{int(p*100)}.png")
            # after track end + 100vh (pinned frame), then +200vh (white starts)
            for i,extra in enumerate([0.0,0.5,1.0]):
                pg.evaluate(f"scrollTo(0,{end}+innerHeight*{extra})"); pg.wait_for_timeout(300)
                pg.screenshot(path=f"{OUT}/{tag}-{name}-frame{i}.png")
        if steps:
            total=pg.evaluate("document.documentElement.scrollHeight")
            y=0
            while y<total:
                pg.evaluate(f"scrollTo(0,{y})"); pg.wait_for_timeout(60); y+=300
            pg.wait_for_timeout(1300)
            pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(300)
        pg.screenshot(path=f"{OUT}/{tag}-{name}-full.png",full_page=True)
        ov=pg.evaluate(OVERFLOW_JS)
        titles=pg.evaluate("Array.from(document.querySelectorAll('iframe')).map(f=>{try{return f.contentDocument&&f.contentDocument.title}catch(e){return 'ERR '+e}})")
        fonts=pg.evaluate("Array.from(document.fonts).filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight)")
        print(name, 'errors:',errs, '| overflow:',json.dumps(ov), '| iframe titles:',titles, '| fonts:',sorted(set(fonts)))
        ctx.close()
    run(1440,900,'d1440',mid=True)
    run(390,844,'m390')
    run(1440,900,'reduced',steps=False,reduced=True)
    for w in (320,768):
        ctx=b.new_context(viewport={'width':w,'height':800}); pg=ctx.new_page()
        pg.route('**/runs/B/K1/assets/*',lambda route: route.fulfill(path="C:/Users/Anton L/anti-slop-design/tests/alunix-ab-r6/runs/B/K1/assets/"+route.request.url.split('/assets/')[1].split('?')[0]))
        pg.goto(URL,wait_until='networkidle'); pg.wait_for_timeout(400)
        total=pg.evaluate("document.documentElement.scrollHeight"); y=0
        while y<total: pg.evaluate(f"scrollTo(0,{y})"); pg.wait_for_timeout(40); y+=400
        pg.wait_for_timeout(1200); print(w,'overflow:',json.dumps(pg.evaluate(OVERFLOW_JS))); 
        if w==320: pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(200); pg.screenshot(path=f"{OUT}/{tag}-w320-full.png",full_page=True)
        ctx.close()
    b.close()
