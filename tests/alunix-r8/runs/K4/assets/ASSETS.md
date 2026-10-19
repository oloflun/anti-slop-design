# K4, assetpaket

F-009: arkitekten specificerar, **lead vendorar**. Byggaren kopierar ingenting hit och
genererar ingenting.

**Noll genererat material i den här cellen.** Higgsfield är ute (`balance` ger
`{"credits":0,"subscription_plan_type":"free"}`, en enda privat workspace, free plan, mätt av
lead 2026-09-09), så steg 1 och 2 i planens § 10.6 faller. Men K4 behövde aldrig genererat
material, och skälet är principiellt snarare än praktiskt: cellens hela argument är att allt
som visas är verkligt och mätbart. En genererad bild vore ett påhittat objekt i en sida vars
tes är att den inte hittar på något. **Ingen asset-lock för en genererad bild skrivs, och
ingen bildprompt författas.** Material som letar efter en användning är inte tillåtet. Raden
står också i `NOTES.md` och i `runs/K4/BRIEF.md` § decision ledger.

---

## 1 · Vad K4 faktiskt behöver

Fyra medieplatser. Två av dem är levande filer i repot och kräver ingen vendorering alls; två
är skärmbilder som måste skjutas.

| # | Roll | Typ | Källa | Status |
|---|---|---|---|---|
| 1 | "Före"-lagret i folden | **live `<iframe>`** | `/sites/before-ai-slop.html` | Finns, se § 2 |
| 2 | "Efter"-lagret i folden | **live `<iframe>`** | `/sites/calyx.html` | Finns, se § 2 |
| 3 | Hōrai som full-bleed objekt i a3 | **skärmbild** `.webp` | `/sites/horai.html` vid 1440 och 390 | Måste skjutas om, se § 3 |
| 4 | Hyperborea som full-bleed objekt i a3 | **skärmbild** `.webp` | `/sites/hyperborea.html` vid 1440 och 390 | Måste skjutas om, se § 3 |

Utöver det: motorns tre filer, som i alla celler.

| # | Roll | Källsökväg | Målsökväg |
|---|---|---|---|
| 5 | Motorn, JS | `~/.claude/skills/design/scripts/scroll/scrollcraft.js` | `tests/alunix-r8/runs/K4/scroll/scrollcraft.js` |
| 6 | Motorn, CSS | `~/.claude/skills/design/scripts/scroll/scrollcraft.css` | `tests/alunix-r8/runs/K4/scroll/scrollcraft.css` |
| 7 | Utjämningsshimen (`--sc-ps`) | `~/.claude/skills/design/scripts/scroll/sc-smooth.js` | `tests/alunix-r8/runs/K4/scroll/sc-smooth.js` |

`template.html` läses av byggaren på plats för stage-markupen och kopieras inte in.
`scroll/NOTE.md`: copy, never edit.

**Ingen logotypfil behövs.** K4 har inget ordmärke någonstans: navigationen är delaren och
folden innehåller exakt fem element i K4:s eget lager. `logo-white.svg` och `logo-black.svg`
kopieras **inte** in.

---

## 2 · De två live-ramarna, bekräftade på disk

`ls -la sites/before-ai-slop.html sites/calyx.html sites/horai.html sites/hyperborea.html`,
kört av mig 2026-09-09:

```
-rw-r--r-- 1 Anton L 197121  9016 Jun 11 15:53 sites/before-ai-slop.html
-rw-r--r-- 1 Anton L 197121 16238 Sep  9 01:47 sites/calyx.html
-rw-r--r-- 1 Anton L 197121 31495 Sep  9 01:47 sites/horai.html
-rw-r--r-- 1 Anton L 197121 32136 Sep  9 01:47 sites/hyperborea.html
```

`curl` mot den lokala servern, samma dag:

```
python "C:/Users/Anton L/.claude/skills/design/scripts/serve.py" --port 3399 --root .
curl -s -o /dev/null -w "%{http_code}" http://localhost:3399/sites/calyx.html          -> 200
curl -s -o /dev/null -w "%{http_code}" http://localhost:3399/sites/before-ai-slop.html -> 200
```

**Båda ramarna är alltså bekräftade, både som filer och över samma origin.** Ingen av dem
kopieras in i `assets/`: de refereras med rot-relativa sökvägar (`/sites/...`) och serveras
från repo-roten enligt PRODUCT.md § Operating Context.

**Nyckeltal som prestandaplanen bygger på, mätta ur filerna:**

- `before-ai-slop.html`: 9 016 B. `<img>` 0 · `<picture>` 0 · `srcset` 0 · externa
  bildvärdar 0. Den enda `url()` i filen är `url(#g)`, en intern referens till den falska
  sparklinens SVG-gradient. **Den kostar i praktiken bara sin egen HTML plus Tailwinds
  CDN-script.**
- `calyx.html`: 16 238 B, men **fyra externa Unsplash-fotografier** hämtade via
  `background-image: url('https://images.unsplash.com/...')` vid `w=1600`, `w=1600`, `w=2000`
  och `w=2400`, plus en `data:image/svg+xml`-grain. Filen redigeras aldrig, alltså kan K4 inte
  påverka de bytesen. Det är budgetens svåraste post och den har en egen beslutsregel i
  `BRIEF.md` § Prestandaplan.

**Etiketten på vänsterhalvan är obligatorisk och ordagrann:** `En typisk mallsida`. Aldrig ett
påhittat kundnamn, aldrig ett varumärke, aldrig en förkortning, aldrig utelämnad. Det är den
enda anledningen till att en anti-referens får köras som innehåll på en Alunix-sida.

---

## 3 · Demo-skärmbilder: vad som finns att ärva, och vad som måste skjutas om

### Vad som finns

`ls tests/alunix-concepts-r3/build/assets/`, kört av mig 2026-09-09:

```
demo-calyx.webp
demo-horai.webp
demo-hyperborea.webp
hero-console.webp
k1-stage-beams.webp
k1-stage-pool.webp
k4-cabin-desk.webp
k4-desk-overhead.webp
logo-black.svg
logo-white.svg
```

Dimensioner och storlek, lästa med PIL:

```
demo-calyx.webp       (1200, 750)  133942 B
demo-horai.webp       (1200, 750)   74334 B
demo-hyperborea.webp  (1200, 750)   46952 B
```

Alla tre är alltså **skrivbordsbredd i 1,6-format** (samma proportion som 1440 × 900,
nedskalad till 1200 × 750), daterade `Sep 4 12:42`.

### Vilka som räcker, och vilka som inte gör det

**Ingen av dem räcker, av två oberoende skäl.**

**Skäl 1: de tre sajtfilerna har ändrats efter att bilderna togs.** Bilderna är daterade
2026-09-04; `horai.html` och `hyperborea.html` är daterade 2026-09-09 01:47. Ändringen är
verifierad i git, inte antagen:

```
git status --porcelain sites/
 M sites/calyx.html
 M sites/horai.html
 M sites/hyperborea.html
 ...
git diff HEAD -- sites/calyx.html sites/hyperborea.html
-  @media (prefers-reduced-motion: reduce) { .reveal { opacity:1; transform:none; transition:none; } }
+  /* F-011: reduced-motion-blocket utgår, rörelsen spelas alltid (superseded 2026-09-07) */
```

Ändringen är i sig liten, men den träffar **exakt det läge skärmbilderna tas i**:
`shoot.py` startar sin browser med `reduced_motion="reduce"` (uttryckligen, med F-011 som
kommentar i källan). Före ändringen tvingade `@media (prefers-reduced-motion: reduce)`
`.reveal { opacity: 1 }`, alltså syntes allt. Efter ändringen finns ingen sådan gren, så
element under vecket står i sitt pre-reveal-läge tills IntersectionObserver utlöser dem.
De ärvda bilderna kan därför visa ett tillstånd sidan inte längre har. Det ligger som **Q13**
i `QUESTIONS.md`.

**Skäl 2: det finns ingen 390-bild alls.** K4 behöver båda bredderna, och katalogen innehåller
bara skrivbordsbredd.

**Slutsats:** `demo-horai.webp` och `demo-hyperborea.webp` **skjuts om vid 1440** och
**skjuts nya vid 390**. `demo-calyx.webp` behövs inte som medieplats (Calyx körs live) men
**kopieras in som reserv** enligt beslutsregeln i `BRIEF.md` § Prestandaplan.

### Kommandoraden som producerar dem, för lead

**Vid 1440 × 900** använder `shoot.py` sin egen fasta viewport och behöver ingen breddflagga.
Från repo-roten, med servern igång på 3399:

```
python "$HOME/.claude/skills/design/scripts/serve.py" --port 3399 --root .

python "$HOME/.claude/skills/design/scripts/shoot.py" \
  tests/alunix-r8/runs/K4/shots/1440 \
  http://localhost:3399/sites/horai.html \
  http://localhost:3399/sites/hyperborea.html \
  http://localhost:3399/sites/calyx.html
```

Det skriver `<slug>--fold.png` och `<slug>--full.png` per URL. **Vi vill ha fold-bilden**,
eftersom medieplatsen är ett full-bleed objekt i en 16:10-ruta, inte en hel sida.

**Vid 390 finns ingen färdig väg.** `shoot.py` och `shoot_slices.py` har båda `WIDTH = 1440`
hårdkodat och tar ingen breddflagga — kontrollerat i källan, inte antaget. Lead kör därför
detta i stället, som är samma anrop med en annan viewport och samma `reduced_motion="reduce"`
som `shoot.py` sätter:

```
python - <<'PY'
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

OUT = Path("tests/alunix-r8/runs/K4/shots/390")
URLS = [
    ("horai",       "http://localhost:3399/sites/horai.html"),
    ("hyperborea",  "http://localhost:3399/sites/hyperborea.html"),
    ("calyx",       "http://localhost:3399/sites/calyx.html"),
]

async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        page = await b.new_page(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
            reduced_motion="reduce",   # samma hostila installning som shoot.py, F-011
        )
        for slug, url in URLS:
            await page.goto(url, wait_until="networkidle", timeout=60000)
            await page.wait_for_timeout(1500)
            path = OUT / f"{slug}--fold-390.png"
            await page.screenshot(path=str(path))
            print(url, "->", path)
        await b.close()

asyncio.run(main())
PY
```

**Konvertering till `.webp` och målsökvägar** (lead kör, byggaren rör inte filerna):

```
python - <<'PY'
from PIL import Image
from pathlib import Path
jobs = [
    ("tests/alunix-r8/runs/K4/shots/1440/localhost-3399-sites-horai-html--fold.png",
     "tests/alunix-r8/runs/K4/assets/demo-horai-1440.webp"),
    ("tests/alunix-r8/runs/K4/shots/1440/localhost-3399-sites-hyperborea-html--fold.png",
     "tests/alunix-r8/runs/K4/assets/demo-hyperborea-1440.webp"),
    ("tests/alunix-r8/runs/K4/shots/1440/localhost-3399-sites-calyx-html--fold.png",
     "tests/alunix-r8/runs/K4/assets/demo-calyx-1440.webp"),
    ("tests/alunix-r8/runs/K4/shots/390/horai--fold-390.png",
     "tests/alunix-r8/runs/K4/assets/demo-horai-390.webp"),
    ("tests/alunix-r8/runs/K4/shots/390/hyperborea--fold-390.png",
     "tests/alunix-r8/runs/K4/assets/demo-hyperborea-390.webp"),
    ("tests/alunix-r8/runs/K4/shots/390/calyx--fold-390.png",
     "tests/alunix-r8/runs/K4/assets/demo-calyx-390.webp"),
]
for src, dst in jobs:
    im = Image.open(src).convert("RGB")
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "WEBP", quality=82, method=6)
    print(dst, im.size, Path(dst).stat().st_size, "B")
PY
```

**Målvärden lead ska kontrollera efter körningen:**

| Fil | Mått | Tak |
|---|---|---|
| `demo-horai-1440.webp` | 1440 × 900 | ≤ 150 kB |
| `demo-hyperborea-1440.webp` | 1440 × 900 | ≤ 150 kB |
| `demo-calyx-1440.webp` (reserv) | 1440 × 900 | ≤ 150 kB |
| `demo-horai-390.webp` | 780 × 1688 (2× av 390 × 844) | ≤ 120 kB |
| `demo-hyperborea-390.webp` | 780 × 1688 | ≤ 120 kB |
| `demo-calyx-390.webp` (reserv) | 780 × 1688 | ≤ 120 kB |

Överskrids ett tak: sänk `quality` till 76 och kör om. Skala aldrig ner måtten — objektet är
full-bleed och en nedskalad bild blir suddig i en 1440-vy.

**Slug-namnen i 1440-körningen är genererade av `shoot.py`s egen `slug()`-funktion**
(`^https?://` bort, allt icke-alfanumeriskt till bindestreck). Skulle de skilja sig från
raderna ovan är det filnamnen på disk som gäller; lead rättar sökvägarna i konverteringen och
noterar det, i stället för att gissa.

---

## 4 · Asset-lock per medieplats

Fyra platser. **Ingen av dem är en generate-prompt.** Två fylls av levande filer i repot, två
av skärmbilder lead skjuter enligt § 3.

```
Asset role:    "Fore"-lagret, foldens vanstra halva
Slot:          full-bleed, 1440x900 vid ps=0, underst av tva lager i samma box;
               synlig bredd = var(--split), som gar 50% -> 0% over a1
Art direction: sites/before-ai-slop.html, live i <iframe>, samma origin, renderad vid sin
               egen naturliga 1440-bredd. Arligt etiketterad `En typisk mallsida` som 11px
               Reddit Mono i ramens ovre vanstra horn, i K4:s eget lager, aldrig inuti ramen.
               Ramen skalas aldrig, transformeras aldrig och flyttas aldrig; bara clip-
               gransen ror sig. Mattnaden faller via filter: saturate() pa WRAPPERN, driven
               av --split.
Avoid:         ett pahittat kundnamn eller varumarke i stallet for etiketten; en ritad
               webblasar- eller telefonram runt ramen (gate 47); en skarmbild i stallet for
               den levande filen medan budgeten haller; transform, scale eller opacity pa
               sjalva ramen; ett skamt, en karikatyr eller ett adjektiv om sidan
```

```
Asset role:    "Efter"-lagret, foldens hogra halva och sidans upplosta yta
Slot:          full-bleed, 1440x900 vid ps=0, overst av tva lager i samma box;
               clip-path: inset(0 0 0 var(--split)) sa att lagret vaxer at vanster
Art direction: sites/calyx.html, live i <iframe>, samma origin, renderad vid sin egen
               naturliga 1440-bredd. Monteras via IntersectionObserver med loading="lazy".
               Bildtexten `Exempelsida: Calyx, florist i Stockholm` ordagrant, 11px Reddit
               Mono, i K4:s eget lager. Ramen ar interaktiv och forblir interaktiv; ett
               osynligt skoldlager laggs over den ENDAST medan pekaren drar delaren, och tas
               bort vid pointerup.
Avoid:         transform, scale, opacity eller filter pa ramen efter att den visats
               (PRODUCT.md SS Operating Context); en ritad ram runt den (gate 47); att ersatta
               den med demo-calyx-1440.webp sa lange budgeten haller; en overlagd rubrik
               inuti ramen
```

```
Asset role:    Horai som full-bleed objekt, a3 objekt 1
Slot:          full-bleed 1440x900 vid skrivbord, 390x844 under 640px; ett objekt per skarm
Art direction: demo-horai-1440.webp / demo-horai-390.webp, skjutna enligt SS 3 mot den
               AKTUELLA filen. Objektet visas helt, aldrig beskuret och aldrig lutat.
               Bildtexten `Exempelsida: Horai, Asian fusion-koncept` ordagrant, 11px Reddit
               Mono, i underkanten, i K4:s eget lager. Ratt Horai-stavning med makron ar
               bindande i den synliga texten.
Avoid:         en ritad enhetsram, en telefonbezel eller trafikljusprickar (gate 47); en
               lutande platta eller ett kort (TASTE SS 2.3); en skugga; en hover-effekt; att
               anvanda den arvda bilden fran 2026-09-04 utan omskjutning (SS 3, skal 1)
```

```
Asset role:    Hyperborea som full-bleed objekt, a3 objekt 2
Slot:          full-bleed 1440x900 vid skrivbord, 390x844 under 640px; ett objekt per skarm
Art direction: demo-hyperborea-1440.webp / demo-hyperborea-390.webp, skjutna enligt SS 3 mot
               den AKTUELLA filen. Bildtexten `Exempelsida: Hyperborea, konferens i Lund`
               ordagrant, 11px Reddit Mono, i underkanten, i K4:s eget lager.
Avoid:         samma lista som Horai; dessutom att lagga de tva objekten sida vid sida, vilket
               skulle aterinfora en split efter upplosningen och darmed motsaga hela avslutet
```

---

## 5 · Reserv, och vad som INTE kopieras in

**Kopieras in som reserv:** `demo-calyx-1440.webp` och `demo-calyx-390.webp` (nyskjutna,
inte de ärvda), så att en trasig Calyx-iframe kan ersättas utan en ny runda, och så att
beslutsregeln i `BRIEF.md` § Prestandaplan kan verkställas.

**Kopieras inte in, med skäl:**

- `k4-cabin-desk.webp`, `k1-stage-pool.webp`, `k1-stage-beams.webp`, `hero-console.webp`,
  `k4-desk-overhead.webp` — fotografiska stillbilder ur r3/r5. **K4 har noll fotografier i
  sitt eget lager.** Det finns ingen plats för dem, och en bild som letar efter en plats är
  precis vad § 10.6 och F-009 finns för att stoppa.
- `logo-white.svg`, `logo-black.svg` — K4 har inget ordmärke. Navigationen är delaren och
  folden har exakt fem element i K4:s eget lager.
- De ärvda `demo-*.webp` från 2026-09-04 — ersatta av omskjutna, se § 3.
- `template.html` — läses på plats, kopieras aldrig.

## 6 · Öppet

- **Q13** (`QUESTIONS.md`): de ärvda demo-skärmbilderna är daterade före F-011-ändringen i
  sajtfilerna. Antagande tills svar: alla demo-bilder skjuts om innan de används. Nästa
  konkreta steg om lead vill spara tid: skjut om vid 1440, lägg den nya bilden bredvid den
  ärvda och läs båda som pixlar; är de identiska räcker den ärvda för 1440 och bara
  390-bilderna behöver skjutas.
- `[fylls i R1]`: byggaren kör `perf_probe.py` mot den monterade sidan och skriver den
  faktiska överföringssiffran, som avgör om båda ramarna får förbli levande.
