# 055 — Astras granskning av R7 (reviews/r7-astra.md), åtta material_fixes

V3d runda 8. Astras fjärde pass, verifierad mot fil och bild. Lead tar alla åtta fynd i
Astras ordning. Copyn rörs inte. Åtta fix, inget annat rörs.

## Fix 1 & 3 (HIGH) — meningsbytet/stegbytet överlappar

`.js .ts`/`.js .cs` öppnar `--in` symmetriskt kring `a` (±f/2) och stänger `--out`
symmetriskt kring `b` (±f/2). Eftersom mening N:s `b` = mening (N+1):s `a` (samma punkt,
`(N+1)/5`), transformeras BÅDA samtidigt över samma fönster: utgående mening är fortfarande
delvis synlig (`--out`<1) medan inkommande redan börjat synas (`--in`>0). Uppmätt överlapp:
130px vid 1440, 62 vid 768, 41 vid 390 (tesen); 9px (casen).

**Fix:** asymmetriska fönster. `--in` öppnar över `[a, a+f]` (börjar vid sin EGEN start,
inte förr), `--out` stänger över `[b-f, b]` (slutar vid sin EGEN slutpunkt, inte senare).
Vid gränspunkten `b_N = a_{N+1}` möts de exakt: mening N:s `--out` har hunnit till 1 (helt
stängd) precis när mening (N+1):s `--in` fortfarande står på 0 (inte börjat) — en ren
växling, 0px överlapp, 0px lucka. Samma ändring i `.js .cs` (casen, generaliserat med
`--n`).

```css
.js .ts{--a:calc(var(--i) / 5);--b:calc((var(--i) + 1) / 5);--f:.04;
  --in:clamp(0,calc((var(--sc-ps,0) - var(--a)) / var(--f)),1);
  --out:clamp(0,calc((var(--sc-ps,0) - (var(--b) - var(--f))) / var(--f)),1);
  ...}
```

## Fix 2 (HIGH) — Calyx-stagens grund genomskinlig

`.case--calyx{--bg:var(--bg);--ink:var(--ink);}` är en cyklisk deklaration (samma
egenskap refererar sig själv på samma selektor) — ogiltig vid beräkningstid, `--bg` blir
tom, `.case-stage{background:var(--bg)}` faller till `transparent`. `.ground` (heroens
foto) syns igenom.

**Fix:** raden tas bort helt. `:root` sätter redan `--bg:#fdfbf4;--ink:#16140f` (rad 130),
och `#case-calyx` ärver dem ostört utan en lokal (trasig) omdeklaration — exakt samma
värden Astra räknar som Expected (`rgb(253, 251, 244)`).

## Fix 4 (HIGH) — Hōrais citatankare

`['#quote-section', -0.40]` lägger sektionens överkant 0,40×ramhöjd UNDER ramens topp.
Expected: sektionen centrerad i ramen. `sites/horai.html` `.quote-section` är
`h-[130vh]`; för en sektion H hög i en ram I hög blir "centrerad" scrollY = sectionTop +
H/2 − I/2, dvs. andra talet `a = H/(2I) − 0,5 = (1,3×I)/(2I) − 0,5 = 0,15` (oberoende av
I:s faktiska värde, ett förhållande). `-0.40` → `+0.15`.

## Fix 5 (HIGH) — Calyx-ramens storlek

Vid 1440: `.case-stage{grid-template-columns:minmax(0,5fr) minmax(0,7fr)}` ger
7/12×(1440−rail_x−gap) = 806px = 56%vw (mål ≥58%/836px). Bytt till `4fr/8fr`:
8/12×1296 = 864px ≈ 60%vw. `.case--horai`s spegelvända kolumner (`7fr/5fr`) bytt till
`8fr/4fr` för symmetri.

Höjd: `.case-stage{padding-block:clamp(24px,4svh,40px)}` äter 72px (36 topp + 36 botten)
ur en 900px stage, kvar 828px minus bildtextens ~39px = 789px = 87,7%vh (mål ≥88%/792px).
Padding-clamp sänkt till `clamp(16px,3svh,32px)` (27px vid 900) → 900−54−39=807px=89,7%vh.

Vid 390: `.case-stage{grid-template-rows:52svh minmax(0,1fr)}` ger case-fig 438,9px,
minus bildtext ≈39px = 400px = 47,4%vh (mål ≥50%/422px). `52svh`→`58svh`: 489,5−39=450,5px
=53,4%vh.

## Fix 6 (HIGH) — Hyperboreas andel av tesbandet

`.thesis-stage{grid-template-columns:minmax(0,1fr) minmax(0,.62fr)}` ger bildkolumnen
0,62/1,62×1296=496px=34,4%vw (mål ≥36%/519px). `.62fr`→`.7fr`: 0,7/1,7×1296=534px=37,1%vw.
Samma fr-tal, samma vw-förhållande vid 768 (kolumnerna är alla vw-relativa: rail-x och
gap är båda `clamp(…,Nvw,…)`), håller ≥36% där också.

## Fix 7 (HIGH) — tomt band vid 390

`.thesis-lines{min-height:calc(7 * .98 * fontsize)}` reserverar sju radhöjder, men ingen
mening tar mer än fyra (mening 3, längst, 60 tecken). `7`→`4` (139px i stället för 243px),
frigör ~104px. Det frigjorda utrymmet går till bilden: `.thesis-stage`s tredje rad
(`.thesis-figure`) sätts till `1fr` i stället för `auto`, och `.thesis-photo-box` får
`flex:1;min-height:0` i en `display:flex;flex-direction:column`-`.thesis-figure` — boxen
växer för att fylla den frigjorda höjden (redan `object-fit:cover`, ingen distorsion).
Bilden flyttar sig inte mellan meningarna (ingen av de nya reglerna läser `--sc-ps`).

## Fix 8 (MEDIUM) — `ridaY(150)` i förhandsvisningen

Hållarens fönster är 100svh lyft + 40svh ensam = 140vh. `ridaY(150)` siktar 10vh förbi,
in i band 01. `ridaY(120)` landar mitt i den ensamma 40vh-zonen (100 till 140), där
kapitelskärmen står ensam utan spår av band 01.

## Gör

1. Kirurgiska `Edit` för alla åtta fixar ovan. Copyn rörs inte.
2. Hjulsekvenser i 20px-steg genom varje tes-/casesteg-byte vid 1440, 768, 390 → mät
   vertikalt överlapp mellan synliga `.ts`/`.cs`, ska vara 0px i varje bildruta.
3. Mät Fix 2 (`getComputedStyle` backgroundColor), 4 (frame-läge, opacitet/blur), 5 och 6
   (`getBoundingClientRect`), 7 (min-height/faktisk höjd), 8 (`?preview=chapter`,
   band 01:s synlighet).
4. Kort grind: noll horisontell scroll 320-1920, `a11y_scan` vid 390/1440, rubrikskript
   (noll delade ord), låst copy 15/15, grep tankstreck/`prefers-reduced-motion`,
   `motion_probe` för tesen och casen vid 1440.
5. `NOTES.md` § V3d R8 med tabell: fix, mål, före, efter, bild.
