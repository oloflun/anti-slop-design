# K1 Skymning — NOTES, runda 6 (kritikertrion, verifierade fynd)

Tretton verifierade fynd (4 blockerande, 3 större, 1 mindre, 5 a11y), rättade i given
ordning. Ett av fynden (8) avslöjade en genuin spänning mellan två tidigare rundors
lösningar — se eget avsnitt nedan.

## Blockerande

### 1. Ramen gick inte att klicka i rörelseläge

**Rotorsak, bredare än rapporterat:** inte bara `.exit-frame-wrap` (z-index 3,
`position:absolute;inset:0`) täckte hela scenen även vid opacitet 0 — samma sak gällde
`.exit-copy` (z-index 5, träffade `elementFromPoint` vid punkt 1000,600 i stället för
ramen) och `.loading-indicator` (opacitet hanteras manuellt i JS, aldrig `data-sc-cue`,
så motorns automatiska pointer-events-växling för cue-element gäller aldrig den). Tre
element, samma felklass: en fullbredds/fullhöjds `position:absolute`-yta som blockerar
träffytan även när den är osynlig.

**Fix:** `pointer-events: none` permanent på alla tre — inget av dem har eget
klickbart innehåll (bara bilder/text, inga länkar).

**Kontrollerat:** `elementFromPoint` på fem punkter (tre begärda + två egna) vid p=0,6
— alla fem träffar `<iframe>`. Upprepad klickning på Hōrais egen Reservations-knapp
INUTI ramen lyckades (Playwright `.click()`).

### 2. Sista aktens avslöjande stannade på hälften

**Rotorsak:** motorns flow-progressformel (`p=(y+vh-top)/(height+vh)`) antar att en
sektion kan scrollas en HEL viewport förbi sin egen topp — sant för en sektion med mer
innehåll under sig, falskt för sidans SISTA sektion. Med `#landing` som sista element
och `height=vh` gav formeln exakt `p=0,5` vid maximal scroll, oavsett viewport.

**Fix:** en egen `--landing-p` (`applyLanding()` i script.js), räknad mot den faktiskt
nåbara scrollsträckan (`scrollHeight - innerHeight`), aldrig motorns `--sc-p` för det
elementet. `.landing-night`s `clip-path` läser nu `--landing-p`.

**Kontrollerat:** `--landing-p` = `1.0000` vid maximal scroll på alla tre begärda
viewportar (1440×900, 1440×700, 390×844) — läst direkt, inte antaget. Skärmbild vid
390×844 (`shots/r6-landing-390x844.png`) läst: nattfotot fullt öppnat, inget svart
band kvar.

### 3. Ramen fångade mushjulet i reduced motion

**Fix:** reservlägets sektion är nu en statisk skärmbild (`demo-horai.webp`) + en
typsatt länk `Öppna Hōrai →`, ingen `<iframe>` alls i den grenen.

**Kontrollerat:** `document.querySelectorAll('iframe').length === 0` i reduced
motion. Sex hjultick över bildens yta flyttade sidans `scrollY` från 1800 till 3600
(exakt 6×300px) — mushjulet styr sidan, inget fångar det. Skärmbild
(`shots/r6-rm-frame.png`) läst: skärmbild + länk, korrekt.

### 4. Tab hoppade från toppbaren till sidfoten

**Fix:** tre typsatta länkar (`Öppna Calyx →`, `Öppna Hōrai →`, `Öppna Hyperborea →`,
K2:s register) i bevisradens tre uppslag, i BÅDA lägena (motion och reservläge).

**Kontrollerat:** Tab-vandring från toppbaren (`shots/r6-tab-focus.png`,
`-focus-light.png`) — ordningen är nu logga → kontakt → Öppna Calyx → Öppna Hōrai →
Öppna Hyperborea → landningens kontaktlänk. Ramen ligger kvar i tab-ordningen medan
den är synlig (oförändrat, `visibility:hidden` tar automatiskt bort dolda element ur
tab-ordningen).

## Större

### 5. Fylld amberbricka bakom 01/02/03

**Fix:** `.proof-row__num` är nu ren text i en ny token `--amber-ink` (#8a5a12, samma
ton som `--sc-accent` men mörkad tills den håller som liten text — `--sc-accent-ink`
fanns redan men är till för text PÅ accenten, inte accenten SOM text). Ingen bakgrund,
ingen padding-brygga.

### 6. Glaslagret lästes som ett moiré-mönster

**Fix:** `.window-glass` fick `filter: blur(1px)`, och JS-opaciteten sänktes (var
0,15–0,55, nu 0,10–0,32). Kontrollerat mot `?preview=window`
(`shots/r6-preview-window.png`): ordmärket "HŌRAI" och underraden läses tydligt,
spröjsen syns som en mjuk textur, inte ett skarpt rutmönster.

### 7. Artefakterna i rutorna 40–60

Mildrat, inte dolt, som orkestreraren bad om — reshoot är ett beslut mellan
orkestreraren och Anton, inte gjort här:
- `warpStreet()`: rutorna 38–62 passerar nu på 60 % av sin tidigare scrollsträcka
  (brytpunkter i frame-fraktion 0,374→0,616 komprimerade från t1-bredd 0,242 till
  0,1452); den friställda sträckan (0,0968 av t1) lades på den efterföljande
  inzoomningen mot fönstret, som nu tar längre tid — långsammare, mer avsiktlig.
- En mjuk vinjett (`.sig-vignette`, topp 0,25) i högra tredjedelen, bara rutorna
  34–66 (mjuk ramp in/ut runt 38–62).

**Kontrollerat:** `shots/r6-vignette.png` läst vid den ruta där vinjetten är som
starkast — lyktstolpen och skylten är synligt dämpade i högerkanten utan att bilden
mörknar överallt.

## Mindre

### 8. Kollisionsrutan vid 44 %

Det här fyndet avslöjade en verklig spänning mellan tre tidigare beslut som jag löste
tillsammans i stället för var för sig:

1. **Geometrisk kontroll visade att den krympta bilden ALDRIG helt lämnar rubrikens
   yta** vid rubrikens ursprungliga bottenposition (uppmätt: rubrikens överkant vid
   59,6 % av viewporthöjden; bildens undre kant, även vid minsta skala, stannar vid
   ~69 % — ett kvarstående, om än litet, geometriskt överlapp oavsett tajmning).
2. Men den vita svepningen (`.exit-sweep`) täcker samma yta INNAN rubriken behöver
   visas, så bilden är osynlig (bakom det ogenomskinliga vita) långt innan
   överlappet spelar någon roll — den geometriska analysen var alltså ett
   överarbetat spår; den riktiga variabeln är NÄR svepningen har täckt rubrikens
   yta.
3. Ett första fixförsök (rubrikens cue senarelagd till 0,94) körde rakt in i **en
   annan, redan existerande spänning**: runda 5:s `-62vh`-marginal på `#proof` (satt
   för att stänga den tomma vita luckan) lät bevisraden börja måla ÖVER hela
   signaturaktens innehåll redan vid ungefär p=0,93 — tidigare än den nya, sena
   rubriktajmningen hann bli klar. Bekräftat med `elementFromPoint`: vid p=0,95
   visade `.sc-wrap.proof-row`, inte rubriken, trots att rubrikens EGEN opacitet var
   1 (ett stapelordningsproblem, inte en cue-bugg).
4. Löst genom att korta svepningens eget fönster (`data-sc-reveal-at` från "0,72 1"
   till "0,72 0,88" — svepningen täcker rubrikens yta klart vid ~p=0,79 i stället för
   att aldrig riktigt hinna före p=1) och sätta rubrikens cue i det nu öppna fönstret
   (0,79–0,86 ungefär, håller till akten släpper): `data-sc-cue="0.79 1 0.06 0"`.
   En första version av den cuen (`"0.79 0.84 0.3 0"`) hade en division-med-noll-bugg
   (rOut=0 med `to` satt till ett tal som INTE är aktens slut ger `outStart=to`, en
   nollbred uttoningsfas) som gjorde att rubriken försvann igen direkt efter p=0,84 —
   hittad och rättad genom att läsa `elementFromPoint` vid flera p-värden, inte genom
   att bara lita på cue-syntaxen.

**Kontrollerat:** `elementFromPoint` vid p 0,75–1,0 i 0,01–0,03-steg
(`shots/r6-collision-fix2-90.png` läst) — rubrikens egna textspann äger punkten
kontinuerligt 0,80–0,92, ingen bild, ingen bevisrad, innan bevisraden tar över rent
vid ~0,93.

## A11y-fynd

### 9. Focus-ringen i ljus zon

**Fix:** `.topbar.zone-light :focus-visible, .proof-section :focus-visible,
.ledger-section :focus-visible { outline-color: var(--ink-on-white); }` — bredare än
bara toppbaren, eftersom samma problem skulle drabba de nya bevisrads-länkarna.

**Kontrollerat:** Tab-vandring, `outlineColor` läst per stopp — `rgb(23,24,27)`
(`--ink-on-white`) på loggan/kontakten/alla tre bevisradslänkar, `rgb(242,196,107)`
(`--sc-accent`, amber) på landningens mailto. Skärmbilder av båda lästa
(`shots/r6-tab-focus.png`, `-focus-light.png`) — ringen syns tydligt i båda zonerna.

### 10. Toppbaren bytte aldrig zon i reduced motion

**Rotorsak, en nivå djupare än rapporterat:** att flytta zonlogiken till en delad
`initTopbarZones()` (som fyndet bad om) räckte INTE ensamt — funktionen observerar
`[data-topbar-zone]`-element, och det attributet fanns bara på motion-lägets sektioner
(`#proof`, `#ledger`, `#landing`), som är `display:none` i reduced motion.
`display:none`-element korsar aldrig en `IntersectionObserver`. Hittat genom att
faktiskt kontrollera `zone-light` efter fixen och se att den fortfarande var `false`.

**Fix:** `data-topbar-zone` tillagt på motsvarande `.rm-section`-element också.

**Kontrollerat:** `zone-light` = `true` över `.rm-section--proof`, `false` (mörk) över
`.rm-section--landing`. Skärmbild (`shots/r6-rm-zone2.png`) läst: `kontakt@alunix.se`
i toppbaren är mörk ink över den ljusa Design-sektionen.

### 11. `#topbar-label` hade `aria-hidden="true"`

**Fix:** attributet borttaget. Kontrollerat: `getAttribute('aria-hidden')` → `null`.

### 12. `.exit-frame` alt-text

**Fix:** ändrad till `Hōrai, startsidan, mörk restaurangidentitet med
serifwordmark.` (samma mönster som bevisradens motsvarande bild), i stället för att
beskriva animationen ("skärmbild som krymper...").

### 13. Ingen laddningsindikator; klassbytet väntade på ett nätverksanrop

**Fix:** `document.documentElement.classList.toggle('motion', !reduce)` körs nu
FÖRST, synkront, direkt vid skriptkörning — `window-track.json` hämtas separat, inuti
`startMotion()`/`renderStatic()`, och bara fönstermasken väntar på den (allt annat i
`applySignature()` är skyddat med `if (!track)`-kontroller som beter sig som
"ruta < 58"). En stillsam rad `Laddar …` i sajtnamnsradens position, opacitet satt i
JS efter `seq.loaded < seq.count`.

**Kontrollerat:** `html.motion`-klassen finns omedelbart efter `DOMContentLoaded`
(innan någon rimlig nätverksrundtripp hunnit slutföras). `loading-indicator`s opacitet
läst direkt (`1`) och efter 2 s (`0`, sekvensen laddad).

## `scroll_verify.py`, båda lägena

`shots/r6-sv-report.json` (motion), `shots/r6-sv-rm-report.json` (reduced) —
kompletta filer, sammanfattning:

```json
// motion
{
  "deadScroll": [{ "from": 2100, "to": 2400, "diff": 0.0005 }],
  "cuesNeverFull": [],
  "unrevealed": ["P.loading-indicator:Laddar …"],
  "contrastUnderMedia": [
    { "text": "", "worst": 1.15, "floor": 4.5 },
    { "text": "kontakt@alunix.se", "worst": 2.45, "floor": 4.5 },
    { "text": "Er hemsida är nutidens visitkort", "worst": 1.11, "floor": 3.0 },
    { "text": "Vi skapar skräddarsydda webbplatser som ", "worst": 1.03, "floor": 3.0 },
    { "text": "Calyx · Hōrai · Hyperborea", "worst": 1.56, "floor": 4.5 },
    { "text": "Laddar …", "worst": 1.16, "floor": 4.5 },
    { "text": "VI BYGGER ERT VARUMÄRKE.", "worst": 1.55, "floor": 3.0 },
    { "text": "Webbdesign, design och system. Allt på e", "worst": 2.15, "floor": 3.0 }
  ],
  "blankBands": [{ "from": 859, "to": 3982, "px": 3123 }, { "from": 6645, "to": 7675, "px": 1030 }]
}
// reduced motion
{
  "deadScroll": [], "cuesNeverFull": [], "unrevealed": [],
  "contrastUnderMedia": [{ "text": "", "worst": 1.15, "floor": 4.5 }],
  "blankBands": []
}
```

**Alla motion-lägets fynd undersökta, ingen ny verklig regression** — samma
verktygsartefakt som runda 4/5 dokumenterade, nu på FLER textelement eftersom denna
runda lade till flera nya scroll-/kinetic-drivna texter (bevisradslänkarna,
laddningsindikatorn, den senarelagda rubrikcuen):

- `unrevealed` för `.loading-indicator`: förväntat — elementet har medvetet ingen
  `data-sc-cue`/`data-sc-in` (opaciteten sätts manuellt i JS baserat på
  laddningsstatus, inte scrollposition), så motorns egen "aldrig avslöjad"-kontroll
  känner inte igen dess reveal-mekanism. Kontrollerat direkt: opacitet `1` vid
  sidladdning, `0` efter att sekvensen laddat klart — fungerar som avsett.
- Samtliga `contrastUnderMedia`-poster utom den återkommande tomma texten är
  scroll-/kinetic-drivna textelement samplade av verktygets FASTA rutnät mitt i en
  avsiktlig ton- eller reveal-övergång, inte i vila. Kontrollerat direkt för de två
  NYA posterna (`Laddar …`, `VI BYGGER ERT VARUMÄRKE.`): båda `opacity:1` vid sina
  respektive formade lägen (`shots`-kontroller ovan). `kontakt@alunix.se` (2,45:1) är
  samma post som redan verifierades legitim i runda 4/5 (utmärkt kontrast i varje
  skärmbild jag faktiskt läst; texten är ALDRIG delvis genomskinlig i vila, bara
  under den 300ms-CSS-övergången när `is-dim`/`zone-light` växlar).
- `blankBands` (859-3982, 3123px) är samma fenomen som tidigare — en enda, nu
  SAMMANHÄNGANDE pinnad akt (500vh) läser som ett stort "nästan enhetligt" fält i en
  hopfogad helsidesbild, exakt vad SKILL.md namnger som ett känt
  avläsningsfenomen för pin/scrub-akter, inte tomhet i sig (bekräftat: varenda
  procentruta jag faktiskt läste den här och tidigare rundor visar rikt innehåll).

## `Skill(design-verify)`, fyra brytpunkter

320/375/414/768, batchat JS-prob: inget horisontellt överflöde, `overflow-x:clip` på
html och body, inga trasiga bilder, inga nätverksfel, exakt 1 `<iframe>` vid varje
brytpunkt, konsolen ren (bara Hōrais kända Tailwind-varning). `smallTargets` steg
från 3 till 5–6 — de nya "Öppna X →"-länkarna och reservlägets "Öppna Hōrai →" är
alla inline-textlänkar (samma WCAG-undantag som redan noterades för
kontaktlänkarna i runda 4), inte knappar.

## Skärmbilder lästa denna runda

`r6-landing-390x844.png`, `r6-preview-window.png`, `r6-rm-frame.png`,
`r6-vignette.png`, `r6-collision-83/90.png` (två omgångar, fyra bilder, innan/efter
fixen), `r6-tab-focus.png`, `r6-tab-focus-light.png`, `r6-rm-zone.png`/`-zone2.png`,
`r6-loading-indicator.png`. Plus samtliga `sv`/`sv-rm`-kontaktark. Omkring 15
skärmbilder faktiskt öppnade och bedömda, utöver de rena JS-kontrollerna
(`elementFromPoint`, `getComputedStyle`, `--landing-p`-läsning) som inte kräver en
bild men ändå kördes och lästes som text.

## Fynd jag inte kunde rätta, och varför

Inget av de tretton fynden lämnades orättat. Fynd 7 är uttryckligen en mildring, inte
en fullständig lösning — orkestreraren avgör med Anton om klippet ska tas om; jag har
inte försökt dölja eller ersätta materialets egna artefakter bortom vad instruktionen
bad om.
