# COPY-R6 — showcase-stegen, Calyx + Hōrai

**R2 av detta uppdrag.** Leadens dom på R1: texterna trimmades i längd men lyftes
aldrig i nivå — R1 var mest inventering av vad sajten innehåller ("Varje meny har en
romersk siffra, ett namn och ett pris per gäst.") i stället för VAL + SKÄL, och några
trimningar blev sämre än originalet. Den här versionen skriver om alla elva från
grunden i formen: **mening 1 = valet, som en handling med verb ("Vi satte/lät/lade")
och ett konkret substantiv ur sajten; mening 2 = varför, uttryckt som vad det gör för
besökaren eller ägaren; högst en tredje mening, bara om den bär en ny konkret sak.**
`index.html` är fortfarande orörd — den här filen levererar bara texten.

## 1. Måttstocken (hero / #tes / process / #pris / #kontakt)

Läste hero, tesen, processens sju steg, prisraderna och kontaktrutan. Det som gör dem
bra, i fallande vikt — och det R1 missade:

- **VAL + SKÄL i den ordningen, alltid.** Processen säger aldrig bara vad som finns,
  den säger vad byrån gjorde och varför det spelar roll för kunden: "Vi bygger sidan i
  kod från grunden, utan färdig mall, **så att den laddar snabbt**." Skälet är aldrig
  valfritt eller löst påhängt — det är hälften av meningen.
- **Korta meningar som bär en sak var.** Sällan mer än 15-20 ord; två-tre meningar per
  stycke, aldrig en bisatskedja.
- **Konkreta substantiv, inga honnörsord.** "testadress", "löpnummer", "tangentbord och
  skärmläsare" — inte "kvalitet" eller "användarupplevelse".
- **Verb framför nominaliseringar, aktiv röst framför "står"-kedjor.** "vi bygger",
  "ni rättar", "vi testar" — processen har praktiskt taget inget passivt "står" i hela
  sju steg. R1:s elva strängar hade "står" i nästan var och en; det var själva tecknet
  på att texten beskrev tillstånd i stället för handling.
- **Vi-röst för byråns val, ni/besökaren/man för läsaren.** Ingen blandning inom samma
  stycke.
- **Ingen självreferens, ingen brasklapp** (F-018, se nedan).

## 2. Regler som styr denna text (design-catalogue/FEEDBACK.md)

- **F-016**: all liten "beskrivande" stiltypisk AI-text är förbjuden — en rad ska
  identifiera, differentiera, lokalisera eller möjliggöra en handling, aldrig bara
  beskriva det uppenbara.
- **F-018**: sidan får aldrig berätta vad den strax ska göra. Ingen färdplan, ingen
  brasklapp, ingen uppställning-brasklapp-färdplan-svit. Gäller lika mycket
  "inventering av sajtens delar" som R1 föll i — en rad som bara radar upp vad som
  finns på skärmen ("Fotona står parvis...") är samma fel i en annan skepnad: den
  säger vad läsaren redan ser i bilden bredvid, i stället för att säga varför det ser
  ut så.

## 3. Faktatabell — varje påstående i den FÄRDIGA texten mot källkoden

| # | Påstående | Stämmer? | Belägg |
|---|---|---|---|
| C1 | Rubriken ligger direkt på fotot | Stämmer | `sites/calyx.html:74,79-83` — `<h1>` inne i `.hero-photo` |
| C1 | Utgåvan har ett nummer i hörnet | Stämmer | `sites/calyx.html:85-86` — "No. 042 — Spring Edition", `col-start-9` + `bottom-0` = nedre högra hörnet |
| C2 | Rubrik och brödtext i samma serif | Stämmer | `sites/calyx.html:26,34` — `font-display: Cardo`, body `font-family: Cardo` |
| C2 | Kursiven sköter betoningen | Stämmer | `sites/calyx.html:37,63,79-83,147,158` m.fl. — `.italic-disp` på rubriker/nyckelord genomgående |
| C2 | Etiketter fick ett skrivmaskinslikt mono | Stämmer | `sites/calyx.html:27,35` — `PT Mono`, `.kicker`-klassen (bildtexter, etiketter, nav) |
| C3 | Fotona satt parvis, med en märkning under varje | Stämmer | `sites/calyx.html:120-137` — två `<figure>` sida vid sida, var sin `<figcaption>` |
| C3 | Märkningen ger varje bild ett nummer och en plats | Stämmer | `sites/calyx.html:125-126,132` — "Cmsn. 0211 — Hotel Pigalle, Drottninggatan" / "02 / 14" |
| C4 | Veckans utbud i en lista med löpnummer, namn, pris i högerkant | Stämmer | `sites/calyx.html:154-191` — `.01`–`.04`, `<h3>`, `<p>`, pris `text-right` |
| C5 | En e-postadress står där ett formulär annars hade stått | Stämmer | `sites/calyx.html:267-277` — `mailto:atelier@calyx.se`, inget `<form>`-element i filen |
| C5 | Besökaren beskriver rummet/ljuset, ateljén svarar med säsongens utbud | Stämmer | `sites/calyx.html:269-271` — "You write us about the room, the light... We write back about what is cuttable that week" |
| H1 | Namnet i stora versaler på ett mörkt foto | Stämmer | `sites/horai.html:50,121` — `hero-img` (mörk bild), `<h1>HŌRAI</h1>` |
| H1 | Loggan i menyraden vaknar när fotot rullat förbi | Stämmer | `sites/horai.html:104-111,372-388` — `#logo` döljs medan hero syns, `logo-hidden` tas bort när hero lämnar viewporten |
| H1 | Namnet visas bara en gång | Stämmer | `sites/horai.html:107,121` — `<a id="logo">` (textuellt dolt under hero) + ett enda `<h1>HŌRAI</h1>` i hela filen |
| H2 | Stycket tänds ord för ord i takt med scrollen | Stämmer | `sites/horai.html:146-148,491-506` — `.word`/`.word.lit`, `updateLede()` styrd av `scrollY` |
| H2 | Rubriken i rött, japanskt tecken ovanför | Stämmer | `sites/horai.html:140-141` — `text-lacquer` på både kanji (家) och `<h2>THE HOUSE</h2>` |
| H3 | En enda mening på mörk grund mellan huset och menyerna | Stämmer | `sites/horai.html:157,173-177` — `bg-walnut`, en `<blockquote>`, sektionsordning House → Quote → Menus |
| H3 | Skärps upp mot mitten, tonar ut igen | Stämmer | `sites/horai.html:419-467` — symmetrisk bell-curve på `proximity`, `blur` 12px→0→12px kring viewportens mitt |
| H4 | Romersk siffra per meny | Stämmer | `sites/horai.html:205,227,249` — `I`, `II`, `III` |
| H4 | Priset i rött, större än rätternas namn | Stämmer | `sites/horai.html:207,217` m.fl. — pris `text-[clamp(3.8rem,7vw,6rem)] text-lacquer` vs namn `text-[clamp(2.6rem,4.6vw,4.4rem)] text-walnut` |
| H4 | **Utan à la carte väljer man en hel meny** | **Stämmer, verifierat** | `sites/horai.html:147` — husets egen text: *"The menu changes weekly. **There is no à la carte.**"* — explicit uttalande i sajtens brödtext, inte en slutsats jag drog själv |
| H4 | Dryckerna fick en egen grön ton | Stämmer | `sites/horai.html:219,241,263` — `+ SAKE`/`+ PAIRING`-raden i `text-jade` |
| H5 | Matsalen som bild över hela bredden, strax före bokningen | Stämmer | `sites/horai.html:285-303` (THE ROOM) direkt före `:305-346` (RESERVATIONS) — sektionsordningen i filen |
| H5 | Texten direkt på fotot, mörk toning från vänster | Stämmer | `sites/horai.html:288,294-299` — `bg-gradient-to-r from-walnut/85 via-walnut/45 to-walnut/10` (mörkast vänster), text i samma `<div>` som bilden |
| H6 | Bokningsknappen ligger kvar i menyraden hela vägen ned | Stämmer | `sites/horai.html:104-108` — `<header class="fixed top-0...">`, RESERVATIONS-länk, aldrig `position:absolute`/villkorad bort |
| H6 | Veckans platser släpps på måndagar | Stämmer | `sites/horai.html:314-315` — "We release each week's seats every Monday at noon Stockholm time." |

Leadens specifika fråga — **finns à la carte på Hōrai eller inte?** — Nej: filen har
tre fasta menyer (I/II/III) och en uttrycklig rad i husets egen text som säger att det
inte finns någon à la carte (`sites/horai.html:147`). Påståendet "Utan à la carte
väljer man en hel meny" är alltså inte en tolkning, det citerar sajtens eget språk.

## 4. De tre passen — körda som Skill-anrop, med konkret loggning per sträng

### Pass 1 — `Skill(copywriting)`: VAL + SKÄL-strukturen, från grunden

R1:s fel var strukturellt, inte bara ett längdproblem, så detta pass skrev om alla elva
`p` från noll enligt formen (verb+substantiv, sedan skäl för besökare/ägare), i ett
första utkast som ännu inte var kortat. Konkret, per sträng (utkastet, innan
copy-editing kortade det):

- **C1**: Bytte "Vi byggde Calyx som ett tidskriftsnummer, med utgåvan i hörnet..." mot
  "Vi valde att lägga rubriken direkt på fotot, och vi gav utgåvan ett eget nummer i
  det övre hörnet... Anledningen är att en bukett är något man vill se stort och nära,
  hellre än gömd bakom en rubrikrad."
- **C2**: Bytte inventeringen (tre påståenden om typsnitt i rad) mot "Vi valde att
  sätta rubrik och brödtext i samma klassiska serif... Om vi hade lagt till ett andra
  rubriktypsnitt hade det dragit åt reklam, så i stället fick etiketterna ett tunt
  skrivmaskinslikt typsnitt."
- **C3**: Bytte "Fotona står parvis med en liten märkning..." (ingen skälmening alls i
  R1) mot "Vi valde att sätta fotona parvis i stället för ensamma... Anledningen är
  att märkningen ger varje bild ett nummer och en plats, vilket gör att paret läses
  som dokumentation snarare än bara stämning." — R3 hade i R1 inget skäl över huvud
  taget; det är den tydligaste enskilda bristen leaden pekade på.
- **C4**: Behöll kärnan (redan nära rätt form i R1) men skrev om till explicit
  val-först: "Vi valde att sätta veckans utbud i en lista i stället för i kort..."
- **C5**: Bytte "Sidan slutar med hur en beställning går till..." (inventering av
  sidans disposition, F-018-doft) mot "Vi valde att sätta en e-postadress på den plats
  där ett vanligt bokningsformulär annars hade stått. Anledningen är att besökaren då
  kan beskriva rummet och ljuset med sina egna ord..."
- **H1**: Bytte "Första skärmen är ett mörkt foto med namnet..." (inventering) mot
  "Vi valde att skriva ut namnet bara en enda gång... Anledningen är att loggan i
  menyraden vaknar till liv först när fotot har rullat förbi, så att besökaren aldrig
  behöver möta namnet två gånger på samma skärm." — R1:s skäl var en ren upprepning
  ("står bara en gång på första skärmen" efter att redan sagt "namnet ... i hörnet");
  nu är skälet en annan, faktisk mekanism (loggan tar över).
- **H2**: Bytte till "Vi valde att låta stycket om huset tändas ord för ord i den takt
  som besökaren själv scrollar i, vilket gör att läsningen blir långsam med flit..."
- **H3**: Bytte till "Vi valde att lägga en enda mening på en mörk botten... vilket gör
  att farten i läsningen sjunker innan priserna kommer."
- **H4**: Bytte den rena inventeringen ("Varje meny har en romersk siffra, ett namn och
  ett pris per gäst.") mot "Vi valde att ge varje meny en romersk siffra, och vi satte
  priset i rött och i ett större typsnitt än rätternas eget namn. Eftersom det inte
  finns någon à la carte måste man välja en hel meny, så blicken ska landa på priset
  först och inte på namnet."
- **H5**: Bytte till "Vi valde att lägga matsalen som en bild över hela bredden, strax
  innan bokningssektionen kommer... så att den som ska boka får se rummet innan hen
  bestämmer sig."
- **H6**: Bytte till "Vi valde att låta bokningsknappen ligga kvar i menyraden hela
  vägen ner genom sidan... Anledningen är att den som inte orkar läsa klart ändå alltid
  har knappen inom räckhåll."

### Pass 2 — `Skill(copy-editing)`, sju svepen

Clarity/Voice höll efter pass 1. Specificity-svepet gjorde det tunga arbetet: strök
"Vi valde att" och "Anledningen är att" ur alla elva (utfyllnad som inte bär mening,
samma familj som humanizerns punkt 12) och lät verbet självt bära handlingen
("Vi satte", "Vi lät", "Vi lade"). Konkret per sträng, utkast → kortad version:

- **C1** (216→148 tecken): "Vi valde att lägga...Anledningen är att en bukett är något
  man vill se stort och nära, hellre än gömd bakom en rubrikrad" → "Vi lade rubriken
  direkt på fotot och gav utgåvan ett nummer i hörnet, som ett magasin. En bukett vill
  man se stor och nära, inte bakom en rubrikrad."
- **C2** (232→174): strök "Om vi hade lagt till... hade det dragit åt reklam" →
  "Ett andra typsnitt hade dragit åt reklam" (samma påstående, kausal bisats blir
  huvudsats).
- **C3** (238→155): strök "vilket gör att" + "snarare än bara stämning" (svag
  motsatspar, So What-svepet bedömde att "läses som dokumentation" bar poängen själv).
- **C4** (223→175): "i stället för i kort" → struket (redundant med nästa mening som
  redan kontrasterar mot "ett rutnät med kort"); "en enda rad" → "en rad".
- **C5** (233→152): "på den plats där ett vanligt bokningsformulär annars hade stått"
  → "där ett formulär annars hade stått" (Specificity-svepet: "vanligt
  bokningsformulär" var en dubblering, sajten har inget bokningsformulär att
  förväxla det med); "med sina egna ord" → "med egna ord".
- **H1** (243→164): strök "två gånger på samma skärm" → "namnet bara en gång"
  (Clarity: föregående mening etablerar redan "över det mörka fotot", "samma skärm"
  var överflödigt).
- **H2** (233→166): "i den takt som besökaren själv scrollar i, vilket gör att
  läsningen blir långsam med flit, ungefär som när någon berättar högt" → "i takt med
  scrollen, långsamt som när någon berättar" (tre bisatser till en).
- **H3** (245→150 vid detta läge): "Meningen är suddig ända tills den når mitten av
  skärmen, skärps upp där, och tonar sedan ut igen, vilket gör att farten..." →
  "Den skärps upp mot mitten och tonar ut igen, så farten sjunker..." (fyra
  bisatser till två huvudsatser).
- **H4** (261→197): "Eftersom det inte finns någon à la carte måste man välja en hel
  meny" → "Utan à la carte väljer man en hel meny" (bisats till huvudsats, samma
  påstående).
- **H5** (232→171): "strax innan bokningssektionen kommer" → "strax före bokningen"
  (Specificity: "bokningssektionen" är sidans egen struktur, F-018-doft; "bokningen"
  är handlingen besökaren gör).
- **H6** (211→165): "hela vägen ner genom sidan" → "hela vägen ned" (redundant
  "genom sidan"); "släpps varje måndag" → "släppas på måndagar".

### Pass 3 — `Skill(humanizer-svenska)`: register och läsbarhet högt

Skannade de sju svepens resultat mot mönsterlistan (nominalisering, anglicism,
hedging, kopulaundvikande, treuppräkning). Inga AI-mönster kvar — men två ord bar fel
register när jag läste dem högt bredvid processtextens ordval:

- **C2**: "ett skrivmaskinsmono" (sammansatt substantiv, låter som ett produktnamn) →
  **"ett skrivmaskinslikt mono"** (adjektiv + substantiv, samma böjningsmönster som
  processtextens egna sammansättningar, t.ex. "en testadress"). +6 tecken (169→175),
  fortfarande inom målet.
- **H3**: "mörk botten" (botten = golv/nedre gräns, fel bild för en bakgrundsfärg) →
  **"mörk grund"** (idiomatiskt för bakgrund/fond på svenska; matchar även hur
  originaltexten på sidan redan uttryckte samma sak). −1 tecken (150→149).

Alla nio övriga strängar lästes högt bredvid processtextens sju steg och höll måttet
utan ändring i detta pass. Sista AI-testet (skillens egen fråga): *"Vad avslöjar att
det här fortfarande är AI-genererat?"* — inget kvarstående mönster; meningarna
varierar i längd, ingen hedging, inget "står"-kedja (högst en gång per `p`, se
teckenkontrollen).

## 5. Per sträng — original på sidan → färdig text

### Calyx

**1. h3**
- Original: `Fotot bär rubriken`
- Färdig: **`Fotot får göra jobbet`**
- Ändrat av: pass 1 (bytte beskrivning mot ett litet ställningstagande — fotot gör
  ett jobb, i stället för att bara ange var rubriken sitter).

**1. p**
- Original: "Vi byggde Calyx som ett tidskriftsnummer, med utgåvan i hörnet och
  rubriken direkt på fotot. En bukett vill man röra vid, och på en skärm kommer ett
  stort foto närmast."
- Färdig: **"Vi lade rubriken direkt på fotot och gav utgåvan ett nummer i hörnet,
  som ett magasin. En bukett vill man se stor och nära, inte bakom en rubrik."**
- Ändrat av: pass 1 satte om till verb-först (vi lade / vi gav) och gjorde skälet
  explicit ("inte bakom en rubrik" i stället för det löst hängande "på en skärm
  kommer ett stort foto närmast"); pass 2 kortade från 216 till 148 tecken; pass 3
  bytte "röra vid" mot "se stor och nära" för att undvika ett taktilt löfte
  ("röra vid") som en skärm inte kan hålla.

**2. h3**
- Original: `En serif för allt man läser`
- Färdig: **`En serif, inget mer`**
- Ändrat av: pass 1/2 — tightare, "inget mer" bär restriktionen (medvetet val bort
  från ett andra typsnitt) som p-texten sedan förklarar varför.

**2. p**
- Original: "Rubriker och brödtext står i samma klassiska serif, och kursiven sköter
  betoningen. Ett andra rubriktypsnitt hade dragit åt reklam. Det enda andra
  typsnittet är skrivmaskinslikt och används till etiketter och bildtexter, som
  anteckningar i marginalen."
- Färdig: **"Vi satte rubrik och brödtext i samma serif och lät kursiven sköta
  betoningen. Ett andra typsnitt hade dragit åt reklam, så etiketter fick ett
  skrivmaskinslikt mono i stället."**
- Ändrat av: pass 1 gjorde "vi satte...lät" till huvudverb i stället för passivt
  "står"; pass 2 slog ihop tre meningar till två och strök "som anteckningar i
  marginalen" (en bild som inte bar ny fakta); pass 3 rättade "skrivmaskinsmono"
  (mellansteg) till "skrivmaskinslikt mono".

**3. h3**
- Original: `Färgen finns redan i bilderna`
- Färdig: **`Bilderna kommer i par`**
- Ändrat av: pass 1 — bytte ämne till det Anton faktiskt pekat ut för steg 3
  (fotoparet med märkningarna, inte färgen/rostton som R1:s originaltext råkade handla
  om).

**3. p**
- Original: "Fotona står parvis med en liten märkning under varje, som i en katalog.
  Grunden är varmt, nästan vitt papper med ett svagt korn. Sidan har en enda egen
  färg, en rostton, och den dyker upp först längre ned."
- Färdig: **"Vi satte fotona parvis och gav paret en liten märkning under, som i en
  katalog. Märkningen ger bilderna nummer och plats, så paret läses som
  dokumentation."**
- Ändrat av: pass 1 lade till det skäl som helt saknades i R1 ("så paret läses som
  dokumentation" — leadens exakta exempel på en tom sträng); pass 2 kortade och
  strök en jämförelse utan bärkraft ("inte bara stämning"); ämnet fokuserades till
  bara fotoparet (färg/papper/korn hörde till en annan sak än det utpekade steget
  och gjorde strängen till en inventering).

**4. h3**
- Original/Färdig: **`Utbudet som prislista`** (oförändrad — bär redan en poäng,
  explicit undantagen av leaden).

**4. p**
- Original: "Veckans utbud står i en lista med löpnummer, namn, en kort beskrivning
  och priset till höger. Kort i ett rutnät hade krävt ett nytt foto av varje bukett
  varje vecka. Med en lista räcker det att skriva om en rad."
- Färdig: **"Vi satte veckans utbud i en lista med löpnummer, namn och pris i
  högerkant. Ett rutnät med kort hade krävt nytt foto varje vecka; med en lista
  räcker det att skriva om en rad."**
- Ändrat av: pass 1 bytte "står" mot "vi satte"; pass 2 slog ihop de två sista
  meningarna med semikolon och behöll leadens uttryckligen godkända fras ordagrant
  ("med en lista räcker det att skriva om en rad"); pass 3: ingen ändring, redan
  naturlig.

**5. h3**
- Original/Färdig: **`Ett mejl räcker`** (oförändrad — explicit undantagen).

**5. p**
- Original: "Sidan slutar med hur en beställning går till. Besökaren skriver om
  rummet och ljuset, och ateljén svarar med vad som finns den veckan. Sådant passar
  dåligt i formulärfält, så vi satte en e-postadress där formuläret annars hade
  stått."
- Färdig: **"Vi satte en e-postadress där ett formulär annars hade stått. Besökaren
  beskriver rummet och ljuset med egna ord, och ateljén svarar med säsongens
  utbud."**
- Ändrat av: pass 1 strök öppningen "Sidan slutar med..." (F-018: beskriver sidans
  egen disposition, inte verksamheten) och gjorde valet till första mening; pass 2
  kortade "vad som finns den veckan" till "säsongens utbud" och tog bort den sist
  hängande formulärfält-motiveringen som redan låg implicit i "med egna ord";
  pass 3: ingen ändring.

### Hōrai

**1. h3**
- Original: `Namnet står en gång`
- Färdig: **`Ett namn, en gång`**
- Ändrat av: pass 1/3 — bytte bort "står" (passivt tillstånd) mot en kort,
  konstaterande form utan verb, samma register som "Ett mejl räcker".

**1. p**
- Original: "Första skärmen är ett mörkt foto med namnet i stora versaler och
  öppettiderna i hörnet. Loggan i menyraden tänds när bilden rullat förbi, så namnet
  står bara en gång på första skärmen."
- Färdig: **"Vi skrev namnet en enda gång, i stora versaler över det mörka fotot.
  Loggan i menyraden vaknar först när fotot rullat förbi, så besökaren möter namnet
  bara en gång."**
- Ändrat av: pass 1 strök "Första skärmen är..." (inventering av vad som visas) och
  öppettiderna (inte del av det utpekade ämnet "namnet på det mörka fotot") till
  förmån för "Vi skrev namnet..." som första handling; pass 2 tog bort en upprepning
  ("på första skärmen" två gånger i originalet); pass 3: bytte "tänds" mot "vaknar"
  för variation (samma faktapåstående, se H2 som redan använder "tänds").

**2. h3**
- Original/Färdig: **`Stycket tänds i er takt`** (oförändrad — bär redan en poäng:
  besökaren styr tempot).

**2. p**
- Original: "Stycket om huset börjar nästan osynligt och tänds ord för ord medan ni
  scrollar. Vi ville att det skulle läsas långsamt, som när någon berättar. Rubriken
  står kvar i rött, med ett japanskt tecken ovanför som en stämpel."
- Färdig: **"Vi lät stycket om huset tändas ord för ord i takt med scrollen, långsamt
  som när någon berättar. Rubriken står i rött, med ett japanskt tecken ovanför som
  en stämpel."**
- Ändrat av: pass 1 gjorde "vi lät... tändas" till huvudverb i stället för att
  beskriva stycket som subjekt ("stycket... börjar... tänds"); pass 2 strök "Vi
  ville att det skulle" (en avsikt bakom avsikten, ren utfyllnad) och slog ihop med
  "långsamt som när någon berättar" i samma sats.

**3. h3**
- Original/Färdig: **`En mening som saktar in`** (oförändrad — bär redan poängen:
  meningens funktion är att bromsa).

**3. p**
- Original: "Mellan huset och menyerna står en enda mening på mörk grund. Den är
  suddig tills den når mitten av skärmen och suddas ut igen när ni scrollar vidare.
  Den står där för att bromsa läsningen före menyer och priser."
- Färdig: **"Vi lade en enda mening på mörk grund mellan huset och menyerna. Den
  skärps upp mot mitten och tonar ut igen, så farten sjunker innan priserna
  kommer."**
- Ändrat av: pass 1 bytte "står" (använt två gånger i originalet) mot "vi lade" som
  förstamening; pass 2 komprimerade tre meningar till två och bytte "suddig tills...
  och suddas ut igen" mot en rörelseriktning ("skärps upp... tonar ut") som är
  samma mekanik men aktivt uttryckt; pass 3 rättade "mörk botten" (mellansteg) till
  "mörk grund".

**4. h3**
- Original/Färdig: **`Priset står större än namnet`** (oförändrad — explicit
  undantagen; enda kvarvarande "står" i hela uppsättningen, i en h3 där det
  fungerar som ett rakt sakpåstående).

**4. p**
- Original: "Varje meny har en romersk siffra, ett namn och ett pris per gäst.
  Priset står i rött, större än namnet. Utan à la carte väljer man en hel meny och
  letar först efter priset. Dryckerna har en egen grön ton."
- Färdig: **"Vi gav varje meny en romersk siffra och satte priset i rött, större än
  rätternas namn. Utan à la carte väljer man en hel meny, så blicken ska landa på
  priset först. Dryckerna fick en egen grön ton."**
- Ändrat av: pass 1 bytte "har"/"står" (tillstånd) mot "vi gav"/"vi satte" (val);
  pass 2 slog ihop mening 1+2 och gjorde "letar först efter priset" till en tydligare
  konsekvens ("blicken ska landa på priset först"); à la carte-faktat kontrollerades
  explicit mot `sites/horai.html:147` denna omgång (se faktatabellen) — det stod
  redan i R1 men saknade fil:rad-belägg tills nu.

**5. h3**
- Original/Färdig: **`Rummet före bokningen`** (oförändrad — bär redan poängen:
  sekvensen är avsiktlig).

**5. p**
- Original: "Precis före bokningen kommer matsalen, i en bild över hela bredden.
  Texten står direkt på fotot, med en mörk toning från vänster så att den går att
  läsa. Den som ska boka vill se var den ska sitta."
- Färdig: **"Vi lade matsalen som en bild över hela bredden, strax före bokningen,
  med texten direkt på fotot. En mörk toning från vänster håller texten läsbar innan
  man bestämmer sig."**
- Ändrat av: pass 1 gjorde "vi lade" till förstamening i stället för att öppna med
  "Precis före bokningen kommer..." (satsen startade på fel subjekt, matsalen som
  agent snarare än byråns val); pass 2 kortade "så att den går att läsa" till
  "håller texten läsbar" och strök "vill se var den ska sitta" (en gissning om
  besökarens tanke som inte bar ny fakta, ersatt av "innan man bestämmer sig" som
  kopplar bilden till handlingen som följer, bokningen).

**6. h3**
- Original/Färdig: **`Knappen fanns där hela tiden`** (oförändrad — explicit
  undantagen).

**6. p**
- Original: "Sist står hur man bokar och när veckans platser släpps. Det som inte
  passar i ett formulär får en egen e-postadress. Den som inte orkar läsa klart har
  haft bokningsknappen i menyraden hela vägen ned."
- Färdig: **"Vi lät bokningsknappen ligga kvar i menyraden hela vägen ned, och satte
  veckans platser till att släppas på måndagar. Den som inte orkar läsa klart når
  knappen ändå."**
- Ändrat av: pass 1 strök öppningen "Sist står hur man bokar..." (F-018: beskriver
  sidans egen disposition/ordning, "sist" är en platsangivelse på sidan, inte ett
  faktum om Hōrai) och gjorde knappens placering till det aktiva valet; pass 2
  strök e-postadress-sidopunkten (redan täckt av Calyx steg 5 i samma showcase,
  blev en tredje mening utan ny konkret sak här) och kortade slutklausulen.

## 6. Teckenkontroll (python)

```
=== CALYX ===
h3 [ 21] OK: Fotot får göra jobbet
p  [148] OK IN-TARGET (stå-count=0): Vi lade rubriken direkt på fotot och gav utgåvan ett nummer i hörnet, som ett magasin. En bukett vill man se stor och nära, inte bakom en rubrik.

h3 [ 19] OK: En serif, inget mer
p  [174] OK IN-TARGET (stå-count=0): Vi satte rubrik och brödtext i samma serif och lät kursiven sköta betoningen. Ett andra typsnitt hade dragit åt reklam, så etiketter fick ett skrivmaskinslikt mono i stället.

h3 [ 21] OK: Bilderna kommer i par
p  [155] OK IN-TARGET (stå-count=0): Vi satte fotona parvis och gav paret en liten märkning under, som i en katalog. Märkningen ger bilderna nummer och plats, så paret läses som dokumentation.

h3 [ 21] OK: Utbudet som prislista
p  [175] OK IN-TARGET (stå-count=0): Vi satte veckans utbud i en lista med löpnummer, namn och pris i högerkant. Ett rutnät med kort hade krävt nytt foto varje vecka; med en lista räcker det att skriva om en rad.

h3 [ 15] OK: Ett mejl räcker
p  [152] OK IN-TARGET (stå-count=1): Vi satte en e-postadress där ett formulär annars hade stått. Besökaren beskriver rummet och ljuset med egna ord, och ateljén svarar med säsongens utbud.

=== HORAI ===
h3 [ 17] OK: Ett namn, en gång
p  [164] OK IN-TARGET (stå-count=0): Vi skrev namnet en enda gång, i stora versaler över det mörka fotot. Loggan i menyraden vaknar först när fotot rullat förbi, så besökaren möter namnet bara en gång.

h3 [ 23] OK: Stycket tänds i er takt
p  [166] OK IN-TARGET (stå-count=1): Vi lät stycket om huset tändas ord för ord i takt med scrollen, långsamt som när någon berättar. Rubriken står i rött, med ett japanskt tecken ovanför som en stämpel.

h3 [ 23] OK: En mening som saktar in
p  [149] OK IN-TARGET (stå-count=0): Vi lade en enda mening på mörk grund mellan huset och menyerna. Den skärps upp mot mitten och tonar ut igen, så farten sjunker innan priserna kommer.

h3 [ 28] OK: Priset står större än namnet
p  [197] OK max-200 (stå-count=0): Vi gav varje meny en romersk siffra och satte priset i rött, större än rätternas namn. Utan à la carte väljer man en hel meny, så blicken ska landa på priset först. Dryckerna fick en egen grön ton.

h3 [ 21] OK: Rummet före bokningen
p  [171] OK IN-TARGET (stå-count=0): Vi lade matsalen som en bild över hela bredden, strax före bokningen, med texten direkt på fotot. En mörk toning från vänster håller texten läsbar innan man bestämmer sig.

h3 [ 28] OK: Knappen fanns där hela tiden
p  [165] OK IN-TARGET (stå-count=0): Vi lät bokningsknappen ligga kvar i menyraden hela vägen ned, och satte veckans platser till att släppas på måndagar. Den som inte orkar läsa klart når knappen ändå.
```

Alla elva `h3` ≤30 tecken. Tio av elva `p` ligger i målintervallet 120-180 tecken;
Hōrai steg 4 ligger på 197 (inom taket på 200) eftersom det bär tre verifierade
sakuppgifter (siffra+färg+storlek, à la carte, dryckernas grönton) i stället för en
uppfylld tredje mening utan ny fakta. "Står" förekommer högst en gång per `p` (noll i
åtta av elva), plus en gång i den explicit undantagna h3 "Priset står större än
namnet". Inget em-dash i någon sträng. Ingen sträng inventerar sajtens delar eller
öppnar med "Sidan..."/"Första skärmen är...".

## 7. Slutliga strängar

```json
{"calyx":[{"h3":"Fotot får göra jobbet","p":"Vi lade rubriken direkt på fotot och gav utgåvan ett nummer i hörnet, som ett magasin. En bukett vill man se stor och nära, inte bakom en rubrik."},{"h3":"En serif, inget mer","p":"Vi satte rubrik och brödtext i samma serif och lät kursiven sköta betoningen. Ett andra typsnitt hade dragit åt reklam, så etiketter fick ett skrivmaskinslikt mono i stället."},{"h3":"Bilderna kommer i par","p":"Vi satte fotona parvis och gav paret en liten märkning under, som i en katalog. Märkningen ger bilderna nummer och plats, så paret läses som dokumentation."},{"h3":"Utbudet som prislista","p":"Vi satte veckans utbud i en lista med löpnummer, namn och pris i högerkant. Ett rutnät med kort hade krävt nytt foto varje vecka; med en lista räcker det att skriva om en rad."},{"h3":"Ett mejl räcker","p":"Vi satte en e-postadress där ett formulär annars hade stått. Besökaren beskriver rummet och ljuset med egna ord, och ateljén svarar med säsongens utbud."}],"horai":[{"h3":"Ett namn, en gång","p":"Vi skrev namnet en enda gång, i stora versaler över det mörka fotot. Loggan i menyraden vaknar först när fotot rullat förbi, så besökaren möter namnet bara en gång."},{"h3":"Stycket tänds i er takt","p":"Vi lät stycket om huset tändas ord för ord i takt med scrollen, långsamt som när någon berättar. Rubriken står i rött, med ett japanskt tecken ovanför som en stämpel."},{"h3":"En mening som saktar in","p":"Vi lade en enda mening på mörk grund mellan huset och menyerna. Den skärps upp mot mitten och tonar ut igen, så farten sjunker innan priserna kommer."},{"h3":"Priset står större än namnet","p":"Vi gav varje meny en romersk siffra och satte priset i rött, större än rätternas namn. Utan à la carte väljer man en hel meny, så blicken ska landa på priset först. Dryckerna fick en egen grön ton."},{"h3":"Rummet före bokningen","p":"Vi lade matsalen som en bild över hela bredden, strax före bokningen, med texten direkt på fotot. En mörk toning från vänster håller texten läsbar innan man bestämmer sig."},{"h3":"Knappen fanns där hela tiden","p":"Vi lät bokningsknappen ligga kvar i menyraden hela vägen ned, och satte veckans platser till att släppas på måndagar. Den som inte orkar läsa klart når knappen ändå."}]}
```

## 8. Leadens slutjustering (efter agentens tre pass) + eget `Skill(humanizer-svenska)`-pass

Agentens R2 lyfte formen (val + skäl), men leaden läste om varje sträng mot sajterna och
processtexten och ändrade sju:

| Steg | Ändring | Varför |
|---|---|---|
| Calyx 1 | "En bukett vill man se stor och nära, inte bakom en rubrik" → "En bukett säljer på hur den ser ut, så fotot fick nästan hela första skärmen" | Rubriken ligger PÅ fotot, så "inte bakom en rubrik" motsade första meningen. Hero är `h-[88vh]` (calyx.html:74), därav "nästan hela". |
| Calyx 2 | "Ett andra typsnitt hade dragit åt reklam, så etiketter fick ett … mono" → "Ett andra rubriktypsnitt hade dragit åt reklam. Bara etiketterna fick ett eget, skrivmaskinslikt typsnitt." | Logiken motsade sig själv (inget andra typsnitt → så fick de ett andra). Originalets "rubriktypsnitt" var det precisa ordet. |
| Calyx 3 | "Märkningen ger bilderna nummer och plats, så paret läses som dokumentation" → "…en märkning med uppdragets nummer och adress. Då läses de som beställningar ateljén har levererat." | Konkret skäl i stället för abstrakt "dokumentation". Belägg calyx.html:124, 131 ("Cmsn. 0211 — Hotel Pigalle, Drottninggatan"). |
| Calyx 4, 5, Hōrai 3, 5 | Öppningen varierad (inte "Vi satte/lade" i varje p) | Elva p med samma öppning är ett strukturellt AI-tecken. |
| Calyx 5 | "säsongens utbud" → "vad som finns den veckan" | Sajten säger "what is cuttable that week" (calyx.html:268), inte säsong. |
| Hōrai 1 | "så besökaren möter namnet bara en gång" → "Annars hade namnet stått två gånger på samma skärm." | Tredubbling (h3 + "en enda gång" + "bara en gång"). Nu ett skäl. |
| Hōrai 4 | "större än rätternas namn" → "större än menyns namn"; dryckesmeningen struken | Faktafel: priset jämförs med menyns namn (horai.html:205–207, SANSAI), inte rätternas. Dryckesmeningen var inventering utan skäl. |
| Hōrai 6 | "satte veckans platser till att släppas på måndagar" struken → "Den som bestämt sig redan vid första menyn ska inte behöva leta efter den." | Släpptiden är restaurangens regel, inte vårt designval; skälet saknades. |

`Skill(humanizer-svenska)` på slutversionen: negativ parallellism hittad och borttagen i två
utkast ("som gjorda beställningar, inte som dekor", "stort en gång, inte smått två gånger").
AI-testet: kvar är att sju av elva börjar med "Vi", vilket matchar processtextens egen vi-röst.

```json
{"calyx":[{"h3":"Fotot får göra jobbet","p":"Vi lade rubriken direkt på fotot och satte utgåvans nummer i hörnet, som på ett magasin. En bukett säljer på hur den ser ut, så fotot fick nästan hela första skärmen."},{"h3":"En serif, inget mer","p":"Rubriker och brödtext går i samma serif, och kursiven sköter betoningen. Ett andra rubriktypsnitt hade dragit åt reklam. Bara etiketterna fick ett eget, skrivmaskinslikt typsnitt."},{"h3":"Bilderna kommer i par","p":"Vi satte fotona parvis och gav varje bild en märkning med uppdragets nummer och adress. Då läses de som beställningar ateljén har levererat."},{"h3":"Utbudet som prislista","p":"Veckans utbud blev en lista med löpnummer, namn och pris i högerkant. Ett rutnät med kort hade krävt nytt foto varje vecka. Med en lista räcker det att skriva om en rad."},{"h3":"Ett mejl räcker","p":"Där ett formulär brukar stå satte vi en e-postadress. Besökaren skriver om rummet och ljuset med egna ord, och ateljén svarar med vad som finns den veckan."}],"horai":[{"h3":"Ett namn, en gång","p":"Vi satte namnet i stora versaler över det mörka fotot och lät loggan i menyraden vänta tills fotot rullat förbi. Annars hade namnet stått två gånger på samma skärm."},{"h3":"Stycket tänds i er takt","p":"Vi lät stycket om huset tändas ord för ord medan ni scrollar, så att det läses långsamt, som när någon berättar. Rubriken är röd, med ett japanskt tecken ovanför som en stämpel."},{"h3":"En mening som saktar in","p":"Mellan huset och menyerna lade vi en enda mening på mörk grund. Den är skarp bara mitt på skärmen och suddas ut igen, så farten sjunker innan priserna kommer."},{"h3":"Priset står större än namnet","p":"Vi gav varje meny en romersk siffra och satte priset i rött, större än menyns namn. Utan à la carte väljer man en hel meny och letar först efter priset."},{"h3":"Rummet före bokningen","p":"Matsalen fick en bild över hela bredden, strax före bokningen, med texten direkt på fotot och en mörk toning från vänster. Den som ska boka vill se var den ska sitta."},{"h3":"Knappen fanns där hela tiden","p":"Vi lät bokningsknappen ligga kvar i menyraden hela vägen ned. Den som bestämt sig redan vid första menyn ska inte behöva leta efter den."}]}
```
