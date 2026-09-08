# FEEDBACK.md — Antons domar, en regel per post

Läses **alltid** i `design/SKILL.md` Step 1b, tillsammans med `TASTE.md`, innan Step 2.
Referensgolvet i `hooks/design-gate.py` spärrar första UI-skrivningen i ett nybygge tills
den här filen är läst. TASTE.md säger hur typ, bild, yta och rörelse ska samspela;
den här filen säger vad Anton faktiskt sagt om det kedjan byggt, och vilken regel som
följer av det.

**Så skrivs en post.** En dom = en post, samma session som domen. Fält: datum · runda/board ·
vad som visades · Antons ord (citat, oredigerat) · dom (bra / dåligt / hade kunnat bli bra om)
· regeln som härleds · status (var regeln portats: TASTE.md §, house-physics, SKILL.md,
eller "bara här"). Regel för orkestreraren: ingen board utan post innan `/conclude`.
Ta aldrig bort en post; en regel som visar sig fel får en ny post som upphäver den.

---

## 2026-09-06 · r6-boarden (port 4624), sex Alunix-celler, K1 Skymning / K2 Affischen / K3 Konsolen

### F-001 · Reservläget utan resa är tomt
- **Visades:** alla sex celler under `prefers-reduced-motion: reduce` (Antons Windows har
  animationseffekter av).
- **Antons ord:** "det var ingen scroll effekt överhuvudtaget, eller någon annanstans. Inte
  heller på de andra sidorna. I övrigt var båda sidorna väldigt platta och intetsägande"
- **Dom:** dåligt. Rörelsen fanns i rörelseläget, men reservläget bar inte sekvensen, så
  sidan blev ett statiskt slutläge.
- **Regel:** under reduced motion visas set-piecets *formade* lägen i ordning som egna
  sektioner (samma lägen som `?preview=`), aldrig en tumnagel av målet och aldrig ett hopp
  till sista rutan. Orkestreraren granskar båda lägena som pixlar och anger läget per bild.
- **Status:** portad till SKILL.md § Motion, house-physics Motion, `design-stop.py` exit-bar
  (kräver rm-bild vid scroll), boardens varningsrad.

### F-002 · Målet i vila får inte förhandsvisa slutläget
- **Visades:** K1 körning 1 (kedjan): fönstret tänt med Hōrai-skärmbilden redan i stillhet.
  K1 körning 2 (native): fönstret tänds först vid scroll.
- **Antons ord:** "Det lilla fönstret i första scenen laddades statiskt från början i ena
  versionen och inte alls i den andra"
- **Dom:** dåligt (körning 1); körning 2:s lösning i rörelseläge är rätt.
- **Regel:** set-piecets mål (fönstret, ordet, objektet) är tyst i vila och tänds vid första
  scrollen; under reduced motion är det fullt närvarande som egen scen.
- **Status:** portad till house-physics Motion, SKILL.md § Motion, målbild K1 v2.

### F-003 · En auktoritet per sida, också när typen bär
- **Visades:** K2 båda körningarna: affischtyp 300 px+, stora skärmbilder och siffror i
  ordmärkesgrad på samma sida.
- **Antons ord:** "det blev 'för mycket', det balanserades inte ut någonstans utan blev bara
  jobbigt att kolla på, i båda versionerna"
- **Dom:** dåligt. Målbilden (Claudes) bad om två auktoriteter.
- **Regel:** ett displayelement per skärm; när typen bär är siffror kickers och skärmbilder
  plates i spalt. Orkestrerarens målbild måste namnge auktoriteten och vad som viker
  (målbildsgrinden, skill-orchestration § 12).
- **Status:** TASTE.md § 1 (redan), skill-orchestration § 12, målbild K2 v2.

### F-004 · Heron behöver något bredvid ordmärket
- **Visades:** K2 båda körningarna utan hero-bild; körning 2 (native) hade fotot *i*
  bokstäverna.
- **Antons ord:** "Båda saknade även hero-bild och lånade bara element från Calyx, körning
  2:s version med bild under texten hade kunnat bli väldigt bra med något mer i hero:n,
  kanske en bild bredvid eller en neutral bakgrund"
- **Dom:** hade kunnat bli bra om. Bokstavsfönstren är rätt idé.
- **Regel:** en typburen hero får en enda dämpad plate bredvid ordmärket (svartvitt,
  dokumentärt), aldrig under; fönstren i bokstäverna ska visa exempelsajterna, inte
  Calyx-fotot ensamt. Antons val 2026-09-06: platen bredvid.
- **Status:** målbild K2 v2; bara här.

### F-005 · Typsnittsblandningen i K2 körning 1 är förebild
- **Visades:** K2 körning 1 (kedjan): två snitt med tydliga roller.
- **Antons ord:** "körning 1 gjorde typografin betydligt intressantare med en bättre
  blandning av typsnitt"
- **Dom:** bra.
- **Regel:** två snitt, rollerna korsar aldrig (TASTE.md § 4.2); K2 v2 utgår från r6
  B-K2:s val.
- **Status:** målbild K2 v2; bara här.

### F-006 · Glaskort med telemetri över ett foto är AI-slop
- **Visades:** K3 båda körningarna.
- **Antons ord:** "'Konsolerna' var katastrofal AI- slop, jag vet inte ens vad det skulle
  likna för något."
- **Dom:** dåligt. Felet satt i målbilden (Claudes), inte i byggarna.
- **Regel:** glaskort, dashboard-över-foto, "live"-punkter och telemetri-chrome hör till
  AI-troplistan och stoppas i målbildsgrinden innan någon brief skrivs.
- **Status:** skill-orchestration § 12 (troplistan), TASTE.md § 5 (komplement).

### F-007 · Matchar inte målbilden = blockerande fel
- **Visades:** K1 båda körningarna mot målbildens "kameran åker in i ett fönster".
- **Antons ord:** "Outputen i den första scenen matchade inte alls beskrivningen i planen."
- **Dom:** dåligt.
- **Regel:** orkestreraren jämför signaturakten mot målbilden bild för bild i rörelseläge
  innan någon annan granskning; avvikelse från signaturakten stoppar rundan.
- **Status:** skill-orchestration § 12 (runda 2); bara här.

### F-008 · Referenserna måste läsas, och briefen får inte förbjuda dem
- **Visades:** noll lästa filer under `design/references/`, ingen TASTE.md, i alla
  kedjeceller.
- **Antons ord:** "skillkedjan inte verkade fyrade som den skulle, med noll referenser
  kollade över alla körningar, vilket är grunden till att den ska fungera"
- **Dom:** dåligt (kedjan och orkestrerarens prompt).
- **Regel:** TASTE.md + FEEDBACK.md + reference-lock + katalogposternas filer inkl.
  `extract/*-DESIGN.md` läses alltid; vid scrollbrief även `scroll/devices.md` +
  `feel-and-fingerprint.md`; hooken nekar annars första UI-skrivningen.
- **Status:** SKILL.md Step 1b/2b, `design-gate.py` referensgolv, `design-vision-track.py`
  `ref-read`, skill-orchestration § 12.

### F-009 · Modellstorlek syns inte i one-shot-läge
- **Visades:** sju Fable-high-processer med samma prompt, ingen dialog.
- **Antons ord:** "jag märker faktiskt ingen skillnad på kvaliteten på Fable-agenternas
  output jämfört med Sonnet"
- **Dom:** iakttagelse, inte en regel om modellen. Formatet (spec som implementation, en
  runda, varv brända på infrastruktur) neutraliserar modellen.
- **Regel:** delegerade byggen körs i rundor med fold-grind och pixelläsning emellan;
  infrastruktur (server, foton, genererat material) levereras av orkestreraren.
- **Status:** skill-orchestration § 12, `scripts/serve.py`, r7-harnesset.

### F-010 · Hōrai är ett fönster i fasaden, inte en ruta utanpå den
- **Visades:** r6 K1 (kedjan) i rörelseläge, `tests/alunix-ab-r6/review/B-K1/grid-motion.png`
  20–25 %: Hōrai-skärmbilden ligger som en platt rektangel ovanpå fasaden medan fotot zoomas.
- **Antons ord:** "Se till att Horai-rutan INTE ligger statisk utanpå fasaden som nu, utan
  visas som ett fönster i fasaden först när man kommer närmare, för att sedan zoomas in, se
  även till att övergången FRÅN horai görs dynamiskt och snyggt"
- **Dom:** dåligt (rutan utanpå); krav på r7.
- **Regel:** när en sida ska "bli" något i ett foto (ett fönster, en skärm, en skylt) ska
  innehållet maskas in i objektets verkliga öppning, med objektets material kvar ovanpå
  (glasreflex, karm), och först när kameran är nära nog att öppningen bär det. Ingen platt
  ruta över fotot. Och en set-piece-akt har en koreograferad utgång, inte bara ett klipp:
  det som tog över skärmen lämnar den genom en rörelse som hänger i motivet.
- **Status:** målbild K1 v2 (signaturakten och akt 3→4), house-physics Motion (nästa
  revision), bara här tills dess.

## 2026-09-07 · r7-boarden (port 4625), K1 dömd med reduced motion oavsiktligt på

### F-011 · Rörelse ska alltid spelas upp, oavsett webbläsare eller systeminställning
- **Visades:** K1-2 i boarden, i tre olika webbläsarkontexter samtidigt (Claude Browser-
  panelen, Antons riktiga Chrome, Coworks inbäddade panel) — alla tre visade reservlägets
  statiska sektioner, ingen rörelse. Grundorsak dubbelkontrollerad: Windows
  "Animationseffekter" var fortfarande av (`UserPreferencesMask` byte 4 = `0x10`, oförändrat
  sedan F-001-diagnosen 2026-09-06), vilket satte `prefers-reduced-motion: reduce` i alla tre
  kontexter samtidigt eftersom det är en OS-nivå-inställning. Byggets kod följde då
  house-physics/SKILL.md-regeln från F-001/F-002 korrekt (visade reservlägets sektioner,
  aldrig en tumnagel) — koden var inte trasig, regeln var fel given vad Anton faktiskt vill.
- **Antons ord:** "Vi behöver göra samma sak som de övriga webbplatserna, vi behöver animera
  oavsett inställningar. Det måste vara en hård regel i designsystemet, ALL animation ska
  fungera och visas oavsett webbläsare och systeminställningar, säkerställ detta." — och,
  efter att jag lade fram avvägningen (att detta är en medveten avvikelse från
  tillgänglighet för besökare med vestibulära besvär, inte bara en bugfix för din egen
  granskning): "B, och gör det till standard globalt som permanent override för all
  accessability audit."
- **Dom:** medvetet, informerat beslut — inte en oavsiktlig lucka. Bekräftat efter att jag
  ställt frågan rakt: gäller det bara din egen granskning, eller den publicerade sajten för
  alla besökare? Svaret var det senare, permanent, globalt.
- **Regel:** rörelse (den delade reveal:en och signaturens set-piece) spelas alltid upp.
  Inget bygge läser `prefers-reduced-motion` eller någon annan webbläsar-/OS-inställning för
  att stänga av eller ersätta rörelsen, och inget bygge har längre en parallell statisk
  reservlägesväg. Detta upphäver F-001/F-002:s regel om reservlägets sekvens av formade
  lägen — det finns ingen reservväg kvar att göra rätt eller fel. `a11y-audit` flaggar inte
  längre avsaknad av reduced-motion-stöd, i något projekt den körs i (global ändring, inte
  bara Alunix). WCAG 2.3.1 (blinkgräns, tre gånger per sekund) är opåverkad — det är en
  säkerhetsgräns, inte en preferens, och den gäller fortfarande.
- **Status:** house-physics.md § Motion (båda ställena), SKILL.md § Motion + shipping-gate-
  raden, `hooks/design-stop.py` (rm-skärmdumpkravet borttaget ur exit-bar),
  `~/.agents/skills/a11y-audit/SKILL.md` (standing override + escalation triggers),
  `~/.agents/skills/a11y-audit/references/principles.md` (annoterad, inte borttagen).

### F-012 · Rörelsen fungerar nu (F-011), men ser hackig och billig ut — orsak inte fastställd

- **Visades:** r7-boarden (port 4625/4626) efter motion-always-fixen, K1 och/eller K2 (Anton
  angav inte vilken cell eller vilken akt specifikt). Mekaniskt korrekt denna gång: rörelsen
  spelade upp oavsett `prefers-reduced-motion`, till skillnad från F-001/F-011:s ursprungsfel.
- **Antons ord:** "scrolleffekten renderade som den skulle, men det såg hackigt och billigt
  gjort ut, nästa agent får analysera närmare /conclude"
- **Dom:** dåligt (visuell känsla), men **orsaken är inte fastställd i den här sessionen** —
  Anton bad uttryckligen att nästa agent gräver i det, inte jag nu. Ingen gissning skriven
  här om vad "hackigt" beror på (frame-rate i push-sekvensen, saknad lerp/easing någonstans
  efter dagens `reduce=false`-patchning, en riktig prestandaflaskhals, eller något annat).
- **Regel:** ingen ännu — det här är en öppen observation, inte en härledd regel. Nästa
  session äger att (1) återskapa exakt vilken cell/akt, (2) mäta (frame-times, `--sc-p`-
  kontinuitet, om `reduce=false`-patchningen i scrollcraft.js/K1/K2 råkade ta bort någon
  smoothing-logik som var villkorad på `!reduce` och nu aldrig körs), (3) skriva den
  härledda regeln som en ny post här när orsaken är känd.
- **Status:** ~~öppen~~ **stängd 2026-09-08 av F-013**, som mätte orsaken i stället för
  att gissa: två fel (värdet stegar; sidan tappar bilder), och F-011 orsakade ingendera.
  Posten står kvar oförändrad ovanför — den var rätt formulerad som en öppen fråga.

### F-013 · F-012 mätt: två orsaker, och ingen av dem var F-011

- **Visades:** ingen board. Det här är en mätning, inte en dom — den stänger F-012:s
  öppna fråga med siffror i stället för hypoteser. Instrument: nytt
  `skills/design/scripts/motion_probe.py`, som driver sidan med ett skriptat hjul
  (100 px var 60:e ms) och loggar bildtid och värdeförändring per frame.
- **Mätt på:** `tests/alunix-concepts-r5/cells/V3b-chain/index.html` (2026-09-08), den
  sida Anton faktiskt tittade på, samt två fixturer som isolerar mekanismen:
  `tests/motion/staircase.html` (rå `--sc-p` → `rotateY`) och `tests/motion/smooth.html`
  (samma rörelse, lerpad).

| Mätpunkt | staircase-fixtur | smooth-fixtur | V3b hero | V3b jätterubrik |
|---|---|---|---|---|
| bildtid p95 | 16,7 ms | 16,7 ms | 140 ms (4× CPU) / 49,9 ms (otrottlad) | samma |
| frames > 33 ms | 0 | 0 | 86 | 62 |
| trappsteg | 18 | **0** | 9 | 16 |
| största steg | 5,6 % | **1,4 %** | 11,8 % | 6,4 % |

- **Orsak 1, värdet stegar.** `scrollcraft.js` dämpar bara två saker: videons
  `currentTime` och pekarens `tilt`/`magnet`. `--sc-p` självt, och därmed all bespoke
  rörelse som läser det, skrivs 1:1 från rå scrollposition i `read()`. På ett mushjul
  betyder det att värdet står stilla mellan hacken och sedan hoppar. Fixturerna visar
  att det inte är bildfrekvensen: **båda kör 16,7 ms p95, bara den råa stegar.**
  Dessutom är `--sc-p` en oregistrerad custom property, alltså en sträng som CSS aldrig
  kan interpolera, och `scrollcraft.css` sätter `transition: none` på cues och copy när
  `.sc-ready` landar — ingenting överbryggar skrivningarna.
- **Orsak 2, sidan är faktiskt långsam.** V3b tappar bilder även otrottlad: p95 49,9 ms
  och 62 frames över 33 ms. `perf_probe.py` mot samma sida ger orsakerna:
  **4,9 MB överföring** (tak 2,5), **19 typsnittsfiler / 732 kB** (tak 3 / 300 kB),
  **17 långa tasks under scroll** (tak 0), vilande `will-change` på fyra element
  (`h1.hero-headline`, `.calyx-wrap`, `h2.giant`, `#projekt`), och bilder utan
  `width`/`height`, `decoding` eller `fetchpriority`. Det är en prestandaflaskhals, inte
  en utjämningsfråga, och den syns som exakt samma ord: "hackigt".
- **Sidofynd, eget regelbrott:** V3b:s tyngsta resurs är en **1,1 MB hero-bild hotlänkad
  från `images.unsplash.com`**. `SKILL.md` Step 5b säger rakt ut att hero-bilden är LCP
  och "must not depend on another company's CDN" — den ska vara nedskalad, WebP och
  vendorad. Ingen granskning hade fångat det förrän överföringen mättes.
- **F-011 orsakade ingendera.** Motordiffen mot uppström är fyra rader.
  `var reduce = false` slog **på** playhead-lerpen (faktor 1,0 → 0,18) och tog inte bort
  någon utjämning; `reduce` gatear tio ställen och alla är avstängningsgrenar.
  F-012:s tredje hypotes är därmed motbevisad mot källan.
- **Regel:** (1) **Bespoke rörelse läser `--sc-ps`, aldrig rå `--sc-p`**, när den driver
  något ögat ser förflytta sig (transform, object-position, clip-path, mask-position).
  Cue-opacitet får läsa `--sc-p`. `--sc-ps` publiceras av
  `skills/design/scripts/scroll/sc-smooth.js`, som kopieras in bredvid motorn (motorn
  redigeras aldrig) och registrerar egenskapen som `<number>` så CSS kan interpolera den.
  (2) **"Ser hackigt ut" är två fel, och båda ska mätas innan något ändras** — takt och
  bildtid. En sida kan hålla 60 fps och ändå stega, och den kan glida perfekt i värdet
  och ändå tappa bilder. `motion_probe.py` rapporterar båda, och en signaturakt är inte
  klar förrän `staircase = 0`, `max_step ≤ 3 %`, p95 ≤ 20 ms och noll frames över 33 ms.
  (3) `will-change` sätts bara medan något rör sig; shimen städar motorns klassbreda
  promoveringar i vila.
- **Efterspel, 2026-09-08:** när `emil-design-eng` kördes över shimen (routern hade
  namngivit den och jag hade hoppat över den, alltså precis r7:s fel) föll tre buggar ut.
  Den allvarligaste: `--sc-ps` registrerades med `inherits: false`, vilket gör att ett
  **barn** som läser `var(--sc-ps)` får `0` i stället för förälderns värde. Akten hade
  stått fryst på varje sida som använde shimen, med ren konsol. Fixturen missade det
  eftersom den inlinade en miniatyr som aldrig registrerade egenskapen. Den laddar nu den
  riktiga filen. Två mindre: `will-change` sattes på akt-behållaren, som inte är elementet
  som rör sig, och värdet skrevs varje frame för varje akt, vilket kostar en
  subträds-omräkning för akter som står stilla. **Och `motion_probe` godkände buggen** —
  ett kort som aldrig rör sig är perfekt jämnt. Därför har proben nu en `DEAD`-kontroll:
  ett värde som inte rör sig alls medan sidan scrollas är ett fel, inte ett godkännande.
  Lärdomen är regeln, inte buggen: **en prob som kan godkänna en död sida är sämre än
  ingen prob**, och båda riktningarna måste bevisas mot samma fixtur.
- **Status:** `scripts/scroll/sc-smooth.js` (ny), `scripts/motion_probe.py` (ny),
  `tests/motion/{staircase,smooth}.html` (fixturer, bevisade i båda riktningarna),
  `tests/alunix-concepts-r5/motion-probe-v3b/` (mätningen sparad). F-012 är därmed
  stängd som fråga; V3b:s egen prestandaskuld är kvar och tas i V3c.
