from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
OUT = Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3d\shots\astra-r23")
REF = Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3c\shots\fasA")
PAIRS = [
 ("Q01","A05-1920.png", REF/"highway-1440/hw-hemsida-1440--s03.png"),
 ("Q02","A07-1920.png", REF/"insign-1440/insign-1440--s03.png"),
 ("Q03","A11-1920.png", REF/"hoy-1440/hoy-webb-1440--s03.png"),
 ("Q04","A14-1920.png", REF/"highway-1440/hw-hemsida-1440--s03.png"),
 ("Q05","A16-1920.png", REF/"hoy-1440/hoy-home-1440--s03.png"),
 ("Q06","A03-390.png",  REF/"highway-390/hw-hemsida-390--s05.png"),
 ("Q07","A05-390.png",  REF/"insign-390/insign-390--s03.png"),
 ("Q08","A10-390.png",  REF/"hoy-390/hoy-webb-390--s03.png"),
 ("Q09","C02-1920.png", OUT/"C06-1920.png"),
 ("Q10","C02-1920.png", REF/"highway-1440/hw-hemsida-1440--s02.png"),
 ("Q11","C02-390.png",  OUT/"C06-390.png"),
 ("Q12","P02-1920.png", REF/"hoy-1440/hoy-home-1440--s08.png"),
 ("Q13","P02-390.png",  REF/"insign-390/insign-390--s10.png"),
]
CAP = {
 "Q01":"VAR: tes -> ritning, scrollY 6720 av 1920x930. REF: highway, ingang till Sa arbetar vi",
 "Q02":"VAR: tes -> ritning, scrollY 6800 (planet 51% av ytan). REF: insign, tjansteavsnitt",
 "Q03":"VAR: tes -> ritning, scrollY 7061 (arket landat). REF: hoy, citatskarm",
 "Q04":"VAR: tes -> ritning, scrollY 7440 (tomt ark ovanfor rubriken). REF: highway processingang",
 "Q05":"VAR: kapitelskarmen, scrollY 7700. REF: hoy kapitelskarm",
 "Q06":"VAR 390: scrollY 5960, NOLL textrutor pa skarmen. REF: highway 390",
 "Q07":"VAR 390: scrollY 6080, planet + tom bla yta. REF: insign 390",
 "Q08":"VAR 390: scrollY 6408, tva tomma lador staplade. REF: hoy 390",
 "Q09":"BADA AR VARA: vanster = kapitelrubriken Exempelcase (136px), hoger = caset Calyx (171px) en skarm senare",
 "Q10":"VAR: Exempelcase-skarmen. REF: highway, rubriken Case direkt ovanfor sina kort",
 "Q11":"BADA AR VARA 390: vanster Exempelcase (40px), hoger Calyx (36px)",
 "Q12":"VAR: prissektionen 1920, siffror i Young Serif 64px. REF: hoy pris/liggare",
 "Q13":"VAR: prissektionen 390, siffror i Young Serif 32px. REF: insign 390 pris",
}
for tag, a, b in PAIRS:
    pa = OUT/a if isinstance(a,str) else a
    pb = Path(b)
    if not pa.exists() or not pb.exists():
        print("MISSING", tag, pa.exists(), pb.exists()); continue
    x = Image.open(pa).convert("RGB"); y = Image.open(pb).convert("RGB")
    h = max(x.height, y.height)
    x = x.resize((int(x.width*h/x.height), h)); y = y.resize((int(y.width*h/y.height), h))
    s = Image.new("RGB", (x.width+28+y.width, h+28), "white")
    s.paste(x,(0,0)); s.paste(y,(x.width+28,0))
    try: f = ImageFont.truetype("arial.ttf", 15)
    except Exception: f = None
    ImageDraw.Draw(s).text((4,h+6), f"{tag}  {CAP[tag]}", fill="black", font=f)
    s.save(OUT/f"{tag}.png")
    print("ok", tag)
