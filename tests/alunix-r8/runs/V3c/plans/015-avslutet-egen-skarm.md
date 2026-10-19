# 015 · Avslutet som egen skärm, med en hårlinje som dras in på `--sc-ps`

- **Status**: TODO (R7, loop 1; radhänvisningar uppdaterade av arkitekten 2026-09-17 mot R6-läget)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46` (boardkopian `27b7db6d` är R4-läget och gäller inte längre)
- **Severity**: MEDIUM
- **Category**: Missed opportunity (sista skärmen saknar rörelse), T-8, H-12, H-25
- **Estimated scope**: 1 fil, ~12 rader CSS, 1 rad markup

## Problem

Avslutet delar viewport med prisblocket och Hōrai (`shots/fasA/v3c-1440/v3c-1440--s06.png`,
plan 007) och är den enda skärmen utan någon scroll-läst förändring (ramsekvensen
`v3c-giant/v3c-1440-life-09..11.png`, `v3c-390--s08.png`). Målbilden: "en rad, en adress,
ingenting mer", ensam på skärmen, och sidan ska sluta stilla, inte tona ut.

```css
/* index.html:919-928 - current (min-height:62svh och display:flex finns redan sedan R4, plan 007) */
  .close{position:relative;z-index:1;min-height:62svh;
    display:flex;align-items:center;
    padding:clamp(64px,12vh,140px) var(--rail-x) clamp(56px,10vh,120px);}
  .close-mailto{display:inline-block;font-family:var(--font);font-weight:300;
    font-size:clamp(1.6rem,6vw,4.2rem);line-height:1;letter-spacing:-.02em;
    color:#f7f5f0;text-decoration:none;
    border-bottom:1px solid rgba(247,245,240,.42);padding-bottom:.12em;
    transition:border-color .16s var(--ease),color .16s var(--ease);}
```

Träffytan: vid 390 är länken 30 px hög (`diag2 mailto390`), under 44 px-golvet (H-35, gate 62;
Astra loop 1, fix 6). Target lägger `min-height:44px` på samma sätt som `.card-cta` (rad 465-470).

```html
<!-- index.html:1354-1356 - current -->
<footer class="close" data-sc-act="flow">
  <a class="close-mailto" href="mailto:kontakt@alunix.se">kontakt@alunix.se</a>
</footer>
```

## Target

`.close` fyller **100 svh** (Astra loop 1, fix 6: 62 svh lämnar 38 svh av principerna i
sista viewporten, `shots/loop-1/slices-1440/v3c-1440--s10.png`; H-12 säger "ensamt"), mailto-
raden står vertikalt centrerad och ensam, och en hårlinje ovanför raden ritas från vänster i
takt med scrollen. Footern är sidans sista akt och kan aldrig nå `--sc-ps` = 1 (dokumentet
slutar när dess underkant möter viewportens): med höjd = vh är maximalt ps = vh / (vh + vh)
= 0,50 vid båda bredderna. Linjen mappas därför på 0 till 0,46 så att den är fullt dragen
när sidan står i botten.

```css
/* target, index.html:919-921 */
  .close{position:relative;z-index:1;min-height:100svh;
    display:flex;flex-direction:column;justify-content:center;align-items:flex-start;
    gap:clamp(20px,3vh,32px);
    padding:clamp(64px,12vh,140px) var(--rail-x) clamp(56px,10vh,120px);}
  /* Hårlinjen ritas ur --sc-ps (F-014): footern är sista akten och når max ~0,38,
     så fönstret är 0 till 0,36. Ingen transition, ingen JS. */
  .close-rule{width:100%;height:1px;background:var(--hairline-dark);transform-origin:left center;
    transform:scaleX(clamp(0,calc(var(--sc-ps,0) / 0.46),1));}
/* target, index.html:922-923. display:inline-flex;align-items:center;min-height:44px på
   .close-mailto (rad 922), som .card-cta. Golvet höjs 1.6rem -> 2rem: vid 390 mätte loop 1 raden till
   25,6 px (`diag.json` mailto h 30), sidans minsta displaymoment; 2rem = 32 px,
   "kontakt@alunix.se" i Public Sans 300 ~ 272 px bred, inom 343 px. */
    font-size:clamp(2rem,6vw,6rem);line-height:1;letter-spacing:-.02em;
```

```html
<!-- target, index.html:1354-1357 -->
<footer class="close" data-sc-act="flow">
  <div class="close-rule" aria-hidden="true"></div>
  <a class="close-mailto" href="mailto:kontakt@alunix.se">kontakt@alunix.se</a>
</footer>
```

Vid 1440: 6vw = 86 px, taket 96 px binder inte; `kontakt@alunix.se` i Public Sans 300 på
86 px ≈ 780 px bred, inom 1 268 px. Vid 390: golvet 32 px (var 25,6).

## Repo conventions to follow

- Allt som förflyttar sig läser `--sc-ps` (`index.html:38-47`, F-014); `sc-smooth.js`
  publicerar `--sc-ps` på varje `data-sc-act`, footern inräknad (rad 1354 bär attributet).
- `min-height` i `svh`, aldrig `vh` (BRIEF § Prestandaplan).
- Tokens: `--hairline-dark` (rad 133) är hårlinjen på mörk grund.
- Ledgerrad finns: `BRIEF.md` § Arkitektens rader, "Avslutet".

## Steps

1. Byt `.close`-regeln (rad 919-921) och lägg `.close-rule` efter den (rad 919-921 har redan `min-height:62svh` och `display:flex;align-items:center` från plan 007: behåll min-height, byt till kolumn-flex enligt Target).
2. Byt rad 923: golv `2rem`, tak `6rem`.
3. Lägg `<div class="close-rule" aria-hidden="true"></div>` som första barn i `<footer>`
   (rad 1355).
4. Mät max `--sc-ps` på footern vid sidans botten (`getComputedStyle(footer).getPropertyValue('--sc-ps')`) vid 1440x900 och 390x844; ligger värdet under 0,46 justeras nämnaren till det uppmätta värdet minus 0,02, och talet skrivs i NOTES.md.
5. Mät att avslutet är ensamt: `document.querySelector('.close').getBoundingClientRect().top` vid maxscroll ≥ 0 och `#principer`s underkant ≤ 0 vid 1440 och 390.
6. Mät `.close-mailto` `getBoundingClientRect().height` ≥ 44 vid 390 och 320.

## Boundaries

- Ingen ny CTA, inget formulär, ingen kolofon (målbilden).
- `border-bottom` på mailto-raden (rad 926) står kvar: den är länkens understrykning, inte
  sektionens linje.
- Matchar inte raderna 919-928 eller 1354-1356: STOPPA.
- Loop 1 (2026-09-17): `diag.json` 1440: `.close` h 558 (62 % av 900), mailto h 76 (67 px glyfstorlek, taket 4,2rem binder); `slices-1440/v3c-1440--s10.png` visar avslutet utan rörelse och med liggarens två sista rader i samma viewport; 390: mailto 30 px hög.

## Verification

- **Mekaniskt:** `motion_probe.py --track "footer.close:--sc-ps,.close-rule:transform" --cpu 4 --wheel 100:60 --ticks 70`: staircase 0, inte DEAD; `scroll_verify.py`: inget nytt `deadScroll`-band i avslutet; `perf_probe.py` CLS ≤ 0,05 (min-height läggs på ett block utan `contain-intrinsic-size`, så ingen dubbel höjdgissning); `a11y_scan.py` 0 violations.
- **Skärmbild:** sista skärmen vid 1440 och 390 som bild: bara hårlinjen och adressen, prisblocket utanför; tolvstegs ramsekvens genom footerns liv visar linjen växa från vänster utan hopp och stå fullt dragen i sista rutan.
- **Feel check:** sidan slutar stilla: när linjen är dragen händer inget mer, ingen fade.
- **Done when:** H-12 (100 svh, ensamt, mailto ≥ 64 px vid 1440) och H-25 (avslutet) bockade; träffytan ≥ 44 px.
