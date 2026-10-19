# Alunix, V3d runda 11: två mobilfynd från Astra. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Läs `{{UT_MAPP}}/reviews/r10-astra.md`. Svaret är `fix`, med två material_fixes, båda bara vid
390 och 375. Vid 1440 är sidan godkänd och oförändrad, och ingenting där får ändras.

1. **Tesbandets foto hoppar 35 px vid mening 3.** Orsaken är animationen av `letter-spacing`
   på mening 3 (`index.html` rad ~620, +0.06em), som gör att meningen bryts på 5 rader i
   stället för 4. Astra har visat att fotot står stilla i alla fem meningarna när
   `letter-spacing` låses under 768.
   **Mål:** fotots `top` är samma i alla fem meningarna vid 390 och 375, med ±1 px. Mät det i
   en hjulsekvens med 20 px-steg åt båda hållen.
2. **Calyx steg 03 beskär fotot 28 px upptill.** Ankaret ligger på rad ~2212.
   **Mål:** foto och märkning ligger helt inne i ramen vid 390 och 375. Använd offset 48 i
   stället för 76, eller ankra på `'#studio + section figure'`. Välj det som håller vid båda
   bredderna.

`Skill(design)` först. Använd kirurgiska `Edit`. Verifiera med enskilda skärmbilder och
mått. Jämför 1440 pixel för pixel mot `{{UT_MAPP}}/shots/astra-r10/ours/`. Kontrollera
också noll horisontell scroll. Leverans: `NOTES.md` § V3d R11. Sista raden ska vara
`V3d R11 klar`.
