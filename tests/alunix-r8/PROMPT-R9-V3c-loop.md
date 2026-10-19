# Alunix r9, runda 9. Cell {{KONCEPT}}. Helhetsloopen, runda 3: sju fixplaner mot golvet i HELHET.md.

Samma session, samma cell. R8 togs som runda; helhetsloopens runda 3 (arkitekten,
`{{UT_MAPP}}/NOTES.md` § Loop 3, `reviews/loop-3-astra.md`) fann tre funktionsfel som går
först (revealens latch är vägberoende, klippningen över en levande ram är bandets bildtid,
previewlägena siktar före typsnitten), ett lägesfel och tre mindre. Den här rundan utför
arkitektens sju fixplaner i `{{UT_MAPP}}/plans/README.md` § R9, i README:s ordning.
Ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

## 0. Läs först

1. `{{UT_MAPP}}/plans/README.md` § R9: vilka planer, i vilken ordning, och beroenden
   (035 först: 036 bygger på samma `--rv` och samma sampler; 039 hänger tre konsumenter på
   035:s `latchTick`; 036 mäts före och efter i två fönster med tre körningar och median;
   041 sist och bara med mätt vinst).
2. Varje R9-plan i sin helhet (Problem / Target / Conventions / Steps / Boundaries /
   Verification): 035, 036, 037, 039, 040, 038, 041. Planerna bär radhänvisningar mot
   R8-filen (md5 `70214a22`); hitta varje ankare med `Grep` innan du redigerar och STOPPA
   (skriv i NOTES § R9) om koden inte matchar i sak.
3. `{{UT_MAPP}}/HELHET.md` § 3 (golvet H-01 till H-35 med arkitektens loop 3-rader; H-01,
   H-05 (a) och H-19 är omskrivna med skäl i raden) och § 4 (tilläggen T-1 till T-8).
4. `{{UT_MAPP}}/reviews/loop-3-astra.md`, `reviews/loop-2-astra.md`, `reviews/loop-1-astra.md`
   och `reviews/r5/` (läs `keep` i var och en: `keep` är det du inte får riva).
5. `{{UT_MAPP}}/PROCESS-UNDERLAG.md` § 3: stegens copy v1 är låst för dig; copy-gaten körs
   av en copy-agent efter loopen. Rör inga strängar.
6. `Skill(design)` (verbet build, komponentskop), `Skill(animate)` och `Skill(emil-design-eng)`
   FÖRE ändringar i rörelse (035, 036, 039, 040), `Skill(a11y-audit)` före 039 (kortsidans
   `inert`). Via `Skill`-verktyget, namngivna i transkriptet, i den ordningen.
7. `~/.claude/skills/design/references/performance.md` och `motion-smoothness.md` före 036
   och 041.
8. `{{UT_MAPP}}/shots/loop-3/scripts/`: `latch_diag.py` (035:s mätning), `motion_probe_ab.py`
   (`--pre "<js>"`: ablation efter `load` + 5 s), `ab_band*.sh` (036:s A/B-fönster och
   `MOUNT`/`WRAP`/`RECIPE`-strängarna), `preview_check.py` (037), `drift2.py` (038, 041),
   `slices_fix.py` (skivfångst med samplern injicerad, tills 035 är byggd). Kopiera till
   scratch och kör därifrån; skriv aldrig i skill-filerna.

## 1. Utför

Planerna i README-ordning, Verification per plan innan nästa öppnas, utfall i transkriptet
och i NOTES § R9: `verified`, `best-effort` (med vad som återstår) eller `reverted` (orsak).
Aldrig `verified` på känsla. Kirurgiska `Edit`-anrop, aldrig `Write` av hela filen, aldrig
shell-skrivningar mot UI-filer. Motorn `scroll/scrollcraft.js`, `scroll/scrollcraft.css` och
`sites/*` rörs aldrig; `scroll/sc-smooth.js` rörs inte i R9 (ingen plan kräver det). Rör
aldrig det som står i rapporternas `keep`: `--sc-ps`-kontraktet (staircase 0, LERP 0,16,
DEAD 0,0005, `inherits:true` på `--sc-ps`), `will-change` bara via klass, sticky som enda
höjdmekanism i processakten, `pathLength="1"` med `*1px`, `@property`-raderna, iframes
`inert` + `pointer-events:none`, `<ol>` med text i DOM, reveal på wrappern (aldrig på
ramen), ramarna orörda efter att de visats (036: under revealen är innehållet
pixelstilla, efter revealen är transformen identitet), `.ground`s `contain:strict`,
`--c-graphite`, A-glyfen, kortets span 3,4 / fönster 0,10 till 0,78, gridankaret (034 A),
prosan synlig (034 B), observern på wrappern (027), `is-asleep`.

Varje plan har mätbara mål (tal eller bild). Mät före och efter där planen säger det, och
skriv båda talen. Faller ett STOPPA-villkor: stanna i den planen, skriv talen, gå vidare till
nästa plan bara om planen uttryckligen tillåter det. 036 och 041 har egna före/efter-grindar
(tre körningar, median) och egna återställningsregler.

Tillägg och färger: inga nya tokens i R9 (`--rv` byter till `inherits:true` i 036; 041:s
stopp är de tre som redan står i attributen, lästa ur `:root`). Ingen inline-hex (gate 48),
inga värden ur demoterade skills (gate 60). Låst copy (femton strängar) rörs aldrig, inte
heller med `&shy;`. Noll tankstreck. Inga tal utöver ritningens mått och de låsta priserna.

## 2. Grinden efter sista planen, i din session

Servern `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten. Kontrollprotokollet gäller (`tests/motion/smooth.html` först, ren kontroll
omedelbart före varje sidmätning; ger kontrollen en ruta > 33 ms: vänta en minut och kör om;
ger den fortfarande brus efter två försök mäts sidan ändå och kontrollens tal skrivs bredvid).

1. `motion_probe.py`, spår `section.hero:--sc-ps,.plate-card:transform` (40 ticks från
   toppen), `#process:--sc-ps` (`--ticks 45`, start 4 700 ned, 9 400 upp), `#giant-section:--sc-ps`
   (start 2 700, 28 ticks), `.price:--sc-ps` (start 3 873, 18 ticks), `footer.close:--sc-ps`
   (start 8 500, 18 ticks); `--wheel 100:60` och `--wheel 20:120`, båda riktningarna;
   **cpu 1 OCH cpu 4**; med `--start` ur scratchkopian. Skriv kontroll och sida sida vid
   sida, och loop 3:s tal (NOTES § Loop 3, `shots/loop-3/probe/`) som utgångsläge. Bar:
   staircase 0 överallt; `--sc-ps` max_step ≤ 3 % vid cpu 1; cpu 1 p95 hero ≤ 20 ms, bandet
   (`#giant-section`, `.price`) ≤ 25, arket ≤ 20; cpu 4 p95 ≤ 20 ms och 0 rutor är H-21:s bar,
   rapporteras med före/efter, gränsar inte rundan. RecalcStyleCount per frame ≤ 1,4 (CDP
   `Performance.getMetrics`, som R8).
2. Latchen (035): fyra scrollsätt till samma scrollY, båda wrapparna ≥ 0,99; noll
   skrivningar efter landning; reload mitt i bandet; resize före bandet (steg 5b).
3. `scroll_verify.py` vid 1440x900 och 390x844 (`--out {{UT_MAPP}}/shots/r9`): H-16;
   `blankBands` vid 390 ska inte längre täcka Calyx och Hōrai (skivorna tas nu med `scrollTo`
   och latchen når 1, så verktyget ser ramarna).
4. `perf_probe.py --cpu 4` vid 1440 och 390: `long-task-under-scroll`, CLS ≤ 0,05, sidans vikt
   (loop 3: 462 081 B).
5. `preflight_taste.py`, `contrast_over_media.py --url` (hero-rubriken och underraden mot
   grunden efter 038; `.price`-raderna; kortbaksidan), `a11y_scan.py`, `tab_walk.py`,
   `reflow.py` vid 320 och 200 % plus 900x600, 1024x640, 1180x740, 1280x800, 1366x640,
   1280x600, 720x450 och 320x568.
6. Grep: `prefers-reduced-motion` 0, U+2013/U+2014 0 i synlig text, inga nya inline-hex
   utanför `:root`, `clip-path` 0 träffar på `.frame-wrap`/`.calyx-wrap`/`.horai-wrap` (036),
   `data-sc-drift` 0 träffar om 041 behölls (annars 2), `getComputedStyle` 0 träffar i
   `readState`/`latchTick`.
7. Skärmbilder, allt i `{{UT_MAPP}}/shots/r9/`: hela sidan i skivor vid 1440 och 390 med
   `scrollTo` som `shots/loop-3/scripts/slices.py`-metoden (utan injicerad sampler: efter 035
   ska ramarna vara hela ändå; 3 s väntan vid Calyx och Hōrai), fold vid
   320/375/390/414/768/1024/1280, `?preview=front|mid|back|ledger|bleed|process-01…07` vid
   1440 och 390 (`wait_until="load"` + 2 s), tolv ramar genom heron, tolv genom `#process`,
   tolv genom `.calyx-fig` och `.horai-fig` (036: irisen och uppdragningen som förut, innehållet
   pixelstilla: jämför ram 6 mot loop 3:s `shots/r8/horai12-1440-05.png`), tolv genom `.price`,
   tolv genom `#giant-section` vid 1440 och 390. Läs varje bild, `läst: <fil>` i NOTES,
   F-007 bild för bild mot varje plans Verification-bild.
8. PageDown-vandringen (a11y fix 3) om igen efter 039: sju av sju steg, och PageUp mitt i
   akten ritar baklänges utan klipp (039 steg 5).
9. `?preview=process-01…07` vid 1440 och 390, i båda riktningarna (037 steg 3): `--kN` = 1,
   `--sc-ps` < `--s(N+1)`, steg N:s sista bana `0px`.
10. Ramarnas vandring (027 steg 2 och 3) vid 1440 och 390: 0 stopp med sovande wrapper i
    viewporten; sömn vid scrollY 0; en resurspost per ram (036 rör wrapparnas inre struktur:
    observern ska fortfarande hitta ramen via `wrap.querySelector('iframe')`).

## 3. Invarianter

F-011 rörelsen spelar alltid. F-014 allt som förflyttar sig läser `--sc-ps` (035:s och
039:s lägen läser shimens lerpade `cur`, aldrig rått `--sc-p` eller rå scrollY för det ögat
ser). Gate 47/79 (ritningen ritar form, aldrig innehåll), 75 (noll tankstreck), 88 (ingen
scroll-cue-text), 94 (staircase 0, max_step ≤ 3 % på `--sc-ps`). Ingen generering, ingen
tredje iframe, en höjdmekanism, `@property` för varje `--p-*` och `--rv`. Ordagrann copy ur
`PRODUCT.md` § Låst copy rörs aldrig, femton strängar, alla ska finnas kvar byte för byte
efter rundan; stegens copy v1 orörd; liggarens tre rader orörda. `PRODUCT.md` § absences.
Motorn och `sites/*` orörda. Fullständig output; måste du pausa: `[PAUSED — plan X av 7]`
som sista rad.

## 4. Leverans

- `{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/shots/r9/`.
- `{{UT_MAPP}}/NOTES.md` § R9: en rad per plan med dom och orsak (talen före/efter där
  planen kräver det), grinden med kontroll- och sidtal (cpu 1 och 4, båda riktningarna),
  RecalcStyleCount per frame, latchtabellen (punkt 2), F-007-tabellen, PageDown/PageUp-
  utfallet, previewkontrollen (punkt 9, båda riktningarna), ramvandringen (punkt 10), låst
  copy 15/15, avvikelser med skäl.
- `{{UT_MAPP}}/BRIEF.md` § decision ledger, "Byggarens rader, R9": raderna planerna anger
  (035 samplern, 036 transformreceptet och `--rv` `inherits:true`, 037 `aimPreview`, 039
  lägena, 040 konturen, 038 24 %, 041 utfallet).
- HELHET.md § 3 rörs INTE av byggaren: arkitekten bockar i loop 4.

Sista raden i sista meddelandet: `R9 klar` eller `[PAUSED — plan X av 7]`.
