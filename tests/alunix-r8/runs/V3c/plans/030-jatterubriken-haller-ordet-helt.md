# 030 · Jätterubriken håller `VARUMÄRKE.` helt: 88 px och −0,04em i den spalt som finns

- **Status**: TODO (R8, loop 2)
- **Severity**: MEDIUM (låst copy delad mitt i ordet på sidans största rubrik)
- **Commit**: R7-läget av `runs/V3c/index.html`, md5 `d30355da`
- **Category**: Visuellt (typografi), H-07, T-5, gate 51-familjen; leadens R7-fynd 3
- **Estimated scope**: 1 fil, 2 rader CSS
- **Källor**: leadens pixelläsning R7 (`s1440-03`, `s1440-04`: `VARUMÄRK` / `E.`); loop 2 `shots/loop-2/diag/diag3.json` `C_giant` (ordbredd × storlek × spärrning), scratch `synth3.py` (kandidatklämman vid 901/1024/1280/1440), `slices-1440/v3c-1440--s03.png`, `preview/preview-1440-ledger.png`

## Problem

Plan 014 höjde taket till 6rem (96 px) mot en antagen spaltbredd på 640 px. Den faktiska
textspalten i `.panel-giant` är **555,2 px** (spalten 651 px minus 48 px padding på var
sida), och `VARUMÄRKE.` mäter **601,5 px** vid 96 px / −0,03em. Ordet får inte plats på
en rad, `hyphens:auto` (R7:s avvikelse) har ingen svensk ordlista i Chrome på Windows och
delar därför inte alls, och `overflow-wrap:anywhere` kapar det där raden tar slut:
`VARUMÄRK` / `E.` (`s1440-03`, `preview-1440-ledger`). Det låsta ordet läses inte som ett
ord.

```css
/* index.html:712-725 - current */
  .giant{font-family:var(--f-display);font-weight:700;
    font-size:clamp(2.1rem,6.7vw,6rem);line-height:.96;letter-spacing:-.03em;
    text-transform:uppercase;text-wrap:balance;overflow-wrap:anywhere;min-width:0;
    hyphens:auto;
    transform-origin:left center;}
```

Uppmätt ordbredd (Geist 700, versaler), fits = ≤ 555,2 px:

| storlek | −0,03em | −0,04em | −0,05em |
|---|---|---|---|
| 96 px | 601,5 | 591,8 | 582,3 |
| 92 px | 576,4 | 567,2 | 558,0 |
| 90 px | 563,9 | **554,9** | 545,9 |
| 88 px | 551,3 | **542,5** | 533,7 |
| 84 px | 526,3 | 517,9 | 509,5 |

96 px kräver en spalt ≥ 606 px (−0,03em) och den finns inte i tvåspaltsbandet: att sänka
panelens padding till 24 px ger 603 px och 96/−0,04em (591,8) med 11 px marginal, men
lägger rubriken 24 px från papperskanten mot liggarens 48, och tar bort ett rail-mått.
Q30 (fem helbredds akter) skulle ge spalten; den frågan är Antons. Det som håller i
dagens band: **88 px vid −0,04em** (542,5 px, 13 px marginal), 5,5 gånger brödtexten
(TASTE § 2.4: ≥ 5 gånger).

Kandidatklämman `clamp(2.1rem, 7.4vw - 18px, 5.5rem)` med `letter-spacing:-.04em` mätt i
sidan (`synth3.py`, `hyphens:manual`, ordet som ett `Range`):

| bredd | spalt | font-size | ordbredd | ordet helt (1 rect) | rader |
|---|---|---|---|---|---|
| 901 | 315,4 | 48,7 | 300,1 | ja | 3 |
| 1024 | 364,8 | 57,8 | 356,2 | ja | 3 |
| 1280 | 480,0 | 76,7 | 473,0 | ja | 3 |
| 1440 | 555,2 | 88,0 | 542,5 | ja | 3 |

Under 900 staplar spalterna (helbredd, 390: 33,6 px, två rader, ordet helt i
`preview-390-ledger.png`).

## Target

```css
/* target, index.html:713-724 */
    /* PLAN 030: 6rem (96 px) kräver en spalt >= 606 px; den faktiska är 555 px
       (651 - 2*48), så ordet VARUMÄRKE. (601 px) kapades mitt i (R7, lead).
       88 px vid -0,04em mäter 542 px och håller ordet helt vid 901..1440 (loop 2,
       synth3: 1 rect, 3 rader). hyphens:auto bort: ingen svensk ordlista i
       Chrome/Windows, och ett låst ord får aldrig delas. */
    font-size:clamp(2.1rem,7.4vw - 18px,5.5rem);line-height:.96;letter-spacing:-.04em;
    text-transform:uppercase;text-wrap:balance;overflow-wrap:anywhere;min-width:0;
    hyphens:manual;
```

`overflow-wrap:anywhere` står som sista skydd (gate 51) men ska aldrig fira för det här
ordet vid någon bredd ≥ 320.

## Repo conventions to follow

- Display sätts med `clamp()` (rad 330, 715); `.js .giant{transform:scale(...)}` (rad 729)
  läser `--sc-ps` och rörs inte.
- Låst copy: textnoden `VI BYGGER ERT VARUMÄRKE.` rörs inte; ingen `&shy;`.
- H-07:s tal: arkitekten skriver om raden till "≥ 88 px, ordet aldrig delat" med
  mätningen som skäl (HELHET § 3, loop 2) och lägger Q31 till Anton (96 px förutsätter
  Q30:s bredd). Ledgerrad i `BRIEF.md` § Byggarens rader, R8: "Jätterubriken 88 px".

## Steps

1. Byt rad 715 (font-size, letter-spacing) och rad 724 (`hyphens:auto` → `hyphens:manual`).
2. Mät vid 901, 1024, 1280, 1440 (och 320, 390, 768 som kontroll): `.giant` font-size,
   `getClientRects()` för ett `Range` över `VARUMÄRKE.` = 1, `scrollWidth ≤ clientWidth`.
3. Mät radantal vid 1440: 3 (`height / (font-size * 0.96)` avrundat).

## Boundaries

- Rör inte `.giant-sub`, liggaren, `--scrub`-fönstret (rad 711) eller `.panel-giant`s
  padding (alternativet ovan är förkastat, inte valt).
- Matchar inte rad 712-725: STOPPA.

## Verification

- **Mekaniskt:** steg 2 ger 1 rect och ingen overflow vid alla sju bredder; `reflow.py`
  320 + 200 % rent.
- **Skärmbild:** `?preview=ledger` vid 1440: `VI BYGGER / ERT / VARUMÄRKE.` på tre rader,
  ordet helt; vid 390 oförändrad mot `shots/loop-2/preview/preview-390-ledger.png`.
- **Feel check:** ingen (statisk typografi); skalsteget 0,92 → 1 på `--sc-ps` syns
  fortfarande i tolv ramar genom jätten.
- **Done when:** H-07 (omskriven till 88 px) bockad med `1 rect` vid 1440 och 1280.
