# 039 · Sidans lägen följer det lerpade värdet: kortsidan, `is-turning` och stegens grupper läser shimens `cur`, inte rå scrollY

- **Status**: TODO (R9, loop 3)
- **Commit**: R8-läget av `runs/V3c/index.html`, md5 `70214a22`
- **Severity**: MEDIUM (states: den inerta kortsidan och den synliga kan gå isär under en snabb vändning; `will-change` vilar på kortet så länge läsaren står inne i pinnen; ett stort hopp uppåt klipper stegets ritning i stället för att rita den baklänges)
- **Category**: States, F-014, performance.md (ingen vilande `will-change`), H-28; Astra loop 3 fix 2 och 3, verifierade mot filen
- **Estimated scope**: 1 fil, ~20 rader JS; bygger på plan 035:s sampler (`latchTick`)
- **Källor**: `index.html` rad 1655 till 1666 (`ps` ur rå scrollY, `is-turning` på `0,0005 < ps < 0,9995`, `setFace(ps >= 0,44)`), rad 1700 till 1712 (`data-on` av på rå `pps` med hysteres 0,03); `scrollcraft.js` rad 835 (`a.p = dwell(raw, 0.2)` på heron, så `--sc-ps` ≠ rå ps); `sc-smooth.js` `tick()`

## Problem

Tre lägen i sidan läses ur **rå** scrollposition medan det ögat ser drivs av det lerpade
och (för heron) dwell-remappade värdet:

1. **Kortsidan.** `setFace(ps >= 0.44)` (rad 1666) byter `inert` på rå `ps`. Det synliga
   kortet vänder vid `--flip` 0,5, dvs `smoothstep(0,10, 0,78, --sc-ps)` = 0,5 → `--sc-ps`
   = 0,44 **efter** motorns dwell-remapp (`dwell(0,44, 0,2)` = 0,452 i rå ps) och efter
   lerpen (som släpar upp till ~0,1 vid snabbt hjul). Under en snabb vändning, och vid ett
   PageDown-hopp över 90°, är den inerta sidan den synliga i flera bildrutor; efter en
   scrollbar-släppning kan de stå isär tills lerpen landat.
2. **`is-turning`.** Klassen (och därmed `will-change:transform` på `.plate-card`, rad
   401) sätts när `0,0005 < ps < 0,9995`, dvs så länge läsaren **står** inne i pinnen, även
   stillastående i sekunder: en vilande `will-change` (performance.md, R3-fyndet).
3. **Stegens grupper.** `data-on` tas bort när rå `pps < s − 0,03` (rad 1708). Ett hopp
   uppåt större än 0,03 av aktens liv (≈ 140 px vid 1440: ett PageUp är 800 px) släcker
   gruppen (`display:none`) medan `--sc-ps` fortfarande ligger över `s` och banan ritar sig
   tillbaka: ett klipp i stället för en baklängesritning, precis det 025 B4 skulle bort.

## Target

Plan 035:s `latchTick` är sidans sampler av shimens lerpade värde; den får tre konsumenter
till, alla lästa ur `acts[i].cur` (aldrig `getComputedStyle`):

```js
/* target, i latchTick efter reveal-loopen */
  var heroAct = acts.filter(function(a){ return a.el === hero; })[0];
  if (heroAct && !isNaN(heroAct.cur)){
    /* kortsidan följer det värde --flip räknas ur */
    if (previewFace === null) setFace(heroAct.cur >= 0.44);
    /* will-change bara medan kortet rör sig: akten lerpar fortfarande */
    var heroTarget = parseFloat(hero.style.getPropertyValue('--sc-p'));
    var heroMoving = !isNaN(heroTarget) && Math.abs(heroTarget - heroAct.cur) > 0.0005;
    if (heroMoving !== turning){ turning = heroMoving; hero.classList.toggle('is-turning', heroMoving); }
    if (heroMoving) again = true;
  }
  var procAct = process && acts.filter(function(a){ return a.el === process; })[0];
  if (procAct && !isNaN(procAct.cur)){
    for (var i = 0; i < stepAnchors.length; i++){
      /* på: rå pps som i dag (banan får börja utan släp); av: först när det lerpade
         värdet passerat s, dvs när ritningen faktiskt dragit sig tillbaka */
      var stepNum = (i + 1 < 10 ? '0' : '') + (i + 1), g = sheetGroups[stepNum];
      if (!g) continue;
      var on = groupsOn[stepNum] ? procAct.cur >= stepAnchors[i].s - 0.005 : processPs() >= stepAnchors[i].s;
      if (groupsOn[stepNum] !== on){ groupsOn[stepNum] = on; g.toggleAttribute('data-on', on); }
    }
    var procTarget = parseFloat(process.style.getPropertyValue('--sc-p'));
    if (!isNaN(procTarget) && Math.abs(procTarget - procAct.cur) > 0.0005) again = true;
  }
```

`readState` behåller `schedule()`-vägen (scroll/resize → rAF) men lämnar de tre besluten
till `latchTick` (som `readState` sparkar igång via `kickLatch()`); `is-turning` sätts
alltså av samplern första bildrutan efter en scroll-händelse (samma bildruta som i dag)
och tas bort när akten landat. `again` håller loopen vid liv bara medan någon akt
fortfarande lerpar, så en stillastående sida gör noll arbete.

## Repo conventions to follow

- `--sc-ps`-kontraktet rörs inte; `sc-smooth.js` rörs inte.
- `setFace` (plan 022: fokus flyttas före inertering, `.sr-only`-kopian) rörs inte i sak; bara villkoret.
- `previewFace` vinner alltid (022 Step 5).
- Ledgerrad i `BRIEF.md` § Byggarens rader, R9: "Kortsidan, `is-turning` och `data-on` av läser shimens `cur`".

## Steps

1. Efter plan 035: flytta `is-turning`-växlingen och `setFace`-anropet från `readState` (rad 1660 till 1666) till `latchTick` enligt Target; `readState` behåller `ps`-beräkningen bara om något annat läser den (annars bort).
2. Flytta `data-on`-loopen (rad 1700 till 1712) enligt Target: "på" ur rå `processPs()`, "av" ur `procAct.cur − 0,005`.
3. Mät kortsidan: hjul 100 px / 60 ms genom heron med en rAF-logg av `--flip` (ur `getComputedStyle(plateCard)`, bara i mätningen) och `faceBack.inert`: `inert` växlar i samma bildruta som `--flip` passerar 0,5 (± 1 bildruta). PageDown från toppen till scrollY 2 000: samma.
4. Mät `is-turning`: scrolla till scrollY 1 000 och stå stilla 2 s: klassen borta inom 40 bildrutor efter sista scroll-händelsen; scrolla igen: klassen tillbaka i första bildrutan.
5. Mät stegen: stå vid `?preview=process-03`:s scrollY (utan preview), PageUp en gång (800 px): `g[data-step="03"]` behåller `data-on` tills `#process`:s `cur` < `--s3`, och `#p-opening`:s `stroke-dashoffset` går kontinuerligt mot 1px (rAF-logg, max_step ≤ 5 % per bildruta) i stället för att hoppa till `display:none`.
6. `motion_probe.py` hero cpu 1, 100:60, båda riktningarna: staircase 0, max_step ≤ 3 %, p95 inte sämre än R8 (36 / 18 ms).

## Boundaries

- Inga nya lyssnare; samplern är 035:s.
- Matchar inte rad 1655 till 1666 eller 1700 till 1712: STOPPA.

## Verification

- **Mekaniskt:** steg 3 till 6.
- **Skärmbild:** `flip-1440/` tolv ramar oförändrade mot loop 3 (`shots/loop-3/flip-1440/`); previews `front|mid|back` oförändrade.
- **Feel check:** vänd kortet med ett snabbt hjul och stanna mitt i: `Tab` går till den sida du ser; PageUp mitt i processakten: ritningen drar sig tillbaka, klipper inte.
- **Done when:** steg 3 till 5 i NOTES § R9 med tal; H-28 utan not.
