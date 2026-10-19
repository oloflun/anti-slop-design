# Alunix r9, V3d runda 1. Cell {{KONCEPT}}. Den inverterade varianten: sju scener, priset i avslutet.

En plan, en runda, visuellt först. Ut-mapp `{{UT_MAPP}}`, port {{PORT}}. Du är en ny session och
känner inte filen: läs innan du skriver.

## 0. Läs först

1. `Skill(design)` som **första** handling, via `Skill`-verktyget. `Skill(animate)` och
   `Skill(emil-design-eng)` **före** du skriver någon rörelse (steg F och E i planen). Alla tre
   namngivna i transkriptet.
2. `tests/alunix-r8/runs/V3c/RAPPORT-LOOPEN.md` i sin helhet. Den förklarar varför förra
   loopen gav nästan ingen synlig förändring. Fem fel du inte upprepar: mekaniska mål i stället
   för visuella, visuellt sist, djärva drag som backas, följdfel, ingen jämförelse sida vid sida.
3. `{{UT_MAPP}}/plans/048-inverterad-variant.md` i sin helhet. Varje värde står där: tokens,
   selektorer, CSS, SVG-koordinater, JS-formler, device-tabellen och beslutet om balansen (G).
4. `{{UT_MAPP}}/PARITET.md`: tabellen du jämför mot och som granskaren dömer efter.
5. `{{UT_MAPP}}/NOTES.md` § Arkitekten (nulägets mätningar) och `tests/alunix-r8/PRODUCT.md`
   § Brand Commitments (den låsta copyn).
6. `{{UT_MAPP}}/index.html`. **Radnumren i planen är ungefärliga.** Hitta varje ankare med
   `Grep` på dess kod. Matchar koden inte planen i sak: skriv en rad i NOTES och fortsätt med
   det planen menar, aldrig med en egen tolkning av beställningen.

## 1. Bygg, i planens ordning A till H

Kirurgiska `Edit`-anrop på `{{UT_MAPP}}/index.html`. **Aldrig `Write` av hela filen**, aldrig
shell-skrivningar (`sed -i`, heredoc) mot UI-filen.

Rör aldrig: motorn `{{UT_MAPP}}/scroll/scrollcraft.js`, `scroll/scrollcraft.css`,
`scroll/sc-smooth.js`; `sites/*`; `runs/V3c/` (någonting där). `@property`-registreringen av
`--sc-ps` (i shimen) rörs inte och inga nya `@property` läggs till. Ingen tredje iframe.

Ordningen är planens: A (priset flyttas), B (adressen), C (akten inverterad), D (jätten
inverterad), E (arket och kameran), F (scenerna), G (balansen), H (jämförelsen). Den visuella
förändringen är uppgiften; ingenting annat i filen ändras.

## 2. Invarianter, bindande

- **Låst copy ordagrant, 15/15** (PRODUCT.md § Brand Commitments; listan har 16 punkter,
  kontrollera varje punkt och skriv ut räkningen). De sju processtyckena och noterna ordagrant.
  **Ingen ny synlig sträng**: planen kräver ingen. Behöver du ändå en, skriv den i NOTES med
  markeringen `[copy-gate]`, i vi-form, utan tal, kunder, tider eller villkor.
- **Noll tankstreck** i synlig text (U+2012 till U+2015), inklusive `alt` och `title`.
- **F-011:** rörelsen spelar alltid. Ingen `prefers-reduced-motion`, ingen statisk
  fallbackgren, ingen läsning av något rörelseval i webbläsaren eller systemet.
- **F-014:** allt som rör sig för ögat läser `--sc-ps` (via `--kN`, `--k`, `--cam`), aldrig rå
  `--sc-p`. Ingen JS skriver stil per bildruta; bandens ticker är ren sticky-scroll.
- Gate 48: varje ny färg är en token i `:root`; noll ny inline-hex (räkna hex utanför `:root` före
  din första `Edit`, skriv talet i NOTES; efter bygget ska det vara samma tal eller lägre). Gate 47/79: Calyx i arket är en riktig produktyta.
- PRODUCT.md: en ram som visats transformeras eller tonas aldrig. `position:sticky` på
  `.calyx-fig` är tillåten (ingen transform); `.rv`-revealen rörs inte.
- Radie 0, inga skuggor, accenten `#1e5e9c` exakt två förekomster.

## 3. Efter bygget: se, jämför, laga i samma runda

Servern: `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten. Sidan: `http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html` ({{UT_MAPP}} relativt repo-roten).

1. **Skivor.** Hela sidan i viewportskivor vid 1440x900 och 390x844 (plain `scrollTo`, 3 s
   väntan per skiva så att ramarna hinner montera) till `{{UT_MAPP}}/shots/r1/slices-1440/` och
   `slices-390/`; `?preview=process-01` till `-07`, `front`, `back`, `ledger` vid båda bredderna
   (`wait_until="load"` + 2 s) till `{{UT_MAPP}}/shots/r1/preview/`. Kontaktark
   `shots/r1/sheet-1440.png` och `sheet-390.png`.
2. **Par-bilder.** För varje rad P01 till P16 i `PARITET.md`: vår skärm i radens läge bredvid
   referensbilden, samma höjd, med PIL, till `{{UT_MAPP}}/shots/r1/par/<id>-1440.png` och
   `<id>-390.png`. Referenserna ligger i `tests/alunix-r8/runs/V3c/shots/fasA/`.
3. **Läs varje bild själv** med `Read`, som bild. Skriv `läst: <fil>` för varje i NOTES. Skriv
   per par-bild en rad: **håller nivån**, eller **håller inte, för att …** med ett mätbart skäl.
4. **Laga det som inte håller, i samma runda.** Ett fynd lagas framåt: större, tydligare,
   bättre placerat. **Backa aldrig ett djärvt drag för att laga ett fel** (en rubrik som bryter
   ordet lagas med radbrytningen eller spaltbredden, inte med en mindre rubrik; ett ark som
   täcker text lagas med bandets höjd, inte med ett mindre ark). Skjut om, jämför om. Högst två
   varv; det som då fortfarande inte håller skrivs som öppet fynd med par-bilden som belägg.
5. **Målen i planens Target-tabell**, varje rad med uppmätt värde bredvid målet: arkets bredd
   vid 1440, 1280, 1024, 768, 390, 320; Calyx-rektangelns andel av arket vid
   `?preview=process-05/06/07` (1440 och 390); stegnummer, stegrubrik och brödtext i px;
   li-höjder och sticky-intervall; adressens font-size och `k`-glyfens höjd ur skärmbilden;
   prisets placering (sista två viewports); ljusbudgeten per skiva (planens § Beslut G punkt 4).
6. **Scrub i båda riktningarna.** Tolvstegs ramsekvens genom steg 03 till 04 vid 1440, ned och
   sedan upp, till `shots/r1/frames/`. Siffrans `color`, rubrikens `--edge` och bandens `top`
   utskrivna per ram: monotona i båda riktningarna, inga hopp.

## 4. Grinden (prestanda och tillgänglighet är en grind, inte målet)

Kontrollprotokollet: `tests/motion/smooth.html` mäts **först** och ska vara ren (inga rutor
> 33 ms); är den inte det, vänta en minut och kör om; efter två brusiga försök mäts sidan ändå
och kontrollens tal skrivs bredvid. Mallen är `tests/alunix-r8/runs/V3c/shots/loop-5/scripts/
probes5.sh`. Den riktade proben (`motion_probe.py` med `--start <scrollY|bottom>`, negativt
hjul för uppåt) kopierar du till `{{UT_MAPP}}/shots/r1/scripts/motion_probe_dir.py`: finns den
inte under scratchpadsökvägen i mallen, gör kopian av `~/.agents/skills/design/scripts/
motion_probe.py` och lägg till `--start` (scrolla till värdet före körningen), inget annat.

1. `scroll_verify.py` vid 1440x900 och 390x844: `cuesNeverFull`, `unrevealed` och
   `contrastUnderMedia` tomma; `blankBands` 0 inom `.stagger`; `blankBands` inne i `#process`
   i helsidesfångsten redovisas som den sticky scenens artefakt och döms på skivorna.
2. `motion_probe`: `#process:--sc-ps` ned och upp (starta ovanför akten respektive nedanför),
   `section.hero:--sc-ps,.plate-card:transform`, `#giant-section:--sc-ps`,
   `#pris:--sc-ps`, `footer.close:--sc-ps`; `--wheel 100:60` och `--wheel 20:120`; cpu 1 och
   cpu 4. Staircase 0 överallt; `max_step` ≤ 3 % på varje `--sc-ps` vid cpu 1. Tal i NOTES.
3. `contrast_over_media.py --url` vid 1440 och 390: prisets och adressens strängar över
   fotot (scroll till `#pris` och till dokumentets slut), akten (`?preview=process-02`, `-06`),
   jätten (`?preview=ledger`). Brödtext ≥ 4,5:1, stor text ≥ 3:1. Faller priset: höj
   `--scrim-close`, krymp aldrig texten.
4. `a11y_scan.py` och `reflow.py` vid 390 och 768 (a11y-audit-skriptens mapp,
   `~/.agents/skills/a11y-audit/scripts/`), `tab_walk.py` vid 1440. Noll HIGH.
5. Noll horisontell scroll vid 320, 375, 390, 768, 1024, 1280, 1440, mätt på elementens
   rektanglar (inte `scrollWidth`); 200 % zoom vid 1440.
6. `?preview=process-0N` vid 1440 och 390: `--sc-ps` = `--eN` ± 0,0001, alla sju, tre
   laddningar per läge vid 390; alla sju `g[data-step]`-grupper får `data-on` (också den nya
   `#p-frame`).
7. Grep: `prefers-reduced-motion` 0; U+2012 till U+2015 0 i synlig text; inline-hex utanför
   `:root` = talet före bygget (arkitektens räkning 2026-09-18: 16 i CSS utan kommentarer, 8 i markup/JS); `@property` oförändrat antal; `data-process` 0 läsare kvar; `getComputedStyle`
   0 träffar i `readState`/`latchTick`.

## 5. Leverans

- `{{UT_MAPP}}/index.html`.
- `{{UT_MAPP}}/shots/r1/`: `slices-1440/`, `slices-390/`, `preview/`, `par/` (P01 till P16 vid
  1440 och 390), `frames/`, kontaktarken, `scripts/`.
- `{{UT_MAPP}}/NOTES.md` § **V3d R1**: planens Target-tabell med uppmätt värde per rad, en
  rad per par-bild (håller nivån / håller inte, för att …), vad du lagade i samma runda och
  hur, grindens tal, `läst: <fil>` för varje bild du läst, avvikelser från planen med skäl.
- `{{UT_MAPP}}/BRIEF.md` § decision ledger, en ny underrubrik `### Byggarens rader, V3d R1`:
  en rad per materiellt val (`--c-drafting`, `--scrim-close`, kameran, bandet, Calyx sticky,
  principerna på papper, adressens storlek).

Fullständig output. Sista raden i ditt svar och i NOTES: `V3d R1 klar` eller
`[PAUSED — steg X]`.
