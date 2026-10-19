# V3d · PARITET

> **Plan 067 (R23, 2026-09-20): P01, P04, P07-P13, P14, P15, P16, P17, P19 och P21 ar omskrivna, och P24 och P25 ar nya. De galler i stallet for raderna i den har filen. Se [PARITET-067.md](PARITET-067.md).**

Tabellen granskaren (Astra) och lead dömer mot. En rad per skärm i V3d. Varje rad har en
referensbild ur `runs/V3c/shots/fasA/` (alla sökvägar nedan är relativa till den mappen) och
ett uttalat drag som V3d ska matcha. **Referensen visar nivån, inte formen**: vi lånar hur den
iscensätter skärmen (skala, vad som äger viewporten, hur mycket luft), aldrig dess palett,
typsnitt, knappar eller copy.

## Hur en rad döms

1. Byggaren skjuter vår skärm vid 1440x900 (och 390x844 där kolumnen 390 är ifylld) i det läge
   raden anger, och lägger den **bredvid** referensbilden i samma höjd med PIL:
   `shots/r1/par/<rad-id>-<bredd>.png` (vänster V3d, höger referensen, 24 px mellanrum,
   radens id och referensens filnamn i bildens underkant i 14 px).
2. Den som dömer läser par-bilden som bild och skriver en rad: **håller nivån** eller
   **håller inte, för att …** med det mätbara skälet (en storlek, en andel av viewporten, ett
   element som saknas).
3. **Slutvillkor:** varje rad i tabellen kan läsas "håller nivån" i sin par-bild. En rad som
   håller i 1440 men inte i 390 håller inte.

## Tabellen

Plan 054 (2026-09-19): P03, P04 och P14 omskrivna, P05 utgången, P17 till P20 nya. Par-bilderna
för de raderna läggs i `shots/r7/par/`.

Plan 057 (2026-09-19, R12): P03, P04, P16, P17, P19 och P20 omskrivna, P21 (prisbron) ny. Par-bilderna
läggs i `shots/r12/par/`, och P03, P04, P17-1, P19-1 och P21 skjuts dessutom vid **1920x930** (Antons
skärm). Tesen har **fyra** meningar (punkt 6). Ramarna döms i en Chromium **utan** `--hide-scrollbars`.

Plan 060 (2026-09-19, R17): P14, P15, P17, P19, P20, P21 och P16 omskrivna, P18 utgången (bryggan
borttagen), P22 (Calyx → Hōrai) och P23 (Hōrais bokning i ramen) nya. Par-bilderna läggs i
`shots/r17/par/`; P14, P17-1, P19-1, P19-6, P21, P22 och P23 skjuts dessutom vid **1920x930**. Gäller
alla rader från R17: **ingen kicker, bildtext, stegskena eller liten förklarande rad** får synas
(F-016), och ramarna har **ingen kantlinje** vid någon bredd eller zoom (magentaprovet, plan 060 B2).

Plan 061 (2026-09-19, R18): P04 omskriven (Blåkopian). P07 till P13 döms nu också på stegtexten: 28 till 32 px vid 1440/1920 (≥ 20 px vid 390), fullt bläck, rubriken i samma storlek ovanför, texten bandets största läsbara massa; `--band-h` ≤ 240 och arket ≥ 76 % vw vid 1440. Par-bilderna läggs i `shots/r18/par/`; P04 skjuts dessutom som fem bilder (`tes-till-ritning-0` till `-4`) vid **1920x930** och 390x844.

| Id | Skärm i V3d (läge) | Referens 1440 | Referens 390 | Vad referensen gör som vi ska matcha |
|---|---|---|---|---|
| **P01** fold | `?preview=front`, scrollY 0 | `hoy-1440/hoy-webb-1440--s00.png` | `hoy-390/hoy-home-390--s00.png` | Ett displayelement och en bild delar skärmen och inget annat; rubriken i affischskala utan konkurrerande text. Vår fold (rubrik ~120 px, kortet 62 % vw) ska läsas lika ensam och lika stor. |
| **P02** kortets baksida | `?preview=back` | `hoy-1440/hoy-home-1440--s00.png` | `hoy-390/hoy-home-390--s00.png` | Objektet äger mitten av skärmen, ett ord i displaystorlek ovanpå eller bredvid, tom grund runt om. |
| **P03** tesbandet (plan 054, 057) | `?preview=thesis-01` till `-04`, en bild per mening | `hoy-1440/hoy-home-1440--s01.png` | `hoy-390/hoy-home-390--s01.png` | Mättad grund äger hela skärmen, displayrubrik vänster, bild höger, **bildens överkant i linje med rubrikens**, fri från kanten med samma luft höger som vänster, bilden ~44 % vw. Hos oss (≥ 1024): blå stage 100 % vw x 100 % vh, fyra meningar, en i taget i 96 px (1920) / ~77 px (1440); Hyperborea **≥ 45 % vw**, överkant = meningens överkant ±8 px, `--rail-x` till höger, står still genom hela bandet. 390: R11:s lösning orörd. Bilden ska läsas som meningens jämbördiga motpart, inte som en bildtext i hörnet. |
| **P04** övergången tes → ritning (plan 061 "Blåkopian", ersätter 057:s rena kant) | `?preview=tes-till-ritning-0` till `-4`, `?preview=chapter`, plus hjulsekvensen 20 px ned och upp | `highway-1440/hw-hemsida-1440--s03.png` och `hoy-1440/hoy-home-1440--s02.png` | `highway-390/hw-hemsida-390--s05.png` | Highway låter en scrollritad tråd leda in i "Så arbetar vi"; hoy byter mättad grund mot nästa kapitel. Hos oss: när den blå plåten lyfter ritas ritningens egna linjer (arkets kanter och stationerna 320/768, på arkets exakta x ±1 px) i vitt på det blå, korsar kanten obrutna och fortsätter i `--hair-ink` över ritbordet, landar på en vågrät linje 40 px ovanför kapitelrubriken, som då bläcks in 62 % → 100 %. Scrubbat på kapitlets `--sc-ps`, båda riktningarna (staircase 0, max_step ≤ 3 %). ≥ 1024: blå del på de linjer som inte krockar med tickstrecken; 768 och 390: linjerna börjar i kanten. **Ingen bildruta där en rubrik är delvis dold av en annan yta eller korsad av en linje** (elementFromPoint-svepet + geometrisk kontroll) vid 1920, 1440, 768 och 390; rubriken får bara klippas av viewportens underkant. Inga etiketter på linjerna (F-016). Ska läsas som att tesen blir ritning i ett drag, inte som en dekor i en tom yta. |
| **P05** (utgången) | Hōrai-bandet finns inte längre (plan 054 steg 5); Hōrai döms i P19 | | | |
| **P06** processens kapitelskärm | scrollY = `#process` topp | `hoy-1440/hoy-home-1440--s03.png` | `hoy-390/hoy-home-390--s03.png` | En rubrik i displaystorlek äger hela skärmen på ren grund med en hårlinje; kapitlet presenteras innan det börjar. Vår "Från samtal till lanserad sida." ≥ 100 px vid 1440. |
| **P07** steg 01 | `?preview=process-01` | `hoy-1440/hoy-home-1440--s03.png` | `hoy-390/hoy-webb-390--s00.png` | Ett stort element på tom grund. Siffran 01 (≥ 150 px) och rubriken i bandet, det tomma arket ≥ 76 % vw under; skärmen är ett steg, inte ett stycke bredvid en ruta. |
| **P08** steg 02 | `?preview=process-02` | `hoy-1440/hoy-webb-1440--s08.png` | `hoy-390/hoy-webb-390--s08.png` | Displaytypografi och en stor bild delar skärmen jämnt; bilden är minst 44 % vw. Måttkedjan 320/768/1440 i 44 px accent ska läsas på avstånd. |
| **P09** steg 03 | `?preview=process-03` | `hoy-1440/hoy-home-1440--s06.png` | `hoy-390/hoy-home-390--s05.png` | Ett kapitel per skärm: rubrik, text, bild, allt inom en viewport, ingen del av nästa kapitel synlig. |
| **P10** steg 04 | `?preview=process-04` | `hoy-1440/hoy-home-1440--s07.png` | `hoy-390/hoy-home-390--s06.png` | Samma kapitelform med ett byte i materialet mellan kapitlen; skiftet mellan steg 03 och 04 ska synas som ett scenbyte (bandet byts), inte som att texten rullar vidare. |
| **P11** steg 05 | `?preview=process-05` | `hoy-1440/hoy-webb-1440--s07.png` | `hoy-390/hoy-webb-390--s05.png` | Produktytan i full bredd, ~78 % vw, är skärmens auktoritet. Calyx ≥ 50 % av arket och arket ≥ 76 % vw. |
| **P12** steg 06 | `?preview=process-06` | `hoy-1440/hoy-webb-1440--s01.png` | `hoy-390/hoy-webb-390--s01.png` | Bilden äger skärmen nästan kant i kant. Calyx i färg ≥ 80 % av arket, ≥ 960x540 px vid 1440; ritningen har dragit sig tillbaka; får inte läsas som en lampa i ett mörkt rum. |
| **P13** steg 07 | `?preview=process-07` | `hoy-1440/hoy-webb-1440--s10.png` | `hoy-390/hoy-webb-390--s09.png` | Bild och avslutande text i balans, bilden störst; revisionsfältet och siffran 07 är detaljer, inte konkurrenter. |
| **P14** case-kapitlet (plan 054, 060) | `?preview=cases` | `hoy-1440/hoy-webb-1440--s04.png` | `hoy-390/hoy-webb-390--s03.png` | Ljus grund i full bredd, en rubrik i displaystorlek äger skärmen, kort stycke under. Hos oss: **`Exempelcase` i Young Serif** (136 px vid 1920, ~130 vid 1440, 40 vid 390), ett ord på en rad, copy-agentens tre meningar i 20 px under; ingen kicker. Ska läsas som ett nytt kapitel och som Alunix egen röst, inte som ett citat ur en av sajterna. |
| **P15** pris + kontakt (plan 060) | `?preview=pris` (dokumentets slut) | `hoy-1440/hoy-home-1440--s08.png` och `hoy-1440/hoy-home-1440--s09.png` | `insign-390/insign-390--s10.png` | Avslutet är ett kapitel på en egen grund: en rubrik, text i läsbar storlek, en tydlig kontaktväg i handlingsstorlek. Hos oss: **allt i en och samma bild vid 1920x930 och 1440x900** (rubrik ≥ 48 px från toppen, kontakten ≥ 24 px från botten), 390 i en bild eller ren följd. Rubrik och siffror i Young Serif (96/64 px vid 1920); `Pris vid förfrågan` halva siffran och på radens baslinje (F-017); kontakten Geist 700 ~21 px understruken, som kortets "Boka ett möte". Ingen kicker, ingen kort rad. |

| **P17** case Calyx | `?preview=case-calyx-01`, `-03`, `-05` | `hoy-1440/hoy-webb-1440--s02.png` | `hoy-390/hoy-webb-390--s01.png` | Text vänster, produktytan höger och störst, båda halvorna bär. Hos oss: ramen ≥ 58 % vw x 88 % vh flush mot högerkanten, **utan rullningslist och utan kantlinje** (zooma 4× på över- och vänsterkant); namnet `Calyx` i Geist kursiv som i R16 (Antons beslut) + raden; **ingen kicker, ingen stegskena, ingen bildtext**; steget ryms i stagen. 390: ramen överst ≥ 50 % vh. |
| **P18** (utgången, plan 060) | Bryggan "Nästa sida säljer en kväll." är borttagen; övergången döms i P22 | | | |
| **P19** case Hōrai | `?preview=case-horai-01`, `-03`, `-06` | `hoy-1440/hoy-home-1440--s02.png` | `hoy-390/hoy-home-390--s02.png` | Spegeln av P17. Hos oss: ramen flush mot vänsterkanten, **utan rullningslist och utan kantlinje** (zooma höger-, över- och underkant); `HŌRAI` i Geist versaler med spärr som i R16; ingen kicker, ingen skena, ingen bildtext; `-03` citatet format i ramen; `-06` se P23. |
| **P20** Hōrai → pris (plan 060) | `?preview=pris-bro-skarv`, `?preview=pris-in` och hjulsekvensen 20 px ned och upp | `hoy-1440/hoy-home-1440--s08.png` | `insign-390/insign-390--s10.png` | Nästa kapitel börjar med sin rubrik utan tomt band. Hos oss: Hōrais svarta stage fortsätter i prisets svarta slöja utan kant (ΔE 0), sedan **framkallas fotot** ur det svarta (slöjans opacitet på `--sc-ps`) och **rubriken skärps** ur oskärpa, helt skarp innan den når viewportens övre 60 %; samma bildrutor baklänges. |
| **P21** prisenheten (plan 060, ersätter prisbron) | `?preview=pris` | `hoy-1440/hoy-home-1440--s08.png` | `insign-390/insign-390--s10.png` | Samma skärm som P15, dömd på ordningen: rubriken, ingressen (val A, 20 till 22 px), tre rader, kontakten. Siffrorna bildar en rytm i högerkanten, texten i samma kolumn är tydligt mindre och står på radens baslinje. All text ≥ 4,5:1 mot den renderade grunden. |
| **P22** Calyx → Hōrai (plan 060, ny) | `?preview=case-seam-text`, `case-seam-ground`, `case-seam`, plus hjulsekvensen 20 px ned och upp | `hoy-1440/hoy-home-1440--s02.png` | `hoy-390/hoy-home-390--s02.png` | Två arbeten efter varandra med luft emellan, ingen text som bryggar. Hos oss: Calyx-textspalten lämnar uppåt, sedan blir stagens papper svart **medan ramen står helt still**; stagen släpper, 18svh svart andrum, Hōrai-stagen kommer in. Ingen synlig kant mellan papper och svart någonstans; avståndet ram till ram 200 till 260 px vid 1920x930. |
| **P23** Hōrais bokning i ramen (plan 060, ny) | `?preview=case-horai-06` | `hoy-1440/hoy-home-1440--s02.png` | `hoy-390/hoy-home-390--s02.png` | Produktytan visas hel. Hos oss: RESERVATIONS / OPEN MONDAYS, BOOK.HORAI.SE och adressen **helt inne i ramen**, ingen bokstav klippt, vid 1920, 1440, 1280, 1024 och 390; vid 1920/1440/1280 syns även "Top floor · press the brass bell. No sign on the street." ovanför ramens underkant. |

## Sammanhanget, en rad till

| Id | Skärm | Referens | Vad som ska hålla |
|---|---|---|---|
| **P16** hela sidan | helsidesskivor 1440 och 1920 i kontaktark (`shots/r12/sheet-1440.png`, `sheet-1920.png`) | `hoy-1440/hoy-home-1440--s00.png` till `--s10.png` i ett kontaktark bredvid | Grunden byter material i en läsbar rytm (hoy: lila, gräddvit, röd). V3d efter plan 060: foto, blått, ritbordet, papper, **papper som blir svart inne i Calyx-pinnen**, svart andrum, Hōrais svart, **svart som framkallas till foto**, foto. Ingen skiva där två material möts i en hård kant. Vid 1920: inget tomt band > 60 % vh, inget som ser trasigt ut. |
