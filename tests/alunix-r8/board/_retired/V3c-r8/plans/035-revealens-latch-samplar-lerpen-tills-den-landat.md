# 035 · Revealens latch samplar shimens lerp tills den landat, inte bara vid scroll-händelser

- **Status**: TODO (R9, loop 3)
- **Commit**: R8-läget av `runs/V3c/index.html`, md5 `70214a22`
- **Severity**: HIGH (funktionsfel: tangentbords-, scrollbar- och programmatisk scroll lämnar Calyx och Hōrai helt eller delvis klippta; a11y F-03-klassen: PageDown-användaren ser aldrig Hōrai)
- **Category**: Funktion (states/reveal), H-27, H-08, F-014, gate 94; leadens R8-fynd 1
- **Estimated scope**: 1 fil, ~12 rader JS i `readState`, 0 rader CSS, 0 rader markup
- **Källor**: leadens pixelläsning R8 (`shots/r8-lead/frames-wait-4600.png`: `--rv` 0,94 → 1 med hjul, 0,0375 PageDown, 0,0714 `scrollTo`); loop 3 `shots/loop-3/latch_diag.json` (fyra scrollsätt före/efter, tal nedan), `slices-1440/v3c-1440--s04.png`, `s05.png` (ramarna helt klippta vid `scrollTo`-fångst), `slices-1440-fix/v3c-1440--s04.png`, `s05.png` (samma skivor med fixen injicerad: Calyx och Hōrai hela), `slices-390-fix/v3c-390--s04.png`, `s06.png`

## Problem

Plan 031 gjorde revealen till en latch ur shimens lerpade aktvärde (`act.cur`). Latchen
räknas i `readState` (rad 1671 till 1685), och `readState` körs bara ur `schedule()`, som
bara scroll- och resize-händelser anropar (rad 1716 till 1718). Shimen fortsätter lerpa
`cur` mot målet i ~30 bildrutor **efter** sista scroll-händelsen (`sc-smooth.js` `tick()`,
`if (live) raf = requestAnimationFrame(tick)`), men ingen samplar `cur` igen. Värdet
`--rv` fryser därför vid den nivå `cur` hade i sista scroll-händelsens bildruta:

| scrollsätt till scrollY 4 703 (`.horai-fig` `--sc-ps` 0,58) | `--rv` Hōrai | `--rv` Calyx | bildrutor där `--rv` skrevs |
|---|---|---|---|
| hjul 100 px / 60 ms | 0,979 | 1 | 10 |
| PageDown | 0,207 | 1 | 1 |
| `window.scrollTo` | **0** | **0** | 0 |
| `scrollTo({behavior:'smooth'})` | **0** | **0** | 0 |

(`shots/loop-3/latch_diag.json`, 1440x900, R8-läget.) Ett hjul ger många händelser, så den
sista händelsen ligger nära landningen; ett tangenttryck eller ett scrollbar-drag ger en
eller ett par händelser medan `cur` fortfarande ligger vid starten; `scrollTo` ger en enda
händelse i samma bildruta som shimen adopterar det första värdet. Samma sak drabbar en
läsare som laddar om sidan mitt i bandet (scroll restoration är en programmatisk scroll).

`R.from`/`R.to` (0,02 till 0,30 och 0,10 till 0,55) stämmer mot flow-aktens spann
(`raw = (y + vh − top) / (h + vh)`, `scrollcraft.js` rad 831): irisen är helt öppen vid p
0,55, figuren centrerad vid p 0,68. `R.sel` matchar rätt akt (`a.el === .horai-fig`,
verifierat i `latch_diag`). Felet är samplingen, inte fönstren eller matchningen.

```js
/* index.html:1671-1685 - current: loopen körs bara när readState körs, dvs per scroll-händelse */
    for (var r = 0; r < reveals.length; r++){
      var R = reveals[r];
      if (!R.act) R.act = (window.__scSmooth && window.__scSmooth.acts || []).filter(function(a){ return a.el.matches(R.sel); })[0] || null;
      var act = R.act;
      var cur = act && !isNaN(act.cur) ? act.cur : 0;
      var t = Math.min(1, Math.max(0, (cur - R.from) / (R.to - R.from)));
      t = t * t * (3 - 2 * t);
      if (t > R.v + 0.002){ R.v = t; R.el.style.setProperty('--rv', t.toFixed(4)); }
    }
```

## Target

Latchen bryts ut i en egen funktion `latchTick` som schemalägger sig själv med `rAF` så
länge någon reveal ligger under 1 **och** dess akt fortfarande lerpar (`|--sc-p − cur| >
DEAD`, båda lästa ur inline-stilen respektive shimens objekt, ingen `getComputedStyle`).
När alla reveals står på 1, eller ingen akt rör sig, slutar loopen; efter revealen sker
noll skrivningar (031:s kontrakt står). `readState` anropar `kickLatch()` i stället för
loopen. Samma fönster, samma smoothstep, samma `--rv`, samma CSS.

```js
/* target, index.html: ersätter loopen i readState */
  var latchRaf = null;
  function latchTick(){
    latchRaf = null;
    var again = false;
    for (var r = 0; r < reveals.length; r++){
      var R = reveals[r];
      if (!R.act) R.act = (window.__scSmooth && window.__scSmooth.acts || []).filter(function(a){ return a.el.matches(R.sel); })[0] || null;
      var act = R.act;
      if (!act || isNaN(act.cur)){ again = true; continue; }
      var t = Math.min(1, Math.max(0, (act.cur - R.from) / (R.to - R.from)));
      t = t * t * (3 - 2 * t);
      if (t > R.v + 0.002){ R.v = t; R.el.style.setProperty('--rv', t.toFixed(4)); }
      var target = parseFloat(act.el.style.getPropertyValue('--sc-p'));
      if (R.v < 1 && !isNaN(target) && Math.abs(target - act.cur) > 0.0005) again = true;
    }
    if (again) latchRaf = requestAnimationFrame(latchTick);
  }
  function kickLatch(){ if (!latchRaf) latchRaf = requestAnimationFrame(latchTick); }
  /* i readState, där loopen stod: */
  kickLatch();
```

`again = true` när akten ännu inte finns (`collect()` väntar på `DOMContentLoaded`) ersätter
R8:s lazy-upplösning; loopen står stilla så fort båda `--rv` är 1. Tröskeln 0,0005 är
shimens `DEAD`; läs den ur `window.__scSmooth.dead` om handtaget finns.

Två tillägg ur Astra loop 3 (fix 1, verifierade mot filen):

- **Aktobjektets identitet.** `sc-smooth.js` `collect()` (rad 79) skapar **nya** aktobjekt
  vid varje `resize` (rad 146), men `R.act` cachas för alltid (rad 1679): efter en resize
  före bandet läser latchen ett dött objekt vars `cur` aldrig uppdateras, och `--rv` fryser.
  Lös akten per tick i stället för att cacha den: `var act = acts.filter(function(a){ return
  a.el === R.fig; })[0]` där `R.fig = R.el.closest('[data-sc-act]')` sätts en gång vid
  mount (sex akter, en jämförelse var; ingen `matches`). `R.act`-fältet tas bort.
- **Exakt 1.** Tröskeln `t > R.v + 0.002` kan lämna `R.v` vid 0,998 till 0,999 för alltid
  (irisen 77,9 % i stället för 78 %). Skriv `1` exakt när `t >= 1 && R.v < 1`, annars
  tröskeln som förut.

Samma mätning med fixen injicerad i sidan (loop 3, `latch_diag.json`, `fix: true`):

| scrollsätt | `--rv` Hōrai | `--rv` Calyx | bildrutor där `--rv` skrevs |
|---|---|---|---|
| hjul | 0,9998 | 1 | 50 |
| PageDown | 0,9995 | 1 | 32 |
| `scrollTo` | 1 | 0,9988 | 15 |
| smooth `scrollTo` | 1 | 0,9988 | 15 |

Alternativ som inte tas: en `onTick`-krok i `sc-smooth.js` skulle ge samma sak men rör
shimens kontrakt (keep); en CSS-`transition` på `--rv` bryter F-014 (allt som rör sig läser
det lerpade värdet).

## Repo conventions to follow

- `--sc-ps`-kontraktet rörs inte (LERP 0,16, DEAD 0,0005, `inherits:true`); `sc-smooth.js` rörs inte i den här planen.
- Ingen `getComputedStyle` per bildruta (F-013); `--sc-p` läses ur `act.el.style` som shimen gör.
- Ramen rörs aldrig; wrappern klipps (plan 018, 031); `is-asleep` (027) rörs inte.
- `@property --rv` (rad 656) står; `initial-value: 1` är no-JS-golvet.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R9: "Revealens latch samplar lerpen per bildruta tills den landat".

## Steps

1. Lägg `latchTick`/`kickLatch` enligt Target före `readState` (efter `reveals`-listan, rad 1516 till 1523, som står kvar oförändrad) och ersätt loopen på rad 1671 till 1685 med `kickLatch();`.
2. Mät fyra scrollsätt till samma scrollY (`.horai-fig.top + 0,58·(h + vh) − vh`, ≈ 4 703 vid 1440x900): hjul 100 px / 60 ms, PageDown (450 ms mellan tryck), `window.scrollTo`, `scrollTo({behavior:'smooth'})`; vänta 2,5 s; läs `--rv` på båda wrapparna ur inline-stilen. Mål: ≥ 0,99 på alla åtta värden. Skriv tabellen (scratchskript som `shots/loop-3/scripts/latch_diag.py`).
3. Räkna `--rv`-skrivningar i en rAF-logg efter att båda står på 1 och läsaren scrollar vidare 3 000 px: 0 skrivningar; och loopens `latchRaf` är `null` (loopen står stilla).
4. Scrolla upp från priset till tesen med hjul: `--rv` 1 på båda hela vägen (latchen backar aldrig).
5. Ladda om sidan med scrollY mitt i bandet (Playwright: `goto`, `scrollTo(0, 4703)`, `reload`, vänta 3 s): `--rv` 1 på Hōrai (scroll restoration är programmatisk scroll).
5b. Resize före bandet (Playwright: `set_viewport_size` 1440x900 → 1280x800 vid scrollY 1000, sedan hjul ner till 4 703): `--rv` 1 på båda (aktobjekten byttes av `collect()`, latchen följde med). Kontroll: `latch_diag` med `fix: true` men `R.act` cachat ger 0 här; det är felet Astra fann.
6. Tolv ramar genom `.calyx-fig` och `.horai-fig` (som `frames.py life`): revealen löper 0 → 1 i samma fönster som R8 (`shots/r8/calyx12-*`, `horai12-*` är målbilden).
7. `motion_probe.py --track ".horai-wrap:clip-path"` cpu 1, 100:60, start `.horai-fig.top − 900`: staircase 0; är spåret DEAD enligt proben, läs `--rv` per frame i rAF-loggen från steg 3 och skriv max_step.

## Boundaries

- Rör inte `sc-smooth.js`, motorn, `is-asleep`/`content-visibility`, fönstren `from`/`to` eller CSS-raderna 651 till 658.
- Ingen `transition` på `clip-path` eller `--rv`.
- Matchar inte rad 1516 till 1523, 1671 till 1685 eller 1716 till 1718: STOPPA.

## Verification

- **Mekaniskt:** steg 2 (åtta värden ≥ 0,99), 3 (0 skrivningar, `latchRaf === null`), 5 (reload); `a11y_scan.py` 0; `reflow.py` 320 + 200 % rent.
- **Skärmbild:** skivorna `s04`, `s05` vid 1440 och `s04`, `s06` vid 390 tagna med `scrollTo` (som `slices.py`) visar Calyx och Hōrai hela: målbilder `shots/loop-3/slices-1440-fix/v3c-1440--s04.png`, `s05.png`, `slices-390-fix/v3c-390--s04.png`, `s06.png`. Före fixen: `shots/loop-3/slices-1440/v3c-1440--s04.png`, `s05.png` (rå grund där ramarna ska stå).
- **Feel check:** PageDown fem gånger från folden: irisen öppnar sig mjukt över Hōrai och står öppen; hjul upp igen: den stänger sig inte.
- **Done when:** H-27 står bockad utan not; steg 2:s tabell i NOTES § R9.
