# 023 · Liggartråden ankrad i liggarens läge

- **Status**: TODO (R6)
- **Commit**: R5-läget av `runs/V3c/index.html`, md5 `fcbee8f1`
- **Severity**: MEDIUM (H-25: rörelsen ska synas där den hör hemma)
- **Category**: Purpose (rörelse som händer utanför skärmen är ingen rörelse)
- **Estimated scope**: 1 fil, 1 rad CSS
- **Källor**: design-perf-reviewer fix 5 (tråden går scaleY 0 → 1 mellan scrollY 2 400 och
  3 200 medan `#projekt`s överkant står 1 374 → 574 px under viewportens överkant)

## Problem

```css
/* index.html:617 - current */
    --scrub:clamp(0,calc((var(--sc-ps,0) - 0.15) / 0.45),1);}
```

`--scrub` driver ordscrubben och trådens `scaleY` i `#giant-section`. Fönstret 0,15 till
0,60 av aktens liv är mätt att löpa medan liggaren fortfarande ligger 574 till 1 374 px
under viewportens överkant: tråden är färdigritad innan liggaren är läsbar. Ordscrubben
har samma fönster och tänds alltså också för tidigt (den var byggd att "läsas färdig långt
innan sektionen lämnar skärmen", rad 614-616; den läses nu färdig innan den kommer in).

## Target

Fönstret ankras så att `scaleY 0 → 1` löper medan liggarens överkant går från +600 till
+90 px under viewportens överkant (perf-rapportens mätning: 0,62 ↔ scrollY 3 160, 0,95 ↔
3 680 vid 1440x900 i R5-läget).

```css
/* target, index.html:617 */
    --scrub:clamp(0,calc((var(--sc-ps,0) - 0.62) / 0.33),1);}
```

Efter plan 019 (processakten byter höjd) och 018 ändras inte `#giant-section`s eget liv,
så talen står; byggaren mäter ändå om (steg 2) eftersom `.stagger`s höjd påverkas av
018:s `content-visibility` bara på ramarna, inte på papperspanelen.

## Steps

1. Byt rad 617.
2. Mät vid 1440x900: scrollY där `#ledgerScrub` överkant = 600 px från viewportens topp
   och där den = 90 px; läs `--scrub` på `#giant-section` vid båda: ≈ 0 respektive ≈ 1.
   Avviker talen mer än 0,05: justera start och bredd så att villkoret håller och skriv
   de uppmätta i NOTES.md.
3. `?preview=ledger` (rad 1455-1458) sätter `--scrub:1` direkt och berörs inte.

## Boundaries

- `.is-scrubbed .thread-fill`, ordscrubbens färgformel (rad 655-665) och `.giant`s skala
  (rad 623) rörs inte.
- Matchar inte rad 617: STOPPA.

## Verification

- **Mekaniskt:** `motion_probe --track "#threadFill:transform"` är blind för ren `scale()`
  (perf-rapportens fidelity-not); mät i stället `getComputedStyle(threadFill).transform`
  vid de två scrollpositionerna (matris `d` ≈ 0 respektive ≈ 1). `scroll_verify` utan nya
  band.
- **Skärmbilder:** tolvstegs ramsekvens genom `#giant-section`s liv (som
  `shots/fasA/v3c-giant/`): tråden börjar när liggaren kommer in under jätterubriken och
  är hel när liggaren står i mitten; orden tänds i samma takt.
- **Feel check:** tråden ritas medan man läser raderna, inte innan.
- **Done when:** H-25 bockad för liggaren; talen i NOTES.md.
