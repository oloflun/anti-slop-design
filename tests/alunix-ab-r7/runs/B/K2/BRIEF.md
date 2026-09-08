# BRIEF.md — Alunix K2 Affischen, runda 1 (referenspaket, ingen kod)

Skriven av Claude (Sonnet) efter läsning av alla källor nedan, i den ordning orkestreraren
angav. Riktningen är låst till `concepts.md` § K2 Affischen v2; den här filen preciserar
grammatik, feeling curve, device-tabell, fingerprint, reduced motion, `?preview=`, typsnitt
och palett innan någon HTML skrivs.

---

## 1. Referensdigest

Tre rader per fil: vad den säger som spelar roll här · vad jag tar med · vad jag avvisar
och varför.

**`SKILL.md` (Step 0, 1, 1b, 2, 2b, 4, § Motion).**
Säger: brand härleder riktning, skills levererar hantverk; auktoritetsregeln (en sak per
sida); Step 2b kräver grammatik + feeling curve + signaturrörelse + fingerprint innan bygge.
Tar med: hela Step 2b-kedjan blir denna BRIEF; "en auktoritet, resten viker" styr varje
sektion. Avvisar: macrostructures/themes (Tier 3-material) — K2 är Tier 2 (referens:
katalogen), inget att uppfinna fritt.

**`design-catalogue/TASTE.md`.**
Säger: en auktoritet per sida (§1); tyst typ↔stark bild, stark typ↔tyst yta (§2.1); ett
papper en accent (§2.2); hårlinjer inte kort (§2.3); skala 5-15× (§2.4); två snitt roller
korsar aldrig (§4.2). Tar med: hela §4 som facit för varje typ/bild-beslut nedan. Avvisar:
kategorin "portfolio/studio"s CTA-fyllnad — K2 har ingen knapp alls, bara typsatta länkar.

**`design-catalogue/FEEDBACK.md` (F-001–F-009).**
Säger: reservläget måste bära sekvensen som egna sektioner (F-001); målets vila får inte
förhandsvisa slutläget (F-002); K2 hade två auktoriteter förut, för mycket (F-003); heron
behövde en plate bredvid ordmärket (F-004); typsnittsblandningen i en av r6-körningarna var
förebild (F-005); referenserna måste faktiskt läsas (F-008). Tar med: F-001–F-005 direkt
in i sektion 9/11 nedan. Avvisar: F-006/F-007 gäller K3/K1, ingen direkt tillämpning på K2
utom som generell varning mot AI-slop-troplistan.

**`references/reference-lock.md`.**
Säger: lås primär referens + 1-2 lånade detaljer före kod; anti-averaging (dominant riktning,
inte medelvärde av tre källor); token-roll följer med token, separeras aldrig. Tar med: hela
metoden för sektion 3 nedan. Avvisar: att låta Spring/Summer och Indoek "mjukna" mot en
gemensam mellanväg — checkat mot anti-averaging-testerna innan leverans.

**`references/house-physics.md` (Structural + Motion).**
Säger: 8-10 namngivna tokens, en mättad accent i displayskala; hårlinjer separerar, ytor
gör inte; minst tre sektionsanatomier; en tonal inversion; signaturrörelsens mål är tyst i
vila och tänds vid första scroll, reduced motion visar formade lägen som egna sektioner.
Tar med: exakt detta för akt 1 (fönstren) och akt 7 (inversionen). Avvisar: grain film och
kicker-apparaten som "alltid" — K2 är typographic poster, inte editorial print; ingen grain.

**`references/scroll/README.md`.**
Säger: Step 2b körs bara på Persuade/Experience-ytor; motorn är opt-in per grammatik; K2:s
egen signaturrörelse ska kodas bespoke, aldrig som en kit-parameter. Tar med: att motorn
(`scrollcraft.js`) bara används om grammatiken kräver scrub/pin/pan — K2:s pin-akt kvalar in.
Avvisar: att blint kopiera `template.html`:s sju-akts-partitur — vår akt-form är egen.

**`references/scroll/grammars.md`.**
Säger: typographic poster = ordmärke i kompositionsskala, förbjuder scrim/kort/fotogrund/
parallax på text; register×grammar-tabellen listar "editorial print" som en av grammatikens
naturliga hem. Tar med: alla åtta förbud rakt av (se sektion 4). Avvisar: filmic one-shot,
continuous world, live surface, gallery/catalog, split stage, chaptered editorial, rhythmic
cutlist — varför i sektion 4.

**`references/scroll/devices.md`.**
Säger: nio devicefamiljer, cue-kontraktet (greet på hero, hold bara sista akten, ground-or-
greet), aldrig samma device två gånger i rad, ≤2 scrub. Tar med: hela tabellen för sektion 7.
Avvisar: `scrub` helt — K2 har noll videoklipp, bespoke mask-glid räknas som `pin` med
staplat beteende, inte som `scrub`-enheten.

**`references/scroll/feel-and-fingerprint.md`.**
Säger: feeling curve före akter; en peak som får mest scrollutrymme och tystnad före sig;
"tell-someone"-testet; fingerprint mot registret, ≥4/6 skiljer per rad. Tar med: formatet
rakt av för sektion 5, 6 och 8. Avvisar: att skriva peaken som en enhetsnamn ("det har en
pin-effekt") — måste vara en mening en besökare skulle säga.

**`scripts/scroll/NOTE.md`.**
Säger: `scrollcraft.js`/`.css` kopieras byte-identiska, temas bara via sex tokens + två
typsnitt, bespoke beteende läser `--sc-p` och skriver egna `data-sc-*` utan att röra motorn.
Tar med: exakt denna gräns för runda 2:s kod. Avvisar: att restyla `.sc-stage`/`.sc-copy`
direkt (AB06-varningen i `devices.md`) — allt bespoke går via egna klasser.

**`scripts/scroll/template.html`.**
Säger: skelettets akt-ordning (scrub>pin>flow>scrub>pan>pin) är EN partitur, inte en mall att
fylla i; fyra+ familjer, aldrig samma två i rad, sista akten är sidans sista element. Tar med:
strukturprincipen (kopiera motorn, skriv egen markup). Avvisar: exempelaktens konkreta
sekvens rakt av — K2:s egen sekvens är pin→reveal→flow→reveal→flow+drift (sektion 7).

**`concepts.md` § K2 Affischen v2.**
Säger: hela målbilden — auktoritet typen, signaturrörelsen "papperet skjuts och blocket
andas", sju akter, förbjudet-listan, fingerprint mot r6 B-K2 (redan räknat till 4/6). Tar med:
målbilden är låst; denna BRIEF preciserar den, ersätter den inte. Avvisar: inget — men jag
omfördelar de sju känslo-raderna över färre faktiska scroll-akter (se sektion 7, motivering).

**`design-catalogue/entries/springsummer/entry.md`.**
Säger: femfärgstak utan accent; Grotesk crushed till 0,75 line-height, en vikt, 170-386px;
Montreal för allt annat inkl. en 43px "stor caption" utan egen mellannivå; typografiska pilar
utan knappram; live klocka+ort typsatt i nav. Tar med: crushed leading-principen, femfärgstak,
klocka-i-nav-mönstret, pilarna. Avvisar: `#fe3939`/`#dedcd3`-hexen och typsnitten Grotesk/
Montreal rakt av — härleds om till Alunix egen sagepapper-värld.

**`entries/springsummer/fold.webp` + `slices/00-05.webp`.**
Säger (bilder): "WE WON" i krossad 0,75 leading, bokstäverna nästan rör vid varandra; en
horisontell projekt-karusell med bildkort som glider ut mot högerkanten; klientloggar som
gråa rektanglar utan skugga; ett inverterat mörkt fotslut. Tar med: den krossade radhöjden
som facit för ALU/NIX-blocket; klientlogg-rutnätet avvisas men "ingen skugga, ingen rundning"
håller. Avvisar: karusellen (K2 har inget produktsortiment att bläddra i) och den röda accenten
(K2:s femfärgstak har ingen kromatisk accent alls, bara papper/bläck/vitt/två gråa).

**`entries/springsummer/extract/springsummer-dk-DESIGN.md`.**
Säger (mätt, designlang): h1 331,84px vid line-height 248,9px (kvot ≈0,75, bekräftar entry.md);
bara 4 unika färger uppmätta live; körsnittsdata visar Supply/Montreal dominerar, inte Grotesk
— ett varnande exempel på att en sajt kan byta look efter capture. Tar med: kvoten 0,75 som
en riktig, uppmätt siffra, inte en gissning. Avvisar: att lita på en enda mätning utan att
korsläsa entry.md:s "vad som fortfarande stämmer"-resonemang — gjort ovan.

**`design-catalogue/entries/indoek/entry.md`.**
Säger: ett enda typsnitt, hierarki bara genom skala; ett bläckblått ink, allt annat är foto;
ordmärket "INDOEK" har ett foto maskat genom bokstävernas öppningar, samma objekt, inte
lager på varandra; handel och redaktionellt delar samma linjerade rutnät utan kort. Tar med:
just masknings-principen (foto genom bokstävernas öppningar) för ALU/NIX-fönstren — kärnan
i K2:s signaturrörelse. Avvisar: enda-typsnitt-regeln rakt av (se § Typsnitt nedan, öppen
fråga) och det bläckblåa som en identisk paletthärledning.

**`entries/indoek/fold.webp` + `slices/00-11.webp`.**
Säger (bilder): "INDOEK" i konturerad outline-typ, ett fönster av produktfoto slice:at genom
mittenbokstäverna; under fold ett strikt linjerat rutnät av bok-/produktkort, ingen rundning,
ingen skugga, en enda blå ink genomgående inkl. prislappar; "About Us"-stycket i tredje
person. Tar med: fönster-genom-bokstav-tekniken, det strikta hårlinjerade rutnätet som facit
för bevisakten och liggarna. Avvisar: outline-typsnittet i sig (för tunt för att bära vikt
300, se TASTE §2.1) och den enda-inkt-paletten (K2 har ingen kromatisk accent alls, till och
med blått skulle vara "en sjätte färg").

**`entries/indoek/extract/indoek-com-DESIGN.md`.**
Säger (mätt): en primärfärg `#135eab` (857 träffar), bakgrund `#efebe3`; en enda typografisk
familj (Calibre, 1160 träffar) dominerar helt, h1 uppmätt till bara 16px (skalan sitter i
bildstorlek, inte i CSS-heading-storlek — mätningen missar wordmark-SVG:n). Tar med: att
hierarkin verkligen bara körs på skala, bekräftat oberoende av entry.md. Avvisar: att kopiera
mätningens hex/font-namn — samma regel som ovan.

**`assets/credits.json`.**
Säger: `plate-desk.webp` är Ricardo Loaiza, Unsplash, licens "Unsplash License". Tar med:
korrekt fotografkredit till sidfoten/kolofonen i runda 3 — inte "Annie Spratt" som i r6:s
kod (annan bild, annan runda). Avvisar: inget att avvisa, ren attributionsdata.

**`tests/alunix-ab-r6/runs/A/K2/index.html`.**
Säger (koden): en riktig `inkScan()`-funktion som renderar bokstaven till en canvas och läser
alfakanalen för att bygga SVG-mask-polygoner ur den faktiska bläckformen (A/U/X), inte en
gissad rektangel; fönstren ligger i bokstävernas ÖPPNINGAR (A:s hål, U:s ring, X:s kilar).
Tar med: hela tekniken rakt av för runda 2:s fönster — det är den enda bevisade lösningen på
"foto genom bokstav" i det här repot. Avvisar: A-K2:s enda-plate-yta (ingen plate bredvid
ordmärket i den byggen — det är just vad F-004 klagade på).

**`tests/alunix-ab-r6/runs/B/K2/index.html`.**
Säger (koden): en rektangulär bildpanel `left:30%` som glider vertikalt BREDVID bokstäverna
(inte maskad genom dem); blocket "andas" genom att font-size/line-height lerpas kontinuerligt
0,78→0,92 istället för ett diskret kinetic-steg; ETT typsnitt (Archivo, variabelt) för allt —
motsäger F-005:s "två snitt"-beröm och TASTE §4.2, se § Typsnitt nedan (öppen fråga). Tar med:
dokumentationsstilen (pre-emit-kritik i en kommentarsrad, reference-lock skriven i huvudet)
och liggar-mönstret för tjänster/pris (hårlinjer, `--q`-styrd clip-path). Avvisar: panelen
bredvid (ej maskad) och enda-typsnittet — se motivering nedan.

**`tests/alunix-ab-r7/runs/B/K2/assets/` (lista + credits.json).**
Innehåller: `plate-desk.webp` (Ricardo Loaiza), `demo-calyx.webp`, `demo-horai.webp`,
`demo-hyperborea.webp` (de tre exempelsajternas förstascreenshots), `logo-white.svg`,
`logo-black.svg`. Tar med: alla sex filer används som de är, ingen egen bildhämtning. Avvisar:
inget saknas för K2 — inget rörelsematerial behövs (det är K1:s `push/`-mapp, inte relevant
här).

---

## 2. Auktoriteten

**Auktoriteten är typen** (TASTE.md §1, rad "Typen (ordmärke eller rubrik i viewport-bredd)").
Namngiven enligt tabellen: ordmärket ALU/NIX i affischskala, en vikt, stram, bär hela sidans
första skärm.

**Vad som viker för den:**
- **Fotot** → en enda dämpad svartvit dokumentär-plate i högerspalten, aldrig under
  ordmärket, aldrig fullbredd (F-004).
- **Färgen** → ingen kromatisk accent alls. Femfärgstaket (papper/bläck/vitt/hårlinje stark/
  hårlinje svag) har inget "en sak"-jobb att göra, för det finns ingen knapp och inget CTA-
  ord att färga.
- **Ytan** → flat papper, ingen textur, inget grain (grammatiken förbjuder scrim/fotogrund
  bakom text; TASTE §2.3 kräver hårlinjer inte kort).
- **Siffrorna** → tjänstenumren (01-03) och priserna är kickers/liggarrader, aldrig i
  ordmärkesgrad (F-003:s lärdom: två auktoriteter på samma skärm är ingen).
- **Rörelsen** → tyst utom i signaturakten, där den enligt TASTE §4.8-preciseringen får vara
  medauktoritet: där viker typen (300, om den fanns) och bilden (suddig/reser); i K2:s fall
  betyder det att blocket självt tillfälligt "blir" rörelsen genom att krossas/andas, men typen
  förblir densamma bokstavsform hela tiden — den byter aldrig vikt eller läsbarhet.

---

## 3. Reference-lock

```text
Primary reference/direction: Spring/Summer (springsummer.dk) — krossad affischtyp i
  affischskala med femfärgstak och en typsatt, obetonad klocka i navraden.
Preserve: crushed leading (~0,75) på affischtypsnittet tills raderna nästan rör vid varandra;
  exakt fem färger totalt, ingen sjätte, ingen kromatisk accent; typografiska pilar utan
  knappram som enda länkstil; riktig klocka+ort typsatt i navraden, ingen widget/badge;
  4px-liknande hårradie som enda avrundningsvärde (K2 sätter taket lägre, ≤2px, se Förbjudet
  i concepts.md).
Borrow only: Indoeks foto-genom-bokstav-teknik (masken mätt ur bläcket med canvas-alfaskan,
  A-K2:s bevisade kod) — körd med exempelsajternas skärmbilder istället för produktfoto;
  Indoeks "handel och redaktionellt i samma linjerade rutnät" lånas som "tjänster och priser
  i samma liggarform".
Role rules: displaytypsnittet sätter ALDRIG kroppstext, kickers eller nav; registertypsnittet
  sätter ALDRIG rubriker i affischgrad; ingen sjätte färg introduceras, inte ens som CTA-
  färg (det finns ingen knapp att färga); den svartvita platen är alltid dämpad/gråskala,
  aldrig en färgbild.
Media strategy: product surface — de tre exempelsajternas riktiga skärmbilder (redan
  vendorade i assets/) i fönstren och i bevisakten; photo:unsplash (vendorad, Ricardo Loaiza,
  se credits.json) för den enda dokumentära platen bredvid ordmärket.
Reject: Spring/Summers faktiska hex (#fe3939/#dedcd3/#000000) och typsnitt (Grotesk/
  Montreal) rakt av; Indoeks faktiska hex (#03315C/#EEEBE3) och Calibre rakt av; en
  rektangulär bildpanel som ligger BREDVID bokstäverna utan att vara maskad ur dem (r6 B-K2:s
  lösning — för svag som bärare av "auktoritet: typen", läser som ett fönster råkar överlappa
  en logga snarare än att logotypen ÄR fönstret); ett enda typsnitt för hela sidan (r6 B-K2:s
  val, se § Typsnitt, öppen fråga mot F-005/TASTE §4.2).
Token commitments: paper (sage, botten hela sidan utom inversionen); ink (bläck, text +
  inversionens botten); white (den enda plåtytan: platen, iframe-bakgrunder); line-1 (stark
  hårlinje på papper); line-2 (dämpad text/hårlinje, egen kontrastmätning per botten — se
  gate om muted-tone-per-ground i house-physics.md).
```

### Beslutsledger

| Beslut | Källa | Roll att bevara | Varför |
|---|---|---|---|
| Krossad leading (~0,75) på ALU/NIX | Spring/Summer (primär), mätt i `springsummer-dk-DESIGN.md` | display-only, aldrig kroppstext | Affischen ska läsas som tryckt, inte satt av CSS-default |
| Foto maskat genom bokstävernas öppningar | Indoek (lånad detalj) + A-K2:s bevisade `inkScan()`-kod (samma repo) | fönster-only, körs aldrig som bakgrundspanel | Gör logotypen till objektet, inte ett fönster som råkar ligga bredvid den |
| En dämpad plate bredvid ordmärket, aldrig under | Antons dom, F-004 | hero-only, en gång på sidan | Explicit orkestrerad korrigering efter r6 |
| Femfärgstak, ingen accent | Spring/Summer (primär) + TASTE §2.2 (undantag: K2 har noll accent, inte en) | palett-only | Ingen knapp finns att färga; en accent utan jobb är brus |
| Tjänster/pris som liggare med hårlinjer | Indoek (rutnät utan kort) + TASTE §2.3 + husfysik "ledger, never card grid" | liggar-only | Håller sidan som ett tryckt dokument, inte en app |
| Två typsnitt, roller korsar aldrig | TASTE §4.2 + F-005 (regel) — se öppen fråga om vilken r6-körning som faktiskt visade detta | display-only vs register-only | Bindande regel; B-K2:s enda-typsnitt avvisas trots att den är den fil orkestreraren pekade ut för "typsnittsvalen" |

**Anti-averaging-kontroll:** Spring/Summer (krossad affischtyp, ingen accent) + Indoek (ett
foto genom bokstäverna) väger INTE ut mot en mjuk mellanväg — de kombineras genom att låta
Spring/Summers regel (femfärgstak, ingen accent, crushed leading) vara dominant och Indoeks
bidrag vara en enda namngiven teknik (masken), inte en stilöverföring av Indoeks egen palett
eller typsnitt. Identitetstestet: byt ut ALU/NIX mot vilken byrås namn som helst — sidan
förblir specifik genom exempelsajternas riktiga skärmbilder i fönstren, inte genom en
utbytbar bild.

---

## 4. Grammatik

**Vald grammatik: Typographic poster.**

Register×grammatik-tabellen (`scroll/grammars.md`) listar typographic poster som en av tre
grammatiker som passar editorial print (K2:s register, ärvt från Spring/Summer). De andra
sju, i en mening var:

1. **Filmic one-shot** — förlorar: K2 har ingen enda linjär emotionell resa genom ett filmiskt
   klipp, det är en affisch, inte en biofilm.
2. **Chaptered editorial** — förlorar: sidan har inget kapitelinnehåll av substans (metod,
   manifest), den är en kort säljande affisch.
3. **Live surface** — förlorar: grammatiken förbjuder marknadsföringschrome och kinetiska
   rubriker rakt av, exakt det K2 bygger på.
4. **Continuous world** — förlorar: det finns ingen verklig geografi att röra sig genom,
   bara en affisch och en liggare.
5. **Gallery/catalog** — förlorar: K2 har ett enda argument (auktoritet: typen), inte ett
   sortiment av jämlika objekt i eget tempo.
6. **Split stage** — förlorar: det finns ingen tvåsidig jämförelse att väga mot varandra.
7. **Rhythmic cutlist** — förlorar: grammatiken kräver 12-20 korta klipp i högt tempo, motsatsen
   till en tyst, tung affisch med en enda krossad rubrik.

---

## 5. Feeling curve

En rad per akt: känsla → vad på skärmen orsakar den. Peaken namngiven. Tell-someone-mening
sist.

```
1  Tyngd       ALU/NIX i affischskala, krossad radhöjd, klockan går på riktigt, Calyx
               redan synlig i fönstren, platen tyst bredvid.
2  Byte        bilden bakom masken glider vertikalt medan bokstäverna står stilla —
               Calyx försvinner, Hōrai fyller samma öppningar, sedan Hyperborea.
3  Andning     blocket släpper: radhöjden går från 0,75 till 1,0, raderna glider isär
               till en ny rubrik som står kvar.
4  Bevis       tre uppslag glider in ur var sin sida, gråskala tonar till färg när
               uppslaget når mitten av skärmen — bevis blir levande en gång.
5  Lista       tjänsterna dras fram radvis, hårlinjer, siffran liten.
6  Räkning     priset landar från höger i displaygrad, sista raden bara ett ord: "Pris
               vid förfrågan".
7  Vila        grunden går från papper till bläck, sista raden är den minsta typen på
               hela sidan.
```

**Peaken: akt 2-3 (Byte→Andning).** Detta är signaturrörelsen och får mest scrollutrymme
(`data-sc-span` störst på sidan) och tystnaden före den (akt 1 håller helt stilla, klockan
är den enda rörelsen). Den engineered peak-tabellen (feel-and-fingerprint.md): asset-budget
= de tre skärmbilderna i högsta kvalitet redan vendorade; tystnad före = akt 1:s stillastående
affisch; mest scrollrum = det enda `pin`-spannet på sidan.

**Tell-someone-meningen:** *"Det är sidan där bokstäverna i ordmärket är riktiga fönster —
du bläddrar tre exempelsajter genom hålen i A, U och X, och när du släpper trycker hela ordet
ihop sig till en ny rubrik."*

---

## 6. Signaturrörelsen

**En mening:** Bilden bakom en bokstavsmask mätt ur det faktiska bläcket glider genom
öppningarna i A, U och X medan ordmärket står stilla, och när scrollen släpper öppnar sig
blockets krossade radhöjd till nästa rubrik — typen är hela tiden objektet, aldrig bakgrunden.

**Hur den hänger i sidans motiv:** K2:s hela idé är "sidan som en tryckt affisch"; en tryckt
affisch kan inte animeras, men den KAN bläddras, precis som Spring/Summers projektkarusell
eller Indoeks roterande skyltfönsterfoto. Signaturrörelsen gör bokstävernas öppningar till
just ett skyltfönster (Indoek-principen) samtidigt som den håller Spring/Summers krossade
typografi som den enda display-auktoriteten på skärmen — de två lånade principerna möts i en
enda rörelse istället för att ligga som två separata effekter.

---

## 7. Device-tabell

Sju känslo-rader (sektion 5) fördelas över **fem faktiska scroll-akter** — akt 1-3 delar en
enda pinnad hero (samma sätt som r6:s båda K2-byggen redan gjorde: en sammanhängande sticky-
region, inte tre separata sektioner). Motiveringen: devices.md tillåter att en pinnad scen
staplar flera enheter ("a pinned stage can hold a scrub clip, a parallax layer, a kinetic
headline... at once"), och ordmärket måste förbli samma DOM-element genom hela byte+andning
för att masken och den krossade radhöjden ska vara samma objekt, inte två utbytta sektioner.

| Scroll-akt | Känslo-rader | Device | Familj | Varför |
|---|---|---|---|---|
| A (hero) | 1 Tyngd, 2 Byte, 3 Andning | `pin`, span ~3.0, bespoke mask-glid på `--sc-p` (Calyx→Hōrai→Hyperborea) staplat med `kinetic` (lines) på rubriken när blocket öppnar | **pin + kinetic** | Ordmärket måste stå still medan bilden bytes bakom det; öppningen till nästa rubrik är en linjebaserad reveal, inte ett nytt videoklipp — noll `scrub`-enheter används alls |
| B (bevis) | 4 Bevis | `reveal` per uppslag (wipe vänster/höger, gråskala→färg vid skärmens mitt) | **reveal** | Tre fristående uppslag i spalt, vart och ett sitt eget instick, ingen anledning att hålla kvar bilden |
| C (tjänster) | 5 Lista | `flow` + `in`, stagger 70-90ms per rad | **flow** | Tre jämlika rader, ren radvis intoning, ingen sekvens att hålla |
| D (pris) | 6 Räkning | `reveal`: hårlinjen dras in, priset glider in från höger per rad | **reveal** | Skiljer sig avsiktligt från akt C:s enkla intoning — priset "landar" som egen händelse, inte bara dyker upp |
| E (avslut) | 7 Vila | `flow` (rubrik/skriv-rad/kolofon, en gång) + `drift`-egenskap (grunden går papper→bläck) | **flow** (+ drift) | Sista akten håller kvar sitt innehåll (cue-kontraktet), driften är sidans enda tonala inversion |

**Kontroll mot reglerna:** 4 distinkta familjer (pin, kinetic, reveal, flow) ≥ 4 ✓. Sekvens
A→B→C→D→E = pin→reveal→flow→reveal→flow, ingen upprepning i rad ✓. `scrub`-enheter: 0 ≤ 2 ✓.

**Cue-kontraktet per akt:**
- **Akt A (hero):** ground-or-greet — ordmärket, klockan och platen är redan fullt synliga
  vid `p=0` (en befolkad grund, inte en tom scen), så ingen explicit greet-cue-form behövs;
  om en cue ändå sätts på rubrik-lagret blir den `"0 0.78 0"` (greet-formen) för säkerhets
  skull.
- **Akt B–D (mellersta):** tvåvärdesramper per element (`"0.1 0.6"`-stil, in→håll→ut), aldrig
  ett en-värde som skulle hålla lyst genom hela un-pin-glidningen (regeln "endast sista akten
  får hålla").
- **Akt E (avslut, sista):** en-värdes hold-cue (`"0.06"`) på rubriken, skriv-raden och
  kolofonen — de får inte tona bort innan sidan tar slut.

---

## 8. Fingerprint mot r6 B-K2

Sex dimensioner, utskrivna, jämfört mot den faktiska koden jag läste (inte mot `concepts.md`s
egen sammanfattning, som kontrollerats och stämmer):

| # | Dimension | r6 B-K2 (läst i koden) | K2 v2 (denna BRIEF) | Skiljer? |
|---|---|---|---|---|
| 1 | Grammatik | typographic poster | typographic poster | **Nej** |
| 2 | Nav | tunn rad, logga vänster, klocka mitten, mejl höger | samma mönster | **Nej** |
| 3 | Hero-device | rektangulär bildpanel `left:30%`, ligger BREDVID bokstäverna, inte maskad ur dem | bilden maskad genom bokstävernas faktiska öppningar (A-K2:s `inkScan()`-teknik), plus en plate bredvid ordmärket (F-004) | **Ja** |
| 4 | Akt-sekvens | pin (kontinuerlig font-size/line-height-lerp) → tre i huvudsak identiska IO-reveal-akter (fade+translateY) för bevis/tjänster/pris → clip-path-nedsläpp vid avslut | pin+kinetic (diskret radhöjdsöppning till ny rubrik) → reveal (wipe/gråskala) → flow (stagger) → reveal (hårlinje+glid) → flow+drift | **Ja** |
| 5 | Avslut | `.close` avtäcks genom en `clip-path: inset()`-gardin som glider bort och avslöjar en redan-satt sektion i displaygrad | grunden själv driftar från papper till bläck (färgövergång, ingen gardin), sidan slutar på sin MINSTA typ (kolofonen), inte på displayraden | **Ja** |
| 6 | Signaturrörelse | "panelglid": en rektangulär bildpanel glider vertikalt bredvid ordmärket, blocket andas via kontinuerlig font-size-lerp | "papper bakom mask + blocket andas": bilden glider GENOM bokstävernas bläckform, blocket öppnar sig i ett diskret steg till nästa rubrik | **Ja** |

**4 av 6 skiljer** (dimension 3, 4, 5, 6) — godkänt mot gaten (≥4/6 krävs).

---

## 9. Reduced motion-planen

Per F-001 (reservläget får aldrig bara vara ett stillastående slutläge): de formade lägena
visas som egna sektioner, i ordning, aldrig en tumnagel av slutläget och aldrig ett hopp till
sista rutan.

1. **Hero, i vila:** ordmärket ALU/NIX i sin faktiska affischstorlek (radhöjd 0,75, INTE
   0,73× nedskalad som under scroll), fönstren visar Calyx statiskt (ingen cykling till Hōrai/
   Hyperborea — de visas fullt ut senare i bevisakten), platen bredvid, klockan går. Detta är
   redan sidans korrekta "grund"-tillstånd, ingen spoiler.
2. **Formad sektion 1 — blocket öppet:** en egen kort sektion direkt under, radhöjd 1,0, med
   "VI BYGGER" / "ERT VARUMÄRKE." som en riktig rubrik (inte en scroll-lerpad mellanposition).
   Detta är den formade änden av signaturrörelsen, visad som innehåll, inte som förhandsvisning.
3. **Bevis:** samtliga tre uppslag i färg direkt (ingen gråskala-till-färg-övergång), i ordning
   Calyx → Hōrai → Hyperborea, staplade.
4. **Tjänster:** liggaren, alla rader synliga direkt.
5. **Pris:** liggaren, alla rader och priser synliga direkt.
6. **Avslut:** botten redan i bläck-tonen (ingen drift att spela upp), rubrik, skriv-rad,
   kolofon i sin slutgiltiga ordning.

Ingen tumnagel av slutläget visas i steg 1; inget hopp till sista rutan — varje formatt läge
är sin egen sektion med egen plats i dokumentflödet.

---

## 10. `?preview=`-planen

Fyra tvingade lägen för skärmbild, ett per betydelsefullt formtillstånd i signaturakten:

| Parameter | Tvingar fram |
|---|---|
| `?preview=calyx` | Hero vid `p=0`: affischen i vila, Calyx i fönstren (samma som defaultläget — inkluderad för symmetri i skärmbildsserien) |
| `?preview=horai` | Hero vid den punkt i akt "Byte" där masken visar Hōrai (mitt i glidningen, block ännu ej öppnat) |
| `?preview=hyperborea` | Hero vid den punkt i akt "Byte" där masken visar Hyperborea (sista bytet, block ännu ej öppnat) |
| `?preview=open` | Hero vid `p=1`: blocket fullt öppnat, radhöjd 1,0, "VI BYGGER ERT VARUMÄRKE." som rubrik |

Implementeras enligt r6 B-K2:s redan fungerande mönster (`URLSearchParams`, `forced` som
override av `target` i scrollhanteraren) — samma mekanism, egen uppsättning namngivna lägen.

---

## 11. Typsnitt och palett

### Typsnitt — öppen konflikt löst, se § 12 för den kvarvarande frågan

**Två snitt, roller korsar aldrig** (TASTE.md §4.2, bindande regel; F-005 bekräftar att
tvåsnittsblandningen bedömdes som "bra" i den run som faktiskt hade två snitt — se § 12).

- **Displayrösten — Archivo** (variabel bredd/vikt), vikt 900, `font-stretch` ~112-125%.
  Används UTESLUTANDE för: ordmärket ALU/NIX, rubriken "VI BYGGER ERT VARUMÄRKE.", priserna
  i displaygrad, slutradens "Alla har rätt till bra design.". Aldrig kroppstext, aldrig
  kickers, aldrig nav.
- **Registerrösten — Familjen Grotesk**, vikt 400/500/600. Används för: navraden (logga-
  etikett, klocka, mejl), beskrivningsraden, bildtexter, liggarnas radtext, tjänsternas
  underrader, kickers (siffrorna 01-03, "Exempelsida: …"), kolofonen. Aldrig i affischgrad.

Ingen tredje familj (inget mono) — tjänsternas siffror och klockan sätts i registerrösten,
tabellsiffror (`font-variant-numeric: tabular-nums`), inte i en separat monofamilj, för att
hålla taket på två snitt.

**Varför just dessa två:** de är samma par som A-K2 redan byggde och som r6-domen (F-005)
pekar ut som den lyckade blandningen; ingen av dem är Spring/Summers Grotesk/Montreal eller
Indoeks Calibre — principen (en tung display-grotesk + en lugnare register-grotesk) är lånad,
inga faktiska typsnitt är det.

### Palett — fem tokens, ingen accent

| Token | Roll | Ungefärlig ton |
|---|---|---|
| `--paper` | botten, hela sidan utom avslutet | ljus salviagrön-grå (sagepapper) |
| `--ink` | text på papper, botten i avslutet | mörk, nästan svart, med en svag grön underton |
| `--white` | den enda lyfta ytan: platen, iframe-bakgrunder | varmvit, aldrig ren `#fff` |
| `--line-1` | stark hårlinje mot papper (rader, ramar) | mellanmörk grå-grön |
| `--line-2` | dämpad text/hårlinje, EGEN mätning mot bläck-botten i avslutet | mörkare på papper, ljusare version krävs mot `--ink` (husfysikens "muted tone per ground"-regel) |

Ingen sjätte färg, ingen kromatisk accent. Priserna, "Pris vid förfrågan", klockan — allt i
`--ink`/`--white`/`--paper`-systemet. Motiveringen är TASTE §2.2 ("ett papper, en accent")
tolkad strikt: K2 har inget CTA-ord eller CTA-knapp att låta en accent göra sin "en sak" på,
så en accent utan jobb hade blivit brus (F-003:s lärdom om två auktoriteter på en skärm).

---

## 12. Öppna frågor till orkestreraren

1. **Typsnitts-konflikten (F-005 vs. faktisk kod i B-K2).** Läsordern pekade ut
   `runs/B/K2/index.html` som facit för "typsnittsvalen och deras motivering", men den filen
   använder i verkligheten ETT typsnitt (Archivo, variabelt) för hela sidan — motsatsen till
   F-005:s beröm av "två snitt med tydliga roller". Jag har löst detta genom att följa den
   bindande regeln (TASTE §4.2) och F-005:s regeltext snarare än B-K2:s faktiska kod, och
   återanvänt A-K2:s tvåsnittspar (Archivo display + Familjen Grotesk register) som redan
   fanns i samma omgång. Stämmer det, eller var avsikten att jag skulle bygga vidare på
   B-K2:s enda-typsnitt-idé (Indoek/Spring-Summer-principen "ett snitt, hierarki bara genom
   skala") och att F-005 syftade på en annan körning än jag tror?
2. **Om den ensamma platen (`plate-desk.webp`) ska återanvändas.** concepts.md placerar den
   bara i hero, bredvid ordmärket (F-004). r6:s båda K2-byggen hade istället en desk-bild vid
   tjänster/pris-akten (annan fil, annan fotograf). Jag har antagit att platen INTE ska
   upprepas i tjänste-/prisakten i v2 (håller "ett displayelement per skärm" strikt) — bekräfta
   att det stämmer, annars behöver akt C/D ett andra foto-alternativ.
3. **Klockans stad.** Alla tre lästa K2-byggen hårdkodar "Stockholm" som ortnamn bredvid
   klockan. Ingen av Alunix-faktan nämner var byrån sitter fysiskt. Antar att "Stockholm"
   fortsatt är rätt (Sverige-baserad byrå, Calyx är uttryckligen "florist i Stockholm") — flagga
   om det är fel antagande.

---

**Avslutning:** 39 filer/bilder lästa (SKILL.md + 10 skill-referensfiler, `concepts.md`,
2 katalogposters `entry.md`, 2 `fold.webp`, 18 `slices/*.webp` [6 Spring/Summer + 12 Indoek],
2 `extract/*-DESIGN.md`, `credits.json`, 2 tidigare K2-byggen i fulltext, samt
assets-mappens innehåll listat). BRIEF.md ligger på
`tests/alunix-ab-r7/runs/B/K2/BRIEF.md`. Tre öppna frågor ovan, den första (typsnitt) viktigast
eftersom den avgör runda 2:s CSS-uppsättning direkt.
