# Alunix r9, runda 13. Cell {{KONCEPT}}. Arket täcker stegtexten mellan 768 och 1279.

En fix. Lead hittade den i exit-granskningens pixlar och mätte den. Ut-mapp `{{UT_MAPP}}`,
port {{PORT}}.

## Felet, mätt av lead 2026-09-17

I planschläget (`@media (max-width:1279px)`, `index.html` rad ~1088) är
`.process-stick` `position:sticky; top:0; z-index:2` med ogenomskinlig
`background:var(--bg)` och `width:min(100%,480px,calc((100svh - 224px) * 320 / 360))`,
`justify-self:center`. `.process-steps` ligger i samma gridcell men tar **full spaltbredd**.
Under 640 px bredd sammanfaller de, så texten passerar snyggt under arket. Över det är arket
smalare än texten, och texten sticker ut på båda sidor om det ogenomskinliga arket och blir
klippt mitt i orden.

Uppmätt överlapp mellan `.process-stick` och `.process-steps li`, vid `scrollY = 0,62 × höjd`:

| Bredd | Arkets box (l, t, b, h) | Överlappande steg | Vertikalt överlapp |
|---|---|---|---|
| 768 | 144, 0, 480, 564 | 01 | 413 px |
| 900 | 210, 0, 480, 564 | 01, 02 | 416 px, 7 px |
| 1024 | 272, 0, 480, 564 | 02, 03 | 275 px, 289 px |
| 1279 | 400, 0, 480, 564 | 02, 03 | 297 px, 267 px |
| 1280 | 512, 153, 691, 389 | inget | 0 (tvåspaltsläget, korrekt) |

Bevis: `{{UT_MAPP}}/shots/final-widths/process-768.png` (steg 01:s rubrik och stycke klipps
i arkets vänsterkant) mot `process-414.png` och `process-320.png`, där texten ligger hel
under arket.

## Fixen

Målet: **texten får aldrig ligga bredare än det sticky arket i planschläget.** Texten ska
passera under arket i samma spalt, som den redan gör vid 320 och 414.

Kravet, och bara det: i `@media (max-width:1279px)`, ge `.process-steps` samma bredd och
samma centrering som `.process-stick` (samma `width`-uttryck, `justify-self:center`), eller
lös det på ett sätt du kan försvara som ger samma resultat. Rör inte tvåspaltsläget
(≥ 1280), inte `.process-stick`s egna mått, inte SVG:ns planschgeometri, inte DOM-ordningen.

Skriv planen som `{{UT_MAPP}}/plans/047-arket-tacker-texten-768.md` i PLAN-TEMPLATE-format
innan du redigerar, med tabellen ovan som Problem och målvärdet nedan som Target, och lägg
in den i `plans/README.md`.

## Verifiering, målvärde

1. **Noll överlapp:** mät `.process-stick` mot varje `.process-steps li` vid 640, 768, 900,
   1024, 1180, 1279 och 1280, vid tre scrollpositioner i akten (0,45 / 0,62 / 0,80 av
   dokumenthöjden). Inget par får ha både horisontellt och vertikalt överlapp över 4 px.
2. **Texten hel:** skärmbilder vid 768, 900 och 1024 i akten; ingen rad får klippas
   horisontellt. Läs dem som bilder.
3. **Radlängd:** brödtextens measure får inte falla under 36 tecken vid någon av bredderna
   (house-physics måttet). Mät i tecken, inte i px.
4. **Inget annat rörs:** 320, 375, 414, 390 och 1440 ser ut exakt som före (skärmbilder före
   och efter, samma scrollpositioner), noll horisontell scroll vid alla bredder.
5. `?process=invert` har samma geometri som pappersläget vid alla testade bredder.
6. Kort grind: `scroll_verify` vid 768 och 1440, `a11y_scan` och `reflow` vid 768, grep för
   tankstreck och inline-hex i de nya raderna. Ingen `motion_probe` behövs, ingen rörelse
   ändras.

## Invarianter

Kirurgiska `Edit`-anrop, aldrig `Write` av hela filen, aldrig shell-skrivningar. Låst copy
rörs inte. Motorn och `sites/*` rörs aldrig. F-011, F-014 gäller. Fullständig output.

## Leverans

`{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/plans/047-*.md`, `{{UT_MAPP}}/shots/r13/`,
`{{UT_MAPP}}/NOTES.md` § R13 med tabellen från punkt 1 före och efter.
Sista raden: `R13 klar` eller `[PAUSED — steg X]`.
