# 013 · Prisblockets material: `--c-graphite`

- **Status**: TODO (R7, loop 1; radhänvisningar uppdaterade av arkitekten 2026-09-17 mot R6-läget)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46` (boardkopian `27b7db6d` är R4-läget och gäller inte längre)
- **Severity**: MEDIUM
- **Category**: Cohesion & tokens (material, inte grå sektion), T-3, H-11, Q27
- **Estimated scope**: 1 fil, 2 rader

## Problem

Prisblocket ligger på `--invert #0c0b08` mot grunden `#0b0c0e`. Skillnaden är en L-enhet;
blocket läser som ett hål i grunden med en kant, inte som ett plan
(`shots/fasA/v3c-1440/v3c-1440--s06.png`; `scroll_verify` 390 rapporterar blocket som
enfärgat band 5 712 till 6 331). TASTE § 4.5: sektioner byter material, inte bara bakgrund.
Hoy visar att ett platt plan per akt bär kapitlet utan kort.

```css
/* index.html:130 - current */
    --bg:#fdfbf4; --ink:#16140f; --invert:#0c0b08; --invert-ink:#fdfbf4;
/* index.html:627 - current */
  .price{background:var(--invert);color:var(--invert-ink);
```

## Target

Ett kallt grafitplan som skiljer sig i valör (L ≈ 27 mot grundens L ≈ 8), inte i kulör
(chroma 0,012, ingen andra accent). `--invert` står kvar för `.horai-wrap` (rad 719).

```css
/* target, index.html:130 (ny token på raden efter) */
    --bg:#fdfbf4; --ink:#16140f; --invert:#0c0b08; --invert-ink:#fdfbf4;
    --c-graphite:oklch(0.27 0.012 250); /* prisblockets plan: valör, inte kulör (T-3) */
/* target, index.html:627 */
  .price{background:var(--c-graphite);color:var(--invert-ink);
```

Hårlinjerna i liggaren (`--hairline-dark`, rad 639-643) står kvar; mätt mot det nya planet
ska de fortfarande synas (rgba(255,255,255,.18) på L 27 ger ~1,6:1, en hårlinje behöver
inte AA).

## Repo conventions to follow

- Tokens i `:root` (rad 122-186), oklch där stacken tillåter (house-physics § Palette).
- Ingen inline-hex (gate 48). Ledgerrad finns: `BRIEF.md` § Arkitektens rader,
  "Prisblockets material".

## Steps

1. Lägg `--c-graphite` efter rad 130.
2. Byt `var(--invert)` → `var(--c-graphite)` på rad 627.
3. Mät kontrasten: `--invert-ink` (#fdfbf4) mot planet med `contrast.py` (mål ≥ 12:1;
   räknat ≈ 12,6:1). `.price-ingress` rgba(253,251,244,.84) mot planet ≥ 7:1.

## Boundaries

- `.horai-wrap` (rad 719) behåller `--invert`.
- Rör inte prisliggarens rader eller priserna (låst copy).
- Matchar inte rad 130 eller 627: STOPPA.
- Loop 1 (2026-09-17): `diag.json` mäter `.price` background `rgb(12, 11, 8)` mot grunden `#0b0c0e`; `slices-1440/v3c-1440--s05.png` visar blocket som ett hål med en kant.

## Verification

- **Mekaniskt:** `contrast.py` på `.price .statement`, `.price-ingress`, `.price-row .label`,
  `.price-row .value` mot `.price`s bakgrund: alla ≥ 4,5:1. Pixelmätning: samplad
  bakgrundspixel i `.price` mot grundpixel utanför blocket skiljer ≥ 12 i L (H-11).
- **Skärmbild:** s6 vid 1440 och prisskärmen vid 390 lästa som bilder; vid squint 5 px
  läser blocket som ett plan, inte som ett hål.
- **Done when:** H-11 bockad; `detect.mjs` inga nya fynd.
