# 032 · Folden vid 390: högst 12 % död grund under underraden; bandets mobilseams 96 px

- **Status**: TODO (R8, loop 2)
- **Commit**: R7-läget av `runs/V3c/index.html`, md5 `d30355da`
- **Severity**: LOW
- **Category**: Visuellt (balans i folden, seams vid 390), H-13, H-05 (390); öppen sedan fas A, "loop 2, egen höjdbudget" (README § Utanför R7); Astra loop 2 (bilder 18, 20: 84 px slitsar)
- **Estimated scope**: 1 fil, 4 rader CSS i ett befintligt mediablock

## B. Bandets seams vid 390 (H-05)

`.stagger{gap:clamp(64px,10vh,96px)}` i blocket ≤ 900 (rad 549) ger 84 px rå grund mellan
panelerna vid 844 px höjd (`slices-390/v3c-390--s02.png`, `s03.png`). H-05: en seam är
aldrig en slits under 96 px. Panelerna byter material, men slitsen är ändå under golvet.

```css
/* target, rad 549 */
    .stagger{flex-direction:column;gap:clamp(96px,12vh,120px);padding:0 0 0;}
```

Vid 844: 101 px; vid 568: 96 px. Mät: avståndet mellan `.panel-thesis.bottom` och
`.calyx-fig.top` (och de tre följande seams) ≥ 96 px vid 390x844 och 320x568.
- **Källor**: loop 1 `diag2 fold390` (137 px = 16,3 %); loop 2 `shots/loop-2/slices-390/v3c-390--s00.png`, `preview/preview-390-front.png` (rubriken börjar vid y ≈ 165, underraden slutar vid y ≈ 707, död grund 137 px under, ~120 px över)

## Problem

Stagen centrerar sitt innehåll (`.hero-stage{justify-content:center}`, rad 305-306) på
alla bredder. Vid 390x844 är innehållet (rubrik 2 rader + kort 4:5 + underrad) ~560 px
högt och luften delas lika: ~120 px över rubriken (under toppraden) och 137 px under
underraden, 16,3 % av viewporten. H-13 sätter 12 % (101 px). Fas A:s läsning står:
folden ser ut att sluta för tidigt, som om något saknades under underraden.

```css
/* index.html:305-306 - current */
  .hero-stage{display:flex;flex-direction:column;justify-content:center;
    padding:clamp(44px,5.6vh,64px) 0 clamp(6px,2.2vh,26px);}
/* index.html:510-522 - current, mediablocket <= 640 */
  @media (max-width:640px){
    .hero-plate{aspect-ratio:4 / 5;
      width:min(calc(100% - 2 * var(--rail-x)),calc(48svh * 4 / 5));}
    .hero-sub{text-align:left;margin-left:var(--rail-x);margin-right:var(--rail-x);
      padding-right:0;}
  }
```

Kortets höjdbudget (48svh) är vald för 320x568 (NOTES § R2) och ska inte växa: vid
390x844 är kortet redan breddbegränsat (342 px brett = 428 px högt), så en högre budget
ändrar ingenting där och spränger 568-skärmen.

## Target

Luften flyttas, inte innehållet: under 640 sätts stagen bottenställd med en bottenpadding
på 10 svh, så den döda grunden under underraden är 84 px (10 %) vid 844 och luften ovanför
rubriken växer med 53 px (toppraden bär den).

```css
/* target, i mediablocket rad 510-522 */
    /* PLAN 032, H-13: centreringen la 137 px (16 %) död grund under underraden vid
       390x844 (diag2). Bottenställt med 10 svh botten flyttar luften upp under
       toppraden, där den bär, utan att röra kortets höjdbudget (48svh, satt för 320x568). */
    .hero-stage{justify-content:flex-end;padding-bottom:10svh;}
```

Vid 320x568: innehåll ~520 px + padding-top 44 + 57 (10 svh) = 621 > 568: `flex-end`
lämnar då rubriken 53 px under toppraden, som i dag med centrering; plan 001:s foldkontroll
(folden hel vid 720x450, inte 320x568) berörs inte, men steg 3 mäter 320x568 ändå.

## Repo conventions to follow

- Foldens höjdbudget mäts, aldrig antas (plan 001, NOTES § R4 `fold_debug`).
- `svh`, aldrig `vh`, i höjdbudgetar (performance.md § 3).
- Ledgerrad i `BRIEF.md` § Byggarens rader, R8: "Folden vid 390 bottenställd".

## Steps

1. Lägg raden i mediablocket.
2. Mät vid 390x844, 375x812, 414x896: `844 − .hero-sub.bottom` ≤ 12 % av höjden; `.hero-
   headline.top ≥ .topline.bottom + 8`.
3. Mät vid 320x568: `.hero-headline.top ≥ .topline.bottom + 8`, `.hero-sub.bottom ≤ 568`
   (ingenting klipps).

## Boundaries

- Rör inte `.hero-plate`s bredd/aspect (kortets budget), `.hero-sub`, `--h1-hrate`.
- Matchar inte rad 305-306 eller 510-522: STOPPA.

## Verification

- **Mekaniskt:** steg 2 och 3 med talen; `reflow.py` 320 rent; plan 001:s tre viewports
  (1280x600, 1024x640, 720x450) oförändrade (blocket gäller ≤ 640 px bredd).
- **Skärmbild:** fold vid 320/375/390/414: underraden ≤ 12 % från botten, ordmärket
  fritt.
- **Feel check:** ingen (statisk).
- **Done when:** H-13 bockad med talet vid 390.
