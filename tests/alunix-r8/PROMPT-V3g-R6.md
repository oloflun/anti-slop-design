Du är byggaren för Alunix {{KONCEPT}}, runda 6. Arbetsmapp `{{UT_MAPP}}`, server-port {{PORT}}.
Designkedjan är påslagen. Bara headless, en webbläsare i taget, stäng alltid. Ingen commit.

## Läs först
1. `{{UT_MAPP}}/EFFECTS.md`: skyddade effekter. Inget där får ändras eller bli sämre.
2. `design-catalogue/FEEDBACK.md` F-019 (rättad) och **F-022** (nytt): Antons dom över rutan.
3. `{{UT_MAPP}}/RAPPORT.md` R3–R5 och `{{UT_MAPP}}/SHOWCASE-SPEC.md`: mekanismen du bygger vidare på.
4. `Skill(design)` med referensgolvet. Läs också `runs/V3f/dither.py` och hur sidans egen
   dither→färg-övergång i `#kontakt` är byggd (sök `dither` i `index.html`). Det är husgreppet
   du ska använda.

## Uppdraget: showcasens textruta på desktop. Inget annat ändras
Antons ord: "Hur godkändes de gröna strecken? Det ser ut som något ofärdigt … Det räcker med att
flytta upp stycket istället, men hela utseendet på det ser fortfarande för platt ut, lös det."

Rutan (`.showcase-rows` under `.showcase-head`) blir tre celler i sidans cellnät, med 1 px svart
fog mellan cellerna, som i resten av rutverket:

1. **Räknarcellen** överst: `03 / 06` och mintspåret, oförändrade.
2. **Textcellen** direkt under: det aktiva steget, samma `h3` (30 px) och `p` (18 px,
   `max-width:40ch`), med samma övertoning och samma tidslinje som nu.
   - Cellens höjd sätts av det längsta steget, så att fogen inte hoppar mellan stegen. Mät
     alla steg och sätt höjden en gång.
3. **Detaljcellen** fyller resten av höjden: **en närbild ur kundsajten som visar det steget
   handlar om**. Det är ett riktigt utsnitt, inte samma vy som iframen visar bredvid.
   - Förslag per steg, välj det tydligaste utsnittet i sajten och motivera kort i rapporten:
     - Calyx: 1 rubriken på fotot · 2 serifen i brödtexten · 3 fotoparet med märkningarna ·
       4 prislistan med löpnummer och pris · 5 e-postadressen/beställningsraden.
     - Hōrai: 1 namnet i versaler på det mörka fotot · 2 stycket med röd rubrik och
       stämpeltecknet · 3 den enda meningen på mörk grund · 4 menyn med romersk siffra och
       rött pris · 5 matsalsbilden med texten · 6 bokningsraden.
   - Bilderna: Playwright headless, `sites/calyx.html` och `sites/horai.html` i 1440 × 900 med
     `deviceScaleFactor: 2`.
     - Skrolla till ankaret och ta en elementskärmbild eller ett utsnitt runt elementet.
     - Beskär till cellens proportion, och välj beskärningen så att det steget beskriver syns
       tydligt och skarpt.
     - Spara färgversionen som WebP (cirka 82) i `{{UT_MAPP}}/assets/steps/`.
     - Gör en dither-version med `dither.py`-metoden (samma kornstorlek och samma två
       bläckvarianter: svart på grått till Calyx, vitt på svart till Hōrai).
   - Rörelsen, per steg och i samma skrubbade tidslinje:
     - bilden tonas in rastrerad när steget byts;
     - sedan löses den upp till färg under stegets vilofönster, som i `#kontakt`;
     - vid nästa stegbyte tonas den ut med texten.
     - Bara `opacity` och `transform` animeras. Inga filter.
   - Bilderna är `aria-hidden` med tom `alt`. Ingen ny synlig copy.
- **Ta bort** stegskalan helt: linjen, strecken, markören, CSS:en och JS:en. Ingenting får
  ersätta den med ett annat ornament.
- Calyx-rutan på `--paper` och Hōrai-rutan på `--black`, som nu. Detaljcellens bakgrund följer
  dither-varianten.
- Mobil: oförändrad.

## Kontroll (du först, sedan leaden)
- Skärmbilder 1440 × 900 av rutan vid varje steg för båda casen, alltså 11 bilder: ett
  ögonblick i vilofönstret där bilden är i färg, och ett vid ett stegbyte. Läs dem.
  - Frågan för varje bild: ser rutan färdig ut, och visar detaljen det texten säger?
- `click_scroll_probe.py` två gånger. Största steg ≤ 90 px, inget sämre än R5.
- `section_probe.py --baseline {{UT_MAPP}}/shots/section-probe-baseline.json` två gånger. Grönt,
  1 laddning per iframe, 0 refreshar, ingen sektion sämre.
- Kontrollera stegen både med hopp och med bakåtscroll, enligt regeln om timeline-längd i
  `devices.md`.
- `verify.py`: 0 px överflöd, och copy-diffen oförändrad utom de uttryckligen tillåtna stegsträngarna (del 2).
- En R6-sektion i `RAPPORT.md` med utsnittsvalen och bildvägarna.

## Del 2: stegtexterna ska hålla sidans nivå
Antons ord: "se till att texterna matchar den övriga sidans nivå". Det gäller showcasens elva steg,
alltså `h3` + `p` för Calyx och Hōrai, på desktop och mobil. Samma strängar finns på båda.
1. Läs först resten av sidans copy som måttstock: hero, tesen, processen, pris och kontakt. Notera
   vad som gör den bra: tempo, konkreta substantiv, verb framför abstrakta ord, längd per mening,
   ingen självreferens (F-018), ingen beskrivande mikrotext (F-016).
2. Kör de tre passen i ordning, som riktiga Skill-anrop och inte ur minnet (husregel 12):
   `Skill(copywriting)` → `Skill(copy-editing)` → `Skill(humanizer-svenska)`.
   - Varje steg ska säga vad vi valde i sajten och varför, konkret, i sidans ton.
   - Fakta får inte ändras: det texten påstår om sajten måste stämma med `sites/calyx.html` och
     `sites/horai.html`. Kontrollera varje påstående mot sajten och rätta det som inte stämmer.
   - Rubrikerna ska vara korta, högst cirka 5 ord, och får inte slå över till två rader i 30 px
     i rutans bredd.
3. Copy-diffen i `verify.py` jämför mot V3d. De ändrade stegsträngarna kommer att flaggas.
   - Lägg dem i en uttrycklig lista över tillåtna nya strängar i `verify.py`, med kommentaren
     "R6: Antons order, showcasens steg".
   - Allt annat ska vara oförändrat.
4. I `RAPPORT.md`: före/efter för varje sträng, och vilket pass som ändrade vad.
