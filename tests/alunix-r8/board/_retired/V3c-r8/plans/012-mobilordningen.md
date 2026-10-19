# 012 · Mobilordningen vid ≤ 900 px: berättelsens ordning s4 → s7

- **Status**: TODO (R7, loop 1; radhänvisningar uppdaterade av arkitekten 2026-09-17 mot R6-läget)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46` (boardkopian `27b7db6d` är R4-läget och gäller inte längre)
- **Severity**: MEDIUM
- **Category**: Cohesion (berättelsens ordning), Q28, H-14
- **Estimated scope**: 1 fil, ~10 rader CSS

## Problem

Under 900 px staplar spalterna som hela spalter: högerspalten först (jätterubrik + liggare,
Hōrai), sedan vänsterspalten (tes, Calyx, pris). Berättelsens s4 (tesen, "Det första
intrycket är digitalt") kommer därför efter s6 (Hōrai), läst i
`shots/fasA/v3c-390/v3c-390--s02.png` till `s06.png`. `BRIEF.md` § STORY låser ordningen
4 → 5 → 6 → 7.

```css
/* index.html:510-515 - current */
  @media (max-width:900px){
    .stagger{flex-direction:column;gap:clamp(10px,2.4vh,40px);padding:0 0 0;}
    .col{flex:1 1 auto;}
    .col-left{order:2;}
    .col-right{order:1;}
  }
```

## Target

Vid ≤ 900 px: tes → Calyx → jätterubrik och liggare → Hōrai → pris → (process, plan 010)
→ avslut. Spalterna upplöses med `display:contents` så att de sex panelerna blir direkta
flexbarn till `.stagger` och kan sorteras med `order`; DOM-ordningen och `.on-paper`-
ärvningen (fokusring på papper, `index.html:206`) rörs inte.

```css
/* target, index.html:510-515 */
  @media (max-width:900px){
    .stagger{flex-direction:column;gap:clamp(10px,2.4vh,40px);padding:0 0 0;}
    .col{display:contents;}
    /* Astra loop 1, fix 1: `.col > * + *` MATCHAR fortfarande (selektorn läser DOM, inte
       layout), och efter 017 bär den clamp(120px,…); nollas här, gap bär avståndet. */
    .col > * + *{margin-top:0;}
    .panel-thesis{order:1;}
    .calyx-fig{order:2;}
    .panel-giant{order:3;}
    .horai-fig{order:4;}
    .price{order:5;}
  }
```

`.col > * + *{margin-top:…}` (rad 509) träffar FORTFARANDE under 900: `display:contents` tar
bort `.col`:s box, inte dess plats i DOM, så selektorn matchar och marginalen läggs på
panelerna som flexbarn till `.stagger` (Astra loop 1, fix 1; R6-planens motsatta påstående
var fel). Därför nollas den i blocket och `gap` på `.stagger` bär avståndet ensamt.

## Repo conventions to follow

- Brytpunkten 900 finns redan för samma block (rad 510, 715, 930).
- `display:contents` på ett element som bär klassen `.on-paper` behåller selektorn
  `.on-paper :focus-visible` (rad 206): den matchar DOM, inte layout.
- Ledgerrad finns: `BRIEF.md` § Arkitektens rader, "Mobilordningen".

## Steps

1. Byt raderna 512-514 mot blocket i Target. Plan 017 lägger samtidigt `.col-right{padding-top:0;}` och ett höjt `gap` i samma block: skriv blocket EN gång med båda planernas rader (017 körs först).
2. Kontrollera att `.calyx-fig,.horai-fig{flex:none;}` (rad 931) fortfarande gäller
   (de är nu flexbarn till `.stagger`, samma effekt).
3. Mät ordningen: `[...document.querySelectorAll('.stagger > .col > *')].map(e=>[e.className, e.getBoundingClientRect().top])` vid 390: stigande y i ordningen tes, calyx, giant, horai, price.

## Boundaries

- Ingen markup flyttas; DOM-ordningen är 1440-layoutens och rörs inte.
- 1440-layouten (rad 505-509, efter 017) rörs inte.
- Matchar inte raderna 510-515: STOPPA.
- Loop 1 (2026-09-17): `slices-390/v3c-390--s03..s06.png` bekräftar att ordningen fortfarande är jätterubrik/liggare → Hōrai → tes → Calyx → pris; `diag.json` 390: giant top 2870, horai 3567, thesis 4150, calyx 4658, price 5274.

## Verification

- **Mekaniskt:** `reflow.py` vid 320 och 200 % zoom: ingen överflödning; `a11y_scan.py`
  0 violations; `tab_walk.py`: tabbordningen oförändrad (DOM-ordning), vilket redovisas
  som avsiktlig avvikelse mellan visuell och fokusordning i NOTES.md om `a11y-audit` flaggar
  den (WCAG 2.4.3 gäller meningsfull ordning; båda ordningarna är meningsfulla, men
  skillnaden ska stå skriven).
- **Skärmbilder:** skivor vid 390 och 768 lästa som bilder: tesen kommer direkt efter
  heron, Calyx efter tesen, priset sist före processakten.
- **Done when:** H-14 bockad vid 390 och 768.
