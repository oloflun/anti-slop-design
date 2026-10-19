# Alunix r9, runda 11. Cell {{KONCEPT}}. Helhetsloopen, runda 5: EN plan, och den stänger inget fynd.

Samma session, samma cell. **Läs det här stycket innan något annat.** R10 togs som runda och
helhetsloopens runda 5 (arkitekten, `{{UT_MAPP}}/NOTES.md` § Loop 5,
`reviews/loop-5-astra.md`) nådde loopens slutvillkor: Astra svarade `ship` med **noll**
`material_fixes`, 29 av 35 rader i `{{UT_MAPP}}/HELHET.md` § 3 är bockade, och de sex öppna
är exakt de som inte kan bockas i loopen (H-02, H-03 och H-08 väntar på Anton via Q30; H-21,
H-22 och H-32 är bildtidens redovisade arkitektoniska golv, och varje fönster mäter lika med
eller bättre än loop 4:s redovisade tal). Smoothness-grinden är grön i båda riktningarna.

**Din runda finns därför inte för att laga något.** Den finns för en beställning från Anton
2026-09-17: han vill se processakten **inverterad** och lägga den bredvid pappersversionen.
Du bygger ett läge, inte en ändring: `?process=invert`, ett additivt CSS-block, en token, en
rad JS. Allt annat på sidan ska komma ut på andra sidan rundan **exakt som det gick in**.
Din viktigaste mätning i den här rundan är inte att det nya läget är snyggt, utan att det
gamla är oförändrat.

En plan: `{{UT_MAPP}}/plans/045-processakten-inverterad.md`. Ut-mapp `{{UT_MAPP}}`, port
{{PORT}}.

## 0. Läs först

1. `{{UT_MAPP}}/plans/README.md` § R11: varför rundan finns och vad som ligger utanför den.
2. `{{UT_MAPP}}/plans/045-processakten-inverterad.md` i sin helhet, inklusive avsnittet
   "Villkoren, Antons ord, som mätbara krav" (a till e) och "Vad jag själv ser i pixlarna,
   för och emot". Planen bär radhänvisningar mot R10-filen (md5 `d3491b4a`); hitta varje
   ankare med `Grep` innan du redigerar och STOPPA (skriv i NOTES § R11) om koden inte
   matchar i sak.
3. `{{UT_MAPP}}/HELHET.md` § 3 (golvet H-01 till H-35 med arkitektens loop 5-rader) och § 4
   (tilläggen T-1 till T-8). Du bockar ingen rad; du får inte sänka någon.
4. `{{UT_MAPP}}/reviews/loop-5-astra.md` § `keep` först, sedan `reviews/loop-4-astra.md`,
   `loop-3-astra.md`, `loop-2-astra.md`, `loop-1-astra.md` och `reviews/r5/` (`keep` i var
   och en: `keep` är det du inte får riva). Loop 5:s `keep` är särskilt tät, för den är
   listan över vad som nyss nådde golvet.
5. `{{UT_MAPP}}/PROCESS-UNDERLAG.md` § 3: stegens copy v1 är låst för dig; copy-gaten körs
   av en copy-agent efter loopen. Rör inga strängar, i inget läge.
6. `Skill(design)` (verbet build, komponentskop) FÖRE ändringen. Via `Skill`-verktyget,
   namngivet i transkriptet. `Skill(animate)` och `Skill(emil-design-eng)` behövs INTE:
   planen rör ingen rörelse, och om du tror att den gör det har du missförstått den.
7. `~/.claude/skills/design/references/color.md` (värde per grund: "Every muted tone needs a
   value per ground", som är precis vad villkor b och c mäter) och `gates.md` § 48 och § 60
   (token, aldrig inline-hex, aldrig ett värde ur en demoterad skill).
8. `{{UT_MAPP}}/shots/loop-5/scripts/`: `previews4.py` (previewlägena med `--sc-ps` mot
   `--eN` per steg), `slices4.py` (skivor med plain `scrollTo` och 3 s väntan),
   `geom5.py` (geometri och pixelmätning), `devices5.py` (beräknad matris per device),
   `probes5.sh` (probmatrisen med kontrollprotokollet), `walkproc5.py` (aktens vandring i
   båda riktningarna). Kopiera till scratch och kör därifrån; skriv aldrig i skill-filerna.
   `previews4.py` och `slices4.py` tar URL som argument, så samma skript ger båda lägena.

## 1. Utför

Plan 045, hela vägen: Problem → Target → Conventions → Steps → Boundaries → Verification.
Utfall i transkriptet och i NOTES § R11: `verified`, `best-effort` (med vad som återstår)
eller `reverted` (orsak). Aldrig `verified` på känsla. Kirurgiska `Edit`-anrop, aldrig
`Write` av hela filen, aldrig shell-skrivningar mot UI-filer.

**Planens hårdaste gräns, upprepad här:** ingen befintlig CSS- eller JS-rad utanför
`:root`-tokenlistan och `?preview=`-blocket redigeras. Blocket är additivt. Verkar en fix
kräva en ändring i pappersvägen: STOPPA och rapportera, för då är jämförelsen inte längre
mellan samma sida i två lägen, och då är hela rundans syfte borta.

Motorn `scroll/scrollcraft.js`, `scroll/scrollcraft.css`, `scroll/sc-smooth.js` och
`sites/*` rörs aldrig. Rör aldrig det som står i rapporternas `keep`: `--sc-ps`-kontraktet
(staircase 0, LERP 0,16, DEAD 0,0005, `inherits:true` på `--sc-ps`), den konstanta
dokumentgeometrin (042), Calyx öppning uppifrån med utraderande transformer (043), den
geometrihärledda `driftHand` (044), `will-change` bara via klass, sticky som enda
höjdmekanism i processakten, `pathLength="1"` med `*1px`, `@property`-raderna, iframes
`inert` + `pointer-events:none`, `<ol>` med text i DOM, reveal på wrappern (aldrig på
ramen), ramarna orörda efter att de visats, `.ground`s `contain:strict`, `--c-graphite`,
A-glyfen, kortets span 3,4 / fönster 0,10 till 0,78, gridankaret (034 A), prosan synlig
(034 B), observern på wrappern (027), `is-asleep` via `f.closest('.frame-wrap')` (036),
latchen med exakt 1 och aktobjekt per tick (035), Hōrais kvadratiska iris och
`measureFrames()` (036 A), monteringen i heroens svans (036 B), `aimPreview` med
generations-id (037), lägena ur shimens `cur` (039), konturen 0 till 0,30 (040), 24 % (038),
driften på `.ground` med stoppen ur `:root` (041).

Tillägg och färger: **exakt en ny token**, `--c-accent-on-dark`, i `:root`, med ett mätt
värde och en ledgerrad. Ingen annan ny token. Ingen inline-hex (gate 48), inga värden ur
demoterade skills (gate 60). Låst copy (femton strängar) rörs aldrig, inte heller med
`&shy;`. Noll tankstreck. Inga tal utöver ritningens mått och de låsta priserna. Ingen ny
`filter`, ingen `invert()`, ingen `mix-blend-mode`.

## 2. Grinden efter planen, i din session

Servern `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten. Kontrollprotokollet gäller (`tests/motion/smooth.html` först, ren kontroll
omedelbart före varje sidmätning; ger kontrollen en ruta > 33 ms: vänta en minut och kör om;
ger den fortfarande brus efter två försök mäts sidan ändå och kontrollens tal skrivs
bredvid).

Grinden har två halvor. **Halva A bevisar att pappersläget är oförändrat** och är den
viktigare. **Halva B mäter det nya läget.**

### A. Pappersläget, utan `?process=` i URL:en

1. **Renderidentitet.** `getComputedStyle` på `.process`, `.process-title`, `.process-lead`,
   `.process-p`, `.process-note`, `.ledger-body p`, `.ledger-num`, `.giant-sub`, `.measure`,
   `.contour`, `.dimline` och `.principles`: skriv ut `color`, `background-color`, `fill`
   och `stroke` **före och efter** din ändring, sida vid sida. Varje par ska vara identiskt.
   Ett enda par som skiljer sig är ett STOPPA-villkor.
2. `motion_probe.py`, spår `section.hero:--sc-ps,.plate-card:transform` (40 ticks från
   toppen), `#process:--sc-ps` (`--ticks 45`, start 4 700 ned, 9 100 upp),
   `#giant-section:--sc-ps` (start 2 700, 28 ticks), `.price:--sc-ps` (start 3 873, 18
   ticks), `.panel-thesis:--sc-ps` (start 2 322, 18 ticks), `footer.close:--sc-ps` (start
   8 200, 18 ticks); `--wheel 100:60` och `--wheel 20:120` för hero och process, båda
   riktningarna; **cpu 1 OCH cpu 4**. Bar: staircase 0 överallt; `--sc-ps` max_step ≤ 3 %
   vid cpu 1 på varje akt (loop 5: hero 1,25 till 1,37, process 0,67 / 0,76, jätten 2,65,
   tesen 2,31 till 2,90, priset 2,33, avslutet 2,66); p95 inte sämre än loop 5:s tal
   (`NOTES.md` § Loop 5, tabellen; cpu 1 hero median 33,6, process 17,1 / 17,0, jätten 50,2,
   priset 46,7, tesen 142,4, avslutet 16,9; cpu 4 hero 280,1 / 49,9, process 83,2 / 50,1,
   jätten 250,0, priset 238,2). Ett fönster som blir mätbart sämre utan att planen rör det
   är brus tills tre sammanflätade körningar med ren kontroll emellan säger något annat;
   kör dem då.
3. Geometrin: `scrollHeight` 10 582 vid 1440 och 11 326 vid 390, **lika vid load och i
   bandet**; motorns topp för `#process` (`ScrollCraft.instances[0].acts`, läst i skript,
   aldrig i sidan) = DOM:ens utan resize, 5 340 respektive 6 152.
4. `scroll_verify.py` vid 1440x900 och 390x844 (`--out {{UT_MAPP}}/shots/r11/papper`):
   `cuesNeverFull`, `unrevealed` och `contrastUnderMedia` tomma; döda band jämförs mot loop
   5:s (`shots/loop-5/probe/scroll-verify-*.txt`).
5. `perf_probe.py --cpu 4` vid 1440 och 390: `long-task-under-scroll`, CLS ≤ 0,05 (R10:
   0,046 vid 1440, 0,000 vid 390), sidans vikt.
6. `a11y_scan.py`, `tab_walk.py`, `reflow.py` vid 320 och 200 % plus 900x600, 1024x640,
   1180x740, 1280x800, 1366x640, 1280x600, 720x450 och 320x568.
7. Grep: `prefers-reduced-motion` 0, U+2012 till U+2015 0 i synlig text, inline-hex-antalet
   utanför `:root` oförändrat (12), `clip-path` 0 träffar på
   `.frame-wrap`/`.calyx-wrap`/`.horai-wrap`, `contain-intrinsic-size` 0 träffar på
   `.price`, `getComputedStyle` 0 träffar i `readState`/`latchTick`s hetväg.

### B. Det inverterade läget, `?process=invert`

8. `contrast_over_media.py --url` på `?process=invert` vid 1440 (scrollY 5 400, 6 500,
   8 000) och 390 (7 000, 8 500): varje brödtextsträng ≥ 4,5:1, varje rubrik ≥ 3:1. Skriv
   varje sträng med sitt tal, som arkitekten gjorde i loop 5. Hårlinjerna räknas separat ur
   de två tokenvärdena: `--hair-ink` mot grunden ≥ 3:1. Accenten: `--c-accent-on-dark` mot
   grunden ≥ 4,5:1, med talet utskrivet (`#1e5e9c` mot `#0b0c0e` är 2,93:1 och underkänns;
   det talet står redan i `BRIEF.md`).
9. Δ L vid de två seams, båda kandidatgrunderna (villkor d i planen): en pixel i prisplanet,
   en i akten, en i avslutsfotot, samma metod som H-11. Fyra tal i NOTES § R11.
10. `?process=invert&preview=process-01` till `-07` vid 1440 och 390: `--sc-ps` = `--eN`
    ± 0,0001 för alla sju, i båda bredderna, **och** `?preview=process-0N` utan
    `?process=` ger samma tal. Vid 390 tre laddningar var (042:s racekontroll gäller
    fortfarande).
11. `a11y_scan.py` och `reflow.py` rena också i invert-läget.
12. `.p-live` (Calyx-bilden i steg 05) har exakt `filter:grayscale(1) contrast(1.05)` i
    **båda** lägena: skriv ut `getComputedStyle(...).filter` för båda. Villkor (a).

### C. Skärmbilder, det Anton faktiskt ska titta på

13. `{{UT_MAPP}}/shots/r11/papper/`: `?preview=process-01` till `-07` vid 1440 och 390
    (14 bilder, `wait_until="load"` + 2 s), plus hela sidan i skivor vid 1440 och 390 med
    plain `scrollTo` och 3 s väntan.
14. `{{UT_MAPP}}/shots/r11/invert/`: `?process=invert&preview=process-01` till `-07` vid
    1440 och 390 (14 bilder), plus hela sidan i skivor vid 1440 och 390 med
    `?process=invert`. **Samma filnamn som i `papper/`**, så att lead kan lägga dem parvis.
15. Läs varje bild, `läst: <fil>` i NOTES § R11. Skriv en rad per stegpar (01 till 07) om
    vad som skiljer i pixlarna, utan att döma: det är Antons dom, inte din.

## 3. Invarianter

F-011 rörelsen spelar alltid, i båda lägena. F-014 allt som förflyttar sig läser `--sc-ps`
(planen rör ingen rörelse; om du skriver en rad som gör det har du gått utanför planen).
Gate 47/79 (ritningen ritar form, aldrig innehåll; Calyx-bilden är en riktig produktyta och
inverteras aldrig), 48 (token, aldrig inline-hex), 60 (inga värden ur demoterade skills),
75 (noll tankstreck), 88 (ingen scroll-cue-text), 93 (CLS ≤ 0,05), 94 (staircase 0,
max_step ≤ 3 % på `--sc-ps`, kontinuitet). Ingen generering, ingen tredje iframe, en
höjdmekanism, `@property` för varje `--p-*` och `--rv`. Ordagrann copy ur `PRODUCT.md`
§ Låst copy rörs aldrig, femton strängar, alla ska finnas kvar byte för byte efter rundan
i båda lägena; stegens copy v1 orörd; liggarens tre rader orörda. `PRODUCT.md` § absences.
Motorn och `sites/*` orörda. Fullständig output; måste du pausa: `[PAUSED — plan 1 av 1]`
som sista rad.

## 4. Leverans

- `{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/shots/r11/papper/`, `{{UT_MAPP}}/shots/r11/invert/`.
- `{{UT_MAPP}}/NOTES.md` § R11: planens dom med orsak; **renderidentitetstabellen (punkt 1),
  före och efter, är rundans viktigaste leverans**; grinden med kontroll- och sidtal (cpu 1
  och 4, båda riktningarna) jämförd mot loop 5:s tal; geometrin (punkt 3); CLS (punkt 5);
  kontrasttabellen i invert-läget (punkt 8); de fyra Δ L-talen (punkt 9);
  previewkontrollen i båda lägena (punkt 10); `.p-live`s filter i båda lägena (punkt 12);
  `läst:`-raderna och de sju stegparens skillnader (punkt 15); låst copy 15/15; avvikelser
  med skäl.
- `{{UT_MAPP}}/BRIEF.md` § decision ledger, "Byggarens rader, R11": två rader, `?process=
  invert` som ett läge i samma fil (aldrig en andra cell) och `--c-accent-on-dark` med sitt
  mätta tal och sitt skäl.
- HELHET.md § 3 rörs INTE av byggaren. Rundan bockar ingen rad och får inte sänka någon.

Sista raden i sista meddelandet: `R11 klar` eller `[PAUSED — plan 1 av 1]`.
