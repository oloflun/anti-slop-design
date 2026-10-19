# COPY · V3d case v1 (casen, bryggan, övergången till priset)

Copy-agent, 2026-09-19. Underlag: `CASE-UNDERLAG.md` (referenserna, principerna, sakunderlaget
ur sajterna). Utkast före kedjan copywriting → copy-editing → humanizer-svenska.

Regler som gäller varje sträng nedan: vi-form, "ni/er" bara mot läsaren, inga tankstreck
(U+2010 till U+2015, U+2212), inga siffror, inga kunder, citat, resultat, tider eller namn.
Calyx och Hōrai kallas exempelsidor för tänkta verksamheter. Varje påstående om ett val går
att se i sajten (radhänvisningar i underlaget). Låst copy rörs inte. Casestegen håller sig
under 40 ord (plan 054 § 13, mobilen).

**Markering:** *ny* = ny sträng, ingen motsvarighet i dag. *ersätter* = ersätter den
namngivna strängen i COPY-V3d-final.

## Case-rubrikerna

Formen är Hoys: namnet först, sedan ett påstående om vad sidan gör. Förslag till markup, så att
namnet behåller sin storlek och påståendet kan brytas på egen rad på mobilen:
`<h2 class="case-title">Calyx <span class="case-claim">läses som en tidskrift.</span></h2>`.
Skärmläsaren läser då hela meningen.

### Calyx (ersätter `Calyx`)

| Alternativ | Idé |
|---|---|
| **Calyx läses som en tidskrift.** | Sajtens bärande grepp: utgåva i hörnet, bildtexter med löpnummer, veckans utbud som innehållsförteckning. **Valet.** |
| Calyx låter blommorna ta färgen. | Färgbeslutet: nästan ingen egen färg. Sant men smalare, och det är ett steg, inte hela idén. |
| Calyx byter utbud varje vecka. | Listan i stället för kort. Säger mer om den tänkta floristen än om sidan. |

### Hōrai (ersätter `Hōrai`)

| Alternativ | Idé |
|---|---|
| **Hōrai sparar bokningen till sist.** | Sidans ordning: huset, pausen, menyerna, rummet och sist bokningen. Rubriken bär ett val som går att ifrågasätta, och steg sex svarar (knappen finns i menyraden hela vägen). **Valet.** |
| Hōrai följer kvällens ordning. | Samma idé, mjukare. Svagare eftersom bokningen i verkligheten kommer före kvällen. |
| Hōrai ställer priset främst. | Menyernas pris som är större än namnet. Bra detalj, men för smal som rubrik och krockar med prisavsnittet längre ned. |

## Case Calyx

Stegen och ramens ankare är oförändrade (`top`, `#studio`, `#studio + section`, `#index`,
`#commission`). Fem steg räcker: varje steg har ett eget beslut att visa i ramen.

| Steg · ramen visar | h3 | p | Markering |
|---|---|---|---|
| 1 · heron | Fotot bär rubriken | Calyx är en exempelsida för en tänkt florist i Stockholm. Vi byggde den som ett tidskriftsnummer, med utgåvan i hörnet och rubriken direkt på fotot. En florist säljer något man vill röra vid, så bilden kom först. | h3 ersätter `Blommorna först`; p ersätter steg 1 p |
| 2 · `#studio` | En serif för allt man läser | Rubriker och brödtext står i samma klassiska serif, och kursiven sköter betoningen. Det enda andra typsnittet är ett skrivmaskinslikt för etiketter och bildtexter. De ska se ut som anteckningar i marginalen. | h3 ersätter `En lågmäld röst`; p ersätter steg 2 p |
| 3 · bildparet | Färgen finns redan i bilderna | Fotona står parvis med en liten märkning under varje, som i en katalog. Grunden är varmt, nästan vitt papper med ett svagt korn. Sidans enda egna färg är en rostton, och i listan står den på ett namn. | h3 ersätter `Bilderna i par`; p ersätter steg 3 p |
| 4 · `#index` | Utbudet som prislista | Veckans buketter står i en lista med namn, några rader och pris till höger. Kort i ett rutnät hade krävt ett nytt foto av varje bukett varje vecka. En rad text är lättare att byta än en bild. | h3 ersätter `En lista, inte kort`; p ersätter steg 4 p |
| 5 · `#commission` | Ett mejl räcker | Sidan slutar med hur en beställning går till: besökaren skriver om rummet och ljuset, och ateljén svarar med vad som finns den veckan. Ett formulär har inte plats för det samtalet. Därför står där bara en e-postadress. | h3 ersätter `Ett sätt att höra av sig`; p ersätter steg 5 p |
| `.case-rail` | Fotot bär rubriken · En serif för allt man läser · Färgen finns redan i bilderna · Utbudet som prislista · Ett mejl räcker | | ersätter nuvarande skena (följer h3) |

Bortval och avvägningar i caset: ett andra rubriktypsnitt (steg 2), egen färg utöver en (steg 3),
kort med foto (steg 4), formulär (steg 5).

## Bryggan

| Plats | Text | Markering |
|---|---|---|
| `h2.bridge-title` | Nästa sida säljer en kväll. | ersätter `Samma arbetssätt. En annan verksamhet.` |
| `.bridge-p` | En bukett syns på ett foto. En middag gör det inte. Hōrai fick berätta om huset, köket och rummet innan den ber om en bokning. | ersätter `En florist och en restaurang behöver olika sidor. Frågorna vi ställer är desamma: …` |

Skäl: den gamla bryggan var en parallell formel ("Samma X. En annan Y.") och frågan i den
upprepade case-kapitlets lead. Den nya säger vad som skiljer uppgifterna åt och förbereder
Hōrais rubrik. "köket" syftar på menyerna, som sajten beskriver som kökets.

## Case Hōrai

Stegen och ankarna är oförändrade (`top`, husets stycke, `#quote-section` centrerad, menyerna,
rummet, `#reservations`). Sex steg behålls: rummet och bokningen är två olika beslut
(se bild före, boka efter), och rubriken bygger på att bokningen står ensam sist.

| Steg · ramen visar | h3 | p | Markering |
|---|---|---|---|
| 1 · heron | Namnet står en gång | Hōrai är en exempelsida för en tänkt restaurang. Första skärmen är ett mörkt foto med namnet i stora versaler och öppettiderna i hörnet. Loggan i menyraden tänds först när rubriken rullat förbi. Namnet står aldrig två gånger på samma skärm. | h3 ersätter `Kvällen först`; p ersätter steg 1 p |
| 2 · huset | Stycket tänds i er takt | Stycket om huset börjar nästan osynligt och tänds ord för ord medan ni scrollar. Vi ville att det skulle läsas i berättarens takt. Rubriken står i rött, med ett japanskt tecken ovanför som en stämpel. | h3 ersätter `Texten tänds ord för ord`; p ersätter steg 2 p |
| 3 · citatet | En mening som saktar in | Mellan huset och menyerna står en enda mening på mörk grund. Den kommer in suddig, blir skarp mitt på skärmen och suddas ut igen. Vi lade den där för att sakta ner läsningen innan det blir menyer och priser. | h3 ersätter `En paus`; p ersätter steg 3 p |
| 4 · menyerna | Priset står större än namnet | Varje meny får en romersk siffra, ett namn och ett pris per gäst, i rött och större än namnet. Gästen väljer en hel kväll, inte en rätt, och det är priset man jämför. Dryckerna står i en egen grön ton. | h3 ersätter `Menyerna som tavlor`; p ersätter steg 4 p |
| 5 · rummet | Rummet före bokningen | Innan bokningen kommer matsalen, i en bild över hela bredden med texten direkt på bilden. Den som ska boka vill se var den ska sitta. Rummet blir det sista man läser innan man gör något. | h3 ersätter `Rummet`; p ersätter steg 5 p |
| 6 · `#reservations` | Bokningen sist, knappen hela vägen | Sidan slutar med hur man bokar: när platserna släpps, var man bokar och vart man mejlar om det inte passar i en bokning. Den som inte vill läsa klart har haft knappen till bokningen i menyraden hela vägen ned. | h3 ersätter `Bokningen sist`; p ersätter steg 6 p |
| `.case-rail` | Namnet står en gång · Stycket tänds i er takt · En mening som saktar in · Priset står större än namnet · Rummet före bokningen · Bokningen sist, knappen hela vägen | | ersätter nuvarande skena (följer h3) |

Bortval och avvägningar i caset: logga och rubrik samtidigt (steg 1), ett stycke som går att
skumma (steg 2), priset som liten rad (steg 4), bokningen tidigt (steg 6, med knappen som
avvägningen).

## Övergången till priset

**Plats.** En ny sektion mellan `#case-horai` och `#pris`, till exempel
`section.to-price` med `aria-labelledby`. I dag går sidan direkt från Hōrais svarta plåt till
prisets foto. Förslag till material: papper (`--bg`), så att svart plåt, papper och foto
följer på varandra med synliga gränser och ljusbudgeten mellan processakten och priset får en
skiva till (plan 054 § 5). Anatomin kapitel i centrerad spalt (som `.cases-chapter`), högst
en skärm. Arkitekten avgör; texten fungerar också som topp i `#pris`, ovanför den låsta
rubriken, om en ny sektion inte ryms.

**Principerna den bygger på** (källor i CASE-UNDERLAG): hela historien först och sedan
priset (Hopkins, Ogilvy); skriv ut priset och säg det rakt (Ogilvy); skriv som en säljare mitt
emot köparen (Hopkins säljtest); gör första steget litet och tydligt (Hopkins, service först);
lova inget som inte redan står på sidan (Ogilvy, håll löften).

### Rubrik (ny)

| Alternativ | Kommentar |
|---|---|
| **Ni har sett arbetet. Här är priset.** | Säljarens mening efter genomgången: det ni just sett, och nu det ni behöver veta. Pekar rakt på prislistan utan omskrivning. **Valet.** |
| Så här kostar det att börja. | Mjukare, men "börja" lovar mer än priset svarar på. |
| Samma arbete, för er verksamhet. | Knyter an till casen men säger inte att priset kommer. Priset ska inte bli en överraskning. |

### Rader

| Plats | Text | Markering |
|---|---|---|
| kicker | Från exempel till er sida | ny |
| `h2` | Ni har sett arbetet. Här är priset. | ny |
| stycke | Calyx och Hōrai byggde vi med samma steg som ert projekt går igenom. Paketen skiljer sig i vad sidan ska kunna göra. | ny |
| mikrorad | Första steget är ett samtal om er verksamhet. Skriv till kontakt@alunix.se. | ny |

Kontroll mot löftena: "samma steg" hänvisar till processakten ("Samma sju steg i varje
projekt"). "vad sidan ska kunna göra" sammanfattar de tre låsta paketraderna (CMS och SEO,
bokning och betalning, skräddarsytt) utan att citera eller ändra dem. "Första steget är ett samtal" är processens steg 01 ("Vi börjar med ett
samtal om er verksamhet"). Inga tider, rabatter, garantier eller villkor. Adressen är den låsta.

Läsordning efter övergången, oförändrad: `Alla har rätt till bra design.` → prisingressen →
de tre låsta raderna och priserna → `kontakt@alunix.se`.

**Ett hänsynstagande till prisingressen.** Stycket ovan säger "Paketen skiljer sig i vad sidan
ska kunna göra". Ingressen på sidan i dag säger "Det tredje beror på omfattningen" (index.html
rad 1856), och COPY-V3d-final säger "Det tredje beror på vad ni behöver". Ingen av dem krockar
med övergången, men om ingressen blir v0:s "vad ni behöver" hamnar "vad sidan ska kunna" och
"vad ni behöver" nära varandra. Då är index.html-varianten ("omfattningen") bättre.

## Orörda strängar i området

Case-kapitlet (`Exempelcase`, `Så blev ritningen en sida.`, `.cases-lead`), kickern
`Exempelcase` i båda casen, iframe-titlar och bildtexter (låsta), hela `#pris` och avslutet.
