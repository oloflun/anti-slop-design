from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3202/tests/alunix-ab-r7/runs/B/K2/index.html"

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(300)
    close_top = page.evaluate("document.getElementById('closeAct').offsetTop")
    close_height = page.evaluate("document.getElementById('closeAct').offsetHeight")
    vh = 900
    span = close_height + vh
    worst = (999, None)
    for i in range(0, 46):
        raw = i / 100.0
        y = max(close_top - vh + raw * span, 0)
        page.evaluate(f"window.scrollTo(0, {y})")
        page.wait_for_timeout(60)
        ratio = page.evaluate("""
            () => {
                function toRGB(str) { const c=document.createElement('canvas'); c.width=1;c.height=1; const ctx=c.getContext('2d'); ctx.fillStyle=str; ctx.fillRect(0,0,1,1); return ctx.getImageData(0,0,1,1).data; }
                function luminance(rgb) { const [r,g,b]=[rgb[0],rgb[1],rgb[2]].map(v=>{v/=255; return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);}); return 0.2126*r+0.7152*g+0.0722*b; }
                const el = document.getElementById('closeAct');
                const bg = toRGB(getComputedStyle(document.body).backgroundColor);
                const fg = toRGB(getComputedStyle(el).color);
                const L1=luminance(bg), L2=luminance(fg);
                const lighter=Math.max(L1,L2), darker=Math.min(L1,L2);
                return (lighter+0.05)/(darker+0.05);
            }
        """)
        if ratio < worst[0]:
            worst = (ratio, raw)
    print("worst contrast:", worst)
    ctx.close()
    browser.close()
