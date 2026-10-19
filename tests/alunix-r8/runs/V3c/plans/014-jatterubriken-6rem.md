# 014 · Jätterubriken upp ett steg: tak 6rem

- **Status**: TODO (R7, loop 1; radhänvisningar uppdaterade av arkitekten 2026-09-17 mot R6-läget)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46` (boardkopian `27b7db6d` är R4-läget och gäller inte längre)
- **Severity**: LOW
- **Category**: Cohesion & tokens (skala), T-5, H-07
- **Estimated scope**: 1 fil, 1 rad

## Problem

`VI BYGGER ERT VARUMÄRKE.` sätts på ~80 px vid 1440 (`clamp(2.1rem,5.8vw,4.8rem)`, taket
4,8rem = 76,8 px binder). Det är 4,8 gånger brödtexten (16 px), under TASTE § 2.4:s golv
5 gånger och långt under Hoys kapitelavdelare (100 till 132 px,
`shots/fasA/hoy-1440/hoy-webb-1440--s04.png`). Skärmen s5 höger har därmed inget
displayelement som väger mot Calyx-ramen till vänster (`v3c-1440--s05.png`).

```css
/* index.html:664-667 - current */
  .giant{font-family:var(--f-display);font-weight:700;
    font-size:clamp(2.1rem,5.8vw,4.8rem);line-height:.96;letter-spacing:-.03em;
    text-transform:uppercase;text-wrap:balance;overflow-wrap:anywhere;min-width:0;
    transform-origin:left center;}
```

## Target

96 px glyfhöjd vid 1440 (6 gånger body), oförändrat golv vid 320.

```css
/* target, index.html:665 */
    font-size:clamp(2.1rem,6.7vw,6rem);line-height:.96;letter-spacing:-.03em;
```

6,7vw vid 1440 = 96,5 px; taket 6rem = 96 px binder. Vid 900 px bredd: 60 px. Vid 390:
golvet 2,1rem = 33,6 px, oförändrat.

## Repo conventions to follow

- Display sätts med `clamp()` och `text-wrap:balance` (rad 300, 665).
- `.js .giant{transform:scale(calc(0.92 + 0.08 * var(--sc-ps,0)))}` (rad 671) läser
  `--sc-ps` och rörs inte; ett större element gör skalsteget synligare (H-25).

## Steps

1. Byt rad 665.
2. Mät radantal och bredd vid 1440 (högerspalten ≈ 640 px): `getBoundingClientRect()` på
   `.giant` och `getClientRects().length`; mål högst 3 rader, ingen glyf utanför
   `#giant-section`s padding-box (`overflow-wrap:anywhere` står kvar som skydd).
3. Mät glyfhöjden: versal-H i Geist 700 vid 96 px ≈ 69 px cap-height; skriv talet i NOTES.

## Boundaries

- Rör inte `.giant-sub` (låst copy) eller liggaren.
- Matchar inte rad 665: STOPPA.
- Loop 1 (2026-09-17): `diag.json` mäter `.giant` font-size 76,8 px, 1 rad-rektangel (två rader i `v3c-1440--s03.png`); högerspalten är 657 px bred efter R6, inte 640.

## Verification

- **Mekaniskt:** `reflow.py` 320 och 200 % zoom utan överflödning; `detect.mjs` (regeln
  `oversized-h1` gäller h1, inte h2; skulle den ändå fira redovisas den med TASTE § 2.4 som
  källa).
- **Skärmbild:** s5 vid 1440 läst som bild: rubriken är skärmens största glyfhöjd i
  högerspalten och väger mot Calyx-ramen vid squint; 390-skivan oförändrad.
- **Done when:** H-07 bockad (≥ 96 px vid 1440, högst 3 rader).
