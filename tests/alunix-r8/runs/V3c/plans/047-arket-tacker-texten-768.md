# 047 — Arket täcker stegtexten mellan 768 och 1279

- **Status**: TODO
- **Commit**: `ee0999d4` (R12-final, `runs/V3c/index.html`)
- **Severity**: HIGH
- **Category**: Visuellt / layout, planschläget (`@media (max-width:1279px)`)
- **Estimated scope**: 1 fil, en `Edit` (ett nytt deklarationsblock)

## Problem

`.process-grid` blir en enkolumnsgrid i planschläget (`index.html:1089`,
`grid-template-columns:1fr; row-gap:0;`). Dess två barn — `.process-stick` (arket, rad
1097-1099) och `.process-steps` (steglistan, rad 894) — hamnar därmed i var sin
grid-rad (uppmätt: `grid-template-rows: 564px 3093.2px` vid 768px), men eftersom arket är
`position:sticky;top:0` stannar det pinnat överst i viewporten medan listans rad scrollar
förbi under det — precis det avsedda "arket flyter över texten som passerar"-mönstret.

Bristen är horisontell, inte vertikal: arket är centrerat och smalare än kolumnen
(`.process-stick{width:min(100%,480px,calc((100svh - 224px) * 320 / 360));
justify-self:center;}`, index.html:1097-1099), men `.process-steps` och dess `<li>`
ärver ingen egen bredd eller centrering och fyller därför HELA kolumnen
(`grid-template-columns:1fr` ger dem 100% av den tillgängliga bredden, vänsterjusterat
som block).

Uppmätt vid 768px, scrollY = 0,62 × dokumenthöjd (`.process-p` i steg 1, `max-width:34ch`
från index.html:900, oförändrad av denna plan):

```
.process-stick  x:144  bredd:480  (centrerat i kolumnen, 675,8px bred)
.process-steps  x:46   bredd:675,8 (vänsterjusterat, full kolumnbredd)
.process-p      x:46   bredd:328  (34ch, vänsterjusterat inom <li>)
```

Textblocket (x 46–374) och arket (x 144–624) överlappar horisontellt i intervallet
x 144–374 (230px): textens vänstra kant (x 46–144, cirka 98px, en handfull tecken per rad)
syns fritt, resten av raden går rakt in under arkets ogenomskinliga bakgrund
(`background:var(--bg)`, `z-index:2`) och klipps mitt i ordet. Arkets högra parti
(x 374–624) täcker ingenting, eftersom textblocket aldrig når dit.

Lead mätte det vertikala överlappet (samma symptom, olika bredder):

| Bredd | Arkets box (l, t, b, h) | Överlappande steg | Vertikalt överlapp |
|---|---|---|---|
| 768 | 144, 0, 480, 564 | 01 | 413 px |
| 900 | 210, 0, 480, 564 | 01, 02 | 416 px, 7 px |
| 1024 | 272, 0, 480, 564 | 02, 03 | 275 px, 289 px |
| 1279 | 400, 0, 480, 564 | 02, 03 | 297 px, 267 px |
| 1280 | 512, 153, 691, 389 | inget | 0 (tvåspaltsläget, korrekt) |

Bevis: `shots/final-widths/process-768.png` (steg 01:s rubrik och stycke klipps i arkets
vänsterkant) mot `process-414.png` och `process-320.png`, där texten ligger hel under
arket — vid 640px och smalare sammanfaller `.process-steps`s fulla kolumnbredd redan med
(eller understiger) arkets 480px, så felet syns bara i den öppna remsan 641–1279px.

## Target

```css
/* target, index.html, i @media (max-width:1279px)-blocket, direkt efter .process-stick */
.process-steps{width:min(100%,480px,calc((100svh - 224px) * 320 / 360));
  justify-self:center;}
```

Samma `width`-uttryck och samma `justify-self:center` som `.process-stick` bär redan
(index.html:1097-1099), ordagrant kopierat. Listan (och därmed varje `<li>`, som är ett
block-barn utan egen bredd) centreras i kolumnen och krymper till exakt samma box som
arket — vid varje viewport-höjd, inklusive den korta-viewport-tredje-termen som redan
håller arket inom `100svh - 224px`. `.process-p`/`.process-note`s egna `max-width:34ch`
rörs inte: de var redan smalare än 480px, så deras radbrytning är oförändrad, bara
blockets POSITION flyttas så att det hamnar innanför arkets box i stället för att sticka
ut på vänster sida av den.

## Repo conventions to follow

- Samma mönster som `.process-stick` självt: `width:min(100%, 480px, calc((100svh -
  224px) * 320 / 360))` plus `justify-self:center` inom en `1fr`-grid (index.html:1097-1099,
  kommentaren där förklarar varför tredje termen finns — samma skäl gäller nu båda
  elementen, inte bara arket).
- Nya regler i planschläget läggs i samma `@media (max-width:1279px)`-block som redan
  finns (index.html:1088), inte ett nytt block.

## Steps

1. I `@media (max-width:1279px){...}` (index.html:1088), direkt efter
   `.process-stick{...}`-regeln (index.html:1097-1099) och före `.process-sheet{aspect-
   ratio:320/360;}` (index.html:1100), lägg till:
   ```css
   .process-steps{width:min(100%,480px,calc((100svh - 224px) * 320 / 360));
     justify-self:center;}
   ```
   En `Edit`. Ingen annan rad i blocket ändras.

## Boundaries

- Rör inte tvåspaltsläget (`≥1280px`, `.process-grid`s bas-regel index.html:887, eller
  `.process-stick`s bas-regel index.html:905).
- Rör inte `.process-stick`s egna mått eller dess `width`-uttryck — kopiera det, ändra
  det inte.
- Rör inte SVG:ns planschgeometri (`#p-outline`, `#p-opening`, `#p-open-rect`,
  `#p-live-img`, `#p-dim-width`, `#p-lead-169`, `#p-title`, `#p-rev`, `#p-m320` etc.,
  index.html:1108-1115).
- Rör inte DOM-ordningen (`order:-1` på `.process-stick` orörd).
- Rör inte `.process-p`/`.process-note`s `max-width:34ch`.
- Matchar inte ankarna i sak (radnummer kan ha drivit): STOPPA och rapportera i stället
  för att gissa.

## Verification

- **Mekaniskt:** noll horisontellt+vertikalt överlapp (>4px i båda) mellan
  `.process-stick` och varje `.process-steps li` vid 640, 768, 900, 1024, 1180, 1279 och
  1280px, vid scrollY 0,45 / 0,62 / 0,80 × dokumenthöjd.
- **Skärmbilder:** 768, 900, 1024px i akten, lästa som bilder — ingen rad klippt
  horisontellt.
- **Radlängd:** `.process-p`s renderade teckenantal per rad ≥36 tecken vid alla testade
  bredder (house-physics-måttet; mätt i tecken, inte px — `max-width:34ch` är en
  ch-enhet, inte en bokstavlig 34-tecken-garanti, så det faktiska antalet mäts separat).
- **Oförändrat på övriga breddpunkter:** 320, 375, 414, 390, 1440 — skärmbilder före/efter,
  samma scrollpositioner, pixelidentiska (tvåkolumnsläget och de smalaste breddpunkterna
  rörs inte av denna regel eftersom `.process-grid` där antingen är tvåkolumns eller redan
  smalare än 480px).
- **`?process=invert`:** samma geometri som pappersläget vid alla testade bredder (regeln
  är bredd/layout, inte ett invert-scopeat block, så den gäller identiskt i båda lägena).
- **Grind:** `scroll_verify` vid 768 och 1440 (om miljön tillåter — se R12:s NOTES för en
  dokumenterad instabilitet i det skriptet; fallback till `motion_probe`/`reflow.py`/
  `contrast_over_media` om det upprepas), `a11y_scan` och `reflow.py` vid 768, `grep` för
  tankstreck (0) och nya inline-hex (0) i den nya raden. Ingen `motion_probe` behövs —
  ingen rörelse ändras, bara en statisk bredd/centrering i ett media-query.
- **Feel check:** scrolla långsamt genom akten vid 768 och 1024px bredd; steg-texten ska
  antingen synas helt (innan/efter arkets sticky-fönster) eller vara helt dold bakom arket
  (aldrig ett halvt ord i kanten).
- **Done when:** noll mätt överlapp vid alla sju breddpunkter och alla tre
  scrollpositionerna, radlängden håller 36-teckensgolvet (eller avvikelsen är rapporterad
  ärligt), och 320/375/414/390/1440 är pixelidentiska med före-läget.
