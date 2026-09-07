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
- **Status:** öppen. Ingen fil ändrad för den här posten. Se `plans/2026-09-03-design-
  rework-v3.md` "In Progress" för handoff-raden till nästa session.
