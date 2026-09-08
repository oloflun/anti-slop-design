from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    page.set_content("<html><body></body></html>")
    data = page.evaluate("""
        () => {
            function toRGB(str) {
                const c = document.createElement('canvas'); c.width=1; c.height=1;
                const ctx = c.getContext('2d');
                ctx.fillStyle = str; ctx.fillRect(0,0,1,1);
                return ctx.getImageData(0,0,1,1).data;
            }
            function luminance(rgb) {
                const [r,g,b] = [rgb[0],rgb[1],rgb[2]].map(v => {
                    v /= 255;
                    return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4);
                });
                return 0.2126*r + 0.7152*g + 0.0722*b;
            }
            function contrast(a, b) {
                const La = luminance(toRGB(a)), Lb = luminance(toRGB(b));
                const lighter = Math.max(La,Lb), darker = Math.min(La,Lb);
                return (lighter+0.05)/(darker+0.05);
            }
            const ink = 'oklch(22% 0.012 150)';
            const paper = 'oklch(85% 0.028 135)';
            const dark = '#1b1f1c';
            const rows = [];
            for (let i = 0; i <= 20; i++) {
                const pct = i * 5;
                const bg = `color-mix(in oklch, ${dark} ${pct}%, ${paper})`;
                const cInk = contrast(ink, bg);
                const cPaper = contrast(paper, bg);
                rows.push({pct, cInk: +cInk.toFixed(2), cPaper: +cPaper.toFixed(2), best: +Math.max(cInk,cPaper).toFixed(2)});
            }
            return rows;
        }
    """)
    for r in data:
        print(r)
    browser.close()
