# COPY · V3d R17 final (case-intro, prissektionen, borttagna småtexter)

Copy-agent, 2026-09-19. Antons beställning 2026-09-19. Kedjan: `COPY-GATE.md` § V3d R17.
`index.html` orörd. Byggaren skriver in kolumnen **final** ordagrant.

## Hur de tre byråerna introducerar sina case

Listsidorna hämtades 2026-09-19 med curl (HTTP 200 på alla tre), synlig text, rubriker och
metabeskrivning extraherades. Tidigare genomläsning av casen: `CASE-UNDERLAG.md`.

**Insign** (`insign.se/projektarkivet/`). Rubriken är bara "Projektarkivet". Under den en
enda rad som säger hur många projekt som är samlade och att de kommer från olika branscher,
sedan filter med antal per kategori och rutnätet. Ingen ton, inget löfte om process; det
säljande ("helt unika hemsidor", "helhetstänk") ligger bara i metabeskrivningen, osynligt.

**Highway Media** (`highwaymedia.se/case/`). Rubriken är bara "Case". Ingen ingress alls:
direkt filterknappar (E-handel, Hemsida, Marknadsföring) och korten, där varje kort bär
kundnamn och levererad tjänst. Arbetet får presentera sig självt.

**Hoy** (`hoy.se/projekt`). Rubriken "Projekt" följs av ett kort, talspråkligt tillägg
(ungefär "utvalda och goa") och sedan direkt korten, namn plus typ av leverans. Ingen
ingress. Rösten sitter i ett enda ord i rubriken, inte i en förklaring.

**Slutsats för oss.** Ingen av de tre förklarar vad ett case är eller vad läsaren ska få ut
av det. De säger som mest vad som finns där och låter namnen göra resten. Vår skillnad mot
dem: våra verksamheter finns inte, och det måste stå (`PRODUCT.md` § Absences), annars läses
Calyx och Hōrai som kunder. Det är alltså den enda sak introt måste säga. Resten är vad
läsaren får: valen, och skälen till dem.

## Case-kapitlet

| plats | tidigare | final | skäl |
|---|---|---|---|
| `h2#case-title` | Så blev ritningen en sida. | Exempelcase | Antons beslut, sätts i serif av byggaren. Samma form som byråernas rubriker ("Projektarkivet", "Case", "Projekt"): ett namn på sektionen, ingen idé. |
| `.cases-lead` | Calyx och Hōrai är exempelsidor vi har byggt. Här berättar vi hur vi tänkte, från första skiss till färdig sida. | Calyx är en florist i Stockholm och Hōrai en restaurang. Ingen av dem finns, men sidorna är färdiga. Vi går igenom vad vi valde i dem och varför. | Första meningen säger vilka de är med konkreta fakta ur de låsta bildtexterna, som nu tas bort, så uppgiften "florist i Stockholm" lever vidare här. Andra meningen är den ärliga uppgiften som skiljer oss från byråerna: verksamheterna är påhittade, arbetet är det inte (litet medgivande som gör resten trovärdigt, Hoys grepp och Pratfall i `Skill(marketing-psychology)`). Tredje lovar det casen faktiskt levererar, val och skäl, och inget mer. "Här berättar vi hur vi tänkte" beskrev sektionen; "från första skiss till färdig sida" lovade en process som casen inte följer steg för steg. "Bredvid varje sida" prövades och ströks: på mobil står ramen inte bredvid. 28 ord. |

## Prissektionen

| plats | tidigare | final | skäl |
|---|---|---|---|
| `h2#pris-title` | Alla har rätt till bra design. | Alla har rätt till bra design. | Låst, ordagrant. |
| `.price-ingress` | Calyx och Hōrai byggde vi med samma steg som ert projekt går igenom. Vi läser verksamheten först och väljer bort allt som inte hjälper den. Så arbetar vi i alla tre paketen, också i det som kostar 26 900 kr. Paketen skiljer sig åt i vad sidan ska kunna göra. Det tredje prissätter vi efter omfattningen. | (ingen text) | Se "Varför ingen text" nedan. |
| `.price-short` | Första steget är ett samtal om vad ni gör. | (ingen text) | Samtalet står redan i processens steg 01, adressen står i avslutet direkt efter. Raden var en tredje upprepning av något läsaren redan vet, och den försvann visuellt utan att något gick förlorat. |

### Varför ingen text

Rubriken + de tre raderna räcker, och de räcker bättre utan text.

1. **Rubriken är påståendet, priserna är beviset.** "Alla har rätt till bra design." följt
   direkt av 26 900 kr är hela argumentet. Varje mening emellan förklarar det läsaren själv
   ser på en sekund. Det är exakt felet Anton pekade ut i den gamla texten.
2. **Läsaren är ingen idiot.** `marketing-principles.md` § 3.5 (valvet): fakta till
   intelligenta köpare, "Consumer not a moron". Raderna *är* fakta. Allt vi kan lägga till
   är antingen en upprepning av raderna eller ett påstående utan belägg.
3. **Säljtestet, § 1.1.** En säljare som har visat två arbeten och lägger fram prislistan
   håller tyst medan kunden läser. Den som pratar över prislistan låter osäker på den.
4. **Skriv ut priset, § 3.2.** Priset står redan rakt ut. Att linda in det i text flyttar
   blicken från talet.
5. **Håll löften, lova inget nytt, § 6.3, och `PRODUCT.md` § Absences.** Det som skulle
   kunna tillföra något nytt här är just det vi inte får skriva: vad som ingår utöver
   raderna (villkor), när det blir klart (tider), att det är tryggt (garantier). Det som
   återstår är självklarheter.
6. **Hick's Law** (`Skill(marketing-psychology)`): en sak att läsa, tre rader att välja
   mellan, en adress direkt efter. Ingen fjärde sak.

**Om Anton ändå vill ha en mening,** är det enda som klarar kraven (ny information, inte en
självklarhet, inte en upprepning av raderna) en mening som kopplar ett case till ett paket:

> Calyx hade fått plats i standardpaketet.

Den gör "alla har rätt" konkret utan att upprepa talet och säger något läsaren inte kan se
själv. **Men det är ett sakpåstående som bara Anton kan bekräfta** (Calyx har CMS-innehåll,
en lista och en e-postadress, ingen bokning eller betalning, så det ser rimligt ut). Används
inte utan hans ok. Hōrai kopplas inte till något paket: dess bokning går via knapp och e-post,
och att kalla det paket 2 vore ett påstående om bokningssystemet vi inte kan stå för.

## Borttagna strängar

Antons beslut: ingen liten beskrivande stiltypisk AI-text (kickers, eyebrows, bildtexter,
sidomenyer med steglistor, små förklarande rader).

| plats | tidigare | final | skäl |
|---|---|---|---|
| `#case` `.kicker-sans` (rad ~1901) | Exempelcase | (borttagen) | Kicker. Ordet blir i stället rubriken. |
| `#case-calyx` `.kicker-sans` (rad ~1912) | Exempelcase | (borttagen) | Kicker. |
| `#case-horai` `.kicker-sans` (rad ~1967) | Exempelcase | (borttagen) | Kicker. |
| `#pris` `.kicker-sans` (rad ~2000) | Från exempel till er sida | (borttagen) | Kicker, uttryckligen nämnd av Anton. |
| `.process-chapter` `.kicker-sans` (rad ~1668) | Så går det till | (borttagen) | Kicker, uttryckligen nämnd av Anton. Rubriken "Från samtal till lanserad sida." bär sektionen ensam. |
| `#case-calyx` `figcaption.frame-cap` | Exempelsida: Calyx, florist i Stockholm | (borttagen) | Bildtext, uttryckligen nämnd av Anton. Uppgiften "florist i Stockholm" flyttar in i case-introt. **Låst i `PRODUCT.md` § Brand Commitments;** Antons beslut 2026-09-19 går före, låslistan bör uppdateras. `iframe title` behålls (osynlig, tillgänglighet). |
| `#case-horai` `figcaption.frame-cap` | Exempelsida: Hōrai, Asian fusion-koncept | (borttagen) | Som ovan. `iframe title` behålls. |
| tesbandet `figcaption.thesis-caption` (rad ~1639) | Exempelsida: Hyperborea, konferens i Lund | (borttagen) | Samma typ av bildtext, samma låskonflikt. Bilden har redan `alt="Startsidan för Hyperborea, en konferens i Lund"`, så namnet finns kvar för skärmläsare. |
| `#case-calyx` `.case-rail` | Fotot bär rubriken · En serif för allt man läser · Färgen finns redan i bilderna · Utbudet som prislista · Ett mejl räcker | (borttagen) | Sidomeny med steglista, uttryckligen förbjuden. Stegens h3 står kvar i texten; railen var en andra kopia (`aria-hidden`). |
| `#case-horai` `.case-rail` | Namnet står en gång · Stycket tänds i er takt · En mening som saktar in · Priset står större än namnet · Rummet före bokningen · Knappen fanns där hela tiden | (borttagen) | Som ovan. |
| `#case-title` | Så blev ritningen en sida. | Exempelcase | Antons beslut (se case-kapitlet). |
| `.price-ingress` | (hela texten, se prissektionen) | (borttagen) | Antons dom över tre av meningarna; de två andra förklarade det raderna redan visar. |
| `.price-short` | Första steget är ett samtal om vad ni gör. | (borttagen) | Se prissektionen. |

## Flaggat, inte borttaget (Antons avgörande)

1. **`.process-lead`**: "Sju steg, samma ordning i varje projekt, så att ni alltid vet var vi
   är." Är en liten förklarande rad av den förbjudna sorten (säger vad listan under redan
   visar, och "så att ni alltid vet" är en självklarhet). Rekommendation: stryk. Ligger utanför
   beställningens två sektioner, därför inte i final-tabellen.
2. **`.process-note` × 7** (t.ex. "Ett tomt ark. Inget ritas innan vi vet vad sidan ska säga.",
   "96 px, radavståndet i liggaren. All rytm räknas ur det."). Marginalanteckningar i
   ritningens röst. De bär processaktens ritningsgrepp och är inte generiska, men de är
   formmässigt "små förklarande rader". Anton avgör.
3. **Case-texternas första steg** börjar "Calyx är en exempelsida för en tänkt florist i
   Stockholm." och "Hōrai är en exempelsida för en tänkt restaurang." Med det nya introt står
   det två gånger. Förslag till nästa runda: stryk första meningen i båda stegen.
4. **`PRODUCT.md` § Brand Commitments** listar de tre bildtexterna som låst copy. Antons
   beslut i dag upphäver det; låslistan behöver en rad om det, som för "VI BYGGER ERT
   VARUMÄRKE.".
5. **`aria-labelledby`** i `#pris` pekar på `pris-title`, som står kvar. Inga brutna id.

## Antons beslut 2026-09-19, efter copy-gaten (lead för in)

| Plats | Tidigare | Final | Skäl |
|---|---|---|---|
| Calyx steg 1 `p` | Calyx är en exempelsida för en tänkt florist i Stockholm. Vi byggde den som ett tidskriftsnummer, … | Vi byggde Calyx som ett tidskriftsnummer, … (resten av stycket oförändrat) | Anton: ja till att stryka meningen, introt säger det redan. "den" byts mot "Calyx" så syftningen håller |
| Hōrai steg 1 `p` | Hōrai är en exempelsida för en tänkt restaurang. Första skärmen är … | Första skärmen är … (resten av stycket oförändrat) | Samma beslut |
| Processens ingress (`.process-lead`) | Sju steg, samma ordning i varje projekt, så att ni alltid vet var vi är. | *(borttagen)* | Anton: ja, den hör till den förbjudna småtexten (F-016) |

## Pristext, Antons andra beställning

Antons beställning 2026-09-19: en text direkt under "Alla har rätt till bra design." som
bryggar från casen till priserna. Den ska bära tre saker: casen är beviset, nivån är densamma
i alla tre prislägena, sidan formas efter kundens egna behov och önskemål. Den ska inte likna
den strukna texten i ordval, grepp eller förutsättning. Kedjan: `COPY-GATE.md` § V3d R17,
"pristext, andra beställningen". Ersätter "(ingen text)" i `.price-ingress` ovan.

### Tre alternativ

| | text | ord | styrka | svaghet |
|---|---|---|---|---|
| A | Med bra design menar vi det ni just har sett. Den nivån får ni på varje rad nedan, och sidan ritar vi efter era egna behov och önskemål. | 28 | Fortsätter rubrikens mening: tar dess eget ord "bra design" och pekar på casen i stället för att förklara dem. "varje rad nedan" leder blicken till priserna. | Casen nämns inte vid namn; läsaren har sett dem, vilket sidans ordning garanterar. |
| B | Calyx och Hōrai ritades efter vad just de behövde. Er sida ritar vi likadant, efter era behov och önskemål, på vilken rad nedan ni än väljer. | 26 | Konkret om hur casen kom till. | Parallellen de/ni är ett mönster, "likadant" ligger nära den strukna textens "samma steg", och "vilken … ni än väljer" är ett förklätt "oavsett". |
| C | Det ni såg i Calyx och Hōrai är nivån på varje rad nedan. Hur er sida blir beror på vad ni behöver och vill ha. | 25 | Kortast och sakligast. | Börjar om i stället för att fortsätta rubriken; "beror på" låter som en brasklapp. |

### Val: A

> Med bra design menar vi det ni just har sett. Den nivån får ni på varje rad nedan, och sidan ritar vi efter era egna behov och önskemål.

- **Läses som rubrikens fortsättning.** Rubriken är ett påstående. Första meningen säger vad
  påståendet betyder genom att peka på beviset, inte genom att beskriva det.
- **Respekterar läsaren.** Inget om hur paketen skiljer sig, inget pris upprepat, ingen
  förklaring av det raderna visar. Den strukna texten sa till kunden vad den skulle förstå;
  A säger bara vad vi menar.
- **"Den nivån … på varje rad"** bär "samma nivå" utan ordet "samma" och utan "också i det som
  kostar"-greppet: ingen rad pekas ut som den billiga.
- **"era egna behov och önskemål"** är Antons egna ord, i kundens ägo. "ritar" knyter till
  processens ritningsgrepp.
- Ordval kontrollerat mot den strukna texten (samma, steg, läser, väljer bort, paket, också,
  kostar, skiljer sig, omfattning) och mot case-introt (florist, finns, färdiga, valde,
  varför, går igenom): A delar inget av dem.

### Principerna som bär A, och varför just de

1. **Bevis före påstående.** `marketing-principles.md` § 3.5 (valvet): fakta till
   intelligenta köpare, "Consumer not a moron". Casen är fakta som redan ligger på sidan;
   texten lägger inte till ett nytt påstående, den pekar på dem. Därför beskriver A:s första
   mening inte casen alls.
2. **Riskminskning genom visat arbete.** `Skill(marketing-psychology)`: *Regret Aversion* och
   *Availability Heuristic*. Köparens risk är att få något sämre än det hen har sett. Vi får
   inte ge en garanti (`PRODUCT.md` § Absences), men "den nivån får ni på varje rad" gör det
   visade arbetet till det man köper, och casen gör utfallet lätt att föreställa sig.
3. **Kundens behov i centrum.** `marketing-principles.md` § 2.2 (individ, inte massa) och
   *Jobs to Be Done*. "era egna behov och önskemål" är textens enda löfte, och det är ett som
   processen redan ger (§ 6.3, lova inget nytt).
4. **Säljtestet, § 1.1.** En säljare som just visat två arbeten säger ungefär: det här menar
   vi, det här får ni, och vi gör det efter er. Sedan prislistan. A är den repliken.
5. **Hick's Law.** En rörelse för blicken, nedåt till raderna. Ingen ny handling.

Avvisat: prisankring och *Good-Better-Best* (radernas ordning är låst), knapphet och
riskreversering (tider, villkor och garantier finns inte).
