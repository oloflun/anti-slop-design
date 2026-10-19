# 011 · Kortvändningens span 3,4, dwell 0,2 och fönster 0,10 till 0,78

- **Status**: TODO (R5, tillsammans med 010)
- **Commit**: b2e1ecd · boardkopian `board/cells/V3c-r8/index.html` md5 `27b7db6d`
- **Severity**: HIGH
- **Category**: Easing & duration (tempo), Purpose & frequency (dead scroll)
- **Estimated scope**: 1 fil, 4 rader

## Problem

Vändningen är sidans topp och den har fel tempo åt båda hållen. Span 2,2 gav en vändning
på 648 px scroll (Anton: "för fort"). Span 4,8 (i dag) ger 2 052 px vändning men lägger
958 px stillastående baksida plus 315 px dwell inne i pinnen: `scroll_verify` rapporterar
band 2 700 till 3 300 med diff **0,0** vid 1440 och 2 529 till 3 091 vid 390
(`shots/fasA/probe/scroll-verify-1440.txt`, `-390.txt`). Läsaren scrollar 1 273 px utan att
något händer. `HELHET.md` § 2, tabellen "Tempot i kortvändningen"; Q25.

```html
<!-- index.html:636 - current -->
<section class="hero" id="hero-section" data-sc-act="pin" data-sc-span="4.8" data-sc-dwell="0.35">
```

```css
/* index.html:286-287 - current */
    --t:clamp(0,calc((var(--sc-ps,0) - 0.12) / 0.6),1);
    --flip:calc(var(--t) * var(--t) * (3 - 2 * var(--t)));
```

```js
/* index.html:877-878 - current */
    /* smoothstep(0.12, 0.72, ps) korsar 0,5 exakt vid ps = 0,42. */
    setFace(ps >= 0.42);
```

## Target

Vändningen tar 1 300 till 1 600 px scroll vid 900 vh (H-18) och den statiska svansen
inklusive dwell är högst 700 px (H-17). Vid 1440x900: pinnad resa (3,4 − 1) · 900 = 2 160 px,
vändning 0,68 · 2 160 = 1 469 px, svans 0,22 · 2 160 + 0,2 · 900 = 655 px.

```html
<!-- target, index.html:636 -->
<section class="hero" id="hero-section" data-sc-act="pin" data-sc-span="3.4" data-sc-dwell="0.2">
```

```css
/* target, index.html:286 (287 oförändrad) */
    --t:clamp(0,calc((var(--sc-ps,0) - 0.10) / 0.68),1);
```

```js
/* target, index.html:877-878 */
    /* smoothstep(0.10, 0.78, ps) korsar 0,5 exakt vid ps = 0,44. */
    setFace(ps >= 0.44);
```

Kommentaren `index.html:278-284` skrivs om till de nya talen (0,10 / 0,78, "ps 0 till
0,10 stilla", "0,78 till 1 baksidan i vila").

## Repo conventions to follow

- Fönstret räknas i ren CSS ur `--sc-ps` (`index.html:278-296`); ingen JS rör `--flip`
  utom `?preview=` (`index.html:966-976`), som är oförändrad.
- Sidans egen loop räknar progress ur `scrollY` (`index.html:867-879`) och bevakar bara
  två gränser; tröskeln 0,44 följer fönstrets mitt exakt som 0,42 följde det gamla.
- Ledgerrad finns redan: `BRIEF.md` § Arkitektens rader, "Kortvändningens tempo".

## Steps

1. Byt `data-sc-span="4.8"` → `"3.4"` och `data-sc-dwell="0.35"` → `"0.2"` på rad 636.
2. Byt `0.12) / 0.6` → `0.10) / 0.68` på rad 286.
3. Byt `ps >= 0.42` → `ps >= 0.44` på rad 878 och kommentaren på rad 877.
4. Uppdatera kommentarerna rad 278-284 och rubrikkommentaren rad 35-38 (span 2.2 står kvar
   där) till 3,4 / 0,2 / 0,10 till 0,78.

## Boundaries

- Rör inte `scale(...)`-parabeln (rad 296), `perspective` (rad 275), `overflow:clip`
  (rad 276): plan 004 äger klippningen.
- Rör inte `?preview=`-lägena.
- Matchar inte raderna 286, 636 eller 877-878 (byggaren R4 kör parallellt): STOPPA och
  rapportera i NOTES.md.

## Verification

- **Mekaniskt:** `scroll_verify.py` vid 1440x900 och 390x844: inget `deadScroll`-band med
  diff < 0,01 utanför 0 till ~380 px (ps 0 till 0,10 = 216 px + fold); band med diff 0,0
  inne i pinnen = 0. `motion_probe.py --track "section.hero:--sc-ps,.plate-card:transform"
  --cpu 4`, 100:60 och 20:120, nedåt och uppåt (kontrollen ren först): staircase 0,
  `--sc-ps` max_step ≤ 3 %.
- **Feel check:** scrolla folden kallt med hjulet: kortet börjar vändas inom två hack,
  vändningen tar ungefär femton hack, baksidan står stilla i högst sex hack innan
  bandet kommer. Uppåt: samma i omvänd ordning, ingen omkastning. Tolvstegs ramsekvens
  (`scratchpad/frames.py flip`) vid 1440 och 390: inga klipp vid något värde.
- **Done when:** scroll_verify utan diff-0,0-band i pinnen vid båda bredderna, proben
  grön på staircase och max_step, H-17 och H-18 bockade i `HELHET.md`.
