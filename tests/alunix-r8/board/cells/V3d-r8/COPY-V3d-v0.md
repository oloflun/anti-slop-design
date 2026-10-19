# COPY · V3d v0 (plan 054)

Arkitekten, 2026-09-19. Utkast v0 till copy-agenten. Varje synlig sträng på sidan efter plan
054, i sidans ordning. Kedjan (copywriting → copy-editing → humanizer-svenska) körs av
copy-agenten efter bygget och rör bara rader med status **förenklad** eller **ny**.

**Status:** **låst** = `PRODUCT.md` § Brand Commitments, rörs aldrig · **oförändrad** = står
som i dag · **förenklad** = samma sak, kortare och tydligare · **ny** = finns inte i dag ·
**flyttad** = låst eller oförändrad text på ny plats · **borttagen** = försvinner med sin sektion.

**Regler för v0:** vi-form, "ni/er" till läsaren, korta satser, inga tankstreck (U+2010 till
U+2015, U+2212; bindestrecket i "e-post" är U+002D), inga tal utöver arkets mått (320, 768,
1440, 16:9, 96 px, 7 rem), stegnumren 01 till 07 och de låsta priserna. Casetexterna är dikt
om vår egen arbetsprocess, uttryckligen för tänkta verksamheter: inga kunder, citat, siffror
eller resultat. Varje casesteg ≤ 40 ord, varje processtycke ≤ 50 ord.

## Dokument och topprad

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| `<title>` | Alunix · webbyrå i Sverige | Alunix · webbyrå i Sverige | oförändrad | |
| meta description | Alunix är en webbyrå i Sverige. Vi skapar skräddarsydda webbplatser. | (samma) | oförändrad | |
| `.topline-mark` | ALUNIX | ALUNIX | oförändrad | |
| `.topline-contact` | kontakt@alunix.se | kontakt@alunix.se | låst | |

## Hero

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| `h1.hero-headline` | Er hemsida är nutidens visitkort | Er hemsida är nutidens visitkort | låst | |
| `#heroPoolImg` alt | En ljuspöl faller diagonalt över ett mörkt scentyg | (samma) | oförändrad | |
| `.card-mark` | Alunix | Alunix | oförändrad | |
| `.card-kicker` | Digital byrå | Digital byrå | oförändrad | |
| `.card-services` | Design · Utveckling · System | Design · Utveckling · System | låst | Enda kvarvarande platsen för tjänsternas namn efter jättesektionen (plan 054 steg 4) |
| `.card-cta` | Boka ett möte | Boka ett möte | oförändrad | |
| `.sr-only` | Alunix. Digital byrå. Design, utveckling, system. Boka ett möte: kontakt@alunix.se. | (samma) | oförändrad | Måste vara lika kortbaksidan (a11y fix 7) |
| `.hero-sub` | Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten. | (samma) | låst | |

## Tesbandet (en mening i taget, alla i samma storlek)

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| `.ts` 1 (`h2`) | Det första intrycket är digitalt. | Det första intrycket är digitalt. | oförändrad | Tesrubriken i dag |
| `.ts` 2 | Skärmen möter besökaren före texten. *(första meningen i `.thesis-support`)* | Skärmen möter besökaren före texten. | oförändrad, flyttad | Egen mening i rubrikplatsen, Antons beställning |
| `.ts` 3 | Innan ett ord är läst bär layout och bild hela argumentet. *(andra meningen i `.thesis-support`)* | Innan ett ord är läst bär layout och bild hela argumentet. | oförändrad, flyttad | Samma |
| `.ts` 4 | (finns inte) | Vi hjälper er att synas på rätt sätt. | ny | Antons mening, ordagrant ur beställningen |
| `.ts` 5 | VI BYGGER ERT VARUMÄRKE. *(i `#giant-section`)* | VI BYGGER ERT VARUMÄRKE. | låst, flyttad | PRODUCT.md kallar den "Tesrubriken"; jättesektionen tas bort (Q1) |
| `.thesis-caption` | Exempelsida: Hyperborea, konferens i Lund | (samma) | låst | |
| Hyperborea `alt` | Startsidan för Hyperborea, en konferens i Lund, i svartvitt | Startsidan för Hyperborea, en konferens i Lund | förenklad | Bilden får färg vid mening 3; "i svartvitt" blir osant |

## Processakten

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| kicker | Så går det till | Så går det till | oförändrad | |
| `h2#process-title` | Från samtal till lanserad sida. | Från samtal till lanserad sida. | oförändrad | |
| `.process-locked` | Webbdesign, design och system. Allt på ett ställe. *(i `#giant-section`)* | Webbdesign, design och system. Allt på ett ställe. | låst, flyttad | Jättesektionen tas bort; raden inleder hur allt görs från ett ställe |
| `.process-lead` | Sju steg, samma ordning i varje projekt, så att ni alltid vet var vi är. | Samma sju steg i varje projekt. Ni vet alltid var vi är. | förenklad | Två korta satser i stället för en med bisats |
| 01 titel | Uppstart | Uppstart | oförändrad | |
| 01 stycke | Vi börjar med ett samtal om er verksamhet: vad ni gör, vilka ni vill nå och vad sidan ska göra för er. Ni behöver inte ha texter eller bilder klara, det räcker att ni kan berätta. Efter samtalet skriver vi ner vad vi hört och vad vi föreslår, så att ni kan läsa och rätta innan något ritas. Det ni får är grunden för allt som följer. | Vi börjar med ett samtal om er verksamhet: vad ni gör, vilka ni vill nå och vad sidan ska göra. Ni behöver inte ha texter eller bilder klara. Efter samtalet skriver vi ner vad vi hört och vad vi föreslår. Ni läser och rättar innan något ritas. | förenklad | 67 → 47 ord. Samma löften (P6); "det räcker att ni kan berätta" och sista meningen upprepade det som redan sagts |
| 01 not | Ett tomt ark. Inget ritas innan vi vet vad sidan ska säga. | (samma) | oförändrad | Redan kort och konkret |
| 02 titel | Planering | Planering | oförändrad | |
| 02 stycke | Vi ritar strukturen innan vi formger sidan: vilka sidor som finns, vad varje sida ska få besökaren att göra och i vilken ordning innehållet kommer. Vi planerar för tre skärmbredder från början, telefon, surfplatta och dator. Mobilen lägger vi inte till sist. Ni ser strukturen som en enkel skiss och godkänner den innan vi går vidare till design. | Vi bestämmer strukturen innan vi formger något: vilka sidor som finns, vad varje sida ska få besökaren att göra och i vilken ordning. Vi planerar för telefon, surfplatta och dator från början. Ni godkänner skissen innan vi går vidare. | förenklad | 62 → 41 ord. "tre skärmbredder" stryks (noten säger det); P7 kvar |
| 02 not | 320, 768 och 1440. Varje sida verifieras vid alla tre. | 320, 768 och 1440. Vi kontrollerar varje sida i alla tre. | förenklad | Aktiv form, vardagsord i stället för "verifieras" |
| 03 titel | Design | Design | låst | Samma ord som tjänsten |
| 03 stycke | När strukturen är klar formger vi sidan: typografi, färg, bild och rytm hämtar vi ur er verksamhet, inte ur en mall. Förslaget lägger vi på en testadress. Ni öppnar den i er egen webbläsare, på er telefon, och ser sidan som era kunder kommer att se den. Ni lämnar synpunkter, vi justerar och ni godkänner innan vi bygger. Inget går i produktion som ni inte sett. | Nu formger vi sidan. Typografi, färg och bild hämtar vi ur er verksamhet, inte ur en mall. Förslaget lägger vi på en testadress som ni öppnar på er egen telefon och dator. Ni säger vad ni tycker, vi justerar och ni godkänner innan vi bygger. | förenklad | 69 → 47 ord. "Inget går i produktion som ni inte sett" upprepade godkännandet; "rytm" är fackord |
| 03 not | 16:9, öppningen där ert innehåll ska sitta. Proportionen bestäms innan bilden finns. | 16:9 är rutan där ert innehåll ska sitta. Formatet bestäms innan bilden finns. | förenklad | En sats med verb; "öppningen" och "proportionen" är ritspråk |
| 04 titel | Utveckling | Utveckling | låst | |
| 04 stycke | Vi bygger sidan i kod från grunden, för de tre bredderna från planeringen. Sidan ska ladda snabbt och fungera med tangentbord och skärmläsare. Texter och bilder ändrar ni själva i ett innehållssystem. Vi visar hur. Sidan är ert att bygga vidare på. Behöver ni bokningar, betalning eller kunddatabas bygger vi det i samma steg, på samma tekniska nivå som resten av sidan. | Vi bygger sidan i kod från grunden. Den ska ladda snabbt och fungera med tangentbord och skärmläsare. Texter och bilder ändrar ni själva i ett innehållssystem, och vi visar hur. Behöver ni bokning, betalning eller kunddatabas bygger vi det i samma steg. | förenklad | 65 → 44 ord. "Sidan är ert att bygga vidare på" (P2:s antagande) stryks: kongruensfel och otydligt löfte; copy-agenten får återinföra det i rätt form om lead vill |
| 04 not | 96 px, radavståndet i liggaren. All rytm räknas ur det. | 96 px mellan raderna. Resten av rytmen räknas ur det. | förenklad | "liggaren" fanns i jättesektionen, som tas bort; raden pekade på något besökaren inte längre ser |
| 05 titel | Innehåll | Innehåll | oförändrad | |
| 05 stycke | Ni kan er verksamhet, vi kan sätta den på plats. Ni levererar texter och bilder i den takt ni har dem. Texten bearbetar vi så att den blir kort och läsbar, bilderna beskär och optimerar vi för webben. Saknas något säger vi till i tid. Vi fyller sidan på testadressen så att ni ser hur den växer. | Ni kan er verksamhet, och vi sätter den på plats. Ni skickar texter och bilder när ni har dem. Vi kortar texten och anpassar bilderna för webben. Saknas något säger vi till i tid. På testadressen ser ni sidan fyllas. | förenklad | 57 → 42 ord. Samma innehåll (P4) |
| 05 not | Strukturen får sitt material. Ritningen blir er sida. | Ritningen får sitt innehåll och blir er sida. | förenklad | En mening |
| 06 titel | Lansering | Lansering | oförändrad | |
| 06 stycke | Innan sidan går live granskar vi den tillsammans på testadressen: varje länk, varje formulär, varje koppling till bokning, betalning och kunddatabas, på telefon och på dator. Vi testar med tangentbord och skärmläsare, i tre bredder och i riktiga webbläsare. Vi flyttar sedan sidan till er adress och kontrollerar att allt fungerar på plats. Ni får en genomgång av sidan och av hur ni ändrar innehåll själva. | Innan sidan går live går vi igenom den tillsammans: varje länk, varje formulär och varje koppling, på telefon och dator. Vi testar med tangentbord och skärmläsare. Sedan flyttar vi sidan till er adress och kontrollerar den där. Ni får en genomgång av hur ni ändrar innehållet själva. | förenklad | 70 → 49 ord. P10 kvar; "i tre bredder" står redan i 02 |
| 06 not | Bläcket står kvar som ram. Ritningen och sidan är samma sak. | Ritningen finns kvar som ram runt den färdiga sidan. | förenklad | Säger vad bilden visar; leder in i case-kapitlet |
| 07 titel | Förvaltning | Förvaltning | oförändrad | |
| 07 stycke | Vi finns kvar efter lansering. En sida är aldrig färdig: ändringar, nya sidor och nya funktioner går samma väg som bygget, testadress först, godkännande, sedan live. Har ni en fråga mejlar ni oss på kontakt@alunix.se. | Vi finns kvar efter lansering. Ändringar, nya sidor och nya funktioner går samma väg som bygget: testadress, ert godkännande, sedan live. Har ni en fråga mejlar ni oss på kontakt@alunix.se. | förenklad | Kolonet flyttat till där listan börjar; P3 oförändrad |
| 07 not | Revisionsfältet fylls. En bokstav, aldrig ett datum. | Varje ändring får en ny bokstav i ritningens hörn. | förenklad | "Revisionsfältet" är ritterm; säger nu vad besökaren ser |
| SVG `title` | Sektionsritning av processen | Ritning av processen | förenklad | Skärmläsartext; "sektionsritning" är fackord |
| SVG `desc` | En måttsatt ritning som visar sidans byggprocess i sju steg och ritar sig själv när sidan scrollas. | En ritning av sidan som växer för varje steg och till sist blir en färdig sida. | förenklad | Beskriver vad som händer, inte hur |
| SVG-texter | 320 · 768 · 1440 · 7 rem · 16:9 · 96 px · A | (samma) | oförändrad | Mått i ritningen |
| `.ledger-num` 01 till 07 | 01 … 07 | (samma) | oförändrad | `aria-hidden`, numrering |

## Case-kapitlet (ersätter "Hur vi tänker")

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| kicker | Hur vi tänker | Exempelcase | ny | Plan 054 § 4: "Kundcase" påstår en kund som inte finns |
| `h2.cases-title` | (finns inte) | Så blev ritningen en sida. | ny | Knyter processaktens ritning till sajterna som följer |
| `.cases-lead` | (finns inte) | Calyx och Hōrai är exempelsidor vi har byggt. Här berättar vi hur vi tänkte, från första skiss till färdig sida. | ny | Säger rakt ut att det är exempel, före första steget |

## Case Calyx (text vänster, sajten skrollar till höger)

Varje steg står ensamt i textplatsen medan sajten visar ankaret inom parentes.

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| kicker | | Exempelcase | ny | Döljs under 768 |
| `h2.case-title` | | Calyx | ny | |
| steg 1 h3 *(sajtens första skärm)* | | Blommorna först | ny | |
| steg 1 p | | Calyx är en exempelsida vi byggt för en tänkt florist i Stockholm. En florist säljer något man vill röra vid. Därför fick fotot hela första skärmen och rubriken står direkt på bilden. | ny | 34 ord. Första meningen gör dikten ärlig (PRODUCT.md § absences) |
| steg 2 h3 *(`#studio`)* | | En lågmäld röst | ny | |
| steg 2 p | | Vi skrev som en ateljé talar: korta stycken och inga utrop. Rubrikerna står i en klassisk serif där kursiven bär betoningen. Brödtexten är lugn och lätt att läsa. | ny | 29 ord. Beslut om typografi |
| steg 3 h3 *(bildparet efter `#studio`)* | | Bilderna i par | ny | |
| steg 3 p | | Fotona står parvis med en liten märkning under varje, som i en katalog. Papperet är varmt och nästan vitt, så att blommorna får stå för färgen. | ny | 28 ord. Beslut om bild och grund |
| steg 4 h3 *(`#index`)* | | Listan ritade vi först | ny | |
| steg 4 p | | Det första vi ritade var veckans utbud. Buketterna står i en lista med namn, beskrivning och pris till höger, inte som kort i ett rutnät. Den enda egna färgen är en rostton, och den används sparsamt. | ny | 38 ord. (Rosttonen står på ett namn i listan och på anfangerna längre ned; "sparsamt" är sant för båda.) Vad som ritades först, struktur, färg |
| steg 5 h3 *(`#commission`)* | | Ett sätt att höra av sig | ny | |
| steg 5 p | | Sidan slutar på mörk grund med en rubrik och en e-postadress. Inget formulär, ingen kalender. En ateljé ska gå att nå på det sätt den faktiskt tar emot beställningar. | ny | 32 ord |
| `.case-rail` | | Blommorna först · En lågmäld röst · Bilderna i par · Listan ritade vi först · Ett sätt att höra av sig | ny | Samma som h3, `aria-hidden`; döljs under 768 |
| iframe `title` | Exempelsida: Calyx, florist i Stockholm | (samma) | låst, flyttad | |
| `figcaption` | Exempelsida: Calyx, florist i Stockholm | (samma) | låst, flyttad | |

## Bryggan

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| `h2.bridge-title` | | Samma arbetssätt. En annan verksamhet. | ny | |
| `.bridge-p` | | En florist och en restaurang behöver olika sidor. Frågorna vi ställer är desamma: vad ska synas först, och vad ska besökaren göra sedan? | ny | 23 ord. Leder från ljust till mörkt utan att påstå något om resultat |

## Case Hōrai (sajten skrollar till vänster, text höger)

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| kicker | | Exempelcase | ny | |
| `h2.case-title` | | Hōrai | ny | |
| steg 1 h3 *(sajtens första skärm)* | | Kvällen först | ny | |
| steg 1 p | | Hōrai är en exempelsida vi byggt för en tänkt restaurang. En plats som serverar på kvällen ska kännas som kvällen. Vi valde en mörk, varm grund och lät namnet stå stort i versaler. | ny | 35 ord. Ärlig inramning, beslut om färg och typ |
| steg 2 h3 *(huset, ordljuset)* | | Texten tänds när ni läser | ny | |
| steg 2 p | | Stycket om huset lyser upp ord för ord medan ni scrollar. Det ska kännas som att någon berättar. Varje avsnitt har ett tecken i rött bredvid rubriken, som en stämpel. | ny | 32 ord. Beskriver det som faktiskt spelar i ramen just då |
| steg 3 h3 *(citatet, format läge)* | | En paus | ny | |
| steg 3 p | | Mellan huset och menyerna står en enda mening på mörk grund. Den blir skarp när ni scrollar fram till den. Vi lade in den så att sidan andas innan det blir praktiskt. | ny | 35 ord. Beslut om struktur |
| steg 4 h3 *(menyerna)* | | Menyerna som tavlor | ny | |
| steg 4 p | | Varje meny har en romersk siffra, ett namn och ett pris i stort rött. Rubrikerna står i klassiska versaler, brödtexten i en serif som är lätt att läsa. Menyn går att läsa på avstånd. | ny | 36 ord. Inga priser återges (sajtens priser är dess egna, inte Alunix) |
| steg 5 h3 *(rummet)* | | Rummet | ny | |
| steg 5 p | | Innan bokningen kommer rummet: en bild av matsalen över hela bredden, med texten direkt på bilden. Man vill se var man ska sitta innan man bokar. | ny | 28 ord. Beslut om bild |
| steg 6 h3 *(`#reservations`)* | | Bokningen sist | ny | |
| steg 6 p | | Sidan slutar med hur man bokar, i klartext: när platserna släpps och vart man skriver. En restaurang lever på bokningar. Det sista på sidan ska vara det besökaren kom för. | ny | 32 ord |
| `.case-rail` | | Kvällen först · Texten tänds när ni läser · En paus · Menyerna som tavlor · Rummet · Bokningen sist | ny | Samma som h3, `aria-hidden` |
| iframe `title` | Exempelsida: Hōrai, Asian fusion-koncept | (samma) | låst, flyttad | |
| `figcaption` | Exempelsida: Hōrai, Asian fusion-koncept | (samma) | låst, flyttad | |

## Priset och avslutet

| Plats | Nuvarande | v0 | Status | Skäl |
|---|---|---|---|---|
| `h2.statement` | Alla har rätt till bra design. | (samma) | låst | |
| `.price-ingress` | Två av tre paket har ett pris utskrivet här. Det tredje beror på omfattningen. | Två paket har priset utskrivet. Det tredje beror på vad ni behöver. | förenklad | "vad ni behöver" i stället för "omfattningen"; tilltal till läsaren |
| rad 1 | Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering. | (samma) | låst | |
| värde 1 | 26 900 kr | (samma) | låst | |
| rad 2 | Paket med bokningssystem, betalning och kunddatabas. | (samma) | låst | |
| värde 2 | 38 900 kr | (samma) | låst | |
| rad 3 | Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera | (samma) | låst | |
| värde 3 | Pris vid förfrågan | (samma) | låst | |
| `.close-mailto` | kontakt@alunix.se | (samma) | låst | |

## Borttagna med sina sektioner

| Plats | Nuvarande | Status | Skäl |
|---|---|---|---|
| `.giant-sub` | Webbdesign, design och system. Allt på ett ställe. | flyttad (se processakten) | Låst |
| `h2.giant` | VI BYGGER ERT VARUMÄRKE. | flyttad (tesens mening 5) | Låst |
| liggaren 01 Design | Identitet och formspråk hämtade ur er verksamhet. Ni ser förslaget på en testadress och godkänner innan vi bygger. | borttagen | Innehållet står i processteg 03 |
| liggaren 02 Utveckling | Byggt i kod från grunden för telefon, surfplatta och dator. Snabbt, tillgängligt och ert att bygga vidare på. | borttagen | Innehållet står i processteg 04 |
| liggaren 03 System | Bokningar, betalning och kunddatabas byggda i samma steg som sidan och skötta efter lansering. | borttagen | Innehållet står i processteg 04 och prisrad 2 (Q2) |
| "Hur vi tänker" (kicker + tre principer) | Vi visar innan vi påstår · Sidan ska fungera för alla · Ni ska kunna ändra själva, med stycken | borttagen | Ersatt av casen (Antons punkt 4, Q5) |

## Kontroll för copy-agenten

- Låsta rader: 16 st, alla finns ovan med status låst; diffa byte för byte före och efter.
- Nya tal: inga. Talmängden efter v0: `01` till `07`, `320`, `768`, `1440`, `16:9`, `96`, `7 rem`,
  `26 900`, `38 900`.
- Upprepningar som är avsiktliga: "Exempelcase" tre gånger (kapitel, två case), rubrikerna
  i `.case-rail` (aria-hidden).
- "Exempelsida vi byggt för en tänkt …" två gånger (Calyx steg 1, Hōrai steg 1): avsiktlig
  parallell, säger samma ärliga sak om båda.
