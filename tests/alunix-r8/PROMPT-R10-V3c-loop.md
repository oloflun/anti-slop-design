# Alunix r9, runda 10. Cell {{KONCEPT}}. Helhetsloopen, runda 4: tre fixplaner mot golvet i HELHET.md.

Samma session, samma cell. R9 togs som runda (leadens pixelläsning godkänd); helhetsloopens
runda 4 (arkitekten, `{{UT_MAPP}}/NOTES.md` § Loop 4, `reviews/loop-4-astra.md`) fann två
funktionsfel i R9:s egen kod och ett kurvfel som R9 ärvde av motorn: prisblockets
platshållare är 297 px högre än blocket (sidan krymper när blocket målas, motorns akttoppar
under bandet står kvar fel, 390-previews är ett race), Calyx-revealen sker aldrig (`.rv`
klipper inte), och grundens ljus släcks i ett steg vid scrollY 3 600. Den här rundan utför
arkitektens tre fixplaner i `{{UT_MAPP}}/plans/README.md` § R10, i README:s ordning.
Ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

## 0. Läs först

1. `{{UT_MAPP}}/plans/README.md` § R10: vilka planer, i vilken ordning, och beroenden
   (042 först: H-15, H-30 och bandets bildtid mäts mot den konstanta dokumenthöjden; 043
   mäts före och efter i Calyx-fönstret med tre körningar och median; 044 är oberoende).
2. Varje R10-plan i sin helhet (Problem / Target / Conventions / Steps / Boundaries /
   Verification): 042, 043, 044. Planerna bär radhänvisningar mot R9-filen (md5
   `909916d1`); hitta varje ankare med `Grep` innan du redigerar och STOPPA (skriv i NOTES
   § R10) om koden inte matchar i sak.
3. `{{UT_MAPP}}/HELHET.md` § 3 (golvet H-01 till H-35 med arkitektens loop 4-rader; H-23 är
   återöppnad med skäl i raden) och § 4 (tilläggen T-1 till T-8).
4. `{{UT_MAPP}}/reviews/loop-4-astra.md`, `reviews/loop-3-astra.md`, `reviews/loop-2-astra.md`,
   `reviews/loop-1-astra.md` och `reviews/r5/` (läs `keep` i var och en: `keep` är det du
   inte får riva).
5. `{{UT_MAPP}}/PROCESS-UNDERLAG.md` § 3: stegens copy v1 är låst för dig; copy-gaten körs
   av en copy-agent efter loopen. Rör inga strängar.
6. `Skill(design)` (verbet build, komponentskop), `Skill(animate)` och `Skill(emil-design-eng)`
   FÖRE ändringar i rörelse (043, 044). Via `Skill`-verktyget, namngivna i transkriptet, i
   den ordningen.
7. `~/.claude/skills/design/references/performance.md` (gate 93, CLS och
   `content-visibility`) och `motion-smoothness.md` före 042 och 043.
8. `{{UT_MAPP}}/shots/loop-4/scripts/`: `mountshift.py` och `pricefix_ab.py` (042:s
   mätning: docH, motorns topp mot DOM:ens, 390-previews i tre laddningar),
   `verify_astra4.py` (043:s andelar och 044:s driftsekvens), `motion_probe_ab.py`
   (`--pre "<js>"`: ablation efter `load` + 5 s), `preview390.py`, `latch4.py`. Kopiera till
   scratch och kör därifrån; skriv aldrig i skill-filerna.

## 1. Utför

Planerna i README-ordning, Verification per plan innan nästa öppnas, utfall i transkriptet
och i NOTES § R10: `verified`, `best-effort` (med vad som återstår) eller `reverted` (orsak).
Aldrig `verified` på känsla. Kirurgiska `Edit`-anrop, aldrig `Write` av hela filen, aldrig
shell-skrivningar mot UI-filer. Motorn `scroll/scrollcraft.js`, `scroll/scrollcraft.css` och
`sites/*` rörs aldrig; `scroll/sc-smooth.js` rörs inte i R10 (ingen plan kräver det). Rör
aldrig det som står i rapporternas `keep`: `--sc-ps`-kontraktet (staircase 0, LERP 0,16,
DEAD 0,0005, `inherits:true` på `--sc-ps`), `will-change` bara via klass, sticky som enda
höjdmekanism i processakten, `pathLength="1"` med `*1px`, `@property`-raderna, iframes
`inert` + `pointer-events:none`, `<ol>` med text i DOM, reveal på wrappern (aldrig på
ramen), ramarna orörda efter att de visats (under revealen pixelstilla, efter revealen
identitet), `.ground`s `contain:strict`, `--c-graphite`, A-glyfen, kortets span 3,4 / fönster
0,10 till 0,78, gridankaret (034 A), prosan synlig (034 B), observern på wrappern (027),
`is-asleep` via `f.closest('.frame-wrap')` (036), latchen med exakt 1 och aktobjekt per tick
(035), Hōrais kvadratiska iris och `measureFrames()` (036 A), monteringen i heroens svans
(036 B), `aimPreview` med generations-id (037), lägena ur shimens `cur` (039), konturen 0 till
0,30 (040), 24 % (038), driften på `.ground` med stoppen ur `:root` (041).

Varje plan har mätbara mål (tal eller bild). Mät före och efter där planen säger det, och
skriv båda talen. Faller ett STOPPA-villkor: stanna i den planen, skriv talen, gå vidare till
nästa plan bara om planen uttryckligen tillåter det. 042 och 043 har egna före/efter-grindar
(tre körningar, median).

Tillägg och färger: inga nya tokens i R10. Ingen inline-hex (gate 48), inga värden ur
demoterade skills (gate 60). Ramarna får inte `content-visibility` bort (018/027 står; 042
gäller bara `.price`). Låst copy (femton strängar) rörs aldrig, inte heller med `&shy;`.
Noll tankstreck. Inga tal utöver ritningens mått och de låsta priserna.

## 2. Grinden efter sista planen, i din session

Servern `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten. Kontrollprotokollet gäller (`tests/motion/smooth.html` först, ren kontroll
omedelbart före varje sidmätning; ger kontrollen en ruta > 33 ms: vänta en minut och kör om;
ger den fortfarande brus efter två försök mäts sidan ändå och kontrollens tal skrivs bredvid).

1. `motion_probe.py`, spår `section.hero:--sc-ps,.plate-card:transform` (40 ticks från
   toppen, och 18 ticks från toppen = pinnen ensam), `#process:--sc-ps` (`--ticks 45`, start
   4 700 ned, 9 400 upp), `#giant-section:--sc-ps` (start 2 700, 28 ticks), `.price:--sc-ps`
   (start 3 873, 18 ticks), `.calyx-wrap:--rv,.calyx-fig:--sc-ps` (start 2 862, 20 ticks),
   `.panel-thesis:--sc-ps` (start 2 322, 18 ticks, ramarna förmonterade med `--pre`),
   `footer.close:--sc-ps` (start 8 500, 18 ticks); `--wheel 100:60` och `--wheel 20:120`
   för hero och process, båda riktningarna; **cpu 1 OCH cpu 4**; med `--start` ur
   scratchkopian. Skriv kontroll och sida sida vid sida, och loop 4:s tal (NOTES § Loop 4,
   `shots/loop-4/probe/`) som utgångsläge. Bar: staircase 0 överallt; `--sc-ps` max_step ≤
   3 % vid cpu 1 (H-23: jätten 3,12 och tesen 3,52 i loop 4, mäts om efter 042); cpu 1 p95
   pinnen ensam ≤ 20 ms, arket ≤ 20, priset ≤ 40, jätten inte sämre än 81,7 (loop 4:s
   A/B-median med platshållaren neutraliserad); cpu 4 p95 ≤ 20 ms och 0 rutor är H-21:s
   bar, rapporteras med före/efter, gränsar inte rundan. RecalcStyleCount per frame ≤ 1,4
   (CDP `Performance.getMetrics`, som R8).
2. Geometrin (042 steg 3): `scrollHeight` lika vid load och i bandet vid 1440 och 390;
   motorns topp för `#process` (`ScrollCraft.instances[0].acts`, läst i skript, aldrig i
   sidan) = DOM:ens utan resize; `#process` inline `--sc-p` vid scrollY 4 800 (1440) =
   0,077 ± 0,002.
3. Latchen (035): fyra scrollsätt till samma scrollY, båda wrapparna ≥ 0,99; resize före
   bandet; noll skrivningar efter landning (`shots/loop-4/scripts/latch4.py`).
4. `scroll_verify.py` vid 1440x900 och 390x844 (`--out {{UT_MAPP}}/shots/r10`): H-16; döda
   band jämförs mot loop 4:s (`shots/loop-4/probe/scroll-verify-*.txt`) på de nya
   positionerna (sidan är 297 / 262 px kortare från load).
5. `perf_probe.py --cpu 4` vid 1440 och 390: `long-task-under-scroll`, **CLS ≤ 0,05 och
   skrivet bredvid R9:s 0,000**, sidans vikt (R9: 476 kB).
6. `preflight_taste.py`, `contrast_over_media.py --url` (folden; `.price`-raderna;
   kortbaksidan), `a11y_scan.py`, `tab_walk.py`, `reflow.py` vid 320 och 200 % plus 900x600,
   1024x640, 1180x740, 1280x800, 1366x640, 1280x600, 720x450 och 320x568.
7. Grep: `prefers-reduced-motion` 0, U+2012 till U+2015 0 i synlig text, inga nya inline-hex
   utanför `:root`, `clip-path` 0 träffar på `.frame-wrap`/`.calyx-wrap`/`.horai-wrap`,
   `contain-intrinsic-size` 0 träffar på `.price`, `getComputedStyle` 0 träffar i
   `readState`/`latchTick`.
8. Skärmbilder, allt i `{{UT_MAPP}}/shots/r10/`: hela sidan i skivor vid 1440 och 390 med
   plain `scrollTo` och 3 s väntan (`shots/loop-4/scripts/slices4.py`-metoden; ramarna
   hela), fold vid 320/375/390/414/768/1024/1280, `?preview=front|mid|back|ledger|bleed|
   process-01…07` vid 1440 och 390 (`wait_until="load"` + 2 s; **390 process-01..07 tre
   laddningar var**, alla formade), tolv ramar genom heron, tolv genom `#process` (den
   första ramen efter prisblocket: ritningen i fas med prosan, `life-01` visar konturen
   bredvid steg 01), tolv genom `.calyx-fig` (043: öppningen dras upp uppifrån, blommorna
   pixelstilla; jämför ram 3 och 6 mot R8:s `shots/r8/calyx12-1440-03.png`, `-05.png`) och
   `.horai-fig` (oförändrad mot R9:s `shots/r9/p036/horai-life-*.png`), tolv genom `.price`,
   tolv genom `#giant-section` vid 1440 och 390, och driftsekvensen scrollY 3 400 till 4 200
   i 20 px-steg vid 1440 (044: ingen ton som byter i ett steg). Läs varje bild, `läst: <fil>`
   i NOTES, F-007 bild för bild mot varje plans Verification-bild.
9. PageDown-vandringen (a11y fix 3) om igen efter 042: sju av sju steg, och PageUp mitt i
   akten ritar baklänges utan klipp (039 steg 5).
10. `?preview=process-01…07` vid 1440 och 390, i båda riktningarna (037 steg 3): `--kN` = 1,
    `--sc-ps` < `--s(N+1)`, steg N:s sista bana `0px`; vid 390 tre laddningar var (042 steg 4).
11. Ramarnas vandring (027 steg 2 och 3) vid 1440 och 390: 0 stopp med sovande wrapper i
    viewporten; sömn vid scrollY 0; en resurspost per ram; Calyx-wrapperns bakgrund
    `#e9e5da` synlig ≈ 100 % vid `--rv` 0 och 0 % vid 1 (043 steg 3).

## 3. Invarianter

F-011 rörelsen spelar alltid. F-014 allt som förflyttar sig läser `--sc-ps` (lägena läser
shimens lerpade `cur`, aldrig rått `--sc-p` eller rå scrollY för det ögat ser; driften är
en funktion av rå scrollY per 041 och rörs inte i det). Gate 47/79 (ritningen ritar form,
aldrig innehåll), 75 (noll tankstreck), 88 (ingen scroll-cue-text), 93 (CLS ≤ 0,05), 94
(staircase 0, max_step ≤ 3 % på `--sc-ps`, kontinuitet). Ingen generering, ingen tredje
iframe, en höjdmekanism, `@property` för varje `--p-*` och `--rv`. Ordagrann copy ur
`PRODUCT.md` § Låst copy rörs aldrig, femton strängar, alla ska finnas kvar byte för byte
efter rundan; stegens copy v1 orörd; liggarens tre rader orörda. `PRODUCT.md` § absences.
Motorn och `sites/*` orörda. Fullständig output; måste du pausa: `[PAUSED — plan X av 3]`
som sista rad.

## 4. Leverans

- `{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/shots/r10/`.
- `{{UT_MAPP}}/NOTES.md` § R10: en rad per plan med dom och orsak (talen före/efter där
  planen kräver det), grinden med kontroll- och sidtal (cpu 1 och 4, båda riktningarna),
  RecalcStyleCount per frame, geometritabellen (punkt 2), latchtabellen (punkt 3), CLS
  (punkt 5), F-007-tabellen, PageDown/PageUp-utfallet, previewkontrollen (punkt 10, båda
  riktningarna, 390 tre laddningar), ramvandringen (punkt 11), låst copy 15/15, avvikelser
  med skäl.
- `{{UT_MAPP}}/BRIEF.md` § decision ledger, "Byggarens rader, R10": raderna planerna anger
  (042 platshållaren bort och dokumenthöjden konstant, 043 Calyx-öppningen klipper och
  kommer uppifrån, 044 leg 2 från överlämningen).
- HELHET.md § 3 rörs INTE av byggaren: arkitekten bockar i loop 5.

Sista raden i sista meddelandet: `R10 klar` eller `[PAUSED — plan X av 3]`.
