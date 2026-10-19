# Alunix, V3d runda 17: Exempelcase, Calyx → Hōrai, prissektionen och förbudet mot småtext. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Antons beställning 2026-09-19 är planerad i `{{UT_MAPP}}/plans/060-case-pris-smatext.md`,
punkt 1–8. All copy har gått igenom copy-kedjan, med humanizer-svenska sist, och ligger i
`{{UT_MAPP}}/COPY-V3d-r17-final.md`. Skriv in den ordagrant, med följande delar:
- introt till Exempelcase,
- sektionen "Pristext, Antons andra beställning", alternativ A, under "Alla har rätt till bra
  design.",
- tabellen "Antons beslut 2026-09-19, efter copy-gaten": första meningen i casens steg 1
  stryks, "Vi byggde Calyx som ett tidskriftsnummer, …", och processens ingress tas bort,
- alla rader som är markerade som borttagna.

Ändra ingen sträng. Om en sträng inte ryms, stoppa och skriv en rad i NOTES.

## Beslut som gäller
- **Typsnitt:** Young Serif via Google Fonts `<link>` och token `--f-serif`, enligt planen.
  Case-namnens behandling från R16 rörs inte.
- **Småtext (F-016, gate 99):** ta bort alla 12 element i planens inventering och de sju
  marginalnoterna i processen. Kortbaksidan, topraden, prisradernas paketbeskrivningar,
  ritningens måttetiketter och allt inne i ramarna står kvar.
- **`sites/horai.html`:** Anton har hävt låset **för bokningssektionen**. Minska
  textstorlekarna där och lägg till planens gap-klass på sektionens egen grid. Ingenting
  annat i sajten ändras, och sajten ska se likadan ut i övrigt när den öppnas direkt. Övriga
  delar av `sites/*` rörs aldrig.
- F-011 och F-014 gäller. Motorn rörs aldrig. Exakt två iframes. Ramarna transformeras
  aldrig. Antalet inline-hex får inte öka.

## Gör
- Kör `Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` först.
- Bygg planens Steps i ordning.
- Använd kirurgiska `Edit`.

## Verifiera, innan du kallar något klart
Starta Chromium med `ignore_default_args=['--hide-scrollbars']`. Döm överlapp bara i
enskilda skärmbilder, aldrig i ihopklistrade kontaktark.
1. Mät varje Target i plan 060 med skript och med bild, med `mouse.wheel`, vid 1920x930,
   1440, 1024, 768, 390 och 375.
2. **Ramarnas kanter:** kör magentatestet ur planen med 0 fel pixlar vid 320–1920 och vid
   zoom 90–200 %.
3. **Prissektionen:** rubriken, texten, alla tre prisraderna och kontakten ska rymmas på en
   skärm vid 1920x930 och 1440x900.
4. **Scrolleffekterna Calyx → Hōrai och in i priset:** hjulsekvens i 20 px-steg åt båda
   hållen, med `motion_probe` och kontrollen först.
5. `python "C:/Users/Anton L/anti-slop-design/skills/design/scripts/microtext_scan.py"` mot
   sidan. Bara kortbaksidans fyra rader får flaggas.
6. Par-bilder för PARITET P14–P23 vid 1920, 1440 och 390, i `{{UT_MAPP}}/shots/r17/`. Läs dem.
7. Grinden:
   - `contrast_over_media --url`,
   - `a11y_scan` och `reflow` vid 390 och 768,
   - `perf_probe`, för att mäta den nya typsnittsbegäran,
   - noll horisontell scroll 320–1920,
   - rubrikskriptet, som ska ge noll delade ord,
   - låst copy enligt PRODUCT.md med Antons hävningar,
   - grep för tankstreck, `prefers-reduced-motion` och inline-hex.

Leverans: `NOTES.md` § V3d R17 med en tabell över Target, mål, uppmätt och bild. Sista raden
ska vara `V3d R17 klar` eller `[PAUSED — steg X]`.
