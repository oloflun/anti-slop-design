# 033 · Priset får sin scroll-lästa förändring: liggarens fyra hårlinjer dras in på `--sc-ps`

- **Status**: TODO (R8, loop 2)
- **Commit**: R7-läget av `runs/V3c/index.html`, md5 `d30355da`
- **Severity**: MEDIUM
- **Category**: Rörelse / flöde, H-25 (priset var den sista skärmen utan scroll-läst förändring efter plan 015), T-8:s språk
- **Estimated scope**: 1 fil, ~6 rader CSS
- **Källor**: HELHET H-25 loop 1 ("priset står kvar till loop 2"); loop 2 `shots/loop-2/process-1440/v3c-1440-life-00.png` (priset stilla), `slices-1440/v3c-1440--s05.png`, `slices-390/v3c-390--s06.png`; avslutets `.close-rule` (plan 015, rad 1003-1004) som förebild

## Problem

Varje skärm ska bära minst en scroll-läst förändring som syns i en tolvstegs ramsekvens
(H-25). Efter R7 saknar bara priset den: blocket står stilla från det att det kommer in
tills det lämnar (`life-00.png`, `s05`). Blocket är en `data-sc-act="flow"` (rad 1142) och
har därmed redan ett eget `--sc-ps` (0 när dess överkant når viewportens underkant, 1 när
dess underkant lämnar överkanten) som ingen regel läser.

```css
/* index.html:687-690 - current */
  .price-ledger{margin-top:2rem;border-top:1px solid var(--hairline-dark);max-width:64ch;}
  .price-row{display:flex;flex-wrap:wrap;justify-content:space-between;
    align-items:baseline;gap:6px 24px;padding:.9rem 0;
    border-bottom:1px solid var(--hairline-dark);}
```

## Target

Samma språk som avslutets hårlinje (plan 015) och arkets måttlinjer: liggarens fyra
hårlinjer (topplinjen + tre radlinjer) ritas från vänster i följd medan blocket passerar
viewportens mitt. Ren CSS ur `--sc-ps`, ingen JS, inga nya färger.

```css
/* target, index.html:687-690 */
  /* PLAN 033, H-25: prisliggarens linjer dras in på --sc-ps (F-014), i följd
     uppifrån, i fönstret 0,18 till 0,50 av aktens liv (blocket i viewportens
     mitt vid 1440: --sc-ps ~0,35). Samma grepp som .close-rule (plan 015). */
  .price-ledger{margin-top:2rem;max-width:64ch;position:relative;}
  .price-ledger::before,.price-row::after{content:"";display:block;height:1px;
    background:var(--hairline-dark);transform-origin:left center;
    transform:scaleX(clamp(0,calc((var(--sc-ps,0) - var(--d,0.18)) / 0.14),1));}
  .price-ledger::before{--d:0.18;}
  .price-row{display:flex;flex-wrap:wrap;justify-content:space-between;
    align-items:baseline;gap:6px 24px;padding:.9rem 0 0;position:relative;}
  .price-row::after{width:100%;margin-top:.9rem;}
  .price-row:nth-child(1)::after{--d:0.24;}
  .price-row:nth-child(2)::after{--d:0.30;}
  .price-row:nth-child(3)::after{--d:0.36;}
```

`border-top`/`border-bottom` på rad 687 och 690 tas bort (linjerna är nu pseudoelementen,
samma 1 px, samma token). No-JS: `--sc-ps` är 0 → `scaleX(0)`: linjerna saknas utan
skript. Det bryter "fails toward visible" för en dekorlinje men inte för innehåll; om
lead vill ha golvet: `.no-js .price-ledger::before,.no-js .price-row::after{transform:none}`
(en rad, `html.no-js` finns redan, rad 64).

Fönstren: aktens liv är `h + vh` = 864 + 900 px vid 1440; 0,18 → 0,50 av det är 318 →
882 px scroll, alltså från att blocket är en tredjedel inne tills det passerat mitten.
Vid 390 (816 + 844): 0,18 → 0,50 = 299 → 830 px. Byggaren mäter att `--sc-ps` på `.price`
faktiskt når ≥ 0,50 innan blocket lämnar viewportens övre halva (det gör den: 0,50 = mitt
i livet); annars justeras `--d`-serien nedåt.

## Repo conventions to follow

- Allt som rör sig läser `--sc-ps` (F-014), ren CSS, ingen `transition`, ingen
  `will-change` (rad 1003-1004 är förebilden).
- Hårlinjer per grund: `--hairline-dark` (rad 137) på grafitplanet.
- `@property` behövs inte (`--d` är en konstant per element, ingen interpolation).
- Ledgerrad i `BRIEF.md` § Byggarens rader, R8: "Prisliggarens linjer på `--sc-ps`".

## Steps

1. Byt rad 687-690 enligt Target (och rad 1026: `.price-row{flex-direction:column}` vid
   ≤ 768 står; `::after` som block fungerar i kolumnriktning).
2. Mät `--sc-ps` på `.price` vid tre scrollägen (blocket 1/3 inne, centrerat, 1/3 kvar)
   vid 1440 och 390: fönstret 0,18 till 0,50 ska ligga inom de tre lägena.
3. Tolv ramar genom `.price` (som `frames.py life`) vid 1440 och 390: linjerna dras in
   en efter en uppifrån; i ram 12 alla fyra hela.
4. Kontrast och layout: raderna behåller sin höjd (`.price-row` höjd före/efter lika ± 1
   px; padding-bottom flyttades till `::after`s margin).

## Boundaries

- Rör inte priserna, etiketterna, `.statement`, `--c-graphite` (plan 013) eller
  `content-visibility:auto` på `.price` (rad 677: `contain-intrinsic-size` står).
- Matchar inte rad 687-694: STOPPA.

## Verification

- **Mekaniskt:** steg 2 och 3; `motion_probe.py --track ".price:--sc-ps"` (start
  `.price.top − 900`, 100:60) vid **cpu 1**: staircase 0, max_step ≤ 3 % (loop 2 mätte
  `.price:--sc-ps` 16,41 % vid cpu 4 och `footer.close` 5,79 % vid cpu 4 mot 2,80 % vid
  cpu 1: en flow-akt med ~1 800 px liv stegar bara när bildtiden faller, H-23-noten);
  cpu 4 rapporteras. `perf_probe` CLS oförändrad (0).
- **Skärmbild:** tolv ramar: ram 3 till 4 topplinjen halvdragen, ram 8 alla fyra hela;
  `s05` vid 1440 med blocket centrerat: fyra hela linjer.
- **Feel check:** scrolla in priset i vanlig hjulfart: linjerna ritar sig i takt med
  blocket, uppifrån och ned, samma tempo som avslutets linje.
- **Done when:** H-25 bockad (alla skärmar bär en scroll-läst förändring) med ramsekvensen.
