# 028 · Bildtiden: shimen läser inline och batchar sina skrivningar, `--sc-p` slutar ärvas, ordscrubben blir sex element

- **Status**: TODO (R8, loop 2)
- **Commit**: R7-läget av `runs/V3c/index.html`, md5 `d30355da`; `runs/V3c/scroll/sc-smooth.js` (sidans egen shim, 144 rader)
- **Severity**: HIGH (H-21, H-22, H-23, H-32; F-013 orsak 2, öppen sedan R4)
- **Category**: Funktion (bildtid), rörelse; profileringsrundan som loop 1 begärde
- **Estimated scope**: 2 filer: `sc-smooth.js` ~15 rader; `index.html` ~12 rader CSS + ~10 rader JS
- **Källor**: `shots/loop-2/profile/profile.json`, `profile2.json`, `profile3.json`, `profile4.json` (CDP `Performance.getMetrics`-deltan, rAF-bildtider, skrivräknare, ablationer), scratch `synth.py`, `synth2.py`, `synth3.py` (kostnaden för EN skrivning, isolerat, cpu 1), `shots/loop-2/probe/` (motion_probe-matrisen)

## Problem

Sidan tappar bildrutor sedan R4 och alla planer hittills har gissat orsaken. Den här
rundan mätte den. Talen är CDP-deltan under en skriptad hjulscroll (100 px / 60 ms) vid
4x CPU, plus kostnaden för en enda `setProperty` isolerat (120 skrivningar, en per rAF,
cpu 1).

**1. Stilomräkning är kostnaden, inte layout, script eller målning.** Per segment
(`profile.json`): heron task 3,76 s varav RecalcStyle 2,44 s (65 %), layout 0,03 s;
bandet 5,80 / 4,40 s (76 %); processakten 8,85 / 6,75 s (76 %); kontrollen
`tests/motion/smooth.html` 0,82 / 0,19 s. Ramarna är inte felet: bandet med ramarna
blockerade (inga sajter alls) mäter p95 144 ms, med ramarna vakna 240 ms, sovande (R7:s
trasiga läge) 304 ms. Grunden är inte felet (`.ground` display:none: ingen skillnad,
`profile.json process-noGround`). Arket är det delvis: `process-noSheet` p95 106 mot 160.

**2. Vad en skrivning kostar** (ms stilomräkning per skrivning, cpu 1, `synth*.py`):

| skrivning | som byggd | ablation |
|---|---|---|
| `section.hero` `--sc-ps` | 1,81 | `.plate-card` display:none 0,52; `.face--back` 1,17; båda SVG-glyferna 1,28 |
| `section.hero` `--sc-p` (motorns, oregistrerad, ärvs) | 1,84 | registrerad `inherits:false` **0,27** |
| `#giant-section` `--sc-ps` | 2,10 | `.is-scrubbed` bort 1,73; **ordens 60 `<span>` upplösta till text 0,84** |
| `#process` `--sc-ps` | 2,20 till 2,57 | arket display:none 0,74; `#p-glyph` kort `d` 1,95 |
| `.price`, `.panel-thesis`, `#principer`, `footer.close` `--sc-ps` | 0,27 till 0,53 | |
| `:root` `--sc-canvas` (motorns drift, rad 983) | 9,13 | registrerad `inherits:true` 7,30; skriven på `.ground` 0,24 |
| kontrollen `#act` `--sc-ps` | 0,17 | |

Kostnaden är inheritance: en ärvd custom property som ändras på en akt invaliderar
varje ättling, och heron/jätten/processakten har 100-tals ättlingar (kortets båda sidor
med två 2 kB-glyfer, liggarens 60 ordspann med `color-mix`, arkets 30 SVG-element med
`calc`-kedjor). `--sc-ps` MÅSTE ärvas (F-013 efterspel: barnen läser den). `--sc-p`
behöver det inte: ingen `var(--sc-p)` finns i `index.html`, `scrollcraft.css` eller
`scrollcraft.js` (grep, loop 2); motorn läser den aldrig tillbaka och shimen läser den
på aktelementet självt.

**3. Shimen tvingar fram extra omräkningar.** `tick()` (sc-smooth.js rad 76-108) läser
`getComputedStyle(a.el).getPropertyValue('--sc-p')` för varje akt och skriver `--sc-ps`
mellan läsningarna. Motorn har just skrivit `--sc-p` på alla akter i samma frame, så
varje läsning tvingar en synkron stilomräkning, och varje mellanliggande skrivning smutsar
ned nästa läsning: RecalcStyleCount per frame 1,7 (heron), 4,6 (bandet), 3,1 (processakten)
mot 1,0 i kontrollen (`profile4.json`).

**Uppmätt med en batchad shim** (scratch `sc-smooth-batched.js`, route-substituerad i
`profile4.py`: läser `--sc-p` ur `a.el.style` i stället för computed style, skriver alla
`--sc-ps` efter alla läsningar, registrerar `--sc-p` `inherits:false`):

| segment | cpu | som byggd p95 / >33 / recalcs per frame | batchad + inherits:false |
|---|---|---|---|
| heron | 4 | 72,1 ms / 72 / 1,72 | 71,8 / 61 / 1,26 |
| bandet | 4 | 195,5 / 86 / 4,57 | 141,0 / 84 / 1,38 |
| processakten | 4 | 159,5 / 131 / 3,06 | 408,0 (brus, se nedan) / 131 / 1,39 |
| heron | 1 | **35,5 / 14** | **18,8 / 9** |
| bandet | 1 | 35,9 / 23 | 35,6 / 20 (mean 25,9 → 20,3) |
| processakten | 1 | 18,4 / 7 | 22,8 / 13 |

`--sc-ps` max_step 1,4 till 2,4 %, staircase 0 i alla körningar, före och efter: kontraktet
står. Omräkningarna per frame går till ~1,2 överallt; tiden per omräkning står kvar, för
den är subträdens egen kostnad (punkt 2). Maskinen var brusig under loop 2 (kontrollen gav
0 till 2 rutor > 33 ms i varje körning, `probe/probe-log.txt`), så cpu 4-talen svänger
±100 ms mellan identiska körningar; cpu 1-talen är stabila och är målvärdena nedan.

**4. Den dyraste konsumenten som går att göra billig utan att ändra vad ögat ser är
ordscrubben.** 60 spann med `--lit` och `color-mix` per ord (rad 769-771) kostar 1,3 ms per
skrivning på jätten; samma front, ritad som EN gradient per textblock med
`background-clip:text`, kostar sex element. Fronten läser fortfarande `--scrub` ur
`--sc-ps` (F-014), båda ändarna har samma valörer (dämpat bläck 62 % → fullt bläck; 6,3:1
och 18:1 mot papperet, plan 021/R3:s a11y-läsning står).

## Target

**A. Shimen** (`scroll/sc-smooth.js`, sidans egen fil, redigeras; motorn rörs inte):

```js
/* target, sc-smooth.js rad 55-66: registrera även den råa, utan arv */
  try {
    if (window.CSS && CSS.registerProperty) {
      CSS.registerProperty({ name: '--sc-ps', syntax: '<number>', inherits: true, initialValue: '0' });
      /* PLAN 028 B: --sc-p är motorns råvärde, skriven på varje akt varje frame.
         Ingen regel läser var(--sc-p) (grep: index.html, scrollcraft.css/.js), så
         den behöver inte ärvas; oregistrerad ärvs den och invaliderar aktens hela
         subträd per skrivning: 1,84 ms → 0,27 ms på heron (synth3). */
      CSS.registerProperty({ name: '--sc-p', syntax: '<number>', inherits: false, initialValue: '0' });
    }
  } catch (e) { /* redan registrerad, eller utan stöd: lerpen fungerar ändå */ }
```

```js
/* target, sc-smooth.js tick(): läs inline, skriv efter alla läsningar */
  function tick() {
    raf = null;
    var live = false;
    var frozen = !!window.__scFreezeMotion;
    var i, a, t, d;
    for (i = 0; i < acts.length; i++) {
      a = acts[i];
      /* PLAN 028 A: motorn skriver --sc-p som inline-stil; läs den där, aldrig via
         getComputedStyle (som tvingar en synkron omräkning per akt och frame). */
      t = parseFloat(a.el.style.getPropertyValue('--sc-p'));
      if (isNaN(t)) { a.next = ''; continue; }
      if (isNaN(a.cur)) a.cur = t;
      if (frozen) { a.cur = t; }
      else {
        d = t - a.cur;
        if (Math.abs(d) > DEAD) { a.cur += d * LERP; live = true; }
        else if (a.cur !== t) { a.cur = t; }
      }
      a.next = a.cur.toFixed(4);
    }
    for (i = 0; i < acts.length; i++) {
      a = acts[i];
      if (a.next && a.next !== a.last) { a.el.style.setProperty('--sc-ps', a.next); a.last = a.next; }
    }
    if (live) raf = requestAnimationFrame(tick);
  }
```

`collect()` får fältet `next: ''`; `settle()` läser på samma sätt (`a.el.style`). Filens
docstring får ett stycke om varför (F-013 mätte stegning; loop 2 mätte omräkningarna).
`motion_probe.py` läser `window.__scSmooth` oförändrat.

**C. Ordscrubben som gradientfront** (`index.html`): JS-ordindelningen (rad 1710-1728)
tas bort, `.w`-regeln (rad 769-771) ersätts:

```css
/* target, index.html:769-771 */
  /* PLAN 028 C. Fronten som EN gradient per block i stället för 60 ordspann:
     samma två valörer (62 % bläck → fullt bläck), samma --scrub, sex element i
     stället för 60 (2,10 → 0,84 ms per --sc-ps-skrivning, synth3). Vinkeln
     100deg gör att fronten löper i läsriktning över ett flerradigt stycke. */
  .is-scrubbed .scrub-text h3,.is-scrubbed .scrub-text p{
    --edge:calc(var(--scrub) * 130%);
    background-image:linear-gradient(100deg,
      var(--ink) 0 calc(var(--edge) - 12%),
      color-mix(in srgb,var(--ink) 62%,var(--bg)) calc(var(--edge) + 12%) 100%);
    -webkit-background-clip:text;background-clip:text;color:transparent;}
```

`.ledger-body h3` och `.ledger-body p` behåller sina `color`-regler som no-JS-golv (utan
`.is-scrubbed` står texten i fullt bläck, som i dag). JS: `giant.classList.add('is-scrubbed')`
står kvar (rad 1727); ordloopen (rad 1712-1726) stryks. Textnoden förblir en textnod (låst
copy byte för byte, `<h3>`/`<p>` oförändrade i DOM).

**E (mätsteg, Astra loop 2 fix 2):** `--k1..--k7` deklareras på `#process` (rad 888-899) och
ärvs av prosan lika väl som av arket. Flytta de sju deklarationerna till `.process-stick`
(arket och bara arket läser dem; `--sc-ps` ärvs dit från `#process` ändå) och mät en
`#process`-skrivning isolerat (`scripts/synth2.py`-metoden) före och efter. Behåll bara om
vinsten är ≥ 0,3 ms per skrivning; annars återställ och skriv talet (mätt i loop 2:
`.process-steps` display:none sparade 0,6 ms, men det tog bort elementen, inte bara
`--kN`-arvet, så vinsten är oviss).

**D (inte i planen, redovisas):** `--sc-canvas` skrivs av motorn på `:root` (9 ms per
ändring, dokumentomfattande). Den ändras bara medan tesen och jätten är mitt i sitt liv
(motorns `driftT`), 7 till 28 gånger per band-körning, och kan inte flyttas utan att
redigera motorn. Registrering `inherits:true` sparar 1,8 ms per skrivning men gör
`--sc-canvas` till en `<color>` som motorn skriver som `rgb()`-sträng: mätt 7,3 ms, inte
värt en ny mekanism. Står kvar som motorfynd i README § Verktyg.

## Repo conventions to follow

- Shimen är sidans egen fil och får redigeras (`scroll/NOTE.md`: motorn kopieras, aldrig
  redigeras; shimen är vägen runt den). `motion_probe.py` läser `window.__scSmooth.acts`
  och `.settle()`, båda behålls.
- `--sc-ps`-kontraktet (`keep` i alla rapporter): staircase 0, max_step ≤ 3 %, LERP 0,16,
  DEAD 0,0005 oförändrade.
- Ordscrubbens valörer ur plan 021/R3 (62 % → 100 % bläck) står; gate 48: bara tokens
  (`var(--ink)`, `var(--bg)`).
- Ledgerrader i `BRIEF.md` § Byggarens rader, R8: "Shimen läser inline och batchar",
  "`--sc-p` utan arv", "Ordscrubben som gradientfront".

## Steps

1. **Mät före** (samma harness som loop 2, scratch `profile4.py` eller `motion_probe.py`
   med kontrollprotokollet): cpu 1 och cpu 4, 100:60, spår `section.hero:--sc-ps`,
   `#giant-section:--sc-ps` (start `.stagger.top − 600`), `#process:--sc-ps` (start
   `#process.top − 900`). Skriv p95, rutor > 33, RecalcStyleCount/frame.
2. Redigera `sc-smooth.js` enligt A och B. Ladda sidan: konsolen ren; `?preview=front|mid|
   back|ledger|process-03` visar samma formade lägen som i `shots/loop-2/preview/`
   (`__scFreezeMotion` läser fortfarande `a.el.style`).
3. Mät efter A+B: **STOPPA-villkor**: staircase > 0 eller max_step > 3 % på något
   `--sc-ps`-spår, eller `?preview=` som inte fryser: återställ shimen och rapportera.
4. Redigera `index.html` enligt C (CSS-regeln, stryk ordloopen). `?preview=ledger`: fronten
   står fullt tänd (alla ord i fullt bläck). Tolv ramar genom `#giant-section`: fronten
   löper från övre vänster till nedre höger genom varje block, aldrig hela blocket på en
   gång.
5. Mät efter C. Kontrast: `contrast.py`/`contrast_over_media.py --url` på `.ledger-body p`
   vid `--scrub` 0 och 1 (dämpat ≥ 4,5:1, fullt ≥ 7:1 mot `--bg`).
6. Grep `getComputedStyle` i `sc-smooth.js`: 0 träffar i `tick()`.

## Boundaries

- Motorn (`scrollcraft.js`, `scrollcraft.css`) rörs inte. Ingen `will-change`. Inga andra
  konsumenter av `--sc-ps` ändras (kortet, plåten, arket, avslutet).
- `--sc-ps` registreras fortfarande `inherits:true`.
- Ordscrubbens copy (liggarens tre rader, låst) rörs inte; `<h3>`/`<p>` byter inte tagg.
- Matchar inte `sc-smooth.js` rad 55-108 eller `index.html` rad 769-771 / 1710-1728: STOPPA.

## Verification

- **Mekaniskt, målvärden ur mätningen (cpu 1, 100:60, kontrollen ren omedelbart före):**
  heron p95 ≤ 20 ms (mätt 18,8 med A+B; var 35,5); bandet p95 ≤ 25 ms (var 35,9; A+B gav
  35,6 med mean 25,9 → 20,3; C tar bort ~1,3 ms per frame till); processakten p95 ≤ 20
  (mätt 18,4 som byggd, får inte bli sämre än 22). RecalcStyleCount ≤ 1,4 per frame i alla
  tre (var 1,7 / 4,6 / 3,1). staircase 0, max_step ≤ 3 % överallt, båda riktningarna.
  Vid cpu 4: rapportera p95 och rutor > 33 före/efter; baren H-21 gäller fortfarande men
  planen lovar den inte (kvarvarande kostnad är subträdens egen: kortet 1,3 ms,
  arket 1,5 ms per frame vid cpu 1, gånger fyra).
- **Skärmbild:** `?preview=ledger` vid 1440 och 390 identisk i innehåll med
  `shots/loop-2/preview/preview-*-ledger.png` (alla ord fullt bläck); tolv ramar genom
  jätten visar fronten löpa.
- **Feel check:** scrolla genom liggaren i vanlig hjulfart: orden tänds i en front som
  följer läsriktningen, mjukt (lerpad), aldrig hela stycket på en gång; kortvändningen
  och arket känns som förut (A ändrar ingen kurva).
- **Done when:** cpu 1-målen ovan håller i båda riktningarna; H-22 bockas om alla tre
  segment ≤ 20 ms; H-21 bockas bara om cpu 4 når 20 ms/0 rutor (rapporteras).
