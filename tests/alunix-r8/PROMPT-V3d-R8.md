# Alunix, V3d runda 8: Astras granskning av R7. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Läs `{{UT_MAPP}}/reviews/r7-astra.md` i sin helhet. Svaret är `fix`, med åtta material_fixes
som är verifierade mot fil och bild. Bevisen ligger i `{{UT_MAPP}}/shots/astra-r7/`. Lead tar
alla åtta i Astras ordning:

1. **Tesbandets meningar ligger över varandra i varje byte**, som mest 130 px vid 1440.
   **Mål:** i varje bildruta syns högst en mening, eller en ren övergång där glyferna aldrig
   överlagras. Använd en mask eller klippning, eller låt den ingående meningen öppna först
   när den utgående är helt ute.
2. **`.case--calyx{--bg:var(--bg)}` pekar på sig själv**, så grunden blir genomskinlig och
   heroens foto syns bakom Calyx-caset. Rätta den till en riktig grund, vald i planens
   balans.
3. **Stegen i casen överlappar på samma sätt som tesbandet**, 9 px i varje byte. Samma mål
   som fix 1.
4. **Hōrais citat pekas ut med `-0.40`.** Sektionen ska stå centrerad i ramen (ungefär
   `+0.15`), så att citatet står format och skarpt.
5. **Calyx-ramen är 56 % av bredden och 87,7 % av höjden.** Målet är minst 58 % och 88 % vid
   1440, och minst 50 % av höjden vid 390.
6. **Hyperborea-bilden i tesbandet är 34,4 % av bredden.** Målet är minst 36 %.
7. **Vid 390 blir ett tomt blått band på cirka 220 px kvar** under meningen. Reservera höjd
   efter den faktiska längsta meningen och bredden.
8. **`ridaY(150)` i förhandsvisningen hamnar fel.** Den ska vara `ridaY(120)`, alltså
   kapitelskärmen ensam.

## Gör
- Kör `Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` först.
- Skriv planen `{{UT_MAPP}}/plans/055-astra-r7.md`.
- Använd kirurgiska `Edit`. Copyn rörs inte.
- Inget djärvt drag får backas.

## Verifiera
- **Fix 1 och 3:** ta en hjulsekvens i 20 px-steg genom varje byte, vid 1440, 768 och 390.
  Mät det vertikala överlappet mellan synliga meningar och synliga steg, och det ska vara
  0 px i varje bildruta. Läs bilderna.
- **Fix 2:** kontrollera att grunden bakom Calyx-caset är täckande.
- **Övriga fixar:** mät dem mot målen ovan.
- **Grind:** noll horisontell scroll 320–1920, `a11y_scan` vid 390 och 1440, rubrikskriptet
  (noll delade ord), låst copy 15/15, grep för tankstreck och `prefers-reduced-motion`, samt
  `motion_probe` för tessektionen och casen vid 1440.

Leverans: `NOTES.md` § V3d R8 med en tabell över fix, mål, före, efter och bild. Sista raden
ska vara `V3d R8 klar` eller `[PAUSED — steg X]`.
