# 053 — Astras tredje granskning (r5-astra.md), fyra material_fixes

V3d runda 6. Astras tredje pass, paritetsläget: `reviews/r5-astra.md` läst i sin helhet.
13/16 paritetsrader håller. Lead tar alla fyra `material_fixes`. Bevis:
`shots/astra-r5/measure.json`, strip- och zoombilderna. Fyra fix, inget annat rörs.

## Fix 1 (HIGH) — mobilarket, steg 06/07: ritningen ligger ovanpå Calyx

`zoom-P12-390-sheet.png`: `#p-glyph` (ordmärket, `translate(24,24)`, ark-fast viewBox-
koordinat) ligger i full ton över fotots övre vänstra hörn. `zoom-P13-390-sheet.png`:
`#p-title`/`#p-rev` (revisionsfältet, mobil-CSS `y16..52`, en tre-radig ISO 7200-stapel
ärvd från FÖRE R5) korsar Calyx nav i övre högra hörnet. Rotorsak: R5 flyttade öppningen
(`#p-opening` y20..191) men rörde varken glyfens fasta koordinat eller revisionsfältets
egna. Samtidigt: mobilzoomen (`#p-cam`, `1+0,08*--cam`) gör öppningen 304×1,08=328
breddenheter > arkets 320 vid `--cam`=1 — uppmätt 367px liveyta i ett 358px ark.

**Fix:**
- `#p-glyph{opacity:var(--cam-fade)}` (mobilt scope). Samma tillbakadragningsmönster som
  `#p-hatch`/`#p-ledgers` redan har (R4 fix 8, rad ~1218) — glyfen tonar ut i takt med att
  kameran zoomar in 05→07, i stället för att stå kvar permanent.
- `#p-title`/`#p-rev` flyttade till den fria remsan OVANFÖR öppningen (y0..20, tom yta)
  och krympta till samma enradiga 32×16-box som skrivbordets (846..876,2..18) redan
  använder: `M280 2 H312 V18 H280 Z` / `x280 y2 w32 h16`.
- `#p-cam` mobilzoom `0,08`→`0,05`: 304×1,05=319,2 ≤ 320, ingen beskärning mot arkets
  egen kant.

**Mål:** inga ritelement ovanpå bilden i steg 06/07 vid 390 eller 768 (768 använder redan
skrivbordskoordinater, obeskurna, ingen kodändring där); bildens alla fyra kanter inom
arket.

## Fix 2 (HIGH) — revisionsbokstaven "A" vid 1440

`MOBILE_TEXT['p-c-rev']` hade kvar `[54,451]` som SKRIVBORDS-koordinat (dött värde sedan
före R4 — `plansch()` skriver alltid markupens egna `x="861" y="13"` på ≥768, listans
index 0/1 påverkar bara <768, men värdet motsade DOM:en och riskerade framtida fel).

**Fix:** `MOBILE_TEXT['p-c-rev']` satt till `[861, 13, 296, 13]` — skrivbordsindex rättat
till markupens verkliga tal, mobilindex flyttat till centrum av fix 1:s nya 32×16-fält
(280..312 → mitten x=296; samma 11px-offset från fältets topp som skrivbordets 861/13 har
i sitt eget 846..876,2..18-fält → y=13).

**Mål:** "A" i revisionsfältet, aldrig över bilden, vid 1440 och 390.

## Fix 3 (HIGH) — aktens utgång vid 1440

Uppmätt (binärsökning, `getBoundingClientRect` var 10:e px 13000–15500): `.process-stick`
släpper vid scrollY≈14020, `.step-band` för steg 07 vid ≈14160 — en 140px lucka där arket
(z-index 2, solid `--bg`) redan glider uppåt medan "07"/FÖRVALTNING fortfarande står
fastnaglad på `top:0`, och skär av texten.

Orsak: `.process-stick`s sticky-behållare är `.process-grid`, som ärver
`.process-steps`s totalhöjd (inklusive `padding-bottom`) — den paddingen styr alltså
STICKENS EGEN släpppunkt. Band 07:s släpp är oberoende av den (bara li07:s egen höjd mot
`--band-h`). R4:s 60svh räckte inte.

**Fix (uppmätt, inte gissat — samma binärsökning körd mot flera paddingvärden):**
`.process-steps{padding-bottom:60svh→80svh}`. Vid 80svh släpper stick vid ≈14200, 40px
EFTER band 07:s eget släpp (≈14160) — bandet hinner alltid lämna scenen innan arket
glider över det.

**Mål:** i en hjulsekvens var 20:e px 13980–14240 vid 1440 är "07"/FÖRVALTNING/brödtexten
antingen hela eller rullar ut i överkant, aldrig avskurna av arkets överkant.

## Fix 4 (HIGH) — jätterubrikens typografiska ögonblick (P04)

`.giant` clampar till 5,5rem (88px) vid 1440 — mindre än kapitelrubrikens 103,68px.
Jätten ska vara sidans starkaste ögonblick efter heron.

**Fix:** `transform:scale()`-mekanismen (som bara ändrar det MÅLADE, aldrig layouten —
ordbrytningen förblir låst vid basclampens 88px oavsett skalvärde) ersatt med en riktig
`font-size`-höjning bunden till `--scrub` (samma variabel som redan styr plåtens
breddökning, `margin-left`/`width`, rad ~951) i stället för det tidigare `--sc-ps`:

```
@media (min-width:901px){
  .js .giant{font-size:calc(clamp(2.1rem,7.4vw - 18px,5.5rem) + var(--scrub,0) * 1.75rem);}
}
```

Vid `--scrub`=0 (plåtens smala 555px-startläge, PLAN 030:s ordbrytningsspalt): 88px,
oförändrad, känd säker marginal (VARUMÄRKE mäter 542px, 13px marginal). Vid `--scrub`=1
(den utskrivna plåten, ≥1189px bred): 88+28=116px, 12px marginal över 110px-golvet.
Skopat till ≥901px (samma brytpunkt som `.panel-giant`s bleed) — under den rörs
basclampen inte, redan verifierad ordbrytningsfri vid 768.

**Mål:** `?preview=ledger` vid 1440: h2 ≥110px, 0 delade ord vid 1024/1280/1440/1920,
VARUMÄRKE helt på en rad.

## Gör

1. Kirurgiska `Edit` för de fyra fixarna ovan.
2. Hjulsekvenser genom processaktens slut vid 1440 (40px-steg), steg 06/07 vid 390 och
   768, jättesektionen vid 768/1024/1280/1440/1920 → `shots/r6/`, läs dem.
3. Kort grind: noll horisontell scroll 320-1920, `a11y_scan` (390, 1440), rubrikskript
   (noll delade ord), låst copy 15/15, grep tankstreck/`prefers-reduced-motion`,
   `motion_probe` för `#process` vid 1440.
4. `NOTES.md` § V3d R6, sista raden `V3d R6 klar` eller `[PAUSED — steg X]`.
