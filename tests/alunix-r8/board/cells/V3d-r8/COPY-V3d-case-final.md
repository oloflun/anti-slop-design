# COPY · V3d case final (casen, bryggan, övergången till priset)

Copy-agent, 2026-09-19. Underlag `COPY-V3d-case-v1.md` och `CASE-UNDERLAG.md`. Kedjan och vad
varje pass ändrade: `COPY-GATE.md` § V3d R12. `index.html` orörd.

Placeringen är densamma som i v1: samma platser, samma ordning, samma markering (ny /
ersätter) och samma förslag till markup för case-rubriken
(`<h2 class="case-title">Calyx <span class="case-claim">…</span></h2>`). Byggaren skriver in
kolumnen **final** ordagrant. Pass: 0 = UX-copy, 2 = copywriting, 3 = copy-editing,
4 = humanizer-svenska, 5 = mekaniskt.

## Case-rubriker

| plats | v1 | final | pass som ändrade | skäl |
|---|---|---|---|---|
| `h2#calyx-title` (ersätter `Calyx`) | Calyx läses som en tidskrift. | Calyx fick bli ett vårnummer. | 4 | Antons "lite roligare". Sajten kallar sig själv "Vol. ix · spring" och "Spring Edition"; "vårnummer" är sajtens egen detalj och en bild, inte en kategori. v1 och Hōrai-rubriken bildade ett par med samma byggnad (namn + presens + bestämning); nu skiljer de sig. |
| `h2#horai-title` (ersätter `Hōrai`) | Hōrai sparar bokningen till sist. | Hōrai serverar bokningen sist. | 4 | Restaurangens eget verb: bokningen som sista rätten. Samma påstående som v1, och steg 6 svarar fortfarande (knappen finns hela vägen). |

## Case Calyx

| plats | v1 | final | pass som ändrade | skäl |
|---|---|---|---|---|
| steg 1 h3 | Fotot bär rubriken | Fotot bär rubriken | ingen | Går att läsa ensam och stämmer mot heron (h1 direkt på fotot). |
| steg 1 p | Calyx är en exempelsida för en tänkt florist i Stockholm. Vi byggde den som ett tidskriftsnummer, med utgåvan i hörnet och rubriken direkt på fotot. En florist säljer något man vill röra vid, så bilden kom först. | Calyx är en exempelsida för en tänkt florist i Stockholm. Vi byggde den som ett tidskriftsnummer, med utgåvan i hörnet och rubriken direkt på fotot. En bukett vill man röra vid, och på en skärm kommer ett stort foto närmast. | 2, 4 | "så bilden kom först" var en slutsats utan skäl (och ekade gamla "Blommorna först"). Nu står skälet: fotot är det närmaste en skärm kommer att röra vid. 40 ord. |
| steg 2 h3 | En serif för allt man läser | En serif för allt man läser | ingen | |
| steg 2 p | Rubriker och brödtext står i samma klassiska serif, och kursiven sköter betoningen. Det enda andra typsnittet är ett skrivmaskinslikt för etiketter och bildtexter. De ska se ut som anteckningar i marginalen. | Rubriker och brödtext står i samma klassiska serif, och kursiven sköter betoningen. Ett andra rubriktypsnitt hade dragit åt reklam. Det enda andra typsnittet är skrivmaskinslikt och används till etiketter och bildtexter, som anteckningar i marginalen. | 3, 4 | v1 listade bortvalet (ett andra rubriktypsnitt) i sin kommentar men inte i texten. Nu står det, med skäl (Hoy-greppet). "De ska se ut som" sammanslaget till en bisats. Sajten: Cardo + PT Mono, inget annat. |
| steg 3 h3 | Färgen finns redan i bilderna | Färgen finns redan i bilderna | ingen | |
| steg 3 p | Fotona står parvis med en liten märkning under varje, som i en katalog. Grunden är varmt, nästan vitt papper med ett svagt korn. Sidans enda egna färg är en rostton, och i listan står den på ett namn. | Fotona står parvis med en liten märkning under varje, som i en katalog. Grunden är varmt, nästan vitt papper med ett svagt korn. Sidan har en enda egen färg, en rostton, och den dyker upp först längre ned. | 0 | Ramen står på bildparet i steg 3; listan syns inte där. Rosttonen finns dessutom på anfangerna längre ned, inte bara på ett namn. Nu stämmer texten med ramen och är sann för hela sidan (första rost i koden: namnet i `#index`). |
| steg 4 h3 | Utbudet som prislista | Utbudet som prislista | ingen | |
| steg 4 p | Veckans buketter står i en lista med namn, några rader och pris till höger. Kort i ett rutnät hade krävt ett nytt foto av varje bukett varje vecka. En rad text är lättare att byta än en bild. | Veckans utbud står i en lista med löpnummer, namn, en kort beskrivning och priset till höger. Kort i ett rutnät hade krävt ett nytt foto av varje bukett varje vecka. Med en lista räcker det att skriva om en rad. | 0, 4 | Pass 0: listan har löpnummer och en rad beskrivning (inte "några rader"), och en post är ett restaurangavtal, inte en bukett → "utbud". Pass 4: sista meningen var ett visdomsavslut; nu säger den vad som händer i praktiken. |
| steg 5 h3 | Ett mejl räcker | Ett mejl räcker | ingen | |
| steg 5 p | Sidan slutar med hur en beställning går till: besökaren skriver om rummet och ljuset, och ateljén svarar med vad som finns den veckan. Ett formulär har inte plats för det samtalet. Därför står där bara en e-postadress. | Sidan slutar med hur en beställning går till. Besökaren skriver om rummet och ljuset, och ateljén svarar med vad som finns den veckan. Sådant passar dåligt i formulärfält, så vi satte en e-postadress där formuläret annars hade stått. | 0, 3, 4 | Pass 0: "bara en e-postadress" var osant, sektionen har också en besöksadress. Pass 3: kolonmeningen delad (klarhet). Pass 4: "har inte plats för det samtalet" var en sentens; nu ett konkret skäl och bortvalet synligt i en mening. |
| `.case-rail` | Fotot bär rubriken · En serif för allt man läser · Färgen finns redan i bilderna · Utbudet som prislista · Ett mejl räcker | Fotot bär rubriken · En serif för allt man läser · Färgen finns redan i bilderna · Utbudet som prislista · Ett mejl räcker | ingen | Följer h3. |

## Bryggan

| plats | v1 | final | pass som ändrade | skäl |
|---|---|---|---|---|
| `h2.bridge-title` | Nästa sida säljer en kväll. | Nästa sida säljer en kväll. | ingen | Konkret, pekar framåt, inte en formel. |
| `.bridge-p` | En bukett syns på ett foto. En middag gör det inte. Hōrai fick berätta om huset, köket och rummet innan den ber om en bokning. | En bukett kan man visa på ett foto. Om en middag måste man berätta, så på Hōrai kommer huset och menyerna före bokningen. | 0, 4 | Pass 4: "X. Y gör det inte." var negativ parallellism i två korta satser, och "huset, köket och rummet" en uppräkning i tre. Pass 0: "köket" var en omskrivning för menyerna; nu står sektionernas riktiga namn. Förbereder rubriken "serverar bokningen sist". |

## Case Hōrai

| plats | v1 | final | pass som ändrade | skäl |
|---|---|---|---|---|
| steg 1 h3 | Namnet står en gång | Namnet står en gång | ingen | |
| steg 1 p | Hōrai är en exempelsida för en tänkt restaurang. Första skärmen är ett mörkt foto med namnet i stora versaler och öppettiderna i hörnet. Loggan i menyraden tänds först när rubriken rullat förbi. Namnet står aldrig två gånger på samma skärm. | Hōrai är en exempelsida för en tänkt restaurang. Första skärmen är ett mörkt foto med namnet i stora versaler och öppettiderna i hörnet. Loggan i menyraden tänds när bilden rullat förbi, så namnet står bara en gång på första skärmen. | 0, 4 | Pass 0: koden döljer loggan medan hela hero-sektionen syns, inte rubriken. "aldrig … på samma skärm" var för starkt (sidfotens © HŌRAI kan dela skärm med loggan). Pass 4: den fristående slutmeningen blev bisats med "så", orsak före följd. |
| steg 2 h3 | Stycket tänds i er takt | Stycket tänds i er takt | ingen | |
| steg 2 p | Stycket om huset börjar nästan osynligt och tänds ord för ord medan ni scrollar. Vi ville att det skulle läsas i berättarens takt. Rubriken står i rött, med ett japanskt tecken ovanför som en stämpel. | Stycket om huset börjar nästan osynligt och tänds ord för ord medan ni scrollar. Vi ville att det skulle läsas långsamt, som när någon berättar. Rubriken står kvar i rött, med ett japanskt tecken ovanför som en stämpel. | 0 | "i berättarens takt" motsade rubriken "i er takt" (det är läsarens scroll som tänder orden). "står kvar": rubriken är sticky medan stycket tänds (sajten). |
| steg 3 h3 | En mening som saktar in | En mening som saktar in | ingen | |
| steg 3 p | Mellan huset och menyerna står en enda mening på mörk grund. Den kommer in suddig, blir skarp mitt på skärmen och suddas ut igen. Vi lade den där för att sakta ner läsningen innan det blir menyer och priser. | Mellan huset och menyerna står en enda mening på mörk grund. Den är suddig tills den når mitten av skärmen och suddas ut igen när ni scrollar vidare. Den står där för att bromsa läsningen före menyer och priser. | 3, 4 | Pass 4: tre verb i rad (kommer, blir, suddas) blev två led. Pass 3: "Vi lade den där" och steg 2:s "Vi ville" gav två vi-meningar i följd med samma form; "sakta ner" ekade h3 "saktar in". |
| steg 4 h3 | Priset står större än namnet | Priset står större än namnet | ingen | Sant: pris 3.8 till 6 rem, namn 2.6 till 4.4 rem. |
| steg 4 p | Varje meny får en romersk siffra, ett namn och ett pris per gäst, i rött och större än namnet. Gästen väljer en hel kväll, inte en rätt, och det är priset man jämför. Dryckerna står i en egen grön ton. | Varje meny har en romersk siffra, ett namn och ett pris per gäst. Priset står i rött, större än namnet. Utan à la carte väljer man en hel meny och letar först efter priset. Dryckerna har en egen grön ton. | 0, 4 | Pass 0: "i rött och större" syftade grammatiskt på alla tre; bara siffra och pris är röda. Pass 4: "en hel kväll, inte en rätt" var "inte X utan Y"; nu sajtens eget faktum (ingen à la carte) som skäl. |
| steg 5 h3 | Rummet före bokningen | Rummet före bokningen | ingen | |
| steg 5 p | Innan bokningen kommer matsalen, i en bild över hela bredden med texten direkt på bilden. Den som ska boka vill se var den ska sitta. Rummet blir det sista man läser innan man gör något. | Precis före bokningen kommer matsalen, i en bild över hela bredden. Texten står direkt på fotot, med en mörk toning från vänster så att den går att läsa. Den som ska boka vill se var den ska sitta. | 2, 4 | Pass 4: sista meningen var ett visdomsavslut; struken. Pass 2: i stället ett konkret val i ramen (toningen från vänster, sajtens `bg-gradient-to-r`) med sitt skäl. |
| steg 6 h3 | Bokningen sist, knappen hela vägen | Knappen fanns där hela tiden | 4 | v1 var två symmetriska halvor med komma och upprepade case-rubrikens "sist". Nu svarar steget på rubriken: bokningen serveras sist, men knappen fanns hela tiden. |
| steg 6 p | Sidan slutar med hur man bokar: när platserna släpps, var man bokar och vart man mejlar om det inte passar i en bokning. Den som inte vill läsa klart har haft knappen till bokningen i menyraden hela vägen ned. | Sist står hur man bokar och när veckans platser släpps. Det som inte passar i ett formulär får en egen e-postadress. Den som inte orkar läsa klart har haft bokningsknappen i menyraden hela vägen ned. | 0, 4 | Pass 4: uppräkning i tre efter kolon; "bokar … bokning" tre gånger. Pass 0: sajten säger "matters that don't fit a form", inte "i en bokning". Menyraden är `fixed` med länken till `#reservations`. |
| `.case-rail` | Namnet står en gång · Stycket tänds i er takt · En mening som saktar in · Priset står större än namnet · Rummet före bokningen · Bokningen sist, knappen hela vägen | Namnet står en gång · Stycket tänds i er takt · En mening som saktar in · Priset står större än namnet · Rummet före bokningen · Knappen fanns där hela tiden | 4 | Följer h3 steg 6. |

## Övergången till priset (ny sektion, placering enligt v1)

| plats | v1 | final | pass som ändrade | skäl |
|---|---|---|---|---|
| kicker | Från exempel till er sida | Från exempel till er sida | ingen | |
| `h2` | Ni har sett arbetet. Här är priset. | Ni har sett arbetet. Här är priset. | ingen | Säljtestet (Hopkins): det en säljare säger mitt emot köparen efter genomgången. Humanizer prövade "två korta satser"-mönstret; behållen eftersom den andra satsen är en ren anvisning, inte en poäng. |
| stycke | Calyx och Hōrai byggde vi med samma steg som ert projekt går igenom. Paketen skiljer sig i vad sidan ska kunna göra. | Calyx och Hōrai byggde vi med samma steg som ert projekt går igenom. Paketen skiljer sig åt i vad sidan ska kunna göra. | 3 | "skiljer sig åt" (idiomatiskt). Innebörden oförändrad. |
| mikrorad | Första steget är ett samtal om er verksamhet. Skriv till kontakt@alunix.se. | Första steget är ett samtal om er verksamhet. Skriv till kontakt@alunix.se. | ingen | Adressen låst, ordagrant. Processens steg 01. |
