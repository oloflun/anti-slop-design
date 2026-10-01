# V3f · Rutverket · byggspec

**Greppet, i en mening:** hela sidan är ETT kontinuerligt, hårt rutnät av celler i full
bredd (0 gap, 1 px svarta skarvar, radie 0). Varje cell är antingen **platt** (vit, grå,
svart eller mint, med jättetypografi) eller **bild** (kundverkens egna bilder,
rastrerade till 1-bitars dither). Diagonalt motstående celler delar tema. När en
bildcell kommer in i vyn **löses rastret upp till full färg** ("det första intrycket är
digitalt": skärmen tänds innan texten läses).

Detta är en reimagination av V3d: samma copy, samma bevis, annan visuell idé.
Inte ett dokument: bildcellerna ska täcka **minst 30 %** av sidans yta vid 1440.

## 1. Källor (läs först)

- Copy-facit: `tests/alunix-r8/runs/V3d/index.html`. Varje synlig sträng ordagrant.
  Noll påhittad text (inga etiketter, klockor, "nr 01"-mikrotexter som inte finns i V3d).
  Undantag: V3d:s SVG-processritning (K3 äger den) får utgå.
  `SEO&#8209;optimering` bär U+2011. `Eller mejla oss direkt på kontakt@alunix.se`.
  Hyperborea är **bild i tesen**, aldrig ett case.
- Mekanik att ärva från `tests/alunix-r8/runs/V3e/index.html`: lat montering av
  Calyx/Hōrai-iframes i samma `update()`-svep som scroll (inte IntersectionObserver),
  och den klibbande inbäddningen (`position:sticky`).
- Referens: Inspo `aspensearch-com` (Split Studio). Tokens nedan är hämtade med
  `get_design_system`, inte gissade. Lån från `cyphr-studio`: rutmönstrets
  pixelupplösning mellan bild och platt yta (endast som rörelse).

## 2. Tokens (Aspen Search, anpassade)

```
--paper #ffffff   --ink #232323   --black #000000   --grey #d9d9d9
--mint #0af474 (enda accent, platta cellfyllningar, aldrig text på vitt)
--mint-soft #a3fbcb
radie 0 överallt. Skarvar: 1px solid #000.
Typ: Geist 500 (assets/fonts/geist-500-latin.woff2) för ALLT display + brödtext,
     letter-spacing -0.04em på display, -0.02em på bröd. Geist Mono 400 för index/mono.
     Geist 700 och Public Sans 300 används inte.
Skala (Aspen, fluid 375→1600):
  headline-50 clamp(52px → 200px) lh .8   (sidans jätteord)
  headline-40 clamp(40px → 100px) lh 1
  headline-20 clamp(32px → 48px)  lh 1
  h3 38px lh 1.1 · body 16px lh 1.3 · body-30 clamp(24px→32px) lh 1.1
  caption 12-14px mono
Container: 1440 max för rutnätet; innehåll i celler har padding 20px (Aspen: 8/20-skala).
```

## 3. Cellkarta (desktop 1440; 12 kolumner, celler om 6 eller 3 kolumner)

1. **Topplist** 48px: svart logocell (logo-white.svg) | ALUNIX | kontakt@alunix.se. Sticky.
2. **Hero, 2×2 kvadranter, exakt `100svh` minus topplist** (heroGuidance: allt i första vyn):
   - ÖV vit: h1 `Er hemsida är nutidens visitkort` i headline-40..50, 2-3 rader, nedre vänster i cellen.
   - ÖH bild: `k1-stage-pool.webp` dithrad. **Visitkortet** ligger OVANPÅ skarven ÖH/NH
     som fysiskt objekt (proportion 85:55, skugga), och vänds 180° (rotateY) på scroll
     under första ~60 % av heron. Framsida: motivbild + logo. Baksida: `Alunix`,
     `Digital byrå`, `Design`, `Utveckling`, `System`, `Boka ett möte` (samma strängar
     som V3d). Ärv kortets innehåll från V3d, inte dess stil.
   - NV bild: `k4-cabin-desk.webp` dithrad.
   - NH mint: tom platt yta som kortet vilar mot (eller den dolda sr-meningen).
3. **Tes**: fullbredds svart cell med `Det första intrycket är digitalt.` i headline-50,
   vit, får skäras av högerkanten. Under: 6+6. Vänster: de tre övriga meningarna som
   tre celler staplade (vit, grå, vit) i headline-20. Höger: Hyperborea-bilden i
   bildcell som löses upp från dither till färg.
4. **Process**: vänster 6 kol grå cell, `Vår process:` mono + `Från samtal till
   lanserad sida.` i headline-40 + undertext, sticky. Höger 6 kol svart: 7 steg som
   rader med mono-index, h3 vit, brödtext i #bdbdbd, 1px skarvar mellan.
5. **Exempelcase**: fullbredd, ordet `Exempelcase` i headline-50 i vit cell vänster 6,
   dithrad `demo-calyx.webp` + `demo-horai.webp` sida vid sida höger.
6. **Calyx**: 7+5. Vänster 7 kol: klibbande levande iframe `/sites/calyx.html` (sticky
   top 48px + ev. ram-inset 20px) i en cell. Höger 5 kol: casehuvud-cell (namn i
   headline-40, `Florist, Stockholm` mono) + fem cellrader vit/grå omväxlande
   (h3 + text). Casets egen färg: hämta en dominerande färg ur Calyx-sajten och
   använd den ENDAST som fyllning i casehuvudets cell.
7. **Hōrai**: spegelvänd (5+7), cellerna svarta i stället för vit/grå, samma logik.
8. **Pris**: reference `pricing/tier-bento` (get_reference_jsx): ledande nivå spänner
   2×2 i mint, de två andra i vit och grå. Innehåll = V3d:s tre prisrader ordagrant.
   Det tabellmässiga ur V3e (tabular-nums, högerställda siffror) behålls.
9. **Kontakt**: Aspens avslutning: jätteord ur V3d:s kontaktcopy i headline-50 över
   dithrad bildcell, med visitkortets baksida (samma kort som i heron, nu stilla) i en
   cell. Mejllänk och boka-länk synliga, 44px mål.
10. **Footer**: svart cell med jättelikt `ALUNIX` (headline-50+ bredd, skuret av
    nederkanten) + V3d:s footer-strängar.

Mobil (<768): allt blir en kolumn, celler staplas, bildceller min-height 60vw,
iframes inte sticky men fortfarande levande, kortet ryms inom viewport.
Tablet 768-1199: 6+6 behålls där det går, 7+5 blir staplat.

## 4. Dither + upplösning (tekniken)

- Generera dithrade varianter med Pillow i `assets/dither/` (Floyd-Steinberg 1-bit,
  bilden nedskalad till ~1/3 och uppskalad NEAREST så punkterna syns, svart på #d9d9d9
  eller vit på svart beroende på cell). WebP, lossless.
- I cellen: dithervarianten under, färgbilden över med en **rutmönstermask** (Cyphr):
  ett 12×12-rutnät av rutor som tänds i en förutbestämd pseudo-slumpordning styrd av
  scrollprogress (CSS-variabel satt i samma `update()`-svep). Inga övergångar som
  faller på `prefers-reduced-motion`: rörelse spelar alltid (F-011).
- Bildcellerna i heron förblir dithrade (de är ramen); tes-, case- och kontaktbilder
  löses upp.

## 5. Spärrar (omdöme, ingen hook stoppar dig)

em-dash i synlig text: noll. Ingen lila/indigo, ingen gradient-mesh, ingen glasmorfism,
inga tre lika kort, ingen 8 px-radius, inga beskrivande mikrotexter.
spacingGuidance: blockrytm mellan sektionsgrupper 96-140 px där celler inte ligger
kant i kant; text rör aldrig viewportkanten (min 20 px). Ingen horisontell overflow vid
390/768/1440/1920. `<meta charset="utf-8">`.

## 6. Leverans

`tests/alunix-r8/runs/V3f/index.html` (en fil, inline CSS/JS, relativa assets + repo-
absoluta `/sites/*.html` och `/tests/alunix-concepts-r3/build/assets/*`).
Serveras med `python skills/design/scripts/serve.py --port 3305 --root .` från repo-roten.
`RAPPORT.md` i samma mapp med uppmätta värden.
