# Alunix, V3d runda 23: vänstertexten, övergångarna, case-kapitlet, priset och kontakten. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Antons beställning 2026-09-20, nio punkter, är planerad i sin helhet i
`{{UT_MAPP}}/plans/067-vanstertext-case-pris-kontakt.md`. **Planen är kontraktet.** Den har
åtta Steps i byggordning, ett Target med mätbara mål per bredd för varje Step, en
device-tabell, en boundaries-lista och en verifieringslista. Följ den. Hitta inte på egna
tal — arkitekten har mätt dem, och Astra har rättat flera av dem.

## Läs först, i den ordningen
1. `Skill(design)`, `Skill(animate)`, `Skill(emil-design-eng)`.
2. `{{UT_MAPP}}/plans/067-vanstertext-case-pris-kontakt.md`, hela.
3. `{{UT_MAPP}}/reviews/r23-astra-estetik.md` — den estetiska domen bakom steg 7, steg 4
   och steg 3. Läs `fidelity` och `ceiling` särskilt.
4. `{{UT_MAPP}}/COPY-V3d-r23.md` — **all synlig text skrivs in ordagrant ur kolumnen
   `final`.** Du ändrar aldrig en sträng. Saknas filen, stoppa.
5. `{{UT_MAPP}}/PARITET-067.md` — de omskrivna och nya raderna. De äldre raderna i
   `PARITET.md` är ersatta för P01, P04, P07–P13, P14, P15, P16, P17, P19 och P21.
6. `{{UT_MAPP}}/reviews/r21-astra.md` § keep — får inte regressera.

## Beslut som redan är fattade och inte omprövas
- **Q1–Q6 är besvarade** i planens frågetabell. Bygg efter svaren.
- Arket blir 68,8 % vw vid 1920 och 67,8 % vid 1440. 1440-talet är en regression mot dagens
  81,1 % och den är **accepterad** — tvåspaltsakten är kundens uttryckliga order och resten
  är aritmetik. Optimera inte bort tvåspalten för att rädda talet.
- **Young Serif tas bort helt.** Inga Google Fonts-anrop, inga preconnect, tre typsnittsfiler.
- **Prisrubriken sätts i Geist 700.** Public Sans finns i en vikt (300); en fet Public Sans
  blir syntetisk, alltså en renderingsdefekt. Sätt aldrig `font-weight` ≥ 600 på Public Sans.
- **Case-ingressen är alternativ A**, ordagrant. Utfall B i planens 4.3 utgår.
- Låst copy räknar **11 synliga rader** i V3d. `PRODUCT.md` är redan uppdaterad av lead, både
  för `.hero-sub` och för formulärlåset. Du rör inte `PRODUCT.md`.

## Arbetssätt
- Kirurgiska `Edit`, aldrig `Write` av hela `index.html`.
- Bygg **i planens stegordning**. Steg 5 och 7 kräver steg 2 och 4 först — deras
  geometri läses ur arkets och kapitlets nya rektanglar.
- **Ett djärvt drag backas aldrig för att laga ett följdfel.** Följdfelet lagas i samma runda.
- Motorn `scroll/*.js` och `scrollcraft.css` rörs aldrig. `sites/*` rörs aldrig. Exakt två
  levande iframes. Ramarna transformeras aldrig. F-011 och F-014 gäller.
- Gate 48: inga inline-hex tillkommer, och steg 6 ska sänka antalet med två.
- **F-016 / gate 99:** inga bildtexter, inga hjälptexter under formulärfält, inga
  dekorativa etiketter, ingen text som beskriver sidan. Nytt sedan förra rundan: **F-018**,
  ingen text på sidan får referera till sidan eller till vad som kommer härnäst.
- Varje nytt CSS- eller markupblock börjar med `PLAN 067 N.` och en INTE-rad.

## Boundaries
Planens boundaries-lista gäller ordagrant. Träffar du en av dem: **stoppa vid det steget**,
skriv raden i `NOTES.md`, och fortsätt med de steg som inte beror på det. Bygg aldrig vidare
förbi en boundary på gissning.

## Verifiera
Planens § Verification, A, B och C, i sin helhet. Det som avgör:
- **Enskilda skärmbilder, aldrig kontaktark som bevis.** Chromium med
  `ignore_default_args=['--hide-scrollbars']`, målläget nått med `mouse.wheel`, en skärmbild
  per sida. Läs dem själv.
- Astras egna skript i `{{UT_MAPP}}/shots/astra-r23/` (`sweep23.py`, `ink23.py`,
  `anchors23.py`) och `shots/astra-r21/plane21.py` **återanvänds oförändrade** som
  regressionsvakt. Skriv inte om dem.
- Varje geometrisk kontroll körs **först mot en medvetet trasig variant**, så att du vet att
  den hittar felet. En kontroll som ger noll mot både trasigt och helt mäter ingenting — det
  har hänt två gånger i det här projektet.
- Par-bilder till `{{UT_MAPP}}/shots/r23/par/`.

Leverans: `NOTES.md` § V3d R23 med en tabell per Step: mätvärde, mål, före, efter, bild.
Sista raden ska vara `V3d R23 klar` eller `[PAUSED — steg X]`.
