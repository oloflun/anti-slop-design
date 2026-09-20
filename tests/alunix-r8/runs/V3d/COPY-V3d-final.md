# COPY · V3d final (plan 054)

Copy-agent, 2026-09-19. Byggarens källa: kolumnen **final** skrivs in ordagrant på platsen i
kolumnen **Plats** (oförändrad från `COPY-V3d-v0.md`). Kedjan: pass 0 UX-copy →
`Skill(copywriting)` → `Skill(copy-editing)` → `Skill(humanizer-svenska)` → pass 5 mekaniskt.
Detaljer per pass: `COPY-GATE.md` § V3d R7.

**Pass-koder:** 0 = UX-copy · 2 = copywriting · 3 = copy-editing · 4 = humanizer-svenska ·
5 = mekaniskt · **–** = ingen ändring efter v0 (alla pass lästa, inget fynd).
Låsta rader är diffade byte för byte mot `PRODUCT.md` § Brand Commitments.

## Dokument och topprad

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| `<title>` | Alunix · webbyrå i Sverige | Alunix · webbyrå i Sverige | – | oförändrad |
| meta description | Alunix är en webbyrå i Sverige. Vi skapar skräddarsydda webbplatser. | Alunix är en webbyrå i Sverige. Vi skapar skräddarsydda webbplatser. | – | oförändrad |
| `.topline-mark` | ALUNIX | ALUNIX | – | oförändrad |
| `.topline-contact` | kontakt@alunix.se | kontakt@alunix.se | – | låst |

## Hero

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| `h1.hero-headline` | Er hemsida är nutidens visitkort | Er hemsida är nutidens visitkort | – | låst |
| `#heroPoolImg` alt | En ljuspöl faller diagonalt över ett mörkt scentyg | En ljuspöl faller diagonalt över ett mörkt scentyg | – | oförändrad |
| `.card-mark` | Alunix | Alunix | – | oförändrad |
| `.card-kicker` | Digital byrå | Digital byrå | – | oförändrad |
| `.card-services` | Design · Utveckling · System | Design · Utveckling · System | – | låst |
| `.card-cta` | Boka ett möte | Boka ett möte | – | oförändrad |
| `.sr-only` | Alunix. Digital byrå. Design, utveckling, system. Boka ett möte: kontakt@alunix.se. | Alunix. Digital byrå. Design, utveckling, system. Boka ett möte: kontakt@alunix.se. | – | måste vara lika kortbaksidan (a11y fix 7) |
| `.hero-sub` | Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten. | Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten. | – | låst |

## Tesbandet

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| `.ts` 1 (`h2`) | Det första intrycket är digitalt. | Det första intrycket är digitalt. | – | oförändrad |
| `.ts` 2 | Skärmen möter besökaren före texten. | Skärmen möter besökaren före texten. | – | oförändrad, flyttad |
| `.ts` 3 | Innan ett ord är läst bär layout och bild hela argumentet. | Innan ett ord är läst bär layout och bild hela argumentet. | – | oförändrad, flyttad |
| `.ts` 4 | Vi hjälper er att synas på rätt sätt. | Vi hjälper er att synas på rätt sätt. | – | Antons mening, ordagrant. Bryter inget: vi-form, "er", inget tal, inget nytt löfte utöver `.hero-sub` |
| `.ts` 5 | VI BYGGER ERT VARUMÄRKE. | VI BYGGER ERT VARUMÄRKE. | – | låst |
| `.thesis-caption` | Exempelsida: Hyperborea, konferens i Lund | Exempelsida: Hyperborea, konferens i Lund | – | låst |
| Hyperborea `alt` | Startsidan för Hyperborea, en konferens i Lund | Startsidan för Hyperborea, en konferens i Lund | – | v0:s förenkling står |

## Processakten

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| kicker | Så går det till | Så går det till | – | oförändrad |
| `h2#process-title` | Från samtal till lanserad sida. | Från samtal till lanserad sida. | – | oförändrad |
| `.process-locked` | Webbdesign, design och system. Allt på ett ställe. | Webbdesign, design och system. Allt på ett ställe. | – | låst |
| `.process-lead` | Samma sju steg i varje projekt. Ni vet alltid var vi är. | Samma sju steg i varje projekt. Ni vet alltid var vi är. | – | "alltid" bär trygghetslöftet, behålls som i V3c |
| 01 titel | Uppstart | Uppstart | – | |
| 01 stycke | Vi börjar med ett samtal om er verksamhet: vad ni gör, vilka ni vill nå och vad sidan ska göra. Ni behöver inte ha texter eller bilder klara. Efter samtalet skriver vi ner vad vi hört och vad vi föreslår. Ni läser och rättar innan något ritas. | Vi börjar med ett samtal om er verksamhet: vad ni gör, vilka ni vill nå och vad sidan ska göra. Ni behöver inte ha texter eller bilder klara. Efter samtalet skriver vi ner vad vi hört och vad vi föreslår. Ni läser och rättar innan något ritas. | – | Uppräkningen är en verklig lista, inte en treregel |
| 01 not | Ett tomt ark. Inget ritas innan vi vet vad sidan ska säga. | Ett tomt ark. Inget ritas innan vi vet vad sidan ska säga. | – | |
| 02 titel | Planering | Planering | – | |
| 02 stycke | Vi bestämmer strukturen innan vi formger något: vilka sidor som finns, vad varje sida ska få besökaren att göra och i vilken ordning. Vi planerar för telefon, surfplatta och dator från början. Ni godkänner skissen innan vi går vidare. | Vi bestämmer strukturen innan vi formger något: vilka sidor som finns, vad varje sida ska få besökaren att göra och i vilken ordning. Vi planerar för telefon, surfplatta och dator från början. Ni godkänner skissen innan vi går vidare. | – | |
| 02 not | 320, 768 och 1440. Vi kontrollerar varje sida i alla tre. | 320, 768 och 1440. Vi kontrollerar varje sida i alla tre. | – | |
| 03 titel | Design | Design | – | låst |
| 03 stycke | Nu formger vi sidan. Typografi, färg och bild hämtar vi ur er verksamhet, inte ur en mall. Förslaget lägger vi på en testadress som ni öppnar på er egen telefon och dator. Ni säger vad ni tycker, vi justerar och ni godkänner innan vi bygger. | Nu formger vi sidan. Typografi, färg och bild hämtar vi ur er verksamhet, inte ur en mall. Förslaget lägger vi på en testadress som ni öppnar på er egen telefon och dator. Ni säger vad ni tycker, vi justerar och ni godkänner innan vi bygger. | – | |
| 03 not | 16:9 är rutan där ert innehåll ska sitta. Formatet bestäms innan bilden finns. | 16:9 är rutan där ert innehåll ska sitta. Formatet bestäms innan bilden finns. | – | |
| 04 titel | Utveckling | Utveckling | – | låst |
| 04 stycke | Vi bygger sidan i kod från grunden. Den ska ladda snabbt och fungera med tangentbord och skärmläsare. Texter och bilder ändrar ni själva i ett innehållssystem, och vi visar hur. Behöver ni bokning, betalning eller kunddatabas bygger vi det i samma steg. | Vi bygger sidan i kod från grunden. Den ska ladda snabbt och fungera med tangentbord och skärmläsare. Texter och bilder ändrar ni själva i ett innehållssystem, och vi visar hur. Sidan är er att bygga vidare på. Behöver ni bokning, betalning eller kunddatabas bygger vi det i samma steg. | 0, 3 | v0 strök P2:s löfte "ert att bygga vidare på", och liggaren som också bar det är borta. Då försvinner ett befintligt löfte från sidan: ändrad innebörd. Återinfört i rätt kongruens ("sidan … er"). 49 ord |
| 04 not | 96 px mellan raderna. Resten av rytmen räknas ur det. | 96 px mellan raderna. Resten av rytmen räknas ur det. | – | |
| 05 titel | Innehåll | Innehåll | – | |
| 05 stycke | Ni kan er verksamhet, och vi sätter den på plats. Ni skickar texter och bilder när ni har dem. Vi kortar texten och anpassar bilderna för webben. Saknas något säger vi till i tid. På testadressen ser ni sidan fyllas. | Ni kan er verksamhet. Vi vet hur den ska stå på sidan. Ni skickar texter och bilder när ni har dem. Vi kortar texten och anpassar bilderna för webben. Saknas något säger vi till i tid. På testadressen ser ni sidan fyllas. | 0, 4 | "vi sätter den på plats" syftade på verksamheten, som inte är vad vi sätter på plats. Två korta satser, samma ansvarsfördelning som originalets "vi kan sätta den på plats" |
| 05 not | Ritningen får sitt innehåll och blir er sida. | Ritningen får sitt innehåll och blir er sida. | – | |
| 06 titel | Lansering | Lansering | – | |
| 06 stycke | Innan sidan går live går vi igenom den tillsammans: varje länk, varje formulär och varje koppling, på telefon och dator. Vi testar med tangentbord och skärmläsare. Sedan flyttar vi sidan till er adress och kontrollerar den där. Ni får en genomgång av hur ni ändrar innehållet själva. | Innan sidan går live granskar vi den tillsammans: varje länk, varje formulär och varje koppling, på telefon och dator. Vi testar med tangentbord och skärmläsare. Sedan flyttar vi sidan till er adress och kontrollerar den där. Ni får en genomgång av hur ni ändrar innehållet själva. | 3, 4 | "går live går vi igenom" ekade, och "genomgång" står i sista meningen. V3c löste samma eko med "granskar" |
| 06 not | Ritningen finns kvar som ram runt den färdiga sidan. | Ritningen finns kvar som ram runt den färdiga sidan. | – | |
| 07 titel | Förvaltning | Förvaltning | – | |
| 07 stycke | Vi finns kvar efter lansering. Ändringar, nya sidor och nya funktioner går samma väg som bygget: testadress, ert godkännande, sedan live. Har ni en fråga mejlar ni oss på kontakt@alunix.se. | Vi finns kvar efter lansering. Ändringar, nya sidor och nya funktioner går samma väg som bygget: testadress, ert godkännande, sedan live. Har ni en fråga mejlar ni oss på kontakt@alunix.se. | – | |
| 07 not | Varje ändring får en ny bokstav i ritningens hörn. | Varje ändring får en ny bokstav i ritningens hörn. | – | |
| SVG `title` | Ritning av processen | Ritning av processen | – | |
| SVG `desc` | En ritning av sidan som växer för varje steg och till sist blir en färdig sida. | En ritning av sidan som växer för varje steg och till sist blir en färdig sida. | – | |
| SVG-texter | 320 · 768 · 1440 · 7 rem · 16:9 · 96 px · A | 320 · 768 · 1440 · 7 rem · 16:9 · 96 px · A | – | mått |
| `.ledger-num` 01 till 07 | 01 … 07 | 01 … 07 | – | `aria-hidden` |

## Case-kapitlet

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| kicker | Exempelcase | Exempelcase | – | Plan 054 § 4 |
| `h2.cases-title` | Så blev ritningen en sida. | Så blev ritningen en sida. | – | |
| `.cases-lead` | Calyx och Hōrai är exempelsidor vi har byggt. Här berättar vi hur vi tänkte, från första skiss till färdig sida. | Calyx och Hōrai är exempelsidor vi har byggt. Här berättar vi hur vi tänkte, från första skiss till färdig sida. | – | Säger att det är exempel innan första steget |

## Case Calyx

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| kicker | Exempelcase | Exempelcase | – | |
| `h2.case-title` | Calyx | Calyx | – | |
| steg 1 h3 *(sajtens första skärm)* | Blommorna först | Blommorna först | – | |
| steg 1 p | Calyx är en exempelsida vi byggt för en tänkt florist i Stockholm. En florist säljer något man vill röra vid. Därför fick fotot hela första skärmen och rubriken står direkt på bilden. | Calyx är en exempelsida vi byggt för en tänkt florist i Stockholm. En florist säljer något man vill röra vid. Därför är första skärmen ett foto, med rubriken direkt på bilden. | 0, 3 | Sant mot sajten: fotot är 88 vh under en navigeringsrad, inte "hela" skärmen. Kortare |
| steg 2 h3 *(`#studio`)* | En lågmäld röst | En lågmäld röst | – | |
| steg 2 p | Vi skrev som en ateljé talar: korta stycken och inga utrop. Rubrikerna står i en klassisk serif där kursiven bär betoningen. Brödtexten är lugn och lätt att läsa. | Vi skrev som en ateljé talar: korta stycken, inga utrop. Rubriker och brödtext står i samma klassiska serif, och kursiven bär betoningen. | 0, 2, 4 | Sajten sätter rubrik och brödtext i samma serif (Cardo); v0 lät dem låta som två val. "lugn och lätt att läsa" var två adjektiv utan belägg; struket |
| steg 3 h3 *(bildparet efter `#studio`)* | Bilderna i par | Bilderna i par | – | |
| steg 3 p | Fotona står parvis med en liten märkning under varje, som i en katalog. Papperet är varmt och nästan vitt, så att blommorna får stå för färgen. | Fotona står parvis med en liten märkning under varje, som i en katalog. Papperet är varmt och nästan vitt, så att blommorna får stå för färgen. | – | Sant mot sajten (bildpar med mono-bildtext, krämvit grund) |
| steg 4 h3 *(`#index`)* | Listan ritade vi först | En lista, inte kort | 0 | Två rubriker med "först" i samma case (steg 1 och 4) betydde olika saker: det besökaren ser först och det vi ritade först. Rubriken säger nu beslutet; "ritade först" står kvar i stycket |
| steg 4 p | Det första vi ritade var veckans utbud. Buketterna står i en lista med namn, beskrivning och pris till höger, inte som kort i ett rutnät. Den enda egna färgen är en rostton, och den används sparsamt. | Det första vi ritade var veckans utbud. Buketterna står i en lista med namn, beskrivning och pris till höger, inte som kort i ett rutnät. Den enda egna färgen är en rostton, och den används sparsamt. | – | Sant: rosttonen står på ett namn i listan och på anfanger längre ned. Inga priser återges |
| steg 5 h3 *(`#commission`)* | Ett sätt att höra av sig | Ett sätt att höra av sig | – | |
| steg 5 p | Sidan slutar på mörk grund med en rubrik och en e-postadress. Inget formulär, ingen kalender. En ateljé ska gå att nå på det sätt den faktiskt tar emot beställningar. | Sidan slutar på mörk grund med en rubrik och en e-postadress. Inget formulär, ingen kalender. En ateljé som tar emot beställningar per mejl ska be om ett mejl. | 3, 4 | "på det sätt den faktiskt" var abstrakt och "faktiskt" utfyllnad. Nu konkret: sajtens ateljé tar beställningar per mejl |
| `.case-rail` | Blommorna först · En lågmäld röst · Bilderna i par · Listan ritade vi först · Ett sätt att höra av sig | Blommorna först · En lågmäld röst · Bilderna i par · En lista, inte kort · Ett sätt att höra av sig | 0 | Följer steg 4:s h3 |
| iframe `title` | Exempelsida: Calyx, florist i Stockholm | Exempelsida: Calyx, florist i Stockholm | – | låst |
| `figcaption` | Exempelsida: Calyx, florist i Stockholm | Exempelsida: Calyx, florist i Stockholm | – | låst |

## Bryggan

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| `h2.bridge-title` | Samma arbetssätt. En annan verksamhet. | Samma arbetssätt. En annan verksamhet. | – | |
| `.bridge-p` | En florist och en restaurang behöver olika sidor. Frågorna vi ställer är desamma: vad ska synas först, och vad ska besökaren göra sedan? | En florist och en restaurang behöver olika sidor. Frågorna vi ställer är desamma: vad ska synas först, och vad ska besökaren göra sedan? | – | |

## Case Hōrai

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| kicker | Exempelcase | Exempelcase | – | |
| `h2.case-title` | Hōrai | Hōrai | – | |
| steg 1 h3 *(sajtens första skärm)* | Kvällen först | Kvällen först | – | |
| steg 1 p | Hōrai är en exempelsida vi byggt för en tänkt restaurang. En plats som serverar på kvällen ska kännas som kvällen. Vi valde en mörk, varm grund och lät namnet stå stort i versaler. | Hōrai är en exempelsida vi byggt för en tänkt restaurang. En plats som serverar på kvällen ska kännas som kvällen. Därför är första skärmen ett mörkt foto, med namnet stort i versaler. | 0, 3 | Osant i v0: sajtens grund är ljust papper; det mörka är det nedtonade fotot. Formen speglar nu Calyx steg 1 |
| steg 2 h3 *(huset, ordljuset)* | Texten tänds när ni läser | Texten tänds ord för ord | 0 | Orden tänds av scrollen, inte av läsningen |
| steg 2 p | Stycket om huset lyser upp ord för ord medan ni scrollar. Det ska kännas som att någon berättar. Varje avsnitt har ett tecken i rött bredvid rubriken, som en stämpel. | Stycket om huset lyser upp medan ni scrollar. Det ska kännas som att någon berättar. Rubriken står i rött med ett japanskt tecken ovanför, som en stämpel. | 0, 3 | Osant i v0: tecknet står ovanför, inte bredvid, och är rött bara i huset och menyerna (rummet och bokningen har det i ljust). Nu beskrivs bara det som syns i ramen. "ord för ord" flyttat till rubriken |
| steg 3 h3 *(citatet, format läge)* | En paus | En paus | – | |
| steg 3 p | Mellan huset och menyerna står en enda mening på mörk grund. Den blir skarp när ni scrollar fram till den. Vi lade in den så att sidan andas innan det blir praktiskt. | Mellan huset och menyerna står en enda mening på mörk grund. Den blir skarp när ni scrollar fram till den. Vi lade den där för att ge besökaren en paus innan menyer och priser. | 3, 4 | "sidan andas" är en sliten bild; "innan det blir praktiskt" sade inte vad. Nu säger meningen vad pausen står före |
| steg 4 h3 *(menyerna)* | Menyerna som tavlor | Menyerna som tavlor | – | |
| steg 4 p | Varje meny har en romersk siffra, ett namn och ett pris i stort rött. Rubrikerna står i klassiska versaler, brödtexten i en serif som är lätt att läsa. Menyn går att läsa på avstånd. | Varje meny får en romersk siffra, ett namn och ett pris. Siffran och priset står i rött. Namnen står i klassiska versaler, brödtexten i en lättläst serif. Menyerna ska läsas som tavlor på en vägg. | 0, 2, 4 | v0 lät namnet låta rött; det är mörkt, bara siffran och priset är röda. "går att läsa på avstånd" var ett resultatpåstående; nu en avsikt som förklarar rubriken |
| steg 5 h3 *(rummet)* | Rummet | Rummet | – | |
| steg 5 p | Innan bokningen kommer rummet: en bild av matsalen över hela bredden, med texten direkt på bilden. Man vill se var man ska sitta innan man bokar. | Innan bokningen kommer rummet: en bild av matsalen över hela bredden, med texten direkt på bilden. Man vill se var man ska sitta innan man bokar. | – | Sant mot sajten |
| steg 6 h3 *(`#reservations`)* | Bokningen sist | Bokningen sist | – | |
| steg 6 p | Sidan slutar med hur man bokar, i klartext: när platserna släpps och vart man skriver. En restaurang lever på bokningar. Det sista på sidan ska vara det besökaren kom för. | Sidan slutar med hur man bokar, i klartext: när platserna släpps och vart man skriver. En restaurang lever på bokningar. Det sista på sidan ska vara det besökaren kom för. | – | Sant: släpptid, bokningsadress och e-post står i sektionen |
| `.case-rail` | Kvällen först · Texten tänds när ni läser · En paus · Menyerna som tavlor · Rummet · Bokningen sist | Kvällen först · Texten tänds ord för ord · En paus · Menyerna som tavlor · Rummet · Bokningen sist | 0 | Följer steg 2:s h3 |
| iframe `title` | Exempelsida: Hōrai, Asian fusion-koncept | Exempelsida: Hōrai, Asian fusion-koncept | – | låst |
| `figcaption` | Exempelsida: Hōrai, Asian fusion-koncept | Exempelsida: Hōrai, Asian fusion-koncept | – | låst |

## Priset och avslutet

| Plats | v0 | final | Pass som ändrade | Skäl |
|---|---|---|---|---|
| `h2.statement` | Alla har rätt till bra design. | Alla har rätt till bra design. | – | låst |
| `.price-ingress` | Två paket har priset utskrivet. Det tredje beror på vad ni behöver. | Två paket har priset utskrivet. Det tredje beror på vad ni behöver. | – | |
| rad 1 | Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering. | Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering. | – | låst |
| värde 1 | 26 900 kr | 26 900 kr | – | låst |
| rad 2 | Paket med bokningssystem, betalning och kunddatabas. | Paket med bokningssystem, betalning och kunddatabas. | – | låst |
| värde 2 | 38 900 kr | 38 900 kr | – | låst |
| rad 3 | Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera | Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera | – | låst |
| värde 3 | Pris vid förfrågan | Pris vid förfrågan | – | låst |
| `.close-mailto` | kontakt@alunix.se | kontakt@alunix.se | – | låst |

## Borttagna med sina sektioner

Oförändrat från v0 (jättesektionen, liggarens tre rader, "Hur vi tänker"). Enda följdändringen:
liggarens "ert att bygga vidare på" lever nu i 04 stycke, se ovan.
