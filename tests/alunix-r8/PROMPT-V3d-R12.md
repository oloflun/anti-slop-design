# Alunix, V3d runda 12: Hyperborea, ridån, case-rubrikerna och prisbron. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Antons feedback från 2026-09-19 finns inplanerad i `{{UT_MAPP}}/plans/057-hyperborea-ridan-case-pris.md`,
punkt 1–6. Copyn för casen, bryggan och prisbron har gått igenom copy-kedjan, med
humanizer-svenska sist, och ligger i `{{UT_MAPP}}/COPY-V3d-case-final.md`. Skriv in kolumnen
`final` ordagrant. Ändra ingen sträng. Ryms en sträng inte i layouten, stoppa och skriv en rad
i NOTES.

## Beslut som gäller
- **Punkt 6:** tesbandet slutar på "Vi hjälper er att synas på rätt sätt." Meningen
  `VI BYGGER ERT VARUMÄRKE.` tas bort helt. Anton har hävt låset på den strängen för V3d
  (PRODUCT.md rad 105), så den låsta copyn räknas som 14 strängar.
- **Q2, typsnitten i case-namnen:** Anton har inte godkänt nedladdning av Cardo- och
  Cinzel-filerna. Använd därför plan 057:s fallback, Geist, med samma tvådelade `h2`-struktur,
  så att typsnittet kan bytas senare med en ändrad token.
- **Q1, Q3 och Q4:** följ planens antaganden, alltså bilden fri från kanten, kickern orörd om
  copyn inte ändrar den, och ridån som en ren kant.

## Gör
- Kör `Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` först.
- Bygg planens Steps i ordning.
- Använd kirurgiska `Edit`. Inget djärvt drag får backas.
- F-011 och F-014 gäller. Motorn och `sites/*` rörs aldrig. Exakt två iframes. Ramarna
  transformeras aldrig. Antalet inline-hex får inte öka.

## Verifiera, innan du kallar något klart
1. Mät varje Target i plan 057 med skript och med bild, med `mouse.wheel`. Mät vid 1920x930,
   som är Antons skärm, samt vid 1440, 1024, 768, 390 och 375.
2. **Rullningslisterna mäts med synliga listor:** starta Chromium med
   `ignore_default_args=['--hide-scrollbars']`, annars syns de inte. Det är därför de missades
   i R1–R11.
3. **Ridån:** kör en hjulsekvens med 20 px-steg vid 1920, 1440, 768 och 390, med
   `elementFromPoint`-kontrollen ur planen. Kör den mot R11-läget först, så att du ser att den
   hittar felet.
4. Par-bilder, en skärmbild per sida, för P03, P04, P16, P17, P19, P20 och P21 vid 1920, 1440
   och 390. Lägg dem i `{{UT_MAPP}}/shots/r12/` och läs dem. Laga det som inte håller i samma
   runda.
5. Grinden:
   - `motion_probe` för tesbandet, casen och prisbron,
   - `contrast_over_media --url`,
   - `a11y_scan` och `reflow` vid 390 och 768,
   - noll horisontell scroll 320–1920,
   - rubrikskriptet, som ska ge noll delade ord,
   - låst copy 14/14,
   - grep för tankstreck, `prefers-reduced-motion` och inline-hex.

Leverans: `NOTES.md` § V3d R12 med en tabell över Target, mål, uppmätt värde och bild. Sista
raden ska vara `V3d R12 klar` eller `[PAUSED — steg X]`.
