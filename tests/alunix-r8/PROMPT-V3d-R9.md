# Alunix, V3d runda 9: tre mobilfynd från Astra. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Läs `{{UT_MAPP}}/reviews/r8-astra.md`. Svaret är `fix`, med tre material_fixes, och alla gäller
bara 390. Vid 1440 håller varje PARITET-rad. **Ingenting vid 1440 får ändras.** Bevisen ligger
i `{{UT_MAPP}}/shots/astra-r8/`.

1. **Hōrais citat syns inte vid 390.** Vid `case-horai-03` ligger citatet bakom sajtens egen
   nav, eftersom ramens innerhöjd är 450 px. Orsaken är Hōrais egen layout, och `sites/*`
   rörs aldrig. Lös det med ramens höjd eller med ankaret på vår sida.
   **Mål:** citatet syns helt i ramen, under navens underkant.
2. **Tomt blått band i tesbandet vid 390.** Det är 285 px mellan tickstrecken och fotot, och
   fotot är 343×215. Orsaken är att figuren ärver `align-self:end` och fotolådan har
   `aspect-ratio:16/10`.
   **Mål:** högst 32 px mellan strecken och fotot, och fotot minst 400 px högt, eller en
   komposition som fyller skärmen utan ett tomt band.
3. **Calyx steg 03 vid 390.** Ramen visar ett foto, men dess bildtext ligger nedanför ramen.
   **Mål:** minst ett foto med sin bildtext helt inne i ramen.

## Gör
- Kör `Skill(design)` först.
- Skriv planen `{{UT_MAPP}}/plans/056-astra-r8-mobil.md`.
- Använd kirurgiska `Edit`. Copyn rörs inte.

## Verifiera
- Ta enskilda skärmbilder (inga kontaktark som bevis) vid 390 och 375 för
  `?preview=thesis-01..05`, `case-horai-03` och `case-calyx-03`, och i hjulsekvens genom
  samma lägen. Läs dem.
- Ta samma lägen vid 1440 och jämför dem pixel för pixel mot före-bilderna i `astra-r8/ours/`.
  De ska vara oförändrade.
- Kör en kort grind: noll horisontell scroll 320–1920, `a11y_scan` vid 390, låst copy 15/15
  och noll tankstreck.

Leverans: `NOTES.md` § V3d R9. Sista raden ska vara `V3d R9 klar` eller `[PAUSED — steg X]`.
