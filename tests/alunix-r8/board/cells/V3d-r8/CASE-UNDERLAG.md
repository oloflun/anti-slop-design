# CASE-UNDERLAG · V3d (Antons beställning 2026-09-19)

Underlag för nya casetexter (Calyx, Hōrai), nya case-rubriker och övergången till priset.
Utkastet som bygger på detta: `COPY-V3d-case-v1.md`.

Läsmetod: listsidorna och varje länkat case hämtades med curl (HTTP 200 på alla), taggarna
skalades bort, rader som återkommer på fler än 30 % av en byrås sidor (meny, sidfot, kontakt)
filtrerades bort och resten lästes i sin helhet. Inga meningar är kopierade nedan; exemplen
beskriver greppet, inte ordalydelsen.

## Vad som lästes

| Byrå | Listsida | Case lästa | Gick inte att nå |
|---|---|---|---|
| Insign | insign.se/projektarkivet/ | **80 av 80** | inga |
| Highway Media | highwaymedia.se/case/ | **7 av 7** | inga |
| Hoy | hoy.se/projekt | **35 av 35** | inga |

Anmärkningar:
- Insign: `project/tapajos-kopiera/` är i själva verket caset Nordisk Portservice (sluggen är
  en kvarglömd kopia). Ungefär 30 av de 80 casen är en enda standardmening om att sidan är
  byggd i WordPress och är responsiv, ibland med ett kundcitat. Ingen process berättas där.
- Highway: listsidan har också en rad "Våra kunder" (KL Projekt, Micans, JAB Logistic m.fl.).
  De länkar till kundernas egna webbplatser, inte till case, och räknas inte.
- Hoy: sidorna är Next.js; brödtexten finns i HTML:en. Tre case (Stora Teatern, Stigberget
  Live, Pangeo) är korta presentationer utan process.

## Insign: kort stycke, tjänstetaggar, värdeord

**Rubrik.** Bara kundens namn ("Carlakliniken", "Orust Motor"). Under rubriken en rad taggar
med levererade tjänster (Webdesign, SEO, Logotyp, UX, Fotografering). Rubriken bär ingen idé.

**Processen.** Berättas sällan. Normalformen är ett stycke: öppning "Efter ett nära samarbete
med X", sedan vad som levererades, sedan en rad värdeord som designen "speglar" (trygghet,
tydlighet, kunskap, professionalism), sist "Resultatet är en modern och lättnavigerad …".
Samma meningsbyggnad återkommer i ett tjugotal case. Kundcitat står i stället för process.

**Längd och ton.** 20 till 200 ord. Säljande, adjektivtung, byråns vi-form. Det här är den
text Anton kallar "AI:ig": värdeord utan belägg och slutsatser utan skäl.

**Det som ändå gör några case mänskliga (grepp att ta med sig):**
1. *Färger med egna namn och en roll.* Ett case namnger sina tre toner och säger vad var och
   en gör (två dova för lugn, en accent för framåtrörelse). Konkret, prövbart mot sidan.
2. *En funktion beskriven som en handling.* Ett bageri-case berättar att kunder kan spara sin
   orderhistorik och upprepa förra beställningen. Läsaren ser situationen framför sig.
3. *Kundens egen tonbeskrivning.* Ett lagerföretag ville att sidan skulle kännas som en
   inbjudan att stanna på kaffe; texten bygger färgvalet på den önskan.

**Motexempel att undvika:** "speglar verksamhetens kärnvärden", "stilren och lättnavigerad",
"en helhet där funktion och estetik samverkar". Tre adjektiv i rad utan ett enda val.

## Highway Media: målsättningar, sedan "eftersom … därför"

**Rubrik.** Tjänst + kundnamn ("Webbutveckling för VBK", "Design och webbutveckling Glenn
Hysén") eller namn + "Kundcase". Mellanrubrikerna är ofta platta tjänsteord ("Behovsanpassad
webbutveckling"); en enda sticker ut, en e-handel som får "naturnära färger".

**Processen, alltid i samma ordning:**
1. Vem kunden är (plats, erbjudande, gärna något sinnligt: havsläge, bubbelbrunch).
2. Varför de hörde av sig ("kontaktade oss med behovet av …").
3. En punktlista "Målsättningar" (tre punkter).
4. Ett eller två stycken om hur vi gjorde, ofta med en orsak framför valet.
5. Ett resultatstycke som upprepar målsättningarna i perfekt form.

**Längd och ton.** 300 till 500 ord. Saklig, men resultatstyckena glider in i samma
adjektivkedja som Insign.

**Grepp att ta med sig:**
1. *Orsaken före valet.* Ett byggkonsult-case: eftersom erfarenhet är företagets största
   tillgång fick projektsektionen en central plats. Ett val, ett skäl, en mening.
2. *En färg med en enda uppgift.* Samma case låter den blå profilfärgen bara markera det som
   går att klicka på. Regeln är konkret nog att kontrollera på sidan.
3. *Strukturen följer det besökaren vill göra.* Ett restaurang-case lyfte upp meny,
   utställare och bordsbokning i huvudmenyn för att det är vad gästen letar efter.

## Hoy: en spänning, konkreta beslut, mellanrubriker som bär en bild

**Rubrik.** Namn + ett kort påstående eller en bild: en kulturfabrik som "hela stadens
vardagsrum", ett lotteri "jorden runt", en uppföljning som frågar hur det gick sen. Sidtiteln
bär ofta en mening med verb (ett resort-case: segla ut på haven). Namnet står först, idén
efter. Det är den formen Anton efterfrågar.

**Mellanrubrikerna är det starkaste greppet.** De är korta bilder eller påståenden, inte
kategorier: "ett kvarter som ännu inte finns", ett fönster där inne blir ute, en modell byggd
i webbläsaren i stället för i gips och frigolit, "lyssna i stället för att läsa". Varje
mellanrubrik går att förstå utan brödtexten.

**Processen:**
1. En öppning som sätter en spänning: ett bostadskvarter som ska säljas innan det är byggt;
   en mässa som måste bli digital; en konsthall där konsten inte får beskäras.
2. Uppdraget i en eller två meningar.
3. Beslut, ett per mellanrubrik, med vad som valdes och varför.
4. Teknik rakt upp och ner, ofta som en kort lista (CMS, frontend, hosting).
5. Resultat med riktiga tal eller citat, när sådana finns. (Detta får vi inte göra.)

**Längd och ton.** 250 till 800 ord. Varm, lite lekfull, självsäker. Vi-form ("Hoy fick
uppdraget", "vi valde").

**Grepp att ta med sig (det som gör texterna mänskliga):**
1. *Något som valdes bort, med skäl.* En mässmonter skulle få en film; byrån lade den linjära
   filmen på hyllan eftersom en mässa handlar om att få röra, och byggde en interaktiv i
   stället. Läsaren ser beslutet ske.
2. *En fysisk detalj ur verksamheten.* Kulturhuset hade redan en profilfärg per våning (lila,
   orange, gul); webben tog över just den ordningen. Detaljen bevisar att byrån tittat.
3. *En iakttagelse om besökaren som skäl.* Ett möbel-case förklarar produktsidornas många
   länkar med att få besökare landar på startsidan; de kommer via sökning.
4. *Ärlighet om arbetet.* Ett webbshop-case säger att briefen var grov i början och att
   tester tar längre tid än man tror; ett ramverks-case att arbetet aldrig blir färdigt.
   Små medgivanden gör resten trovärdigt.

## Vad det betyder för Alunix casetexter

Dagens text (COPY-V3d-final) är redan konkret, men den känns genererad av tre skäl:
1. **Varje steg har samma form:** iakttagelse, "Därför …", och en sentens som sista mening
   ("Det sista på sidan ska vara det besökaren kom för."). Hoy varierar formen.
2. **Inget väljs bort.** Inget steg nämner ett alternativ eller vad valet kostade.
3. **Rubrikerna är symmetriska** ("Blommorna först", "Kvällen först", "Bokningen sist") och
   case-rubrikerna är bara namnen, som hos Insign.

Därför, i utkastet: namn + påstående i case-rubriken (Hoy); mellanrubriker som går att läsa
ensamma (Hoy); orsak före val (Highway); minst två bortval eller avvägningar per case (Hoy);
en fysisk detalj per steg som går att se i ramen (alla tre när de är bra); aldrig värdeord som
"speglar" eller "stilren" (Insigns motexempel). Det vi inte kan låna: kundcitat, resultat,
tal. Våra sajter är exempel för tänkta verksamheter (PRODUCT.md § Absences).

## Kunskapsbasens marknadsföringsdomän: principer för övergången till priset

Sökt med `python ~/.agents/scripts/qmdv.py` på övergång till köp, prisankring,
riskreversering, nästa steg/CTA, förtroende före pris och köppsykologi. Domänen bor i
`wiki/domains/marketing/` (valvet); den kanoniska filen är `marketing-principles.md`.
Riskreversering och garantier finns i valvet bara i snipe-leads-referenser
(`offers/references/guarantee-design.md`) och är uteslutna här: en garanti vore ett nytt
löfte. Prisankring (marketing-psychology: visa det högre priset först) används inte heller:
paketraderna och deras ordning är låsta, och ett påhittat jämförelsepris vore ett påhittat tal.

Principerna som bär övergången (sökvägar relativa till valvets `wiki/`):

1. **Hela historien först, sedan beslutet.** När läsaren har gett oss uppmärksamhet ska alla
   argument finnas i samma läsning; fakta säljer, adjektiv gör det inte.
   Källa: `domains/marketing/marketing-principles.md` § 3.5 →
   `sources/2021-09-26-founders-207-claude-hopkins-scientific-advertising.md`
   § Full story once you have attention; `sources/2023-06-05-founders-306-david-ogilvy-confessions-of-an-advertising-man.md` § More information sells.
   *För oss:* casen är den fulla historien. Övergången ska inte lägga till fler påståenden,
   bara säga att nästa fakta är priset.

2. **Skriv ut priset.** Ett smycke i ett skyltfönster utan prislapp får ingen att fråga.
   Källa: `sources/2019-07-28-founders-82-david-ogilvy-ogilvy-on-advertising.md`
   § Specific copy + always try to include price (principen § 3.2 i marketing-principles).
   *För oss:* övergången ska peka rakt på priset och inte linda in det. Rubriken säger "här är
   priset", inte "investering" eller "låt oss prata".

3. **Säljtestet: skriv som en säljare som sitter mitt emot köparen.** Skulle meningen hjälpa
   en säljare att avsluta ansikte mot ansikte? Annars stryks den.
   Källa: `domains/marketing/marketing-principles.md` § 1.1 →
   `sources/2021-09-26-founders-207-claude-hopkins-scientific-advertising.md` § Sentence test.
   *För oss:* efter att ha visat två arbeten säger en säljare ungefär "så här kostar det, och
   så här börjar vi". Övergången ska låta så, inte som en slogan.

4. **Sänk tröskeln till första handlingen.** Den som får göra något nu, med kupongen i
   fickan, gör det; intresse som skjuts upp dör.
   Källa: `domains/marketing/marketing-principles.md` § 2.1 →
   `sources/2021-03-08-founders-170-claude-hopkins.md` § Service först och § Collison install.
   *För oss:* säg vad första steget är (samtalet om verksamheten, samma som processens första
   steg) och var det börjar (adressen). Inget nytt erbjudande, bara att steget är litet.

5. **Håll det som redan är lovat, lova inget nytt.** De bästa verksamheterna håller menyns
   löfte även när det kostar.
   Källa: `domains/marketing/marketing-principles.md` § 6.3 →
   `sources/2023-06-05-founders-306-david-ogilvy-confessions-of-an-advertising-man.md`
   § Keep promises.
   *För oss:* övergången får bara hänvisa till sådant som sidan redan säger (processen, de
   tre paketen, adressen). Inga tider, rabatter, garantier eller villkor.

Kompletterande, ur `Skill(marketing-psychology)` (inte valvet): *Commitment & Consistency*
(ett litet första steg gör nästa lättare) stöder punkt 4; *Hick's Law* stöder att övergången
har en enda handling, inte flera.

## Sakunderlag ur sajterna (kontrollerat i källkoden)

**Calyx** (`sites/calyx.html`):
- Byggd som ett tidskriftsnummer: "Vol. ix · spring" i menyradens vänstra hörn, ordmärket
  centrerat i kursiv, "No. 042 · Spring Edition" bredvid heron, bildtexter med löpnummer.
- Hero: foto 88 vh (min 640 px) under menyraden, rubriken i stor serif direkt på fotot.
- Typsnitt: Cardo för rubrik och brödtext; PT Mono (jämnbrett) bara för etiketter,
  bildtexter och valutaetikett. Kursiven bär betoningen.
- Färg: krämvit grund, nästan svart bläck, en rostton (på ett namn i listan och på
  anfangerna längre ned). Mossgrönt och salvia finns i paletten men används inte i markupen.
  Ett svagt korn ligger över hela sidan.
- `#studio`: kort ateljétext, ett stort kursivt citat (sajtens eget, citeras inte av oss).
- Bildparet: två foton med mono-bildtext; det högra förskjutet nedåt från 768 px, staplade
  under det.
- `#index`: veckans utbud som lista (löpnummer, namn i kursiv, beskrivning, datum, pris till
  höger i tabellsiffror). Inga foton i listan, inga kort.
- `#commission`: mörk grund, en lång rubrik, ett stycke om hur en beställning går till
  (besökaren skriver om rummet, ljuset, måltiden; ateljén svarar med vad som finns den
  veckan; förslaget kommer i ett mejl, uttryckligen utan portal och kalenderlänk), en
  e-postadress, en besöksadress. Inget formulär.
- Sajten har påhittade kundomdömen (fiktiva för den tänkta floristen). Nämns inte i casen.

**Hōrai** (`sites/horai.html`):
- Hero: helskärmsfoto med mörk toning, 蓬莱 i små spärrade tecken ovanför namnet, HŌRAI i
  mycket stora versaler (Cinzel). I hörnet: öppetdagar, antal platser, en meny per kväll.
- Menyraden är fast och har bara ordmärket och en knapp till bokningen. Ordmärket göms så
  länge heron syns och tänds när den rullat förbi (koden: för att det krockar med den stora
  rubriken). Namnet står alltså aldrig två gånger på samma skärm.
- Typsnitt: Cinzel (romerska versaler) för rubriker och siffror, Vollkorn för brödtext,
  Noto Serif JP för tecknen.
- Färg: varmt papper, valnötsbrun, lackrött (tecken och rubrik i huset och menyerna,
  menyernas siffror och priser), jadegrönt bara för dryckestilläggen.
- Huset: stycket börjar på 18 % opacitet och tänds ord för ord i takt med scrollen; rubriken
  står i rött med ett tecken ovanför och ligger kvar (sticky) medan stycket läses.
- Citatet: 130 vh mörk sektion; meningen kommer in suddig, är skarp när sektionen står mitt i
  skärmen och suddas ut igen efter. Kopplat till scrollen i båda riktningarna.
- Menyerna: romersk siffra, namn i versaler, antal rätter, beskrivning, vilka dagar,
  pris per gäst i rött och större än namnet. Ingen à la carte; en meny per kväll.
- Bildpar med två rätter, bildtext med meny och rätt.
- Rummet: foto över hela bredden, mörk toning från vänster, text direkt på bilden.
- Bokningen: mörk grund, rubrik med "öppnar på måndagar" i rött, när platserna släpps, länk
  till bokningen, en e-postadress för det som inte passar i ett formulär, adressen och att
  huset saknar skylt mot gatan.

**Iakttagelse om prisingressen:** `runs/V3d/index.html` rad 1856 har "Två av tre paket har
ett pris utskrivet här. Det tredje beror på omfattningen." medan COPY-V3d-final har "Två paket
har priset utskrivet. Det tredje beror på vad ni behöver." Utkastet rör ingen av dem men
skriver övergången så att den inte krockar med någondera.
