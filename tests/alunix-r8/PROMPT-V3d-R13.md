# Alunix, V3d runda 13: Hōrais rubrik och prisblocket som en enhet. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Anton läste R12:s copy den 2026-09-19. Behåll "Calyx fick bli ett vårnummer.". Hōrais rubrik
gick att läsa fel. Bron "Ni har sett arbetet. Här är priset." ska bort.

Copy-kedjan är körd, med humanizer-svenska sist, och texten ligger i
`{{UT_MAPP}}/COPY-V3d-pris-final.md`. Skriv in kolumnen `final` ordagrant och ta bort de
strängar som tabellen markerar som borttagna.

## Gör
1. **Hōrais rubrikrad** blir "Hōrai dukar upp kvällen och ber om bokningen sist." Det gäller
   i den tvådelade `h2`:an från R12, med oförändrad form.
2. **Prisblocket blir en enhet.** Ordningen är kicker "Från exempel till er sida", rubriken
   "Alla har rätt till bra design." (låst), den nya texten och den korta raden, och sedan
   prisliggaren med de tre låsta raderna.
   - Bron `#bro` slås ihop med `#pris`, eller tas bort. Välj den lösning som behåller R12:s
     visuella övergång från Hōrais svarta yta till fotogrunden, alltså tonövergången och
     hårlinjen ned till liggaren. Övergången ska nu leda in i rubriken "Alla har rätt till bra
     design.".
   - Ta bort brons "Ni har sett arbetet…", dess stycke, dess mikrorad och den gamla
     prisingressen.
   - Ge rubriken ett id och rätta `aria-labelledby`. Inga referenser får peka på element som
     inte finns.
   - `?preview=pris-bro` ska visa den nya enheten.
3. Rubriken "Alla har rätt till bra design." och texten under den ska läsas som ett
   sammanhang, med texten direkt under rubriken och priserna direkt därefter, inte på varsin
   skärm. Vid 1920, 1440 och 390 ska rubriken, texten och den första prisraden synas
   tillsammans i något scrolläge.

`Skill(design)` först. Använd kirurgiska `Edit`. Rör ingenting annat från R12.

## Verifiera
- Ta enskilda skärmbilder, via `mouse.wheel`, av prisblocket och av övergången från Hōrai
  vid 1920x930, 1440, 768 och 390, och läs dem.
- Kontrollera noll horisontell scroll 320–1920, `a11y_scan` vid 390 och 1440 (inga trasiga
  `aria`-referenser), låst copy 14/14, noll tankstreck och rubrikskriptet.

Leverans: `NOTES.md` § V3d R13. Sista raden ska vara `V3d R13 klar`.
