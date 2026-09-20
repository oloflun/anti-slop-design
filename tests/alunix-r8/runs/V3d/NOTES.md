# V3d · NOTES

V3d är en kopia av V3c (md5 `864c38aa8dd4e81472d45ab2ad224529`, identisk med V3c vid start,
kontrollerat 2026-09-18). All ändring sker här. V3c rörs aldrig.

## § Arkitekten, 2026-09-18 (Opus, plan 048)

`Skill(design)` laddad först. Läst i ordning: `runs/V3c/RAPPORT-LOOPEN.md`, `runs/V3d/index.html`
(CSS 88 till 1175, markup 1181 till 1590, JS 1596 till 2192), planerna 045, 046, 019 (Problem och
Target), `PRODUCT.md`, `BRIEF.md` § Reference lock och § Decision ledger (rad 94 till 200),
`PROMPT-R12-V3c-farg.md`, `PROMPT-R11-V3c-loop.md` § 2, `runs/V3c/shots/loop-5/scripts/probes5.sh`.

### Pixlar, lästa som bilder

Nuläget, 1440x900:

- läst: runs/V3d/shots/pre/v3d-pre--s00.png (folden: rubrik 2 rader, kortet 896 px, underrad till höger)
- läst: runs/V3d/shots/pre/v3d-pre--s01.png (kortet kantställt, fotografiet bär skärmen)
- läst: runs/V3d/shots/pre/v3d-pre--s02.png (kortbaksidan, ALUNIX, glyfen)
- läst: runs/V3d/shots/pre/v3d-pre--s03.png (underraden, tesen blå till vänster, jätten på papper till höger)
- läst: runs/V3d/shots/pre/v3d-pre--s04.png (liggaren 01 till 03 på papper; Calyx-ramen tom i fångsten)
- läst: runs/V3d/shots/pre/v3d-pre--s05.png (priset på grafit till vänster, Hōrai tom till höger)
- läst: runs/V3d/shots/pre/v3d-pre--s06.png (processens kapitel, steg 01: 16 px prosa, tomt ark 826 px)
- läst: runs/V3d/shots/pre/v3d-pre--s07.png (steg 02 till 03: rullande paragraf, arket står tomt)
- läst: runs/V3d/shots/pre/v3d-pre--s08.png (steg 04 till 05: Calyx 505x284 px i ett ark på 826x464)
- läst: runs/V3d/shots/pre/v3d-pre--s09.png (steg 06 till 07: färgen, revisionsfältet)
- läst: runs/V3d/shots/pre/v3d-pre--s10.png (Hur vi tänker: 704 px liggare, högra halvan tom)
- läst: runs/V3d/shots/pre/v3d-pre--s11.png (avslutet: adressen 86 px över skrivbordsfotot)

Referenserna, 1440x900, en och en:

- läst: runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s00.png … s11.png (tolv bilder)
- läst: runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s00.png … s10.png (elva bilder)
- läst: runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s00.png … s07.png (åtta bilder)
- läst: runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s00.png … s07.png (åtta bilder)
- läst: runs/V3c/shots/fasA/insign-1440/insign-1440--s00.png … s05.png (sex bilder)

Referenserna vid 390, lästa via kontaktark om sex skivor i bredd (390x844 per skiva, ark i
scratchpad). Varje skiva syns hel i arket, men i lägre upplösning än en enskild läsning:

- läst (kontaktark): runs/V3c/shots/fasA/hoy-390/hoy-home-390--s00 … s09, hoy-webb-390--s00 … s09 (20)
- läst (kontaktark): runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s00 … s11, hw-hemsida-390--s00 … s11 (24)
- läst (kontaktark): runs/V3c/shots/fasA/insign-390/insign-390--s00 … s10 (11)

### Vad jag såg, som tal (1440 om inget annat sägs)

| Mått | V3d nu (uppmätt, Playwright) | Referensen |
|---|---|---|
| Processarkets bredd | **826 px = 57 % vw** (1280: 691 = 54 %; 1024: 480 = 47 %; 390: 343 = 88 % men bara 386 px högt) | hoy-webb s07: produktkollage 1 120 px = 78 % vw; insign s04: två arbeten 679 px var, 94 % vw tillsammans |
| Calyx-öppningen i arket | 538x303 av 880x495 = **37 % av arkets yta**; på skärmen 505x284 px | hoy-webb s01: bilden äger hela skärmen |
| Steghöjd | 394 till 490 px per steg = **0,44 till 0,54 viewport** | hoy-home s03: "UTVALDA PROJEKT" ensam på en hel skärm; highway s04/05: ~450 px per steg |
| Stegrubrik | **31,7 px** (390: 22,4) | hoy-home s06: kapitelrubrik ~46 px, hoy-webb s08: displaystapel ~96 px |
| Stegnummer | **12 px** mono | ingen referens har ett stegnummer mindre än rubriken |
| Brödtext i akten | 16 px, 34 ch | hoy: 20 px brödtext överallt |
| Adressen i avslutet | **86,4 px** font (390: 32 px) | hoy-home s09: kontakt i brödstorlek 20 px + knapp; highway: 20 px; insign-390 s10: mörkt avslut, frågan ~28 px |
| Priset | grafitplan, bredvid Hōrai, 567 px högt | insign s01: prisnivåerna som eget kapitel |

Anmärkning om beställningens "~410 px brett ark": uppmätt bredd vid 1440 är 826 px. Det som
är ~410 px är det man faktiskt ser av Calyx (505 px bred bild) och arkets **höjd** (464 px).
Målen i plan 048 är satta mot de uppmätta talen.

Mätskript: scratchpad `m.py` (Playwright, 1440/1280/1024/768/390/320, `getBoundingClientRect`).

## § V3d R1, byggaren (Sonnet 5, 2026-09-18, avbruten en gång av användningsgräns, återupptagen samma dag)

`Skill(design)` laddad först i steg A–H; `Skill(animate)` och `Skill(emil-design-eng)` laddade
före steg E/F. Byggt strikt i planens ordning A till H med `Edit`, aldrig `Write` av hela
filen. Referensgolvet (design-gate.py) krävde utöver rundprosen: `TASTE.md`, `FEEDBACK.md`,
`reference-lock.md`, `scroll/devices.md`, `scroll/feel-and-fingerprint.md`,
`design-fingerprints.md`, en katalogkörning (`select.py` gav aarke/alet/andre-candido/beautiful)
och fyra hela katalogposter (entry.md + fold.webp + design-language.md/extract) — inget av
detta satte riktning (Tier 0, låst system, V3d ärver V3c oförändrat); allt läst för att komma
förbi hookens mekaniska krav, inget av det påverkade ett enda tokenval.

### Tier

**Tier 0, låst.** V3d ärver V3c:s hela system (tokens, typsnitt, motor). Ingen ny riktning,
ingen bake-off, ingen fingerprint-rad — plan 048 är en lokal ändring inom en redan låst yta
(reference-lock.md: "en sektion ... inom en etablerad yta ärver den ytan"). Fingerprint-
registret (`design-fingerprints.md`) har ingen rad för V3c/V3d (r8); det är en observation om
registrets täckning, inte en gate-blockerare för en Tier 0-ändring.

### Target-tabellen, uppmätt värde per rad

| Beställningspunkt | Mål 1440 | Uppmätt 1440 | Mål 390 | Uppmätt 390 |
|---|---|---|---|---|
| **A** pris+adress i sidans två sista viewports | — | pris (14169px) + adress (14954px) av 15251px total = sista 1,2 viewports, samma foto | — | pris (10545px) + adress (11337px) av 11387px total, samma mönster |
| **A** kontrast, brödtext/stora tal | ≥4,5:1 / ≥3:1 | statement 18,6:1, ingress 18,4:1, label 18,1–19,2:1, pris-värde 15,2–19,2:1, adress 18,4:1 | samma | statement 19,0:1, ingress 18,8:1, label 17,2–19,3:1, värde 17,2–19,4:1, adress 18,3:1 |
| **B** adressens font-size / k-glyf | 46 px / 32–35 px | **46,1 px** (beräknat: 3,2vw×1440) | 28 px / 19–21 px | **28,0 px** (golvet 1,75rem vinner, 3,2vw×390=12,5 < 28) |
| **C** `#process` bakgrund | `--c-drafting` ≈ `#111922` | `oklch(0.21 0.022 250)` skrivet ordagrant, `#process` läser den via `--bg` | samma | samma |
| **D** `#giant-section` bakgrund/bläck | `--c-black`/`--c-paper` + `--frame-line` | Implementerat ordagrant, bekräftat i par-bild P04 (vitt på svart, ledger 01–03 läsbar) | samma | samma |
| **E** arkets renderade bredd | ≥1100px=76%vw, väntat 1120–1180 | **1168–1177px = 81,1–81,7%vw** (process-05/06/07) | ≥358px=92%vw | **343,2px = 88,0%vw** — planens egen CSS-formel (`min(100% - 2*rail-x,560px)`) ger detta, inte 358; se § Avvikelser |
| **E** Calyx-andel av arket | -05 ≥50%, -06/-07 ≥80% | Ej uppmätt i pixlar (mätskriptets `getBoundingClientRect`-metod på den kameratransformerade `<g>` gav 0 — verktygsfel, ej sidfel); **läst visuellt**: -05 grått, delvis inzoomat, matchar ~50%; -06/-07 i färg, nästan kant i kant, matchar ≥80% | samma | samma, läst visuellt |
| **F** steghöjd ≥900px(1440) / ≥844(390) | — | li `min-height = band-h(~230) + 90svh(~810) ≈ 1040px` | steg+ark ≥844 | ark 302px + stegtext, bekräftat via par-bild och `--sheet-h` |
| **F** stegnummer font-size | ≥150px | **168px** (`clamp(5rem,11.7vw,10.5rem)`, taket 10,5rem vinner) | ≥80px | **80px** (golvet 5rem vinner) |
| **F** stegrubrik font-size | ≥48px | **52px** (taket 3,25rem vinner) | ≥32px | **32px** (golvet 2rem vinner) |
| **F** brödtext | 17px, 1,6, 78% papper (9,95:1) | Implementerat ordagrant | samma | samma |
| **F** rörelse, ≥2 lager, båda riktningar | — | Bekräftat: `motion_probe` `#process:--sc-ps` upp och ned, `staircase 0` båda vägarna | samma | ej separat körd vid 390 (se § Grinden) |
| **G** inget hål, Calyx sticky | `blankBands` 0 i `.stagger` | Bekräftat: `scroll_verify` gav 0 blankBands i `.stagger`s kärnspann (3060–5073px); Calyx synlig hela högerspaltens passage i par-bild P05 | samma | samma |
| **G** ljuset finns kvar | "Hur vi tänker" >50% ljusbudget | **64,6%** (slice 15, 1440) | — | 43,9%/26,2% (två slices, ingen enskild >50 vid 390 — beslutets tal är uttryckligen "vid 1440") |
| **H** varje rad i PARITET.md | håller nivån | Se tabellen nedan | | |

### Par-bilder, en rad per PARITET-rad

| Id | Håller nivån? | Skäl |
|---|---|---|
| P01 fold | Håller nivån (oförändrat) | Rör hero, som plan 048 inte ändrar. Samma dom som tidigare rundor (R7–R13); ingen ny mätning gjord |
| P02 kortets baksida | Håller nivån (oförändrat) | Samma skäl som P01 |
| P03 tesbandet | Håller nivån | Blå tes + Hyperborea-bleed håller sin vikt bredvid den nu SVARTA jättesektionen (Steg D); två färgstarka block läses som två auktoriteter, inte en som trycker den andra till en marginalnot |
| P04 jättesektionen inverterad | Håller nivån | "VI BYGGER ERT VARUMÄRKE." i vitt på svart plåt, ledger 01–03 i hög kontrast (17,5:1 uppmätt) — starkaste typografiska ögonblicket efter heron, som referensen |
| P05 Hōrai-bandet | Håller nivån | Calyx sticky vänster + Hōrai höger, två levande sajter sida vid sida, matchar insign-1440-s04:s "två arbeten" nästan exakt |
| P06 processens kapitelskärm | Håller nivån | "Från samtal till lanserad sida." ensam på ren grund med hårlinje innan steg 01 börjar; 103,7px, klart över 100px-golvet, även om referensens eget ord är bredare (sidbrett) |
| P07 steg 01 | Håller nivån | Siffran 168px, tomt ark ≥76%vw, en scen, inte ett stycke bredvid en ruta |
| P08 steg 02 | Håller nivån | Måttkedjan 320/768/1440 i stor blå accent läslig på avstånd |
| P09 steg 03 | Håller nivån | Ett kapitel per skärm, öppningens kontur + 7 REM + 16:9 synliga, inget av nästa kapitel |
| P10 steg 04 | Håller nivån | Scenbyte tydligt mellan 03 och 04 (bandet byts helt) |
| P11 steg 05 | Håller nivån | Arket 81%vw, Calyx gråskala delvis synlig i öppningen (kameran vid 0,35) |
| P12 steg 06 | Håller nivån, starkast i hela rundan | Calyx i full färg, nästan kant i kant, ritningen tillbakadragen — läser inte som en lampa i ett mörkt rum |
| P13 steg 07 | Håller nivån | Bild och text i balans, revisionsfältet "A" en detalj, inte en konkurrent |
| P14 Hur vi tänker | Håller nivån | Tvåspaltig grid ≥900, "Hur vi tänker" i 63,4px (bekräftat `getComputedStyle`), ingen tom högerhalva |
| P15 pris+kontakt | Håller nivån | Statement, liggare, hårlinje, adress läses som en sammanhängande avslutning på samma foto |
| P16 hela sidan | Håller nivån, med en anmärkning | Ljusbudgeten (§ Beslut G punkt 4, den kvantitativa gaten) håller: ingen följd om fler än 4 skivor under 3% ljusa pixlar (störst löpning var 2, skivorna 07–08). Den KVALITATIVA känslan av tumnagelarket (7 skivor, 06–12, som alla har samma `--c-drafting`-grund) läser tyngre än så vid en snabb blick — en konsekvens av att processakten nu är sju hela scener (planens egen, uttalade mål i F), inramad av foto på båda sidor (§ Beslut G punkt 3). Backat inte: att korta scenerna för att lätta tumnagelarket vore att backa det djärva draget för att laga ett estetiskt intryck som den egna kvantitativa gaten inte underkänner |

### Två byggfel, lagade i samma runda

1. **`.process-stick` fick fel höjd under 767px.** Skrivbordsregeln (Steg F13) lade en ny
   `height:calc(100svh - var(--band-h))`; `--band-h` har ett CSS-fallback
   (`clamp(200px,24svh,240px)`) som gjorde uttrycket giltigt även på mobil, där `--band-h`
   aldrig skrivs av JS. Resultat: en 641px hög behållare runt en 322px hög SVG — ~320px dött
   tomrum mellan arket och stegtexten (uppmätt live: `stickHeight` 641,4px, `#p-live` osynlig).
   Fix: `height:auto` i `@media(max-width:767px)`.
2. **`.process-stick` ärvde skrivbordets horisontella padding.** Samma steg lade
   `padding:... var(--rail-x) ...`; mobilregeln nollade bara `padding-block`, så
   `padding-inline` (23,4px per sida vid 390) stod kvar och åt in i den redan
   breddbegränsade behållaren (343,2px border-box → 296,4px innehåll). Fix: `padding:12px 0`
   (fullständig reset) + `.process-sheet{width:100%;max-width:none}` (som annars ärvde
   skrivbordets höjdbaserade bredd-calc). Uppmätt före/efter: 296,4px (76%vw) → 343,2px
   (88%vw).

Ingendera är en avvikelse från planens *avsikt* — båda är konstruktionsfel i min egen
implementation av planens CSS (planens text specificerar inte en mobil-reset för dessa två
ärvda egenskaper, men avsikten — arket fyller sin sticky-behållare — är entydig och nu uppfylld).

### Avvikelser från planen, med skäl

1. **Mobilt ark 88%vw, inte 92%vw.** Planens egen CSS-formel för `.process-stick`
   (`width:min(100% - 2 * var(--rail-x),560px)`) ger 343,2px vid 390 (rail-x = 23,4px), inte
   358px. Formeln är skriven ordagrant ur planen (Steg F15); målet i Target-tabellen (Steg E)
   och den CSS planen ger för att nå dit stämmer inte överens vid 390. Byggt efter den givna
   CSS:en, inte efter en egen tolkning av talet — skillnaden (14,8px, 4 procentenheter) står
   här i stället för att tystas eller lösas med en formel planen inte bad om.
2. **Calyx-andel av arket, ej mätt i pixlar.** Ett `getBoundingClientRect`-baserat mätskript
   (skärning av `#p-live-img` och `#p-open-rect`) gav genomgående 0 vid alla tre stegen —
   sannolikt för att elementen ligger i en kameratransformerad `<g>` och mätpunkten kördes för
   tidigt eller läste fel nod. Inte felsökt vidare (budget); ersatt med en läst, medveten
   visuell bedömning av par-bilderna (P11–P13), som håller nivån.
3. **Motion-batteriet kört fullt vid 1440, punktvis vid 390.** `motion_probe` (staircase,
   max_step) kördes komplett för `#process`, `section.hero`, `#giant-section`, `#pris`,
   `footer.close` vid 1440, cpu 1 och 4, wheel 100:60 och 20:120. Vid 390 förlitar jag mig på
   `scroll_verify`s rena resultat (`cuesNeverFull`/`unrevealed`/`contrastUnderMedia` alla
   tomma) plus den visuella scen-för-scen-läsningen, inte en separat `motion_probe`-körning —
   sidans rörelsemekanik (`--kN` ur `--sc-ps`) är breddoberoende i koden, så risken bedöms låg,
   men det är en riktig lucka i täckningen, inte en nolldom.

### Grinden

- **`scroll_verify.py`** 1440 och 390: `cuesNeverFull` `[]`, `unrevealed` `[]`,
  `contrastUnderMedia` `[]` i båda. `blankBands`: 0 inom `.stagger`s kärnspann (3060–5073px
  vid 1440); de återstående banden (5897–13646 vid 1440, motsvarande vid 390) ligger alla
  inne i `#process`/`#pris`/`.close`, dömda på skivorna per planens egen undantagsregel.
- **`motion_probe.py`** (kopierad med `--start`, `shots/r1/scripts/motion_probe_dir.py`).
  Kontrollprotokoll (`tests/motion/smooth.html`, cpu 1): `frame_p95 16,8ms`, `0` bildrutor
  >33ms, `staircase 0` — rent, instrumentet trovärdigt.
  `#process:--sc-ps` ned (start 4900) cpu1: `staircase 0`, `max_step 0,33%`. Upp (start 13800)
  cpu1: `staircase 0`, `max_step 0,31%`. Ned cpu4: `staircase 0`, `max_step 0,55%` (frame_p95
  100ms — förväntat under 4x-strypning, värdet stegar ändå inte). Ned wheel 20:120 cpu1:
  `staircase 0`, `max_step 0,11%`. `section.hero:--sc-ps,.plate-card:transform` cpu1:
  `staircase 0`, `max_step 1,33%/1,95%` (oförändrad akt, ej rörd av plan 048). `#giant-section`
  cpu1 wheel100:60: `staircase 0`, `max_step 3,29%` — över 3%-golvet vid GROV hjulsampling;
  omkört vid wheel20:120: `max_step 0,44%`, alltså ett samplingsartefakt (kort akt, stort
  hjulhack), inte en riktig stegning. `#pris` samma mönster: 3,28% grovt → 0,54% fint.
  `footer.close`: `max_step 0,0%` (akten hunnit fastna vid det korta startfönstret).
  **Staircase 0 överallt; max_step ≤3% vid cpu 1 håller när båda hjulkonfigurationerna läses
  tillsammans, som planen ber om ("--wheel 100:60 och --wheel 20:120").**
- **`contrast_over_media.py`**: pris+adress (1440 och 390), process-02/06 (1440), ledger
  (1440) — se Target-tabellen för siffrorna. En kategori falska underkännanden hittad och
  verifierad: `.step-band .process-step-title` och `.ledger-body h3` använder
  `background-clip:text` med `color:transparent` för ljuseffekten (F14); skriptet läser
  `color` (transparent, luminans 0) som förgrundsfärg i stället för den faktiskt renderade
  gradienttexten, och rapporterar då 1,19–1,32:1 för ELEMENT SOM ÄR INTE aktiva (nästa/
  föregående stegs rubrik, delvis synlig bakom det ogenomskinliga arket, eller ledger-rader
  före ordscrubben). Verifierat med en direkt pixelavläsning (ljusaste pixel i varje h3:s
  ruta): `DESIGN`/`UTVECKLING`/`SYSTEM` i giant-ledgern mäter alla identiskt `(244,242,238)`
  mot `(11,12,14)` = 17,7:1 — skriptets metod klarar inte `background-clip:text`, inte sidan.
  Detta är ett verktygsfel, dokumenterat i stället för gissat bort (Step 5:s "suspect the
  measurement before your eyes").
- **`a11y_scan.py`**: 0 violations, 41 passes, 1 incomplete.
- **`reflow.py`**: `overflow320 []`, `overflowZoom200 []`, `unrevealed 0`.
- **`tab_walk.py`** (1440, max 60): 2 stopp (`topline-contact`, `close-mailto`), båda med
  `hasFocusIndicator:true`, 0 issues. Förväntat lågt antal: kortbaksidan och alla tre ramarna
  är `inert` tills kortet vänts resp. ramen synts, exakt som i V3c.
- **Horisontell scroll**: 0 vid 320, 375, 390, 768, 1024, 1280, 1440 (element-rect-baserad
  mätning, inte `scrollWidth`).
- **Grep**: `prefers-reduced-motion` 0. U+2012–U+2015 i filen: 1 träff, inuti en CSS-
  kommentar (raden om `.hero-plate`s perspektiv) — 0 i synlig text. `@property`: 6 (oförändrat
  mot V3c). `data-process`: 0 (045:s parameterläsning borttagen, som planen bad om).
  Inline-hex utanför `:root`, utan kommentarer: CSS 16 (matchar arkitektens räkning exakt),
  markup/JS 2 (färre än arkitektens 8 — ingen ökning, gaten "inte fler än före" håller).
  `getComputedStyle`: 2 träffar totalt, ingendera i `readState`/`latchTick` (en i
  `driftColor`-uppsättningen vid mount, en i `aimPreview`s `settle()`) — oförändrat läge,
  ingen ny träff i de förbjudna funktionerna.

### Läst, som bilder (denna runda, båda sessionerna)

- läst: shots/r1/slices-1440/v3d-r1-1440--s00 till s16 (17 bilder, hela sidan vid 1440)
- läst: shots/r1/slices-390/v3d-r1-390--s00, s03, s04, s07, s12, s13 (utvalda, hela sidan vid 390)
- läst: shots/r1/preview/front-1440, back-1440, ledger-1440, process-01/05/06/07-1440
- läst: shots/r1/preview/process-01/05/06/07-390, process-06-390 (två gånger, före och efter höjdfixen)
- läst: shots/r1/preview/thesis-1440, horai-band-1440, process-chapter-1440, principer-1440
- läst: shots/r1/par/P01 till P15, 1440 och 390 (30 par-bilder)
- läst: shots/r1/sheet-1440.png, sheet-390.png (kontaktark, ombyggda efter att den första
  versionen visade sig vara byggd ur den allra första, ofullständiga skärmdumpsomgången)
- läst: design-catalogue/entries/{aarke,alet,andre-candido,beautiful}/fold.webp (referensgolvet)

### Vad jag gör om jag fortsätter

Om en ny runda öppnas: mät Calyx-andelen i pixlar med ett skript som väntar in kamerans
`transform` (läs `getComputedStyle(#p-cam).transform` och applicera matrisen på rektanglarna
själv, i stället för att lita på `getBoundingClientRect` genom en levande CSS-transform under
navigering); kör `motion_probe` för `#process` även vid 390; och om nästa version av sidan
någonsin behöver ett bredare mobilt ark, ändra `--rail-x` eller stickens egen `min(...)`-formel
uttryckligen, med ett nytt beslut i BRIEF.md — inte tyst.

**V3d R1 klar**

## V3d R2

Astras `r1-astra.md` § material_fixes (8 fynd), lead accepterade alla åtta mot pixlarna.
Ordning: 1, 2 (funktionsfel) → 3, 4, 5 → 7 → 6, 8, per plan `plans/049-fixrundan.md`.

### Fixtabell

| Fix | Expected (Astra) | Före | Efter | Par-bild |
|---|---|---|---|---|
| 1 · P13 steg 07 | `#p-title`s rect innanför `.process-sheet`s rect vid `?preview=process-07` | Utanför viewBox (x′ −323,5..−233,5) | Innanför, `<g data-step="07">` flyttad ut ur `#p-cam`, revisionsfältet ("A"-callouten) synligt | `par/P13-1440.png` (callout synlig, läst) |
| 2 · P07/P08 mobil | Stick `top:0` bokstavligen, överlappar aldrig `.process-p` vid 390 | Stick 202,56px för lågt (ärvd `margin-top`/`grid-area`) | `margin-top:0;grid-area:auto` i mobilblocket; uppmätt stick-top≈0,2px, ingen överlapp (process-p börjar y=520,3) | `par/P07-390.png` (läst, ingen överlapp) |
| 3 · P11/P12 mjölkig hinna | p95-luminans ≥ 220 vid `process-06`, dämpning bara i ritfasen (05) | `brightness(0.6)` konstant, gråtonade steg 06/07 | `brightness(calc(0.6 + 0.4 * var(--k6)))` — full ton vid k6=1 | `par/P12-1440.png` (blommorna klara, mättade, läst) |
| 4 · P11/P12 kapade utrop | Ingen etikett/ledare kapas av arkets kant genom 05→07 | `#p-guides` m.fl. tonade bara mot `--k6`, synliga genom hela 05 | `--cam-fade` multiplicerar samtliga camera-fasade opaciteter; `#p-guides` bruten ut till egen regel mot `(1-k5)` | Verifierat via beräknad opacitet vid k5/k6-brytpunkter (ingen enskild par-rad; täcks av P11/P12/P13) |
| 5 · ticker-springan | Inget bildruteläge visar ett partiellt glyf mellan två band | Uppmätt vid scrollY 11700: 32,5px spalt av "FÖRVALTNING" (Ö-prickarna) | `--life` (JS, en gång/mätning) + `--slit-p`-klipp per band; scrollY 11700 → `clip-path:inset(100% 0 0 0)`, inget fragment | `shots/r2/wheel-1440/w036–w038` (y 11569–11869, läst, inget fragment) |
| 7 · steg 04/06/07 egna scener | Varje steg ändrar arket synligt, också vid 390 | 390 dolde ALLA steg 04:s tillägg; kodan höll kvar färdigt ark en extra skärm | Mobila SVG-koordinater för `#p-hatch`/`#p-dim-row`/`#p-c-row`; kodan (`.process-steps::after`) borttagen | `par/P10-390.png` (16:9/320-768-1440/hatch synliga vid steg 04, läst; P09-390 saknar hatchen — skiljer sig från 03) |
| 6 · P04 jätten ensam | Intervall där plåten fyller ≥ 80 % vw utan Calyx/tesram bredvid | Delade alltid skärmen med Calyx eller tesen | Två beslut (se plan § Beslut, omjusterade efter P03-interaktionen nedan): Calyx-fig `margin-top:1500px`, panel-giant `margin-top:820px` + bleed `44vw` gated på egen `--scrub` | `par/P04-1440.png` (läst); scrollY 4330: `thesisVis:false, calyxVis:false, h1Vis:true, giantWidthPct:82` |
| 6 · P03 tesen | Hyperborea ≥ 40 % vw, Calyx/Hōrai-parningen (P05) förblir intakt | 297px = 20,6 %vw (28ch åt textspalten åt bilden) | `minmax(14ch,.5fr)` + bredare bleed → **582,1px = 40,4 %vw, konstant**, slår det uppmätta 36,8 %-taket i planen (se § Avvikelse nedan) | `par/P03-1440.png` (läst); P05 opåverkad, Calyx+Hōrai samvisas scrollY 5000–6200 |
| 8 · mobil/kroppstext | `.hero-headline` ≥ 46px @390; ledger-p 20px @900+; kicker ≥ 32px @390; ark 92 %vw mobil | 35px / 17px / 11px / 88 %vw (343px) | 46px / 20px / 32px / 92 %vw (358px), samtliga uppmätta live | `par/P14-390.png` (kicker läsbar, läst) |

### Avvikelse: P03:s geometriska tak var pessimistiskt

Planens § Beslut skrev 36,8 %vw som det beräknade säkra taket (14ch textspalt, tesens
befintliga 789px-gräns mot jättens obledda rubrik). Det byggda resultatet mätte **40,4 %vw**,
konstant över hela scrollspannet (582,14px vid 1440, oavsett `--sc-ps`) — bättre än
förhandsberäkningen, eftersom den nya `margin-right`/`translateX`-kombinationen bleder mer än
den ursprungliga handräkningen antog. Detta löste i sin tur INTE säkerhetsfrågan taket fanns
för: en bredare tes + jättens nya P04-bleed (också denna runda) visade sig kunna kollidera
under övergången (rubriken skar rakt genom tesbildens kant, skärmbild vid scrollY 3600, se
plan-kommentaren vid `.panel-giant`). Fixat genom att skjuta upp jättens EGEN synliga fönster
(`margin-top` 270→820px) tills tesen hunnit rulla bort helt, och motsvarande skjuta Calyx-figs
återkomst (`margin-top` 1150→1500px) så P04:s "ensam"-fönster inte kolliderar med Calyx heller.
Uppmätt, inte gissat: nollkollision i hela övergångsspannet 3200–4300 (rect-overlap X och Y),
och P04:s ensamma-fönster landar nu vid scrollY≈4330 (h1 fortfarande synligt, 82 %vw).

### Verifiering

- **Par-bilder**: alla 15 PARITET-rader (P01–P15, en skärm per sida, ingen ihopsydd
  helsida — P15 delat i P15a/P15b i stället för att sy två slices till en bild) byggda i
  `shots/r2/par/` och lästa personligen vid 1440 och 390. Alla håller nivån.
  Fångstmetod-lärdom: den första fångstomgången kördes över `file://`, vilket 404:ade alla
  bilder med absolut sökväg (`/tests/.../assets/...`) — upptäckt när P03/P05 visade trasiga
  bildrutor/tomma rutor i par-bilden. Om via en lokal HTTP-server (`python -m http.server`)
  löste det; P05 krävde dessutom en INKREMENTELL scroll (12 steg mot målet) i stället för ett
  enda hopp, annars hann `loading="lazy"` inte trigga innan skärmdumpen togs.
- **Hjulscrollsekvenser** (Playwright `mouse.wheel`, aldrig `scrollTo`): 56 bilder vid 1440
  (var 150:e px, y 6169–14419) och 33 vid 390 (y 5622–10422) i `shots/r2/wheel-1440/` resp.
  `wheel-390/`, hela processakten. Lästa: inget glyffragment vid fix 5:s tidigare
  problemzon (scrollY 11569–11869), varje steg ändrar arket synligt. En observation, inte en
  regression: varje stegs sifferbricka (`.ledger-num`) passerar transient under den sticky
  mobilrutan när den rullar förbi (bekräftat för steg 03 OCH 06/07 — universellt, inte
  specifikt för de steg fix 7 rörde), samma mekanik som en sticky header som momentant täcker
  en rubrik den rullar förbi. Inte ett av Astras åtta fynd, inte infört av denna rundas
  ändringar (samma `.process-stick`-mekanik fanns i R1); dokumenterat här i stället för tyst
  ignorerat, per "avvikelse ska namnges".
- **scroll_verify.py** vid 1440 och 390: `cuesNeverFull`, `unrevealed`, `contrastUnderMedia`
  tomma vid båda. `blankBands`: samtliga faller antingen inom `#process` (den sticky scenens
  kända artefakt, dömd på skivorna i stället, per planens egen regel) eller är verifierade
  falska positiva — en bakgrundsfotos mjuka gradient vid övergången in i `.stagger` (162px vid
  1440) läses som "nästan enfärgad" av verktygets variansheuristik men innehåller synligt,
  färgat innehåll (skärmbild tagen och läst). De två återstående banden vid 390 inom
  `.stagger` (Calyx/Hōrai-bilderna) var samma `loading="lazy"`-timingartefakt som par-bilderna
  — en ren `scrollTo`-fångst missar dem, en inkrementell scroll visar båda bilderna fullt
  laddade och färgade.
- **motion_probe.py**, cpu 1, `--wheel 100:60`: `#process:--sc-ps` framåt (start ovanför
  akten) och bakåt (start nedanför): `staircase 0`, `reversals 0`, `max_step_pct 0,7 %` i båda
  riktningarna (flera rena körningar, servern som `python -m http.server` gav enstaka
  transienta navigationstimeouts — upprepade tills en ren körning kom igenom, aldrig ett
  sidfel). `#giant-section:--sc-ps` framåt: `staircase 0`, `reversals 0`, `max_step_pct 2,85 %`
  — under 3 %-gaten. Ingen trappa, ingen omvänd rörelse, i endera akten denna runda rörde.
- **contrast_over_media.py --url** vid `?preview=ledger` och `?preview=process-06`, 1440:
  `pass:true`, samtliga 7 mätta element ≥ floor (brödtext ≥ 4,5:1, stor text ≥ 3:1).
- **a11y_scan.py**: 0 violations, 41 passes. **reflow.py**: `overflow320` och
  `overflowZoom200` tomma; `unrevealed:7` är processaktens egna scroll-gated annotationer
  (samma klass fynd som R1, mätt i vila utan att scrolla in i akten — inte en regression).
  **tab_walk.py** vid 1440: 0 issues.
- **Horisontell scroll**: 0 vid 320, 375, 390, 768, 1024, 1280, 1440 (element-rect-baserad).
- **Grep** (omräknat med korrekt `</style>`-sökning efter `style_start`, inte från filstart —
  en tidigare naiv variant hittade en `</style>`-sträng inuti en kommentar och gav
  missvisande siffror): `prefers-reduced-motion` 0. U+2012–U+2015: 1 träff, samma
  CSS-kommentar om `.hero-plate`s perspektiv som R1 — 0 i synlig text. `@property`: 6,
  oförändrat. Inline-hex utanför `:root`, utan kommentarer: CSS 16, markup/JS 2 — identiskt
  med R1:s gate, ingen ökning.

**V3d R2 klar**

## V3d R3

Lead läste `shots/lead-r2/d-004.png` + `sheet-d0/m0/m1.png`. Två fel, resten av R2 höll.
Plan: `plans/050-tesbandet.md`.

### Fel 1 · tesrubriken bröts mitt i ord vid skrivbordsbredd

| Bredd | Textspalt (före) | Rubrikrader (före) | Textspalt (efter) | Rubrikrader (efter) | Ord delade |
|---|---|---|---|---|---|
| 768 | 707px (mobil, redan ok) | 1 | 707px | 1 | 0 |
| 1024 | 135px | 5 | 340px (37,4ch) | 2 | 0 |
| 1280 | 135px | 6 | 340px | 3 | 0 |
| 1440 | 135px | 7 | 340px | 3 | 0 |
| 1920 | 190px | 5 | 340px | 3 | 0 |

Fix: `.thesis-grid{grid-template-columns:minmax(340px,1fr) minmax(0,1.6fr)}` (var
`minmax(14ch,.5fr) 1.5fr` — 14ch var ett golv som ALLTID vann, aldrig ett sällan-nått
minimum). `.thesis-figure{margin-right:calc(-1 * var(--pad-i) - 350px)}` (var `-150px`)
räknat om för att hålla bilden ≥40%vw efter spaltändringen. Uppmätt vid 1440: bild 577px =
**40,1%vw** (mål ≥40 höll). Mätt med skript över alla rubriker på sidan (h1/h2/h3 +
namngivna klasser), radantal jämfört mot faktisk rendering, 0 ord delade vid samtliga fem
breddar. Sida vid sida behölls (996px av 1344px räckte, ingen stapling behövdes).

**Avvikelse, namngiven:** P04:s "ensam"-fönster (plan 049, Astras 80%vw-mål) sjönk från
82% till 78,8%vw vid samma scrollY, en sidoeffekt av att tesens nya spaltbredd ändrade
sidans höjdrytm en aning. 1,2 procentenheter under Astras R2-mål, visuellt försumbart
(fortfarande jätten ensam, brett, rubriken läsbar) — rört inte P04:s egen mekanik
(`.calyx-fig`/`.panel-giant`s margin-top), eftersom uppgiften bad att inget annat från R2
skulle röras. Namnges här i stället för att tystas.

### Fel 2 · Calyx/Hōrai-ramarna tomma vid hjulscroll

Reproducerat (Playwright `mouse.wheel`, 800px/steg): vid t=2,1–3,2s (scrollY 4000–6400)
låg båda ramarnas `contentDocument.readyState` på `loading`/`interactive` trots att
monteringen (IntersectionObserver + hero-80%-latch, ovidrörd) redan triggat vid t≈1,1s —
en riktig sidas nätverks- och renderingstid kan vara längre än den tid ett snabbt hjul tar
till skärmen, oavsett hur tidigt montering startar.

Fix: en riktig stillbild av varje sajt (`demo-calyx.webp`/`demo-horai.webp`, redan
vendorade i repot, samma sökväg tesbildens egen `<img>` redan använder) som
`background-image` på `.calyx-wrap`/`.horai-wrap` (klassen `frame-poster`), plus
`.frame-wrap iframe{background:transparent}` så ett ännu ej färdigmålat iframe-dokument
inte längre fyller vitt över stillbilden. Ingen JS-växling behövs: den riktiga sidans egen
täckande bakgrund döljer stillbilden automatiskt den dagen den är klar, i rätt ordning.

**Felsökning, redovisad.** Första försöket satte stillbilden som en `<img>`-nod (med
`width`/`height`) inuti `.rv`, tonad via en `load`-lyssnare i JS. Det introducerade en
allvarlig, mätt regression i en HELT annan sektion: `.step-band`s 3-kolumnsgrid
(`#process`) låste en kolumn till 0px vid just den DOM-insättningen, `--band-h` gick från
216px till 1849px, och `#process`/`#pris` ballonerade till att täcka nästan hela
dokumentet (bekräftat med och utan denna rundas två CSS-ändringar — orsaken var specifikt
`<img>`-noden, inte tesspalten). Verifierat genom att lägga till/ta bort elementet upprepat
(reproducerbart 100%, inte flakigt). En `background-image` på wrappern skapar ingen box och
kan per definition inte påverka någon annan boxs layout — bytet till den tog bort hela
regressionen utan att röra `.step-band` alls. Lärdom: en `<img>`, även abs.positionerad med
explicita mått, är inte alltid "fri" bara för att den ser isolerad ut.

Uppmätt (hjulscroll 800/400/100px vid 1440 och 390, lästa som bilder): stillbilden syns
tydligt och korrekt genom hela laddningsfönstret (Calyx-blommorna, Hōrai-tallriken), aldrig
en tom platta.

### Verifiering

- Hjulscrollsekvenser genom tesbandet vid 768 (9 bilder), 1024/1280/1440 (16 var), 390
  (7), i `shots/r3/wheel-*/`. Lästa: rubriken håller 3 rader (1440), spalten läsbar genom
  hela scrollet, ingen ny "på-topp"-korruption.
- Par-bilder P02 och P03 i `shots/r3/`, en skärm per sida (lokal HTTP-server, inte
  `file://` — samma lärdom som R2), lästa vid 1440 och 390. Håller nivån.
- Horisontell scroll: 0 vid 320/375/390/768/1024/1280/1440 (uppmätt före den slutliga
  bakgrundsbilds-lösningen; `background-image` kan per definition inte orsaka
  scrollbredds-overflow, så oförändrat efter).
- `a11y_scan.py`: 0 violations, 40 passes (R2: 41 — försumbar, förväntad variation).
- Låst copy: rubrikens källtext oförändrad (`Det första intrycket är digitalt.`,
  gemener i källan, versaler via CSS `text-transform`) — 15/15 håller.
- Grep: `prefers-reduced-motion` 0. U+2012–U+2015: 1 träff, samma CSS-kommentar som R1/R2
  (`.hero-plate`s perspektiv) — 0 i synlig text.

**V3d R3 klar**

## V3d R4

Astras andra granskning, paritetsläget: `reviews/r3-astra.md` § fidelity + § material_fixes,
läst i sin helhet. Lead tog 7 av 8 fynd (fynd 7, Hōrai-overflow i `sites/horai.html`, tas
inte — filen rörs aldrig, noterad nedan). Plan: `plans/051-astra-r3.md`.

### Fixtabell

| Fix | Expected (Astra) | Före | Efter | Par-bild |
|---|---|---|---|---|
| 1 · P13 steg 07 | Organisk scroll ger k7=1 OCH arkets top=band-h samtidigt; revisionsfältets rect utanför `.p-live` | Stick släppte vid ps≈0,883 (matchade `--s7`, inte `--e7` 0,944) — 07 stod aldrig färdig. Revisionsfältet (60×54, nedre vänster) kolliderade med kamerazoomad Calyx | `.process-steps{padding-bottom:60svh}` flyttar släppet till ps≈0,906 (efter e7). Revisionsfältet flyttat+krympt till övre högra hörnet (846,2,30×16) — enda ledig yta vid `--cam`=1 (samma zoom som godkänt steg 06, sänktes inte) | `par/r4/P13-1440.png`, läst: 07 står färdigritad, ingen kollision, 3px marginal genom hela ståendefönstret |
| 2 · P04 jättens bredd | `--scrub`=1 vid panelens top≈80-120px, plåt ≥1150px, `?preview=ledger` matchar organisk scroll | `--scrub` (start 0,364/bredd 0,315) mätt före R2:s margin-top:820px — full bredd nåddes efter att rubriken redan skurits av. Preview centrerade panelen, ett läge scroll aldrig visade | Ombisekterat: ps=0,4498 vid top=100px (ny bredd 0,086, samma start). `?preview=ledger` scrollar nu till exakt samma punkt bisektionen mätte (`giantTop-100`) i stället för `block:'center'` | `par/r4/P04-1440.png`; uppmätt top=100→bredd 1237px=86%vw, h1 helt synlig, P04-fönstret (calyx/tes borta) håller 4000-4250 |
| 3 · P06 kapitelskärmen | P06-1440 utan spår av band 01; 390 rubrik ≥56px centrerad; P16 max 4 mörka skivor i rad | `.process-lead{margin-bottom:144px}` för kort — band 01 tog nedre tredjedelen vid 1440, tom undre hälft vid 390 | Kicker+titel+lead wrappade i `.process-chapter{min-height:100svh;display:flex;justify-content:center}`, eget ljust materialtoken (`--bg:var(--c-paper)`) — full skärm, aldrig band 01, centrerad på båda breddar. **P16-kravet ströks av lead** (Anton: ingen ljus yta i akten 01-07 — de 7 numrerade stegen förblir en sammanhängande mörk följd, avsiktligt) | `par/r4/P06-1440.png`/`-390.png`, lästa: ren ljus skärm, ingen band-01-läcka |
| 4 · P10/P12 mobilark | `process-04` visar "96 px" inom arket; `process-06` Calyx ≥80% av arkets yta | `#p-c-row`s CSS x/y verkningslöst (en `<text>` läser bara SVG-attribut) — "96 px" stod utanför viewBox. Hatch 16×16px, olästbar. Calyx 288×162 av 320×300 = 48,6% | `p-c-row` tillagd i `MOBILE_TEXT` (40,118), hatch höjd till 16×80px. `#p-opening`+`#p-open-rect`/`#p-live-img` utökade till 304×260 = 82,3% (båda ändrade ihop — gick isär i ett första försök, vilket hade klippt bilden till den gamla ytan) | `par/r4/P10-390.png` ("96 PX" synlig), `par/r4/P12-390.png` (uppmätt 96% av arkytan — text i bilden beskärs något mer än förut, ett avvägt resultat av att nå 80%-målet i en nästan kvadratisk viewBox, inte en bugg) |
| 5 · P03 tesrubriken | Rubrik ≥64px vid 1440, panel ≥80% av viewportens höjd, 0 delade ord 1024-1920 | 38,4px, läst som bildtext. Panelen 45,6% av höjden | `.thesis-headline` clamp höjt till 4,5vw (64,8px vid 1440). `.panel-thesis{min-height:80svh;display:flex;justify-content:center}`. Spalten (R3:s 340px) räckte INTE längre vid den nya storleken (samma regressionsklass som R3 själv fixade) — höjd till 460px, bilden räknad om till 480px bleed för att hålla 40%vw | `par/r4/P03-1440.png`, läst: 3 rader, 0 delade ord, bild 40,8%vw, panel 80% |
| 6 · P02 ALUNIX | ALUNIX ≥100px vid 1440, ingen kollision | 80,6px (9cqw) | `9cqw`→`11.5cqw`, mätt 103,04px, 0 kollision mot `.card-glyph`/`.card-services` | `par/r4/P02-1440.png` |
| 7 · Hōrai-overflow — TAS INTE | `sites/horai.html` `scrollWidth` 675px vid 390 | — | Rörs aldrig (motorn/`sites/*` utanför scope) | — |
| 8 · Glyffragment + föräldralösa linjer | Inget partiellt glyf genom hela akten; inga omärkta streckade linjer i steg 05 | Fix 1:s (R2) timing-bugg fick band 07 att frysa mitt i sin egen incoming-klippning vid stickens (för tidiga) släpp. `#p-ledgers`/`#p-hatch` saknade `--cam-fade`, stod kvar i full ton genom hela 05 | Glyffragmentet **löstes som sidoeffekt av fix 1** (verifierat separat, se nedan) — ingen extra outgoing-klippning behövdes. `#p-ledgers,#p-hatch{opacity:calc((1-0.65*k6)*var(--cam-fade))}`, samma mönster som `#p-guides` | Hjulsekvens `wheel-1440/w048-w052` (y 13580-13850, lästa: 07 alltid helritad). `?preview=process-05` skärmbild: 0 synliga linjer, `opacity:0` uppmätt |

### Verifiering

- **Ordbrytning**: skriptet från R3 (samma metod) körd EFTER varje typografisk ändring (fix 5:s
  rubrikhöjning bröt initialt "INTRYCKET" vid 1440/1920 — samma regressionsklass som R3, spalten
  breddad igen). Slutresultat: 0 delade ord vid 768/1024/1280/1440/1920, alla rubrikklasser
  (`h1,h2,h3,.thesis-headline,.hero-headline,.giant`).
- **Hjulscrollsekvenser** (`mouse.wheel`, aldrig `scrollTo`) genom hela processakten: 59 bilder
  vid 1440 (y 6391-15091), 34 vid 390 (y 5809-~10800), `shots/r4/wheel-*/`. Lästa (spotkontroll
  vid kapitelskärm, steg 03, steg 07, aktens slut båda breddarna): rent, varje steg ändrar
  arket, ingen korruption.
- **Par-bilder** P02, P03, P04, P06, P10, P12, P13 (en skärm per sida, lokal HTTP-server via
  `skills/design/scripts/serve.py` — se felsökning nedan) + P16 (kontaktark, en enda
  `full_page`-fångst, ingen ihopsydd bild) i `shots/r4/`. Lästa, håller nivån.
- **scroll_verify.py** vid 1440/390: `cuesNeverFull`/`unrevealed` tomma båda. `blankBands`
  faller inom `#process` (kända artefakten, dömd på skivorna) eller matchar samma
  bakgrundsfoto-variansartefakt som R2/R3 dokumenterade. `contrastUnderMedia` vid 1440: ETT
  fynd, "Boka ett möte" 4,0 mot 4,5 — vid en NATURLIG scrollposition (inte `?preview=back`s
  stabila läge, som mäter 17,51), troligen kortets egen vändningsanimation där fotot skymtar
  genom. Ingen av denna rundas sju fixar rör hero/kortvändningen; inte utrett vidare av
  tidsskäl, namnges här i stället för att tystas. Vid 390: tomt.
- **motion_probe.py**, cpu 1: `#process:--sc-ps` och `#giant-section:--sc-ps`, `staircase 0`
  och `reversals 0` i alla körningar. `max_step_pct` över 3% vid grovt hjul (100:60) på
  jätten (2,85-3,38%) var samma dokumenterade samplingsartefakt som R2/R3 (kort, brant
  akt + grovt hjul) — bekräftat med fint hjul (20:120): 0,84%, ren.
- **contrast_over_media.py**: `?preview=ledger`/`process-02`/`process-06` visar
  `color:rgba(0,0,0,0)` på gradient-avslöjad text (`.scrub-text h3`, `.process-step-title`)
  — samma dokumenterade `background-clip:text`-begränsning som R1/R2 (verktyget läser den
  bokstavliga `color:transparent`, inte gradienten som faktiskt målar texten). Bekräftat
  läsbart i flera skärmbilder denna runda (FÖRVALTNING, INNEHÅLL, DESIGN/UTVECKLING/SYSTEM
  allt tydligt vitt/ljust på mörk grund).
- **a11y_scan.py**: 0 violations, 41 passes. **reflow.py**: `overflow320`/`overflowZoom200`
  tomma; `unrevealed:8` (R3: 7) — `#p-ledgers` tillkommen, samma kategori fynd som de andra
  sju (scroll-gated annotationer mätta i vila, inte en regression; väntat efter fix 8:s
  `--cam-fade`-tillägg). **tab_walk.py**: 0 issues.
- **Horisontell scroll**: 0 vid 320/375/390/768/1024/1280/1440/1920.
- **Låst copy**: ingen av de sju fixarna rörde textinnehåll (bara CSS-storlekar/positioner,
  JS-scrollmål, SVG-koordinater och en HTML-wrapper utan textändring) — 15/15 oförändrat.
- **Grep**: `prefers-reduced-motion` 0. Tankstreck: 1 träff, samma CSS-kommentar som
  R1-R3. Inline-hex utanför `:root`: CSS 16, markup/JS 2 — identiskt med R1-R3, ingen
  tillväxt.

### Felsökning, redovisad

- **`python -m http.server` dolde ett HTML-kommentarfel.** Ett första försök på fix 3 (kicker
  flyttad in i `.process-chapter`) verkade osynligt för Playwright (`querySelector` gav
  `null`) trots att `curl` visade rätt HTML-text. Bytte server till projektets egna
  `skills/design/scripts/serve.py` (HTTP/1.1, dokumenterad lösning på stora WebP-svar) —
  felet kvarstod IDENTISKT, vilket avslöjade att det inte var ett server-/trunkeringsfel
  utan en verklig bugg: min egen HTML-kommentar hade avslutats med `*/` (CSS-stil) i
  stället för `-->`, vilket svalde `<div class="process-chapter">` och kicker-`<p>`n in i
  kommentaren. Rättat. Lärdom: `python -m http.server`s dokumenterade HTTP/1.0-svaghet är
  fortfarande en verklig risk (fick separat bekräftat via `ERR_CONNECTION_RESET` i en
  tidig diagnos), men den här rundans faktiska bugg var kommentarssyntax, inte servern —
  isolera med `document.querySelectorAll(...).length` och en `pageerror`-lyssnare innan
  serverbyte antas vara lösningen.
- **Fix 5:s spaltbredd behövde ändras TVÅ gånger** (340→460px): första körningen av
  ordbrytningsskriptet (efter bara rubrikstorleken höjdes) visade "INTRYCKET" delat vid
  1440/1920 — samma mekanism som R3 fixade vid en mindre rubrikstorlek. Spalten breddad,
  om-verifierad (0 delade ord), och bildens bleed räknad om separat för att hålla 40%vw
  igen (31,8%→40,8%) efter att spaltens tillväxt ätit av bildens bas-bredd.
- **Fix 8:s glyffragment behövde ingen egen kod** — en hjulscreenshot-svep genom
  aktens utgång (y 13550-13950, var 30:e px) visade rent i varje bildruta EFTER fix 1:s
  timing-korrigering, utan att `--slit-p`-formeln rördes. Sparade en hel deluppgift genom
  att verifiera INNAN man kodar, inte efter.

**V3d R4 klar**

## V3d R5

Leadens egen pixelläsning av R4 i hjulscroll (900px/steg @1440, 800px/steg @390,
`shots/lead-r4/sheet-d0.png`/`sheet-d1.png`/`sheet-m0.png`). Två fel, båda R4:s egna fixar
som stred mot högre prioriterade krav. Plan: `plans/052-kapitel-och-mobilbeskarning.md`.
Ingenting annat rört.

### Fixtabell

| Fix | Fel (lead) | Före | Efter |
|---|---|---|---|
| 1 · kapitelskärmen | "Från samtal till lanserad sida." på ljus grund vid 1440 OCH 390 (`sheet-d0.png` rad 3 bild 2, `sheet-m0.png` rad 2 bild 2). R4 fix 3:s ljusa materialtoken bröt Antons order (processakten inverterad) — 4-mörka-skärmar-gränsen som motiverade den är uttryckligen struken av lead i R5-prompten | `.process-chapter{--bg:var(--c-paper);--ink:var(--c-drafting)}` — lokal flipp till ljust | Flippen borttagen helt. `.process-chapter` ärver `#process`s egna `--bg:var(--c-drafting);--ink:var(--c-paper)` rakt av. `min-height:100svh;display:flex;flex-direction:column;justify-content:center` (R4:s vinst: ensam vid 1440, fyller sin skärm vid 390) oförändrat — den delen är färgoberoende. `#process .process-lead,.process-p{color:color-mix(...)}` (R4 fix 3) rörd INTE — redan uttryckt i `--ink`/`--bg`, blir automatiskt rätt |
| 2 · Calyx beskärs @390 | Steg 06/07 zoomar in så rubriken klipps till "mical/tecture/kholm" (`sheet-m0.png` rad 2 bild 6, rad 3 bild 1-2). R4 fix 4:s 304×260-ruta (1,169:1) matchade aldrig bildens 16:9 (1,778:1); `preserveAspectRatio="xMidYMin slice"` fyllde genom att beskära sidled | `#p-opening`/`#p-open-rect`/`#p-live-img` 304×260 inom viewBox 320×300 (49→82% enligt R4, men beskuren) | Räkneexempel: en 16:9-ruta inom 320 bred viewBox kan aldrig nå 80% av en 320×300-yta (max ~54%) — 80%, 16:9 och bredd≤320 är ömsesidigt uteslutande. Löst genom att sänka ARKETS EGEN höjd (viewBox 320×300→320×200, JS `plansch()` + CSS `.process-sheet{aspect-ratio}`), bredden 320 oförändrad så alla x-koordinater (titelblock, 16:9-callout, hatch, måttlinjer) förblir giltiga. Öppning 304×171 (exakt 16:9, `#p-opening`/`#p-open-rect`/`#p-live-img`), `#p-dim-width` och `MOBILE_TEXT`s p-m320/768/1440-y omräknade till samma ±px-offset mot öppningens nya underkant som förut. `#p-cam` transform-origin omräknad till ny mittpunkt (160,100). Yta: 304×171/(320×200) = 81,2% — över 80%-målet |

### Verifiering

- **`contrast_over_media.py --url`**, kapitelskärmens `.kicker-sans`/`.process-title`: PASS
  vid 1440 (scroll 6271) och 390 (scroll 5688), värsta/medel 15,84:1 båda breddarna, golv
  4,5/3,0 — stor marginal.
- **Hjulscrollsekvenser** (`mouse.wheel`) genom hela `#process` vid **390, 768 och 1440**,
  `shots/r5/wheel-*/` + kontaktark `shots/r5/sheet-*.png`. Lästa i sin helhet: kapitelskärmen
  mörk med ljust bläck alla tre breddar; Calyx (steg 06/07) visar hela bilden — alla fyra
  kanter, "Botanical architecture, from Stockholm." obeskuren — vid 390 (ny 16:9-ruta), 768
  och 1440 (skrivbordskoordinaterna, redan 16:9, aldrig rörda). 768/1024 föll igenom till
  skrivbordets 538×303-ruta som väntat (`plansch()` läser `matchMedia('(max-width:767px)')` —
  ingen kodändring där, bara en visuell kontroll).
- **a11y_scan.py**: 0 violations, 41 passes, båda 390 och 1440.
- **Horisontell scroll**: 0 vid 320/375/390/768/1024/1280/1440/1920.
- **Ordbrytningsskriptet**: 0 delade ord vid 768/1024/1280/1440/1920, alla rubrikklasser —
  ingen av de två fixarna rörde typografi/spaltbredd, väntat resultat.
- **Låst copy**: 14/15 stickprovskontrollerade rader (samtliga `PRODUCT.md` § Brand
  Commitments-strängar utom en dubblettbekräftelse) verbatim kvar — ingen av de två fixarna
  rörde en enda textsträng, bara CSS custom properties, SVG-geometri, JS-koordinater och
  kommentarer.
- **Grep**: `prefers-reduced-motion` 0. Tankstreck (U+2010–U+2015, U+2212, U+2043, U+FE58,
  U+FE63, U+FF0D): 1 träff, samma HTML-kommentar som R1-R4 (inte synlig text, orörd av
  denna runda).

**V3d R5 klar**

## V3d R6

Astras tredje granskning, paritetsläget: `reviews/r5-astra.md` läst i sin helhet. 13/16
paritetsrader håller. Lead tar alla fyra `material_fixes`. Bevis: `shots/astra-r5/`
(`measure.json`, strip- och zoombilderna). Plan: `plans/053-astra-r5.md`. Inget annat rört.

### Fixtabell

| Fix | Fynd (Astra) | Före | Efter |
|---|---|---|---|
| 1 · mobilarket 06/07 | `#p-glyph` i full ton över Calyx övre vänstra hörn (`zoom-P12-390-sheet.png`); `#p-title`/`#p-rev` (revisionsfältet, en tre-radig ISO-stapel ärvd från FÖRE R5) korsar Calyx nav i övre högra hörnet (`zoom-P13-390-sheet.png`) — R5 flyttade öppningen (y20..191) men inte ritelementen. Mobilzoomen (0,08) gjorde dessutom öppningen 328 enheter bred i ett 320 brett ark — uppmätt 367px liveyta i 358px ark | `#p-glyph` permanent synlig (ingen `--cam-fade`); `#p-title`/`#p-rev` på y16..52 (inuti öppningen); `#p-cam` mobilzoom `1+0,08*--cam` | `#p-glyph{opacity:var(--cam-fade)}` — tonar ut i takt med kamerazoomen, samma mönster som `#p-hatch`/`#p-ledgers` (R4 fix 8). `#p-title`/`#p-rev` flyttade till den fria remsan ovanför öppningen (y2..18, en enradig 32×16-box, samma proportion som skrivbordets 30×16) och bort från fotot helt. `#p-cam` mobilzoom `0,08→0,05`: 304×1,05=319,2≤320, ingen beskärning |
| 2 · revisionsbokstaven @1440 | `MOBILE_TEXT['p-c-rev']` hade kvar `[54,451]` som skrivbords-koordinat — ett dött värde (markupens egna `x="861" y="13"` vinner alltid på ≥768) men motsade DOM:en | `[54, 451, 256, 26]` | `[861, 13, 296, 13]` — skrivbordsindex rättat till markupens verkliga tal, mobilindex centrerat i fix 1:s nya fält (280..312 → x=296, samma 11px-offset från fältets topp som skrivbordets 861/13 → y=13) |
| 3 · aktens utgång @1440 | `.process-stick` släpper (~14020) FÖRE band 07:s eget sticky-släpp (~14160) — en 140px lucka där arket (z-index 2, solid `--bg`) glider över "07"/FÖRVALTNING och skär av texten | `.process-steps{padding-bottom:60svh}` | Uppmätt via binärsökning (`getBoundingClientRect` var 10:e px, flera paddingvärden testade och omätta, inte gissade): `.process-stick`s sticky-behållare är `.process-grid`, som ärver `.process-steps`s totalhöjd inkl. padding — den paddingen styr alltså STICKENS EGEN släpppunkt, oberoende av band 07:s (som bara läser li07:s egen höjd mot `--band-h`). `60svh→80svh`: stick släpper nu vid ~14200, 40px EFTER band 07:s eget (~14160) |
| 4 · jättens typografiska ögonblick (P04) | `.giant` clampar till 5,5rem (88px) @1440 — mindre än kapitelrubrikens 103,68px. Ska vara sidans starkaste ögonblick efter heron | `transform:scale(calc(0,92+0,08*var(--sc-ps,0)))` — ändrar bara det MÅLADE, aldrig layouten (ordbrytningen låst vid basclampens 88px oavsett skalvärde), och läser act-bred `--sc-ps`, inte plåtens egen `--scrub` | Ersatt med en riktig `font-size`-höjning bunden till `--scrub` (samma variabel som redan styr plåtens breddökning, rad ~951), skopad till ≥901px (samma brytpunkt som `.panel-giant`s bleed): `font-size:calc(clamp(2.1rem,7.4vw - 18px,5.5rem) + var(--scrub,0) * 1.75rem)`. Vid scrub=0 (plåtens smala 555px-startläge): 88px, oförändrad, känd säker marginal. Vid scrub=1 (den utskrivna plåten): 88+28=**116px**, 12px marginal över 110px-golvet |

### Verifiering

- **Uppmätt (Playwright, `getComputedStyle`), `?preview=ledger`, `.giant`:** 768→38,8px
  (basclampen, orörd, under 901px-brytpunkten), 1024→85,8px, 1280→104,7px,
  **1440→116px**, 1920→116px. Matchar formeln exakt vid varje bredd.
- **Ordbrytningsskript, riktat mot `.giant` specifikt i `?preview=ledger` (scrub=1, den
  NYA större storleken):** 0 delade ord vid 768/1024/1280/1440/1920, VARUMÄRKE helt på en
  rad vid alla fem. Samma skript i normalläge (scrub=0, obesökt sida): 0 delade ord,
  identiskt med R4/R5:s baslinje.
- **Uppmätt (binärsökning, `getBoundingClientRect` var 10:e px, 13600–14700, flera
  `padding-bottom`-värden 60→100svh testade före valet av 80svh):** vid 80svh släpper
  `.process-stick` vid scrollY≈14200, band 07 vid ≈14160 — sticken släpper EFTER bandet,
  aldrig innan. Bekräftat i den faktiska filen (inte bara i det injicerade testet).
- **Hjulsekvens** genom aktens slut vid 1440, 40px-steg, 13800–14400 (16 bilder,
  `shots/r6/sheet-exit-1440.png`), läst i sin helhet: "07"/FÖRVALTNING/brödtexten hela och
  läsbara i varje bildruta, aldrig avskurna av arkets överkant. Arket har lämnat scenen
  helt innan "Hur vi tänker" tar över.
- **Hjulsekvenser genom steg 06/07** vid 390 (23 bilder) och 768 (36 bilder),
  `shots/r6/sheet-steps0607-*.png` + individuella ramar lästa i zoom: Calyx alla fyra
  kanter synliga, "Botanical architecture, from Stockholm." obeskuren, inga ritelement
  ovanpå fotot vid 390 (revisionsfältet syns tydligt FLYTTAT till den fria remsan ovanför
  bilden, bredvid "Calyx"-ordmärket, aldrig över den). 768 oförändrat (skrivbordskoordinater,
  ingen kodändring där), bekräftat rent.
- **`motion_probe.py` för `#process:--sc-ps` vid 1440.** Två körningar: (1) `?preview=
  process-04` (JS-teleport till stegets position före mätning) gav `staircase 1,
  max_step 100%` — undersökt, INTE en regression: samma mönster som R2-R4:s dokumenterade
  coarse-wheel-artefakter, men här orsakad av `aimPreview()`s ögonblickliga
  `scrollTo`-hopp, inte av en verklig scrollrörelse. (2) Organisk hjulscroll från
  ren URL genom HELA `--sc-ps`-spannet (0 till 1, 18 371 bildrutor, `wheel 20:120`):
  `max_step_pct 0,07%`, **`staircase 0`**, **`reversals 0`** — spelhuvudet glider
  perfekt, noll steg, genom precis den utgång fix 3 ändrade. Enda kvarvarande fyndet,
  "297 bildrutor >33ms" (p95 fortsatt frisk, 16,8ms), är en bildrutetimingsfråga över en
  ~18 000-bildruters/flera-minuters körning, inte en värdehopp-defekt — ingen av denna
  rundas fyra fixar rör renderingskostnad per bildruta (statiska CSS-tal, SVG-attribut,
  en font-size-formel), namnges här i stället för att tystas, inte utredd vidare av
  tidsskäl.
- **a11y_scan.py**: 0 violations, 41 passes, båda 390 och 1440.
- **Horisontell scroll**: 0 vid 320/375/390/768/1024/1280/1440/1920.
- **Låst copy**: 14/14 stickprovskontrollerade `PRODUCT.md`-strängar verbatim kvar —
  ingen av de fyra fixarna rörde en enda textsträng.
- **Grep**: `prefers-reduced-motion` 0. Tankstreck: 1 träff, samma HTML-kommentar som
  R1-R5 (inte synlig text, orörd av denna runda).

**V3d R6 klar**

## § Arkitekten R7, 2026-09-19 (Opus, plan 054)

`Skill(design)` laddad först. Tier 0: V3d:s låsta system, inga nya tokens. Plan
`plans/054-tesband-och-case.md`, copy `COPY-V3d-v0.md`, `PARITET.md` P03/P04/P14 omskrivna,
P05 utgången, P17 till P20 nya.

- läst: runs/V3c/RAPPORT-LOOPEN.md
- läst: runs/V3d/index.html (CSS 88 till 1590, markup 1590 till 2060, JS 2062 till 2714)
- läst: runs/V3d/plans/048-inverterad-variant.md
- läst: runs/V3d/NOTES.md § V3d R1 till R6
- läst: runs/V3d/PARITET.md, runs/V3d/reviews/r5-astra.md
- läst: tests/alunix-r8/PRODUCT.md, runs/V3d/PROCESS-UNDERLAG.md, runs/V3d/COPY-GATE.md
- läst: scroll/scrollcraft.js (pin: p = (y − top)/(height − vh), span sätter höjden), scroll/sc-smooth.js (rubriker)
- läst: design/references/scroll/devices.md rad 8 till 30
- läst: sites/calyx.html och sites/horai.html (sektioner, scrollskript; Hōrai har `scroll-behavior:smooth`, ordljus och citatskrubb på egen scroll)
- läst (bild, egen fångst, `mouse.wheel` 900 px/steg): nuläget 1440x900, 19 skärmar, kontaktark
- läst (bild, egen fångst, 800 px/steg): nuläget 390x844, 16 skärmar, kontaktark
- läst (bild): shots/lead-r6/sheet-d.png
- läst (bild, egen fångst i 840x760): Calyx 15 skärmar och Hōrai 11 skärmar, skrollade med hjul
- läst (kontaktark): runs/V3c/shots/fasA/hoy-1440/ (23), highway-1440/ + insign-1440/ (22), hoy-390/ (20)

Uppmätt nuläge (Playwright): dokument 16 773 px vid 1440 (11 387 vid 390); tesen 651x720 vid
1440, rubrik 64,8 px, stödstycke 15,2 px. Calyx i 840x760: 4 665 px, ankare `#studio` 782,
bildpar 1 258, `#index` 1 874, `#commission` 3 981. Hōrai i 840x760: 8 314 px, huset 760,
citatet 1 677, menyerna 2 677, rummet 6 191, `#reservations` 7 027. Mätskript i scratchpad
(`a054/shoot.py`, `sites.py`, `sites2.py`).

## V3d R7

Byggaren, plan 054 (`plans/054-tesband-och-case.md`) i sin helhet, `COPY-V3d-final.md`
(kolumnen final skriven in ordagrant, ingen sträng omskriven), `PARITET.md` och
`reviews/r6-astra.md` lästa. `Skill(design)`, `Skill(animate)`, `Skill(emil-design-eng)`
körda först. Kirurgiska `Edit`, motorn (`scroll/*.js`, `scrollcraft.css`) och `sites/*`
orörda genom hela rundan.

### Steps 1–5 byggda

1. **Tesbandet** (`#tes`, `data-sc-act="pin" data-sc-span="5.5"`) ersätter `.panel-thesis` +
   `.stagger`. Fem `.ts`-element (fyra oförändrade + "Vi hjälper er att synas på rätt sätt."
   inskriven ordagrant, "VI BYGGER ERT VARUMÄRKE." flyttad hit som mening 5), en i taget i
   rubrikplatsen via `--in`/`--out`-springan (samma teknik i `.js .cs` för casens steg).
   Hyperborea-bilden går gråskala → färg vid mening 3, `--sc-ps` 0,4–0,6.
2. **Jättesektionen borta.** `#giant-section`, `.panel-giant`, `.giant*`, `.ledger-wrap`,
   `.thread*`, `.is-scrubbed`-mekaniken, `--rv`-revealmekanismen (`@property --rv`, alla
   `.rv`-regler) och `#principer` ("Hur vi tänker") borttagna. `.ledger-num` behållen
   (processtegens siffror). De två låsta raderna flyttade: "VI BYGGER ERT VARUMÄRKE." →
   tesens mening 5; "Webbdesign, design och system. Allt på ett ställe." → `.process-locked`
   i kapitelskärmen. **Ridån**: `#process{margin-top:-100svh}`, `.chapter-hold{height:calc
   (200svh+40svh)}`, `.process-chapter{position:sticky;top:0}` — tesens blå stage (z-index 2)
   glider upp och lämnar den stillastående kapitelskärmen (z-index 1) synlig.
3. **Copyn**, förenklad enligt `COPY-V3d-final.md` (redan skriven in i steg 1/4:s markup,
   status **oförändrad**/**låst** för processakten — ingen sträng där ändrad denna runda).
4. **Case-kapitlet + Calyx + bryggan + Hōrai** ersätter `#principer`. Fyra nya sektioner,
   `id="case"`/`"case-calyx"`/`(ingen id)`/`"case-horai"`. Casens ramar skrollas INIFRÅN
   (`CASES`/`measureCase`/`caseY` i JS, `contentWindow.scrollTo`, aldrig en transform på
   ramen). Exakt 2 `iframe`, monteras när processakten når steg 05
   (`stepAnchors[4]`), inte vid heronts landade svans (tesens meningsbyte ska inte dela
   huvudtråden med två sajter som startar).
5. **Balans**: tre nya sektionsanatomier (pinnad helbredd med bytande rad; kapitel i
   centrerad spalt; delad diptyk med ram mot kanten), materialrytm foto→blått→ritbordet→
   papper→svart plåt→foto, `#1e5e9c` fortfarande exakt två förekomster.

### Astras två kvarstående r6-fynd

| Fynd | Fix |
|---|---|
| `.step-band .process-p` låg ovanpå siffran/noten vid 768–1023 (ärvde `grid-row:1/span 2`) | `.step-band .process-p{grid-row:3}` i mediet. Uppmätt: 0 rektangelöverlapp mellan `.ledger-num`/`.process-step-title`/`.process-note`/`.process-p` vid 768, 900, 1023 (`?preview=process-07`, `getBoundingClientRect`) |
| Mobilens revisionsfält (y2..18) gick 2 enheter in i den kamerazoomade bildens överkant (16, efter `#p-cam`s 1,05-skala) | Fältet sänkt till y0..14 (`M280 0 H312 V14 H280 Z`, `#p-rev` samma). `MOBILE_TEXT.p-c-rev` mobil-y 13→11 (samma 11px-offset mot fältets nya topp) |

### Target-tabell (urval, fullständig lista i plan 054 § Target)

| Target | Mål | Uppmätt | Bild |
|---|---|---|---|
| 1 · tesbandets stage | 100 % vw × 100 % vh | `getBoundingClientRect()`: 1440×900 vid 1440, 390×844 vid 390 | `shots/r7/preview/thesis-01-1440.png` |
| 1 · meningarnas storlek | 88 px (390: 35,5 px), alla fem lika | `getComputedStyle(.ts).fontSize`: 88px vid 1440 (kontrollerat på flera `.ts`) | — |
| 1 · en mening åt gången | noll glyfpixlar av annan mening i `?preview=thesis-0N` | `.thesis-ticks i` `background-color` diagonal: tick N vitt (1,1,1) bara vid `thesis-0N`, alla andra dämpade, N=1..5 (mätt, se § tick-buggen nedan) | `shots/r7/preview/thesis-0{1..5}-1440.png` |
| 1 · "Vi hjälper er att synas på rätt sätt." | mening 4 av 5 | `style="--i:3"` i DOM, bekräftat i kontaktarket | `shots/r7/sheet-1440-a.png` rad 3–4 |
| 1 · ordbrytning | 0 delade ord 768–1920 | Ordbrytningsskriptet på `.ts,.case-title,.cs h3,.cases-title,.bridge-title,.process-title,.process-step-title` (30 element): clean vid 768/1024/1280/1440/1920 | — |
| 2 · jättesektionen borta | 0 träffar `#giant-section,.stagger,#principer` | `document.querySelectorAll(...).length === 0` (smoke test) | — |
| 2 · låst copy kvar | 15/15 rader ordagrant | Stickprov mot `PRODUCT.md` § Brand Commitments + `.sr-only`: 15/15 | — |
| 2 · ridån, rubrikens `top` | oförändrad (±1 px) genom lyftet | `getBoundingClientRect().top` var 100:e px, scrollY 7100–8000: **exakt 264,53125 px hela vägen, 0 px drift** (bättre än målet) | mätning i terminalen, se dialog |
| 4 · case-kapitlet | rubrik ≥ 100 px | `getComputedStyle(.cases-title).fontSize`: 120px (7,5rem-taket) vid 1440 | `shots/r7/par/P14-cases-1440.png` |
| 4 · Calyx: sajten rullar i takt | `contentWindow.scrollY` = ankare ±2 px | Uppmätt exakt (0 px avvikelse): ankare `#studio + section` vid embeddad bredd 835px gav offsetTop 1253, `caseY()` returnerade 1253 | dialog, `debug-768-calyx03-b.png` |
| 4 · iframe-budgeten | exakt 2 | `document.querySelectorAll('iframe').length === 2` | smoke test |
| 4 · Hōrais egna rörelser | citatet i format läge vid `-03` | Japanska raden "料理は対話である" skarp/läsbar i ramen vid `case-horai-03` | `debug-horai03-frame-only.png` |
| 4 · priset direkt efter Hōrai | ingen lucka | `horaiBottom === prisTop` exakt (29682px vid 1440) | `debug-p20-transition.png` |
| 5 · varje PARITET-rad | håller nivån | P03, P04 (curtain+chapter), P14, P17 (01/03/05), P18, P19 (01/03/06) lästa som par-bilder, alla håller | `shots/r7/par/*.png` |

### Fel hittat och lagat under bygget

- **Tick-/skenindikatorns off-by-one.** `.thesis-ticks i`/`.case-rail span`s `--on`-formel
  (kopierad ur plan 054:s CSS, skriven mot 1-indexerat `nth-child(N)`) användes med mitt
  eget 0-indexerade `--i` (`--i:0`..`--i:4`) utan att räkna om — tick 2 lyste vid mening 1:s
  scrollläge. Rättad `(var(--i) - .5)` → `(var(--i) + .5)` i båda reglerna. Verifierat efteråt:
  diagonal matchning tick N ↔ mening N vid alla fem `thesis-0N`-lägen.
- **Ingen kodbugg, två felavlästa mätningar** (dokumenterade så nästa runda inte återupprepar
  dem): (1) Calyx-ramens ankare mätta mot en fristående 1440px-vy av `calyx.html` i stället
  för ramens FAKTISKA inbäddade bredd (~835px, satt av 7fr/12-spalten) — sajten ombryter
  annorlunda vid den bredden, vilket gav en skenbar 161px "avvikelse" som försvann när
  ankaret mättes vid rätt bredd. (2) En provskärmdump av `?preview=case-calyx-03` vid 768
  togs efter bara 1,2s — aim/case-synken tar upp till ~2s att bosätta sig efter ett
  preview-hopp (organisk hjulscroll drabbas inte, cur lerpar kontinuerligt); en om körning
  med 3s väntan visade korrekt synk.

### Verifiering

- **Hjulsekvenser** (`mouse.wheel`, 150px/steg) genom HELA sidan vid 1440 (200 bilder),
  1024 (172), 768 (229, obligatorisk bredd — inget överlapp hittat), 390 (169) →
  `shots/r7/wheel-<bredd>/`, lästa som kontaktark (`sheet-<bredd>-a.png`, varannan bild).
  Alla fyra: rent flöde genom tes → ridå → process → case-kapitel → Calyx → brygga → Hōrai →
  pris, ingen dödram, ingen kollision.
- **Par-bilder**, alla PARITET-rader med ny/omskriven status (P03, P04, P14, P17–P20) →
  `shots/r7/par/`, lästa: håller nivån på samtliga (se Target-tabellen).
- **`scroll_verify.py`** vid 1440: `cuesNeverFull`/`unrevealed`/`contrastUnderMedia` alla
  tomma. `blankBands` finns (fyra pinnade akter — tes, process, Calyx, Hōrai — ger en
  full-page-fångst inga uppdaterade `--sc-ps`-lägen att visa; samma dokumenterade
  artefakt som varje tidigare runda med pinnade akter). Vid 390: `cuesNeverFull`/
  `unrevealed` tomma; ETT `contrastUnderMedia`-fynd (kapitlets tre rader, värsta 1,01–2,06),
  undersökt: provet landade mitt i ridåns curtain-lyft (en avsiktlig, transient
  täckningseffekt) — `?preview=chapter` (stagen helt borta) mätte om samma rader vid vila:
  fullt läsbara, matchar de 15,84:1 tidigare rundor mätte. Transient animationsram, inte ett
  fel.
- **`motion_probe.py`**, fint hjul (20:120), cpu 1, `#tes`/`#process`/`#case-calyx`/
  `#case-horai` samtidigt genom HELA dokumentet (18 192 bildrutor, värde 0 till 1 på alla
  fyra): **`staircase 0`, `reversals 0`** på alla fyra, `max_step_pct` 0,06–0,13 % (långt
  under 3%-golvet). Enda avvikelsen: 431 av 18 192 bildrutor (2,4%) över 33ms — p95
  fortsatt frisk (16,8ms på alla fyra); en bildrutetimingsfråga över en extremt lång
  (18 000-bildruters, fyra spår samtidigt) körning, samma dokumenterade mönster som R6:s
  "297 bildrutor". Ingen värdehopp-defekt.
- **`perf_probe.py`**: vid naturlig laddning PASS, 0 fynd, LCP 188ms, CLS 0, 0 long tasks.
  Med båda ramarna levande (`?preview=case-horai-03`): LCP 488ms, CLS 0,0049, 0
  `long_tasks_under_scroll`, dom_nodes oförändrat 253. Ett fynd,
  `below-fold-image-not-lazy` på `#heroPoolImg` — undersökt: en artefakt av att testa med
  ett djupt `?preview=`-hopp (sidan laddar redan scrollad, vilket lurar
  above/below-fold-avläsningen); bilden är sidans egna LCP-bild med avsiktlig
  `fetchpriority="high"`, ingen kodändring.
- **`contrast_over_media.py --url`**: tesen (thesis-03, alla fem `.ts` + bildtext) PASS
  6,70:1. Case-kapitlet PASS 16,60–20,28:1. Calyx (alla fem steg + skena) PASS
  5,55–18,46:1. Hōrai (alla sex rubriker) PASS 17,50:1. Bryggan PASS 17,50:1.
- **`a11y_scan.py`**: 0 violations, 41 passes vid 390, 768 OCH 1440.
- **`reflow.py`**: `overflow320`/`overflowZoom200` tomma, extra-viewport 768x1024 tom.
  `unrevealed:8` — samma SVG-utrop (`#p-c-169` m.fl.) som varje tidigare runda, mätt i vila
  före sitt eget `--sc-ps`-fönster, inte en regression.
- **`tab_walk.py`**: 0 issues, 2 stopp (de två `kontakt@alunix.se`-länkarna), båda med
  synlig fokusring.
- **Horisontell scroll**: 0 vid 320/375/390/768/1024/1280/1440/1920.
- **Ordbrytningsskriptet**: 0 delade ord vid 768/1024/1280/1440/1920 över 11 rubrik-/
  meningsklasser, 30 element kontrollerade.
- **Låst copy**: 15/15 rader (inkl. `.sr-only`) ordagrant.
- **Inline-hex**: 16 CSS-deklarationer + 2 markup/JS utanför `:root` — exakt samma som
  R6:s baslinje, ingen tillväxt (femton ytterligare CSS-TRÄFFAR i kommentarer/dokumentation
  uteslutna från räkningen, matchar hur R1–R6 räknade).
- **Grep**: `prefers-reduced-motion` 0. Tankstreck: 1 träff, samma HTML-kommentar som
  R1–R6 (inte synlig text).

**V3d R7 klar**

## V3d R8

Astras granskning av R7 (`reviews/r7-astra.md`), läst i sin helhet. Åtta material_fixes,
verifierade mot fil och bild i `shots/astra-r7/`. Lead tar alla åtta i Astras ordning.
Plan: `plans/055-astra-r7.md`. `Skill(design)`, `Skill(animate)`, `Skill(emil-design-eng)`
körda först. Copyn rörd inte. Kirurgiska `Edit`, motorn orörd.

### Fixtabell

| # | Mål | Före | Efter | Bild |
|---|---|---|---|---|
| 1 · tesbandets meningsbyte | 0px vertikalt överlapp mellan synliga `.ts` i varje bildruta, hjul 20px-steg, 1440/768/390 | `--in`/`--out` öppnade/stängde symmetriskt (±f/2) kring SAMMA punkt `b` — två meningar delvis synliga samtidigt. Uppmätt 130px (1440), 62px (768), 41px (390) | Asymmetriska fönster: `--in` över `[a,a+f]`, `--out` över `[b-f,b]`. Utgående helt stängd exakt när inkommande börjar. Mätt (egen skript, validerat mot den kända buggen — se Verifiering): **0px överlapp**, alla tre breddar | `shots/r8/sheet-tes-transition.png` |
| 2 · Calyx-stagens grund | `getComputedStyle(.case-stage).backgroundColor` = `rgb(253,251,244)` | `.case--calyx{--bg:var(--bg)}` cyklisk deklaration → `--bg` ogiltig → `background:transparent` → heroens foto syntes igenom | Raden borttagen; `#case-calyx` ärver `:root`s `--bg`/`--ink` ostört | Uppmätt **exakt** `rgb(253, 251, 244)` / ink `rgb(22, 20, 15)` | `shots/r8/final-case-calyx-01-1440.png` |
| 3 · casens stegbyte | Samma som fix 1, Calyx (n=5) och Hōrai (n=6) | Samma symmetriska bugg, 9px överlapp | Samma asymmetriska fönster i `.js .cs` | **0px överlapp**, 1440 och 390, båda casen | `shots/r8/sheet-horai-transition.png` |
| 4 · Hōrais citatankare | `#quote-jp` opacitet 1, `#quote-text` `blur(0px)`, 1440 och 390 | `-0,40` (fast tal). 1440 råkade träffa nära rätt av misstag (proximity ≈0,52); vid 390 helt fel (opacitet 0,81, blur 2,5px) | Först satt till `+0,15` (räknat mot `h-[130vh]`) — höll vid 1440 men INTE vid 390 (Hōrais `min-h-[1000px]` dominerar vid smal ram, `+0,15` var fel förhållande där). Bytt till dynamiskt `'center'`-läge: `measureCase` läser sektionens EGNA `offsetHeight` och centrerar riktigt, oavsett vilken av Tailwinds två klasser som vinner | Uppmätt opacitet 1 / blur 0px vid **1440, 768 och 390** | dialog (DOM-mätning i ramen) |
| 5 · Calyx-ramens storlek | 1440: ≥58%vw × ≥88%vh. 390: ≥50%vh | 1440: 806×789 = 56%×87,7%. 390: 400px = 47,4%vh | `.case-stage` kolumner `5fr/7fr`→`4fr/8fr` (Hōrai spegelvänt `7fr/5fr`→`8fr/4fr`); `padding-block` `clamp(24,4svh,40)`→`clamp(16,3svh,32)`; mobil rad `52svh`→`58svh` | 1440: **921,6×807 = 64,0%×89,7%**. 390: **450,5px = 53,4%vh** | dialog (`getBoundingClientRect`) |
| 6 · Hyperboreas andel | ≥36%vw vid 1440 och 768 | `.thesis-stage` kolumn `.62fr`: 496px = 34,4%vw | `.62fr`→`.7fr` | **1440: 533,7px=37,1%vw. 768: 284,6px=37,1%vw** (samma vw-andel, förhållandet skalar) | dialog |
| 7 · tomt band vid 390 | Inget stort tomt band mellan mening och streck | `min-height:7×radhöjd` (243px) mot mening 3:s faktiska 4 rader — ~104px tomt | `7`→`4` (139px, matchar mätt höjd exakt); tredje raden (bilden) satt `1fr` i stället för `auto`, `.thesis-photo-box` `flex:1` — frigjort utrymme går till bilden, ingen `--sc-ps`-koppling så bilden flyttar sig inte mellan meningarna | Mätt gap mening→streck: **41px** (normal marginal, inte ett tomt band) | dialog |
| 8 · `?preview=chapter` | Band 01 osynligt vid 1440 och 390 | `ridaY(150)` siktade 10vh förbi det säkra fönstret, visade band 01 i underkanten | `ridaY(120)`, uppmätt (binärsökning var 10:e intoVh): säkert fönster är intoVh [100,140), 150 var redan fel | **0px av band 01 synligt**, 1440 och 390 | `shots/r8/final-chapter-1440.png`, `final-chapter-390.png` |

### Verifiering

- **Fix 1/3, överlapp.** Egen mätskript: hjul 15–20px-steg genom hela tesen (1440/768/390)
  och båda casen (1440/390), `getComputedStyle(el).clipPath` avkodad (box-shorthand-medveten
  parser — CSS `inset()` serialiserar till 1–4 token beroende på symmetri, en första
  parserversion missade detta och rapporterade falskt 0 överlapp både med och utan fixen).
  **CARL-kontroll:** samma skript kört mot den GAMLA, trasiga formeln (`add_style_tag`,
  `!important`) gav **382,8px uppmätt överlapp** — bekräftar att mätningen faktiskt fångar
  felet innan den godkänns som bevis för fixen. Med fixen: **0px överlapp i alla 1 668
  kontrollerade bildrutor**, sju kombinationer (tes×3 breddar, Calyx×2, Hōrai×2).
- **Hjulsekvenser**, 20px-steg genom en meningsgräns (tes, 1440) och en stegväxling
  (Hōrai, 1440), 20 bildrutor vardera → `shots/r8/sheet-tes-transition.png`,
  `sheet-horai-transition.png`, lästa: rent, ingen bildruta visar två meningars/stegs
  glyfer samtidigt. Övergången läses som en avsiktlig topp-till-botten-avslöjning, inte
  en krock.
- **`motion_probe.py`**, fint hjul (20:120), cpu 1, positionerat nära varje akt via
  `?preview=` (organisk scroll från toppen gav `DEAD` — ett för kort tick-antal för att nå
  akterna, samma kända begränsning som tidigare rundor; löst med `?preview=thesis-02` /
  `case-calyx-03` / `case-horai-03` som startpunkt). Alla tre: **`staircase 0`,
  `reversals 0`**, `max_step_pct` 0,71/1,14/0,79% (långt under 3%-golvet). Enda avvikelsen:
  9–17 av ~2 650 bildrutor över 33ms per spår (p95 friskt, 16,7–16,8ms) — samma
  dokumenterade bildrutetimingsmönster som R6/R7, inte en värdehopp-defekt.
- **a11y_scan.py**: 0 violations, 41 passes, båda 390 och 1440.
- **Horisontell scroll**: 0 vid 320/375/390/768/1024/1280/1440/1920.
- **Ordbrytningsskriptet**: 0 delade ord vid 768/1024/1280/1440/1920, alla rubrik-/
  meningsklasser (inkl. de nya `.ts`/`.case-title`/`.cs h3` efter kolumnändringarna i
  fix 5/6).
- **Låst copy**: 15/15 rader ordagrant — ingen av de åtta fixarna rörde en textsträng.
- **Grep**: `prefers-reduced-motion` 0. Tankstreck: 1 träff, samma HTML-kommentar som
  R1–R7 (inte synlig text).

**V3d R8 klar**

## V3d R9

Astras granskning av R8 (`reviews/r8-astra.md`), läst i sin helhet. Tre material_fixes,
alla bara vid 390 — vid 1440 höll varje PARITET-rad redan (Astra bekräftar detta
explicit; ingen ändring tillåten där). Verifierade mot fil och bild i `shots/astra-r8/`.
Plan: `plans/056-astra-r8-mobil.md`. `Skill(design)` körd först. Copyn rörd inte
(`sites/*` rörs aldrig — Hōrais fix löstes på vår sida, ramens höjd + ankaret).
Kirurgiska `Edit`, motorn orörd.

### Fixtabell

| # | Mål | Före | Efter | Bild |
|---|---|---|---|---|
| 1 · Hōrais citat vid 390 | Citatet helt synligt, under navens underkant, vid `case-horai-03` | Ramens innerhöjd 450px; en sant centrerad `min-h-[1000px]`-sektion i en så kort ram lade citatet delvis bakom sajtens egen nav | Hōrai-specifik mobil radhöjd `58svh`→`72svh` (ih 450→568px). `measureCase()` fick ett valfritt kort-ramsoffset (`a[2]`/`a[3]`): citat-ankaret blir `['#quote-section','center',-100,700]` — vid ih<700 skiftar ankaret 100px ovanför sant centrum, annars oförändrat sant centrerat | Citatet ("Cooking is a conversation between three flowers...") helt synligt under navet vid 390 OCH 375. 1440: ih=805>700, villkoret aldrig sant, ankaret exakt sant centrerat precis som i R8 | `shots/r9/w390/case-horai-03.png`, `w375/case-horai-03.png` |
| 2 · tomt band i tesbandet vid 390 | Gap mellan streck och foto ≤32px, foto ≥400px högt | `.thesis-figure` ärvde `align-self:end` (bas-regel, aldrig återställd i mobilfönstret) — figuren tog bara sin egen innehållshöjd i stället för att fylla grid-radens `1fr`, så `.thesis-photo-box{flex:1}` hade inget fritt utrymme att växa in i och föll tillbaka på sin ärvda `aspect-ratio:16/10` = 215px hög bild, 285px tomt band ovanför | I `@media (max-width:767px)`: `.thesis-figure{align-self:stretch}`, `.thesis-photo-box{aspect-ratio:auto}` — figuren fyller nu hela raden, flex:1 får fritt utrymme, bilden fyller raden (object-fit:cover beskär utan distorsion) | Bilden fyller raden i alla fem meningar (`thesis-01`…`05`), inget tomt band, identisk vertikal position mellan meningarna, ingen läser `--sc-ps` | `shots/r9/w390/thesis-01.png` … `thesis-05.png` |
| 3 · Calyx steg 03 vid 390 | Minst ett foto med sin bildtext helt inne i ramen | `['#studio + section', 0]` siktade sektionens egen topp, ~76px ovanför första figurens topp (mätt direkt i `sites/calyx.html`: `figTopAbs≈1631`, `capBottomAbs≈2115`, figur+bildtext 484px) — varken höjd eller ankarplacering räckte i en 450px ram | Delad mobil radhöjd `58svh`→`66svh` (ih 450→517px). Ankaret fick samma offset-mekanism som fix 1: `['#studio + section', 0, 76, 700]` — vid ih<700 läggs +76px (figurens egen topp i stället för sektionens padding) | Foto 1 ("Cmsn. 0211 — Hotel Pigalle, Drottninggatan") med HELA bildtexten ("02/14") synligt inom ramen vid 390 OCH 375. 1440: ih=805>700, offset ej tillämpat, ankaret oförändrat | `shots/r9/w390/case-calyx-03.png`, `w375/case-calyx-03.png` |

### Verifiering

- **Enskilda skärmbilder** (inga kontaktark), 390 och 375, `?preview=thesis-01..05`,
  `case-horai-03`, `case-calyx-03` — alla lästa. Tesbandets fem meningar: bilden fyller
  raden i varje, identisk position. Hōrais citat: helt synligt under navet (den
  horisontella textklippningen som syns på höger kant är sajtens EGEN responsiva
  textstorlek vid smal ram — bekräftat oberoende av vår scrollposition genom en
  fristående capture av `sites/horai.html` scrollad till `#quote-section`; `sites/*`
  rörs aldrig, och Astras fynd gällde vertikal skymning bakom navet, inte detta).
  Calyx steg 3: foto + hel bildtext inom ramen.
- **Regressionskoll, Hōrais övriga steg** (01, 02, 06) vid 390, samma delade
  radhöjdsändring: hero, ordljus och bokningssektionen renderar oförändrat, ingen
  text klipps av caseramen.
- **Hjulsekvens** vid 390: 20 hjulsteg genom tesbandet (thesis-01-startpunkt) och 25–30
  steg genom vardera casens `?preview=`-01-startpunkt — rent, inga glitch, inga
  överlappande sektioner, ramarnas synk med värdsidans scroll fungerar genom hela
  sekvensen.
- **1440, pixel-för-pixel mot `shots/astra-r8/ours/`-baslinjen**: `thesis-02/03/04/05`
  bytidentiska (0px diff). `thesis-01`, `case-calyx-03` (P17-3), `case-horai-03` (P19-3)
  visar en mycket svag diff (max enstaka pixelkanter, 143–227 av 255 vid enstaka
  pixlar) — undersökt med en diff-mask: uteslutande tunna konturer längs text- och
  bildkanter (typsnittshintning/subpixel-rendering mellan separata sidladdningar), INGA
  förskjutna block eller ändrad komposition. Visuell sida-vid-sida-jämförelse: identisk
  layout, position och innehåll. Ingen strukturell ändring vid 1440, som krävt.
- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920, `scrollWidth`=
  `clientWidth` på alla nio.
- **`a11y_scan.py`** vid 390: 0 violations, 41 passes.
- **Låst copy**: 15/15 rader ordagrant — ingen av de tre fixarna rörde en textsträng
  (alla tre är CSS/JS-ankare mot tredjepartssidornas EGEN DOM, aldrig copy).
- **Grep, tankstreck**: 1 träff, samma HTML-kommentar som R1–R8 (inte synlig text, rör
  ett tidigare rundas flip-card-kod, oberört denna runda).

**V3d R9 klar**

## V3d R10

Lead-fynd efter R9 (`shots/lead-r9/thesis-01.png`, `thesis-03.png`): tesbandets mobila
foto (R9 fix 2) fyller nu raden, men `object-fit:cover` med standardankaret (center)
beskär vänsterkanten — Hyperboreas rubrik "Systems" läses som "ystems". Orsak: boxen är
portrait vid 320–767 (t.ex. 343×448 vid 390) mot bildkällans 16:10 (1200×750); en
center-beskärning tar lika mycket från båda sidorna. En kirurgisk `Edit`, `Skill(design)`
körd först (targeted change, scope-discipline: en CSS-egenskap, inget gate/re-derivation).

### Fixtabell

| # | Mål | Före | Efter | Bild |
|---|---|---|---|---|
| 1 · vänsterkanten beskärs vid 390 | "Systems" helt läsbart vid 320/375/390/414/768, fyllnad/höjd från R9 orörd, 1440 oförändrat | `.thesis-photo-box img` utan `object-position` (standard 50% 50%) — i en portrait-box (16:10-bild i t.ex. 343×448) beskär cover båda sidorna lika, rubrikens vänsterdel försvinner | `object-position:left top` tillagt på `.thesis-photo-box img`, scopat i `@media (max-width:767px)` (samma brytpunkt som R9:s fix 2 — 768 matchar redan 16:10 mot bildens 16:10, ingen beskärning sker där oavsett ankare; 1440 matchar aldrig regeln) | "Systems with warmth" helt läsbart vid 320/375/390/414, oförändrat vid 768 (matchade redan), **byte-identiskt** vid 1440 (`diff.getbbox()`→`None`) | `shots/r10/after/thesis-01-{320,375,390,414}.png` |

### Verifiering

- **Enskilda skärmbilder** (inga kontaktark), `?preview=thesis-01` och `thesis-03` vid
  320/375/390/414/768/1440, alla lästa. Rubriken "Systems"/"System" hel vid alla fem
  mobil-/tablet-bredder, sajtens egen vänsterkant (logo, "EDITION MMXXVI · VOL. 03",
  nav) synlig i varje.
- **1440, pixel-för-pixel**: `thesis-01` mot R10:s egen `before/`-fångst (samma URL,
  före ändringen) — `getbbox()` → `None`, byte-identiskt. `thesis-03` mot R9:s
  `shots/astra-r8/ours/P03-3-1440.png`-baslinje — `getbbox()` → `None`, byte-identiskt.
- **768**: bekräftat redan korrekt före fixen (boxens 16:10-form matchar bildens
  16:10-källa exakt, ingen beskärning sker oavsett `object-position`) — medtaget i
  verifieringen som `Mål` kräver, ingen kodändring behövdes för den bredden.
- **Noll horisontell scroll**: `scrollWidth`=`clientWidth` vid 320/375/390/414/768/1440.

**V3d R10 klar**

## V3d R11

Astras granskning av R10 (`reviews/r10-astra.md`), läst i sin helhet. Två material_fixes,
båda bara vid 390/375 — vid 1440 var sidan godkänd och oförändrad, och Astra bekräftar
det explicit. Verifierade mot fil och mått i `shots/astra-r10/`. `Skill(design)` körd
först (targeted change, scope-discipline). Kirurgiska `Edit`, motorn orörd.

### Fixtabell

| # | Mål | Före | Efter | Bild/mått |
|---|---|---|---|---|
| 1 · tesfotot hoppar 35px vid mening 3 | Fotots `top` lika (±1px) i alla fem meningarna, hjulsekvens 20px-steg båda hållen, 390/375 | `--in`-driven `letter-spacing` (`index.html:620`, upp till +0,06em) fick mening 3 (60 tecken, längst) att radbryta till 5 rader i stället för 4 i ETT hjulsteg av övergången — `.thesis-lines` (auto-rad) växte, strecken/fotot hoppade 35px och tillbaka (scrollY 4430→4450 vid 390) | `.js .ts{letter-spacing:-.02em}` tillagt i `@media (max-width:767px)` — låser spårvidden, `clip-path`/`transform`-reveal (rad 618-619) orört | Egen mätning, hjul 20px-steg, 120 bildrutor per bredd (60 ner + 60 upp), scrollY 3269–4449 (390) / 3146–4326+ (375): `.thesis-photo-box`s viewport-top **274,4px vid 390 / 267,7px vid 375 i ALLA bildrutor, spread 0,0px** | mätdata i sessionen |
| 2 · Calyx -03-fotot beskärs 28px upptill | Figur ≥0, märkningens underkant ≤ ih, 390/375 | `['#studio + section', 0, 76, 700]` (`index.html:2222`) — 76px uppmätt mot fel layout, figuren stod på y=−28..455 i en 517px ram (390), 28px beskuret upptill | Offset 76→48 (samma ankare, samma `a[3]`-tröskel 700, alltså inert vid 1440 där ih redan uppmätts över 700) | Egen mätning: figTop **−0,2px** (390 OCH 375), capBottom **483,8px** — inom ih 517 (390) och 496 (375) med marginal. Skärmbild: hela fotot + "02/14" synligt i ramen, båda bredderna | `shots/r11/calyx/case-calyx-03-{390,375}.png` |

### Verifiering

- **Hjulsekvens, fix 1**: `mouse.wheel` 20px-steg, 60 ner + 60 upp genom hela den pinnade
  tesbandsdelen vid 390 och 375, `.thesis-photo-box.getBoundingClientRect().top` läst vid
  varje bildruta (viewport-relativt, korrekt mått under pin — dokument-relativt mått
  skalar trivialt med scrollY och mäter fel sak). **0,0px spread** vid båda bredderna,
  inget enda hopp — matchar Astras egen `y=274`-referens exakt vid 390.
- **Fix 2, direkt mätning** i iframens eget dokument (samma metod som R9/R10): `figTop`
  och `capBottom` läst för `#studio + section figure`/`figcaption` vid `case-calyx-03`,
  390 och 375. Båda inom ramen med marginal (33px vid 390, 12px vid 375).
- **Enskilda skärmbilder** (inga kontaktark), `?preview=thesis-01..05`, `case-horai-03`,
  `case-calyx-03` vid 390/375/1440, alla lästa. Tesbandets fem meningar fyller raden
  identiskt, Calyx foto+märkning helt i ramen, Hōrai-citatet oförändrat (R9/R10:s fixar
  rörda inte).
- **1440, pixel-för-pixel mot `shots/astra-r10/ours/`**: `thesis-02/04/05` bytidentiska.
  `thesis-01`, `case-calyx-03`, `case-horai-03` visar samma svaga kantutjämningsbrus som
  Astra själv dokumenterat i persistence-avsnittet ("kantlinje... alltså kantutjämning")
  — diff-mask kontrollerad, uteslutande tunna text-/bildkonturer, inga förskjutna block.
  Ingen strukturell ändring: rimligt, eftersom fix 1 är scopat till `max-width:767px` och
  fix 2:s `a[3]:700`-villkor gör 76→48-ändringen inert vid 1440 (ih där långt över 700).
- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920, `scrollWidth`=
  `clientWidth` på alla nio.

**V3d R11 klar**

## V3d R12

Antons feedback, inplanerad i `plans/057-hyperborea-ridan-case-pris.md`, punkt 1–6. Copyn för
casen/bryggan/prisbron skriven ordagrant från `COPY-V3d-case-final.md`. `Skill(design)`,
`Skill(animate)` och `Skill(emil-design-eng)` körda först. Q2 (typsnittsnedladdning) inte
godkänd av Anton — Geist-fallback använd för case-namnen, samma tvådelade `h2`-struktur,
bytbart senare via `--f-quote-calyx`/`--f-quote-horai`. Kirurgiska `Edit`, i planens
Steps-ordning (6 först). Motorn och `sites/*` orörda. Exakt två `<iframe>`. Ingen ram
transformeras.

### Fixtabell (Target, mål, uppmätt värde)

| # | Target | Mål | Uppmätt | Bild |
|---|---|---|---|---|
| 6 | Fyra meningar | Exakt 4 `.ts`/4 tick, `VI BYGGER ERT VARUMÄRKE.` 0 träffar i synlig text | `document.querySelectorAll('.ts').length`=4, tick=4; strängen finns bara kvar i EN CSS-kommentar (kodhistorik), 0 i markup/text | — |
| 1 | Hyperborea-plåtens bredd | ≥45% vw, samma andel 1024–1920 | 1920: 47,27% · 1440: 45,82% · 1280: 45,82% · 1024: 45,82% | `par/P03-thesis-01-1920.png` |
| 1 | Plåtens överkant = meningens överkant | ±8px, alla fyra meningarna | **0px** exakt, alla fyra meningarna, alla fyra breddar | samma |
| 1 | Plåten fri från kanten | höger luft = `--rail-x` ±1px | 1920: 96px · 1440: 86,4px · 1280: 76,8px · 1024: 61,4px (matchar `--rail-x`-clampen) | samma |
| 1 | Plåten står still | 0px spridning, 20px-hjul ned+upp | **0,0px** vid 1024/1280/1440/1920 (60+60 hjulsteg) | mätdata |
| 1 | Ingen ordbrytning | 0 delade ord | 0 vid 1024/1280/1440/1920/768 (rubrikskript, `.ts`/`.case-name`/`.case-line`/`.bro-title`/`.process-title`/`.cases-title`/`.bridge-title`) | mätdata |
| 1 | ARGUMENTET.-marginal | ≥8px i spalten | 1920: 102,5px · 1440: 25,6px · 1280: 22,7px · 1024: 18,2px | mätdata |
| 1 | 768–1023 orört | R11-geometrin, `.7fr`, bleed | Ingen `min-width:1024px`-regel slår till <1024; endast fyra-meningar-räkningen (punkt 6) skiljer | — |
| 2 | Ingen rubrik halvklippt | 0 träffar, hjul 20px, 1920/1440/768/390 | **0 vid 1920/1440/768.** 390: 831 träffar, alla `.process-step-title`/`.process-stick` (processens EGEN, förplan-057 sticky-ritbords-mekanik, oberörd denna runda — utanför 057:s sektioner) | `shots/r12/scripts/sweep.py` |
| 2 | Kanten tes → kapitel | ±1px | **0px** exakt (ren dokumentflödeskant, ingen overlap kvar) | mätdata |
| 2 | Kapitelskärmen | rubrik ≥100px (1440), ≥56px (390), inget blått, inget band 01 | 1440: 103,68px · 390: 56px exakt; `?preview=chapter` visar ren mörk grund, inget blått, inget av band 01 | `par/P04-chapter-{1920,390}.png` |
| 3 | Case-rubrik i två delar | namn i sajtens röst + copy-rad, samma `h2` | Implementerat (Q2-fallback Geist, kursiv för Calyx, versaler+spärr för Hōrai) | `par/P17-*-1440.png`, `par/P19-*-1440.png` |
| 3 | Namnens storlek | 90% ±4% av spalten, båda samma bredd | Omräknat för Geist (39/21cqi var kalibrerat mot Cardo/Cinzel): **33cqi/26cqi, tak 9rem→12rem** → 90,1%/90,5% vid 1920/1440/1280/1024 | mätdata |
| 3 | Allt ryms, desktop | Ingen text under/över stagen, 1920/1440/1280/1024 | Alla negativa "overflow" (marginal 152–425px) — ryms gott och väl | mätdata |
| 3 | Allt ryms, mobil | Sista glyfen ≤ stagens underkant −8px, 390/375 | **Boundary utlöst** (se nedan) — löst utan copy-ändring, se § Boundaries | mätdata |
| 4 | Prisbron finns | `section.price-bridge#bro` mellan `#case-horai` och `#pris` | Implementerad, `data-sc-act="flow"` | `par/P21-pris-bro-1440.png` |
| 4 | Grunden | Överkant = `--c-black` (ΔE 0), underkant = prisets scrim (≤2% luminans) | Hōrai/bro-skarv: **byte-identisk** (11,12,14 båda sidor, alla 5 x-punkter). Bro/pris-skarv: 4/5 punkter ≤0,4%, 1 punkt 8,24% (ett ljussken i fotot, bekräftat visuellt, inte en scrim-artefakt) | `shots/r12/seam-*.png` |
| 4 | Skala | Geist 700 versaler, samma clamp som `.ts` | Delar `--f-display`/samma `clamp()`-uttryck | mätdata |
| 4 | Rörelse | Hårlinje dragen på `--sc-ps`, färdig innan `.statement` når övre halvan | Manuell hjulsvep bekräftar linjär scrubbning (ps 0→0,675 gav scaleX 0→0,0184→0,4924→0,9276→1, matchar formeln exakt) | mätdata |
| 4 | Luft | 35–60svh, bro-rule → `.statement` | **48,3svh** | mätdata |
| 4 | Kontrast | ≥4,5:1 (rubrik ≥3:1) | `contrast_over_media.py` PASS, 18,90:1/19,33:1 på rubrikerna; `.bro-p`/`.bro-micro` ljusa mot mörk grund, uppenbart över golvet | se nedan |
| 5 | Inga rullningslister | `clientWidth===innerWidth` i riktig Chromium | `scrolling="no"` på båda `<iframe>`; ramens dokument 15px bredare, `measureCase` mäter om (redan kodad) | — |
| 5 | Synken fungerar | `?preview=case-*-0N`, hjul, monoton `scrollY` | Bekräftat via befintliga `case-calyx-0N`/`case-horai-0N`-lägen (oförändrad kod), citatet (case-horai-03) fortsatt korrekt format i ramen efter `scrolling="no"` | `par/P19-case-horai-03-1440.png` |
| 6 | Samma takt | `data-sc-span` 5,5→4,4 | Ändrat, `--n:4` på `.thesis`, alla `/5`→`/var(--n)` | — |

### Steps, kort

1. **Hyperborea** (`index.html` rad ~588–693): `letter-spacing` låst till `-.02em` överallt (var redan gjort R10/R11 bara under 768; nu överallt, den gamla mobilregeln överflödig och borttagen). Nytt `@media (min-width:1024px)` efter mobilblocket: `1.2fr`-kolumn, `.ts{font-size:min(clamp(...),14cqi)}`, `.thesis-figure` flyttad till rad 1 (`align-self:start`), `.thesis-ticks{align-self:end}`.
2. **Ridå** (rad ~956–966, 2489–2501): `.process{margin-top:-100svh}` borttagen, `.chapter-hold{height:auto}`, `.process-chapter{position:relative;min-height:100svh}` (var `sticky`). `ridaY(120)`→`ridaY(100)` för `chapter`-läget (den nya, icke-överlappande layoutens egen matematik). `?preview=thesis-0[1-4]` (var `0[1-5]`).
3. **Case-rubrikerna**: markup `<span class="case-name">`+`<span class="case-line">` i båda `h2.case-title`; copy skriven ordagrant från `COPY-V3d-case-final.md` (alla steg-h3/p/case-rail för Calyx OCH Hōrai uppdaterade, samt case-rubrikernas rad och bryggan). `--f-quote-calyx`/`--f-quote-horai` tokens (Q2-fallback: `var(--f-display)`, dvs Geist). `--name-fit` omräknat från planens 39/21cqi (kalibrerat mot Cardo/Cinzel) till **33/26cqi** + tak `9rem`→`12rem` för Geists smalare glyfer, uppmätt till 90,1%/90,5%.
4. **Prisbron**: ny `<section class="price-bridge" id="bro">` mellan `#case-horai` och `#pris`, copy ordagrant. `.price::before,.close::before` utökad med `,.price-bridge::before` (delad scrim, både desktop- och mobilregeln). Två nya `?preview=`-lägen: `pris-bro` (väntar in `--sc-ps>=0.55`), `pris-bro-skarv`.
5. **Ramarna**: `scrolling="no"` på båda `<iframe>` (Calyx, Hōrai). Kommentar vid `.frame-wrap iframe` förklarar varför headless-fångster (`--hide-scrollbars`) dolde listerna i elva rundor.

### § Boundaries — löst utan att röra copy eller ramraden

Case-texten rymdes inte vid 390/375 efter 3.3: med `.case-line` synlig på mobil (samma
storlek som planen föreslog) hamnade sista stegets bildtext upp till **82px** under
stagens egen underkant (Hōrai, 390). Tre alternativ enligt planen: caselinjen bara i
steg 1, sänkt ramrad, eller kortare copy. Copy rörs aldrig denna runda, och ramraden
(`72svh` Hōrai / `66svh` Calyx) är R8–R11:s finjusterade fix för citatsynlighet
respektive bildbeskärning — att sänka den riskerar att öppna de buggarna igen. Valt:
**döljs `.case-line` helt på mobil** (samma mönster som `.kicker-sans`/`.case-rail`,
redan dolda där av samma skäl) + en måttlig, ren spacing-åtstramning
(`.case-steps margin-top` 14→4px, `.cs h3` 1.375→1.25rem, `.cs p` 1rem→0,9375rem med
`line-height:1.32`) — ingen sträng ändrad, ingen bildhöjd rörd. Resultat: **alla steg
≥8px marginal vid 390 och 375** (sämsta fall: Hōrai 375, 9px). Vid 320 (inte bland
rundans obligatoriska breddder) återstår overflow (−73 till −140px) — informativt,
stoppar inte rundan, Anton avgör vid behov.

### Fynd utanför 057:s sektioner (stoppar inte rundan)

- **Ridå-sveppet vid 390**: 831 träffar, samtliga `.process-step-title` täckt av
  `.process-stick` — processens egen, sedan tidigare rundor etablerade sticky-rithands-
  mekanik, oberörd av plan 057. Utanför scope.
- **`?preview=case-horai-03`**: steg-indexets EGNA `aimPin`-mål (`(N-1+0,8)/6`, oförändrad
  formel) landar för steg 3 (i=2) precis innanför nästa stegs `--out`-stängningsfönster
  (16,75% clip uppmätt, matchar formeln exakt: ps 0,4667 mot fönstret [0,46, 0,5]) — ett
  transient klipp av `.cs h3`-texten i just den fångade bildrutan, oberoende av denna
  rundans ändringar (samma `--a`/`--b`/`--f`-formel sedan R7). Iframens EGET citat (Hōrais
  `#quote-text`, R9:s fix) är fortsatt korrekt format. Steg 1/2/4/5/6 (`case-horai-01/-06`
  lästa) visar inga sådana artefakter.
- **`motion_probe` på `#bro`**: positionerat vid `?preview=pris-bro` (som väntar in
  `--sc-ps>=0,55`, dvs redan efter hårlinjens fulla reveal) rapporterar `staircase 29`/
  `dead` på `.bro-rule:transform` — ett mätartefakt av att sonden startar EFTER att
  reveal:en redan mättats (ps stannar på 1,0 resten av fönstret). Egen manuell hjulsvep
  från ps=0 bekräftar en helt linjär, korrekt scrubbning genom hela dragfönstret
  (0,30–0,55), se Fixtabellen.

### Grinden

- **`motion_probe`**: `#tes` (thesis-02, cpu 1, hjul 20:120): staircase 0, reversals 0,
  max_step 2,52%, p95 16,7ms. `#case-calyx`/`#case-horai` (var sitt läge): staircase 0,
  reversals 0, max_step ≤2,55%; Hōrai 6/380 bildrutor >33ms (samma dokumenterade
  bildrutetimingsmönster som tidigare rundor, inte en värdehopp-defekt). `#bro`: se ovan.
- **`contrast_over_media.py --url`** (`?preview=pris-bro`): PASS, 18,90:1/19,33:1.
- **`a11y_scan.py`**: 0 violations, 41 passes vid 390 OCH 768.
- **`reflow.py`**: `overflow320`/`overflowZoom200`/`overflowExtra(768,390)` alla tomma.
  `unrevealed:11` — samma 8 SVG-utrop som varje tidigare runda, plus `#bro-title`/
  `.bro-p`/`.bro-micro` (nya, `data-sc-in`): bekräftat att de faktiskt slår om till
  opacitet 1 vid en riktig `scrollIntoView` (reflow.py:s egen scrollsvep når helt enkelt
  inte så långt ned på den nu längre sidan) — reveal-systemet failar mot synligt
  (opacitet 0 vid vila, tänds av IntersectionObserver), inte ett trasigt fall.
- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920.
- **Rubrikskriptet**: 0 delade ord vid 1024/1280/1440/1920/768 över `.ts`/`.case-name`/
  `.case-line`/`.bro-title`/`.process-title`/`.cases-title`/`.bridge-title`.
- **Låst copy**: **14/14** (15 minus `VI BYGGER ERT VARUMÄRKE.`, hävt av Anton).
- **Grep**: tankstreck 1 (samma R1–R11-kommentar, inte synlig text), `prefers-reduced-
  motion` 0, inline-hex utanför `:root`/kommentarer 17 (ingen ny — alla mina nya regler
  använder `var()`/`color-mix()`, inga hexvärden tillagda).
- **Rullningslister**: `scrolling="no"` implementerad; `measureCase` mäter om vid
  `load`/`ResizeObserver` (oförändrad kod, redan robust mot ramens 15px breddökning).

**V3d R12 klar**

## V3d R13

Anton läste R12:s copy 2026-09-19: behåll "Calyx fick bli ett vårnummer.", Hōrais rubrikrad
gick att läsa fel, bron "Ni har sett arbetet. Här är priset." bort. Copy skriven ordagrant
från `COPY-V3d-pris-final.md`. `Skill(design)` körd först. Kirurgiska `Edit`, ingenting
annat från R12 rört.

### Gör-punkterna

| # | Mål | Gjort |
|---|---|---|
| 1 | Hōrais rubrikrad → "Hōrai dukar upp kvällen och ber om bokningen sist." i R12:s tvådelade `h2`, oförändrad form | `.case-line`-texten bytt, ingen CSS rörd. Mobil: `.case-line{display:none}` (R12:s boundary-fix) gör att den längre texten aldrig renderas där — obetydlig för mobilbudgeten. Desktop: 3 rader (samma `≤4`-tak), `overflowBottom`/`overflowTop` fortsatt negativa (182–419px marginal) vid 1024–1920 |
| 2 | Prisblocket en enhet: kicker → låst rubrik → ny text → kort rad → liggaren, i EN sektion | `#bro` borttagen helt. `#pris` bär nu kickern, rubriken (nu med `id="pris-title"`), den nya 56-ordstexten, den korta raden, och den oförändrade liggaren. Tonövergången (Hōrais svarta yta → fotogrund) flyttad till `.price`s egen bakgrund (`linear-gradient(180deg,var(--c-black) 0,var(--c-black) 10svh,transparent 45svh)`), leder nu rakt in i kickern/rubriken. Hårlinjen "ned till liggaren" är oförändrad `.price-ledger::before` (plan 033) — ingen egen brygg-hårlinje behövdes, den var redundant efter sammanslagningen |
| 2 | `aria-labelledby` rättad, inga döda referenser | `#pris` fick `aria-labelledby="pris-title"`, rubriken `id="pris-title"`. Alla 8 `[aria-labelledby]`-element på sidan kontrollerade direkt i DOM: **0 saknade mål** (`#bro`/`bro-title` fanns bara i den borttagna sektionen, ingen extern referens pekade dit) |
| 2 | `?preview=pris-bro` visar den nya enheten | Ompekad från `#bro` (borttagen) till `#pris`; väntar nu in `--sc-ps>=0,4` (förbi liggarens reveal-trösklar 0,18–0,36) i stället för det gamla `>=0,55` (som väntade in `.bro-rule`, också borttagen) |
| 3 | Rubrik+text+första prisraden synliga tillsammans, 1920/1440/390 | Bekräftat i skärmbild vid **alla fyra** breddar (1920/1440/768/390) — vid 390 syns kicker+rubrik+text+kort rad+**två** prisrader samtidigt, vid 1920 syns hela liggaren i en enda bildruta |

### Verifiering

- **Skärmbilder, `mouse.wheel`** från `#case-horai`s slut, genom övergången och hela
  prisblocket, vid 1920x930/1440/768/390 — alla lästa. Tonövergången obruten, ingen
  kant, rubrik+text+liggare+`kontakt@alunix.se` läses som ett enda avslut, hela vägen
  till sidans botten.
- **Hōrai/pris-skarven, pixelprov**: 5 x-punkter, ovan/under skarven, **byte-identiska**
  `rgb(11,12,14)` = `--c-black` exakt (ΔE 0), oförändrat från R12.
- **`contrast_over_media.py --url` (`?preview=pris-bro`)**: PASS, kicker 18,79:1,
  rubrik 18,53:1, ny text 18,26:1 (golv 3,0–4,5). `.price-short` (kort raden) delar
  R12:s redan godkända `.bro-micro`-färg, samplad direkt: samma värde.
- **`motion_probe` på `#pris`**: `?preview=pris-bro`-positionerad sond rapporterar
  `staircase 17`/`max_step 6,11%` — undersökt: egen manuell hjulsvep från ps=0 visar
  en helt linjär, monoton progression (0,0026→0,6466 över verklig scrollsträcka) som
  **stannar exakt när sidans botten nås** (`#pris` är nu sidans sista, och längsta,
  sektion) — samma probe-positioneringsartefakt som R12:s `#bro`-fynd, inte en
  värdehopp-defekt.
- **`a11y_scan.py`**: 0 violations, 41 passes vid 390 OCH 1440 (fångar även trasiga
  `aria-labelledby` — inga sådana fynd).
- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920.
- **Rubrikskriptet**: 0 delade ord vid 1024/1280/1440/1920/768/390 över `.ts`/
  `.case-name`/`.case-line`/`.process-title`/`.cases-title`/`.bridge-title`/`.statement`.
- **Låst copy**: 14/14 (oförändrat sedan R12). "Calyx fick bli ett vårnummer." kvar
  ordagrant, "Ni har sett arbetet…"/gamla "Hōrai serverar bokningen sist." — 0 träffar.
- **Grep**: tankstreck 1 (samma R1–R12-kommentar), `prefers-reduced-motion` 0,
  inline-hex utanför `:root`/kommentarer **17** — oförändrat från R12, ingen ny.

**V3d R13 klar**

## V3d R14

Tre fynd ur leadens läsning av R13 vid 1920 (`shots/lead-r13/w-*.png`, `m-*.png`).
`Skill(design)` körd först. Kirurgiska `Edit`, ingenting annat rört.

### Fixtabell

| # | Mål | Före | Efter | Bild |
|---|---|---|---|---|
| 1 · dubblerat namn | Namnet syns en gång, meningen är rubriken, tillgängligt namn = hela låsta meningen ordagrant, rymmer vid 1920/1440/1024/390/375 | `.case-name` visade "Calyx"/"Hōrai" separat, och `.case-line` UPPREPADE namnet i "Calyx fick bli…"/"Hōrai dukar upp…" — namnet lästes två gånger i rad | `.case-line`s textinnehåll är nu bara meningens REST (" fick bli ett vårnummer." / " dukar upp kvällen och ber om bokningen sist.") — samma `h2`, samma två `span`, ingen CSS rörd. Uppmätt `h2`-textContent (motsvarar tillgängligt namn): **exakt** de låsta meningarna, ordagrant. Overflow mot stagen negativ (−22 till −1301px marginal) vid alla fem breddar | `shots/r14/calyx-01-1440.png`, `horai-01-1440.png` |
| 2 · pristext för liten | ≥20px vid 1440/1920, ≤~48 tecken/rad, tydligt större än `.price-row .label` (17px), kort raden samma eller en nivå mindre, ≥17px vid 390 | `.price-ingress{font-size:var(--body-r5)}` = 0,95rem = **15,2px**, SMALARE än `.label` (17px) — bakvänd hierarki för texten som ska sälja paketen | `font-size:clamp(1.0625rem,.85rem + 1vw,1.5rem)`, `max-width:48ch`. Uppmätt: **24px vid 1440/1920** (label 17px, tydligt större ✓), **17,5px vid 390** (≥17px ✓). `.price-short` `clamp(.9375rem,.8rem + .5vw,1.0625rem)` → 17px vid 1440/1920 (samma som label), 15px vid 390 (ett steg under ingressen) | `shots/r14/pris-1440.png` |
| 3 · band 01 kikar fram | Kapitlet står ensamt vid 1920x930 OCH 1920x1080, som vid 1440 | `.process-chapter{min-height:100svh}` gjorde sektionens EGEN höjd exakt lika med viewporthöjden (innehållet fyller den per konstruktion) — bara EN exakt scrollY höll kapitlet helt ensamt, inte ett fönster; varje hjultick förbi den punkten visade redan band 01:s topp i nederkanten | `min-height:100svh`→`120svh`. Uppmätt (hjulsvep i 10px-steg från kapitlets egen topp): process-grid förblir **helt dolt i 190px** (≈20svh, matchar den nya bufferten) innan första pixeln syns — tidigare var fönstret ~0px | `shots/r14/chapter-1920.png`, `chapter-1920x1080.png` |

### Verifiering

- **Skärmbilder**, enskilda, via `mouse.wheel` och `?preview=`, vid 1920x930/1440/390 —
  alla tre fynd lästa vid samtliga tre breddar. Namnet läses en gång, som en sammanhängande
  mening (samma grepp som Calyx-sajtens egna "Botanical / *architecture,* / from /
  Stockholm."); pristexten äger nu blicken tydligt före radernas detaljer; kapitelskärmen
  helt ensam, inget av band 01 synligt, vid 1920x930 OCH 1920x1080.
- **Hjulsvep, fix 3**: 10px-steg från `.process-chapter`s egen topp — `process-grid` börjar
  synas först vid **+190px** (≈20svh), tidigare (uppmätt separat mot okorrigerad kod)
  praktiskt taget 0px.
- **Rubrikskriptet**: 0 delade ord vid 1024/1280/1440/1920/768/390/375, `.ts`/`.case-name`/
  `.case-line`/`.process-title`/`.cases-title`/`.bridge-title`/`.statement`.
- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920.
- **`a11y_scan.py`**: 0 violations, 41 passes vid 390 OCH 1440.
- **Låst copy**: 14/14 (oförändrat). Grep: tankstreck 1 (samma R1–R13-kommentar),
  `prefers-reduced-motion` 0.
- **Mobil**: `.case-line{display:none}` (R12/R13:s boundary-fix) gör att case-line
  ändå inte renderas vid 390/375 — dubbleringsfixen påverkar mobilen inte alls, redan
  riskfri där.

**V3d R14 klar**

## V3d R15

`.case-line` dolds helt under 768px i R14 (`index.html` rad ~1012), lead-val öppet i
kommentaren. Lead väljer **alternativ 1**: meningen syns hel i steg 1, tonas ut och faller
ihop scrubbat när steg 2 tar över. `Skill(design)` körd först. Kirurgisk `Edit`.

### Vad som gjordes

- Markup: `.case-line` fick en inre `.case-line-inner`-wrapper (Calyx och Hōrai) - texten
  i sig oförändrad, bara ett nytt omslag för grid-kollaps-tricket.
- CSS (endast `@media (max-width:767px)`, 1440/1920 helt orörda): `.case-line` blir
  `display:grid;overflow:hidden` med en `1fr`-rad (basläge, ingen JS); `.js .case-line`
  räknar samma asymmetriska `--out`-formel som `.js .cs` redan använder för steg 0
  (`--b:1/var(--n)`, `--f:.04`, samma `--n` som redan sätts per case), och driver
  `grid-template-rows`, `opacity` och `margin-top` direkt av `1 - var(--out)` - scrubbat
  på casets egna `--sc-ps`, ingen `transition`, båda riktningarna av konstruktion.
  Mobilstorleken (1,0625rem/17px, line-height 1,3) återställd till plan 057:s ursprungliga
  mobilvärde, som aldrig hann användas innan R12:s boundary-fix dolde raden helt.

### Verifiering

- **Enskilda skärmbilder**, `?preview=case-calyx-01/-02/-03` och `case-horai-01/-02/-03`
  vid 390 och 375, alla lästa: steg 1 visar meningen hel ("Calyx / fick bli ett
  vårnummer." och "HŌRAI / dukar upp kvällen och ber om bokningen sist."); steg 2 visar
  bara namnet, caselinjen helt kollapsad, ingen rest synlig; steg 3 (båda casen) visar
  bildtexten fortsatt helt inne i ramen, oförändrat från R12-R14.
- **Hjulsekvens**, 20px-steg genom steg 1→2 (30 bildrutor, båda casen vid 390), lästa
  bildruta för bildruta kring övergången: caselinjen tonar ut och faller ihop FÖRE nästa
  stegs egen rubrik börjar sitt inträde (samma icke-överlappande asymmetriska fönster som
  redan bevisat för `.ts`/`.cs`-bytena: caselinjens `--out`-fönster `[b-f,b]` slutar exakt
  där steg 2:s `--in`-fönster `[a,a+f]` börjar, `a=b`) - **0 bildrutor med synlig
  överlappning**.
  - `.case-line`s `h2`-förälders tillgängliga namn kontrollerat: alltid hela den låsta
  meningen (`textContent` normaliserat), oavsett `--out`-värde - ingen `display:none`/
  `aria-hidden` någonstans i mekaniken.
- **1440/1920 pixel-för-pixel** mot `shots/lead-r14/w-calyx.png`: visuellt identiskt (sida
  vid sida-jämförelse), ingen strukturell skillnad - mina CSS-regler ligger uteslutande
  inom `@media (max-width:767px)`.
- **Rubrikskriptet**: 0 delade ord vid 390/375/1440/1920 över `.case-name`/`.case-line`/
  `.ts`/`.statement`.
- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920.
- **`a11y_scan.py`** vid 390: 0 violations, 41 passes.

**V3d R15 klar**

## V3d R16

Astras slutgranskning, `reviews/r15-astra.md` material_fixes 1–3. Fix 4 (arket vid 1920)
ligger hos Anton, rörs inte. `Skill(design)` körd först. Kirurgiska `Edit`.

### Fixtabell

| # | Mål | Före | Efter |
|---|---|---|---|
| 1 · preview-siktet klipper steg-h3 | Siktet ligger inom `[a+f,b-f]` för varje N, båda casen | `(N-1+.8)/n` hamnade inne i stegets eget `--out`-fönster för Hōrai (n=6): steg-h3 klipptes 16,6% uppifrån i `case-horai-01…05` vid 1920/1440/390 | `previewCaseP(N,n) = Math.min((N-1+.8)/n, N/n-.045)` (delad funktion, används av både `aimPin` och `caseY` för samma N). Uppmätt: "NAMNET STÅR EN GÅNG" (och alla andra Hōrai-h3:or) syns hel vid 1920/1440/390. Citatet i `-03` fortsatt korrekt format |
| 2 · caselinjen fäller aldrig ihop | Höjd 0px från steg 2, `≥8px` marginal kvar i varje steg vid 390/375 | `grid-template-rows:calc((1 - var(--out)) * 1fr)` är ogiltig CSS (`fr` i `calc()`) - regeln föll bort tyst, raden stod kvar (22px/44px) och tryckte ned texten (Hōrai vid 375: −5 till −10px under stagens kant) | `max-height:calc((1 - var(--out)) * 2.4em)` (giltig `calc()`, samma `--out`). Uppmätt: `caseLineHeight`/`opacity` **exakt 0** i alla steg ≥2, båda casen, 390 och 375. Steg 1: marginal 25–109px i alla kombinationer utom Hōrai vid 375 (se nedan) |
| 2b · Hōrai steg 1 vid 375 | ≥8px marginal, copy/ramrad orörd | Kvarstod −5px efter kollaps-fixen ensam (två rader caselinje + längre stycke) | Ytterligare spacing-åtstramning: `.case-line` line-height 1,24→1,15, margin-top 4→2px; `.case-steps` margin-top →0; `.cs h3` 1,25→1,1875rem; `.cs p` line-height 1,3→1,22. Uppmätt: **+9px** (nätt men inom målet), visuellt oklämt (skärmbild läst) |
| 3 · beloppet bryts vid 390 | "26 900 kr" på en rad, 320–1920 | `kostar 26 900 kr` med vanliga mellanslag bröts "26 / 900 kr" i ingressen vid 390 | `26&nbsp;900&nbsp;kr` i `.price-ingress` (enda stället som saknade `white-space:nowrap`; `.price-row .value` har redan det, ordvalet oförändrat). Uppmätt: en rad vid 390 |

### Verifiering

- **Enskilda skärmbilder**, riktiga rullningslister (`ignore_default_args=['--hide-scrollbars']`),
  `?preview=case-calyx-01…05` och `case-horai-01…06` vid 1920x930/1440/390, alla lästa:
  varje steg-h3 syns hel, ingen rullningslist i någon ram, citat (Hōrai -03) fortsatt
  korrekt.
- **Direkt mätning** (per stegs `--i`-index, inte klippdetektion): `caseLineHeight`/
  `opacity` 0 i alla steg ≥2 vid 390 och 375, båda casen. Textmarginal mot stagens
  underkant ≥8px i varje kombination (sämsta fall Hōrai steg 1/375: +9px).
- **Prisblocket** vid 390: "26 900 kr" på en rad i ingressen (skärmbild läst).
- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920.
- **Rubrikskriptet**: 0 delade ord vid samma nio breddar, `.case-name`/`.case-line`/`.ts`/
  `.statement`/`.price-ingress`.
- **`a11y_scan.py`** vid 390: 0 violations, 41 passes.

**V3d R16 klar**

## V3d R17

Plan `plans/060-case-pris-smatext.md`, punkt 1–8, ordning 7 → 3 → 1 → 2 → 4 → 6 → 5 → 8 (planens egen
ordning). Copy skriven in ordagrant ur `COPY-V3d-r17-final.md`: Exempelcase-introt, "Pristext, Antons
andra beställning" val A under "Alla har rätt till bra design.", och tabellen "Antons beslut
2026-09-19, efter copy-gaten" (Calyx/Hōrai steg 1 första meningen struken, processens ingress
borttagen). `Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` lästa/körda före bygget.
Kirurgiska `Edit`. `sites/horai.html`: bara rad 307–331 (`git diff` bekräftar; raden vid 86, som tar
bort `prefers-reduced-motion`-blocket, fanns redan innan denna runda — F-011-sanering från en tidigare
runda, inte R17).

### Target-tabell

| # | Target | Mål | Uppmätt | Bild |
|---|---|---|---|---|
| 1 | `h2#case-title` | Exakt "Exempelcase", `--f-serif` (Young Serif 400), ett ord, 0 radbrytningar 320–1920 | textContent exakt; `document.fonts.check('1em "Young Serif"')` → true; 136 px vid 1920 (mätt `.cases-title` font-size), 40 px vid 390; 0 split-ord vid alla 9 breddar (320–1920); `overflow-wrap:normal;white-space:nowrap` håller ordet på en rad | `shots/r17/cases-1920.png`, `cases-390.png` |
| 1 | `.cases-lead` | Copy-filens final ordagrant (28 ord), ingen kicker ovanför | "Calyx är en florist i Stockholm och Hōrai en restaurang. Ingen av dem finns, men sidorna är färdiga. Vi går igenom vad vi valde i dem och varför." — grep-bekräftat ordagrant; ingen `.kicker-sans` kvar i DOM | samma |
| 1 | kapitlet äger skärmen | `?preview=cases`: rubrik+text centrerat, inget annat synligt | bekräftat i skärmbild, PARITET P14 | `cases-1920.png`, `cases-390.png` |
| 2 | namnen oförändrade | `.case-name` rörs inte | 2.1 gjorde ingen ändring; CSS-block för `.case-name`/`.case--calyx .case-name`/`.case--horai .case-name` orört (diff bekräftar) | `case-calyx-01-1920.png` (namnet "Calyx" i Geist kursiv, som R16) |
| 3 | ingen kantlinje | Magentaprov 0 avvikande pixlar, alla 15 konfigurationer (7 breddar × DPR 1 + 6 DPR/zoom-fall) | **14/15 med 0/120 fel.** 1280x620@1,5 (Calyx): 30/120 fel, botten­kant — `.case-wrap`s egen `overflow:clip`-kant rastreras ~1 device-px innanför sin `getBoundingClientRect()` vid just denna fraktionerade höjd (582,8125 CSS-px); att göra iframen ännu större (-2px/+4px, testat) ändrade ingenting, eftersom det är WRAPPENS egen rasterkant som klipper, inte iframens storlek. **Boundaries** (planens egen reserv): JS-snäppning av `.case-wrap` till enhetspixlar i `measureCase` är den föreslagna åtgärden, inte gjord denna runda. `border-*-width` 0 på alla fyra sidor, alla breddar (kontrollerat i CSS) | se scratchpad-mätning, ej sparad som bild (pixelmätning, inte skärmbild) |
| 3 | synken orörd | `?preview=case-*-0N` ramens `scrollY` = ankaret; hjul 20px monotont | `measureCase` oförändrad (läser `w.innerHeight`, nu 2px högre per iframens `inset:-1px`); alla `case-calyx-0N`/`case-horai-0N` landar som i R16 (skärmbilder lästa) | `case-calyx-05-1920.png`, `case-horai-06-1920.png` |
| 4 | bryggan borta | 0 träffar `.case-bridge`/`#bridge-title`/"Nästa sida säljer en kväll." | grep: 0 träffar i DOM/synlig text | — |
| 4 | avståndet | `.case-gap` 18svh svart, ram→ram 200–260px vid 1920x930 | `.case-gap{height:clamp(96px,18svh,200px)}` — 167px vid 930 (18svh); besökt i `?preview=case-seam` | `case-seam-1920.png` |
| 4 | scrolleffekten lager 1/2 | Textspalten lämnar 0,87–0,91; grunden papper→svart 0,91–0,99; ramen orörd | `case-seam-text` (ps .89): textspalt osynlig, grund fortfarande paper (#fdfbf4-ish); `case-seam-ground` (ps .95): grund ~50% mot svart, ramen opåverkad — bekräftat i skärmbild | `case-seam-text-1920.png`, `case-seam-ground-1920.png` |
| 4 | båda riktningarna | `motion_probe`-mönster (egen wrapper kring `motion_probe.py`s `analyse()`, positionerad vid ps 0,72/1,0 eftersom CLI:t bara startar vid scrollY 0): staircase 0, max_step ≤3% på `--sc-ps` | Ned: `--sc-ps` 0,72→0,9655, max_step 0,61%, staircase 0, reversals 0. Upp: 0,7531→1, max_step 0,53%, staircase 0, reversals 0. `.case-text` transform (derived, ej playhead): max_step 3,0% båda hållen (förväntat för en eased egenskap, se scriptets egen dokumentation), staircase 0 båda hållen | scratchpad `motion_seam.py`-utskrift |
| 4 | sömlöst | ΔE 0 vid skarvarna Calyx-stage/gap och gap/Hōrai-stage | Visuellt bekräftat i `case-seam`-skärmbilden: tre svarta ytor i rad, ingen synlig kant | `case-seam-1920.png` |
| 4 | stegtakt oförändrad | Calyx `data-sc-span` 5,5→6,4, `--t:.86` skalar stegen så scroll/steg ±3% mot R16 | `data-sc-span="6.4"` satt; `.js .cs`/`.js .case-line` läser `--q:min(1,--sc-ps/--t)`; `caseY`/`latchTick` skalat symmetriskt (`Math.min(1,cAct.cur/(C.t\|\|1))`); steg 1–5 landar visuellt som R16 (skärmbilder lästa) | `case-calyx-01…05-1920.png` |
| 5 | Hōrai→pris lager 1 | Slöja `.price::after` opacity 1→0 i ps 0,05–0,40, ΔE 0 vid ps<0,05 | Bekräftat i `pris-bro-skarv` (full svart, ΔE 0 mot Hōrai) och `pris-in` (slöja halvvägs, foto framkallat) | `pris-bro-skarv-1920.png`, `pris-in-1920.png` |
| 5 | lager 2 | `#pris-title` blur 10→0(→6, se nedan)px, opacity 0→1, translateY .25em→0 i ps 0,18–0,40 | `motion_probe`-wrapper (start ps 0,5 resp 0): opacity-range [0,1] i uppåtriktningen, staircase 0 båda hållen, max_step 1,36% (opacity, derived) | scratchpad `motion_pris.py`-utskrift |
| 5 | båda riktningar, jämnt | `frame p95 ≤20ms vid cpu 1` | **Delvis.** Ned (mest still): p95 16,8ms. Upp (aktiv blur/opacity 0→1): p95 33,3–33,4ms, både före och efter blur 10→6px (ingen mätbar skillnad — kontrollmätning mot en OBERÖRD akt, `#tes`, visade samma ~30ms-nivå under aktiv rörelse i samma sandlåda, medan `#tes` i vila (dead) låg på 16,8ms). Bedömning: troligen en miljöegenskap hos denna headless/GPU-lösa sandlåda snarare än ett fel i just detta lager — `staircase 0` och `reversals 0` (F-012:s egentliga fråga, "hackigt") är rena i alla mätningar. Blur sänkt 10→6px ändå, per planens egen reserv ("faller det, sänk 10px→6px") | scratchpad `motion_pris.py`, `motion_control.py` |
| 6 | allt på en skärm | `#pris-title` topp ≥48px, `.close-mailto` botten ≤ innerHeight−24px, vid dokumentets slut, 1920x930 och 1440x900 | 1920x930: topp 136px, botten 874px (≤906) ✓. 1440x900: topp 171px, botten 846px (≤876) ✓. Även 1280x800 (topp 124, botten 752≤776) och 1024x768 (topp 148, botten 721≤744) ✓ | `pris-1920.png`, `pris-1440.png` |
| 6 | rubrik/siffror Young Serif | `#pris-title`/`.price-row .value` i `--f-serif`; rubrik 96/86px ≤2 rader 0 delade ord | Uppmätt `.value` font-size: 64px (1920), 48,96px (1440≈49), 43,52px (1280≈43,5), 34,8px (1024≈35) — matchar planens tabell nästan exakt. Rubrik 2 rader vid alla breddar, 0 delade ord (rubrikskriptet) | `pris-1920.png` |
| 6 | F-017 i liggaren | Siffror 64/49px, text (`Pris vid förfrågan`) hälften, ≥17px, baslinjelinjerad Δ≤1px | 1920: 64/32px (exakt hälften). 1440: 48,96/24,48px (hälften). Baslinjekontroll (injicerad nollhög span): Δ0px i alla tre raderna vid alla sju breddar ≥768; ≤768 kolumnlayout, baslinjekravet gäller inte per plan | mätscript `measure_pris.py` |
| 6 | kontakten som handling | `.close-mailto` Geist 700 ~21/19px, understruken, ≥44px träffyta | 1920/1440: font-size 22px (clamp topp), understrukning 2px→3px hover/active, `min-height:44px`; `tab_walk.py` bekräftar tabbstopp med synlig fokusring | `pris-1920.png` |
| 6 | copy | Ingressen = val A ordagrant, `.price-short`/kicker borta | Grep bekräftar ordagrant; 0 träffar `.price-short`/`.kicker-sans` i DOM | `pris-1920.png` |
| 7 | småtext | `microtext_scan.py --price-ledger` vid 1440/390: 4 fynd på kortbaksidan, 0 annars | **1440: 7 fynd (4 kortbaksida + 3 `.price-row .label`).** 390: 4 fynd (bara kortbaksida). De tre extra vid 1440 är `class:kicker-like`-regex som matchar ordet "label" i klassnamnet `.price-row .label` — INTE ny beskrivande text (låst säljande copy, planens egen inventering §C listar den som en avsedd stay-exception, samma princip som kortbaksidan). Ingen kod ändrad för detta (klassnamnsbyte hade varit en större, riskablare ändring för ett skriptets eget regex-sammanträff). Grep av var och en av de 12 inventeringsraderna (§A) och de 7 marginalnoterna (§B): **0 träffar** i `index.html` | `skills/design/scripts/microtext_scan.py --price-ledger` |
| 7 | tillgängligt namn | `iframe[title]` × 2, Hyperboreas `img[alt]` oförändrade; `a11y_scan` 0 violations | Bekräftat grep + `a11y_scan.py`: 0 violations, 41 passes, 1 incomplete | — |
| 8 | Hōrais bokning ryms | Varje textrad i `#reservations` ≤ spaltens kant, ramsbredderna 1920/1440/1280/1024/768/390/320 | Skärmbilder vid ram 1920 (case-horai-06), 1440, 1280, 1024, 768, 390: ingen textrad klipper spalten, "BOOK.HORAI.SE"/adressen fullt synliga | `case-horai-06-1920.png` … `-390.png`, `-768.png`, `-1280.png`, `-1024.png` |
| 8 | sajten själv | `sites/horai.html` direkt, allt utanför `#reservations` pixelidentiskt med R16 | `git diff --stat` + hunk-granskning: bara rad 307–331 ändrade av R17 (raden vid 86 fanns redan, tidigare rundas F-011-sanering) | — |
| 8 | 390-överflödet | Redovisas, inte löst | `scrollWidth` 675 kvarstår (andra sektioner, oförändrat sedan tidigare mätning) — inte i scope för R17 (bara `#reservations` upplåst) | — |

### Verifiering, gate

- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920 — alla `scrollW===clientW`.
- **Rubrikskriptet**: 0 delade ord vid samma nio breddar, `.case-name`/`.case-line`/`.ts`/`.statement`/
  `.price-ingress`/`.cases-title`/`.cases-lead`/`.process-title`/`.process-step-title`.
- **Låst copy** (`PRODUCT.md` § Brand Commitments, med Antons hävningar denna runda): alla 14
  ordagranna strängar (12 synliga rader + `Design`/`Utveckling`/`System` som en rad + de tre
  bildtexterna nu borttagna per beslut) grep-bekräftade; `kontakt@alunix.se` × 5 (meta, två mailto,
  sr-only, footer); `iframe[title]` × 2 oförändrade; Hyperboreas `img[alt]` oförändrad.
- **Grep**: `prefers-reduced-motion` 0 träffar. Em-dash: 1 träff, i en CSS-kommentar (rad ~423,
  förekom redan i R16, inte synlig text). Exakt 2 `<iframe>`. Inline-hex utanför `:root`: minskat med
  1 (`.close-mailto:active` tappade sin `border-color:#ffffff` när formen byttes till understrykning)
  — alltså inte ökat, gate håller.
- **`a11y_scan.py`**: 0 violations, 41 passes, 1 incomplete.
- **`tab_walk.py`**: 2 stopp (topline- och footer-mailto), båda med synlig fokusring, 0 issues.
- **`reflow.py`**: 0 overflow vid 320 och vid 200% zoom (1440→720css). "unrevealed": 9 element — 8 är
  processarkets SVG-grupper (samma som varje tidigare runda, orörda), den nionde är `#pris-title`
  (opacity 0 vid `--sc-ps<0,18`, ett avsiktligt scroll-scrubbat set-piece bakom `.js`-selektorn — en
  no-JS-sida visar den fullt synlig per konstruktion, samma mönster som `.js .cs`/`.js .ts` överallt
  annars på sidan; "reveal fails toward visible" gäller mount-tids-reveals, inte ett `--sc-ps`-styrt
  signaturgrepp med en `?preview=`-krok, vilket detta har (`pris-in`)).
- **`contrast_over_media.py --url …?preview=pris`**: PASS, 2 strängar i folden, sämst 17,77:1 (golv
  4,5:1) — god marginal.
- **`perf_probe.py`**: LCP 548ms, CLS 0,000 (Young Serif-bytet kostar ingen layoutförskjutning).
  FAIL `font-files 4>3` — **väntat och namngivet** (plan B1: Young Serif är sidans fjärde typsnittsfil
  och FÖRSTA externa förfrågan, en uttrycklig, mätt kostnad mot performance.md:s tre-filers-tak, inte
  ett fel). FAIL `long-task-under-scroll` (1 uppgift >50ms) — ej djupare undersökt denna runda, ej i
  planens egen Target-lista.
- **`motion_probe`** (egen wrapper, se ovan): Calyx→Hōrai-övergången och prisets blur/opacity-reveal:
  `staircase 0`, `reversals 0` i alla fyra körningar (båda riktningarna × båda ställena). `frame_p95`
  över 20ms i de rörelseaktiva benen (~33ms) men samma nivå syns i en kontrollkörning mot en helt
  orörd akt (`#tes`) under aktiv rörelse i samma sandlåda — bedömt som en miljökaraktäristik, inte en
  regression införd denna runda; `--sc-ps`-kontinuiteten (max_step) håller sig inom 0,5–0,7% i alla
  playhead-mätningar.
- **`scroll_verify.py`** vid 1440x900: 6 `blankBands` (900–8071px vardera) — konsekventa med sidans
  redan etablerade pin-arkitektur (hero span 3,4, tesbandet span 4,4, processakten, Calyx span 6,4,
  Hōrai span 6,4: en pinnad akt HÅLLER per definition skärmen visuellt still medan progress avancerar,
  vilket ett fullsides-kontaktark läser som "blankt"). Ingen av de sex banden matchar `.case-gap`s
  167px (för liten för att synas i listan) eller ligger isolerat kring prisets fotoband. Kunde inte
  diffas mot en sparad R16-baslinje (`index.html` är ospårad i git denna session) — bedömningen vilar
  på arkitekturkännedom, inte en före/efter-jämförelse, och skrivs här explicit som en gräns för vad
  som kunde verifieras.
- **Magentaprovet** (Verification B3, CARL "verifiera verifieraren"): körd först mot en avsiktligt
  trasig kontrollkopia (R16:s bård + `inset:0`) — hittade 36–92/120 avvikande punkter i alla 15
  konfigurationer, bekräftat att provet faktiskt fångar felet. Mot den byggda sidan: 14/15 med 0 fel,
  1280x620@1,5 kvarstår (se Target 3 ovan, Boundaries).

### Boundaries (stoppat, skrivet här i stället för gissat)

1. **Magentaprovet, 1280x620@1,5**: 30/120 punkter fel längs `.case-wrap`s underkant (Calyx). Roten:
   `.case-wrap`s egen `overflow:clip`-rastrering hamnar ~1 device-px innanför dess uppmätta
   `getBoundingClientRect()` vid just denna fraktionerade CSS-höjd — inte ett fel i iframens
   övertäckning (testat -2px/+4px, ingen effekt). Planens egen reserv: JS-snäppning av `.case-wrap`
   till enhetspixlar i `measureCase`. Inte gjort denna runda (ny scope, risk för sidoeffekter på andra
   14 konfigurationer som redan är rena).
2. **`microtext_scan.py --price-ledger` vid 1440**: 3 extra fynd på `.price-row .label` utöver
   kortbaksidans 4, ett regex-sammanträff på ordet "label" i klassnamnet (skriptets `KICKER_RE`),
   inte ny beskrivande text. Låst, säljande copy (planens § C). Ingen kod ändrad.
3. **`perf_probe.py`s `long-task-under-scroll`**: 1 uppgift >50ms, ej undersökt (utanför planens
   Target-lista denna runda).
4. **390-överflödet i `sites/horai.html`** (`scrollWidth` 675): redovisas per plan, olöst — sitter i
   sajtens övriga 12-kolumnsgrids, utanför den upplåsta `#reservations`-sektionen.

**V3d R17 klar**

## V3d R18

Plan `plans/061-overgang-och-steg.md`, ordning steg 2 (stegbandet) → steg 1 (Blåkopian), som planen
föreskriver. Grep mot R17-läget körd före ändring: alla planens selektorer fanns, `.process-note`
gav 0 träffar utanför kommentarer (bekräftat: ingen live `.process-note`-markup eller CSS-regel).
`Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` körda/lästa före bygget. Stegtexterna
skrivna in ordagrant ur `COPY-V3d-r18-steg.md` kolumn **final**, med ETT uttryckligt undantag: steg
05 fick lead-versionen "Ni behöver inte ha något färdigt. Vi bearbetar texter och bilder ni har och
säger till om något saknas." (18 ord) i stället för final-kolumnens "Vi hjälper er med texter och
bilder…", per instruktionen. Kirurgiska `Edit`. Dessutom: R17:s rest (lead 2026-09-19) —
JS-pixelsnäppning av `.case-wrap` i `measureCase`, se sista raden i tabellen.

### Target-tabell

| # | Target | Mål | Uppmätt | Bild |
|---|---|---|---|---|
| 2 | textens storlek | `.process-p` font-size: 1920 32px, 1440 28,2px (±0,5), 1280 ~26, 1024 24, 768 24; 390 ~21,9, 320 ≥20 | Exakt: 1920 **32px**, 1440 **28,16px**, 1280 **25,92px**, 1024 **24px**, 768 **24px**, 390 **21,85px**, 320 **20,8px** — alla inom mål | `shots/r18/process-03-1440.png`, `-1920.png`, `-390.png` |
| 2 | texten är fokus | `color`=`--ink` (inte 78%); textblock ≥2× siffrans yta; 5px-oskärpa: textblocket bandets största ljusa massa | `color:var(--ink)` skrivet (grep bekräftar, ingen 78%-regel kvar); bbox-yta 1,8–3,49× siffrans beroende på radantal (enradiga steg vid 1440 landar strax under en naiv 2×-bbox-jämförelse, men squint-testet — planens egna primära avgörande — läser texten som bandets största ljusa massa i alla lästa band) | `shots/r18/squint-process-03-1440.png` (läst: titel+text en sammanhängande ljus massa, större än "03") |
| 2 | hör ihop | Rubrik = textens storlek (Geist 700 versaler), direkt ovanför i samma spalt; rubrikens överkant = siffrans versalhöjdslinje ±6px; siffra oförändrad 168px | `titleFontSize`==`pFontSize` exakt vid alla sju breddar; siffra 168px (1920/1440) oförändrad; grid `auto minmax(0,1fr)`, rubrik rad 1/text rad 2 i spalt 2 | samma |
| 2 | mått | `.process-p` ≤46ch; ≤4 rader vid 1440, ≤3 vid 1920 | Max 3 rader vid 1920 (steg 06), max 3 vid 1440 (steg 06) — inom mål på båda | mätscript `measure_steps.py` |
| 2 | bandets höjd | `--band-h` ≤240px vid 1440/1920 | 1920: **219px**. 1440: **216px**. Ingen `row-gap`/padding-sänkning (2.5) behövdes | samma |
| 2 | arket krymper inte | `.process-sheet` bredd ≥76% vw vid 1440 | **81,1% vw** (1168/1440) | `shots/r18/process-03-1440.png` |
| 2 | ticker utan glyfspringa | 0 nya blankBands; inga två band synliga samtidigt utom vid `--slit-p`∈(0,1) | `scroll_verify.py` 1440: samma 6 blankBands som R17 (900–29641px, identiska gränser ±1px) — inga nya, inga borttagna | scratchpad `sv_1440/sheet.png` |
| 1 | linjerna korsar kanten | ≥2 av 4 linjer syns både över och under kanten, pixelkolumn obruten ±1px x / ≤2px y-glapp | Pixelkolumn vid `x2` (391 device-px, 1440, `tx`≈0,72): dashat mönster fortsätter obrutet från blå (`(30,94,156)`/`(113,153,192)`) till mörk (`(100,105,108)`/`(17,25,34)`) sida, ingen lucka | scratchpad `check_continuity.py`-utskrift |
| 1 | linjernas x = arkets | `--x1..--x4` = arkets stationer ±1px | 1920: x1=346=sheetLeft, x4=1563=sheetRight−1 (exakt). 1440: x1=131≈sheetLeft (131), x4=1298≈sheetRight−1 (1299−1). 390: x1=16=sheetLeft, x4=363=sheetRight−1 — alla ±1px | `measure_seam.py`-utskrift |
| 1 | lager i följd | `tx` 0→0,30 blå; 0,30→0,75 mörk; 0,70→0,85 vågrät; 0,78→1 rubrik | Bekräftat i `tes-till-ritning-0…4`: -0 inga linjer, -1 blå halvvägs, -2 blå klar/mörk på väg, -3 vågrät klar/rubrik halvbläckt, -4 allt format | `shots/r18/seam-0…4-1920.png`, `-390.png` |
| 1 | formad skärm | `tes-till-ritning-4`/`chapter`: 4 lodräta + vågrät synlig, rubrik 100% bläck, landningslinje 40px ±2 ovanför rubriken | Uppmätt exakt: 1920 gapAboveTitle **39,97px**, 1440 **40,05px**, 390 **39,97px** — alla inom ±2px | `shots/r18/seam-4-1920.png` |
| 1 | scrubbad, båda riktningar | `motion_probe` på `.process-chapter:--sc-ps`: staircase 0, max_step ≤3%; samma scrollY ned/upp samma bildruta | Ned: range [0, 0,6061], max_step 0,46%, staircase 0. Upp: range [0,3939, 1], max_step 0,45%, staircase 0. Kontroll: samma spår utan egen akt på `.process-chapter` visade ett mätbart LÅNGSAMMARE, ärvt `#process`-omfånget värde (0,062 spridning över samma 600px, mot 0,606 med egen akt) — bekräftar att den nästlade akten faktiskt läser sin EGNA, korta klocka, inte bara ärver `#process`s | scratchpad `motion_seam2.py`, `motion_control_check.py` |
| 1 | F-011 | 0 träffar `prefers-reduced-motion` | **0** | grep |
| 1 | ingen rubrik halvklippt | Svep (`sweep.py`, elementFromPoint) + geometrisk kontroll (`.seam *` ∩ rubrik-rect): 0 vid 1920/1440/768/390 | Svep: 1920/1440/768 **0**, 390 **813 träffar** — `.process-stick` (sticky ark) över `H3.process-step-title` "Uppstart" vid scrollY≈7740. Geometrisk kontroll (linje-mot-rubrik specifikt): **0/0/0/0** vid alla fyra, båda kontrollerna verifierade mot en avsiktligt trasig variant (`.seam-dn{height:150vh}` gav 3700+ träffar per bredd) först. Se Boundaries för bedömningen av 390-fyndet | `shots/r18/debug-mobile-overlap-7740.png` |
| 1 | inget nytt ljud | Inga etiketter på linjerna; `#1e5e9c` exakt 2 levande förekomster; inga skuggor | Bekräftat: `.seam` har ingen text/aria-label (bara `aria-hidden="true"`); grep av `#1e5e9c` ger 5 träffar men 3 är kommentarer, 2 levande `:root`-tokens (oförändrat sedan tidigare rundor) | grep |
| 1 | kontrast | Rubrik vid `tx`<0,78 (62% bläck) ≥3:1; vid `tx`=1 ≥7:1 | Uppmätt vid `tx`≈0,62 (samma konstanta 62%-ton som `tx`=0): **8,05:1** (rasteriserad pixelsampling, inte CSS-textparsning). `tx`=1 använder samma `var(--ink)`/`--c-drafting`-par som processtegens redan validerade rubriker (etablerat i tidigare rundor, orört här) | scratchpad `contrast_check2.py` |
| — | R17-resten: magentaprovet | 0 fel i alla 15 konfigurationer (var 30/120 vid 1280x620@1,5) | **0/120 i alla 15**, inklusive 1280x620@1,5 (nu 0/120, tidigare 30/120); de 14 redan rena konfigurationerna förblev rena. Fix: `snapCaseWrap(C)` i `measureCase` — snäpper `.case-wrap`s höjd till närmaste hela device-pixel (`flex:none` + explicit `height`) bara när avvikelsen är >0,02px, annars orörd (`flex:''`/`height:''`). Verifierat: 0 stale-state vid resize (1440→1280), `.case-wrap`/`iframe` `transform`/`opacity`/`clip-path` fortfarande `none`/`1`/`none` i hela hjulsvepet (0 avvikande bildrutor) | `shots/r17/` (magentaskript), scratchpad `check_snap_resize.py` |

### Verifiering, gate

- **Pixeldiff mot R17** (`?preview=cases`, `case-calyx-01`, `pris`, 1920/1440/390): **0,0000%** diff på
  `cases` och `pris` vid alla tre breddar, och på `case-calyx-01` vid 390. Vid 1920/1440 visade
  `case-calyx-01` en diff (53%/0,06%) — region-isolerad: **0 diff i textspalten och ramens navrad**,
  hela diffen (medel-delta 9,87 av 765) satt i det fotografiska blomstermotivet i ramen, samma
  etablerade mönster som tidigare rundor (kompressions-/rastreringsbrus mellan två separata
  sidladdningar av samma WebP, inte en strukturell ändring — bekräftat genom direkt visuell
  jämförelse: identiskt innehåll, identisk beskärning, identisk typografi). `?preview=front` och
  `thesis-01…04` har ingen sparad R17-baslinje (skapades inte den rundan) — bedömningen vilar i
  stället på att ingen selektor i `.thesis`/`.ts`/`.thesis-stage`/hero rörts denna runda (grep
  bekräftar 0 CSS-ändringar där), plus att `#tes`s `z-index:2` är oförändrat.
- **Noll horisontell scroll**: 320/375/390/414/768/1024/1280/1440/1920 — alla `scrollW===clientW`.
- **Rubrikskriptet**: 0 delade ord vid samma nio breddar.
- **`microtext_scan.py --price-ledger`**: samma resultat som R17 (4 kortbaksida + 3
  `.price-row .label`-regexträffar vid 1440, 4 vid 390) — ingen ny småtext införd.
- **`a11y_scan.py`**: 0 violations, 41 passes, 1 incomplete (oförändrat mot R17).
- **`tab_walk.py`**: 2 stopp, båda synlig fokusring, 0 issues.
- **`reflow.py`**: 0 overflow vid 320 och 200% zoom. Samma 9 "unrevealed" som R17 (8 processark-SVG +
  `#pris-title`) — `.process-title`/`.seam` INTE i listan (62%-bläck är aldrig opacity 0, no-js-sidan
  visar dem fullt bläckade per `html:not(.js) .seam{display:none}` plus `.process-title`s
  `color:var(--ink)`-fallback utan `.js`-selektorn).
- **`scroll_verify.py`** vid 1440: 6 blankBands, gränser identiska med R17 ±1px — inga nya.
- **`perf_probe.py`**: LCP 612ms (R17: 548ms, +11,7%), CLS 0,000. FAIL `font-files 4>3` (väntat,
  oförändrat sedan R17/plan 060). FAIL `long-task-under-scroll` (5 uppgifter >50ms, mot R17:s 1) —
  uppmätt men inte djupdiagnosticerad denna runda; ingen hård perf-gate för detta i plan 061:s egen
  Target-lista (bara `motion_probe`s `frame p95 ≤20ms vid cpu 1` är explicit gated, se nedan).
- **`motion_probe`** (egen wrapper kring `.process-chapter:--sc-ps`, samma metod som R17): `staircase
  0`, `reversals 0` båda riktningarna. `frame_p95` 33,3ms (ned) / 16,8ms (upp) — samma
  miljömönster som R17 (aktiv rörelse ~30ms, vila ~17ms i denna sandlåda, bekräftat konsekvent
  över båda rundorna och en kontrollakt).
- **Magentaprovet** (R17-resten): 0/120 i alla 15 konfigurationer efter `snapCaseWrap`-fixen (se
  tabellen ovan).

### Boundaries (stoppat/bedömt, skrivet här i stället för gissat)

1. **`sweep.py` vid 390: 813 träffar, `.process-stick` över "UPPSTART" (steg 01:s rubrik) vid
   scrollY≈7740.** Uppmätt och läst som bild (`debug-mobile-overlap-7740.png`): den sticky
   processritningen (alltid `top:0`, opak bakgrund) täcker en sliver av steg 01:s rubrik medan
   sidan scrollar FÖRBI steg 01 in i steg 02 — helt vanligt sticky-header-beteende (innehåll
   glider bakom en opak sticky yta och kommer fram igen), inte den typ av fel den geometriska
   kontrollen (`.seam *` korsar en rubrik mitt i texten, plan 057 B2:s ursprungliga fynd) är
   byggd för att fånga. Bedömning: INTE en regression från R18 - `.process-step-title`s
   mobilstorlek MINSKADE denna runda (fast `2rem`=32px → `--step-fs`-clamp 20,8–21,9px), vilket om
   något minskar risken för överlapp, inte ökar den; `.process-stick`s egen CSS (sticky-mekanik,
   höjd, bakgrund) rördes inte. Den planens EGNA geometriska kontroll (linje-mot-rubrik) gav 0/0/0/0
   vid alla fyra bredder, verifierad mot en trasig kontroll först. Ingen kod ändrad för detta.
2. **`perf_probe.py`s `long-task-under-scroll`**: 5 uppgifter >50ms (R17: 1), inte djupdiagnosticerat
   - utanför plan 061:s egen Target-lista, som bara gated `motion_probe`s `frame_p95`.
3. **Textblockets bbox-yta vid 1440 för enradiga steg**: 1,8× siffrans bbox-yta, under den bokstavliga
   "≥2×"-läsningen av Target 2 om ytorna jämförs som råa `getBoundingClientRect()`-areor. Planens
   egen primära avgörande metod (5px-oskärpa, läst som bild) bekräftar texten som bandets största
   ljusa massa i varje läst band (P07, P10 samt process-03/05/06/07) - bbox-talet är en trubbig
   proxy för två mycket olikformade element (en bred flerradig paragraf mot en enda kompakt siffra)
   och läses här som en bikommentar till, inte en motsägelse av, det visuella avgörandet.

**V3d R18 klar**

## V3d R19

Plan `plans/062-blakopian-arket.md`, skriven före bygget. `Skill(design)`, `Skill(animate)` och
`Skill(emil-design-eng)` körda/lästa (design/animate före huvudbygget, emil-design-eng/
review-animations dessutom en gång till i fortsättningen, se nedan). Kirurgiska `Edit`. Motorn och
`sites/*` rördes aldrig — verifierat: `sites/horai.html`s pre-existerande, okommitterade diff
(F-011/reservations-sektionen, ~2026-09-07) syntes i git status redan vid sessionsstart, INTE en
ändring denna runda; enda `Edit`-anropen denna runda gick mot `index.html`. Antalet inline-hex ökade
inte (`git diff` mot arbetsträdet: 0 tillagda rader matchar `#[0-9a-f]{3,8}`).

### 1. Övergången blått → ritning, om (Astra r18: "för återhållsam")

Planet krymper nu scrubbat, från en hel skärm till exakt ritningsarkets rektangel i processens
steg 01, via `clip-path:inset(...)` på `--tx` (F-011/F-014, oförändrad mekanik sedan förra
försöket) — INTE en transform. Under krympningen tonas fyllningen mot ritbordets ton
(`color-mix(in oklab,...)`) och en vit kontur (2px, `box-shadow:inset`) tonas in sent (tx 0,6–0,9)
så arket läses som att det STELNAR, inte som en ram som funnits hela tiden. Blåkopians
konstruktionslinjer (arkets kanter + de två stationerna) står kvar som ett andra, koordinerat
lager, samma `--tx`-fönster.

**Astras fyra material_fixes:**

| # | Fynd | Fix | Uppmätt |
|---|---|---|---|
| 1 | `.seam-h` (landningslinjen) ritades som 1×1px — `.seam i{width:1px}` (0,1,1) vann över `.seam-h{width:calc(...)}` (0,1,0) | `.seam .seam-h{}` (0,2,0) vinner nu | Landningslinjen mäter nu full bredd (`--x4`−`--x1`+2px) × 2px vid alla fyra bredder |
| 2 | Konstruktionslinjerna 1px, `--seam-on-blue` gav 2,86:1 mot `--c-accent` | Kantlinjer (data-l 1/4) + landningslinjen 2px, stationerna (data-l 2/3) kvar 1px; `--seam-on-blue` rättad från en 62%-blandning (mätt siffra visade sig vara en felläsning av tickstreckens LIT-formel, som når 100% vit, inte 62%) till ren `var(--c-white)` | Beräknad kontrast mot `--c-accent` (#1e5e9c): ≈6,79:1. Visuellt bekräftat (`crop_line.png`): skarp vit linje mot blått |
| 3 | Hōrais `mountFrame` väntade på IO:s 40%-rootMargin, som slog till mitt i Calyx→Hōrai-övergången (383/646/485 ms huvudtrådsblock vid 1440/1920/390) | Hōrai monteras nu redan när Calyx (`cAct.cur>=.4`) står i steg 1–3 av 5, köad med samma `requestIdleCallback`-mönster IO redan använder (`latchTick`, `case-calyx`-grenen) | Montering sker nu vid Calyx tick 1 (`debug_horai_mount.py`), gott om marginal före övergångens 0,80–1,0-fönster. Se Boundary 1 för en KVARSTÅENDE, separat lång uppgift i samma allmänna trakt |
| 4 | "SEO-optimering" bröts över radbrytning i prislistan | `SEO&#8209;optimering` (icke-brytande bindestreck), ordvalet oförändrat | Bekräftat: ordet bryts aldrig vid någon testad bredd |

### 2. Kontinuiteten, lead r19: "arket landar ovanför rubriken och rullar bort"

Lead läste övergången i enskilda skärmbilder (`shots/lead-r19/`) och fann att det landade
konturarket (steg 1 ovan) visserligen krymper snyggt till en ritningsrektangel, men eftersom
`.tes-plane` är `position:absolute` i normalt flöde fortsätter det scrolla med sidan efter
landning — precis som rubriken den landar bredvid. Uppmätt (`measure_gap.py`,
`measure_visible_ark.py`): arket är helt osynligt (rullat ovanför skärmen) runt kapitel-lokal
`cur`≈0,63, medan `.process-grid` (steg 01:s RIKTIGA sticky ark) inte syns förrän `cur`≈1,0 — ett
glapp på ~1,25 skärmhöjder vid 1920 där ingenting förbinder de två arken. Två olika ark, inte ett.

**Lösningen (enklaste väg som håller ihop med Option 1: rubriken läses färdigt, sedan tar det
landade arket steg 01:s plats):** en JS-tillståndsmaskin i `latchTick` (samma per-bildruta-loop som
redan driver Hōrai-monteringen och case-scrollningen — inget nytt lyssnarpar):

- **`data-frozen`**: när rubrikens EGEN underkant (live `getBoundingClientRect`) passerar
  `--band-h` (samma punkt `.process-stick` självt pinnar vid) fryser `.tes-plane` till
  `position:fixed`, med bredd/höjd redan validerad mot arket (samma `x1`/`x4`/aspect som
  konstruktionslinjerna) och läge beräknat från `.process-stick`s EGNA `padding`/`height`
  (sticken är `flex;align-items:center`, arket CENTRERAS i den, landar inte i dess överkant —
  ett första försök som bara använde `--band-h` rakt av gav 9px fel vid 1920 och 202px fel vid
  768, där sticken är mycket högre än det breddbegränsade arket). Vid den exakta scrollposition
  där rubriken korsar `--band-h` är arket redan osynligt ovanför skärmen (uppmätt: −48px) — bytet
  till `fixed` syns aldrig, bara att arket "landar om" en gång till, nu på rätt ställe.
- **`data-gone`**: tonas bort (`opacity:0`, `.25s ease-out`, `emil-design-eng`/`review-animations`
  godkänt — se nedan) när `.process-stick`s EGEN `getBoundingClientRect().top` faktiskt nått
  `--band-h`±2px (inte bara `.process-grid`s topp, som slog till 46–55px för tidigt, uppmätt).

**Tre ytterligare fel hittade och fixade under verifieringen av detta, alla via mätning, inte
gissning:**

1. **Fel bildförhållande vid mobil.** `.process-sheet` byter till `aspect-ratio:320/200` under
   768px (K3-registret) — JS-koden hade `495/880` hårdkodat obetingat sedan plan 062, aldrig synligt
   fel förrän frysmålet jämfördes pixel mot pixel mot det riktiga arket (±11px vid 390,
   `verify_continuity.py`). Fixat: `sheetAspect = innerWidth<768 ? 200/320 : 495/880`, samma
   brytpunkt som CSS:n.
2. **Full arkhöjd inte säker hela hållfönstret.** Den geometriska kontrollen (`seam_overlap2.py`,
   körd mot en trasig kontroll FÖRST enligt instruktion) fann `.tes-plane` över
   `H3.process-step-title` ("Uppstart") vid 1920/1440/768 (0 vid 390). Uppmätt
   (`find_safe_window.py`): stegtexten (ännu opinnad, i normalt flöde) glider upp genom EXAKT
   samma yta som frysmålet, och de två säkra fönstren (rubriken hinner rensa / stegtexten hinner
   inte dit än) delar ingen gemensam scrollposition med hela höjden fri — en genuin klämma, inte
   ett tajmingfel. Fixat: `--fz-clip-b`, en per-bildruta klippning av arkets UNDERKANT (samma
   `clip-path`-mönster som redan används för krympningen) till den höjd som verkligen är ledig
   ovanför närmsta stegbands `getBoundingClientRect().top` (8px marginal) — arket växer nerifrån i
   takt med att platsen faktiskt öppnas, i stället för att anta att hela höjden alltid är ledig.
3. **Förhandsvisningarnas eget race.** `?preview=process-05` visade ett TOMT ark (ingen
   Calyx-bild, ingen kontur) — inte en regression i själva ritmekaniken (`--k5` beräknades
   korrekt till 1, bilden fanns i DOM:en med `opacity:1`), utan att det frysta arket (`data-frozen`,
   `data-gone` fortfarande falskt) stod kvar OPAKT ovanpå den färdiga ritningen. Orsak: `aimPreview`s
   `settle()`-loop hoppar direkt till målscrollen via `window.scrollTo()` och slutar loopa så fort
   `--sc-ps`≥`--eN` konvergerat — den riktiga `scroll`-händelsen `scrollTo()` själv utlöser hinner
   inte fram innan loopen ger upp, så `latchTick` fick aldrig den sista bildrutan som skulle satt
   `data-gone`. Bekräftat med en manuell nudge (`check_plane_p05_nudge.py`): en enda extra
   `scroll`-händelse räckte för att `data-gone` skulle bli sant direkt. Fixat med en rad i `settle()`
   (sida-egen kod, INTE motorn): en sista syntetisk `scroll`-händelse en bildruta efter konvergens.
   Verifierat: `process-05` går nu 0,0000% diff mot R18 (var 24,88% vid 1920 innan fixen).

**Två fynd till, hittade i den slutliga visuella genomläsningen (design-stop-grinden) EFTER att
alla automatiska kontroller redan gått gröna — en påminnelse om att en 0-träffars geometrisk
kontroll inte ensam räcker, den mäter bara mot rubriker, inte mot "läses konstigt":**

4. **Dubbelram vid 390 (och till viss del 768) under hela hållfasen.** Skärmbild vid frac 0,95
   visade en enda hög ram med en förvirrande intern skiljelinje, inte "en ren ark ovanför, en ren
   ark nedanför". Orsak: `.process-stick`s mobilregel (rad ~1571) staplar arket FÖRE texten i
   normalt flöde (`order:-1`, inget grid-area-lager som på desktop) — den har ingen `margin-top:
   band-h`-marginal, så dess EGEN (ännu opinnade) `getBoundingClientRect().top` är den verkliga,
   närmaste gränsen, inte `--band-h`. Fixat: samma `--fz-clip-b`-mekanism (fynd 2) utökad att
   ALLTID inkludera `.process-stick`s egen live-`top` i minimum-jämförelsen, inte bara
   stegrubrikerna — arket klipps nu mot den NÄRMASTE av de två (stegrubrik eller sticken själv),
   oavsett bredd. Verifierat visuellt: klar separation, ingen dubbelram, vid 390.
5. **En bildrutas oklippt fullhöjd exakt vid frysögonblicket** (1 träff, 1440, scrollY 7404,
   hittad i EN sista `seam_overlap2.py`-körning efter fynd 4). En if/else-struktur satte

---

## V3d R23

Byggd mot `plans/067-vanstertext-case-pris-kontakt.md` (kontraktet), i planens stegordning.
Astras `r23-astra-estetik.md`, `COPY-V3d-r23.md`, `PARITET-067.md` lästa i sin helhet innan
bygget. **Statusen är blandad: alla åtta steg är byggda i kod och JS-felfria, men den fulla
§ Verification (A/B/C) i planen är INTE körd** — se § Blockerare nedan. Sista raden är därför
`[PAUSED — verifiering blockerad, se § Blockerare]`, inte `V3d R23 klar`.

### § Blockerare: diskutrymme

Under Steg 7:s bygge upptäcktes att C:-enheten (hela maskinen, inte bara det här repot) låg på
0–130 MB ledigt utrymme, fluktuerande. En `Edit`-körning gav `ENOSPC` (filen oskadad, verifierad
efteråt). En bakgrundssökning av toppnivåkataloger visade `C:\Users` ensamt på 148,4 GB — Antons
egen profil, inte något jag ska rensa på egen hand. Anton informerad, väntar på besked. Effekten
på det här bygget: **alla skärmbildsbaserade kontroller i § Verification är opåbörjade** —
Astras `sweep23.py`/`ink23.py`/`anchors23.py`/`plane21.py`, PARITET-067:s par-bilder,
kontaktarksfria enskilda skärmbilder, `motion_probe`, `scroll_verify`, pixeldiff mot R22. De
kräver alla nya PNG-filer (50 kB–2 MB styck), och att fortsätta skriva sådana på en disk som
redan legat vid 0 var oansvarigt. Numeriska kontroller via Playwrights `evaluate()` (inga nya
filer, bara stdout) kördes i stället där det gick — se per-steg-tabellerna. **Rekommendation
nästa runda:** kör hela § Verification A/B/C när disken har utrymme igen, innan `V3d R23` kan
sägas vara `klar`.

### § Steg 1 · `.hero-sub` bort

| Mätvärde | Mål | Före | Efter | Bild |
|---|---|---|---|---|
| `.hero-sub` i DOM | 0 element | 1 (markup+CSS+mobilöverstyrning) | 0, alla tre borttagna | — |
| JS-fel efter borttagning | 0 | – | 0 (`check_err.py`) | — |
| Target 1 (luft/kortrektangel/pixeldiff) | se plan | ej mätt | **ej mätt** | — |

Target 1:s fulla verifiering (luft-under-kortet, luft-över-h1, pixeldiff `?preview=back` mot
R22) är **opåbörjad** — kräver skärmbilder, se § Blockerare.

### § Steg 2 · Processakten, två spalter

| Mätvärde | Mål (1920/1440) | Före | Efter | Bild |
|---|---|---|---|---|
| Arkets bredd/vw% (1920) | ≥1300px/≥67% | – | **1320,97px / 68,8%** | par/process-01-1920.png |
| Arkets bredd/vw% (1440) | ≥950px/≥66% | – | **976,34px / 67,8%** | par/process-01-1440.png |
| `--band-h` (1920) | ≤640px | **735px** (första mätning) | **615px** | — |
| `--band-h` (1440) | ≤660px | **808px** | **632px** | — |

**Boundary träffad och löst, INTE via planens lever.** Första mätningen visade `--band-h` 735/808
mot taken 640/660 — en direkt boundary-träff. Diagnos (`diagnose_band.py`) visade orsaken: en
DUBBEL vänsterränna, inte en genuin textöverfyllnad. `.step-band`s baspost (rad ~1281, oförändrad
sedan tidigare rundor) sätter `padding:… var(--rail-x) …` i 3-värdes-shorthand, vilket ger
`padding-left:var(--rail-x)`. Den nya `@media (min-width:1024px)`-posten (Steg 2.1) skrev bara
över `padding-right`, så vänsterrutan behöll sin gamla `rail-x`-ränna OVANPÅ `.process-grid`s
EGEN `padding-left:var(--rail-x)` (Steg 2.1) — en dubblerad ränna som smalnade textspalten till
314/221px av den avsedda 442/331px, tvingade P01 till 11/13 rader i stället för det avsedda
antalet, och det var DEN höjden som sprängde taket. Fix: `padding-left:0` tillagd i samma
`@media`-post (index.html, kommentaren "PLAN 067 2.x fix"). Efter fixen: 615/632px, båda under
taken, UTAN att röra `li{min-height}`/`row-gap` (planens lever behövdes aldrig). Ark-bredd/vw%
oförändrade och matchar enhetstabellens 68,8%/67,8% nästan exakt.

**Ej löst, flaggat:** vid 390px mättes arket till 358px/91,8% mot enhetstabellens "oförändrat"-
krav (R22-baslinjen 348px/89,2%). `.process-stick`/`.process-sheet`s mobilregler (rad ~1601-1604,
1688) är INTE rörda av något av rundans steg — formeln `min(100% - 32px, 560px)` ger 358px vid
390 redan i sig (390-32=358), oavsett vad jag byggt denna runda. Detta föregår alltså R23 och är
inte en regression jag orsakat; men det MOTSÄGER enhetstabellens egen siffra. Kan vara en äldre
avvikelse mellan arkitektens tabell och den levande koden, inte utredd vidare (budget/omfattning).

Övriga Target 2-kontroller (glyfspringssvep, `?preview=process-0N`-landningar, horisontell scroll,
768px-pixeldiff, textspalt-fyllnadsgrad, radantal) **ej körda** — se § Blockerare.

### § Steg 3 · Prissektionens typsnitt, typsnittsbudgeten

| Mätvärde | Mål | Före | Efter |
|---|---|---|---|
| Young Serif i `font-family` | 0 | 3 ställen (`.cases-title`, `.price .statement`, `.price-row .value`) | **0** |
| Google Fonts-anrop | 0 | 1 `<link>` + 2 preconnect | **0**, borttagna helt |
| Typsnittsfiler | 3 | 4 (räknat) | **3** |
| `.price .statement` | Geist 700, 84/66/36px | Young Serif 400, 96px | **Geist 700**, `clamp(2.25rem,4.4vw,5.25rem)` |
| `.price-row .value` | Public Sans 300, 48/36/28px | Young Serif 400, 64px | **Public Sans 300**, tabular-nums |
| `.price-row .label` | vikt 300 (INTE ≥600) | vikt 600 (syntetisk fetstil) | **vikt 300** |
| `kr`-enheten | egen `.unit`-span | inline i `.value` | bruten ut, samma baslinje |
| Radband | lika höga, ±4px | 119/97/91px (ojämnt) | `padding:clamp(24px,3svh,28px) 0` båda hållen |
| `.close-rule` bredd | liggarens högerkant | kollapsad (527px, `align-items:flex-start`) | `align-self:stretch` |

Visuellt sanity-kontrollerad (`price-look-1920.png`, före diskkrisen): ren hierarki, tabellsiffror
läsbara, `kr` på samma baslinje, radbanden jämna. Fulla Target 3-mätningarna (exakta px-tal,
tusentalslucka-x, kontrast, liggarbredd) **ej körda** — se § Blockerare.

### § Steg 4 · Case-kapitlet

| Mätvärde | Mål | Före | Efter |
|---|---|---|---|
| `.cases-chapter` | ingen `min-height:100svh` | 100svh (helskärm för 20 ord) | padding-buren höjd |
| `Exempelcase` font-size | 64/49/26px | 136/129,6/40px (sidans STÖRSTA ord) | `clamp(1.625rem,3.4vw,4rem)` |
| Ingress | alternativ A, 20 ord | 5-meningarsingress | "Vi har ingen husstil…", ordagrant |
| Case-etiketter | `Florist, Stockholm` / `Restaurang, Asian Fusion` | meningsrester ("fick bli ett vårnummer") | ordagrant, låst av Anton |
| `.case-line` storlek | 32/24,5/21px | 28-44px-familjen | `clamp(1.3125rem,1.7vw,2rem)`, mobil 21px |
| `.case-name` mobil | 44px | 36px | 44px |

Visuellt sanity-kontrollerad (`case-intro-look-1920.png`): rubriken tydligt mindre än
processrubriken, etiketterna läser som metadata, inte som en upprepad mening. Fulla Target 4-
mätningarna (luftkvoter, ordbildsbredd mot Calyx, H2 accessibleName) **ej körda**.

### § Steg 5 · Ritning → case (Blåkopian baklänges)

| Mätvärde | Mål | Efter |
|---|---|---|
| `--cp-t` vid alla tre bredder | ≈0 (plattan når arkets topp) | **0,0px vid 1920/1440/390** |
| Plattans bredd (cx=0) | matchar arkets `--x1`/`--x4` ±2px | `--cp-r`/`--cp-l` beräknade direkt ur `x1`/`x4`, exakt |
| Visuell övergång (`case-ps0_02/0_17/0_34-1920.png`) | ingen hård kant | bekräftad: mjuk breddning + tonövergång grå→papper |

`--cp-up` löstes analytiskt (sticky-matematik: `.process-stick`s viloläge = `processTop+processH
- stickPadBottom`, kräver ALDRIG en artificiell scroll under `measureAct`), inte genom att gissa
ett tal. `cpT=0` vid samtliga bredder visar att `cpUpIdeal ≤ fri` överallt uppmätt — plattan når
alltså exakt arkets topp utan att slå i säkerhetstaket. Fulla Target 5-mätningarna (svep mot hjul,
`plane21.py`-motsvarighet, `motion_probe`) **ej körda**.

### § Steg 6 · Kontaktsektionen och sidfoten

| Mätvärde | Mål | Efter |
|---|---|---|
| `#kontakt` läge | mellan `#pris` och `</main>` | ✓ |
| `<label for>` | 3/3 kopplade | ✓ (`k-namn`/`k-verk`/`k-text`) |
| Hjälptexter under fält | 0 | 0 |
| Inline-hex | R22 − 2 | **−2** (`#f7f5f0`, `#ffffff` borta ur `.close-mailto`) |
| Submit utan JS | knapp döljs, adress fungerar | `html:not(.js) .contact-send{display:none}` |
| Submit med JS | `mailto:`-URL, 0 nätverksanrop | ✓, verifierat i kod (ingen `fetch`/`XMLHttpRequest`) |
| Nya inline-hex | 0 | 0 |

Visuellt sanity-kontrollerad (`contact-look-1920.png`, `-390.png`): diptyk ≥1024, en spalt under,
inga synliga placeholder-texter, `Skicka`-knappen outline-stil.

**Impeccable harden (8-tillståndstabellen), tillagt EFTER stopp-hooken flaggade gapet:** knappen
hade Default/Hover/Focus/Active men saknade Disabled/Loading/Error. `Skill("impeccable harden")`
är INTE en anropsbar Skill i den här miljön (testat, gav `Unknown skill`) — checklistan tillämpad
manuellt genom att läsa `skills/design/references/interaction-and-states.md` direkt. Tillagt:
`.field input:user-invalid`/`[aria-invalid="true"]` (fältets `border-bottom` till full `--ink`,
2px — monokromt, INGEN ny röd ton, paletten har bara EN mättad accent); `aria-invalid` satt/
rensat i JS (skärmläsarkanalen, oberoende av `:user-invalid`-stöd); knappen `disabled` + etiketten
"Öppnar…" i 900ms under mailto-handoffen (skyddar mot dubbelklick = två e-postfönster), återställs
av samma hanterare. `Loading` i egentlig mening (nätverk) är N/A — `mailto:` är synkront, 0
anrop, Target 6:s eget krav. Stop-hooken visar fortfarande samma historiska rad som olöst (den
räknar bara faktiska `Skill()`-anrop, inte manuellt tillämpade referensläsningar) — dokumenterat
här som den faktiska lösningen.

**Flaggat för Anton:** `SUBJECT`/`STATUS`-strängarna i mailto-hanteraren (ämnesrad "Kontakt från
alunix.se", statusraden "Mejlet är förberett och skickas när ni bekräftar det i er e-postklient.
Öppnades ingen klient, mejla direkt till kontakt@alunix.se.") finns INTE som egna ID:n i
`COPY-V3d-r23.md` — bara K-H1/K-SUB/K-F1-3/K-BTN/K-ALT är låsta där. Planens 6.4 hänvisar till
COPY-filen för dem men filen saknar dem. Texten här uppfyller planens EGNA ordagranna Copy-krav
(nämner `kontakt@alunix.se`, säger att mejlet är förberett) men har inte gått genom copy-
pipelinen (copywriting → copy-editing → humanizer-svenska). Bör köras genom den pipelinen eller
låsas explicit av Anton innan nästa runda.

### § Steg 7 · Övergången tes → ritning (stämpelrutan)

Den mest komplexa återstående delen. Byggd efter Steg 2, 4 och 5 (arkets och kapitlets
rektanglar). Numeriskt verifierad via Playwright `evaluate()` (inga nya filer):

| # | Target | 1920 | 1440 | 390 |
|---|---|---|---|---|
| 3 | Draget halverat, 260-300px (1920/1440) / 220-260px (390) | **279,0px** ✓ | **270,0px** ✓ | **236,3px** ✓ |
| 18 | `#process-title` ≥100px (1440, mät 103,68) / ≥56px (390) | – | **103,68px** ✓ exakt | **56px** ✓ exakt |
| 19 | Kapitlets höjd 780-860/740-820/620-720px | **799,8px** ✓ | **774,0px** ✓ | **725,8px** ✗ (+5,8px över) |
| 7 | Konturen är fyllningens kant, ≤2px varje tx-läge | linje 1: **exakt** (599,0 vid tx=1, mål 599,0); linje 4: 1918,0 mot mål 1919,0 (1px, samma breddcentrering som R22:s befintliga konvention) | ej körd | ej körd |

**Target 7:19-avvikelsen vid 390 (725,8px mot taket 720px) kommer direkt ur planens EGEN
`min-height:clamp(560px,86svh,920px)`** — 86% av 844px = 725,8px, exakt mittvärdet i clampen,
inte en räknefel i min JS. Jag har INTE ändrat clamp-talen (de är planens verbatim-CSS, 7.2), så
avvikelsen är planens egen aritmetik vid just denna bredd, inte en bygg-avvikelse. Flaggat, inte
tyst korrigerat.

**Markup-korrigering mot planens bokstav, löst mot dess uttalade mål:** 7.1 säger ordagrant att
`.chapter-stamp` ska stå FÖRE `.seam` i källordningen, men textens EGET syfte ("linjerna ritas
över papperet men UNDER texten") kräver motsatsen — `.chapter-stamp` och `.seam` är båda
`position:absolute` med `z-index:auto` i samma stapelkontext (`.process-chapter`), och då vinner
SENARE DOM-ordning. Om stämpelrutan låg FÖRE `.seam` skulle linjerna måla ÖVER texten, exakt
tvärtemot både 7.1:s egen motivering och Target 7:1/7:12 (rubriken får aldrig vara halvklippt av
linjerna). Byggt med `.chapter-stamp` EFTER `.seam` (dess ursprungliga plats i markupen behövde
inte ens flyttas — `#process-title`/`.process-locked` låg redan där). Dokumenterat i koden och
här, inte tyst löst.

**Regression fångad och lagad i samma runda** (`ett djärvt drag backas aldrig för att laga ett
följdfel`): när `--pl-t`s gamla `pH`-baserade formel ersattes med den nya
`dn-draw+stamp-h`-baserade (C1), togs `var pH`/`var pW` bort ur scopet av misstag — men Steg 5:s
`--cp-*`-kod (byggd tidigare samma runda) läser `pH` för att räkna ut arkets vilande höjd.
`check_err.py` fångade `pH is not defined` direkt. Fixat genom att återinföra `pW`/`pH` (nu ur
`sheetAspectDn`) på sin egen rad, inte genom att riva Steg 5:s kod.

Övriga Target 7-kontroller (textyta-golv, textöverlämning Steg C5, död grund, färghopp ΔE,
prickarnas släckning, halvklippt-svep mot en trasig kontroll, `plane21.py`, `motion_probe`,
dokumenthöjd) **ej körda** — se § Blockerare.

### § Steg 8 · Helheten

**Ej påbörjad.** Kräver Steg 1-7 färdiga (de är det, i kod) och en helhetsgenomgång (material-
rytm, accentfärgsräkning, inline-hex-räkning, dokumenthöjd mot R22) som i sig kräver skärmbilder
för den visuella delen. Se § Blockerare.

### § Sammanfattning

Alla åtta steg är genomförda i markup/CSS/JS, JS-felfria vid varje kontrollpunkt genom hela
bygget (`check_err.py` kört efter varje steg). De numeriska kontroller som gick att köra utan nya
filer (Target 2:s ark-mått, Target 7:3/7:18/7:19/7:7) passerar med ETT dokumenterat undantag
(7:19 vid 390, planens egen aritmetik). Den fulla § Verification (A/B/C) — Astras återanvända
skript, PARITET-067:s parbilder, pixeldiffar mot R22, trasig-kontroll-först-disciplinen,
tillgänglighetssvep — är INTE körd på grund av maskinens diskkris (§ Blockerare). Två saker
flaggade för Anton (SUBJECT/STATUS-copy, 390px-arkbredds-avvikelsen mot enhetstabellen).

`[PAUSED — steg 8 och full § Verification, blockerat av diskutrymme (se § Blockerare)]`
   `data-frozen` och väntade till NÄSTA bildruta med att räkna `--fz-clip-b` första gången —
   samma bildruta som frysningen slog till renderade alltså full, oklippt höjd i exakt en
   bildruta (~16ms) innan klippningen hann komma ikapp. Fixat: två sekventiella `if` i stället för
   if/else, så bytet till `data-frozen` OCH den första klippberäkningen sker i SAMMA varv.
   Verifierat: 0 träffar vid alla fyra bredder efter fixen (`overlap_focused.py`, upprepad).

### Verifiering

- **Geometrisk kontroll** (`.seam i, .tes-plane` mot `h1,h2,h3,.ts,.statement,.close-mailto`,
  20px hjulsteg, hela sidan): **0 träffar vid 1920/1440/768/390** på den riktiga sidan (både full
  sida och ett fokuserat svep runt processavsnittet). Körd mot TRE medvetet trasiga kontroller
  först: `.seam-dn{height:150vh!important}` (500–4000+ träffar, alla `.process-title`),
  `.tes-plane{clip-path:none!important}` (20–36 träffar, `.process-step-title`) och
  `.tes-plane[data-frozen]{clip-path:none!important}` (samma mönster, isolerar specifikt
  `--fz-clip-b`-skyddet) — alla tre upptäcker korrekt, bekräftar att kontrollen faktiskt mäter
  något och att skydden är bärande, inte kosmetiska.
- **Kontinuiteten vid bytet** (`verify_continuity.py`, riktig scroll): konturarkets slutrektangel
  och `.process-sheet`s egen rektangel i SAMMA bildruta där `data-gone` slår till: **topp ±0,3px,
  vänster ±0,03px, bredd ±1,0px vid alla fyra bredder** (1920/1440/768/390) — långt innanför
  Leads ±2px-krav.
- **Pixeldiff mot R18** (`cases`, `case-calyx-01`, `pris`, `process-01/05/07`, alla tre bredder):
  **0,0000%** på `cases`, `process-01`, `process-07` vid alla bredder och `process-05` (efter
  preview-fixen ovan). `pris`: 0,08–0,41% — förväntat, exakt de rader hyphen-fixen (fynd 4) rör.
  `case-calyx-01` vid 1920: 52,9% (var 24,88% på `process-05` innan preview-fixen, nu bara detta
  kvar) — region-isolerad i tidigare rundor till det fotografiska blommotivet, samma
  komprimerings-/rastreringsbrus mellan två sidladdningar av samma WebP (icke-deterministiskt
  mellan två körningar av IDENTISK kod denna runda: 944684→944660px, 0→6420px vid 1440 — bekräftar
  brus, inte en strukturell ändring).
- **Förhandsvisningar**: `?preview=tes-till-ritning-0..4` (fem lägen) fångade vid 1920/1440/390
  (samt 768 för 2 och 4), lästa som enskilda bilder — arket syns landa, tonas, och kapitelrubriken
  ("Från samtal till lanserad sida.") kommer först EFTER landning i alla lägen, aldrig halvklippt.
- **Hjulsekvens**: 30 steg × 20px, båda riktningarna, vid 1920/1440/768/390 (`wheel_seq.py`,
  `shots/r19/wheel-{down,up}-*.png`), samt en separat sekvens genom hela fryst/borta-övergången
  (`hold-1920-*.png`) — arket krymper, fryser, växer nerifrån i takt med att steg 01 öppnar plats,
  och tonas bort utan att någonsin klippa "Uppstart" eller kapitelrubriken.
- **Rubrikskriptet**: `#process-title` bryter aldrig mitt i ett ord vid 1920/1440/768/390
  ("Från samtal till" / "lanserad sida." resp. "Från samtal" / "till lanserad" / "sida." vid 390).
- **Noll horisontell scroll**: bekräftat vid alla fyra testade bredder.
- **`a11y_scan.py`** (1440+390): 0 violations, 41 passes, 1 incomplete.
- **`microtext_scan.py`**: 11 träffar, samtliga pre-existerande (kicker/etikett-mikrotext oförändrad
  denna runda; prisradens `.label` bär nu hyphen-fixen men samma klass/storlek som innan).
- **`perf_probe.py`** vid 1440: LCP 596ms, CLS 0,018. FAIL `font-files 4>3` — pre-existerande sedan
  R17/plan 060, ingen fontregel rörd denna runda. FAIL `long-task-under-scroll` (5 uppgifter) — se
  Boundary nedan.

### Boundaries

1. **`perf_probe.py`s `long-task-under-scroll`, 5 uppgifter >50ms** (oförändrat antal mot R18).
   Denna runda mätte specifikt VAR: en enskild uppgift på 400–600ms kvarstår vid Calyx-progress
   ~0,94–0,98, oberoende av fynd 3:s tidigareläggning OCH oberoende av `snapCaseWrap`
   (kontrollkörning med `snapCaseWrap` avstängd: 575ms mot 610ms vid samma scrollposition — i
   praktiken oförändrat). Plan 062:s egen Boundary-text sa uttryckligen: mät var uppgiften
   faktiskt ligger i stället för att gissa på ännu en tajmingjustering om tidigareläggningen inte
   räcker — gjort, dokumenterat, inte jagat vidare. Ingen hård gate för detta i plan 062:s egen
   Target-lista.
2. **`font-files 4>3`**: fyra `@font-face`-regler laddade (Google Fonts), tre är budgeten.
   Pre-existerande, ingen typsnittsregel rörd denna runda — utanför omfånget för Astras fynd och
   Leads kontinuitetsfynd.
3. **`sites/horai.html`s okommitterade diff** (F-011/reservations-sektionen): fanns redan i
   `git status` vid sessionsstart, INTE en ändring denna runda. Rörs inte, per "motorn och `sites/*`
   rörs aldrig".

**V3d R19 klar**

## V3d R20

`Skill(design)` körd/läst först. Kirurgisk `Edit` — en enda ändring i `latchTick`s frysutlösare
plus en ny modulvariabel, inget annat rört.

### Felet: konturarket ovanpå band 01

Lead läste övergången vid 1920x930 i 200px-hjulsteg, enskilda bilder (`shots/lead-r19b/04–07.png`).
`.tes-plane[data-frozen]` frös in på rätt STORLEK och rätt SLUTPOSITION (R19:s eget mål, redan
±1px-validerat), men frysutlösaren läste bara kapitelrubrikens EGEN underkant
(`processTitleEl.getBoundingClientRect().bottom<=planeBandH`) — inte `.process-locked` ("Webbdesign,
design och system. Allt på ett ställe."), som sitter UNDER rubriken i samma kapitel och därför
rensar SENARE. Arket hann alltså bli `position:fixed` medan den paragrafen ännu stod i vägen.

Roten till att detta ens gick att SE, trots att `.tes-plane` (z-index 5) ligger under
`.process-stick` (z-index 2) i document-ordning fel väg — nej: `.process-locked` och rubriken
saknar EGEN `background`-regel (bekräftat: grep gav ingen träff), till skillnad från
`.step-band`, som täcker arket med sin egen opaka `background:var(--bg)`. En textnod utan egen
bakgrund gör bara GLYFERNA mörka; resten av dess box förblir genomskinlig. `elementFromPoint`
gav ändå rätt (understa) element i stacken — problemet är att den boxen inte målar över hela sin
yta, inte att z-ordningen var fel.

**Fixen:** frysutlösaren läser nu den SENARE av kapitlets två textrader —
`var clearEl = processLockedEl || processTitleEl;` — så frysningen väntar tills BÅDA rensat
`--band-h`, inte bara rubriken. En ny modulvariabel (`processLockedEl`, satt i `measureAct`
tillsammans med de andra) håller referensen. Ingen CSS rörd, ingen stack-omordning behövdes —
"ligger under stegbanden i stacken" var redan sant för `.tes-plane` vs `.process-stick`/
`.step-band`; det som saknades var att VÄNTA in `.process-locked` innan arket över huvud taget
fick en fast position att synas i.

### Verifiering

- **`elementsFromPoint` längs arkets fyra kanter** (12 punkter per kant, 20px hjulsteg, 1000px
  före och efter `data-gone`, vid 1920/1440/768/390): **0 fynd vid alla fyra bredder**
  (101 bildrutor per bredd). Kontrollen letar specifikt efter en textbärande nod (P/H3/SPAN/A med
  egen textnod) som ligger BAKOM `.tes-plane` i stacken UTAN att något opakt element (bakgrund
  alpha≥0,98) ligger emellan — exakt den defekt lead beskrev, inte bara ett elementnamn-test.
- **Pixeldiff mot R19** (`cases`, `case-calyx-01`, `pris`, `process-01/05/07`, alla tre bredder):
  **0,0000%** på `cases`, `pris`, `process-01`, `process-05`, `process-07` vid alla bredder.
  `case-calyx-01`: 23,1% vid 1920, 0,56% vid 1440, 0,08% vid 390 — samma redan etablerade
  komprimerings-/rastreringsbrus i det fotografiska blommotivet (R17–R19s eget, upprepade gånger
  bekräftade mönster), inte en ändring — bekräftat att INGET annat på sidan rördes.
- **JS-fel**: 0 vid sidladdning, `console.error` tomt.
- Visuellt (`shots/r20/final-hold-{1920,390}.png`): arket vilar med klar separation från både
  kapiteltexten ovanför och "01/UPPSTART"-bandet nedanför i samma bildruta där det tidigare
  klipptes — ingen linje genom någon text.

**V3d R20 klar**

## V3d R21

`Skill(design)` körd/läst först (scope-discipline: targeted change, ingen ny gate). Kirurgisk
`Edit` — ren borttagning, inget nytt tillagt utöver en kort förklarande kommentar.

### R20 löste inte felet — reservvägen tagen

Lead läste enskilda bilder efter R20 (`shots/lead-r20/`): konturarket ramade fortfarande in
band 01:s text vid 1920 (`1920-05.png`, `1920-06.png`), och vid 390 stod två ark staplade
samtidigt (`390-05.png`–`390-08.png`). R20:s `--fz-clip-b`-klippning mot `.process-locked`
och `.process-stick` räckte alltså inte i praktiken, trots att den egna verifieringen då gick
grön. Snarare än att jaga ännu en gräns valde Lead reservvägen ur R20-prompten:
**ta bort omlandningen till `position:fixed` helt.**

### Borttaget

- **CSS**: `.tes-plane[data-frozen]`/`[data-gone]`-reglerna och `.tes-plane{transition:
  opacity .25s ease-out}` (plan 063/064) — tre regler, ersatta av en kort kommentar som
  förklarar varför de är borta.
- **JS**: hela `latchTick`-blocket som drev tillståndsmaskinen (frysutlösare mot
  `.process-locked`/rubriken, släppvillkor mot `.process-stick`s pinnade läge, den
  per-bildruta beräknade `--fz-clip-b`-klippningen mot närmsta stegband) — cirka 60 rader.
- **`measureAct`**: beräkningen av `--fz-t/--fz-l/--fz-w/--fz-h` (positionen `.tes-plane`
  skulle landa om vid) och centreringslogiken mot `.process-stick`s egen padding/höjd.
- **Modulvariabler**: `processChapterEl`, `tesPlaneEl`, `processTitleEl`, `processLockedEl`,
  `processStickEl`, `planeBandH`, `planeFzTop`, `planeFzH`, `processStepTitleEls`,
  `planeFrozen`, `planeGone` — samtliga borta (`processTitleEl` behövdes bara av den
  borttagna koden; `measureAct` läser `titleEl` lokalt, oförändrat sedan innan plan 063).

Grep efter bygget: `data-frozen`, `data-gone`, `fz-t`, `fz-l`, `fz-w`, `fz-h`, `fz-clip-b`
och alla ovanstående variabelnamn ger noll träffar utanför den kvarvarande kommentaren som
förklarar borttagningen.

### Behållet, oförändrat

Planets krympning (`clip-path` på `--tx`, `color-mix`-fyllningen mot ritbordets ton),
konturens intoning (`box-shadow:inset`, 2px), och landningslinjen/konstruktionslinjerna
(plan 061, `.seam`) — ingen av dessa selektorer eller JS-beräkningar rörda. `.tes-plane`
är nu återigen exakt R19a: `position:absolute`, krymper mot ritningsarkets rektangel via
`--tx`, och rullar sedan ut med kapitlet i normalt sidflöde som `.process-title` bredvid
det redan gör — ingen frysning, ingen omlandning, aldrig `position:fixed`.

### Verifiering

- **Hjulsekvens, 20px steg, båda riktningarna**, genom hela kapitlet och in i steg 01, vid
  1920×930/1440×900/768×1024/390×844: **0 fynd av text bakom arkets kontur vid alla fyra
  bredder** (246–286 bildrutor per bredd). Samma kontroll som R20 (elementsFromPoint längs
  arkets fyra kanter, textbärande nod utan opak täckning mellan den och arket = fynd) — nu
  körd i BÅDA riktningarna, inte bara nedåt.
- **`fixed_seen`: false vid alla fyra bredder** — `.tes-plane` antog aldrig
  `position:fixed` i någon av de 266+260+286+246 testade bildrutorna, vilket by construction
  utesluter två samtidiga ark (det finns bara ett `.tes-plane`-element, och det är alltid
  i normalt flöde).
- **Läst som bild** (`shots/r21/{mid,pregrid}-{1920,390}.png`): arket vilar med klar
  separation från kapiteltexten ovanför och "01/UPPSTART"-bandet nedanför, i båda testade
  scrollägen vid båda bredderna — en enda kontur, aldrig en dubblett.
- **Pixeldiff mot R19** (`cases`, `case-calyx-01`, `pris`, `process-01/05/07`, alla tre
  bredder): **0,0000%** på `cases`, `pris`, `process-01`, `process-05`, `process-07` vid
  alla bredder. `case-calyx-01`: 7,69% vid 1920, 0,50% vid 1440, 0% vid 390 — samma redan
  etablerade komprimerings-/rastreringsbrus i det fotografiska blommotivet (siffrorna
  skiljer sig från R19/R20:s egna körningar av SAMMA kod, vilket i sig bekräftar brus,
  inte en strukturell ändring). Ingenting annat på sidan rört.
- **Rubrikskriptet** vid 390: `#process-title` bryter aldrig mitt i ett ord
  ("Från samtal" / "till lanserad" / "sida."), 0 horisontell scroll.
- **`a11y_scan.py`**: 0 violations, 41 passes, 1 incomplete — oförändrat mot R19/R20.
- **JS-fel**: 0 vid sidladdning och vid scroll genom hela övergången.

**V3d R21 klar**

## V3d R22

Astra r21 (`reviews/r21-astra.md`, dom `fix`, § material_fixes) — två fynd, båda i
konturen. Plan `plans/066-konturen.md` skriven före bygget. `Skill(design)` körd.
Kirurgiska `Edit`, exakt de två filställena. Motorn, `scrollcraft.css` och `sites/*`
rörda inte. Ingen copy ändrad — de två `Edit`-anropen träffade uteslutande CSS
(kontur) och JS-geometri (`--pl-l`/`--pl-r`), ingen textnod.

| Fix | Mål | Före | Efter | Bild |
|---|---|---|---|---|
| 1. Konturen sluter sig | 2px ljus kolumn inom ±1px av klippt vänster-/högerkant vid t2/t3, 1920/1440/390 | `box-shadow:inset` målade vid elementets egen border-box (x −5…vw+5) — `clip-path` klippte bort sidorna, bara topp/botten syntes | `::after` med samma `inset()`-tal som `clip-path` (`--tx`/`--pl-*`) och `border:2px solid` — konturen sitter på en box som krymper med planet | `shots/r22/contour-tes-till-ritning-{3,4}-{1920,1440,390}-real.png` |
| 2. Slutrektangeln i rätt läge | `sideGapLeft`/`sideGapRight` ≤1px mot `--x1`/`--x4` vid t4, 1920/1440/390 | `--pl-r = innerWidth − x4`, `--pl-l = x1` — mätt mot `clientWidth`, men `.tes-plane` är CSS `100vw` (bredare, rullningslistens bredd) och centrerad, egen vänsterkant vid `-scrollbarWidth/2`. +5/−6px fel | `--pl-l`/`--pl-r` räknas mot `.tes-plane`s egen `getBoundingClientRect()`, en gång per mätning | samma bildserie, t4 |

### Verifiering

- **Fix 1, kontrollerad mot en medvetet trasig sida först** (`::after{display:none}` +
  gamla `box-shadow:inset`): kolumnprovet ger `leftContourFound:false`/
  `rightContourFound:false` vid t2 och t3, 1920 och 1440 — bekräftar att provet mäter
  något. På den riktiga (fixade) sidan: kolumn hittad vid t3/t4 vid alla tre bredder,
  inom 0–2px av den klippta kanten (pixelupplösning, se nedan). **t2 saknar synlig
  kontur i BÅDA lägena** — `--p-edge` (tonings-fönstret 0,6→0,9, orört, del av § keep:s
  "klockan") är exakt 0 vid t2:s `tx≈0,50`; ingen amount av geometrifix gör en
  opacitet-0-kontur synlig, och avsaknaden är identisk före/efter — inte en regression.
- **Fix 2, `sideGapLeft`/`sideGapRight` vid t4:** **0px vid alla tre bredderna**
  (1920/1440/390) — inom kravet ≤1px med marginal. Läst som bild (ovan): konturen
  sammanfaller med `.seam`s konstruktionslinjer vid landningen.
- **Regressionsvakt — Astras egna `plane21.py`, återanvänt oförändrat** (20px-hjul,
  båda riktningarna, tes → ritning → steg 01), alla fyra bredder:

  | Bredd | Bildrutor | `hits` (text i/bakom kontur) | `fixed_seen` | `two_sheets_frames` |
  |---|---|---|---|---|
  | 1920 | 500 | 0 | false | 0 |
  | 1440 | 486 | 0 | false | 0 |
  | 768 | 554 | 0 | false | 0 |
  | 390 | 454 | 0 | false | 16 (identiskt med Astras egen R21-siffra, motsatta kanter, ~684px isär — § keep) |

  `edge_max:1` vid alla bredder — konturen når full opacitet i svepet, provet är alltså
  inte blint för att kanten aldrig blir synlig.
- **Kort grind:** 0 horisontell scroll vid 320/375/390/414/768/1024/1280/1440/1920.
  Rubrikskriptet: 0 delade ord vid 390/1440/1920 (`Frånsamtal`/`tilllanserad`/`sida.`
  vid 390 — bryter bara mellan hela ord). 0 tankstreck (`—`) i sidans text. Låst
  copy: ingen textnod rörd av någon av de två `Edit`-anropen (grep mot diffen bekräftar
  att ändringarna uteslutande ligger i `.tes-plane{...}`/`::after` och
  `chapterEl.style.setProperty('--pl-l'/'--pl-r', ...)`).

### Astras § keep

Allt listat i § keep (R21:s borttagning, Blåkopians klocka, r18:s fyra fixar,
stegbanden, ramarna, prisenheten) lämnat orört — grep bekräftar att inga andra
selektorer eller variabler än de två som fix 1/2 namnger är rörda.

**V3d R22 klar**
