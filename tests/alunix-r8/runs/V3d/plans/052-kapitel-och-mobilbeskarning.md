# 052 — Kapitelskärmen mörk igen + Calyx obeskuren vid mobil

V3d runda 5. Lead har läst R4 i hjulscroll (900px/steg @1440, 800px/steg @390)
och hittat två fel som R4 själv introducerade. Två fix, inget annat rörs.

## Fel 1 (HIGH) — kapitelskärmen är ljus

`.process-chapter` (index.html rad ~1031) flippar lokalt `--bg:var(--c-paper);
--ink:var(--c-drafting)`. Det var R4 fix 3, ett svar på Astras "bryt de mörka
skärmarna" — men Anton har order på att processakten är helt inverterad, och
kapitelskärmen hör till akten (den är inte ett av de sju numrerade stegen, men
den är `#process`s eget barn, inte ett fristående mellanrum). Leads R4-prompt
strök uttryckligen 4-mörka-skärmar-gränsen. Den gäller inte.

**Fix:** ta bort `--bg`/`--ink`-flippen och `background`/`color`-satserna i
`.process-chapter` helt. `#process` sätter redan `--bg:var(--c-drafting);
--ink:var(--c-paper)` (rad ~1358) — utan den lokala flippen ärver
`.process-chapter` akten mörka grund/ljusa bläck automatiskt, precis som
resten av `#process`. `min-height:100svh;display:flex;flex-direction:column;
justify-content:center;padding-block` behålls oförändrat — det är den delen
som löser "ensam vid 1440, fyller sin skärm vid 390", och den är färgoberoende.

`#process .process-lead,.process-p{color:color-mix(in srgb,var(--ink) 78%,
var(--bg))}` (rad ~1365) rörs INTE — formeln är redan uttryckt i `--ink`/`--bg`
och blir automatiskt rätt (ljus text) när tokens inte längre flippas lokalt.

HTML-kommentaren ovanför `.process-chapter` i markupen (rad ~1693) uppdateras
så den inte längre hävdar en ljus grund som nu är felaktig.

Verifiering: `contrast_over_media.py --url` på kapitelrubriken/leaden vid
1440 och 390, plus en direkt skärmbildsläsning (samma false-positive-mönster
som R1/R2/R4 för `background-clip:text` gäller inte här — kapitlets text har
ingen sådan gradient).

## Fel 2 (HIGH) — Calyx beskärs vid 390

Mobilens öppning (`@media max-width:767px`, rad ~1449-1450) är 304×260 =
1,169:1. Källbilden är 16:9 (1,778:1) och `#p-live-img` använder
`preserveAspectRatio="xMidYMin slice"` (beskär till fyllnad, oavsett rutans
egen proportion) — mismatchen beskär bilden i sidled, rubriken "Botanical
architecture, from Stockholm." klipps till "mical / tecture / kholm" i steg
06/07.

Räkneexempel (dokumenterat i föregående runda): en 16:9-ruta som håller sig
inom nuvarande 320 breda viewBox kan aldrig nå 80% av en 320×300-yta (max
~54%). 80% OCH 16:9 OCH bredd ≤320 är ömsesidigt uteslutande i den formen.
Enda vägen, per leads egen instruktion: ändra arkets EGEN proportion vid
mobil, inte öppningens beskärning.

**Fix — ny mobil geometri, bredd 320 oförändrad (alla x-koordinater för
titelblock/16:9-callout/hatch/måttlinjer förblir giltiga), bara höjden och
öppningens höjd ändras:**

| Element | Före | Efter |
|---|---|---|
| viewBox (JS `plansch()` + CSS `.process-sheet`) | `320 300` | `320 200` |
| `#p-outline` (arkets ram) | `V299.5` | `V199.5` |
| `#p-opening`/`#p-open-rect`/`#p-live-img` | `y20 w304 h260` (→ x8..312, y20..280) | `y20 w304 h171` (→ x8..312, y20..191) — 304×171 = 16:9 exakt |
| `#p-dim-width` (måttlinjen under arket) | `M0 286 H320` | `M0 197 H320` (samma +6px-offset under öppningens nya underkant 191) |
| `MOBILE_TEXT.p-m320/p-m768/p-m1440` mobil-y | `276` | `187` (samma -4px-offset över öppningens nya underkant, oförändrat mönster) |
| `#p-cam` transform-origin | `160px 149px` | `160px 100px` (ny vertikal mittpunkt, 200/2) |

Allt som ligger nära öppningens TOPP (titelblock `#p-title`/`#p-rev` y16-52,
16:9-callout `#p-dot-169`/`#p-lead-169`/`p-c-169` y60-68) och allt som redan
ligger inom öppningens övre ~155px (`#p-hatch` y75-155, `#p-dim-row`,
`p-c-row`-etiketten) rörs INTE — öppningens topp (y20) är oförändrad och dess
nya underkant (191) ligger fortfarande gott om marginal under dem (155<191).

**Yta:** 304×171 / (320×200) = 51984/64000 = 81,2% — över Astras 80%-mål, med
marginal. Ingen beskärning: rutans egen proportion (16:9) matchar nu källbilden
exakt, så `preserveAspectRatio="xMidYMin slice"` beskär noll pixlar (slice-läget
blir identiskt med fit när rutans och bildens proportion redan är samma).

768 och 1024 (`@media max-width:1023px and min-width:768px`) rör varken
`#p-open-rect`/`#p-live-img`/`#p-cam` — `plansch()` läser
`matchMedia('(max-width:767px)')`, så 768+ faller igenom till
SKRIVBORDSKOORDINATERNA (538×303, redan 16:9, redan obeskuren). Kontrolleras
med en skärmbild vid 768, ingen kodändring väntad där.

`--sheet-h` är JS-uppmätt (rad ~2271, `getBoundingClientRect` i
`measureAct`), inte hårdkodad — anpassar sig automatiskt till den nya, kortare
arkhöjden utan egen ändring.

## Gör

1. Kirurgiska `Edit` för de två fixarna ovan.
2. Hjulscrollssekvenser (`mouse.wheel`) genom `#process` vid 390, 768, 1440 →
   `shots/r5/`, läs dem själv.
3. Kort grind: `contrast_over_media`, `a11y_scan` (390, 1440), noll
   horisontell scroll 320-1920, rubrikskript (noll delade ord), låst copy
   15/15, grep för tankstreck och `prefers-reduced-motion`.
4. `NOTES.md` § V3d R5, sista raden `V3d R5 klar` eller `[PAUSED — steg X]`.
