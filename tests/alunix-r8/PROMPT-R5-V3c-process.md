# Alunix r9, runda 5. Cell {{KONCEPT}}. Processakten "Ritningen" och kortvändningens tempo.

Samma session, samma cell. R4 utförde fixplanerna 001 till 008. Den här rundan bygger den
åttonde skärmen: en ritad processakt på papper, sju steg, efter `.stagger` och före
avslutet, enligt arkitektens plan, och sätter kortvändningens tempo. Ut-mapp `{{UT_MAPP}}`,
port {{PORT}}.

## 0. Läs först, i denna ordning, innan du rör filen

1. `{{UT_MAPP}}/plans/010-process.md` i sin helhet. Varje värde står där: placering,
   viewBox, banor per steg, fönster i `--sc-ps`, device-tabellen, `@property`-raderna,
   copyutkast v0, token-tabellen, mobilplanschen, `?preview=`-lägena, Steps 1 till 11,
   Boundaries, Verification.
2. `{{UT_MAPP}}/plans/011-*.md` (kortvändningen: span, dwell, smoothstep-fönstret).
3. `{{UT_MAPP}}/HELHET.md` § 3, raderna H-28 till H-33 (akten) och H-21 till H-25 (rörelsen).
4. `tests/alunix-r8/board/cells/K3-r8/index.html` rad 100 till 300 och 676 till 860: ritningens
   klassregler, `pathLength="1"`, `stroke-dashoffset`-uttrycken med `*1px`, den reducerade
   planschen (rad 389 till 476) och viewBox-bytet i JS (rad 1101 till 1124). Lånas som form
   och teknik, aldrig som sida.
5. `Skill(design)` (verbet build, komponentskopet: en ny sektion i en befintlig sida) och
   de referenser den routar till; `Skill(animate)` och `Skill(emil-design-eng)` före device-
   tabellen; `Skill(find-animation-opportunities)` gaten på varje bana du överväger utöver
   planens (svaret ska vara nej). Anropa skills via `Skill`-verktyget, namngivna i
   transkriptet: lead mäter kedjan per agent.

Planens radhänvisningar gäller boardkopian före R4. **R4 har flyttat rader.** Hitta varje
ankare med `Grep` (`.stagger`, `<footer class="close"`, `function readState`, `var MODES`,
`.kicker-sans`) innan du redigerar; matchar inte koden planens beskrivning i sak, stoppa
och skriv vad som skiljer i NOTES.md § R5 i stället för att gissa.

## 1. Bygg, i planens ordning

Plan 010 Steps 1 till 11, sedan plan 011. Kirurgiska `Edit`-anrop på `{{UT_MAPP}}/index.html`,
en Step i taget, aldrig `Write` av hela filen. UI-filer författas bara med `Write`/`Edit`;
`design-gate.py` nekar `cat >`, heredoc, `tee`, `sed -i`, `Set-Content` och inline-skript
(ledgersignal `shell-write`). Motorn i `{{UT_MAPP}}/scroll/` redigeras aldrig, `.sc-*`
restylas aldrig, `sites/*` rörs aldrig. Ingen tredje `<iframe>`; steg 05 använder
`{{UT_MAPP}}/assets/demo-calyx-1440.webp` (finns) som `<image>` i en `<clipPath>`.

Räkna banorna innan du skriver dem: högst 60, alla med `pathLength="1"`. Varje `<path>`,
`<rect>` och `<line>` kan namnges kontur, måttlinje, hjälplinje, skraffering, ledare eller
utrop (gate 47/79: form, aldrig innehåll; ingen ritad chrome, ingen fejkad UI).

Kommentar i källan vid sektionen som namnger vad som ersätts:
`<!-- PROCESS: ett ritat ark i sju tillstånd, INTE fyra ikonkort eller en tidslinje med punkter -->`.

## 2. Copy

Copyutkast v0 ur plan 010 skrivs in ordagrant och markeras `<!-- copy v0, copy-gate i R6 -->`.
Copy-gaten körs av en copy-agent efter granskningen, inte av dig. Låst copy ur `PRODUCT.md`
§ Brand Commitments (femton strängar) rörs aldrig; `Design`, `Utveckling`, `System` står
kvar som liggarens rubriker, bara underraderna byts. Noll tankstreck (även U+2010 till
U+2015). Inga tal utöver 320 · 768 · 1440, 16:9, 7 rem, 96 px, och de låsta priserna.

## 3. Grinden efter sista Step, i din session, utfallen i transkriptet och NOTES.md § R5

Servern: `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten. Kontrollprotokollet gäller: mät `tests/motion/smooth.html` först, och sidan
bara när kontrollen är ren.

1. `motion_probe.py --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --cpu 4 --track "#process:--sc-ps,#p-outline:stroke-dashoffset,#p-opening:stroke-dashoffset" --wheel 100:60` och `--wheel 20:120`, båda riktningarna; sedan `--track "section.hero:--sc-ps,.plate-card:transform"` för plan 011. Baren: staircase 0, p95 ≤ 20 ms, noll rutor > 33 ms, `--sc-ps` max_step ≤ 3 %. Spåra aldrig rått `--sc-p`.
2. `scroll_verify.py --url … --out {{UT_MAPP}}/shots/r5`: inga nya `deadScroll`-band inne i `#process`, heron-svansen ≤ 700 px (H-17).
3. `perf_probe.py --cpu 4` vid 1440 och 390: CLS ≤ 0,05 vid 390, sidans egen vikt växer högst med bildens storlek.
4. `preflight_taste.py`, `node ~/.agents/skills/impeccable/scripts/detect.mjs --json`, `contrast_over_media.py --url` på papperet under arket, `a11y_scan.py` (SVG:n `role="img"` med `<title>` och `<desc>`, stegen som `<ol>`), `tab_walk.py`, `reflow.py`.
5. Grep i `index.html`: `prefers-reduced-motion` 0 träffar; U+2013/U+2014 0 träffar i synlig text; inga nya inline-hex (gate 48).
6. Skärmbilder: `?preview=process-01` till `07` vid 1440 och 390; tolv ramar genom `#process`s liv vid 1440 (som `shots/fasA/v3c-giant/`); heron vid `--flip` 0 / 0,25 / 0,5 / 0,75 / 1 efter plan 011; 320 / 375 / 414 / 768 hela sidan. Allt i `{{UT_MAPP}}/shots/r5/`. **Läs varje bild som pixlar**, `läst: <fil>` i NOTES.md, och skriv F-007 bild för bild mot plan 010:s målbildstabell: `matchar` eller `avviker: <vad>`.
7. Feel check ur plan 010 § Verification, skriven i NOTES.md med vad du såg.

## 4. Invarianter

F-011 rörelsen spelar alltid; ingen `prefers-reduced-motion`. F-014 allt som förflyttar sig
läser `--sc-ps`, utropens opacitet också. `@property` för varje `--p-*`-lokal (F-013).
`will-change` bara via klass i fönstret, genom den befintliga rAF-läsaren. En höjdmekanism
för akten (`min-height` på sektionen och sticky-arket, aldrig `contain-intrinsic-size`
ovanpå). Ingen generering. `PRODUCT.md` § absences: inga kunder utöver de tre, inga tal,
inget team. Fullständig output; måste du pausa: `[PAUSED — Step X]` som sista rad.

## 5. Leverans

- `{{UT_MAPP}}/index.html` med `#process`, tokens, `?preview=process-01…07`, plan 011.
- `{{UT_MAPP}}/shots/r5/`.
- `{{UT_MAPP}}/NOTES.md` § R5: en rad per Step med utfall, banräkningen, F-007-tabellen,
  grinden med kontroll- och sidtal, feel check, låst copy 15/15 bekräftad, och varje
  avvikelse från plan 010 med skäl.
- `{{UT_MAPP}}/BRIEF.md` § decision ledger: raderna ur plan 010 Step 11.

Sista raden i ditt sista meddelande: `R5 klar` eller `[PAUSED — Step X]`.
