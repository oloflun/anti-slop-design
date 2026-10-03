# V3g R10 · beslutslogg

Beställning: Anton 2026-10-03, "Kör nästa runda enligt § 4, jag godkänner planen."
Plan: `AUDIT-ALUNIX-R9.md` § 4. Brief för katalogvalet: `BRIEF-R10.md`.
Backup före första ändringen: `index.before-r10.html`.

## 1. Kedjan (läst innan första UI-skrivningen)

- Skill(design), `chain-discipline.md`, `fault-taxonomy.md`, `TASTE.md`, `FEEDBACK.md`,
  `ANTON-VISION-OCH-FEEDBACK.md`, `reference-lock.md`, `house-physics.md` (Structural + Motion).
- Scroll: `README.md`, `grammars.md`, `devices.md`, `feel-and-fingerprint.md`,
  `showcase-floor.md`, `journeys/era-residence.md` (§ 2b läst), fingerprint-registret.
- Katalogvalet: `select.py --brief BRIEF-R10.md --k 4` → highwaymedia, clapat, a-lign,
  digidop (alla modern clean / chaptered editorial / portfolio). Lästa: entry.md + fold.webp,
  highwaymedias design-language.
- Rörelseark (motion_floor 2, lästa som bild): `forgeautomotive-co`, `filmbot`,
  `era-residence`. Kontrollerat i entry.md: alla tre `motion_floor: 2`.
- Skills: lenis, gsap-core, gsap-scrolltrigger, gsap-timeline, gsap-plugins.
- Copy: copywriting → humanizer-svenska på varje ny sträng (§ 5).

Tier 0 i praktiken: riktningen är låst av den byggda sidan (Rutverket: vitt papper i svarta
celler, en mint, Geist + Geist Mono). Inget nytt token, ingen ny färg.

## 2. Vad som lånas, och varifrån

| Övergång / grepp | Lånat från | Vad som tas | Vad som lämnas |
|---|---|---|---|
| process → showcase: fotot växer ur sin ram till Calyx-ramen | **Forge** (stickbilden växer från ett kort bakom rubriken till helbild, "the zoom is the transition into the next chapter") och **Filmbot** (helbild som bär bytet) | Kort → full ram, scrubbat åt båda hållen. Fotot lämnar en tom ram efter sig. | Forges ENTER-grind och grå text före fyllning. |
| ...och fotot löses upp i sajten | sidans egen dither → färg-rutnät + **Davide Cattaneo**-raden i golvets § 4 (pixel-block dissolve) | Rutnätet som redan är sidans material (R3) blir dörren in i den levande ramen | Ingen ny effekt-familj; ingen toning av iframen |
| showcase → pris: mintspåret fyller sin yta och blir prisets mark | **Era § 2b**, "the bowl hands its colour on": formen växer tills den *är* nästa sektions mark | Spåret (4 px) fyller radytan uppifrån, rinner ned i högerkolumnen och breder ut sig över prisrubrikens cell; samma färgfält fortsätter som bentons mintruta | Eras halvmåne och text på kurvan |
| pris → kontakt: mintrutan krymper till kortets skugga | **Era § 2b**, "the reverse grow" (fullbleed krymper tillbaka till ett inramat kort) | Samma grepp baklänges: fältet drar ihop sig till kortets skugga och kortet lämnas ut ur pris | Eras fönsterram |
| Typ och media i samma ram | **a-lign** ("photos tucked between words"), golvets regel 5 (Khanh: "a title that parts so the gallery grows in the gap") | En bild i luckan efter "samtal" i processrubriken, öppnas i läsfart, står sedan still | a-ligns streckade ramar, grå text före aktivering |
| Sektionsnavigering | highwaymedia (nav i headern), Era (fast header) | Fyra textankare i topplinjens vita mittcell | Pill-knappar, hamburgermeny |

Signaturobjektet (regel 3) är fortfarande visitkortet; R10 lägger till att mintfältet följer
med från showcase via pris till kortets skugga, så kortet "lämnas ut" ur fältet.

Tre olika orsaker, aldrig samma två gånger i rad: foto som växer och löses upp (T1),
färgfält som flödar och blir mark (T2), färgfält som krymper till ett föremål (T3).

## 3. Formbeslut som planen kräver

- **Väljaren flyttar in i pinnen.** § 4 punkt 1 kräver att processfotot växer till Calyx-ramen,
  och punkt 4 att casebytet nås inne i pinnen. Mellan processen och showcasen låg ordet
  "Exempelcase" och väljaren (två stora skärmbilder). De tas bort ur flödet; väljarens två
  knappar (skärmbild + namn, mintmarkering på vald) står nu överst i showcasens sidokolumn,
  i alla lägen. Casebytet behåller den skyddade övertoningen och gör inget scrollhopp alls.
  Ordet "Exempelcase" ersätts av topplinjens ankare "Exempel" och showcasens egen rubrik.
- **Processrubriken utan kicker** (F-016) och utan raden under: "Webbdesign, design och system.
  Allt på ett ställe." flyttar till heron (punkt 6) och står bara där.
- **Processkolumnen under 1200 px:** fotot flyttas efter stegen (rubrik, steg, foto) så att det
  ligger sist när showcasen kommer, även på 768 och 390.
- **Prisrubrikens cell får mint som vilomark**, eftersom den är fältet som showcasen lämnar
  över. Bentons mintruta fortsätter samma fält.
- **Rytmband:** process → showcase och showcase → pris tas bort (ersatta av T1, T2).
  Tes → process behålls (ingen ny övergång där).

## 4. Skyddat, och hur det skyddas

- Tesens överlämning, heron och kortet: koden rörs inte, utom att heroraden (punkt 6) får egna
  linjemasker och samma maskdrift som h1 (en ägare per egenskap: laddningen äger raderna,
  scrollen äger maskerna).
- Showcasen: pinnen skapas fortfarande en gång, aldrig dödad; `scrub:true`; ingen iframe
  transformeras eller tonas av R10. T1 ritar en separat yta *ovanpå* ramen och tar bort den
  ruta för ruta. Övertoningen vid casebyte är oförändrad.
- Kontaktkortet: självvändningen vid 0,7 är orörd; T3 slutar före 0,7 och lämnar kortets
  vanliga svarta skugga i vila.
- Lenis: `lerp .075`, `wheelMultiplier .6`, enda utjämningslagret. Alla nya triggers
  `scrub`/progress-drivna utan numerisk scrub.

## 5. Copy (copywriting → humanizer-svenska)

| Sträng | Var | Not |
|---|---|---|
| Webbdesign, design och system. Allt på ett ställe. | heron, under h1 | låst ordagrant (PRODUCT.md) |
| Vi lämnar pris efter första samtalet. | pris, ingressens skala | godkänd i planen |
| Mejla oss om ett möte | hero- och kontaktkortet | säger vad länken gör (mailto) |
| Så berättar vi vad vi kan göra för er och föreslår en tid för ett första samtal. | kontakt, ingressens skala | ersätter "Så berättar vi vad vi kan göra för er."; ekot av rubrikens "Berätta" behålls, inget tidslöfte |
| Process · Exempel · Paket · Kontakt | topplinjen | ankare |
| Calyx · Hōrai (grupp "Välj exempel", bara för skärmläsare) | showcasen | knappar |

Humanizer-utfall: "Vi svarar med ett förslag på tid…" som egen mening gav två meningar med
samma längd och två "vi" i rad; sammanslaget till en mening med ett subjekt.

## 6. Golvet regel för regel (fylls i efter mätningen)

Se § 6 längre ned när rörelsearket är läst.
