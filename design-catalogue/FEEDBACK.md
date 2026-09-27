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

### F-014 · Ungated-tier auto-arm kan aldrig fånga kedjans egna exempelsajter

- **Visades:** Stop-hooken på orkestrerarsessionen själv, 2026-09-09: "12 UI-filer
  ändrade utan armad designsession (ingen rapport)". Verifierat mekaniskt exakt: sju
  `sites/*.html` (F-011-saneringen) och fem `skills/design/scripts/*.py`
  (rörelsegrind-fixen, F-013:s uppföljning) — allt riktigt arbete, tidigare noggrant
  testat åt båda hållen av den agent som utförde det, men osynligt för kedjans egen
  mätning.
- **Första hypotesen var fel, och det är värt att skriva ner varför.** Antog att
  `Agent`-subagenter kör i egna sessioner utan delad ledger. Testat empiriskt: en
  dispatchad subagent läste tillbaka **exakt** samma `CLAUDE_CODE_SESSION_ID` som
  föräldern (`echo $CLAUDE_CODE_SESSION_ID` gav identiskt värde i båda). Ledgern
  (T1:s session-scopning) delas alltså redan korrekt mellan förälder och
  dispatchad subagent — det är inte ett sessions-scoping-problem.
- **Den verkliga orsaken:** `hooks/design-route.py`s auto-arm-gren kräver
  `tier(root) == "0-locked"` (rad ~76: `auto_arm = (not was_armed and tier ==
  "0-locked" and strong_routes and ...)`). `anti-slop-design`-repot har ingen
  `DESIGN.md` — `L.tier(Path('.'))` ger **"ungated"**, bekräftat direkt. Det är
  korrekt för en klientsajt utan låst kontrakt (ingen kan auto-arma bara på en
  routningsträff), men träffar precis så här: kedjans EGNA `sites/*.html` —
  exemplen andra sessioner läser som referens — ligger i samma ogaterade repo och
  kan därför **aldrig** auto-arma, oavsett hur stark routningsträffen är. Arming
  kräver i stället antingen ett `UserPromptSubmit` klassat som designintent
  (`design-intent.py`) eller ett explicit `Skill(design)`-anrop
  (`design-telemetry.py`) — ingen av de vägarna körs av en dispatchad
  `Agent`-subagent, och orkestreraren laddade själv aldrig skillen.
- **Regel, föreslagen men inte verkställd:** mekanismen fungerar som avsedd för
  klientprojekt; gapet är specifikt att repots EGNA `sites/`-mapp aldrig kan nå
  `0-locked`. Två vägar, ingen byggd: (a) varje session som redigerar `sites/*.html`
  eller `skills/design/scripts/*.py` instrueras/kontrolleras att explicit köra
  `Skill(design)` eller motsvarande innan skrivning, oavsett tier; (b)
  `design-route.py` får ett uttryckligt undantag som auto-armar på en stark
  hantverksroute även vid `tier == "ungated"` när sökvägen ligger under `sites/`
  i det egna repot (repots demosajter är per definition "på riktigt", inte en
  ogaterad kundmapp). Nästa session som rör kedjan äger att välja och bevisa vald
  väg åt båda hållen (en icke-triggande redigering nekas fortfarande att passera
  ogranskad; en riktig routningsträff mot `sites/` armar).
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

## 2026-09-15 · r8-boarden (port 4626), K4 Delaren dömd som mönster, inte som sida

### F-015 · Före/efter-delaren är ett referensmönster, inte ett helsideskoncept
- **Visades:** K4-r8 på boarden, hela sidan: den tippande delaren mellan
  `sites/before-ai-slop.html` och Calyx, R3-läget med plan 004 öppen.
- **Antons ord (ur beställningen 2026-09-15, återgivet):** K4-slidern från förra sessionen
  sparas som referens för den typen av före/efter-showcase, inte som helsideskoncept.
  Huvuduppgiften är i stället K3:s ritning som processakt i V3-sidan.
- **Dom:** hade kunnat bli bra som del, inte som helhet. Delaren som mekanik håller
  (två hela sidor i miniatyr, ps 0,40 med Calyx som vyns största objekt, verified i R3);
  som bärande idé för en hel byråsida räcker den inte.
- **Regel:** en showcase-mekanik som bevisar ett påstående (före/efter) är ett
  *mönster* i katalogen av egna akter, inte ett koncept. Den får återanvändas som en
  sektion i en sida vars grammatik bär den; den bygger ingen sida ensam. K4-cellen
  parkeras som det mönstret, med sin BRIEF, NOTES och `?preview=`-lägen som
  referensmaterial. Plan 004 (bildtexten klipps under 640) förblir öppen och stänger
  inte cellen, eftersom cellen inte längre ska skeppas.
- **Status:** bara här, plus raden i `tests/alunix-r8/STATUS.md` och `runs/K4/NOTES.md`.

## 2026-09-19 · Antons stående förbud, ingen board — läst direkt av Alunix-sidan

### F-016 · Liten "beskrivande" stiltypisk AI-text är helt förbjuden
- **Visades:** ingen board. Antons ord är ett stående beslut, inte en dom över en
  körning, men han pekade konkret på Alunix-sidan (`tests/alunix-r8`): små
  kickers/eyebrows ("EXEMPELCASE", "FRÅN EXEMPEL TILL ER SIDA", "SÅ GÅR DET TILL"),
  bildtexter ("Exempelsida: Hōrai, Asian fusion-koncept", "Exempelsida: Calyx, florist
  i Stockholm"), sidomenyer som listar stegrubriker i liten grå text, och små
  förklarande rader under rubriker i liten storlek ("Första steget är ett samtal om
  vad ni gör.").
- **Antons ord:** "All sån liten 'beskrivande' stiltypisk AI-text är härmed helt
  förbjuden och jag vill att designsystemet härmed aktivt arbetar emot det och kollar
  efter det i befintliga sidor."
- **Dom:** dåligt, generellt — inte begränsat till Alunix-cellen som visade det.
- **Regel:** ingen liten text vars enda jobb är att fylla, förklara det uppenbara,
  eller se designad ut. Testet: gör raden ett jobb läsaren behöver (identifierar,
  differentierar, lokaliserar eller möjliggör en handling), eller talar den bara om
  sidan/exemplet i mindre storlek än brödtexten? Det senare tas bort. Antons uttryckliga
  undantag: en sajts egen genre-apparat som är stilenlig OCH bär en funktion i den
  genren är inte utfyllnad — Calyx tidskriftsapparat (utgåva, löpnummer, plats-index)
  och Hōrais avsiktliga etiketter (rätt-namn, servis-nummer) identifierar verkliga
  saker på riktiga sajter i den genren; en digital byrås demo-sida i Alunix genre har
  ingen sådan licens.
- **Status:** portad till `anti-patterns.md` § Descriptive microtext (gate 99),
  `production-tells.md` gate 99, `gates.md`, SKILL.md § Apparatus (marknadssidor:
  default noll), kontroll `skills/design/scripts/microtext_scan.py`,
  `design-catalogue/MICROTEXT-AUDIT.md`.

### F-017 · Prisliggarens displaystorlek är bara för siffror, inte för texten bredvid
- **Visades:** ingen board — samma session, prisliggarmönstret i katalogen
  (`house-physics.md` § Ledger, redan i bruk i Calyx/Hyperborea).
- **Antons ord (parafraserat i beställningen, samma dag):** displaystorlek i en
  priskolumn är bara för siffror (kompakta figurer som bildar rytm); text i samma
  kolumn ("Pris vid förfrågan") sätts ett steg mindre och linjeras mot siffrornas
  baslinje; en kontaktrad storleksätts som en handling, inte som en rubrik.
- **Dom:** regel, inte ett fel som redan visats — katalogens befintliga ledgers
  (Calyx, Hyperborea) skrevs redan så (siffra i display, valuta i kicker), men
  regeln stod inte skriven separat från valutaetiketten, så en textrad ("Pris vid
  förfrågan", "Kontakta oss") kunde av misstag ärva samma display-storlek som
  priset. Skrivs ner nu så nästa bygge inte chansar.
- **Regel:** i en ledger-rad bär enbart siffercellen display-storleken; en textcell i
  samma kolumn (`"Pris vid förfrågan"`, en enhet, en villkorstext) sätts ett
  typografiskt steg mindre än siffran och baslinjelinjeras mot den, aldrig
  samma storlek. En kontaktrad (telefon, mejl, boka-länk) storlekssätts som en
  handling — knapptext- eller länkstorlek — aldrig som en rubrik.
- **Status:** portad till `house-physics.md` § Ledger, never card grid, kontrollen
  `microtext_scan.py --price-ledger`.

### F-018 · Sidan får aldrig berätta vad den strax ska göra
- **Visades:** boardgranskning 2026-09-20, Alunix V3d (`tests/alunix-r8`), ingressen
  under kapitelrubriken Exempelcase: "Calyx är en florist i Stockholm och Hōrai en
  restaurang. Ingen av dem finns, men sidorna är färdiga. Vi går igenom vad vi valde i
  dem och varför."
- **Antons ord:** "är återigen helt hjärndött, och precis samma AI-slop som jag
  reagerade på tidigare."
- **Dom:** dåligt, generellt. Samma familj som F-016, men en annan storlek: detta är
  brödtext, inte småtext, så `microtext_scan.py` ser den aldrig.
- **Diagnos, tre drag som bär felet:**
  1. **Färdplanen.** "Vi går igenom vad vi valde i dem och varför" beskriver sidans
     egen disposition. En läsare som ser en case-sektion vet redan att den innehåller
     case; raden talar om formen i stället för att säga något.
  2. **Brasklappen.** "Ingen av dem finns" ber om ursäkt för arbetet innan det visats,
     och sänker det läsaren just ska bedöma.
  3. **Uppställningen.** Formen uppställning → brasklapp → färdplan är LLM-default för
     "introducera ett avsnitt" och känns igen på sitt tempo, inte på sina ord.
- **Regel:** ingen text på sidan refererar till sidan. En ingress, en kicker eller en
  inledande rad handlar om verksamheten, arbetet eller läsarens fråga — aldrig om vad
  avsnittet nedanför innehåller, i vilken ordning det kommer, eller varför det finns.
  Ingen brasklapp om materialets status före materialet. Testet: stryk raden och se om
  läsaren tappar något annat än en beskrivning av det hen ändå ser. Gör hen inte det,
  var raden utfyllnad — och ett avsnitt som bara har en rubrik ska hellre sättas så att
  rubriken bär ensam än förses med en ingress som fyller ut.
- **Status:** portad till `anti-patterns.md` § Descriptive microtext (ny underrubrik
  § The page narrating itself), `production-tells.md` gate 99, `gates.md` gate 99,
  `skills/design/references/copy-gate.md`.

## 2026-09-25 · r8-boarden (port 4626), V3g "Rutverket · mjuk showcase" runda 2

### F-019 · Textrutans rubrik får inte ta över
- **Visades:** V3g R2, showcasens textruta på desktop med stegrubriken i cirka 120 px
  (`En mening som saktar in`, `Ett mejl räcker`) över ett stort skuggat stegtal (`03`, `05`).
- **Antons ord:** "showcasen är bättre men rubriken är alldeles för stor och ger inte önskad
  effekt, det tar över på ett dåligt sätt, testa en annan layout på texten men behåll
  mekanismen."
- **Dom:** mekanismen bra (övertoning, räknare, mintspår), typografin i rutan dålig.
- **Regel:** i en ruta som följer en levande sajt är sajten huvudsaken och texten
  bildtexten. Stegrubriken står i rubrikskala (h3, ungefär 28–32 px), inte i displayskala.
  Rutans tomma yta fylls med innehåll, aldrig med förstorad text eller jättesiffror, och
  aldrig med ornament (se F-022, som upphäver den tidigare formuleringen "fylls med struktur").
- **Status:** V3g EFFECTS.md, runda 3-briefen.

### F-020 · Scrollen går för fort, och mjukheten får inte offras för farten
- **Visades:** V3g R2, hela sidan med Lenis-standard (ett hjulsteg = 100 px) och hero-pinnen
  `+=120%`.
- **Antons ord:** "när man scrollar ned en gång på hjulet så hoppar man ned från toppen av
  sidan och kastas förbi kortet så man knappt hinner se det vändas … tvinga sakta ned
  scrollen … var extra noga med att se till att den är mjuk och jämn hela vägen." Om
  showcasen: "den hoppar ned för sidan väldigt hastigt mellan texterna."
- **Dom:** dåligt, generellt.
- **Regel:** husets tempo är `wheelMultiplier: 0.6`, `lerp: 0.075`. En pin vars innehåll
  läsaren ska se ske spänner minst 200 vh. Den inbäddade sajten glider mellan ankare över
  större delen av segmentet, aldrig i ett ryck. Allt verifieras jämnt med `section_probe.py`.
- **Status:** `references/scroll/devices.md` § Load-bearing rules.

### F-021 · En bra effekt försämrades av en ändring någon annanstans
- **Visades:** V3g R2 mot V3f. Tesrubriken "Det första intrycket är digitalt." var orörd i
  koden men märkbart mer statisk och ryckig.
- **Antons ord:** "var också bättre förra rundan, nu är den mer statisk och ryckig. Ta reda
  på anledningen … systemet får inte ta fel på bra effekter och göra de sämre, agenterna
  måste ha tydliga instruktioner och riktlinjer för vad som är bra."
- **Grundorsak (mätt):** iframes i en pinnad scen laddades om vid varje
  `ScrollTrigger.refresh()`, eftersom pin-spacern flyttar dem i DOM:en. Varje omladdning bad
  om en ny refresh, och loopen gick hela besöket: 6–12 omladdningar per iframe per pass.
  Felet fanns redan i V3f. R2 förladdade den andra sajten och dubblade kostnaden, och tesens
  p95 gick från 33 till 50–100 ms.
- **Regel:** godkända effekter skyddas. De står i körningens `EFFECTS.md` med en uppmätt
  signatur. Varje runda kör `section_probe.py` på HELA sidan mot baslinjen, och en sektion
  som blivit sämre blockerar rundan även om ingen rad i den ändrats. En iframe i en pin
  kräver en egen `pinSpacer`, och en refresh anropas aldrig från en iframes `load`.
- **Status:** `references/motion.md` § Approved effects are protected,
  `references/scroll/devices.md`, `scripts/section_probe.py`.

### F-022 · Dekorativa streck läses som ofärdig kod
- **Visades:** V3g R4–R5, showcasens textruta med en lodrät "stegskala" (tunn linje, fem–sex
  streck, glidande mintmarkör) som skulle bära rutans höjd. Specen var leadens egen (R3), och
  leaden godkände den själv på skärmbild.
- **Antons ord:** "Hur godkändes de gröna strecken? Det ser ut som något ofärdigt som släppts
  igenom koden. Det räcker med att flytta upp stycket istället, men hela utseendet på det ser
  fortfarande för platt ut, lös det."
- **Dom:** dåligt, generellt.
- **Regel:** ett element som inte bär innehåll och inte är ett godkänt husgrepp (rastret,
  cellnätet, mintlinjen som markering) byggs inte för att fylla yta. Tom yta är ett
  kompositionsproblem: flytta innehållet, eller ge ytan riktigt innehåll (bild, detalj ur
  arbetet). "Det syns i alla fall" räcker inte som godkännande. Leadens egen spec granskas med
  samma fråga som byggarens: skulle Anton se det här som färdigt?
- **Status:** V3g runda 6-briefen; `references/motion.md` § Approved effects (leaden är inte
  undantagen).
