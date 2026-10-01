# V3c, assetpaket

F-009: arkitekten specificerar, **lead vendorar**. Byggaren kopierar ingenting hit och
genererar ingenting (Higgsfield är spärrat på byggarens argv).

V3c ärver materialet från `tests/alunix-concepts-r5/cells/V3b-chain/`, som i sin tur
refererar bilder som fysiskt bor i `tests/alunix-concepts-r3/build/assets/`.

## 1 · Filer som ska kopieras in

Kontrollerat på disk 2026-09-09. `ls -la tests/alunix-concepts-r3/build/assets/`:

```
-rw-r--r-- 133942 Sep  4 12:42 demo-calyx.webp
-rw-r--r--  74334 Sep  4 12:42 demo-horai.webp
-rw-r--r--  46952 Sep  4 12:42 demo-hyperborea.webp
-rw-r--r--  21318 Sep  4 13:23 hero-console.webp
-rw-r--r--  16576 Sep  4 22:53 k1-stage-beams.webp
-rw-r--r--  64998 Sep  5 00:51 k1-stage-pool.webp
-rw-r--r--  42240 Sep  4 13:23 k4-cabin-desk.webp
-rw-r--r-- 136356 Sep  4 22:53 k4-desk-overhead.webp
-rw-r--r--   3522 Sep  4 12:43 logo-black.svg
-rw-r--r--   3522 Sep  4 12:43 logo-white.svg
```

`ls "$HOME/.claude/skills/design/scripts/scroll/"`:

```
NOTE.md  sc-smooth.js  scrollcraft.css  scrollcraft.js  template.html
```

| # | Roll | Källsökväg | Målsökväg | Finns |
|---|---|---|---|---|
| 1 | Grund (kontinuerlig svartvit fond, `--sc-canvas`-drift i tre stopp) | `tests/alunix-concepts-r3/build/assets/k4-cabin-desk.webp` | `tests/alunix-r8/runs/V3c/assets/k4-cabin-desk.webp` | ja, 42 240 B |
| 2 | Hero-plåtens framsida (ljuspölen) | `tests/alunix-concepts-r3/build/assets/k1-stage-pool.webp` | `tests/alunix-r8/runs/V3c/assets/k1-stage-pool.webp` | ja, 64 998 B |
| 3 | Demo, Calyx | `tests/alunix-concepts-r3/build/assets/demo-calyx.webp` | `tests/alunix-r8/runs/V3c/assets/demo-calyx.webp` | ja, 133 942 B |
| 4 | Demo, Hōrai | `tests/alunix-concepts-r3/build/assets/demo-horai.webp` | `tests/alunix-r8/runs/V3c/assets/demo-horai.webp` | ja, 74 334 B |
| 5 | Demo, Hyperborea (plåten som bleeder) | `tests/alunix-concepts-r3/build/assets/demo-hyperborea.webp` | `tests/alunix-r8/runs/V3c/assets/demo-hyperborea.webp` | ja, 46 952 B |
| 6 | Logotyp, vit (logo-docken på kortets framsida) | `tests/alunix-concepts-r3/build/assets/logo-white.svg` | `tests/alunix-r8/runs/V3c/assets/logo-white.svg` | ja, 3 522 B |
| 7 | Logotyp, svart (reserv för pappersspalten) | `tests/alunix-concepts-r3/build/assets/logo-black.svg` | `tests/alunix-r8/runs/V3c/assets/logo-black.svg` | ja, 3 522 B |
| 8 | Motorn, JS | `~/.claude/skills/design/scripts/scroll/scrollcraft.js` | `tests/alunix-r8/runs/V3c/scroll/scrollcraft.js` | ja |
| 9 | Motorn, CSS | `~/.claude/skills/design/scripts/scroll/scrollcraft.css` | `tests/alunix-r8/runs/V3c/scroll/scrollcraft.css` | ja |
| 10 | Utjämningsshimen (`--sc-ps`) | `~/.claude/skills/design/scripts/scroll/sc-smooth.js` | `tests/alunix-r8/runs/V3c/scroll/sc-smooth.js` | ja |
| 11 | Geist 700, latin `.woff2` (display på kortbaksidan, den typsatta länken) | Google Fonts, `fonts.gstatic.com`, hämtad av bevakaren 2026-09-10 (F-009: lead/bevakare vendorar) | `tests/alunix-r8/runs/V3c/assets/fonts/geist-700-latin.woff2` | ja, 13 364 B |
| 12 | Geist Mono 400, latin `.woff2` (register, max fyra etiketter) | samma | `tests/alunix-r8/runs/V3c/assets/fonts/geist-mono-400-latin.woff2` | ja, 9 864 B |
| 13 | Public Sans 300, latin `.woff2` (display i heron + brödtext) | samma | `tests/alunix-r8/runs/V3c/assets/fonts/public-sans-300-latin.woff2` | ja, 14 564 B |

Typsnitten (11–13) är SIL OFL alla tre, latin-subsetet som Google själva serverar, summa
37 792 B mot `performance.md` § 1:s tak. De ersätter Google Fonts-länken i R3 (byggaren skriver
`@font-face` + `preload`, med `unicode-range` för latin och metrikmatchad fallback per familj).
Under hela R2 laddades de tre familjerna över nätet från Google Fonts, inte från fallback-
stacken, så R2:s mätningar togs mot rätt glyfer men fel laddningsväg.

**Inte ärvda, med skäl:**

- `k4-desk-overhead.webp` (136 kB): läst som pixlar. Färgfoto av ett kafébord med
  surfplatta, mugg och bakverk. Fel värld (V3c är gråskala), stockkomposition, och det
  finns ingen plats på sidan för den. Kopieras inte.
- `hero-console.webp` (21 kB): läst som pixlar. Portrattbeskuren version av samma stuga
  som grunden, med ett skrivbord och en hårdkantad ljustrapets på väggen. Skulle dubblera
  grundens eget motiv i plåten. Kopieras inte.
- `k1-stage-beams.webp` (17 kB): läst som pixlar. Diagonala ljusstrålar i dis. **Kopieras
  ändå med** som reserv för väg (a) nedan, se § 3. Om lead väljer en annan väg används den
  inte, och då tas den bort ur `assets/` innan R2.
- Motorns `template.html`: läses av byggaren på plats för stage-markupen, kopieras inte in
  i cellen.

## 2 · F-007-kontrollen av hero-plattans stillbild

Full dom med de tre mätbara skälen står i `tests/alunix-r8/concepts-V3c.md` § F-007. I
korthet: **ljuspölen bär inte flippen.** Cirka 60 % av bildytan ligger på eller nära ren
svart, alltså samma värde som kortets baksida, så vändningen går från svart rektangel till
svart rektangel; motivet saknar kant och rak struktur som kan förkortas i perspektiv, vilket
är det ögat läser en Y-rotation med; och logo-docken sitter på ett parti helt utan textur.

## 3 · Ingen omtagning. Vägarna som återstår, i planens § 10.6 steg 3-ordning

Higgsfield är ute: `balance` ger `{"credits":0,"subscription_plan_type":"free"}`, en enda
privat workspace på free plan, mätt av lead 2026-09-09. Steg 1 (Higgsfield) och steg 2
(Codex `image_gen`, som ändå inte ger något som steg 3 inte ger bättre här) faller.
**Ingen asset-lock för en omtagning skrivs.** Kvar är steg 3:s fyra vägar.

### (a) En annan ruta ur befintligt r5-material

Enda realistiska kandidaten är `k1-stage-beams.webp`: tre hårda diagonala ljusstrålar i
dis, läst som pixlar. Vinst: strålarna är raka linjer och förkortas läsbart i perspektiv,
vilket löser skäl 2. Förlust: den löser inte skäl 1 (ungefär 55 % av ytan är fortfarande ren
svart, samma värde som baksidan) och inte skäl 3 (logo-docken landar antingen på strålarna
eller på död svart). Den byter dessutom motiv från "ett kort på ett bord" till
"scenbelysning", vilket är ett annat rum än grundens.
**Kostnad: noll. Risk: låg. Vinst: en tredjedel av felet.**

### (b) Ny beskärning eller omgradering av den nuvarande bilden

Efterbehandling enligt `assets.md` regel 1 (korn, asymmetrisk beskärning, gradering)
räknas inte som generering. Konkret: källan är 1600x1067 och det belysta partiet ligger
ungefär x 180-1080, y 400-1000. En 16:9-beskärning på ~900x506 ur det partiet fyller hela
rutan med tyget, och en svartpunktslyft från 0 till 5-7 % luminans gör väven närvarande
över hela ytan medan toppen hålls kvar vid 78-82 % så plåten inte tar auktoriteten från
rubriken. Det löser skäl 1 och skäl 3 helt och skäl 2 inte alls. Filstorleken hamnar långt
under taket 250 kB, och 900x506 matchar precis plåtens renderade 896x504 vid 1440.
**Kostnad: en ffmpeg- eller PIL-körning. Risk: låg. Vinst: två tredjedelar av felet.**
Måltal om lead kör den: svartpunkt >= 5 % luminans över hela rutan, topp <= 82 %,
4:5-centerbeskärningen (mobil under 640 px) ska fortfarande innehålla ljuspölen.

### (c) Riktig fotografi via Step 5b:s kontaktarks-pipeline

Skulle kunna ge det enda som (a) och (b) inte kan: ett verkligt kort eller pappersark under
snedljus, med en rak kant och en kastskugga. Löser alla tre skälen. Kostnaden är en hel
pipeline-körning plus kontaktarksläsning, och risken är materiell: det närmaste sökbara
motivet ("business card on dark desk", "paper sheet raking light") är precis den
stockkomposition TASTE § 5 räknar som avvisad, och ett nytt hero-motiv i en cell vars hela
premiss är att estetiken är låst är ett nytt bygge, inte en iteration.
**Kostnad: hög. Risk: medel till hög. Vinst: hela felet, men med en ny risk.**

### (d) Ändra koreografin så att den bild som finns bär flippen

§ 10.6 steg 3 säger uttryckligen: byt **deviceform**, aldrig kvaliteten. Felet är en
relation mellan bild och device, inte bara en egenskap hos bilden: bilden har en tydlig,
enda riktad ljuskälla, och den nuvarande koreografin använder den inte alls. Två tillägg,
båda rena `opacity`-kompositioner utan `filter` och utan layout, båda drivna av samma
`--flip` som redan finns:

1. **Framsidan mörknar när planet vrider sig bort från ljuset.** Ett `::after` på
   `.face--front` i `var(--c-black)` vars `opacity` går 0 -> 0,65 över `--flip` 0 -> 0,5.
   Löser skäl 1: fram- och baksida får olika värdekurva, och mötet vid 90 grader blir en
   övergång i stället för ett klipp.
2. **En specular-hårlinje på den ledande kanten.** Ett 2 px brett element längs kortets
   ledande vertikala kant, `opacity` som toppar vid `--flip` = 0,5 och är 0 vid 0 och 1.
   Löser skäl 2: den ger rotationen exakt den raka linje som förkortas, utan att lägga till
   ett objekt i motivet.

Båda sitter **inuti** målbildens egen fysik ("som ett visitkort man vänder med handen; vid
90 grader syns bara hairlinen, det är ärligt") och lägger till noll nytt innehåll, noll nya
filer och noll begärda krediter.
**Kostnad: två CSS-regler. Risk: låg, mätbar i `motion_probe`. Vinst: skäl 1 och 2 helt,
skäl 3 kvar.**

### Rekommendation

**Väg (d).** Den är den enda som § 10.6 steg 3 namnger explicit, den kostar ingenting, den
kan inte importera ett nytt motiv eller en ny stockkomposition, och den träffar de två
skäl som faktiskt gör flippen oläsbar. Väg (b) är gratis och riskfri och bör köras
**efter** R2 om leads pixelläsning av folden fortfarande säger att framsidan läser som en
svart rektangel; den ändrar inget i koden och kan därför läggas till utan att röra en runda.
Väg (a) avråds: den byter motiv utan att lösa mer än (b) gör. Väg (c) avråds i r8 och
noteras som en punkt för en senare runda om Anton vill öppna hero-motivet.

Raden som skriver in bytet står i `runs/V3c/BRIEF.md` § decision ledger.

## 4 · Asset-lock per medieplats

Ingen av dessa är en generate-prompt. Alla fyra platser fylls av redan vendorat material.

```
Asset role:    Hero plate front, the card's photographic face
Slot:          16:9 at width min(100% - 2*rail, 56vh*16/9) = 896x504 at 1440; 4:5 under 640px;
               left-anchored at --rail-x, inside figure.hero-plate
Art direction: k1-stage-pool.webp as vendored. Low-key grayscale, one directional light
               source, no subject, no text, no people. The light pool travels by
               object-position on --sc-ps between p 0 and 0.12 and keeps travelling
               through the turn.
Avoid:         any second light source; any recolouring; any crop that pushes the pool
               out of the 4:5 centre crop; blowing the highlight past 82% luminance
```

```
Asset role:    Page ground, continuous grayscale world
Slot:          fixed, full viewport, behind every section, tinted by --sc-canvas drift
Art direction: k4-cabin-desk.webp as vendored, grayscale, unchanged from V3b
Avoid:         a second background photograph; any gradient replacing it; any transform
```

```
Asset role:    Hyperborea plate, bleeding past the blue block's right edge
Slot:          inside section.panel-thesis, left column, translateX(11%) past the padding
Art direction: demo-hyperborea.webp as vendored. Black and white where it meets the blue
               block (mattis-studio's own role rule)
Avoid:         colour photography against the accent block; a caption under the photo
               instead of beside it
```

```
Asset role:    Wordmark, logo dock on the card's front face
Slot:          top-left inside figure.hero-plate, straddling the plate's own hairline
Art direction: logo-white.svg inline, currentColor, no fill of its own
Avoid:         a second wordmark inside the plate; any glow, halo or hairline border
               around the mark
```

`demo-calyx.webp` och `demo-horai.webp` är **reserver**, inte medieplatser: Calyx och Hōrai
visas live i `<iframe>` från repo-roten. De två filerna kopieras in så att en trasig iframe
kan ersättas av en skärmbild utan en ny runda, och används inte annars.

## demo-calyx-1440-color.webp (vendorad av lead 2026-09-17, plan 046)

| Fält | Värde |
|---|---|
| Fil | `assets/demo-calyx-1440-color.webp`, 1076x606, 79 178 B |
| Källa | `board/cells/K4-r8/assets/demo-calyx-1440.webp` (1440x900, 206 966 B), omkodad av lead med Pillow LANCZOS, kvalitet 70 |
| Roll | Steg 05 till 07 i processakten: arket får sitt material, och färgen kommer i steg 06 när ritningen har blivit en sida (Antons beställning 2026-09-17, Q33) |
| Mätt | max chroma 138 (gråskaleversionen mäter 1); budget ≤ 90 kB håller med 10 822 B marginal |
| Varför två filer | `demo-calyx-1440.webp` kodades om till gråskala av lead före R6 (perf-fynd 6, 206 966 → 59 520 B). Den står kvar som ritningens material; färgversionen är den färdiga sidan. Byggaren avgör i plan 046 om båda behövs samtidigt eller om filtret räcker |
| Provenance | Skärmbild av `sites/calyx.html`, kedjans egen exempelsajt. `PRODUCT.md` § Evidence sanktionerar den |
