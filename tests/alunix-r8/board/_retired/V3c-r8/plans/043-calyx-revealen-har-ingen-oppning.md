# 043 · Calyx-revealen har ingen öppning: `.rv` klipper inte, så ramen står hel vid varje `--rv`

- **Status**: TODO (R10, loop 4)
- **Commit**: R9-läget av `runs/V3c/index.html`, md5 `909916d1`
- **Severity**: HIGH (funktion: den ena av sidans två ramrevealer sker aldrig; PRODUCT.md "reveal sker en gång på wrappern"; H-25, H-27; F-002-principen, målet tyst i vila och tänds vid scroll)
- **Category**: Funktion / states (revealen), H-25, H-27; Astra loop 4 fix 2, verifierad av arkitekten (`shots/loop-4/astra-verify/`)
- **Estimated scope**: 1 fil, 2 rader CSS (en `overflow:clip`, två tecken i två `calc()`), en kommentar
- **Källor**: `index.html` rad 676 till 678 (`.frame-wrap .rv{position:absolute;inset:0;}`, `.calyx-wrap .rv{transform:translateY(calc((1 - var(--rv)) * 100%));}`, `.calyx-wrap .rv iframe{transform:translateY(calc((var(--rv) - 1) * 100%));}`), rad 650 (`.frame-wrap{overflow:clip}`); plan 036 Target ("wrapperns overflow:clip visar den övre delen: samma bild som inset(0 0 (1−rv)·100% 0)", som var fel); loop 4 `shots/loop-4/astra-verify/verify_astra4.json`, `calyx-rv0.png`, `calyx-rv0.5.png`, `calyx-rv1.png`, `horai-rv0.png`, `horai-rv0.5.png`

## Problem

036 A ersatte `clip-path:inset(0 0 (1−rv)·100% 0)` på wrappern med en inre box `.rv` som
flyttas `translateY((1−rv)·100%)` och en ram som flyttas tillbaka lika mycket. Men `.rv`
klipper inte (`overflow` visible), och wrapperns `overflow:clip` sitter på wrapperns egen,
stillastående box. Ramens sammansatta position är därför wrapperns topp vid varje `--rv`,
och wrappern visar hela ramen. Mätt (1440x900, ramen monterad och vaken, `--rv` tvingad):

| `--rv` | `.rv` top (viewport) | ramens top | andel wrapperbakgrund synlig | Hōrai (samma mätning), andel svart |
|---|---|---|---|---|
| 0 | 850 | 40 | 0,1 % | 99,9 % |
| 0,25 | 648 | 40 | 0,1 % | |
| 0,5 | 445 | 40 | 0,1 % | 31,8 % |
| 1 | 40 | 40 | 0,1 % | 13,1 % |

Hōrais iris fungerar (`.rv` har `border-radius:50%;overflow:clip`); Calyx-revealen är en
no-op sedan R9. Loop 3:s A/B-recept (`ab_band5.sh` RECIPE) hade samma fel, så talen
"57,7 / 53,0 ms" för hela receptet mätte en Calyx utan klippning. R9:s pixelkontroll för 036
jämförde `--rv` 1 mot R8 (identiskt, korrekt) och Hōrais iris vid 0,25 / 0,5 / 0,75; Calyx
vid < 1 kontrollerades inte mot R8:s `calyx12-1440-*.png`.

```css
/* index.html:676-678 - current */
  .frame-wrap .rv{position:absolute;inset:0;}
  .calyx-wrap .rv{transform:translateY(calc((1 - var(--rv)) * 100%));}
  .calyx-wrap .rv iframe{transform:translateY(calc((var(--rv) - 1) * 100%));}
```

## Target

`.rv` är öppningen och måste klippa; den kommer **uppifrån** (som `inset` som klippte
underkanten: synligt är wrapperns övre `rv`-andel) med ramen kontratranslaterad så att
innehållet står pixelstilla. Vid `--rv` 0 ligger `.rv` helt ovanför wrappern (wrapperns
`overflow:clip` gömmer den), vid 0,5 täcker den wrapperns övre halva, vid 1 hela wrappern och
båda transformerna är identitet.

```css
/* target, index.html:676-678 */
  /* PLAN 043 (loop 4): .rv är öppningen och klipper; den kommer uppifrån
     (samma bild som R8:s inset(0 0 (1-rv)*100% 0)) med ramen kontra-
     translaterad så innehållet står stilla. Utan overflow:clip på .rv
     (R9) visade wrappern hela ramen vid varje --rv (astra-verify/). */
  .frame-wrap .rv{position:absolute;inset:0;}
  .calyx-wrap .rv{overflow:clip;transform:translateY(calc((var(--rv) - 1) * 100%));}
  .calyx-wrap .rv iframe{transform:translateY(calc((1 - var(--rv)) * 100%));}
```

Procenten är `.rv`:s egen höjd (= wrapperns) respektive ramens (= samma): summan är noll,
ramen står på wrapperns topp i alla lägen. Vid `--rv` 1 identitet: ramen rörs aldrig efter
att den visats (PRODUCT.md). `.horai-wrap .rv` rörs inte (den har redan `overflow:clip`).

## Repo conventions to follow

- Ingen `clip-path`/`mask`/`filter` på `.frame-wrap`, `.rv` eller ramen (036 Boundaries); `overflow:clip` på en inre box är receptet Hōrai redan använder.
- Observern på wrappern (027), `is-asleep` via `f.closest('.frame-wrap')` (036), `--rv` `inherits:true`, latchen (035): orörda.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R10: "Calyx-öppningen klipper och kommer uppifrån; innehållet pixelstilla".

## Steps

1. **Mät före** (scratch `motion_probe_ab.py`, cpu 1, 100:60, tre körningar, median p95): Calyx-fönstret `--start 2862 --ticks 20` med spår `.calyx-wrap:--rv,.calyx-fig:--sc-ps` (revealen går över akten 0,02 till 0,30 ≈ scrollY 2 900 till 3 700), utan `--pre`. Loop 4 har inget Calyx-fönster; jättefönstret (2 700 + 28) som byggd: 94,1 ms median (`shots/loop-4/probe/ab/giant-asbuilt-*`).
2. Ändra rad 677 och 678 enligt Target.
3. Pixelkontroll (scratch, som `shots/loop-4/scripts/verify_astra4.py`): wrappern i vy, ramen monterad, `--rv` tvingad till 0 / 0,25 / 0,5 / 1: andel wrapperbakgrund (`#e9e5da`) i wrapperns yta ≈ 100 / 75 / 50 / 0 % (± 3 %); innehållet i den synliga delen vid 0,5 pixelidentiskt med samma region vid 1 (diff 0); vid 1 identiskt med R9 (`shots/loop-4/astra-verify/calyx-rv1.png`) och R8:s `shots/r8/calyx12-1440-11.png`. Jämför 0,25 / 0,5 mot R8:s `calyx12-1440-03.png`, `-05.png` (± 8 px i öppningens kant).
4. Tolv ramar genom `.calyx-fig` (som R9:s `shots/r9/p036/calyx-life-*.png`): öppningen dras upp uppifrån och ned, tallriken (Hōrai) och blommorna (Calyx) står stilla.
5. **Mät efter** som steg 1: p95 inte sämre än före + 5 ms; `.calyx-wrap:--rv` staircase 0.
6. Ramarnas vandring (027 steg 2, 3) och sömn vid scrollY 0: oförändrat; en resurspost per ram.

## Boundaries

- Rör inte `.horai-wrap .rv`, `measureFrames()`, `--rv-s/--rv-w/--rv-h`.
- Rör inte revealfönstret (`from` 0,02, `to` 0,30 i `reveals`).
- Matchar inte rad 650 eller 676 till 678: STOPPA.

## Verification

- **Mekaniskt:** steg 3 (andelar och pixeldiff), steg 5 (tal), steg 6.
- **Skärmbild:** steg 3:s fyra lägen; `slices-1440/…s04` och `slices-390/…s04` oförändrade (`--rv` 1 där); i en skiva där `.calyx-wrap` står med `--rv` ≈ 0,5 syns wrapperns övre halva som Calyx och nedre halva som `#e9e5da`.
- **Feel check:** hjul in i bandet vid 1440: Calyx dras upp ur wrapperns överkant medan blommorna står stilla; ingen ram som "bara finns".
- **Done when:** H-27 bockad utan not om Calyx; H-25:s Calyx-rad sann.
