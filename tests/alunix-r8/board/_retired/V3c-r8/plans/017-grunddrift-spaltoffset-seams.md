# 017 · Grunddriften synlig, spaltoffset ≥ 96 px, seams utan slitsar

- **Status**: TODO (R7, loop 1; radhänvisningar uppdaterade av arkitekten 2026-09-17 mot R6-läget)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46` (boardkopian `27b7db6d` är R4-läget och gäller inte längre)
- **Severity**: HIGH
- **Category**: Cohesion (grund och seams), Physicality (stagger), T-6, H-04, H-05, H-19
- **Estimated scope**: 1 fil, ~10 rader CSS; en mätning före och efter

Tre fynd med samma plats (bandet under heron). Tre steg, var och en mätbar för sig.

## Problem

**A. Grunddriften syns inte.** Motorn driftar `--sc-canvas` `#0b0c0e` → `#123f68` →
`#f4f2ee` (rad 1029, 1084), och `.ground` blandar tonen över fotot med
`background-blend-mode:color` (rad 201-208). Men rad 245 lägger `filter:grayscale(1)` på
hela elementet **efter** blandningen, så den blå tonen tas bort innan den når skärmen.
Skivorna `shots/fasA/v3c-1440/v3c-1440--s04.png` och `s05.png` visar samma svärta bakom
tesen som bakom heron. Driften är död av konstruktion, inte av värde.

```css
/* index.html:235-245 - current */
  .ground{position:fixed;inset:0;z-index:0;pointer-events:none;contain:strict;
    background-image:linear-gradient(
        color-mix(in srgb,var(--sc-canvas) 62%,transparent),
        color-mix(in srgb,var(--sc-canvas) 62%,transparent)),
      var(--ground-img);
    background-size:cover,cover;
    background-position:center center,center 40%;
    background-repeat:no-repeat,no-repeat;
    background-blend-mode:color,normal;
    filter:grayscale(1) contrast(1.08) brightness(.5);}
```

**B. Spalterna toppalignar.** Blå tes (vänster) och papper (höger) börjar på samma y
(`v3c-preview/v3c-1440-ledger--fold.png`: båda y 104; `v3c-giant/v3c-1440-life-02.png`:
båda y 610). House physics: paired columns never top-align.

**C. Slitsar av rå grund.** Panelerna ligger med `clamp(10px,2.4vh,40px)` mellan sig (rad
509) och bandet börjar 0 px under pinnen (rad 507: `padding:0 …`), så seams är 20 till 30 px
smala slitsar av foto (`v3c-1440--s04.png` y 690 till 720; `life-02.png`). H-05: en seam är
≥ 160 px luft, ett helbrett materialbyte eller ett överlapp; aldrig en slits under 96 px.

```css
/* index.html:505-509 - current */
  .stagger{position:relative;display:flex;align-items:stretch;
    gap:clamp(20px,3.2vw,56px);
    padding:0 clamp(16px,3vw,40px) 0;}
  .col{min-width:0;flex:1 1 50%;display:flex;flex-direction:column;}
  .col > * + *{margin-top:clamp(10px,2.4vh,40px);}
```

## Target

**A.** Fotot förblir gråskala men tonen når skärmen: gråskalan läggs på **fotolagret**, tonen
på ett lager ovanpå, inne i samma `contain:strict`-element. Två pseudo-element, ingen
`mix-blend-mode` mot sidans backdrop (R2 mätte att den kostade), bara mot `.ground`s egen
stapel.

```css
/* target, index.html:235-245 */
  .ground{position:fixed;inset:0;z-index:0;pointer-events:none;contain:strict;
    background:var(--c-black);}
  /* Fotot, gråskalat en gång på sitt eget lager. */
  .ground::before{content:"";position:absolute;inset:0;
    background:var(--ground-img) center 40% / cover no-repeat;
    filter:grayscale(1) contrast(1.08) brightness(.5);}
  /* Tonen, ovanpå det gråskalade fotot. `color`-blandning inne i .ground:s egen
     stackningskontext (contain:strict skapar den), aldrig mot sidans backdrop. */
  .ground::after{content:"";position:absolute;inset:0;
    background:color-mix(in srgb,var(--sc-canvas) 62%,transparent);
    mix-blend-mode:color;}
```

Mätbart: en grundpixel utanför panelerna (t.ex. x 1 400, y 850 vid 1440 när tesen står i
mitten av skärmen) skiljer ≥ 12 RGB-steg mot samma position i folden (H-19). Om
`motion_probe` visar att `::after` med `mix-blend-mode` kostar (p95 eller rutor > 33 ms
sämre än före), byt `mix-blend-mode:color` mot `opacity:.62` och `background:var(--sc-canvas)`
med `mix-blend-mode:multiply`; kostar även det: STOPPA och rapportera talen, driften får då
en egen fråga till Anton i stället för en gissning.

**B och C.** Högerspalten börjar 120 px lägre än vänster vid ≥ 900; seams inne i spalterna är
≥ 160 px; bandet börjar 160 px under pinnen (H-05 (a): kontinuerlig grund = minst 160 px
luft; planens tidigare 96/120 låg under sitt eget golv, Astra loop 1).

```css
/* target, index.html:505-509 */
  .stagger{position:relative;display:flex;align-items:stretch;
    gap:clamp(20px,3.2vw,56px);
    /* H-05: seamen mot pinnen är ett författat mellanrum, inte en slits. Den tidigare
       padding-top:0 (BRIEF, "flow direkt efter pin") gällde en halvtom skärm; 96 px är
       luft, inte en skärm. */
    padding:clamp(160px,18vh,200px) clamp(16px,3vw,40px) 0;}
  .col{min-width:0;flex:1 1 50%;display:flex;flex-direction:column;}
  /* H-04: paired columns never top-align. */
  .col-right{padding-top:clamp(96px,12vh,140px);}
  /* H-05 (a): kontinuerlig grund kräver >= 160 px luft (Astra loop 1: 16vh = 144 px vid 900). */
  .col > * + *{margin-top:clamp(160px,18vh,200px);}
```

Under 900 (rad 510-515, plan 012 äger blocket) gäller `gap` på `.stagger` och `.col-right`s
padding nollas: lägg `.col-right{padding-top:0;}` i det blocket. Mobilseams: `gap` höjs till
`clamp(64px,10vh,96px)` i samma block (H-05 vid 390: ≥ 96 px eller materialbyte; panelerna
byter material, så 64 px räcker som golv).

## Repo conventions to follow

- `.ground` har inga barn och `contain:strict` (rad 208-234, mätt i R2); pseudo-element
  bryter inte containment.
- `--ground-img` sätts som token i JS (rad 1371-1372) och läses oförändrat.
- BRIEF § decision ledger "Flow direkt efter pinnen" (padding-top 0) ersätts av en ny rad:
  96 px luft är H-05:s golv och inte en halvtom skärm; skriv raden.
- Ledgerrad för driften finns: `BRIEF.md` § Arkitektens rader, "Grunddriften"; för
  offset/seams: skriv en rad med H-04/H-05 som källa.

## Steps

1. **Mät före:** `motion_probe.py --track "section.hero:--sc-ps,.panel-thesis:--sc-ps" --cpu 4 --wheel 100:60 --ticks 70` med kontrollen ren; spara p95 och rutor > 33 ms. Sampla grundpixeln (x 1 400, y 850) vid scrollY 0 och vid scrollY där `.panel-thesis` står centrerad; skriv RGB i NOTES.md.
2. Byt `.ground`-blocket (rad 235-245) mot Target A.
3. **Mät efter:** samma prob; samma pixelsampling. Villkor: p95 och rutor > 33 ms inte sämre, pixelskillnad ≥ 12. Annars fallback enligt Target A, sedan STOPPA om även den kostar.
4. Byt rad 505-509 mot Target B/C; lägg `.col-right{padding-top:0;}` och det höjda `gap`-värdet i blocket på rad 510-515 (koordinera med plan 012: samma block).
4b. **D, bleeden mot rubriken.** Rad 505: `gap:clamp(20px,3.2vw,56px)` → `gap:clamp(20px,4vw,58px)`; rad 560: `translateX(calc(10% + 24% * var(--sc-ps,0)))` → `translateX(calc(10% + 23% * var(--sc-ps,0)))`. Mät vid 1440 med `--sc-ps` satt till 1 på `.panel-thesis` (som `diag2.py`): `.thesis-photo-box` right ≤ `.giant` left − 4 px, och överhänget (box.right − panel.right) ≥ 96 px. Räknat: spalterna blir 651 px, plåten ~300 px, 33 % = 99 px, box.right ≈ 796 mot rubrikens 803. Håller inte båda villkoren: STOPPA och skriv talen (H-20:s 96 och kollisionen kan då inte båda lösas i den här geometrin).
5. Mät spaltoffset vid 1440: `.panel-thesis` och `.panel-giant` `getBoundingClientRect().top` skiljer ≥ 96 px. Mät varje seam: avståndet mellan panelernas kanter i samma spalt ≥ 160 px; mellan pinnens spacer-slut och första panelen ≥ 160 px.
6. Kör `scroll_verify.py` vid 1440 och 390: `blankBands` får inte få ett nytt band av luften (luften är < 60 % av en viewport per seam, så bandet ska inte fira; firar det ändå redovisas det mot `gates.md` § Both directions som en för girig tröskel, inte som ett fel i sidan).

## Boundaries

- Motorn och `data-sc-drift`-värdena (rad 1029, 1084) rörs inte.
- `.ground`s `contain:strict` står kvar; ingen `will-change` (R2 mätte att den fördubblade tappade rutor).
- Panelernas inre padding (`--panel-pad-y`) rörs inte.
- Matchar inte raderna 235-245, 505-515 eller 558-560: STOPPA.
- Loop 1 (2026-09-17): `shots/loop-1/diag/diag.json` bekräftar utgångsläget: `.panel-thesis` och `.panel-giant` båda top 3060 (offset 0), `.stagger` top 3060 = heroens slut (slits 0 px); skivan `slices-1440/v3c-1440--s03.png` visar båda spalterna toppalignade vid y 360. Hyperborea-bleeden (H-20): loop 1 mätte den vid `--sc-ps` = 1 (`shots/loop-1/diag2`, 1440x900): överhäng 103 px förbi tesplåtens ram (H-20:s 96 uppfyllt), men plåtens högerkant hamnar på x 799,9 mot jätterubrikens textkant x 791, alltså 9 px in i `VI BYGGER`; efter B (högerspalten 120 px lägre) ligger rubriken (y 3235 till 3376) helt i plåtens höjdspann (y 3197 till 3386), så intrånget blir synligt. Steg D nedan tar det: spaltrännan vidgas 46 → 58 px och bleedens tak sänks 34 → 33 %, så att plåten stannar 5 px före textkanten med 100 px överhäng.

## Verification

- **Mekaniskt:** proben före/efter enligt steg 1 och 3 sida vid sida i NOTES.md; pixelsampling ≥ 12 steg (H-19); rect-mätningar (H-04 ≥ 96 px, H-05 inga slitsar < 96 px); `scroll_verify` utan nya band; `perf_probe.py` CLS oförändrad; `contrast_over_media.py --url` på hero-rubriken och underraden mot den nya grunden ≥ 4,5:1 (grunden är fortfarande `brightness(.5)`).
- **Skärmbild:** skivor vid 1440: bakom tesen är grunden mätbart blåare än i folden och bakom papperet mätbart ljusare; bandets övre kant har luft, inte en slits; högerspalten börjar synligt lägre än vänster. 390-skivor: seams ≥ 64 px.
- **Feel check:** scrolla från folden till priset: grunden ändrar ton i tre steg utan att hoppa (driften är motorns interpolation), panelerna ligger som plattor på ett bord med luft emellan, inte som kakel.
- **Done when:** H-04, H-05 och H-19 bockade; probens tal inte sämre än före.
