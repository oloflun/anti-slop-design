# Alunix r9, runda 8. Cell {{KONCEPT}}. Helhetsloopen, runda 2: åtta fixplaner mot golvet i HELHET.md.

Samma session, samma cell. R7 togs som runda; helhetsloopens runda 2 (arkitekten,
`{{UT_MAPP}}/NOTES.md` § Loop 2, `reviews/loop-2-astra.md`) fann tre funktionsfel som går
först (ramarna vaknar aldrig, bildtiden, processaktens ankare) och fem mindre. Den här rundan
utför arkitektens åtta fixplaner i `{{UT_MAPP}}/plans/README.md` § R8, i README:s ordning.
Ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

## 0. Läs först

1. `{{UT_MAPP}}/plans/README.md` § R8: vilka planer, i vilken ordning, och beroenden
   (027 först: bandets balans och bildtiden mäts med levande ramar; 028 mäts EFTER 027 med
   samma harness före och efter sina egna steg; 034 före 031: båda rör `readState`; 031
   läser shimens `acts[i].cur`, som 028 A behåller).
2. Varje R8-plan i sin helhet (Problem / Target / Conventions / Steps / Boundaries /
   Verification): 027, 028, 034, 031, 033, 029, 030, 032. Planerna bär radhänvisningar mot
   R7-filen (md5 `d30355da`); hitta varje ankare med `Grep` innan du redigerar och STOPPA
   (skriv i NOTES § R8) om koden inte matchar i sak.
3. `{{UT_MAPP}}/HELHET.md` § 3 (golvet H-01 till H-35 med arkitektens loop 2-rader; H-07 är
   omskriven till 88 px) och § 4 (tilläggen T-1 till T-8).
4. `{{UT_MAPP}}/reviews/loop-2-astra.md`, `reviews/loop-1-astra.md` och `reviews/r5/` (läs
   `keep` i var och en: `keep` är det du inte får riva).
5. `{{UT_MAPP}}/PROCESS-UNDERLAG.md` § 3: stegens copy v1 är låst för dig; copy-gaten körs
   av en copy-agent efter loopen. Rör inga strängar.
6. `Skill(design)` (verbet build, komponentskop), `Skill(animate)` och `Skill(emil-design-eng)`
   FÖRE ändringar i rörelse (028, 031, 033), `Skill(a11y-audit)` före 034 och 032. Via
   `Skill`-verktyget, namngivna i transkriptet, i den ordningen (R7 läste dem efteråt; det
   är en avvikelse, inte en metod).
7. `~/.claude/skills/design/references/performance.md` och `motion-smoothness.md` före 028:
   planen ändrar sidans egen shim (`scroll/sc-smooth.js`), aldrig motorn.

## 1. Utför

Planerna i README-ordning, Verification per plan innan nästa öppnas, utfall i transkriptet
och i NOTES § R8: `verified`, `best-effort` (med vad som återstår) eller `reverted` (orsak).
Aldrig `verified` på känsla. Kirurgiska `Edit`-anrop, aldrig `Write` av hela filen, aldrig
shell-skrivningar mot UI-filer. Motorn `scroll/scrollcraft.js`, `scroll/scrollcraft.css` och
`sites/*` rörs aldrig; `scroll/sc-smooth.js` är sidans egen fil och redigeras enligt plan
028 (och bara den). Rör aldrig det som står i rapporternas `keep`: `--sc-ps`-kontraktet
(staircase 0, LERP 0,16, DEAD 0,0005, `inherits:true` på `--sc-ps`), `will-change` bara via
klass, sticky som enda höjdmekanism i processakten, `pathLength="1"` med `*1px`,
`@property`-raderna, iframes `inert` + `pointer-events:none`, `<ol>` med text i DOM, reveal
på wrappern (aldrig på ramen), `.ground`s `contain:strict`, `--c-graphite`, A-glyfen,
kortets span 3,4 / fönster 0,10 till 0,78.

Varje plan har mätbara mål (tal eller bild). Mät före och efter där planen säger det, och
skriv båda talen. Faller ett STOPPA-villkor: stanna i den planen, skriv talen, gå vidare till
nästa plan bara om planen uttryckligen tillåter det. 028 har egna STOPPA-villkor (staircase,
max_step, `?preview=` som inte fryser) och egna målvärden vid cpu 1; cpu 4 rapporteras,
gränsar inte planen.

Tillägg och färger: inga nya tokens i R8 (`--rv` i 031 är en registrerad lokal, ingen
färg). Ingen inline-hex (gate 48), inga värden ur demoterade skills (gate 60). Låst copy
(femton strängar) rörs aldrig, inte heller med `&shy;`. Noll tankstreck. Inga tal utöver
ritningens mått och de låsta priserna.

## 2. Grinden efter sista planen, i din session

Servern `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten. Kontrollprotokollet gäller (`tests/motion/smooth.html` först, ren kontroll
omedelbart före varje sidmätning; ger kontrollen en ruta > 33 ms: vänta en minut och kör om;
ger den fortfarande brus efter två försök mäts sidan ändå och kontrollens tal skrivs bredvid).

1. `motion_probe.py`, spår `section.hero:--sc-ps,.plate-card:transform` (40 ticks från
   toppen), `#process:--sc-ps` (`--ticks 45`, start `#process`s överkant minus en viewport),
   `#giant-section:--sc-ps` (start `.stagger.top − 600`, 28 ticks), `footer.close:--sc-ps,
   .price:--sc-ps` (start `.price.top − 900`, 18 ticks); `--wheel 100:60` och `--wheel
   20:120`, båda riktningarna (uppåt: negativt px-tal och start vid aktens slut; saknar din
   kopia `--start`, skriv scrollY-starten via `page.evaluate` i en kopia i scratch, aldrig
   i skill-filen); **cpu 1 OCH cpu 4**. Skriv kontroll och sida sida vid sida, och loop 2:s
   tal (NOTES § Loop 2, `shots/loop-2/probe/`) som utgångsläge. Bar: staircase 0 överallt;
   `--sc-ps` max_step ≤ 3 % vid cpu 1; cpu 1 p95 hero ≤ 20 ms, bandet ≤ 25, arket ≤ 20
   (plan 028:s målvärden); cpu 4 p95 ≤ 20 ms och 0 rutor är H-21:s bar, rapporteras med
   före/efter, gränsar inte rundan. RecalcStyleCount per frame ≤ 1,4 (CDP
   `Performance.getMetrics` före/efter en körning, som scratch `profile4.py` i loop 2).
2. `scroll_verify.py` vid 1440x900 och 390x844 (`--out {{UT_MAPP}}/shots/r8`): H-16;
   `blankBands` vid 390 ska minska när ramarna vaknar (loop 2: sex band, varav tre är
   sovande ramar).
3. `perf_probe.py --cpu 4` vid 1440 och 390: `long-task-under-scroll`, CLS ≤ 0,05 (032
   ändrar foldens fördelning vid 390; 030 rubrikens höjd), sidans egen vikt (loop 2:
   452 879 B; 028 C tar bort ~60 spann ur DOM vid körning, inte ur filen).
4. `preflight_taste.py`, `contrast_over_media.py --url` (hero-rubriken och underraden mot
   grunden efter 029; liggarens text vid `--scrub` 0 och 1 efter 028 C; `.price`-raderna;
   kortbaksidan), `contrast.py` där planen säger det, `a11y_scan.py`, `tab_walk.py`,
   `reflow.py` vid 320 och 200 % plus 900x600, 1024x640, 1180x740, 1280x800, 1366x640,
   1280x600, 720x450 och 320x568 (032).
5. Grep: `prefers-reduced-motion` 0, U+2013/U+2014 0 i synlig text, inga nya inline-hex
   utanför `:root`, `getComputedStyle` 0 träffar i `sc-smooth.js`s `tick()`, `data-sc-reveal`
   0 träffar på `.frame-wrap`, `data-sc-in` 0 träffar på `.process-steps`.
6. Skärmbilder, allt i `{{UT_MAPP}}/shots/r8/`: hela sidan i skivor vid 1440 och 390 (som
   `shots/loop-2/slices-*`, med 3 s väntan vid Calyx och Hōrai så ramarna hinner ladda),
   fold vid 320/375/390/414/768/1024/1280, `?preview=front|mid|back|ledger|bleed|
   process-01…07` vid 1440 och 390 (**`wait_until="load"` + 1,5 s**, loop 2:s verktygsfynd),
   tolv ramar genom heron (`--flip` 0 till 1), tolv genom `#process`, tolv genom
   `.calyx-fig` och `.horai-fig` (031), tolv genom `.price` (033), tolv genom
   `#giant-section` (028 C) vid 1440 och 390. Läs varje bild, `läst: <fil>` i NOTES, F-007
   bild för bild mot varje plans Verification-bild.
7. PageDown-vandringen (a11y fix 3) om igen efter 034: sju av sju steg.
8. `?preview=process-01…07` vid 1440 och 390, i båda riktningarna: preview N visar steg 01
   till N (konturen och glyfen med `stroke-dashoffset 0px` från preview 02) och inte N+1
   (034 A; R7:s kontroll mätte bara N+1).
9. Ramarnas vandring (027 steg 2 och 3) vid 1440 och 390: 0 stopp med sovande wrapper i
   viewporten; sömn vid scrollY 0; en resurspost per ram.

## 3. Invarianter

F-011 rörelsen spelar alltid. F-014 allt som förflyttar sig läser `--sc-ps` (031:s `--rv`
härleds ur shimens lerpade värde, aldrig ur rått `--sc-p`). Gate 47/79 (ritningen ritar
form, aldrig innehåll), 75 (noll tankstreck), 88 (ingen scroll-cue-text), 94 (staircase 0,
max_step ≤ 3 % på `--sc-ps`). Ingen generering, ingen tredje iframe, en höjdmekanism,
`@property` för varje `--p-*` och `--rv`. Ordagrann copy ur `PRODUCT.md` § Låst copy rörs
aldrig, femton strängar, alla ska finnas kvar byte för byte efter rundan; stegens copy v1
orörd; liggarens tre rader orörda (028 C byter regel, inte text). `PRODUCT.md` § absences.
Motorn och `sites/*` orörda. Fullständig output; måste du pausa: `[PAUSED — plan X av 8]`
som sista rad.

## 4. Leverans

- `{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/scroll/sc-smooth.js`, `{{UT_MAPP}}/shots/r8/`.
- `{{UT_MAPP}}/NOTES.md` § R8: en rad per plan med dom och orsak (talen före/efter där
  planen kräver det), grinden med kontroll- och sidtal (cpu 1 och 4, båda riktningarna),
  RecalcStyleCount per frame före/efter, F-007-tabellen, PageDown-utfallet, preview-
  kontrollen (punkt 8, båda riktningarna), ramvandringen (punkt 9), låst copy 15/15,
  avvikelser med skäl.
- `{{UT_MAPP}}/BRIEF.md` § decision ledger, "Byggarens rader, R8": raderna planerna anger
  (027 observern, 028 shimen/`--sc-p`/gradientfronten, 034 ankaret/prosan, 031 latchen,
  033 prisliggaren, 029 40 %, 030 88 px, 032 folden/seams).
- HELHET.md § 3 rörs INTE av byggaren: arkitekten bockar i loop 3.

Sista raden i sista meddelandet: `R8 klar` eller `[PAUSED — plan X av 8]`.
