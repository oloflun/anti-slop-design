# FEEDBACK.md — Antons domar, en regel per post

Läses **alltid** i `design/SKILL.md` Step 1b, tillsammans med `TASTE.md` och `ANTON-VISION-OCH-FEEDBACK.md`
(repo-roten: den breda riktningen, inte domarna), innan Step 2.
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

### F-023 · Copyn ska beskriva vägvalen och låta som en byrå, inte som AI
- **Visades:** V3g R7, showcasens stegtexter: en mening om vad som valdes och en om varför,
  i en ruta per steg.
- **Antons ord:** "Testa att ta bort rutorna och låta texten ta lite mer plats, gör den mer
  visuellt intressant och låt den bli lite längre i 2 stycken, försök även att göra copyn
  mindre 'AI'-ig och mer beskrivande kring själva processen och vägvalen, ta inspiration från
  webbyråerna jag nämnde som referenser från början av Alunix bygget."
- **Dom:** för kort och för tillrättalagd. Varje steg hade samma form.
- **Regel:** case- och processtext skrivs i två stycken: situationen och valet med orsaken
  först (Highway), sedan det som valdes bort eller vad valet kostar, plus en detalj som syns i
  ramen (Hoy). Bortval skrivs som alternativ som fanns, aldrig som händelser i ett projekt som
  inte funnits. Inga värdeord (Insigns "speglar", "stilren"). Alla tre pass körs som skills:
  copywriting, copy-editing, humanizer-svenska. Faktan kontrolleras mot sajtens källkod.
- **Status:** `tests/alunix-r8/runs/V3g/COPY-R8.md`, byggd i V3g R8/R8b.

### F-024 · En enda referens räcker inte som riktning
- **Visades:** V3f R2, hela sidan byggd på Aspen Search ensam efter ett `compare` som gav
  `sameRegister:false`.
- **Antons ord:** "Det ser bra ut, designen är mycket mer unik men den baseras enbart på en
  referens istället för att ta inspiration från flera enligt de instruktioner som ska finnas
  för MCP:n, finns det någon anledning för detta?" Senare: "nästan perfekt på en gång och
  redan bättre och mer unikt än v3d."
- **Dom:** resultatet bra, processen bröt instruktionen.
- **Regel:** `compare` är ett trianguleringsverktyg. `sameRegister:false` är ett skäl att välja
  vilket drag som tas ur varje referens, inte att välja bort alla utom en. Låset anger en
  dominerande referens och minst två lån (komposition, typ, rörelse) med vad som lånas.
- **Status:** `tests/alunix-r8/HANDOFF-V3f.md` § 2 och § 6 steg 1; ska in i `inspo-mcp.md`.

### F-025 · Rörelse får inte stjäla läsningen, och bilder får inte förstoras för att nå ett mått
- **Visades:** V3f R2–R4: tesrubriken drev förbi kanten, `Exempelcase` klipptes, tumnaglar
  uppskalade till 140 vh.
- **Antons ord:** "De stora rubrikerna klipps, 'första intrycket' hinner man knappt se.
  Bilderna på de båda referenssidorna är fortfarande helt statiska och suddigt inzoomade."
- **Dom:** dåligt, generellt.
- **Regel:** varje rubrik står helt synlig, oklippt och stilla i minst 40 vh; rörelse sker före
  och efter. Ett ytmått (t.ex. 30 % bildyta) får aldrig uppfyllas genom att förstora samma
  lågupplösta bild. Referensbilder tas nya, skarpa och utzoomade (2× skala).
- **Status:** `tests/alunix-r8/runs/V3f/RUNDA5-SPEC.md` § A–B; `references/motion.md` läsregel.

### F-026 · En sektion måste ha en tanke, inte bara innehåll
- **Visades:** V3f R5, kontakten: stor rubrik, ett kort och död yta.
- **Antons ord:** "kontaktsektionen måste göras roligare, det finns ingen tydlig tanke där."
- **Dom:** dåligt. Löstes med greppet "kortet lämnas över": heron speglad, kortet vänds av
  besökaren och vänder sig självt vid 70 % scroll.
- **Regel:** varje sektion bär ett grepp som går att säga i en mening. Saknas det är det
  kompositionsproblemet, inte en dekorationsbrist (se F-022).
- **Status:** `tests/alunix-r8/runs/V3f/RUNDA5-SPEC.md` § C. Verifierat i pixlar.

### F-027 · Alunix V3g R9: en egenskap har en ägare, och exempelsidor bär inga riktiga namn
- **Visades:** V3g R8 → R9, Antons nio skärmdumpar 2026-10-03. Problemen: hero-rubriken
  fragmenterad efter scroll ned och upp, tesens stapel bredvid Hyperborea-ramen, showcase-text
  som beskrev det ögat redan ser, rubriker som satt ihop med ingressen, och verkliga person- och
  platsnamn på exempelsidorna.
- **Antons ord:** "ta bort priserna och lägg istället till en beskrivning av de olika paketen";
  "Kör sedan en design-audit på hela sidan utifrån det nya golvet".
- **Dom:** planen (`PLAN-ALUNIX-R9.md`) godkändes och byggdes. Kritikern hittade samma tvåägarfel
  i heron som R9 § 1 hade rättat för raderna (`.hero-nh` clipPath ägdes av både laddnings- och
  scrolltidslinjen). Kritikern fann också `.32`-avståndet för snålt mot x-höjdsregeln, och att
  Calyx-steg 2 påstod "ett enda typsnitt" om en sida satt i Cardo + PT Mono.
- **Regel:** (1) Varje animerad egenskap på ett element har exakt en tidslinje som ägare. En
  scrubbad `.to()`/`.fromTo()` på något som laddningen redan flyttat ger fel läge efter
  tur-och-retur, så scrollrörelsen flyttas till ett annat element (masken, ett inre lager) eller
  tas bort. Kontrollen är scroll ned och upp igen, sedan mätt läge vid scrollY 0. (2) Ingress
  under display-rubrik: `calc(rubrikstorlek * .5)`, så att baslinje till ingress är minst en
  x-höjd. (3) Exempel- och demosidor bär inga verkliga person- eller platsnamn (staden får stå);
  `microtext_scan.py --names` ska ge 0 träffar. (4) Påståenden i case-text kontrolleras mot
  sajtens källkod, även typsnittspåståenden (F-023).
- **Status:** `tests/alunix-r8/runs/V3g/index.html` R9, mätt headless 1440/768/390;
  `house-physics.md` (ägarregeln, x-höjdsavståndet, optisk mitt); `SKILL.md` (namnregeln).

### F-028 · Ändra inget som inte är beställt; copy-gaten skriver inte om godkänd copy
- **Visades:** Alunix V3g R10 (2026-10-03). Byggaren förlängde två godkända rader:
  - "Så berättar vi vad vi kan göra för er." blev "… och föreslår en tid för ett första samtal."
  - "Boka ett möte" blev "Mejla oss för att boka ett möte".

  Den byggde också fler ändringar än Anton beställt: tumnaglar för casebytet, en frimärksbild i
  processrubriken, kantiga mintövergångar och en större hero-rubrik som klipptes under
  topplinjen.
- **Antons ord:** "blir för långt, det var bättre innan. … Ändra inget om jag inte bett om det,
  copy-gaten ska inte omarbeta redan godkänd copy, endast skapa ny där det inte finns eller
  förbättra om det beställs av användaren". Och: "R10 gjorde mer ändringar än jag beställde - Dela
  upp dem i 2 olika flikar - en med enbart vad jag beställde och en med dina kreativa ändringar".
- **Dom:** dåligt.
- **Regel:**
  1. Copy-gaten körs bara på ny text, eller på text användaren bett om att förbättra. Godkänd copy
     ändras aldrig av gaten, en byggare eller en granskare.
  2. En plan som föreslår ändringar i godkänd copy eller layout bygger förslagen först efter ett
     uttryckligt ja per punkt.
  3. Beställt och eget initiativ levereras i separata varianter (två flikar).
- **Status:** `SKILL.md` Step 6 och `references/copy-gate.md` (Scope). Alunix: flik 7 =
  beställt, flik 9 = kreativt.

## 2026-10-18 · Snajp koncept-boarden (`snipe-leads/koncept/`, port 4620), fem landningskoncept

### F-029 · Dygnet är riktningen; rörelsen ska upp till byrånivå och referenserna ska blandas
- **Visades:** boarden med fem koncept för Snajps landningssida: 01 Dygnet (warm photographic,
  dagsljuslager i multiply över ett papper, Newsreader + Rethink Sans, bärnsten), 02 Inkorgen
  (modern clean, delaren), 03 Meningen (typografisk affisch), 04 Katalogen (showroom-hylla),
  05 Kapitlen (kall rapport, ritad horisont). Varje koncept byggt på EN primär katalogreferens.
- **Antons ord:** "Nummer 1 kommer närmast estetiskt, skippa de övriga och bygg 5 nya koncept
  utifrån Nr 1, behåll den i befintligt format. Ta inspiration från nya källor och blanda dem,
  använd inte en för varje och ha fortfarande, ljus, skandinavisk Saas som målbild och öka
  ambitionsnivån ytterligare för animationerna och övergångarna, det ska vara Saas blandat med
  prisvinnande webbagenturer på världsnivå, fortsätt tills det är uppnått och slutversionerna
  alla överträffar sina referenser"
- **Dom:** bra för 01 (estetiken), dåligt för 02–05 (riktningen), och för alla fem: rörelsen
  räcker inte, och en referens per koncept är för tunt (samma sak som F-024).
- **Regel:** (1) För Snajp är Dygnets estetik riktningen: ljust papper i dagsljus, en lätt serif
  med kursivt accentord, varma fotografier av nordiskt ljus, produktytor i hårlinjeramar,
  liggare. Nya koncept är varianter av den, inte nya register. (2) Varje koncept blandar minst
  tre nya källor (en dominant och två lån, F-024), och inget koncept tar samma dominanta källa
  som ett syskon. (3) Rörelsen hålls mot byråsidorna i katalogen (motion_floor 2) och inte mot
  husets golv: varje koncept har en dörr som är en enda tagning, en signaturakt med minst två
  koordinerade lager och minst fyra materiella övergångsorsaker. (4) Rundan är inte klar förrän
  leaden har sett varje koncept bredvid sina referensark och kan säga var det är bättre; går det
  inte att säga, byggs en runda till.
- **Status:** `snipe-leads/koncept/_delat/KONTRAKT-R3.md` (plan på disk); bara här tills det
  visat sig hålla.

## 2026-10-19 · Snajps startsida (localhost:3005), showcase-rutorna och översikten

### F-030 · Ytor glider in på en fjäder; bara texten avtäcks, en yta i taget
- **Visades:** startsidan efter 2026-10-18: showcase-rutorna klipptes fram nedifrån och
  skrubbades samtidigt i y medan sidan passerade, och den isärtagna översikten pinnades.
- **Antons ord:** "Showcase- rutorna är fortfarande laggiga och vibrerar vid scroll, särskilt om
  man scrollar fram och tillbaka. Det är även fortfarande en tonad scroll-reveal, jag vill att
  själva rutorna rör sig in mjukt på skärmen och att enbart den beskrivande texten revealas
  istället, en ruta i taget, inte båda samtidigt. Rörelsen för rutan ska inte vara statisk och
  spikrak, den vara mjuk och glida in stoppa och studsa tillbaka lite, men väldigt subtilt, tänk
  apple"
- **Dom:** dåligt. Orsaken till vibrationen var mätbar: en CSS-transition (`.rise`) på samma
  `transform` som GSAP skrubbade varje bildruta.
- **Regel:** en yta tonas eller klipps aldrig fram. Den glider in från sin sida på Apples fjäder
  (apple-design § 4, dämpning ~0.75, respons ~0.75 s), passerar målet några pixlar och fjädrar
  tillbaka; först när den landat avtäcks dess beskrivande text rad för rad. En yta i taget
  (kö). Ankomsten spelar en gång och skrubbas aldrig, och ingen CSS-transition får ligga på en
  egenskap GSAP skriver.
- **Status:** `SKILL.md` § The craft floor (Motion-punkten "Objects arrive on a spring");
  Snajp: `DESIGN.md` § Ankomstfjädern, `gsap.js: spring`. Värdena ersatta av F-031.

## 2026-10-19 · Snajps startsida, polering i tre varv (commits `125cc38`, `6c478d1`, `57914a6`, `79d93cb`)

Varje post nedan har en skill i `~/.agents/skills/` som bär beställningen, det som föll,
ändringen och det godkända läget med värden: `spring-arrival`, `hero-on-photo`,
`live-text-reveal`, `photo-stands-whole`, `showcase-surfaces`, `showcase-copy-scope`,
`count-up-in-view` och processen `motion-verification-preview`. Routingtabellen
(`component-routing.md`) pekar på dem när liknande kod skrivs.

### F-031 · Studsen ska synas: `spring(0.66, 0.95)`, inte 0.75/0.75
- **Visades:** startsidan 2026-10-19 efter F-030: rutorna gled in på `spring(0.75, 0.75)`,
  cirka 3 % förbi målet (omkring 5 px på rutans inglidning), 1,1 s till vila.
- **Antons ord:** "Gör även animeringarna för rutorna jämnare och mjukare, och gör
  studsseffekten/tillbakafjädringen tydligare."
- **Dom:** hade kunnat bli bra om studsen syntes. "Subtilt" i F-030 betydde inte
  teatraliskt, inte osynligt. Godkänt efter ändringen: "ändringarna kom in precis som jag
  ville".
- **Regel:** ankomstfjädern är `spring(0.66, 0.95)`: cirka 6 % förbi målet (omkring 11 px
  på rutans inglidning), cirka 1,6 s till vila, mjukare och längre glidning. En studs under
  cirka 5 px räknas som ingen studs. Riktningen i F-030 står; värdena ersätts.
- **Status:** `SKILL.md` § The craft floor (Motion-punkten), skillen `spring-arrival`,
  Snajp `DESIGN.md` § Ankomstfjädern.

### F-032 · Ingen skugga bakom hjältetexten; ett band i fotot, mätt
- **Visades:** startsidan 2026-10-19: en oval mörkning bakom ingressen för läsbarheten på
  mobil.
- **Antons ord:** "Testa göra skuggan i heron svagare, eller skippa den helt."
- **Dom:** dåligt. Mörkningen syntes som en skugga, ett föremål bakom texten, inte en del av
  fotot.
- **Regel:** text på ett foto får aldrig en form bakom sig. Räcker fotot inte (ingressen
  under 4,5:1 mot horisontens ljusaste 5 % på 375 px) läggs ett mjukt band i fotot med
  scrimmens ton (`.hero-band`, 0 → 0,48 → 0 över bandet) och höjs tills mätningen håller:
  0,42 gav 4,29:1, 0,48 gav 5,32:1. Ingressen är helt papper med en mjuk textskugga, aldrig
  dämpat papper ("knappt läsbar mot herobilden", 2026-10-19 morgon).
- **Status:** skillen `hero-on-photo`; Snajp `DESIGN.md` § Measured floors.

### F-033 · Agenttext skrivs fram live, vid varje knapptryck; motiveringar på vanliga ord
- **Visades:** startsidan 2026-10-19: showcase-rutornas utkast avtäcktes rad för rad; demons
  omskrivningar byttes ut på en gång; panelen visade motiveringar med principer, filer och
  "CTA"; varje knapp på startsidans exempelmejl svarade att demot bara fanns för
  /demo-bolagen.
- **Antons ord:** "Skapa även effekten att texten skrivs live, för alla
  omgenereringar/knappval också, ta även bort alla tekniska referenser, endast korta
  motiveringar."
- **Dom:** dåligt. Demon ska kännas som att agenten skriver, och motiveringen läses av en
  kund, inte av en utvecklare.
- **Regel:** text som en agent skriver (utkast, svar, motivering) skrivs fram med markör,
  cirka 8 ms per tecken klämt till 0,7–2,6 s, efter att rutan landat, vid varje knapptryck.
  Motiveringen är en kort mening på vanliga ord: prompten ber inte om referenser och en spärr
  i kod stryker dem ändå. Varje demoknapp ger ett eget genererat svar, aldrig en reservmening
  om demot. Skärmläsaren får hela texten direkt (`sr-only`), framskrivningen är
  `aria-hidden`.
- **Status:** skillarna `live-text-reveal` och `showcase-copy-scope`; Snajp `lib/skrivs.ts`,
  `LiveText`, `lib/textkvalitet.ts: utanReferenser`.

### F-034 · Ett betonat ord i hjälterubriken, sist, i en accent som syns mot fotot
- **Visades:** /support 2026-10-19: rubriken `*Support 24/7*`, hela i accent. I första
  rättningen: 7:an i `text-warning` (OKLCH L 0,50), osynlig mot solnedgången på desktop fast
  DOM sade att den renderades.
- **Antons ord:** "Hela herotexten för support är i färg, gör så att enbart 7:an är det."
  Och: "med betoning på sover, samma med Support, men byt det till: Era kundärenden
  hanterade, 24/7".
- **Dom:** dåligt (hela rubriken i färg). Accentens ljushet upptäcktes av agenten i en zoomad
  skärmbild innan push.
- **Regel:** ett ord eller en siffra betonas, sist i meningen, i den ljusa accenten
  (`text-ochre`, L 0,74), aldrig den mörka (`text-warning`, L 0,50). Synligheten kontrolleras
  med zoomad skärmbild på desktop mot fotot, inte med DOM.
- **Status:** skillarna `hero-on-photo` och `live-text-reveal`; Snajp `copy.ts`.

### F-035 · Foton står hela; en avtäckning läses som långsam laddning
- **Visades:** startsidan 2026-10-19: bildplattorna klipptes fram från vänster eller
  nedifrån (`clip-path`, 1,2 s), fotobanden skrubbades fram uppifrån.
- **Antons ord:** "Gör även så att bilderna laddas hela, nu ser det ut som att de renderas,
  som att sidan laddas långsamt."
- **Dom:** dåligt. En svepande avtäckning över ett fotografi ser ut som en bild som avkodas
  rad för rad.
- **Regel:** ingen `clip-path`, mask eller skrubbad klippning på ett element som innehåller
  ett foto. Rörelse på ett foto är drift i ramen: parallax, långsam skala. `reveal`
  (devices #4) är för konstruerade ytor och band utan bild.
- **Status:** skillen `photo-stands-whole`; `scroll/devices.md` § 7-noten.

### F-036 · En skärmdump bredvid konstruerade ytor är ett annat material; ytorna fyller rutan på desktop
- **Visades:** den isärtagna översikten (en skärmdump i fyra delar, beställd 2026-10-18 och
  rättad i tre rundor för hack tills den stod stilla på p95 17 ms) och showcase-rutorna med
  mobilens typskala på 1920 px.
- **Antons ord:** "Ta även bort hela dashboard-sektionen, den tillför inte något i nuläget och
  skiljer sig från de konstruerade rutorna." Och: "Gör även texten i rutorna större i desktop
  och låt den fylla upp dem mer".
- **Dom:** dåligt. Rörelserättningarna var rätt men ändrade inte materialet: raster, egen
  chrome och 9 px text bredvid handbyggda rutor i sidans typografi.
- **Regel:** produktytor på marknadssidan är konstruerade (JSX, exempeldata, produktens
  tokens) i en familj, aldrig skärmdumpar. På desktop fyller innehållet rutan: `zoom` 1,12
  från 1280 px och 1,25 från 1536 px, `min-height` delad med zoomen så rutan behåller sin
  höjd; under 1280 px orört.
- **Status:** skillen `showcase-surfaces`; Snajp `.case-zoom`, `DashboardIsar` borttagen
  (commit `6c478d1`).

### F-037 · Delad copy skalas per produktsida
- **Visades:** /support 2026-10-19: "Varför Snajp finns"-styckena, delade med /vart-team,
  började med "B2B-prospektering är tidskrävande …".
- **Antons ord:** "Se även till att texten för Om oss-sektionen på supportsidan inte
  innehåller massa leads-referenser."
- **Dom:** dåligt.
- **Regel:** ett delat textblock läses på varje sida det visas. Nämner det den andra
  produkten görs en variant per produkt (`varforSupport`) och väljs på `product`. Båda
  språken i samma commit.
- **Status:** skillen `showcase-copy-scope`; Snajp `copy.ts`, `LandingPhoto.tsx`.

### F-038 · Hjälterubriken skrivs fram långsammare än rutorna, med paus före det betonade ordet
- **Visades:** startsidan 2026-10-19 efter F-033: rutornas text skrevs fram, hjälterubriken
  radmaskades fortfarande.
- **Antons ord:** "Gör även så att hero-texten skrivs ut på samma sätt som rutan, fast
  långsammare och mer effektfullt, med betoning på sover"
- **Dom:** beställning, godkänd efter en rättning ("Allt är jättebra nu"). Första bygget hade
  en `prefers-reduced-motion`-spärr som i Antons miljö (`reduce`) aldrig lät rubriken skrivas;
  F-011 gäller, spärren togs bort innan push.
- **Regel:** rubriken skrivs 58 ms per tecken, +260 ms efter kommatecken, +650 ms före det
  betonade ordet, som skrivs 140 ms per tecken; markör i textens färg som blinkar; start när
  dörren öppnat och fonterna laddat, reserv efter 4 s; ingen preferensspärr; `sr-only` hel
  text. Ersätter radmaskningen för hjälterubriken: SplitText och framskrivning delar aldrig
  element.
- **Status:** skillen `live-text-reveal` (`HeroText`); Snajp `DESIGN.md` § Motion.

### F-039 · Tal räknas fram först när de står helt i bild, och inte för fort
- **Visades:** resultatvyns nyckeltal 2026-10-19, första bygget: `IntersectionObserver` med
  threshold 0,6, 250 ms + 160 ms per tal, 1,6 s, kubisk utbromsning.
- **Antons ord:** "Kan du göra så att dessa siffror 'genereras' i realtid när man kommer
  dit?" och sedan: "De är helt fulladdade vid scroll och genereras endast snabbt vid
  sidladdning om man redan befinner sig där, vilket man inte gör, det måste ske naturligt vid
  scroll och när de är helt i bild, det får inte gå för snabbt"
- **Dom:** dåligt. Räknaren startade när talet stack upp vid nederkanten, medan raden tonades
  in, och var klar innan den syntes. Agentens verifiering hoppade direkt till raden mitt på
  skärmen och kunde inte falla. Godkänt efter ändringen: "Allt är jättebra nu".
- **Regel:** en räknare startar när hela talet står ovanför skärmens nedersta femtedel
  (`threshold: 1`, `rootMargin` −20 % i botten), 450 ms efteråt (intoningen klar), ett tal i
  taget med 280 ms mellan, 2,6 s per tal, kvadratisk utbromsning. Bredden reserveras med det
  färdiga värdet; enhet och decimaler följer med; `sr-only`. Ersätter devices.md § 7 ("fires
  at half visibility", "1,2–1,8 s") på sidor där raden själv tonas in. Verifiering: kom
  nedifrån, läs 0 vid nederkanten, skrolla upp, skärmbilder vid 0/1/2/3,5 s med fliken
  fronted.
- **Status:** skillarna `count-up-in-view` och `motion-verification-preview`;
  `scroll/devices.md` § 7; Snajp `RaknaUpp` i `AgentResultat.tsx`.
