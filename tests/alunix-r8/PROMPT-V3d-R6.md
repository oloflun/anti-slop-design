# Alunix, V3d runda 6: Astras tredje granskning. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Läs `{{UT_MAPP}}/reviews/r5-astra.md` i sin helhet. Svaret är `fix`, med fyra material_fixes.
13 av 16 paritetsrader håller nivån. Bevisen ligger i `{{UT_MAPP}}/shots/astra-r5/`
(`measure.json`, strip- och zoombilderna). Lead tar alla fyra fynden:

1. **Vid 390, steg 06 och 07, ligger ritningen kvar över Calyx.** `#p-glyph` står i full ton
   över bildens övre vänstra hörn. `#p-title` och `#p-rev` korsar Calyx navigation, en
   regression från R5, eftersom öppningen flyttades men ritelementen inte följde med. Zoomen
   1,08 gör dessutom bilden 367 px bred i ett ark på 358 px.
   **Mål:** inga ritelement ligger över bilden i steg 06 och 07 vid 390 eller 768, och bildens
   alla fyra kanter ligger inom arket.
2. **Revisionsbokstaven vid 1440.** `MOBILE_TEXT['p-c-rev']` har kvar skrivbordskoordinaterna
   54/451 och skriver över markupens 861/13. "A" hamnar därför över Calyx nedre vänstra hörn.
   **Mål:** "A" står i revisionsfältet och inte över bilden, vid både 1440 och 390.
3. **Aktens utgång vid 1440.** `.process-stick` släpper vid ungefär 14000, medan band 07
   ligger kvar sticky till ungefär 14160. Arket glider då upp över band 07 och skär av "07"
   och brödtexten.
   **Mål:** arket och band 07 släpper samtidigt, eller så lämnar bandet före arket. Ingen
   bildruta i en hjulsekvens med 40 px-steg genom 13800–14400 får skära av text.
4. **Jätterubriken (P04) ska vara sidans starkaste typografiska ögonblick efter heron.** I dag
   är `.giant` 88 px, alltså mindre än kapitelrubriken på 104 px.
   **Mål:** minst 110 px vid 1440. Inget ord får brytas vid någon bredd från 768 till 1920,
   och det låsta ordet VARUMÄRKE ska stå helt på en rad. Skalan anpassas till plåtens
   startläge, så att den smala början inte bryter ord.

## Gör
- Kör `Skill(design)` först.
- Skriv planen `{{UT_MAPP}}/plans/053-astra-r5.md`.
- Använd kirurgiska `Edit`.
- Inget djärvt drag får backas.
- Verifiera varje fix mot sitt mål med skript och med bild:
  - hjulsekvenser genom processaktens slut vid 1440, i 40 px-steg,
  - steg 06 och 07 vid 390 och 768,
  - jättesektionen vid 768, 1024, 1280, 1440 och 1920.
  Lägg bilderna i `{{UT_MAPP}}/shots/r6/` och läs dem.
- Kör en kort grind: noll horisontell scroll 320–1920, `a11y_scan` vid 390 och 1440,
  rubrikskriptet (noll delade ord), låst copy 15/15, samt grep för tankstreck och
  `prefers-reduced-motion`. Kör `motion_probe` för `#process` vid 1440, eftersom utgången
  ändras.

Leverans: `NOTES.md` § V3d R6. Sista raden ska vara `V3d R6 klar` eller `[PAUSED — steg X]`.
