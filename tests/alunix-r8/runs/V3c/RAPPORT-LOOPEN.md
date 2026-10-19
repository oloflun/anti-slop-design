# Rapport: V3c-bygget, varje runda och varför resultatet blev så litet

Skriven av lead 2026-09-18 på Antons begäran, före bygget av den inverterade varianten.
Källorna är `NOTES.md`, `plans/README.md`, `HELHET.md` och `reviews/loop-1..5-astra.md`.

## Kort svar

Du har rätt. Utanför processakten ser sidan i stort sett ut som när vi började. Det berodde
inte på otur, utan på hur jag satte upp loopen. **Loopen mätte om sidan fungerade, inte om
den var bra.** Den kunde sedan säga "klart" utan att sidans komposition hade ändrats. Fem
beslut gjorde det, och alla var mina:

1. **Referensgolvet mätte fel saker.** `HELHET.md` fick 35 rader. Ungefär två tredjedelar
   är tekniska trösklar: millisekunder per bildruta, procent per scrollsteg, pixelavstånd i
   skarvar och kontrastkvoter. De tre raderna som krävde en ny komposition parkerades som
   fråga Q30 till dig. Det var H-02 (varje akt äger sin egen skärm), H-03 (grunden byter
   material) och H-08 (ett dominerande element per skärm). Jag lät ändå loopen avslutas
   medan de stod öppna.
2. **Jag förbjöd granskaren att ha smak.** När jag skrev om `agents/codex-review.md` gav
   jag Astra uppdraget "aldrig en estetisk omstyrning" (rad 52 och 162). Därför kunde Astra
   bara hitta fel. När den till slut svarade `ship` betydde det "inga buggar kvar", inte
   "nivån är nådd".
3. **Visuellt kom alltid sist.** Varje runda sorterade planerna funktion → states → flöde
   → visuellt → kod, med högst åtta planer. Funktionsfelen fyllde platserna först, så
   visuella förbättringar trängdes ut runda efter runda.
4. **Vi lagade våra egna fel.** Ramarnas sövning (plan 018, R6) gav upphov till fem
   följdplaner på fyra rundor: 026, 027, 031, 035 och 036, plus 043 för Calyx. Ingen av dem
   syns för en besökare. De återställer bara det som fungerade före 018.
5. **Varje djärvt drag backades i stället för att lagas.** Jätterubriken gick från 96 till
   88 px när ordet bröts, i stället för att brytningen lagades. Grunddriften gick 62 → 40 →
   24 % när den blev för blå, alltså tillbaka nästan till gråskalan vi började med. Kvar
   blev en sida som liknar utgångsläget.

Till det kommer processaktens form, som är just det du nu kallar en rullande paragraf. Jag
förklarar den under R6.

## Runda för runda

Med "syns" menar jag om en besökare utan mätverktyg skulle se skillnaden.

### Fas 0 och fas A (15/9): underlaget

**Gjort:** Servrarna startades och kortvändningen fotograferades vid fem lägen. Arkitekten
(Fable) läste 228 skärmbilder av V3c, K3, insign, highwaymedia och hoy. Därefter skrev
arkitekten `HELHET.md` och lade in highwaymedia och hoy i katalogen.

**Motivering:** Planen krävde att arkitekten läste pixlar, inte minnen, och satte ett golv
som loopen kunde bocka av.

**Vad som gick fel:** Arkitekten såg rätt sak i referenserna. Hoy ger varje kapitel en egen
skärm i full bredd, och det står i HELHET § 1. Men golvet skrevs som kontrollerbara
påståenden, och det som är lättast att kontrollera är tal. Kompositionsskillnaden mot hoy
blev en fråga till dig i stället för en plan. **Syns:** ingenting, det här var underlag.

### R4 (15/9): åtta fixar på den gamla sidan

**Gjort:** Planerna 001–008. Folden klipptes inte längre vid låg skärmhöjd. Ramarna slutade
stjäla scroll och tabb. CLS vid 390 gick till 0. Kortets kant klipptes inte längre, och
signaturaktens bildtid förbättrades. Kickern kom tillbaka på kortets baksida, avslutet fick
en egen yta och Hyperborea-plåten fick sin bleed.

**Motivering:** Rena fel från V3b som stod i vägen innan processakten kunde byggas.
**Syns:** lite. Plåtens bleed och avslutets yta märks, resten är korrigeringar.

### R5 (15/9): processakten byggs

**Gjort:** Plan 010. Ett SVG-ark i sju tillstånd, ritat på `--sc-ps`, med fråga och svar
per steg. Plan 011 gav kortvändningen spannet 3,4.
**Motivering:** Din beställning. **Syns:** ja, det här är den stora förändringen.

### Granskningen efter R5 (16/9): fem rapporter

Kvartetten och Astra gav 40 fynd, och de flesta togs (tabellen i `plans/README.md`).
Samtidigt sa du att stegen var fråga och svar i stället för riktiga beskrivningar. Jag
skrev `PROCESS-UNDERLAG.md` ur referenserna.

### R6 (16/9): processakten görs om till prosa. Här började "den rullande paragrafen"

**Gjort:** Plan 019 lade stegen som prosa i flödet, med arket sticky bredvid eller ovanför
och copy v1. Plan 020 rättade arkets geometri. Därtill kontrast (021), kortets fokus (022),
liggartråden (023) och ramarnas sövning (018).

**Motivering, som den stod:** a11y-granskaren visade att PageDown hoppade över steg 02, 04
och 06, och att två stegtexter kunde ligga ovanpå varandra. Prosa i flödet löste båda utan
hållfönster. Sektionens höjd blev textens, så steg 07 kunde inte hamna utanför.

**Vad det kostade:** Varje steg blev ett stycke i brödtextstorlek, med en liten rubrik och
en marginalrad, utan egen skärm och utan egen scen. Arket står still i 480–560 px medan
texten rullar förbi. Tillgänglighetsproblemet hade kunnat lösas med en scen per steg, med
riktig höjd och text i DOM:en. Jag valde den billigaste lösningen på a11y-fyndet och vägde
aldrig av den mot slagkraften. **Syns:** ja, men åt fel håll för det du ville ha.

### Loop 1 = R7 (17/9): den enda runda som syntes

**Arkitekt och Astra:** Astra svarade `rebuild` med åtta fynd.
**Gjort:** Processakten fick railmarginal och rättade fönster (025). Grunddriften, 96 px
spaltoffset och skarvar kom med 017, och mobilordningen med 012. Prisblocket fick ett
grafitplan (013) och jätterubriken 6 rem (014). Avslutet fick en hårlinje och **mailto 2 →
6 rem** (015). Kortbaksidan fick en A-glyf (016), och ramarnas montering gjordes idempotent
(026).
**Motivering:** H-raderna 04, 05, 07, 09, 11, 12 och 19. **Syns:** ja: driften, prisets
plan, rubriken, glyfen och adressen.

**Adressens storlek kommer härifrån.** H-12 krävde "minst 64 px glyfhöjd". Talet valde
arkitekten för att avslutet skulle kännas som ett eget ögonblick. Det är inte mätt mot
någon referens, och jag granskade aldrig om 6 rem var rätt storlek. Det var inte rätt.

### Loop 2 = R8 (17/9): tre rader visuellt, fem rader lagning

**Astra:** `fix` med tre fynd. **Gjort:** Ramarna vaknade aldrig efter R6 (027). Därtill
bildtiden (028), processaktens ankare (034), ramarnas reveal (031) och prisliggarens
hårlinjer på scroll (033). **Driften backades** 62 → 40 % (029) och **rubriken backades**
6 rem → 88 px (030) sedan ordet brutits "VARUMÄRK-E.". Folden vid 390 rättades (032).
**Motivering:** Mina egna pixelfynd efter R7 fick gå först: ramarna var tomma, driften var
en blå tvätt och ordet bröts. **Syns:** Driften och rubriken blev mindre än i R7, och
hårlinjerna tillkom.

### Loop 3 = R9 (17/9): nästan bara följdfel

**Astra:** `fix` med sex fynd. **Gjort:** Revealens latch var vägberoende (035). Revealen
fick inte klippa levande ramar (036), previewlägena fick sikta rätt (037) och kortets
tillstånd läste fel värde (039). Arkets kontur rättades (040), **driften backades 40 → 24
%** (038) och skrivningen flyttades (041).
**Motivering:** Latchen som R8 byggde fungerade bara med mushjul, inte med PageDown. Det
var ett riktigt tillgänglighetsfel. **Syns:** i praktiken ingenting, driften är nu nästan
gråskala igen.

### Loop 4 = R10 (17/9): tre osynliga fixar

**Astra:** `fix` med tre fynd. **Gjort:** Prisblockets platshållare fick sidan att krympa
297 px (042). Calyx-revealen hade ingen öppning (043), och driftens överlämning hoppade i
en bildruta (044).
**Syns:** nej.

### Loop 5 = R11 (17/9): `ship`

**Astra:** `ship` med noll fynd. Samtidigt skrev Astras egen § ceiling att hoy "fortfarande"
skiljer sig genom en auktoritet per kapitel i full bredd. Granskaren såg alltså gapet men
fick inte kalla det ett fynd. HELHET låg på 29 av 35, och de sex öppna var kompositionen
(Q30) och bildtiden. **Jag godtog slutvillkoret.**
**Gjort:** Bara din beställning, `?process=invert` som läge i samma fil (045).
**Syns:** bara via en URL-parameter som boarden inte skickar vidare. Därför kunde du inte
se den.

### Copy-gaten, R12 och R13 (17/9)

Copy-gaten körde fem pass med humanizer-svenska sist, och fjorton rader skrevs om. R12
gav Calyx färg i steg 06 (046). R13 fick arket att sluta täcka texten mellan 768 och 1279
px (047). Det var ett fel som hade funnits sedan R6 och som ingen runda hade fångat.
**Syns:** Calyx färg, ja. R13 bara i mellanbredder.

## Summan i tal

| | Planer | Syns för en besökare | Lagar något vi själva orsakat |
|---|---|---|---|
| R4 | 8 | 2 | 0 |
| R5–R6 | 8 | processakten (2 former) | 0 |
| Loop 1–4 (R7–R10) | 26 | 7, varav 3 backades senare | 9 |
| R11–R13 | 3 | 1 (Calyx färg) + invert bakom en parameter | 1 (R13) |

Fyra looprundor gav sju synliga ändringar, och tre av dem drogs tillbaka. Sidans struktur är
densamma: hero, tesband med jätterubrik bredvid Calyx, pris bredvid Hōrai, processen och
avslutet. Kompositionsfrågan mot hoy lämnades öppen hela vägen.

## Vad jag gör annorlunda nu

Du vill se större resultat på färre försök. Så här ändrar jag upplägget för den nya
varianten:

1. **Dina krav är golvet, som synliga mål.** Varje punkt i din beställning blir en rad med
   ett visuellt mål mätt i skärmbild. Exempel: arkets storlek som andel av viewporten, hur
   stor del av arkets öppning Calyx fyller, stegrubrikernas storlek, att varje steg äger en
   egen skärm och adressens storlek. Inga millisekundrader avgör om något är klart.
2. **Granskaren får ha smak.** Astra får nu uttryckligen döma estetiken. Varje skärm från
   oss visas bredvid motsvarande skärm hos hoy och highwaymedia, i samma bild. `ship` kräver
   att Astra skriver att skärmen håller referensens nivå, inte bara att inget är trasigt.
3. **Visuellt först.** Byggrundan gör alla dina ändringar i en plan, i ordningen du gav
   dem. Tekniska fel som uppstår lagas inom samma runda, och ett djärvt drag backas aldrig
   för att laga ett fel.
4. **En stor byggrunda, högst två fixrundor.** Ingen runda räknas som klar om den bara lagar
   följdfel.
5. **Processakten blir scener, inte en paragraf.** Varje fas får en egen skärm med stort
   stegnummer och rubrik i displaystorlek, och texten tonas in mot arket. Texten ligger
   kvar i DOM:en, så att PageDown och skärmläsare fungerar. Det var tillgänglighetsskälet
   till prosan, och det går att uppfylla utan att offra scenen.
6. **Jag jämför själv, sida vid sida.** Före varje "klart" läser jag varje skärm bredvid
   referensens motsvarighet. Det räcker inte att bocka av rader.
