# Alunix, V3d runda 18: processtegen i större text och övergången "Blåkopian". Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Antons beställning 2026-09-19 är planerad i `{{UT_MAPP}}/plans/061-overgang-och-steg.md`.
Stegtexterna har gått igenom copy-kedjan, med humanizer-svenska sist, och ligger i
`{{UT_MAPP}}/COPY-V3d-r18-steg.md`. Skriv in kolumnen `final` ordagrant, med ett undantag:
**steg 05** får lead-versionen "Ni behöver inte ha något färdigt. Vi bearbetar texter och
bilder ni har och säger till om något saknas." tills Anton har bekräftat att Alunix skriver
och fotograferar åt kunden.

## Gör
- Kör `Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` först.
- Grep:a planens selektorer mot R17-läget innan du ändrar något. `.process-note` ska ge 0
  träffar.
- Bygg planens Steps i ordning: stegtypografin först, sedan övergången. Planens antaganden
  gäller (Q1 att linjerna står kvar, Q2 att texten är 62 % bläck i början, Q3 att titeln har
  samma storlek som texten).
- Planens stoppvillkor gäller: den kapslade akten och z-index-lyftet. Stoppa och rapportera
  om de slår till.
- Använd kirurgiska `Edit`. F-011 och F-014 gäller. Motorn och `sites/*` rörs aldrig. Antalet
  inline-hex får inte öka. Inget djärvt drag får backas.

## Verifiera
Starta Chromium med `ignore_default_args=['--hide-scrollbars']`. Döm bara i enskilda
skärmbilder, aldrig i ihopklistrade kontaktark.
1. Mät alla Targets i 061.
2. Hjulsekvens i 20 px-steg åt båda hållen genom övergången och genom hela processakten vid
   1920x930, 1440, 768 och 390. Kontrollera noll halvklippta rubriker, med båda
   kontrollerna ur planen och båda först körda mot en medvetet trasig version. Kontrollera
   också noll glyfspringor mellan banden.
3. `motion_probe` för processakten och övergången, med kontrollen först, åt båda hållen.
4. Pixeldiffa hero, tesbandet, casen och priset mot R17-läget. Ingen oavsiktlig ändring får
   finnas.
5. Kör `microtext_scan.py`, och bara kortbaksidan får flaggas. Kör rubrikskriptet, som ska ge
   noll delade ord. Kontrollera noll horisontell scroll 320–1920 och kör `a11y_scan` vid 390
   och 1440.
6. Lägg par-bilder för P04 och P07–P13 vid 1920, 1440 och 390 i `{{UT_MAPP}}/shots/r18/` och
   läs dem.

Leverans: `NOTES.md` § V3d R18 med en tabell över Target, mål, uppmätt värde och bild. Sista
raden ska vara `V3d R18 klar` eller `[PAUSED — steg X]`.

## Tillägg från lead: R17:s rest
Magentaprovet vid 1280x620 och 150 % (Calyx underkant) gav 30 av 120 fel punkter. Använd
plan 060:s egen reserv: JS som snäpper `.case-wrap` till hela enhetspixlar i `measureCase`.
Målet är 0 fel i alla 15 konfigurationer, och de 14 som redan är rena ska förbli rena.
