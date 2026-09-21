# Alunix, V3d runda 24. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

**Läs `{{UT_MAPP}}/R24-BRIEF.md` först.** Den bär rundans nio fel med mätvärden och kontroller,
och läget i filen: fel 1, 5 och 9 är redan lagda och ska inte återupprepas. Den här prompten är
bara dispensern.

R23 byggde plan 067 i sin helhet. **Stämpelrutan fungerar och rörs inte.** Tvåspaltsakten,
case-kapitlet, priset och kontaktsektionen är byggda och ska inte backas.

Antons dom över R23: *"Alla punkter från beställningen syns är gjorda … och resten av
ändringarna motsvarade inte riktigt heller mina förväntningar även om de utfördes på papper."*
**Avbockade punkter är inte samma sak som nådd nivå.** Det är målet. Hans feedback ordagrant,
bild för bild: `{{UT_MAPP}}/HANDOFF-2026-09-20.md` § 3.

**Läs i små stycken.** Stora verktygssvar har fällt den här rundan två gånger.

## De nio felen, i korthet. Detaljerna i `R24-BRIEF.md`

1. `--tx` oregistrerad custom property → `NaN` som tyst blir 0. **Lagt.**
2. `.tes-plane`s fyllning är ljusare än accenten från start; ska vara exakt `var(--c-accent)`
   för `tx ≤ 0,75`. Byggt, **overifierat** — kan redan vara löst av fel 1. Mät.
3. 46 av 121 bildrutor under 18 % textyta. Byggt, **overifierat**.
4. `aimFlow` siktar på plan 061:s gamla tx-fönster. Byggt, **overifierat**.
5. Processektionerna: trång spalt, för lång text, siffran i texten, klippt rubrik.
   **Copyn är lagd** — gör spalt, avstånd och rubrik.
6. Övergången till Exempelcase: den mörka rutan över papperet.
7. Case-ingressen är fortfarande slop. **Ej påbörjad.** Skriv inte en tredje variant på samma
   stans — kundens situation eller ingen rad alls.
8. Kontaktsektionen: animationen långsammare, sektionen inverterad till svart, ny led, bild
   under texten, ny mejlrad, `Boka ett möte` → `#kontakt`. **Ej påbörjad.** Fältformen rörs inte.
9. Steg 05 är P4-frågan, nu besvarad. **Lagt.**

## Invarianter

- Motorn `scroll/*.js` och `scrollcraft.css` rörs aldrig. `sites/*` rörs aldrig.
- Exakt två levande iframes. Ramarna transformeras aldrig. F-011 och F-014 gäller.
- **Kontaktformulärets fältform rörs inte.**
- R23:s resultat får inte backas: stämpelrutan, tvåspaltsakten, arkets 1311 px, priset utan
  serif, case-kapitlets storlek och luft.
- Gate 48, gate 99 / F-016, F-018. Inga tankstreck. **Räkna om låst copy efter
  stegomskrivningen och skriv talet i `NOTES.md`** — R23 räknade 11.
- Läs `~/.agents/skills/design/references/chain-discipline.md`. M1–M3, V1–V2 och O2 är inte
  råd i den här rundan, de är orsaken till att den finns.

## Verifiera

- **Alla nio fel** har en kontroll i `R24-BRIEF.md`. Kör var och en **mot nuvarande (trasigt)
  läge först**, så att du ser att den hittar felet. En kontroll som ger grönt mot både trasigt
  och lagat mäter ingenting — det har hänt tre gånger i det här projektet.
- **Rapportera i renderat, inte i bytes.** Att strängen finns i filen eller i svaret över HTTP
  är inte ett bevis. Beviset är en **renderad bild av den sida Anton öppnar**, läst som bild.
- Enskilda skärmbilder, aldrig kontaktark som bevis. Chromium med
  `ignore_default_args=['--hide-scrollbars']`, `mouse.wheel`, en skärmbild per sida.
- Kort grind: 0 horisontell scroll 320–1920, 0 JS-fel, rubrikskriptet, låst copy.
- **Kör därefter hela plan 067 § Verification A/B/C** (`{{UT_MAPP}}/plans/067-*.md`), som R23
  aldrig hann med på grund av full disk. Det är den körningen som avgör om R23 plus R24 kan
  kallas klara.

Leverans: `{{UT_MAPP}}/NOTES.md` § V3d R24 med en tabell per fel: mål, före, efter, bild.
Sista raden ska vara `V3d R24 klar` eller `[PAUSED — fel X]`.
