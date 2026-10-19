# COPY-GATE — V3c, r9

Copy-agent, 2026-09-17. Ram: `PROCESS-UNDERLAG.md` § 3 (copy v1) och § 4 (antagandena
gäller; ingenting som kräver Antons ja är inskrivet). Endast strängar redigerade, med
kirurgiska `Edit`-anrop. Markup, CSS, JS och attribut orörda.

Fem pass i ordning: pass 0 UX-copy → `Skill(copywriting)` → `Skill(copy-editing)` →
`Skill(humanizer-svenska)` (sist av de tre skills) → pass 5 (maskinellt plus hand).

## Kontroll

| Kontroll | Utfall |
|---|---|
| Låst copy, byte för byte före/efter | **15/15 identiska** |
| Tankstreck i synlig text (U+2010–U+2015, U+2212, U+2043, U+FE58, U+FE63, U+FF0D) | **0** |
| Nya tal | **0.** Talmängden identisk före/efter: `01`–`07`, `320`, `768`, `1440`, `16:9`, `96`, `26 900`, `38 900` |
| `deslop.py`, per sektion och hel sida | 5/5 CLEAN (tes, pris, liggare, process, principer, hela sidan) |
| Svenska tvillingar, 8 kategorier / 63 mönster | 0 träffar (enda träffen `sajt` är `exempelsajterna`, projektets egen term ur `PRODUCT.md`) |
| `jag` i synlig text | 0 |
| Namnet Klova | 0 |
| Meningar > 25 ord | 0 (före: 1) |
| Struktur efter redigering | 7 `li[data-step]`, 7 `.process-p`, 7 `.process-note`, HTTP 200 |

## Ändrade strängar

| Före | Efter | Pass | Skäl |
|---|---|---|---|
| Skärmen möter besökaren före texten. Fram till dess bär layout och bild hela argumentet. | Skärmen möter besökaren före texten. **Innan ett ord är läst** bär layout och bild hela argumentet. | 0, 3, 4 | "Fram till dess" saknade syftning: första meningen ger ingen tidpunkt. Samma påstående, nu med utsatt hållpunkt. |
| Identitet och formspråk **hämtat** ur er verksamhet. | Identitet och formspråk **hämtade** ur er verksamhet. | 0, 3 | Kongruensfel. Två samordnade substantiv kräver pluralform. |
| … byggda i samma steg som **sajten** och skötta efter lansering. | … byggda i samma steg som **sidan** och skötta efter lansering. | 3, 4 | Registerbrott: sidan säger "sidan" och "webbplats" överallt annars. Anglicism i en byråröst som annars är svensk. |
| … Det dokumentet är grunden för allt som följer, **och ni får det**. | … **Det ni får** är grunden för allt som följer. | 0, 2 | UX: det enda läsaren behöver ("ni får det") låg sist som bisats. Nu först. 14 ord → 8. Båda fakta kvar. |
| Vi ritar **sidans struktur innan vi ritar dess utseende** … att göra**,** och i vilken ordning … dator**, så att mobilen inte blir en efterhandskonstruktion.** | Vi ritar **strukturen innan vi formger sidan** … att göra och i vilken ordning … dator**. Mobilen lägger vi inte till sist.** | 0, 2, 3, 4 | "dess utseende" stel genitiv; "formger" knyter steget till 03 som öppnar med samma verb. Serialkomma bort (ej svenskt bruk). "efterhandskonstruktion" är jargong med en annan vardagsbetydelse; ersatt med rak sats som bryter styckeblocket. Samma löfte. |
| 320, 768 och 1440, de tre bredder varje sida verifieras vid. | 320, 768 och 1440. **Varje sida verifieras vid alla tre.** | 0, 3, 4 | Strandad preposition, läste inte som etikett. Passiv behållen: marginalrösten är agentlös ("Inget ritas", "Revisionsfältet fylls"). |
| **Med strukturen på plats** formger vi sidan: … rytm **hämtas** ur er verksamhet … **testadress som ni öppnar i er egen webbläsare, på er egen telefon, så att ni ser det som era kunder kommer att se det.** Ni lämnar synpunkter, vi justerar**,** och ni godkänner innan vi bygger **vidare**. | **När strukturen är klar** formger vi sidan: … rytm **hämtar vi** ur er verksamhet … **testadress. Ni öppnar den i er egen webbläsare, på er telefon, och ser sidan som era kunder kommer att se den.** Ni lämnar synpunkter, vi justerar och ni godkänner innan vi bygger. | 0, 2, 3, 4 | Passiv → aktiv. "på plats" förekom tre gånger på sidan; en borttagen. Meningen delad (5-ordsmening bryter blocket). "er egen" två gånger → en. Serialkomma bort. "bygger vidare" här krockade med steg 04:s "bygga vidare på" i en annan betydelse; "innan vi bygger" säger samma sak och matchar liggarens rad 01. |
| 16:9, öppningen …, **proportionen bestämd innan bilden finns.** | 16:9, öppningen … **. Proportionen bestäms innan bilden finns.** | 0, 3 | Tre appositioner i rad, den sista utan verb. Nu en sats med verb. |
| … för de tre bredderna vi planerade **för**. Sidan ska ladda snabbt, fungera med tangentbord och skärmläsare **och gå att bygga vidare på**. … i ett innehållssystem**;** vi visar hur. … samma tekniska nivå som **sajten**. | … för de tre bredderna **från planeringen**. Sidan ska ladda snabbt och fungera med tangentbord och skärmläsare. … i ett innehållssystem**. Vi visar hur.** … samma tekniska nivå som **resten av sidan**. | 0, 2, 3, 4 | Känd skavank: "bygga vidare på" två gånger. Den första stryks; P2:s antagande "Sidan är ert att bygga vidare på" står kvar i sak. Dubbelprepositionen "för … för" bort. Semikolon → punkt (produktionstell i svensk webbcopy). Registerfix "sajten". |
| 96 px, radavståndet i liggaren, **en mätt enhet som all rytm räknas ur.** | 96 px, radavståndet i liggaren**. All rytm räknas ur det.** | 0, 2, 3 | Samma appositionsstapel; abstrakt svans ersatt av en sats. |
| … i den takt ni har dem**; vi bearbetar texten så att den är kort och läsbar och beskär och optimerar bilderna för webben.** … **Sidan fylls** på testadressen … | … i den takt ni har dem**. Texten bearbetar vi så att den blir kort och läsbar, bilderna beskär och optimerar vi för webben.** … **Vi fyller sidan** på testadressen … | 0, 2, 3, 4 | Fyra "och" i en sats; delad i två parallella satser med framflyttat objekt (svensk ordföljd). Semikolon bort. Passiv "Sidan fylls" → aktiv. |
| **Innan sidan går live går vi igenom** den tillsammans på testadressen: … | **Innan sidan går live granskar vi** den tillsammans på testadressen: … | 0, 3, 4 | "går live går vi" ekade. "granskar" tar bort ekot och frigör "genomgång" till sista meningen, där löftet hör hemma. Samma handling. |
| Vi finns kvar efter lansering. En sida är **ett levande dokument**: … | Vi finns kvar efter lansering. En sida är **aldrig färdig**: … | 2, 4 | "levande dokument" är kontorsfras (humanizer § 1/§ 15). Samma påstående i rak svenska. Inget nytt löfte: P3:s antagande ("bara vi finns kvar och ändringar går samma väg") oförändrat. |
| De tre exempelsajterna **på den här sidan** är riktiga … | De tre exempelsajterna **här på sidan** är riktiga … | 4, 3 | Naturligare svensk ordföljd, ett ord kortare, samma syftning. |

## Lämnade orörda, och varför

| Sträng | Skäl |
|---|---|
| De femton låsta raderna i `PRODUCT.md` § Brand Commitments | Låsta. Diffade byte för byte före och efter: identiska. |
| Kicker `Så går det till`, rubrik `Från samtal till lanserad sida.` | Svarar redan på vad avsnittet är och hur långt processen sträcker sig. Inget att skärpa. |
| `Sju steg, samma ordning i varje projekt, så att ni alltid vet var vi är.` | "alltid" är kvalificerare som copywriting normalt stryker, men det är just den ordet som bär trygghetslöftet (Highways "full insyn" i vår form). Behållet medvetet. |
| De sju stegtitlarna (Uppstart … Förvaltning) | Ettordsetiketter, ingen av dem tvetydig. |
| Marginalrad 01, 05, 06, 07 | Redan korta, konkreta, i ritningens agentlösa röst. |
| Princip 2 och 3 med rader | "kontrast som går att läsa i solljus" är sidans mest konkreta rad; "En sida ni inte kan uppdatera åldras från dag ett" är dess vassaste. Inget att vinna. |
| `Det är inte ett tillägg, det är hur vi bygger.` | Formellt humanizer § 9 (negativ parallellism), men mönstrets synd är tomhet, och här står en konkret uppräkning direkt före. Behållet medvetet, flaggat här. |
| Liggarens rad 02: `Snabbt, tillgängligt och ert att bygga vidare på.` | Tre adjektiv utan motivering (humanizer § 8), men de två första är belagda i steg 04 och det tredje är P2:s antagande. Liggarraden är avsiktligt komprimerad. |
| Liggarens rad 03: `… skötta efter lansering.` | Starkare än P3:s antagande i § 4, men raden står så i § 3:s copy v1 och redan i filen. Att försvaga den vore också ändrad innebörd. Lämnad; **lead bör avgöra** om P3 ska sänka den. |
| Prisblockets ingress | Två meningar, båda sanna, andra meningen besvarar invändningen "varför saknas pris". "utskrivet" bär positioneringen "priset står framme". |
| Tesrubriken `Det första intrycket är digitalt.` | Utanför uppdragets uppräkning (bara "tesens stycke" ingår). |
| Kortbaksidan (`Alunix`, `Digital byrå`, `Boka ett möte`) och `.sr-only`-kopian | Utanför uppdragets uppräkning. `.sr-only`-raden måste dessutom förbli ordagrant lika kortbaksidan (a11y-fix 7). |
| Bildtexter | Alla tre är låsta rader. |

## Upprepningar som står kvar, medvetet

`godkänner innan vi bygger`, `i kod från grunden`, `telefon, surfplatta och dator`,
`med tangentbord och skärmläsare`, `ert att bygga vidare på` förekommer två gånger var —
en gång i processakten och en gång i liggaren. Liggaren är stegens kortform; att de säger
samma sak är formens avsikt, inte en tell. Inom ett och samma stycke finns ingen
upprepning kvar (steg 04:s dubbla "bygga vidare på" var den enda och är åtgärdad).

## Anmärkning till lead: grinden, inte copyn

Den `design-gate`-kopia som faktiskt kör är den installerade plugin-cachen
(`~/.claude/plugins/cache/anti-slop-design/anti-slop-design/1.0.0/hooks/design-gate.py`).
Den **unionerar** alla `catalogue-select`-rader i sessionen. Repots egna kopior
(`.claude/hooks/` och `hooks/`, byte-identiska) är redan rättade till
`select_rows[-1]` — exakt den r8 R1-bugg kommentaren i filen beskriver. Cachen är alltså
efter repot. Följden här: två `select.py`-körningar (en mot `BRIEF.md`, som avviker, och en
mot `BRIEF-draft.md`, som reproducerar BRIEF:ens kanoniska lås) unionerades till nio slugs,
och referensgolvet krävde att alla nio lästes färdigt innan en enda sträng fick ändras.
Golvet är uppfyllt ärligt, inte kringgått: ingen hook avstängd, ingen env-flagga satt,
ingen ledger-rad redigerad. Cachen behöver uppdateras (kräver Antons go-ahead enligt
push-regeln).

## V3d R7

Copy-agent, 2026-09-19. Plan 054, underlag `COPY-V3d-v0.md`. Leverans `COPY-V3d-final.md`
(v0 | final | pass som ändrade | skäl, 94 rader, placering och v0-text maskinellt jämförda
mot v0: identiska). `index.html` orörd. Casefakta lästa mot `sites/calyx.html` och
`sites/horai.html` och mot ankarna i plan 054 steg 12 (vad som står i ramen i varje steg).

### Pass 0, UX-copy
Varje sträng läst som gränssnittstext, varje casesteg mot sajtens innehåll i sitt
scrollintervall. Fynd:
- Calyx steg 4 h3 "Listan ritade vi först" krockade med steg 1 "Blommorna först" (två "först"
  med olika betydelse i samma case) → "En lista, inte kort"; skenan följer.
- Calyx steg 1: fotot fyller inte "hela" första skärmen (88 vh under navigeringen) → "första
  skärmen är ett foto".
- Calyx steg 2: sajten sätter rubrik och brödtext i samma serif; v0 beskrev två val.
- Hōrai steg 1: "mörk, varm grund" osant; sajtens grund är ljust papper, det mörka är
  hero-fotot → "första skärmen är ett mörkt foto".
- Hōrai steg 2: tecknet står ovanför rubriken, inte bredvid, och är rött bara i huset och
  menyerna → beskriver bara husets rubrik. h3 "Texten tänds när ni läser" → "Texten tänds ord
  för ord" (scrollen tänder orden, inte läsningen); skenan följer.
- Hōrai steg 4: namnen är mörka, bara siffran och priset röda.
- Process 04: v0 strök "ert att bygga vidare på" och liggaren som bar det är borta; löftet
  hade försvunnit från sidan (ändrad innebörd) → återinfört som "Sidan är er att bygga vidare
  på." (rätt kongruens).
- Process 05: "vi sätter den [verksamheten] på plats" syftade fel.
- Utan fynd: tesens fem meningar (Antons "Vi hjälper er att synas på rätt sätt." ordagrant,
  bryter inget), processledet, noterna, kapitlet, bryggan, prisingressen.

### Pass 2, `Skill(copywriting)`
Enkelt före komplext, aktivt före passivt, ärligt före sensationellt. Ändrat: Calyx steg 2
("lugn och lätt att läsa" struket, två adjektiv utan belägg); Hōrai steg 4 ("går att läsa på
avstånd" var ett resultat → avsikt: "ska läsas som tavlor på en vägg"). Inga nya löften.

### Pass 3, `Skill(copy-editing)`, sju svep med loop-backs
Klarhet: Calyx steg 5 "på det sätt den faktiskt tar emot beställningar" → konkret "per mejl
… be om ett mejl"; Hōrai steg 3 "innan det blir praktiskt" → "innan menyer och priser".
Röst: Hōrai steg 1 speglar nu Calyx steg 1 ("Därför är första skärmen …"). Process 06:
"går live går vi igenom" ekade mot "genomgång" → "granskar" (samma lösning som V3c).
Svep 4 till 7 (bevis, specificitet, känsla, noll risk) gav medvetet inga tillägg: skillens
förslag (siffror, omdömen, kundcase, garantier) är förbjudna enligt `PRODUCT.md` § absences.

### Pass 4, `Skill(humanizer-svenska)`, sist av de tre skills
Varje svensk sträng läst. Ändrat: "faktiskt" (utfyllnad, § 12) ur Calyx steg 5; "sidan
andas" (sliten bild) ur Hōrai steg 3; "lättläst serif" i Hōrai steg 4; process 05 delad i två
korta satser. AI-testet: kvar är "X, inte Y" i Calyx steg 4 och dess rubrik; behållet
eftersom kontrasten är konkret (lista mot kortrutnät), inte § 9:s tomma parallellism. Efter
detta pass ändrades ingen sträng.

### Pass 5, mekaniskt
| Kontroll | Utfall |
|---|---|
| Låst copy, byte för byte (`PRODUCT.md` § Brand Commitments, 18 strängar inkl. de tre tjänsterna) | **18/18** i final-kolumnen |
| Tankstreck (U+2010–U+2015, U+2212, U+2043, U+FE58, U+FE63, U+FF0D) | **0** |
| Tal | `01`, `07`, `320`, `768`, `1440`, `16:9`, `7` (rem), `96`, `26 900`, `38 900`. **Inga nya** |
| Påhittade kunder, citat, resultat, team, tider | 0. Casen återger inga av sajternas priser, namn, citat eller omdömen |
| `deslop.py --text` per sektion (tes, process, kapitel, Calyx, brygga, Hōrai, pris) | 7/7 **5/5 CLEAN** (`--view` tar en vy i HTML, inte en fil; `--text` är rätt läge för strängar) |
| Svenska tvillingar för hand (utgör, representerar, möjliggör, faktiskt, verkligen, inte bara, semikolon, utrop …) | 0 |
| `jag` / Klova | 0 / 0 |
| Meningar > 25 ord | 0 |
| Ordtak | processtycken 42 till 49 (≤ 50), casesteg 22 till 36 (≤ 40) |
| Vi-form, "ni/er" | ja; "man" bara om gäster på de tänkta sajterna (Calyx 1, Hōrai 5 och 6) |

### Flaggat för Anton
1. `.ts` 4 "Vi hjälper er att synas på rätt sätt." står ordagrant. "på rätt sätt" är vagt,
   men meningen bär bara fram till "VI BYGGER ERT VARUMÄRKE."; inget att åtgärda.
2. Process 04 "Sidan är er att bygga vidare på." återinförd (v0 hade strukit den).
3. Process 04 v0 strök "på samma tekniska nivå som resten av sidan" och 06 "i riktiga
   webbläsare". Båda var löften i sak. Lämnade strukna enligt arkitektens v0 (ordgränsen),
   men lead bör bekräfta att de får gå.
4. Casen beskriver sajternas typografi och färg; Calyx- och Hōrai-sajterna själva innehåller
   påhittade citat och namn (Calyx omdömen, Hōrais kockar). Casetexterna nämner dem inte, men
   ramen visar dem live. Ärvt från sajterna, utanför copy-uppdraget.

## V3d R12

Copy-agent, 2026-09-19. Antons beställning: casetexten "känns fortfarande väldigt AI:ig",
rubrikerna "lite roligare", övergången till priset ska bli "en bra visuell och mental övergång
till att köpa". Underlag `COPY-V3d-case-v1.md`, `CASE-UNDERLAG.md`. Leverans
`COPY-V3d-case-final.md` (plats | v1 | final | pass som ändrade | skäl, en rad per sträng,
placering oförändrad från v1). `index.html` orörd. Varje valpåstående läst mot
`sites/calyx.html` och `sites/horai.html` och mot ankarna i plan 054 (`CASES` i § 4).

### Pass 0, UX-copy
Varje casesteg läst mot vad ramen visar på sitt ankare. Fynd:
- Calyx steg 3 (ramen på bildparet) talade om rosttonen "i listan", som inte syns förrän
  steg 4, och rosttonen står också på anfangerna → "den dyker upp först längre ned".
- Calyx steg 4: listan har löpnummer och en rad beskrivning; en post är ett restaurangavtal,
  så "buketter" → "utbud".
- Calyx steg 5: "bara en e-postadress" osant, sektionen har också besöksadressen.
- Hōrai steg 1: loggan döljs medan hela hero-sektionen syns (IntersectionObserver på
  `#hero-section`), inte rubriken; "aldrig på samma skärm" för starkt.
- Hōrai steg 2: "i berättarens takt" motsade h3 "i er takt".
- Hōrai steg 4: "i rött och större" syftade på siffra, namn och pris; bara siffra och pris är
  röda, namnen mörka.
- Hōrai steg 6: sajten säger "matters that don't fit a form", inte "i en bokning".
- Bryggan: "köket" var en omskrivning; sektionerna heter huset och menyerna.
- Övergången: läsaren ska förstå att nästa fakta är priset och vad första steget är. Svarar
  redan på det; inget fynd.

### Pass 2, `Skill(copywriting)`
Specifikt före vagt, skäl före slutsats. Calyx steg 1: "så bilden kom först" (slutsats utan
skäl) → skälet står: en bukett vill man röra vid, på en skärm kommer ett stort foto närmast.
Hōrai steg 5: visdomsavslutet ersatt av ett konkret val i ramen (mörk toning från vänster så
att texten går att läsa, sajtens `bg-gradient-to-r`). Inga nya löften.

### Pass 3, `Skill(copy-editing)`, sju svep med loop-backs
Klarhet: Calyx steg 5 kolonmeningen delad; övergången "skiljer sig" → "skiljer sig åt".
Röst: Hōrai steg 2 och 3 slutade båda på en vi-mening med samma form → steg 3 "Den står där
för att bromsa läsningen"; "sakta ner" ekade h3 "saktar in". Calyx steg 2: bortvalet (ett
andra rubriktypsnitt) som v1 bara nämnde i kommentaren står nu i texten med skäl. Svep 4 till
7 (bevis, specificitet, känsla, noll risk) gav medvetet inga tillägg: skillens förslag
(omdömen, tal, garantier, riskreversering) är förbjudna enligt `PRODUCT.md` § absences.
Övergångens mikrorad svarar redan på "vad händer sen".

### Pass 4, `Skill(humanizer-svenska)`, sist av de tre skills
Mönstren Anton pekade på, sträng för sträng:
- Symmetriska rubrikpar: case-rubrikerna "Calyx läses som en tidskrift." och "Hōrai sparar
  bokningen till sist." hade samma byggnad → "Calyx fick bli ett vårnummer." (sajtens egen
  "Vol. ix · spring") och "Hōrai serverar bokningen sist." (restaurangens verb). Hōrai steg 6
  h3 "Bokningen sist, knappen hela vägen" (två symmetriska halvor, upprepade rubrikens "sist")
  → "Knappen fanns där hela tiden"; skenan följer.
- Visdomsavslut: struket i Calyx steg 4 ("En rad text är lättare att byta än en bild."),
  Calyx steg 5 ("Ett formulär har inte plats för det samtalet."), Hōrai steg 5 ("Rummet blir
  det sista man läser innan man gör något.").
- "Inte X utan Y" och negativ parallellism: Hōrai steg 4 "en hel kväll, inte en rätt" →
  sajtens faktum "Utan à la carte"; bryggan "En middag gör det inte." → "Om en middag måste
  man berätta".
- Uppräkningar i tre: bryggan "huset, köket och rummet" → två led; Hōrai steg 3 tre verb →
  två led; Hōrai steg 6 kolonlistan med tre led → två meningar.
- Abstrakta värdeord: inga fanns i v1; inga tillkom.
AI-testet: kvar är "Ni har sett arbetet. Här är priset." (två korta satser). Behållen: andra
satsen är en anvisning, inte en poäng, och det är säljarens mening efter genomgången (Hopkins
säljtest, CASE-UNDERLAG princip 3). Vad saknades för en människa på byrån: bortvalen med skäl
(typsnitt, kort med foto, formulär) och en egen ton i rubrikerna; båda inlagda. Efter detta
pass ändrades strängar bara för pass 5:s ordgräns.

### Pass 5, mekaniskt
| Kontroll | Utfall |
|---|---|
| `deslop.py --text` per sektion (rubriker, Calyx, brygga, Hōrai, övergång) | **5/5 sektioner, score 5/5 CLEAN** |
| Tankstreck (U+2010 till U+2015, U+2212, U+2043, U+FE58, U+FE63, U+FF0D) i final-kolumnen och i hela final-filen | **0** |
| Siffror i final-kolumnen | **0**. "romersk siffra" och "à la carte" är ord, inga tal |
| Låst copy | `kontakt@alunix.se` ordagrant i mikroraden; övriga låsta strängar i området (bildtexter, iframe-titlar, `#pris`) orörda |
| Påhittade kunder, citat, resultat, team, tider | 0. Casen återger inga av sajternas namn, priser, citat eller omdömen; "öppettiderna i hörnet" och "när veckans platser släpps" säger var uppgiften står, inte uppgiften |
| Svenska tvillingar (utgör, representerar, möjliggör, faktiskt, verkligen, inte bara, semikolon, utrop), `jag`, Klova | 0 |
| Ordgräns casesteg ≤ 40 (plan 054 § 13) | Calyx 35 till 40, Hōrai 35 till 40; pass 5 kortade Calyx 1 och Hōrai 1 till 4 (46, 42, 41, 41, 48 ord → ≤ 40) utan ändrad innebörd |
| Meningar > 25 ord | 0 |
| Vi-form | ja; "ni" om läsaren som scrollar (Hōrai 2, 3), "man" om besökare på de tänkta sajterna |
| Final-kolumnen maskinellt jämförd mot de kontrollerade strängarna | identiska |

### Flaggat för Anton
1. Case-rubrikerna har ny ton: "Calyx fick bli ett vårnummer." och "Hōrai serverar
   bokningen sist." v1:s "Calyx läses som en tidskrift." finns kvar som rakare alternativ.
2. Hōrai steg 6 h3 "Knappen fanns där hela tiden" ersätter v1:s rubrik och därmed skenan.
3. Calyx steg 2 "Ett andra rubriktypsnitt hade dragit åt reklam." är vårt omdöme om ett
   bortval, inte ett faktum ur sajten.
4. Hōrai steg 2 "Rubriken står kvar": husets rubrik är `md:sticky`, alltså bara från 768 px
   ramvidd. Är ramen smalare på mobilen stämmer "kvar" inte där; byggaren kontrollerar.
5. Övergångens rubrik "Ni har sett arbetet. Här är priset." står kvar ordagrant från v1.
6. Prisingressens krock (v1 § Ett hänsynstagande) gäller fortfarande: behåll index.html:s
   "Det tredje beror på omfattningen".

## V3d R13

Copy-agent, 2026-09-19. Antons feedback på `COPY-V3d-case-final.md`: Hōrais rubrik gick att
feltolka, bron "Ni har sett arbetet. Här är priset." tas bort, "Alla har rätt till bra design."
blir rubrik för en enhet rubrik → säljande text → prisliggaren. Leverans
`COPY-V3d-pris-final.md`. `index.html` orörd.

### Pass 0, UX-copy
- Hōrai: "serverar bokningen sist" läses som "bokningar i andra hand". Påståendet som ska fram:
  sidan *ber om* bokningen sist, men knappen finns hela vägen (steg 6). Utkast: "Hōrai dukar
  upp kvällen innan den ber om en bokning." ("den" kunde syfta på kvällen, bytt i pass 4).
- Prisblocket: den nya ingressen ersätter bron och den gamla ingressen. Innebörden att det
  tredje paketet saknar fast pris bevaras. Adressen står under liggaren (`.close-mailto`),
  så slutraden får inte upprepa den. `aria-labelledby="bro-title"` pekar på en borttagen
  rubrik; flaggat för byggaren.
- Underlag: `marketing-principles.md` § 2.1, 3.2, 3.5, 6.3 (valvet, lästa per grupp) och
  `Skill(marketing-psychology)` (Commitment & Consistency, Activation Energy, Hick's Law).
  qmdv-sökningen gav inga träffar i marknadsdomänen; filen lästes direkt.

### Pass 2, `Skill(copywriting)`
Nytta före egenskap: "väljer bort det som inte behövs" → "väljer bort allt som inte hjälper
den" (verksamheten). Specifikt före vagt: rubrikens löfte kopplat till ett låst pris ("också
i det som kostar 26 900 kr").

### Pass 3, `Skill(copy-editing)`, sju svep med loop-backs
Klarhet: "Vi börjar i verksamheten" → "Vi läser verksamheten först" (casens egen filosofi).
Röst: kickern "Från exempel till er sida" och "som er sida går igenom" ekade → "ert projekt".
So what: "Paketen skiljer sig åt …" leder blicken till raderna. Bevis, specificitet: inga nya
påståenden, bara det låsta priset. Nollrisk: skillens förslag (garanti, "kostar ingenting",
tider) avvisade enligt `PRODUCT.md` § Absences; första steget räcker som tröskelsänkare.

### Pass 4, `Skill(humanizer-svenska)`, sist av de tre skills
- Hōrai: "den" kunde syfta på "kvällen" → "Hōrai dukar upp kvällen och ber om bokningen sist."
  "… före bokningen" förkastad (läses som kvällen innan).
- Jämna styckeblock (fyra meningar på 12 till 17 ord) → sista satsen utbruten till en kort
  mening, och "har inget fast pris" (negation) → "Det tredje prissätter vi efter omfattningen."
  (aktivt vi).
- Eko: "er verksamhet" i slutraden efter "verksamheten" → "Första steget är ett samtal om
  vad ni gör." (processens steg 01).
- AI-testet: kvar är att "Så arbetar vi i alla tre paketen" kan låta som en slogan. Behållen,
  eftersom den direkt följs av ett pris och därmed är ett påstående som går att pröva.

### Pass 5, mekaniskt
| Kontroll | Utfall |
|---|---|
| `deslop.py --text` (Hōrai-rubriken; kicker + rubrik + text + kort rad) | **2/2, score 5/5 CLEAN** |
| Tankstreck U+2010 till U+2015, U+2212 i final-kolumnen | **0** (se kontrollen nedan) |
| Låst copy | "Alla har rätt till bra design.", tre radbeskrivningar, 26 900 kr, 38 900 kr, Pris vid förfrågan ordagranna |
| Nya tal | **0**. Enda talet i texten är det låsta "26 900 kr"; "tre paketen" står redan på sidan |
| Ordgräns | text 56 ord, 5 meningar, längsta 15 ord; kort rad 9 ord |
| Kontaktadress i texten | 0 (står under priserna) |
| Vi-form, ni/er, `jag`, Klova, utrop, semikolon | vi/ni ja; övriga 0 |

### Flaggat för Anton
1. Hōrai-rubriken säger "sist" igen, men nu om *frågan*, inte om bokningen i sig. Bryggans
   stycke före caset ("… på Hōrai kommer huset och menyerna före bokningen.") säger nästan
   samma sak; om det känns dubbelt kan bryggan kortas i en senare runda.
2. Texten upprepar "26 900 kr" som står i rad 1 några rader nedanför. Det är avsiktligt (det
   är där "alla har rätt" blir pengar), men det är ett dubbelt tal på skärmen.
3. `.price-bridge#bro` som egen sektion blir tom. Byggaren avgör om plåten/övergången behålls
   utan text eller slås ihop med `#pris`.

## V3d R17

Copy-agent, 2026-09-19. Antons beställning: case-introt blir "Exempelcase" + text, prisets
text skrivs om (tre meningar dömda som självklarheter), och all liten beskrivande AI-text
(kickers, bildtexter, steg-rails, förklarande rader) är förbjuden från och med nu. Leverans
`COPY-V3d-r17-final.md`. `index.html` orörd.

### Pass 0, UX-copy
- Läste byråernas listsidor (curl, HTTP 200 × 3): Insign "Projektarkivet" + en rad om
  antal, Highway "Case" utan ingress, Hoy "Projekt" + två talspråkliga ord. Ingen förklarar
  vad ett case är. Enda saken vårt intro *måste* säga och de inte behöver: verksamheterna
  är påhittade (`PRODUCT.md` § Absences).
- Bildtexterna tas bort, så "florist i Stockholm" behöver ett nytt hem: introt.
- Pris: vad kan en text under rubriken säga som raderna inte redan säger och som inte är ett
  villkor, en tid eller en garanti? Svar: nästan inget. Utkast: ingen text.
- Underlag: `marketing-principles.md` § 1.1 (säljtestet), 3.2 (skriv ut priset), 3.5
  ("Consumer not a moron"), 6.3 (lova inget nytt), valvet, läst direkt.
  `Skill(marketing-psychology)`: Hick's Law, Pratfall.

### Pass 2, `Skill(copywriting)`
Intro: specifikt före vagt ("florist i Stockholm", "restaurang" i stället för
"exempelsidor"); ärligt före sensationellt ("Ingen av dem finns"). "Här berättar vi hur vi
tänkte, från första skiss till färdig sida" struken: beskriver sektionen och lovar en
kronologi casen inte har. Pris: skillens standardsektioner (risk reversal, CTA-upprepning)
avvisade, se Absences och Hick's Law.

### Pass 3, `Skill(copy-editing)`, sju svep
Klarhet: "Bredvid varje sida står …" fel på mobil (ramen staplas) → "Vi går igenom vad vi
valde i dem och varför." So what: introts tre meningar svarar på vem, vad är sant, vad får
jag. Prove it: allt i introt syns i casen. Zero risk: priset får ingen riskreversering
(skulle vara ett nytt löfte). Pristext: varje kandidatmening föll på so what eller var en
upprepning av raderna.

### Pass 4, `Skill(humanizer-svenska)`, sist
- "Verksamheterna är påhittade, sidorna har vi byggt på riktigt." symmetrisk kontrast,
  låter som en slogan (mönster 9) → "Ingen av dem finns, men sidorna är färdiga."
- "i sin helhet" prövad, struken (utfyllnad).
- AI-test: kvar är att tredje meningen beskriver innehållet. Behållen, eftersom den lovar
  något konkret (val och skäl) som byråerna saknar, och Anton bad om en text.

### Pass 5, mekaniskt
| Kontroll | Utfall |
|---|---|
| `deslop.py --text` (introt; reservmeningen för priset) | **2/2, score 5/5 CLEAN** |
| Tankstreck U+2010 till U+2015, U+2212 i hela `COPY-V3d-r17-final.md` | **0** |
| Låst copy | "Alla har rätt till bra design." och prisraderna ordagranna. Bildtexterna borttagna på Antons beslut, konflikt med låslistan flaggad |
| Nya tal | **0** |
| Ordgräns | intro 28 ord, 3 meningar; pristext 0 ord |
| "vi X, inte Y", visdomsavslut, tre-uppräkning, utrop, semikolon, `jag`, Klova | 0 |
| Vi-form, ni/er | ja |

### Flaggat för Anton
1. Priset: ingen text rekommenderas. Enda reservmening: "Calyx hade fått plats i
   standardpaketet.", ett sakpåstående som kräver hans ok.
2. `.process-lead` och de sju `.process-note` är av den förbjudna sorten; lead rekommenderas
   struken, noterna är hans avgörande.
3. Case-stegens första meningar upprepar nu introt ("… en exempelsida för en tänkt …").
4. `PRODUCT.md` låslista behöver uppdateras för de tre bildtexterna.

### V3d R17, pristext, andra beställningen
Antons beställning 2026-09-19: en text mellan rubriken "Alla har rätt till bra design." och
priserna som bryggar från casen till köp (casen som bevis, samma nivå i alla lägen, kundens
egna behov och önskemål), utan den strukna textens ordval och grepp. Leverans:
`COPY-V3d-r17-final.md` § "Pristext, Antons andra beställning". `index.html` orörd.

**Pass 0, UX-copy.** Tre saker att bära, högst 40 ord, i rubrikens röst, blicken nedåt till
raderna. Förbjudna ord listade ur den strukna texten (samma, steg, läser, väljer bort, paket,
också, kostar, skiljer sig, omfattning) och ur case-introt (florist, finns, färdiga, valde,
varför, går igenom). Underlag: `marketing-principles.md` § 1.1, 2.2, 3.5, 6.3 (valvet, läst
direkt).

**`Skill(marketing-psychology)`.** Valda: Regret Aversion och Availability Heuristic (casen
som visat utfall i stället för garanti), Jobs to Be Done (kundens behov), Hick's Law.
Avvisade: anchoring, good-better-best, scarcity, riskreversering (låst ordning, Absences).

**`Skill(copywriting)`.** Tre alternativ (A, B, C). Klart före smart: A pekar på casen i
stället för att beskriva dem. Ingen CTA-upprepning, adressen står direkt efter priserna.

**`Skill(copy-editing)`, sju svep.** Klarhet: utkastet "… och vad sidan blir bestämmer era
egna behov och önskemål" gick att läsa baklänges (objekt först, båda leden kan vara subjekt)
och blev "och sidan ritar vi efter era egna behov och önskemål". So what: varje mening bär
ett av de tre uppdragen. Prove it: "det ni just har sett" är beviset, strax ovanför. Zero
risk: ingen garanti, visat arbete i stället.

**`Skill(humanizer-svenska)`, sist.** "Den nivån gäller varje rad nedan" (myndighetsverb)
blev "Den nivån får ni på varje rad nedan". B: "håller samma nivå" struket ("samma"); kvar är
ett förklätt "oavsett", därför inte valt. AI-test på A: kvar är att första meningen är en
definition. Behållen, eftersom den är rubrikens egen fortsättning och inte en slogan.

**Mekaniskt.**

| Kontroll | Utfall |
|---|---|
| `deslop.py --text` A, B, C | **3/3, score 5/5 CLEAN** |
| Tankstreck U+2010 till U+2015, U+2212 i de nya sektionerna | **0** |
| Låst copy | Rubriken ordagrann; inga låsta priser upprepade |
| Nya tal | **0** |
| Ord | A 28, B 26, C 25 |
| "inte X utan Y", visdomsavslut, tre-uppräkning, "oavsett", utrop, semikolon, `jag`, Klova | 0 i A |

**Val: A.** "Med bra design menar vi det ni just har sett. Den nivån får ni på varje rad
nedan, och sidan ritar vi efter era egna behov och önskemål."

## V3d R18

Antons beställning 2026-09-19: processtegen ska vara kortare, stå i större text och få ett tydligare löfte per steg. Marginalnoterna tas bort utan ersättning (F-016). Leverans: `COPY-V3d-r18-steg.md`. `index.html` är inte ändrad.

- **Pass 0, UX-copy.** Ett löfte per steg, fördelat så att inget upprepas: skriftligt underlag (01), skiss och mobil (02), testadress och godkännande (03), CMS och "er att bygga vidare på" (04), innehållshjälp (05), tester och genomgång (06), förvaltning och adressen (07).
- **`Skill(copywriting)`.** Klart före smart. Titlarna står kvar, och varje text läses på ett ögonkast.
- **`Skill(copy-editing)`, sju svep.** Klarhet: i 02 blev "vad varje sida ska få besökaren att göra" till "vad de leder till". So what: i 04 knöts "kod från grunden" till "er att bygga vidare på". Prove it: testerna i 06 stöds av P10.
- **`Skill(humanizer-svenska)`, sist.** I 01 blev "får ni vårt förslag skriftligt" till "skriver vi ner vårt förslag" (aktivt verb). I 02 fick participet ge plats för verbet "planerar". AI-test: kvar är den jämna tvåmeningsformen, som beställningen själv kräver.
- **Mekaniskt.** `deslop.py --text` gav 7/7 CLEAN. Tankstreck 0, siffror 0, 18 till 22 ord per steg, låst copy ordagrann.
- **Flaggat.** Löftet om innehållshjälp i 05 går längre än P4-antagandet (se leveransfilen).

## V3d R23

Antons beställning 2026-09-20. **Underkänt, och varför:**

1. **R18:s processteg (18 till 22 ord) underkända som för kortfattade.** "Texten blev även
   aningen för kortfattad … förmedla trygghet och expertis, samtidigt som det inte blir för
   långt att läsa." De två ytterligheterna är nu mätta: V3c 57 till 67 ord per steg läste som
   en rullande paragraf man scrollar förbi, R18 18 till 22 ord förmedlade inte längre
   expertis. **Ny norm: 35 till 45 ord, två till tre meningar per steg.** Lärdomen är att
   ordgränsen inte får sättas utan att sakinnehållet räknas: R18 kortade genom att stryka
   löften (testadressen på er egen skärm, länk- och formulärkontrollen, att genomgången lär
   er ändra själva, att nya sidor går samma väg), inte bara utfyllnad. Vid nästa
   kortningsbeställning: stryk retoriken först, räkna löftena efteråt, och kontrollera att
   inget löfte försvunnit från sidan.
2. **Ingressen till Exempelcase underkänd som "helt hjärndött" och "precis samma AI-slop".**
   Strängen var `Calyx är en florist i Stockholm och Hōrai en restaurang. Ingen av dem finns,
   men sidorna är färdiga. Vi går igenom vad vi valde i dem och varför.` Felet är en form,
   och den formen är härmed förbjuden: **uppställning → brasklapp → färdplan.** Var och en
   för sig: uppställningen förutsätter att läsaren inte förstår att en case-sektion innehåller
   case; brasklappen ("Ingen av dem finns") ber om ursäkt för arbetet innan det visats;
   färdplanen ("Vi går igenom … och varför") är sidan som beskriver sig själv, alltså F-016
   och gate 99 i löptext i stället för i microtext. R17 lät den tredje meningen passera med
   motiveringen "den lovar något konkret som byråerna saknar", det var fel bedömning, och
   den ursäkten får inte återanvändas. **Regel: en ingress ska handla om oss och vårt arbete,
   aldrig om sektionens upplägg, och aldrig be om ursäkt för att exemplen är påhittade.**
3. **Case-rubrikerna ersatta, ordagrant av Anton:** `Florist, Stockholm` och `Restaurang,
   Asian Fusion` i stället för `fick bli ett vårnummer.` och `dukar upp kvällen och ber om
   bokningen sist.` R12:s "ny ton i rubrikerna" är därmed avvecklad. Rubrikerna är nu
   etiketter, inte meningar, och kapitlet har ingen egen röst kvar före stegen. Det är
   skälet till att ingressen rekommenderas behållas (alternativ A) i stället för att strykas.

**Ny sektion beställd:** kontaktsektion längst ned efter priserna (rubrik, kort rad, tre
fältetiketter, knapptext, adressen kvar som alternativ väg in). Ingen hjälptext under fälten,
inga svarstider, inga villkor, inga tal.

Leverans `COPY-V3d-r23.md`. `index.html` är inte ändrad. Kedjan kördes i ordning: pass 0
UX-copy → `Skill(copywriting)` → `Skill(copy-editing)` → `Skill(humanizer-svenska)` sist →
pass 5 mekaniskt. Inget pass hoppades över.

| Kontroll | Utfall |
|---|---|
| `deslop.py --text`, sjutton strängar | **17/17, score 5/5 CLEAN** |
| Tankstreck U+2010 till U+2015, U+2212, U+2043, U+FE58, U+FE63, U+FF0D och bindestreck | **0** |
| Siffror | **0** |
| Låst copy | `kontakt@alunix.se` ordagrant två gånger; ingen annan låst sträng berörd |
| Ordräkning, stegen | 37, 37, 44, 37, 37, 37, 35 (kravet 35 till 45) |
| Meningar per steg | tre i alla sju; längsta mening 23 ord |
| Ingress | 20 ord, två meningar |
| Treuppräkning, "inte X utan Y", visdomsavslut, sentens, semikolon, utrop, `jag`, Klova | **0** |

**Flaggat, i korthet** (fullständigt i leveransfilen): P4 är fortfarande obesvarad och steg
05 står därför i den försiktiga formen; kontaktformuläret krockar med `PRODUCT.md`
("inget formulär", "ingen egen server") och behöver både en låslisteuppdatering och ett
beslut om mottagare; formuläret saknar svarsväg eftersom inget e-postfält beställts;
`Asian Fusion` i rubriken stavas annorlunda än den låsta `Asian fusion-koncept` i ramens
`title`; adressen hamnar på tre ställen på sidan.
