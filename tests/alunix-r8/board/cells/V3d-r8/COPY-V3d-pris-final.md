# COPY · V3d pris final (Hōrais rubrik, prisblocket som en enhet)

Copy-agent, 2026-09-19. Antons feedback på `COPY-V3d-case-final.md`. Kedjan: `COPY-GATE.md`
§ V3d R13. `index.html` orörd. Byggaren skriver in kolumnen **final** ordagrant.

## Hōrais rubrikrad

| plats | tidigare | final | skäl |
|---|---|---|---|
| `h2#horai-title .case-line` | Hōrai serverar bokningen sist. | Hōrai dukar upp kvällen och ber om bokningen sist. | "serverar bokningen" gick att läsa som att bokningar kommer i andra hand. Nu är det sidan som *ber om* bokningen, och det görs sist; "dukar upp kvällen" säger vad som kommer före (huset, menyerna, rummet) med restaurangens eget verb. Annan byggnad än "Calyx fick bli ett vårnummer." (två verb i presens mot "fick bli" + substantiv). |

Alternativen som prövades:
1. **Hōrai dukar upp kvällen och ber om bokningen sist.** Vald. Otvetydig om ordningen, har ett eget verb ur restaurangen, och lämnar vändningen åt steg 6.
2. Hōrai visar matsalen innan den ber er boka. Klar men platt, täcker bara rummet (steg 5), och "er" gör läsaren till matgäst mitt i en text där "ni" är byråns kund.
3. Hōrai låter gästen äta med ögonen innan den bokar. Livlig, men idiomet är slitet och "den" kan syfta på fel led; säger inte att det är sidan som väntar med frågan.

Förkastad variant av 1: "Hōrai dukar upp kvällen innan den ber om en bokning." ("den" kunde syfta på kvällen) och "… kvällen före bokningen" (läses som kvällen innan bokningsdagen).

## Följdkontroll Hōrai-steg 6 och sidomenyn

| plats | tidigare | final | skäl |
|---|---|---|---|
| steg 6 h3 | Knappen fanns där hela tiden | Knappen fanns där hela tiden | Oförändrad. Rubriken säger att sidan ber om bokningen sist; steg 6 svarar att knappen ändå fanns i menyraden hela vägen. Paret hänger ihop bättre än förut, eftersom "ber om" gör skillnaden mellan frågan (sist) och knappen (hela tiden) tydlig. |
| steg 6 p | (oförändrad) | Sist står hur man bokar och när veckans platser släpps. Det som inte passar i ett formulär får en egen e-postadress. Den som inte orkar läsa klart har haft bokningsknappen i menyraden hela vägen ned. | Ingen ändring behövs. |
| steg 5 h3 | Rummet före bokningen | Rummet före bokningen | Oförändrad; ligger i linje med "dukar upp kvällen". |
| `.case-rail` | Namnet står en gång · Stycket tänds i er takt · En mening som saktar in · Priset står större än namnet · Rummet före bokningen · Knappen fanns där hela tiden | (oförändrad) | Följer h3; ingen h3 ändrades. |

## Prisblocket i sin helhet (bron och `#pris` blir en enhet)

Ordning i den nya enheten: kicker → rubrik → text → kort rad → prisliggaren. Sektionen
`.price-bridge#bro` försvinner som egen textsektion; om byggaren behåller dess plåt och
övergång är det en layoutfråga, texten nedan är allt som står.

| plats | tidigare | final | skäl |
|---|---|---|---|
| kicker (ovanför rubriken) | Från exempel till er sida (i `#bro`) | Från exempel till er sida | Flyttas upp över den låsta rubriken. Den gör övergångsarbetet så att rubriken kan stå ensam. |
| `h2.statement` | Alla har rätt till bra design. | Alla har rätt till bra design. | Låst, ordagrant. Nu blocket rubrik. |
| `.price-ingress` (ny text, ersätter den gamla) | Två av tre paket har ett pris utskrivet här. Det tredje beror på omfattningen. | Calyx och Hōrai byggde vi med samma steg som ert projekt går igenom. Vi läser verksamheten först och väljer bort allt som inte hjälper den. Så arbetar vi i alla tre paketen, också i det som kostar 26 900 kr. Paketen skiljer sig åt i vad sidan ska kunna göra. Det tredje prissätter vi efter omfattningen. | Knyter an till casen (samma steg för florist, restaurang och er), säger filosofin i en mening (läsa först, välja bort), gör rubriken konkret i pengar (samma arbete i det billigaste paketet, med det låsta priset), leder blicken till raderna (vad som skiljer dem) och behåller innebörden att det tredje inte har något fast pris. 56 ord. |
| kort rad (efter texten, före liggaren) | Första steget är ett samtal om er verksamhet. Skriv till kontakt@alunix.se. (i `#bro`) | Första steget är ett samtal om vad ni gör. | Litet, tydligt första steg, samma som processens steg 01 ("vad ni gör"). Adressen står redan under priserna och upprepas inte. "vad ni gör" i stället för "er verksamhet" undviker eko med textens "verksamheten". |
| rad 1 | Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering. · 26 900 kr | (oförändrad) | Låst. |
| rad 2 | Paket med bokningssystem, betalning och kunddatabas. · 38 900 kr | (oförändrad) | Låst. |
| rad 3 | Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera · Pris vid förfrågan | (oförändrad) | Låst. |

## Borttagna strängar

| plats | tidigare | final | skäl |
|---|---|---|---|
| `h2#bro-title` | Ni har sett arbetet. Här är priset. | (borttagen) | Antons beslut. Ersatt av den låsta rubriken "Alla har rätt till bra design." |
| `.bro-p` | Calyx och Hōrai byggde vi med samma steg som ert projekt går igenom. Paketen skiljer sig åt i vad sidan ska kunna göra. | (borttagen) | Båda meningarna lever vidare i den nya prisingressen. |
| `.bro-micro` | Första steget är ett samtal om er verksamhet. Skriv till kontakt@alunix.se. | (borttagen) | Ersatt av den korta raden utan adress. |
| `.price-ingress` (gammal) | Två av tre paket har ett pris utskrivet här. Det tredje beror på omfattningen. | (ersatt) | Innebörden bor kvar i "Det tredje prissätter vi efter omfattningen."; att två har pris syns i liggaren direkt under. |
| `aria-labelledby="bro-title"` | | | Byggaren: pekar på en borttagen rubrik; enheten märks upp med `h2.statement` (ge den ett id). |

## Principerna som bär texten

| princip | källa | användning |
|---|---|---|
| Hela historien först, fakta före adjektiv | valvet `wiki/domains/marketing/marketing-principles.md` § 3.5 → `[[sources/2021-09-26-founders-207-claude-hopkins-scientific-advertising]] › §Full story` | Casen är historien. Texten lägger inga nya påståenden, bara pekar tillbaka på dem ("samma steg") och vidare till raderna. |
| Specifika claims | § 3.2 → `[[sources/2021-09-26-founders-207-claude-hopkins-scientific-advertising]] › §Specificity`, `[[sources/2019-07-28-founders-82-david-ogilvy-ogilvy-on-advertising]] › §Price and letter-copy` | "Alla har rätt till bra design" blir ett pris: samma arbete "också i det som kostar 26 900 kr". Det enda talet är ett låst tal. Priset står rakt ut. |
| Service först, sänk tröskeln till första handling | § 2.1 → `[[sources/2021-03-08-founders-170-claude-hopkins]] › §Service först` | Slutraden: första steget är ett samtal, inget köp. Stöds av Commitment & Consistency och Activation Energy (`Skill(marketing-psychology)`). |
| Håll löften, lova inget nytt | § 6.3 → `[[sources/2023-06-05-founders-306-david-ogilvy-confessions-of-an-advertising-man]] › §Keep promises` | Allt i texten finns redan på sidan: stegen ("Samma sju steg i varje projekt"), bortvalen i casen, samtalet i steg 01, priserna. Inga garantier, rabatter, tider eller villkor. |
| Hick's Law | `Skill(marketing-psychology)` | En handling, inte två: adressen står bara under priserna. |

Medvetet inte använt: prisankring (visa högst först) och decoy, eftersom radernas ordning är
låst; riskreversering, eftersom en garanti vore ett nytt löfte (`PRODUCT.md` § Absences).
