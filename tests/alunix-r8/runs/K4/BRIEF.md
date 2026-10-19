# BRIEF — Alunix r8, cell K4 · Före/Efter · delaren tippar

Skelettet är skrivet av arkitekten. Fält märkta `[fylls i R1]` fyller **byggaren** i runda 1.
Fält utan den märkningen är låsta och ändras bara med en ny rad i decision ledger som namnger
källan (F-post, TASTE-§, katalogpost, planparagraf).

Målbilden är `tests/alunix-r8/malbilder/K4.md` (planens § 7.5, ordagrant) och den är bindande.
Målbildsgrinden i sin helhet, inklusive alla 36 fingerprint-rader och de mätta talen:
`tests/alunix-r8/concepts-K4.md`.

---

## catalogue-select

```
catalogue-select: paper, gocanopy, harkcap, mode, customer-io
```

Skriven av `python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K4/BRIEF-draft.md --k 4 --wildcard --explain`
till `.impeccable/design-session.jsonl`. Wildcard = `customer-io`. Full utdata, poäng och
skälen till att `future-fur` (11 poäng) och `dovetail` (8 poäng) föll bort står i
`concepts-K4.md` § catalogue-select. **Byggaren kör om samma kommando i sin egen session** och
rapporterar avvikelse; vid avvikelse gäller raden ovan.

### Byggarens egen körning, R1, med avvikelse

**Avvikelse, och den är rapporterad innan den är förklarad.** Lead-instruktionen sade
`--brief tests/alunix-r8/runs/K4/BRIEF.md`. Arkitekten körde mot `BRIEF-draft.md`. Jag körde
först det instruktionen sade, ordagrant:

```
python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K4/BRIEF.md --k 4 --wildcard --explain
```

Hela utdatan, ordagrant:

```
Brief: tests\alunix-r8\runs\K4\BRIEF.md  ->  4 poster

    6  aarke                    warm photographic      gallery/catalog
       +6 fritext (bar, before, cta, full-bleed)
    6  aevi-wellness            modern clean           chaptered editorial
       +6 fritext (accent, full-bleed, hairline, one)
    6  alet                     editorial print        gallery/catalog
       +6 fritext (accent, chroma, colour, never)
    6  altitude-beverages       editorial print        chaptered editorial
       +6 fritext (colour, display, full-bleed, gradient)

Mediastrategi ur posternas egna falt (Photo search) - locken ska inte gissa:
  - aarke: Unsplash first, Pexels second. - "kitchen counter natural light product styled" - "coffee maker steel kitchen morning light" - "marble count
  - aevi-wellness: Unsplash first, Pexels second. - "skincare bottles overlapping flat lay natural light" - "dropper bottle apothecary product close up" - "min
  - alet: Unsplash first, Pexels second. - "editorial product photography warm natural light" - "interior photography natural light desaturated" - "på
  - altitude-beverages: Unsplash first, Pexels second. - "beverage can product shot gradient background studio" - "condensation can drink close up" - "rosemary garn

catalogue-select skriven: aarke, aevi-wellness, alet, altitude-beverages  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Orsaken är mekanisk och kontrollerad, inte gissad.** `BRIEF.md` är ett skelett vars
strukturfält (`Register:`, `Grammar:`, `Category:`, `Mode:`, `Authority:`) inte finns och vars
fritext till största delen är arkitektens instruktioner till mig, inte målbildens språk.
Skriptet får därför noll poäng på register, grammatik, kategori, mode och auktoritet, och
faller tillbaka på ren fritextmatchning. Kvar blir fyra poster som alla står på 6 poäng, och
utfallet är då den alfabetiska ordningen: `aarke`, `aevi-wellness`, `alet`,
`altitude-beverages`. `paper` finns inte ens i listan. Två oberoende belägg för att det är
skelettet och inte cellen som orsakar det: sifferbilden är identisk för alla tre celler i
rundan (V3c, K3 och K4 fick samma fyra slugar mot sina egna skelett i samma minut), och
samma kommando mot `BRIEF-draft.md` reproducerar arkitektens rad exakt.

**Kontrollkörningen mot draftfilen, i min egen session, hela utdatan ordagrant:**

```
python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K4/BRIEF-draft.md --k 4 --wildcard --explain
```

```
Brief: tests\alunix-r8\runs\K4\BRIEF-draft.md  ->  5 poster

   14  paper                    modern clean           split stage
       +3 register | +3 grammatik | +2 category | +1 mode | +2 auktoritet | +3 fritext (accent, chrome, product)
   12  gocanopy                 modern clean           chaptered editorial
       +3 register | +2 category | +1 mode | +2 auktoritet | +4 fritext (bar, nav, pill, product)
   12  harkcap                  modern clean           split stage
       +3 register | +3 grammatik | +1 mode | +5 fritext (flat, gradient, kickers, nav)
   12  mode                     modern clean           split stage
       +3 register | +3 grammatik | +2 category | +1 mode | +3 fritext (accent, mode, tracking)
   11  customer-io              modern clean           live surface
       +3 register | +2 category | +1 mode | +2 auktoritet | +3 fritext (pill, product, under) | wildcard: utanfor kategorin

Mediastrategi ur posternas egna falt (Photo search) - locken ska inte gissa:
  - paper: Unsplash first, Pexels second. - "software interface mockup minimal desk" - "laptop screen design tool workspace" - "minimal desk setup natu
  - gocanopy: Unsplash first, Pexels second. - "city skyline dusk aerial teal" - "financial district buildings evening light" - "downtown skyscrapers blue
  - harkcap: Unsplash first, Pexels second (for the team/office secondary imagery only — the hero itself is a bespoke 3D render, not stock photography). 
  - mode: Unsplash first, Pexels second. - "team collaborating desk candid natural light" - "coworkers reviewing screen office documentary" - "data an
  - customer-io: Unsplash first, Pexels second. - "desk plant natural light soft focus interior" - "home office daylight blurred background" - "minimal works

catalogue-select skriven: paper, gocanopy, harkcap, mode, customer-io  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Vad som gäller.** Arkitektens rad, ordagrant, enligt lead-instruktionen. Jag byter inga
referenser på egen hand. Min sessionsledger bär nu båda raderna, och den sista är
`paper, gocanopy, harkcap, mode, customer-io`, alltså den referensgolvet läser inför R2.
Skriptet är deterministiskt: samma fil in ger samma rad ut, och skillnaden ligger helt i
vilken fil som pekas ut.

**Vad som bör rättas, men inte av mig:** instruktionens filsökväg, inte urvalet. Ett skelett
kan per konstruktion inte poängsättas, eftersom dess fritext beskriver arbetsordningen och
inte designen. Raden ligger som en öppen fråga sist i det här dokumentet.

## Design Read (en rad)

**Två utskrifter kant i kant på ett varmt ark**, i register `modern clean` och grammatik
`split stage`: två färdiga webbplatser delar en enda rektangel, ett blått streck markerar var
den ena slutar och den andra börjar, och scrollen flyttar strecket tills den ena är kvar.

Lane-frasen, en gång och inte igen: *varmt tryckark, två levande gränssnitt kant i kant, ett
enda blått streck i sömmen.* Kategori `portfolio` / `product-focused`, auktoritet
**produkten** (TASTE § 1 rad 4: objektet ofritt i mitten, typen nästan tyst, ytan flat).

## Dial-deklaration

**variance 8 · motion 6 · density 3.** Arkitektens riktvärden, bekräftade efter egen prövning,
med en precisering på density.

- **variance 8.** Grammatiken `split stage` har tre rader i ett register på 36, och ingen av
  de tre gör det K4 gör: r1 K2 delar skärmen med en fast textspalt, r2 R5 ramar in den med en
  konsol, r3 build ställer två egna heron sida vid sida. K4 ställer i stället två **främmande,
  färdiga** sidor mot varandra i samma ruta och låter besökaren flytta gränsen. Det är inte 10,
  eftersom grammatiken i sig är låst av målbilden och delad med tre rader; det är inte 6,
  eftersom hero-device, aktform, avslut och signatur alla är obesatta i registret.
- **motion 6.** En enda pinnad akt bär hela rörelsen; efter den är sidan `reveal`, `flow`,
  `kinetic` och `count`, alltså kedjans normalfall. Det som lyfter siffran från 4 till 6 är att
  signaturen inte bara är scrolldriven utan **gripbar**, med avbrytbarhet, fjäder och
  velocity-handoff, och att den samtidigt driver fyra egenskaper från ett tal. Det som hindrar
  den från 8 är att ingenting utanför a1 rör sig på ett sätt besökaren kan påverka.
- **density 3.** Nio skärmar, ett displayelement per skärm, och K4:s eget lager innehåller
  exakt fem elementtyper: rubrik, monoetikett, liggarrad, hårlinje, delare. **Precisering som
  arkitektens siffra inte fångar:** vid ps = 0 är den *upplevda* tätheten hög, eftersom vyn
  innehåller två kompletta webbplatser. Den tätheten är lånad, inte författad; den tillhör
  innehållet och inte K4:s lager, och den är hela poängen med folden. Dialen mäter det jag
  ritar, och det jag ritar är fem element. Konsekvensen för R2 är enkel och kontrollerbar:
  varje gång ett element vill tillkomma i K4:s lager ska det kunna namnges som en av de fem,
  annars ska det bort (samma kontroll som troplistans F-006-rad).

## Reference lock (7 fält)

```text
Primary reference/direction: paper (design-catalogue/entries/paper) — varm kanvas, tvatons
  rubrik med identiska metriker, en enda kromatisk accent inhagnad utanfor UI-handling.
  14 poang, hogsta i katalogen mot denna brief.
Preserve: tvatonsrubriken som foldens enda typografiska handelse (identisk grad, identisk
  vikt, identisk tracking, bara fyllnadsfargen skiljer, aldrig två grader och aldrig två
  snitt); en enda kromatisk accent som aldrig är text, aldrig en lank och aldrig en knapp;
  plan yta utan elevation, hairline som enda strukturmedel; radie 0 overallt; kanvas som är
  varm men inte gradde.
Borrow only: (1) gocanopy — inramningen av rubriken med två små monoetiketter, roterad 90
  grader sa att `Fore` och `Efter` står till vänster och höger om raden i stallet for over och
  under den. (2) harkcap — hairlinelistan som barande sektionsform, anvand for
  skillnadsliggaren, utan ett enda kort. (3) customer-io, lanad som AVVISNING: dess
  signaturdrag är att lana trovardighet at en skarmbild genom att iscensatta den i ett
  fotograferat rum; K4 lanar ingenting, produkten kors live i ramen.
Role rules: `#1E5E9C` finns på exakt ett objekt, delaren, och det objektet existerar exakt en
  gang på sidan; accenten är aldrig text, aldrig en lank, aldrig en ram, aldrig ett tal,
  aldrig en yta. Switzer är enbart rost (rubriker, brodtext, priser) och satter aldrig en
  etikett eller ett radnummer. Reddit Mono är enbart register (två kickers, liggarens
  radetiketter, radnummer 01-03, tre bildtexter) och satter aldrig en rubrik, en brodtext
  eller ett pris. Max fyra monoetiketter på hela sidan; K4 anvander två i folden. Rollerna
  korsar aldrig. Hairline `--hair` är sidans enda strukturlinje utover delaren.
Media strategy: product surface (Calyx live i `<iframe>` från repo-roten; Horai och
  Hyperborea som egna skarmbilder) + product surface, anti-reference (before-ai-slop live i
  `<iframe>`, arligt etiketterad `En typisk mallsida`). Enum, ett varde per plats. INTE
  photo:unsplash, INTE photo:pexels, INTE generated, INTE drawn system, INTE placeholder.
  Noll genererat material i cellen, se assets/credits.json.
Reject: handtagsknopp, ikon, dubbelpil eller "dra"-text på delaren (gate 88); ritad
  webblasar- eller telefonram, flikrad, URL-falt, trafikljusprickar (gate 47); div-byggd
  produkt-UI, graf, sparkline, stapeldiagram (gate 79); glaskort, statuschip, live-prick,
  procentavlasning av delarens lage (F-006); centrerad copy och symmetriskt avslut
  (grammars.md, split stage); full-bleed sektion fore upplosningen (samma rad); `pan`,
  `drift`, `spotlight`, `magnet`, mer an en `scrub` (samma rad); mork inversion i avslutet;
  logotypvagg, omdomen, betyg, kundantal, år i branschen, team, kontor; en andra accent;
  skugga; gradient i K4:s eget lager; tidsstampel eller klocka; `transition: all`.
Token commitments: paper `oklch(0.957 0.013 85)`; paper-2 `oklch(0.928 0.018 78)`; ink
  `oklch(0.26 0.021 62)`; ink-2 `oklch(0.62 0.014 70)`; hair `oklch(0.80 0.010 78)`; blue
  `oklch(0.47 0.13 252)` = `#1E5E9C`, ett bruk, ett objekt, en forekomst; radie 0 overallt;
  noll box-shadow; pricing: styckelista med ledarpunkter, aldrig kort; services: tre rader ur
  en mask med 01-03 i marginalen, aldrig kort; display Switzer ~112px avslutsrubrik / ~44px
  foldrubrik; body Switzer 15px; register Reddit Mono 11px, tracking 0.18em.
```

## Decision ledger

En rad per materiellt val. Ett val utan rad skeppas inte.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Palett** | Varmt papper `oklch(0.957 0.013 85)`, varmt bläck `oklch(0.26 0.021 62)`, dämpad ton `oklch(0.62 0.014 70)`, hårlinje `oklch(0.80 0.010 78)`, accent `#1E5E9C` = `oklch(0.47 0.13 252)` | Lead-lås 2026-09-09 (K4:s papper är varmt, K3 har låst kallt `oklch(0.95 0.012 230)`) + `paper`-postens kanvasprincip | TASTE § 4.4, ett papper och en accent som gör en sak | De två nya cellerna får inte dela temperatur; hue 85 mot hue 230 är 145° isär vid samma låga chroma, och ingen av dem är kräm |
| **Accentens plats och frekvens** | `#1E5E9C` finns på **ett objekt**, delaren, som existerar exakt **en gång** på sidan; aldrig text, aldrig länk, aldrig ram, aldrig tal | `mode` § What to borrow (inhägnad till en komponenttyp), skärpt ett steg; `paper` § Role rules (blått aldrig på knapp, länk eller stor text) | "Fence the single accent colour to one component type" | En komponentregel kan drifta när en ny komponent uppstår; ett objekt som bara finns en gång kan inte drifta. Regeln är granskningsbar med en `grep` |
| **Typ** | **Switzer** (röst, Fontshare, variabel `wght` 100–900) + **Reddit Mono** (register, Google Fonts, variabel `wght` 200–900); rollerna korsar aldrig | `brand.md` fyra steg, utförda i `concepts-K4.md` § (6) | TASTE § 4.2, två snitt och rollerna korsar aldrig; mono får bara vara register | Tvåtonsdevicen kräver ett snitt utan egen händelse på raden, och degraderingen 500 → 200 kräver en lång viktaxel. Varken Switzer eller Reddit Mono finns i r1–r7, i `sites/`, i reflexlistan eller i K3:s val eller reserver. Reservval om Fontshare faller: **Onest** (Google Fonts, samma axel) |
| **Nav** | **Ingen bar, ingen meny, inget ordmärke i toppen.** Delaren är hela chromen: en lodrät hårlinje över full viewporthöjd, i bläck med `#1E5E9C` som sitt enda kromatiska värde. `kontakt@alunix.se` som 15 px text i "efter"-halvans övre högra hörn | Målbilden (planens § 7.5) + `grammars.md` split stage, kolumnen *Shape* | "No bar; divider IS the chrome" | Grammatiken säger det ordagrant, och det är den dimension som skiljer K4 från r2 R5 och r3 build, de två andra split stage-raderna i registret |
| **Hero-device** | Två levande sajter i **samma** 1440×900-ruta, staplade som två lager: `sites/before-ai-slop.html` underst, Calyx överst, åtskilda av `clip-path: inset(0 0 0 var(--split))` på det övre lagret. **Ingen ram skalas, transformeras eller flyttas någonsin — bara clip-gränsen rör sig.** Över båda en enradig tvåtonsrubrik som korsar sömmen | Målbilden + `paper` § Signature move + PRODUCT.md § Operating Context | AB06, motorn redigeras aldrig; F-010, fönstret i fasaden och inte en ruta utanpå den | En clip-gräns är det enda sättet att flytta gränsen mellan två sidor utan att röra någon av dem. En `transform: scale()` på en ram skulle bryta PRODUCT.md:s krav att en visad ram ska gå att använda |
| **Aktform** | 6 akter, 9 skärmar: `pin` span 2,4 dwell 0,22 → `reveal` **per sida** → `flow`+`in` → `kinetic` lines → `count` → `reveal` | Målbilden, med tre ändringar (nedan) | `grammars.md` split stage *Leans*: "`pin` with divider, `reveal` per side, real `count`" — alla tre används | Grammatikens tre egna lutningar bär cellens tre viktigaste akter |
| **Aktform, ändring 1** | Målbildens vågräta idé för Hōrai/Hyperborea blev `flow` + `in` med stagger 90 ms, inte `pan` | `grammars.md`, split stage, kolumnen *Bans* | `pan` är uttryckligen förbjuden i den här grammatiken | Målbilden namnger inte familjen, så ingen låst rad bryts; `flow` håller "i tur och ordning" |
| **Aktform, ändring 2** | Målbildens andra `flow` (paketen) blev `count` | `devices.md` § device kit + § 7 | "never the same one twice running"; en count kräver verifierade tal | `26 900` och `38 900` är sanna; `Pris vid förfrågan` räknar inte, den skrivs |
| **Aktform, ändring 3** | `VI BYGGER ERT VARUMÄRKE.` placerades som a2:s löphuvud, inte som egen akt | PRODUCT.md § Brand Commitments (låst copy) + `feel-and-fingerprint.md` § The peak | Ordagrann copy bevaras; en sida med tre toppar har ingen | Målbildens aktlista nämner aldrig tesraden, men strängen är låst copy och måste finnas på sidan |
| **Avslut** | Kollapsen till en kolumn på **samma varma papper**: "efter"-ytan fyller bredden, `Alla har rätt till bra design.` i displayskala vänsterställd, `kontakt@alunix.se` som mailto under. Ingen inversion, inget formulär, ingen sticky CTA, ingen footerrad | Målbilden + r7 § Alunix, fakta + `grammars.md` split stage | "close is the collapse to one column"; "Never: symmetric close"; "inget formulär som skickar någonstans" | Rut-testet: kategorins default är ett mörkt CTA-band plus ett formulär. Avslutet ligger avsiktligt osymmetriskt |
| **Memorable detail** | **Delaren tippar.** Scrollen äger delarens målvärde via `--sc-ps`; pekaren får sätta ett eget värde 1:1 från en 44 px bred osynlig träffyta med `cursor: col-resize`; släppet lämnas tillbaka till målvärdet genom en **kritiskt dämpad fjäder, damping 1,0**, seedad med pekarens hastighet vid `pointerup`; rörelsen är avbrytbar med behållen position och hastighet; det som målas är alltid fjäderns utvärde, aldrig pekarens råa x. Samtidigt degraderas rubrikens före-halva: `wght` 500 → 200 och `letter-spacing` 0 → 0,06 em | `paper` (tvåtonsrubriken, omtolkad till ett gränssnitt som förstör sin egen device) + `apple-design` § interruptibility / presentationsvärde / velocity | `reference-lock.md`: Memorable detail-raden är obligatorisk | Målbildens tell-someone är att den dåliga sidan trycks ut ur bild av den bra, och besökaren ska kunna skjuta på själv |
| **Ingen affordans på delaren** | Ingen knopp, ingen ikon, ingen dubbelpil, ingen "dra"-text, ingen tooltip. `cursor: col-resize` är hela affordansen | Gate 88 + lead-instruktionen | "Any scroll cue" — bottenkanten behöver ingen etikett, och inte heller mitten | En ritad affordans skulle förvandla sidans chrome till en widget, vilket är precis jämförelseslider-klichén |
| **Mallsidans degradering** | `filter: saturate()` på **wrappern** runt `sites/before-ai-slop.html`, driven av `--split`. Ingen `transform`, ingen `opacity`, ingen `scale` på någon ram. Regeln "en visad ram får aldrig transformeras eller tonas" tolkas som gällande de **tre Alunix-exempelsajterna**, inte antagonisten | PRODUCT.md § Operating Context, snävad | Beviset ska gå att använda | Antagonisten är inte bevis, den är argumentets andra halva. De tre exempelsajterna rörs aldrig. **Se Q12** — antagandet gäller tills Anton svarar |
| **Hōrai och Hyperborea som skärmbilder** | Två vendorade `.webp` i stället för två ytterligare live-ramar; Calyx förblir live | Målbilden ("full-bleed **objekt**") + `performance.md` § 1 | Överföringsbudget ≤ 2,5 MB | Fyra samtidiga iframes är inte försvarbart inom budgeten, och PRODUCT.md princip 1 är uppfylld så länge minst ett bevis är levande och användbart på sidan |
| **Ingen generering** | Noll genererat material i K4. Ingen asset-lock för en genererad bild skrivs, ingen bildprompt författas | Planens § 10.6 fallback steg 3 (Higgsfield `balance` = 0 krediter, free plan, en privat workspace, mätt av lead 2026-09-09) + cellens egen premiss | "byt deviceform, aldrig kvaliteten"; material som letar efter en användning är inte tillåtet | K4 behövde aldrig genererat material: cellens hela argument är att allt som visas är verkligt och mätbart. En genererad bild vore ett påhittat objekt i en sida vars tes är att den inte hittar på något |
| **Rörelsens datakälla** | Allt som förflyttar sig läser `--sc-ps` via `--split`; endast cue-opacitet läser `--sc-p`. `--split` publiceras som ett registrerat `<number>` | F-014 punkt 1 + `motion-smoothness.md` § The rule | "Bespoke motion reads `--sc-ps`, never raw `--sc-p`" | En clip-gräns som stegar är exakt fault 1 i `motion-smoothness.md`, och den syns bättre på en rak lodrät linje än på något annat |
| **Reduced motion** | Fältet finns inte. Ingen `prefers-reduced-motion`-gren, inget statiskt reservläge, ingen reduced-motion-plan | F-011 | Rörelsen spelas alltid | Pensionerat fält ur r7-briefen; skelettet innehåller det inte |
| **Prestanda** | Se § Prestandaplan nedan; varje post har ett målvärde. Två live-iframes är budgetens svåraste post och har en egen beslutsregel | F-013 + `performance.md` § 1 | Gate 93 | Calyx hämtar fyra externa Unsplash-bilder som K4 inte kan påverka, se § Prestandaplan |

### Byggarens rader, R1

Elva rader. Fyra av dem rättar ett tal eller en formulering i det låsta underlaget, och de
står först, eftersom en rad som rättar en premiss måste läsas före en rad som bygger på den.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Rättelse: mallsidan är inte fri från externa resurser** | Prestandaplanens rad "vänsterramen (`before-ai-slop.html`, 9 016 B, noll bilder, **noll externa resurser**)" är fel i sin sista tredjedel och skrivs om till "noll bilder, **tre externa värdar**". Filen laddar `https://cdn.tailwindcss.com` (play-CDN, en JIT-kompilator som körs i ramen) samt `fonts.googleapis.com` + `fonts.gstatic.com` för Inter i fyra vikter | Egen mätning 2026-09-10: `grep -oE 'https://[a-z0-9.-]+' sites/before-ai-slop.html \| sort -u` ger exakt `cdn.tailwindcss.com`, `fonts.googleapis.com`, `fonts.gstatic.com`. Byte-talet 9 016 stämmer (`stat -c %s`) | `performance.md` § 6, "Shipping a number from this file that you did not measure on the actual page" | Budgetposten är alltså inte 9 016 B utan 9 016 B plus en Tailwind-kompilator plus fyra typsnittsfiler, **och samma tre värdar laddas en andra gång av `calyx.html`**, som kör samma CDN och samma fontvärdar. Två ramar innebär två Tailwind-instanser. Det gör den här posten svårare än planen antar, inte lättare, och det ändrar vad `perf_probe` ska jämföras mot |
| **Rättelse: iframes får inte monteras vid load** | Ingen av de två ramarna monteras eagerly. Båda monteras av **en** `IntersectionObserver`, men vänsterramen får `rootMargin` så att den monteras vid första `requestIdleCallback` efter first paint, och högerramen en viewport i förväg. `loading="lazy"` på båda, `width`/`height` på båda | `performance.md` § 6 Never, rad 6: "An iframe mounted at load". Prestandaplanens ord "monteras **eagerly**, eftersom den är folden" står i direkt konflikt med den raden | Gate 93 | Skälet planen anger (den är folden) är just skälet regeln finns: en ram i folden är det som konkurrerar med LCP. Lösningen behåller planens avsikt utan att bryta regeln, eftersom LCP-elementet enligt planen ändå är rubriken, som är text och redan målad när ramarna monteras. Kontrollen är mekanisk: `perf_probe` ska namnge rubriken som LCP-element |
| **Rättelse: Calyx avslöjar sig själv i ramen** | Högerramen monteras alltid vid `scrollTop = 0` och får aldrig scrollas av K4. Skälet skrivs ut här så att ingen "fixar" det i R3 | Egen läsning av `sites/calyx.html` rad 294–298: ett `IntersectionObserver`-skript sätter klassen `reveal` (`opacity: 0; translateY(28px)`) på **varje** `section, h1, h2, h3, blockquote, figure, li` och avslöjar dem vid `threshold: 0.12` | AB06, motorn och exempelsajterna redigeras aldrig | Ramens egen viewport är 1440 × 900, så bara hero-sektionen är synlig och den avslöjas vid mount. Allt under den står kvar i sitt pre-reveal-läge. Det är rätt för K4, som bara ska visa folden, men det betyder att en ram som någonsin scrollas skulle visa en halvavslöjad sida. Ramen står stilla, punkt |
| **Rättelse: PRODUCT.md princip 2 mot liggarens tolv tal** | Skillnadsliggaren innehåller tolv tal, vilket vid en snabb läsning ser ut att bryta princip 2 ("vi har två priser och en numrering, fler tal finns inte, så fler tal skrivs inte"). Den gör det inte, och skillnaden skrivs ut på sidan: liggarens tal är **inte påståenden om Alunix** utan mätvärden om två filer som serveras från samma origin, med kommandot utskrivet | PRODUCT.md § Product Principles 2 + § Absences; TASTE § 4.9 | "Siffror får vara textur bara om de är sanna" | Princip 2 förbjuder tal *om verksamheten* (år, kunder, projekt, betyg). Ett tal som säger att en fil innehåller nio textfärger är kontrollerbart av läsaren med samma kommando. **Kontrollen i R3:** varje tal på sidan ska kunna spåras till antingen `measure.py`, källräkningen, `26 900`, `38 900` eller `01–03`. Finns ett tal utan spår ska det bort |
| **Etiketten `En typisk mallsida` är folden, inte en bildtext** | Etiketten sätts i 11 px Reddit Mono i vänsterlagrets **övre vänstra hörn**, i K4:s eget lager, och den är alltid ovanför clip-gränsen så länge `--split > 0`. Den tonar aldrig, den flyttar sig aldrig och den försvinner först när lagret är helt bortklippt | Lead-instruktionens invariant 9; `credits.json` `label_required`; egen läsning av `before-ai-slop.html` | Anti-referensen får köras som innehåll endast om den är ärligt märkt | Antagonisten innehåller **påhittade bevis**: `Trusted by 10,000+ teams worldwide`, `10k+ Happy customers`, `99.99%`, `10x`, och en logotypvägg med sex uppfunna märken. De ligger inuti dess ram och räknas i liggaren, men en besökare som missar etiketten kan läsa dem som Alunix påståenden, och det vore precis det PRODUCT.md § absences förbjuder. Etiketten är därför inte dekoration utan den enda spärren, och den får aldrig degraderas tillsammans med mättnaden |
| **Delarens mått och träffyta** | Delaren är 1 px bred i `--ink` med `#1E5E9C` som sitt enda kromatiska värde, full viewporthöjd. Träffytan är ett osynligt syskonelement, 44 px brett, centrerat på linjen, `cursor: col-resize`, `touch-action: none`. Ingen knopp, ingen ikon, ingen text, ingen tooltip | Gate 88; `apple-design` § 2 (`setPointerCapture`, grabOffset) och § 10 (hysteres ~10 px) | 44 px är tap-target-golvet; `cursor: col-resize` är hela affordansen | En ritad affordans förvandlar sidans chrome till en widget, alltså precis jämförelseslider-klichén. En osynlig träffyta ger samma gripbarhet utan att rita något. Hysteresen på 10 px hindrar att ett klick i ramen läses som ett drag |
| **Fjäderns exakta värden** | Kritiskt dämpad fjäder, damping ratio **1,0**, response **0,35 s**, seedad med pekarens hastighet vid `pointerup` (medelvärde över de sista tre `pointermove` inom 80 ms). Ingen översläng, ingen `bounce`. Implementerad som en egen integrator i samma rAF-loop som skriver `--split`, aldrig som en CSS-transition | `apple-design` § 4 (damping 1,0 som default; response är inte duration), § 3 (aldrig CSS-transitions för gestdrivet), § 5 (velocity handoff) | Alltid animera från presentationsvärdet | Målbilden låser damping 1,0. Response 0,35 s ligger mellan Apples 0,3 (drawer) och 0,4 (reposition), och delaren är en repositionering av en gräns, inte ett ark som får in. **Ingen momentum-projektion** (`apple-design` § 6): det finns inga snap-punkter att projicera mot, målet ägs av scrollen |
| **`--split` som registrerad egenskap, och riktningen** | `@property --split { syntax: "<number>"; inherits: true; initial-value: 0.5 }`, ett tal 0–1, **inte** en procent. `inherits: true` är obligatoriskt | F-014 punkt 1; F-013:s efterspel: `--sc-ps` registrerades först med `inherits: false`, vilket gav barn värdet 0 och frös akten med ren konsol | Bespoke rörelse läser `--sc-ps` | Exakt samma bugg är tillgänglig här och den är tyst. `--split` läses av fyra barn (efter-lagret, delaren, rubrikhalvan, mallsidewrappern), alltså är `inherits: true` inte en detalj utan hela mekanismen. `<number>` och inte `<percentage>` gör att samma tal kan driva `inset()`, `translateX`, `font-variation-settings` och `saturate()` genom fyra `calc()` utan enhetskonvertering |
| **Tangentbordsvägen är samma kodväg** | Delaren får `tabindex="0"`, `role="separator"`, `aria-orientation="vertical"`, `aria-valuemin/max/now`. Vänster- och högerpil flyttar målvärdet 2 %, `Home` och `End` sätter 1 och 0. Alla fyra går genom **samma fjäder** som pekaren, alltså ingen andra kodväg och ingen synlig extra affordans | Persona **Edge** i det här dokumentet; `a11y-audit` pass för tangentbord | Delaren är sidans enda interaktion, alltså är den också dess enda tangentbordsmål | Om delaren bara lyssnar på pointer-händelser saknar sidans signatur helt tangentbordsväg, och det är den enda interaktionen som finns. Att lägga den i samma fjäder betyder att avbrytbarheten och velocity-handoffen gäller också där, gratis |
| **Cue-kontraktet, skrivet ut** | a1 `0 1 0 0` (hälsa och håll, ground finns i form av två sajter), a2 `0.12 0.5`, a4 `0.1 0.9 0.15 0.4`, a5 `0.1 0.5`, a6 **`0.25`, ett enda värde** | `devices.md` § The cue contract, alla fem reglerna | "Only the last act may hold"; "A hero cue needs the greet form" | Foldens innehåll finns redan vid ps = 0, så en tvåvärdescue skulle ge en tom rubrikrad på första skärmen varje besökare ser. Och a6 måste hålla, annars tonar avslutsraden och mejladressen ut innan sidan tar slut. Mellanakternas cues har alla en platå, eftersom en triangelcue rör full opacitet i ett enda ögonblick |
| **Ny copy passerar copy-gaten i R3, inte här** | De sex radetiketterna och de tre tjänsteunderraderna är skrivna i § Copy-plan som förslag och är markerade som ogatade | Lead-instruktionen (copy-gaten körs i R3); `copy-gate.md` | Ordagrann Alunix-copy ändras aldrig, ny copy gatas | Att skriva dem nu och gata dem sedan är rätt ordning: liggaren kan inte layoutas utan att etiketternas längd är känd, och gaten kan inte köras på en tom lista |

### Byggarens rader, R2

Sju rader. Fyra är avvikelser mot målbilden, tre är val målbilden lämnar öppna. Alla mätta
tal och hela nedbrytningen står i `NOTES.md` § R2.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Viktaxeln skrivs som `font-weight`** | Rubrikhalvans degradering 500 → 200 skrivs `font-weight: calc(500 - 300 * var(--d))`, inte `font-variation-settings` som målbilden namnger | `performance.md` § 2 | Ordagrant: "`font-weight` as a property, never `font-variation-settings`" | Referensregeln är senare och mer specifik än målbildens formulering. Den betalar dessutom två gånger: mot ett icke-variabelt reservsnitt snappar `font-weight` till närmaste vikt och visar fortfarande en förändring, medan `font-variation-settings` hade varit helt inert |
| **`letter-spacing` toppar på 0,012 em** | Inte målbildens 0,06 em | Egen mätning i `act-mid-1440.png`, R2 | TASTE § 4.9 i sin generella form: det som visas ska vara sant om det som faktiskt händer | Tracking ackumulerar vänster till höger och är därför störst exakt vid sömmen, där de två rubrikkopiorna möts. Vid 0,06 em och 56 px är driften ~77 px vid 23:e tecknet, vilket sköt en hel glyf ur läge: `nutidens` renderades `nu\|idens`. Det läser som en raderad bokstav, inte som förfall. Vid 0,012 em är driften ~15 px, under en glyfbredd, och halvorna möts rent |
| **Rubriken behåller sin grad genom hela akten** | Ingen fall till 11 px monoetikett vid s3, tvärtemot `concepts-K4.md` § (3) | R2-promptens § 2 + briefens egen § Motion-tes, Continuity | "Den byter aldrig grad, aldrig snitt, aldrig radbrytning under akten" | Prompten är senare än concepts-filen och säger det uttryckligen. Briefens continuity-tes säger samma sak med andra ord: det är samma rad hela vägen och bara ena halvans vikt och tracking ändras |
| **Ingen `data-sc-cue` på foldens chrome** | Aktens cue `0 1 0 0` implementeras utan attributet | `performance.md` § 1 (vilande `will-change` = 0) + SKILL.md (reveal-system faller mot synligt) | Gate 93 | `0 1 0 0` betyder full opacitet hela akten, alltså visuellt identiskt med ingen cue. Attributet kostade tre saker: `scrollcraft.css` lägger en klassbred `will-change` på varje `[data-sc-cue]`, som `perf_probe` fångade vilande och som inte går att städa utan att redigera motorn; det startar folden på `opacity: 0`; och det ger ingen beteendeskillnad. Cue-kontraktet är uppfyllt i sak |
| **Calyx ligger underst och klipps aldrig** | Mallsidan ligger överst och är det enda lager som klipps och filtreras | Egen mätning, R2 | `performance.md` § 3, håll den animerade ytan liten | Två klippta lager gav p95 66,7 ms vid 4× CPU, ett gav 50,0 ms. Det flyttar dessutom klippningen från den tunga ramen till den lätta, och gör F-010 sant om pixlarna och inte bara om identiteten: den yta som fyller ramen vid ps = 1 har aldrig repainats av akten |
| **Tangentbordet scrollar akten** | Piltangenterna flyttar 2 % av `--split` genom att scrolla, inte genom ett lokalt värde i fjädern som R1:s brief föreslog | Persona **Edge** i det här dokumentet; `a11y-audit`, tangentbordspasset | Delaren är sidans enda interaktion, alltså också dess enda tangentbordsmål | Ett lokalt värde fjädrar tillbaka till scrollens värde inom 350 ms, så en tangentbordsanvändare hade fått noll varaktigt resultat av sidans enda interaktion. Att scrolla ger samma varaktiga effekt som hjulet. Mätt: 0,2778 → höger → 0,2585 (steg 2 %) → vänster → 0,2778 |
| **Nytt token `--ink-3` för 11 px-registret** | `oklch(0.50 0.016 68)`. `--ink-2` blir displayskala enbart | Egen kontrastmätning mot sidans renderade färger | WCAG AA 4,5:1 under 24 px; SKILL.md, ett värde som saknas lyfts till ett namngivet token | `--ink-2` på `--paper` är 3,21:1, vilket räcker för rubrikhalvan på 56 px och inte för något annat. De 11 px-etiketterna bär `En typisk mallsida`, alltså den sträng som gör det försvarbart att köra en anti-referens som innehåll, och den får vara sist av allt på sidan att vara svårläst. Efter bytet 5,27:1 |

## Direction contract

- **THESIS:** Skillnaden mellan sidan ni har och sidan ni kunde ha är inte en åsikt, den är
  synlig i samma rektangel och mätbar i sex tal, och ni får själva ta tag i gränsen mellan dem.
- **OWN-WORLD:** Världen är ett varmt tryckark där två utskrifter ligger kant i kant under
  jämnt ljus, och det enda Alunix själv ritar är strecket där de möts. Ingen annan sida i
  kedjan kör sin egen motståndare live och etiketterad bredvid sitt eget bevis, och ingen annan
  låter besökarens hand avgöra hur mycket av vardera som syns. Byrån påstår ingenting om sitt
  hantverk; den lägger fram två filer och ett mätprotokoll.
- **STORY:** Nio skärmar, en mening var, i ordning (skärmtabellen i `concepts-K4.md` § (3)).
  1. **s1** Två färdiga webbplatser står stilla mot varandra i samma ruta, och en enda rad text
     korsar sömmen i två toner, dämpad över den ena och bläck över den andra.
  2. **s2** Strecket börjar gå åt vänster och den vänstra sidans typ tunnas ut medan den tappar
     färg, som om påståendet demonstrerade sig självt.
  3. **s3** Strecket har lämnat ramen, Calyx fyller bilden, och rubriken har krympt till en
     etikett i hörnet.
  4. **s4** Skillnaden blir sex tal i displaygrad, avdelade av hårlinjer, där varje tal avslöjas
     från sin egen sida av linjen.
  5. **s5** Hōrai i full bredd, hel, en enda bildtext under.
  6. **s6** Hyperborea likadant, en i taget, aldrig sida vid sida.
  7. **s7** Tre tjänstenamn stiger ur en mask, tre rader i olika längd, radnumren i marginalen.
  8. **s8** Två priser räknas upp och det tredje står i klartext i stället för bakom en knapp.
  9. **s9** En rad i displayskala och en mejladress på ett papper som slutar röra sig.
- **FIRST VIEWPORT:** Vid 1440 × 900, ps = 0, exakt fem element i K4:s eget lager, uppräknade i
  målningsordning. (1) **Tvåtonsrubriken** `Er hemsida är nutidens visitkort`, en enda rad
  Switzer ~44 px, `wght` 500, vänsterställd men satt så att raden korsar sömmen vid 50 %;
  tecknen till vänster om sömmen i `--ink-2`, tecknen till höger i `--ink`, identisk grad,
  identisk vikt, identisk tracking. (2) **Kickern `Före`**, 11 px Reddit Mono, tracking 0,18 em,
  `--ink-2`, till vänster om raden. (3) **Kickern `Efter`**, samma sättning, till höger om
  raden. (4) **Delaren**, en 1 px lodrät linje över full viewporthöjd vid `--split` = 0,5.
  (5) **`kontakt@alunix.se`**, 15 px Switzer, `--ink`, i efter-halvans övre högra hörn.
  Därutöver etiketten `En typisk mallsida` i vänsterlagrets övre vänstra hörn, som är en
  ofrånkomlig del av att antagonisten visas alls och räknas till lagret utan att vara ett
  designelement. Allt annat i vyn är **innehåll**: de två sajterna, som inte är K4:s element
  utan K4:s bevis. Noll bar, noll meny, noll ordmärke, noll knapp, noll badge, noll bild.
- **FORM:** Ett plant varmt ark utan djup, där struktur uteslutande görs av hårlinjer och
  radie 0, ingenting kastar skugga, ingenting har en gradient, papperet byter aldrig temperatur,
  och den enda kromatiska händelsen på hela sidan är ett blått streck som är en meter och inte
  en dekoration.

## Persona-skisser

`reference-lock.md` § Three persona sketches. Villkoren är situationella, inte bara permanenta.

```text
Primary: Verksamhetsagare i Sverige, 35 till 55, som redan HAR en hemsida hen är missnojd med
  och inte kan satta ord på varfor · barbar dator, 1440 bredd, kontorsuppkoppling, mitt på
  dagen · kom for att se om någon kan forklara skillnaden utan branschjargong.
Edge:   Samma person på en maskin utan mus, som scrollar med tangentbord och navigerar med
  Tab · Page Down flyttar `--sc-ps` i hopp, inte i hack, och delaren har ingen tangentbords-
  vag alls om den bara lyssnar på pointer-handelser · det som bryter forst är signaturakten,
  om den bara lases med en pekare.
Stress: Samma bestallare på en telefon, 390 bredd, på en pendeltag med en hand upptagen och
  daligt natverk · två iframes är det första som inte laddar; sidan måste fortfarande gora
  sitt argument nar den hogra ramen är tom, och priserna och mejladressen får aldrig hamna
  bakom en interaktion.
```

Intersektionen som betalar två gånger: kravet att delaren ska fungera utan pekare är samma fix
som gör den användbar på en telefon där en dragrörelse konkurrerar med sidans egen scroll, och
kravet att sidan ska bära sitt argument med en tom höger ram är samma fix som gör den läsbar
för den som har bilder avstängda.

Den persona som är obekvämast: **Edge**, därför att den ställer signaturakten mot en
inmatningsmetod som inte har någon pekare alls, och det är den som lättast designas runt i
stället för för. **Konkret krav:** delaren har `tabindex="0"`, `role="separator"`,
`aria-orientation="vertical"` och svarar på vänster- och högerpil med steg om 2 % genom samma
fjäder som pekaren använder — alltså ingen separat kodväg och ingen synlig extra affordans.
`motion_probe` körs med `--wheel 20:120` **och** `--wheel 100:60`, och `staircase` ska vara 0
i båda.

## Motion-tes

Låst, ur `concepts-K4.md` § (5). Byggaren skriver om den med sina egna ord och lägger till
värden.

- **Focal:** Ögat följer **en lodrät linje**, och sidan ger det inget alternativ. Under hela a1
  står allt annat i vyn absolut stilla: ingen av de två sajterna flyttar en pixel, rubriken
  ligger kvar på sin rad, kickerna byter inte plats. Det enda som ändrar läge på skärmen är
  delarens `translateX`. Ett enda fokusskifte i hela akten, vid **ps ≈ 0,68**, när linjen
  passerar viewportens vänsterkant och blicken faller på ytan som blev kvar. Att linjen är det
  enda blå på sidan är inte ett färgval, det är fokusmekanismen.
- **Continuity:** Ingenting tonar in ur intet och ingenting hoppar in i vy. Båda sajterna är
  monterade och målade vid ps = 0; det enda som ändras är hur mycket av var och en som är
  synlig. Delaren startar i mitten där den redan syntes, färdas **monotont** åt ett håll och
  lämnar ramen: den vänder aldrig, den studsar aldrig, den nollställs aldrig, och den har ingen
  loop i vila. Rubriken är samma rad hela vägen och byter bara vikt och tracking på sin ena
  halva, alltså är det samma glyfer som stod där vid ps = 0. **F-010, uttryckligt:** ytan som
  fyller ramen vid ps = 1 är samma Calyx-ram som stod till höger vid ps = 0, samma DOM-nod,
  samma monterade dokument, inte en ny ruta ovanpå. Att scrolla uppåt kör hela sekvensen
  baklänges, tecken för tecken.
- **Feedback:** Scrollen **är** handen på delaren. 1 % aktprogress = 1 % förflyttning, i båda
  riktningarna, ingen låsning, ingen hijack utöver motorns egen `pin`. Pekaren har **samma
  auktoritet som hjulet**, inte mindre: `pointerdown` på den 44 px breda osynliga träffytan tar
  över värdet direkt och 1:1 med respekt för var på linjen greppet togs (`grabOffset`),
  `pointermove` skriver det, `pointerup` lämnar tillbaka det till scrollens värde genom en
  kritiskt dämpad fjäder seedad med hastigheten vid släppet. Rörelsen är **avbrytbar**: ett
  nytt `pointerdown` mitt i återgången tar vid i det läge och den hastighet fjädern hade,
  nollställer inte och hoppar inte. Det som målas är alltid fjäderns utvärde, aldrig pekarens
  råa x. Tangentbordet får exakt samma kanal, 2 % per piltryck genom samma fjäder.
- **Budget:** **En** `pin` på hela sidan (span 2,4, dwell 0,22). **Ett** tal, `--split`,
  skrivet **en gång per bildruta** av **en** rAF-loop som stannar av sig själv när
  `|mål − nuvarande| < 0,0005`. `--split` driver fyra egenskaper genom fyra `calc()` i CSS
  (`clip-path: inset()` på efter-lagret, `translateX` på delaren,
  `font-variation-settings` + `letter-spacing` på rubrikens före-halva, `filter: saturate()` på
  mallsidewrappern) och noll av dem läser layout. **Noll layoutläsningar i scroll-handlern**,
  som är passiv och bara schemalägger. `will-change: transform` bara på delaren och på de två
  lagrens wrappers, och bara medan `0 < ps < 1`. Två självhostade variabla `.woff2`, noll
  Google Fonts-länk i K4:s eget lager, noll `preconnect` från K4. Måltal vid 4× CPU, mätta i
  båda riktningarna med `motion_probe --wheel 20:120` **och** `--wheel 100:60`:
  `staircase = 0`, `max_step ≤ 3 %`, bildtid p95 ≤ 20 ms, noll frames > 33 ms.

**Författad tystnad** (så att `scroll_verify.py`s `blankBands` inte larmar falskt): de första
0,10 av a1 är avsiktligt orörliga. Båda sajterna står helt stilla medan besökaren läser
rubriken. Det är stillheten före toppen, inte död scroll.

## Feeling curve

| Akt / skärm | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| a1, s1–s3 | **Tillfredsställelse** ← TOPPEN | Två färdiga webbplatser står emot varandra i samma ruta, och den ena trycks ut ur bild av den andra medan besökarens hand kan ta tag i gränsen |
| a2, s4 | **Skärpa** | Känslan blir ett tal: sex mätta par i displaygrad, var och en avslöjad från sin egen sida |
| a3, s5–s6 | **Tillit** | Två sajter till, hela, i full bredd, en i taget |
| a4, s7 | **Klarhet** | Tre ord, tre rader, olika längd, ingenting annat i vyn |
| a5, s8 | **Trygghet** | Priserna räknas upp och det tredje står i klartext i stället för bakom en knapp |
| a6, s9 | **Ro** | En rad och en adress på ett papper som slutar röra sig |

Aldrig två lika i rad. Toppen är a1.

**Byggarens bekräftelse, rad för rad.** Alla sex bekräftas, ingen ändras, och skälet står per
rad så att bekräftelsen är en prövning och inte en nick.

| Akt | Dom | Prövningen |
|---|---|---|
| a1 Tillfredsställelse | **Bekräftad som topp.** | Den enda akten där besökaren kan göra något, och den enda med en `pin`. Den har sidans största span (2,4) med bred marginal, och den har tystnaden före sig inbyggd i sina egna första 0,10. `feel-and-fingerprint.md` § The peak kräver alla tre, och alla tre finns |
| a2 Skärpa | **Bekräftad.** | Skiljer sig från a1 i art och inte bara i grad: a1 är taktil, a2 är kognitiv. Det är precis övergången från att känna till att veta, och den kräver att a1 slutar med att något är avgjort |
| a3 Tillit | **Bekräftad, med en risk noterad.** | Två hela sajter i full bredd är rätt känsla efter sex tal. Risken är att en akt utan interaktion direkt efter en akt med sex tal kan läsas som en paus; motverkas av att objekten är fullbleed och alltså inte kan läsas som "mer information" |
| a4 Klarhet | **Bekräftad.** | Tre ord i olika radlängd efter två bildtunga skärmar är den största kontrasten i hela kurvan. Att `kinetic` ligger här och inte tidigare är vad som gör det till klarhet och inte till effekt |
| a5 Trygghet | **Bekräftad.** | `count` på två sanna tal följt av en klartextrad är trygghet och inte skryt, just eftersom det tredje priset inte gömmer sig |
| a6 Ro | **Bekräftad.** | Enda akten där ingenting rör sig när den är klar. Kurvan måste sluta i vila, annars slutar sidan i en känsla av att något återstår |

Ingen rad delar känsla med sin granne, och den enda paret som ligger nära varandra i art
(a4 Klarhet och a6 Ro) är åtskilda av a5.

## Tell-someone

> Det är sajten där den dåliga hemsidan bokstavligen trycks ut ur bild av den bra, och man kan
> ta tag i gränsen och skjuta på själv.

## Device-tabell

Kolumnen **läser** anger `--sc-p` eller `--sc-ps` per device. F-014: allt som ögat ser
förflytta sig läser `--sc-ps`.

| # | Akt | Device | Familj | Läser | Varför |
|---|---|---|---|---|---|
| 1 | a1 | `pin` span 2,4 dwell 0,22, cue `0 1 0 0` | pin | `--sc-ps` (via `--split`) | Split stages egen lutning, ordagrant "`pin` with divider" |
| 2 | a1 | bespoke `paintSplit`: `clip-path: inset()` på efter-lagret, `translateX` på delaren, `font-variation-settings` + `letter-spacing` på rubrikens före-halva, `saturate()` på mallsidewrappern | bespoke paint | `--sc-ps` (via `--split`) | Fyra egenskaper, ett tal, en rAF-loop |
| 3 | a1 | kickernas cue-opacitet | cue | `--sc-p` | Opacitet förflyttar sig inte |
| 4 | a2 | `reveal` per sida, `left` på före-kolumnen och `right` på efter-kolumnen | reveal | `--sc-ps` | Split stages andra lutning, ordagrant "`reveal` per side" |
| 5 | a3 | `flow` + `in`, stagger 90 ms | flow | `--sc-p` (opacitet); motorns egen (14 px-lyftet) | Full-bleed objekt får passera efter upplösningen; de ska inte pinnas |
| 6 | a4 | `kinetic` lines, cue `0.1 0.9 0.15 0.4` | kinetic | motorns egen (raderna); `--sc-ps` (radnumrens hårlinje) | En kinetisk rubrik per sida, och rader är rätt form |
| 7 | a5 | `count`, `data-sc-count-at="0.1 0.5"`, 1,4 s | count | motorns egen | Split stages tredje lutning, "real `count`"; bara sanna tal |
| 8 | a6 | `reveal`, cue `0.25` (ett värde: sista akten måste hålla) | reveal | `--sc-ps` | Avslutet ska lösa upp, inte tona ut |

Fem familjer, aldrig samma två i rad. **Noll `pan`, noll `drift`, noll `spotlight`, noll
`magnet`, noll `scrub`** — alla fem förbjudna av split stage. `will-change` bara på delaren
och på de två lagrens wrappers, och bara medan `0 < ps < 1`.

## Rejected-lista

Ur `find-animation-opportunities`-gaten, fyra frågor per kandidat. Full tabell i
`concepts-K4.md` § (5). Avvisade: delaren snäpper tillbaka till 50 % · handtag, knopp eller
"dra"-text på delaren · hover-lyft på skillnadsliggarens rader · mallsidan faller isär eller
skakar · delaren rör sig av sig själv i vila · marquee med exempelsajternas namn · spotlight
eller magnet på avslutets mailto. Behållna som bärande: delaren som scroll- och pekardriven
gräns · rubrikens före-halva som degraderas längs delaren.

### Byggarens ytterligare kandidater, R1

Sex kandidater till, var och en genom `find-animation-opportunities`-gatens fyra frågor
(frekvens, syfte, hastighet, funktion). Fem avvisade, en behållen med villkor.

| Kandidat | Frekvens | Syfte | Hastighet | Funktion | Dom |
|---|---|---|---|---|---|
| **Rubriktecknen byter ton individuellt när sömmen passerar genom dem** (varje glyf går från `--ink-2` till `--ink` i det ögonblick delaren korsar den) | En gång per besök, kontinuerligt genom a1 | Göra tvåtonsbrytningen till en följd av delarens läge i stället för ett statiskt val | Bunden till `--split`, ingen egen varaktighet | **Ja, och den är avgörande.** Utan den är tvåtonen ett påstående; med den *är* tonen var gränsen går | **Behållen, med villkor.** Implementeras som två absolut överlagrade kopior av samma rad, den nedre i `--ink-2` och den övre i `--ink`, där den övre klipps av samma `inset()` som efter-lagret. Villkoret: **exakt samma clip-tal**, annars driftar tonbrytningen från sömmen och devicen blir en effekt. Aldrig per-glyf-DOM, som skulle betyda 34 element som skrivs varje bildruta |
| Delaren får en subtil skugga eller glöd så att den "lyfter" från de två sidorna | Alltid synlig | Läsbarhet mot ljusa partier i båda sajterna | Statisk | Marginell, och den finns en billigare lösning | **Avvisad.** Noll `box-shadow` i K4:s lager (TASTE § 2.3, F-006), och en glöd på sidans enda accent skulle göra strecket till ett objekt med djup i en värld som är plan. Läsbarhetsproblemet är verkligt och löses i stället med 1 px `--ink` under det blå, alltså en tvålagerslinje utan oskärpa |
| Parallax på de två lagren, så att sajterna glider olika fort medan delaren rör sig | Hela a1 | Djup | Bunden till scroll | Ingen, och den bryter kravet | **Avvisad.** PRODUCT.md § Operating Context: en visad ram får aldrig transformeras. En parallax *är* en transform på ramen. Dessutom är hela continuity-tesen att bara gränsen rör sig |
| Skillnadsliggarens tal räknar upp i stället för att wipeas fram | En gång, a2 | Låna a5:s energi till a2 | 1,2 s per rad | Ingen, och den kostar en device | **Avvisad.** `devices.md` § device kit: aldrig samma familj två gånger; `count` är redan bokad till a5, och en `count` i a2 skulle göra a5 till en upprepning. Wipe per sida är dessutom det som håller argumentets geometri levande efter att delaren är borta |
| Rubriken följer med ner och blir a2:s löphuvud i en kontinuerlig rörelse | En gång per besök | Kontinuitet mellan a1 och a2 | ~600 ms | Marginell, och den skapar ett andra fokus | **Avvisad.** Rubriken faller redan till en 11 px monoetikett i s3, alltså är övergången redan löst med en gradändring. Att dessutom flytta den genom akterna ger a2 två saker att titta på, och a2:s displayelement är talen |
| En framstegsindikator för delarens läge, hur diskret som helst | Hela a1 | Orientering | Bunden till `--split` | Ingen | **Avvisad, och den är den farligaste i listan.** En avläsning av delarens läge är exakt F-006:s telemetri-chrome, och antagonisten som körs bredvid innehåller redan ett dashboardkort som gör just det. Sidan får aldrig rapportera ett tillstånd om sig själv. Delarens läge **är** avläsningen |

## Delight-tes

Delaren tippar.

## Asset-lock per medieplats

Fyra platser, fullständiga block i `runs/K4/assets/ASSETS.md` § 4: före-ramen · efter-ramen ·
Hōrai-objektet · Hyperborea-objektet. **Ingen av dem är en generate-prompt, och ingen
generate-prompt författas i den här cellen** (`assets/credits.json`,
`generated_material.present: false`). Saknas något: skriv `[needs asset: ...]` och gå vidare,
generera aldrig.

## Fem live-rubriker i kategorin, ordagrant

Webbsök `webbyrå digital byrå webbdesign Sverige`, H1 hämtad från varje sida 2026-09-10 och
citerad exakt.

| # | Rubrik, ordagrant | Källa |
|---|---|---|
| 1 | `Webbyrå i Stockholm` | frojd.se |
| 2 | `Digitalbyrå / Webbyrå i Stockholm` | ead.se |
| 3 | `Marknadsföring och webb som driver fler kunder till dig` | sitea.se |
| 4 | `Den norrländska Webbyrån som hjälper dig att synas digitalt.` | norrlandswebbyra.se |
| 5 | `Webbdesign - vi gör inget lagom` | digitalwebbyra.se/webbdesign |

Vad ribban faktiskt är: tre av fem säger bara vad företaget är och var det ligger, och den
fjärde säger vad byrån gör för sig själv. Bara nummer 5 har ett tonfall. Alunix ordagranna
rubrik, `Er hemsida är nutidens visitkort`, säger i stället något om läsaren, och det är den
enda av de sex som gör det. Den ändras aldrig, och ingen ny rubrik på sidan får falla tillbaka
till kategoriformen "substantiv plus ort".

**Byggarens egen hämtning, 2026-09-10. Alla fem rader stämmer ordagrant.** Sökningen kördes på
`digital byrå webbdesign Sverige` och H1 hämtades per sida.

| # | Kontroll | Utfall |
|---|---|---|
| 1 | `frojd.se` | `Webbyrå i Stockholm`. **Identisk.** |
| 2 | `ead.se` | `Digitalbyrå / Webbyrå i Stockholm`. **Identisk.** |
| 3 | `sitea.se` | `Marknadsföring och webb som driver fler kunder till dig`. **Identisk**, och den sitter på rotsidan. **Notering, ingen tyst ändring:** min egen sökning rankade i stället undersidan `sitea.se/digital-byra/`, vars H1 lyder `Din digitala byrå i Stockholm`. Den sidan har dessutom sjutton H1-element, alltså en egen defekt. Arkitektens rad står kvar eftersom rotsidan är rätt jämförelseobjekt, men den alternativa rubriken noteras här och stärker analysen nedan: den är återigen formen substantiv plus ort |
| 4 | `norrlandswebbyra.se` | `Den norrländska Webbyrån som hjälper dig att synas digitalt.` **Identisk.** Ordet `synas` är kursiverat i källan. Ingen rotation observerad, alltså är raden stabil och inte en variant |
| 5 | `digitalwebbyra.se/webbdesign` | `Webbdesign - vi gör inget lagom`. **Identisk**, inklusive det korta bindestrecket, som är sajtens eget tecken och citeras som det står |

Två observationer utöver kontrollen, båda relevanta för R3. **För det första:** min sökning
gav inte samma femma som arkitektens. Fyra av fem sammanföll (`frojd.se`, `sitea.se`,
`digitalwebbyra.se`, `ead.se`), medan `norrlandswebbyra.se` inte låg bland mina träffar och
`limetta.se`, `entire.se` och `wilsoncreative.se` gjorde det. Femman är alltså en av flera
möjliga femmor, och analysen under tabellen håller ändå: också de tre nya kandidaterna är
`Digitalbyrå i Stockholm`-formade. **För det andra:** ingen av de fem citerar ett tal, och
ingen av dem säger något om läsaren. K4 gör båda, och det är den enda av de sex sidorna som
gör någotdera.

## Copy-plan

**Ordagrant, ändras aldrig** (PRODUCT.md § Brand Commitments): hero-rubriken
`Er hemsida är nutidens visitkort`, underraden, tesrubriken `VI BYGGER ERT VARUMÄRKE.`
(versal form, r7-promptens sträng, se Q9), raden
`Webbdesign, design och system. Allt på ett ställe.`, tjänsterna `Design` / `Utveckling` /
`System` med 01–03, de tre paketraderna med priser, prisrubriken
`Alla har rätt till bra design.`, `kontakt@alunix.se`, och de tre bildtexterna
`Exempelsida: Calyx, florist i Stockholm` / `Exempelsida: Hōrai, Asian fusion-koncept` /
`Exempelsida: Hyperborea, konferens i Lund`.

**Nya strängar i K4** (går genom copy-gatens fem pass i R3):

- `Före` och `Efter` — de två monoetiketterna. Två ord, inga fler.
- `En typisk mallsida` — etiketten på vänsterhalvan. **Ordagrann och obligatorisk.** Den får
  aldrig bytas mot ett påhittat kundnamn, ett varumärke eller en förkortning, och den får
  aldrig utelämnas.
- Skillnadsliggarens sex radetiketter, ordagrant, skrivna i R1 och **ogatade tills R3**. De
  namnger vad som mätts och dömer aldrig.

  | # | Etikett, ordagrant | Varför just den formuleringen |
  |---|---|---|
  | 01 | `Textfärger` | Namnger enheten, inte omdömet. Inte `Färgkaos`, inte `Antal färger` (som skulle kunna läsas som hela paletten och inte bara texten) |
  | 02 | `Typvikter` | Samma. Inte `Typografisk disciplin`, som är en dom |
  | 03 | `Typskala` | Talet under är ett spann och en faktor, och etiketten säger vilken storhet det är. Inte `Kontrast`, som betyder något annat i den här kedjan |
  | 04 | `Kortformer` | Räknar `rounded-lg/xl/2xl` i källan. Inte `Kort med skugga`, som målbilden skriver, eftersom det som faktiskt räknas är radien och inte skuggan. Att skriva `skugga` vore ett tal som inte är mätt |
  | 05 | `Gradienter` | Räknar gradienter i källan. Rakt av |
  | 06 | `Fotografier` | Inte `Riktiga fotografier`, som lägger in ett värdeord i etiketten. Talet säger noll mot fyra, och det räcker |

  Reservraden, om en av de sex faller vid ombrytning: `Sidmarginal vid 1440`.

  **En regel för hela liggaren, som gäller varje etikett:** substantiv i plural, ett eller två
  ord, ingen artikel, inget adjektiv, ingen jämförelse i etiketten. Jämförelsen görs av de två
  talen, och den ska kunna läsas åt båda hållen av någon som är oense.
- De tre tjänsteunderraderna, som PRODUCT.md redovisar som öppna (Q6). **Förslag skrivna i R1,
  ogatade tills R3.** Byråröst i vi-form, korta satser, fakta före adjektiv, inga tankstreck,
  inga påståenden om kunder eller resultat, och ingen av dem längre än raden ovanför sig:

  | # | Namn (låst) | Underrad (förslag, ogatad) |
  |---|---|---|
  | 01 | `Design` | `Vi ritar sidan innan vi bygger den.` |
  | 02 | `Utveckling` | `Vi skriver koden själva, i det här repot.` |
  | 03 | `System` | `Bokning, betalning och kunddatabas när ni behöver det.` |

  Motiveringen till att de får finnas alls: PRODUCT.md kräver "en kort underrad var" och
  lämnar texten öppen, så raden är beställd men inte skriven. Motiveringen till just dessa: de
  säger vad byrån **gör**, inte vad kunden får, och rad 02 är den enda på hela sidan som
  refererar till sidan man tittar på, vilket är samma sorts belägg som ramarna. Rad 03 återger
  paketrad två med andra ord och kan behöva bytas i R3 om copy-gaten läser det som upprepning.

**Noll tankstreck i synlig text.** Gäller varje ny sträng, inklusive liggarens etiketter.

**Förbjudet i copy:** varje ord som dömer mallsidan. Sidan visar och mäter; den kallar
ingenting fult. Ett tal som säger 9 mot 4 är hårdare än varje adjektiv och är dessutom
kontrollerbart av läsaren.

## Skillnadsliggaren, med de mätta talen

Sex rader. **Varje tal är mätt av arkitekten 2026-09-09 mot de två faktiska filerna**, med
kommandon och ordagrann utdata i `concepts-K4.md` § Mätning. TASTE § 4.9: siffror får vara
textur bara om de är sanna. **Hittar byggaren ett annat tal när hen kör om mätningen är det
byggarens tal som gäller, och avvikelsen skrivs som en rad i ledgern.**

Servern startas från repo-roten: `python ~/.claude/skills/design/scripts/serve.py --port 3399 --root .`
Mätningen körs om med:
`python ~/.claude/skills/design/scripts/measure.py http://localhost:3399/sites/before-ai-slop.html`
och samma kommando mot `/sites/calyx.html`.

| # | Vad som mätts | En typisk mallsida | Calyx | Källa till talet |
|---|---|---|---|---|
| 01 | Textfärger | **9** | **4** | `measure.py` → `distinctTextColors` |
| 02 | Typvikter | **4** | **1** | `measure.py` → `distinctWeights` |
| 03 | Typskala, minsta till största | **12 → 60 px**, 5,0× | **11 → 130 px**, 11,8× | `measure.py` → `fontSizeRange` |
| 04 | Kortformer (`rounded-lg`/`xl`/`2xl`) | **8** | **0** | Källräkning, kommandot i `concepts-K4.md` § Mätning |
| 05 | Gradienter i källan | **8** | **2** (båda scrim över foto) | Samma källräkning |
| 06 | Riktiga fotografier | **0** | **4** | Samma källräkning: `<img>` 0 i båda; `url()` ger 1 SVG-referens mot 1 grain + 4 Unsplash-fotografier |

**Reservrad om en av de sex faller vid ombrytning:** `Sidmarginal vid 1440`: **0 px** mot
**32 px** (`measure.py` → `contentWidthUsed` 1440 mot 1376).

**En rad målbilden namnger men mätningen inte bär, och som därför är struken:** `hårlinjer`.
`measure.py` ger `hairlineRules` **12 för mallsidan och 10 för Calyx**, alltså tvärtemot vad
målbilden antar. Raden får inte återinföras och får inte vändas till en fördel med en annan
tolkning. Källa: TASTE § 4.9.

**Formregel för liggaren:** hårlinjerader (harkcap-formen), aldrig kort, aldrig en graf,
aldrig en stapel, aldrig en sparkline (gate 79). Talen i displaygrad i `--ink`, etiketterna i
11 px Reddit Mono i `--ink-2`. Före-talet står till vänster om hårlinjen och avslöjas från
vänster; efter-talet står till höger och avslöjas från höger.

## Prestandaplan

Mot budgeten i `performance.md` § 1. Varje rad har ett målvärde.

| Post | Budget | Plan i K4 |
|---|---|---|
| **Två live-iframes** (budgetens svåraste post) | Total överföring ≤ 2,5 MB vid 1440 | Vänsterramen (`before-ai-slop.html`, 9 016 B, noll bilder, noll externa resurser) monteras **eagerly**, eftersom den är folden. Högerramen (`calyx.html`, 16 238 B, men **fyra externa Unsplash-bilder** vid `w=1600/1600/2000/2400` som K4 inte kan påverka) monteras via **IntersectionObserver + `loading="lazy"`**, och båda `<iframe>` får `width`/`height` så att inget lager hoppar. `content-visibility: auto` med `contain-intrinsic-size` på a3–a6. **Mätt i R2: 1 690 kB vid 1440, alltså inom taket.** Båda ramarna förblir levande och beslutsregeln nedan utlöses inte. LCP 472 ms, CLS 0,000. **Men se § Byggarens öppna frågor B6:** rörelsebaren faller ändå, och den ram som kostar är Calyx, inte mallsidan, så regeln nedan namnger fel ram. **Två rättelser till den här raden, med belägg, se decision ledger:** (a) vänsterramen är **inte** fri från externa resurser, den laddar `cdn.tailwindcss.com` plus `fonts.googleapis.com`/`fonts.gstatic.com` (Inter, fyra vikter), och Calyx laddar samma tre värdar, alltså kör sidan **två Tailwind-kompilatorer**; (b) ordet "eagerly" utgår, `performance.md` § 6 förbjuder en ram monterad vid load, så båda ramarna monteras av IntersectionObserver och vänsterramen dessutom vid första `requestIdleCallback` efter first paint. **Beslutsregel om talet överstiger 2,5 MB:** vänsterramen degraderas till en skärmbild och högerramen förblir live, aldrig tvärtom — PRODUCT.md princip 1 säger att beviset ska gå att använda, och antagonisten är inte bevis |
| **LCP-elementet** | LCP ≤ 1,8 s | LCP-elementet är **K4:s egen tvåtonsrubrik**, inte någon av ramarna. Den är text i ett självhostat variabelt snitt med `<link rel="preload" as="font" crossorigin>` på Switzer och `font-display: swap` med metric-matchad fallback via `size-adjust`. Ingen ram får vara sidans LCP-element; om `perf_probe` säger något annat är det ett fel som ska åtgärdas, inte förklaras |
| **Typsnittsfiler** | ≤ 3 filer, ≤ 300 kB | Exakt **två** självhostade `.woff2`: Switzer variabel (`wght` 100–900) och Reddit Mono variabel (`wght` 200–900). Ingen Google Fonts-länk, ingen `preconnect`. `preload` bara på Switzer, som är folden |
| **Långa tasks under scroll** | 0 | En passiv scroll-lyssnare som bara schemalägger; **en** rAF-loop som läser `--sc-ps` och skriver `--split`; deadband som stoppar loopen i vila. Noll layoutläsningar i scroll-handlern. `sc-smooth.js` kopieras in oförändrad (`scroll/NOTE.md`: copy, never edit) |
| **Vilande `will-change`** | 0 | Sätts bara på delaren och på de två lagrens wrappers, och bara medan `0 < ps < 1`. Inga klass-nivå-promoveringar |
| **`filter` på en iframe-wrapper** | Ingen mätbar kostnad i frame-tiden | `saturate()` på **en** wrapper, ingen `blur`, ingen `drop-shadow`. **Mätt i R2, och filtret kostar ingenting:** p95 50,0 ms med `filter: saturate()` aktivt och 50,0 ms med `clip-path` **och** `filter` helt borttagna, alltså identiskt. Filtret behålls. Ytan är dessutom mindre än planen antog, eftersom mallsidelagret nu ligger överst och klipps till sin egen krympande halva, så den filtrerade ytan går från 50 % till 0 % över akten i stället för att ligga still. **Risknotering som R2 ska bevaka:** filtret ligger på en wrapper som täcker upp till halva viewporten, och `performance.md` § 1 sätter taket "`filter` på > 50 % av viewporten: 0". Ytan är per konstruktion `var(--split)` bred, alltså ≤ 50 % från ps ≈ 0,5 och nedåt men **exakt 50 % vid ps = 0** och mer i `?preview=before`. Mätningen ska därför köras vid `--split` = 1, inte vid 0,5 |
| **Externa resurser i K4:s eget lager** | 0 | Noll. Inga bilder, inga ikoner, inga CDN-anrop. De enda externa bytes som sidan orsakar kommer inifrån `calyx.html`, som är en fil vi inte redigerar |

Dessutom: `min-height: 100dvh`, aldrig `100vh`. Ingen `transition: all`. Ingen
`backdrop-filter`. `text-wrap: balance` på rubriker. Alla `<img>` har `width` och `height`.

Målvärden som ska vara sanna innan rundan lämnas, mätt vid 4× CPU: `staircase = 0`,
`max_step ≤ 3 %`, frame p95 ≤ 20 ms, noll frames > 33 ms, båda scrollriktningarna,
LCP ≤ 1,8 s, CLS ≤ 0,05.

## `?preview=`-plan

| Läge | Vad det tvingar | Varför det behövs |
|---|---|---|
| `?preview=before` | `--split: 100%` (delaren vid högerkanten, mallsidan fyller ramen) | Lead ska kunna skärmbilda argumentets startpunkt utan att scrolla |
| `?preview=split` | `--split: 50%` | Baslinjen för folden, exakt 50/50 |
| **`?preview=after`** | **`--split: 0%`** — det upplösta läget, "efter"-sidan fyller bilden | **Obligatoriskt.** F-007-kontrollen av s3 kan inte köras utan det, och lead ska kunna skjuta det upplösta läget i vila |
| `?preview=mid` | `--split: 25%`, alltså mitt i degraderingen | Kontrollen att rubrikens före-halva faktiskt tunnas och att den fortfarande är läsbar mot papperet |
| **`?preview=drag`** | `--split: 50%` plus `document.documentElement.dataset.scDrag = "1"`, vilket sätter träffytan till 30 % opacitet i `--blue` **bara i det här läget** | Affordansen är avsiktligt osynlig (gate 88), vilket betyder att ingen granskare kan se om träffytan sitter rätt eller är 44 px bred. Läget gör den synlig för mätning och aldrig för en besökare. Det är den enda `?preview=` som visar något som inte finns på sidan, och skälet står här så att ingen tar det för en affordans |
| **`?preview=degraded`** | `--split: 10%` och `window.__scFreezeMotion = true` | Rubrikens före-halva är som tunnast strax innan sömmen lämnar ramen, alltså är det där degraderingen ska granskas mot papperet. `?preview=mid` (25 %) visar mitten av rörelsen; det här läget visar dess ände, och `--ink-2` vid `wght` 200 är den kritiska kontrastmätningen i hela cellen |
| **`?preview=a2`** | Scrollar till a2:s början och sätter `data-sc-reveal-at` till sitt slutläge | F-007 körs skärm för skärm, och s4 (skillnadsliggarens tal) är den enda skärmen efter folden vars formade läge kräver en avslöjning som redan gått klart. Utan läget måste lead scrolla manuellt och kan fånga en wipe i flykten |

Alla lägen sätter `window.__scFreezeMotion = true` så att shimen spårar det råa värdet exakt
och skärmbilden visar det formade läget, inte en lerp i flykten. Alla lägen kopplar dessutom
bort pekarens drag, så att en skärmbild aldrig kan fångas mitt i en fjäder.

## Fingerprint

Fingerprint-gaten (≥ 4/6 mot varje registerrad) **gäller K4 fullt ut**: cellen är ett nytt
koncept, inte en iteration. Alla 36 rader står utskrivna i `concepts-K4.md` § (4). **Lägsta
summa: 5/6**, mot r1 K2 Tjänsteledger, r2 R5 Konsolram och r3 build — de tre andra
split stage-raderna i registret — och i samtliga fall är den delade dimensionen *grammatik*,
som målbilden själv låser. Ingen rad faller under 4/6 och ingen rad delar mer än en dimension.

Mot **K3** klarar K4 alla sex dimensionerna plus de två extra (temperatur och typsnitt),
alltså 8/8; den tunnaste raden är *aktform*, och skälet står utskrivet i `concepts-K4.md`
§ (4). Den föreslagna registerraden för K4 förs in av lead efter Antons dom, inte av byggaren.

**Byggarens kontroll, R1.** Jag har läst hela `wiki/projects/_index/design-fingerprints.md`,
alla 141 rader: rubrik, båda läsanvisningarna, de 7 seedraderna, de 29 Alunix-raderna och
avsnittet *Vad dessa rader delar*. **Ingenting i registret motsäger den föreslagna raden**, och
arkitektens utfall stämmer på alla tre punkter jag kunde kontrollera mot källan: 7 + 29 = 36
byggrader, tre `split stage`-rader (r1 K2, r2 R5, r3 build), och ingen rad under 4/6.

Fyra saker registret säger som cellen bör bära med sig, och som inte står i § (4):

1. **Registrets egen varning träffar inte K4, men den träffar nära.** Avsnittet *Vad dessa
   rader delar* pekar ut två navmönster som förbrukade (den tunna scrollande topprad som fem
   `continuous world`-rader delar, och den fixerade minimala baren som fyra `filmic one-shot`-
   rader delar) och två hero-devicer likaså. K4:s nav och hero ligger utanför båda listorna,
   men bara därför att cellen inte har någon topprad alls. Skulle R2 någon gång behöva
   "bara en liten rad" i toppen landar cellen omedelbart i det mest förbrukade mönstret i
   registret. Raden står här som en spärr inför R2.
2. **`before-ai-slop` har en egen registerrad, och den är instruktiv i den här cellen.** Dess
   signaturkolumn säger `none — no bespoke interaction at all, not even a scroll reveal`.
   K4 kör alltså en rad ur registret **live inuti** en annan rad ur registret. Det är, så vitt
   registret visar, unikt, och det är värt att lead noterar när K4:s rad förs in: den nya raden
   innehåller en befintlig rad som innehåll.
3. **Registret säger att rader är append-only och aldrig redigeras för att ge plats.**
   K4 begär ingen ändring i någon befintlig rad, och `before-ai-slop`-raden ska stå kvar
   oförändrad även när den citeras som innehåll av K4.
4. **Den enda mekaniska osäkerheten jag hittade** är att registrets huvud är daterat
   `updated: 2026-09-03` medan Alunix-blocket är daterat `appended 2026-09-09`. Datumfältet är
   alltså inaktuellt. Det påverkar ingen gate och jag ändrar det inte, eftersom registret bor i
   valvet och den här sessionen bara skriver under `runs/K4`. Noterat för lead.

Den föreslagna registerraden för K4 förs in av lead efter Antons dom, inte av mig.

## Vad jag måste slå

En rad per låst referens. Full tabell med mätpunkter i `concepts-K4.md` § (7).

**Varje rad namnger sitt belägg.** Lead läste referensernas folds som pixlar efter R1 och tre
påståenden gick inte att belägga ur folden ensam; arkitekten belade dem sedan ur respektive
`entry.md`. Pekaren står därför i raden, där påståendet läses, och inte bara i § Lästa
referenser. **En rad utan pekare stryks ur låset i fas 2.**

- **`paper`** — tvåtonsrubrikens två toner betyder något (var den ena sajten slutar och den
  andra börjar), och devicen förstörs med avsikt av delaren i stället för att stå still.
  **Belägg:** `entry.md` § Signature move och § Why it works stycke 2, som säger ordagrant att
  de två raderna har identisk grad, vikt och tracking och att effekten kommer *"entirely from
  colour"*, samt § What to leave rad 1, som säger att devicen inte tål en betoning mitt i
  meningen. Bekräftat i pixlar i `paper/fold.webp` och `paper/slices/00`: brytningen ligger på
  en semantisk gräns, inte på en radbrytning. **Folden ensam räcker inte** för påståendet att
  metrikerna är identiska; det står i texten, inte i bilden.
- **`harkcap`** — undanhållandet sker i berättelsen, inte i pekaren, så det händer även för
  den som aldrig hovrar; och objektet är metaforen i stället för att sakna en.
  **Belägg:** `harkcap/slices/04` som pixlar (hover-listan: tolv namn i ljusgrått, ett i
  helsvart, porträttet centrerat över listan) plus `entry.md` § Signature move för mekaniken
  och § What to leave rad 3, som är postens egen anmärkning att heroobjektet *"carries no
  explicit metaphor tied to NAV financing"*. Hårlinjeformen som skillnadsliggaren ärver står i
  `harkcap/slices/05` och `06` som pixlar, inte i folden.
- **`mode`** — accenten är inhägnad till ett **objekt** som finns exakt en gång, inte till en
  komponenttyp; och samma sorts displaytal levereras i en hårlinjeliggare utan ett enda kort.
  **Belägg:** `entry.md` § What to borrow punkt 4, ordagrant *"Fence the single accent colour
  to one component type"*, och § Signature move, som beskriver statkortet med `8.2K` i
  Paper White och etiketten i chartreuse. Kortet är sett i pixlar i `mode/fold.webp`
  (mörkgrönt kort, stapeldiagram, uppe till höger).
- **`gocanopy`** — exakt två monoetiketter på hela sidan, och de namnger de två halvorna i
  stället för att stötta ett påstående.
  **Belägg:** `entry.md` § Signature move för den lodräta inramningen, och — viktigare för
  K4:s 90-gradersrotation — **`gocanopy/slices/08` som pixlar**, där samma två monoetiketter
  står **vågrätt** på en gemensam baslinje i footern, `INTELLIGENCE THAT COMPOUNDS` vänster och
  `AI-NATIVE FROM DAY ONE` höger. Posten nämner aldrig den varianten i text. Rotationen är
  alltså en läsning av källan och inte en uppfinning ovanpå den, och det är den slicen som
  belägger det.
- **`customer-io`** — noll lån. Produkten körs i ramen och går att använda med musen; ingen
  skärmbild iscensätts i något.
  **Belägg:** `entry.md` § Signature move, ordagrant *"the staged screenshot-in-a-room"* och
  *"It borrows the credibility of a lifestyle photo for a screenshot"*, plus
  `customer-io/fold.webp` som pixlar (dashboarden i ett suddigt dagsljusrum under folden).
  Den här raden slår referensen genom att ta bort ett steg, så belägget är postens egen
  formulering av vad steget är.
- **`before-ai-slop`** — noll av dess drag citeras i K4:s eget lager, och varje påstående om
  den är ett mätt tal med kommandot utskrivet.
  **Belägg:** filen läst i sin helhet som kod (`sites/before-ai-slop.html`, 156 rader), och
  varje tal i § Skillnadsliggaren med sitt kommando i `concepts-K4.md` § Mätning. Egen
  R1-mätning: `families {"Inter": 61}`, alltså är antagonistens typsnitt Inter, vilket är ett
  av skälen att Inter är uteslutet i § decision ledger rad Typ.

## Lästa referenser

Tre rader per fil: vad den gör · vad jag tar · vad jag lämnar. Arkitektens digest står i
`concepts-K4.md` § Lästa referenser och ersätter inte den här.

**Vad jag faktiskt öppnade som pixlar, exakt.** Alla fem `fold.webp` och **alla 55 slices**:
`paper/slices/00–10` (11), `gocanopy/slices/00–08` (9), `harkcap/slices/00–11` (12),
`mode/slices/00–10` (11), `customer-io/slices/00–09` (10). Inget påstående nedan bygger på en
bild jag inte öppnat. **Antal filer lästa i den här sessionen: 33** (5 `entry.md`, 5
`design-language.md`, 60 bilder räknade som 5 slug-set, 2 sajtfiler, 7 kedjereferenser,
1 registerfil, 5 cellfiler, 5 hämtade H1). Räkningen står i rundans slutrapport.

### Smak och återkoppling

| Fil | Vad den gör | Vad jag tar | Vad jag lämnar |
|---|---|---|---|
| `design-catalogue/TASTE.md` (hela) | Beskriver harmonin i 89 sparade källor som fem relationer och tio beslutsregler, med **en auktoritet per sida** som den bärande | § 1 rad 4 (produkten bär, typen tyst eller versal i små grader, ytan flat), § 2.3 (hårlinjer och ton på ton, aldrig kort), § 2.4 (5–15× skalkontrast), § 4.4 (ett papper, en accent som gör en sak), § 4.9 (siffror som textur bara om de är sanna) | § 2.2:s tillåtelse att vit yta får vara varmvit i undantagsfall (K4:s papper är uttryckligt varmt, inte vitt), och § 4.10 (ordmärket får vara heron), som K4 inte har något ordmärke för |
| `design-catalogue/FEEDBACK.md` (alla 14 poster) | Antons domar, en regel per post, med citat och status | **F-006** (glas, dashboard, live-prickar, telemetri: den känsligaste posten här, eftersom antagonisten *innehåller* ett sådant kort), **F-007** (målbildskontroll bild för bild, vilket är varför skärmlistan är nio och inte sex), **F-010** (samma ram vid ps = 1 som vid ps = 0, aldrig en ny ruta), **F-011** (rörelsen spelas alltid, inget reservläge, fältet finns inte), **F-014** (`--sc-ps`, och särskilt efterspelets `inherits: true`-bugg, som är direkt återanvändbar på `--split`) | F-001 och F-002:s reservlägesregler, uttryckligen upphävda av F-011; F-004:s krav på en plate bredvid ordmärket, som gäller en typburen hero och inte den här |

### De fem valda katalogposterna

| Post | Vad den gör | Vad jag tar | Vad jag lämnar |
|---|---|---|---|
| **`paper`** `entry.md` + § Motion + § Reference lock | Bygger folden på en tvåtonsrubrik med **identiska metriker** där bara fyllnadsfärgen skiljer, och hägnar in sitt enda blå till märke och kodsyntax, aldrig knapp eller länk. Tre lagers skugga finns men bara på produktskärmbilden | Devicen ordagrant som foldens rubrikform, plus inhägnadsprincipen flyttad från komponent till **objekt**. Och `cubic-bezier(0.16,1,0.3,1)` som cue-kurva | Krämkanvasen, radie 4/8/12–24, hela skuggsystemet, och overshoot-kurvan `cubic-bezier(0.34,1.3,0.64,1)`, som är oförenlig med damping 1,0 |
| `paper/fold.webp` + `slices/00–10` (pixlar) | Folden bekräftar posten exakt: rad 1 i bläck, rad 2 och 3 i skiffer, samma grad och vikt. 01 är en logotypvägg, 02 och 07 är centrerade halvcirkelsektioner, 08 är en `Series A $34M`-panel, 09 och 10 är avslutet | Att tvåtonsbrytningen ligger på en **semantisk** gräns och inte på en radbrytning. Och avslutets form i 10: sidan slutar på en textrad och en adress | Topplänkraden, den fyllda knappen, trafikljusprickarna (gate 47), de centrerade halvcirklarna, logotypväggen i 01, `$34M`-panelen i 08, och det präglade jätteordmärket bakom footern i 09 och 10 |
| `paper/extract/paper-design-design-language.md` | Motion: springy, scroll-linked, fyra varaktigheter 100–800 ms, ease-out i 32 bruk. Material: flat, saturation 0,226, shadow blur 0 px, 6 gradienter, radie upp till 9999 px | Bekräftelsen att en flat yta med saturation kring 0,2 är det som gör tvåtonsdevicen läsbar | Alla sex gradienter, radie 9999, och `transition: all` som står i dess Common Transitions |
| **`harkcap`** `entry.md` + `design-language.md` | Låter ett enda renderat objekt bära hela auktoriteten med rubriken satt litet mot det, och undanhåller lagets identitet tills pekaren är på plats. Material: shadow profile none, 0 gradienter | **Undanhållandet flyttat från pekaren till berättelsen**, och proportionen objekt stort / typ litet. Och beviset att ett tungt visuellt hero inte behöver ett enda djupknep | 3D-renderingen, talen över glaset, hela laget, `Click to Expand`-navet, och `transition: all` som posten själv använder |
| `harkcap/fold.webp` + `slices/00–11` (pixlar) | 04 är hover-listan: tolv namn i ljusgrått, ett i helsvart, porträtt över listan. 05 och 06 är den bärande formen: **hårlinjerader med rubrik vänster, brödtext i mitten och ett jättenumeral 01/02/03 höger**, på svart. 02 är statbandet, 07–10 är nyhetslistan, 11 är footern | Exakt två saker. **(a)** Hårlinjelistan som kan bära ett helt avsnitt utan ett enda kort, vilket är skillnadsliggarens form. **(b)** Radnumret i marginalen i displaygrad, som är tjänsteliggarens 01–03 | Chipsen, det fyllda blå kortet, den svarta footern, porträtten, glaset, och att numret är serif och jättestort (K4:s radnummer är 11 px mono, eftersom typen viker för produkten) |
| **`mode`** `entry.md` + `design-language.md` | Hägnar in accenten till exakt en komponenttyp, låser serifen till 36 px och uppåt i en enda vikt, delar radien i två roller och bygger djup ur en färgstack i stället för skugga | Inhägnaden, skärpt från komponenttyp till **objekt som finns exakt en gång**, och regeln att tracking skärps med graden. Och varningen i dess Design System Score mot fyra typsnittsfamiljer | Färgstacken, serifen, chartreusen, båda radievärdena, och `Signature move` helt: det är ett kort, och `8.2K` är inte Alunix tal |
| `mode/fold.webp` + `slices/00–10` (pixlar) | Folden är tre överlappande chartreusegula pratbubblor med rubriken i, ett dokumentärt teamfoto, och ett mörkgrönt statkort med stapeldiagram. 03 och 04 är isometriska lagerillustrationer, 06 är ett citatkort med porträtt, 08 är ett bento-rutnät med ikoner, 09 och 10 är footern | **Ingenting av kompositionen.** Posten är i K4 en regelkälla, inte en formkälla | Bubbelformerna, teamfotot, statkortet, stapeldiagrammet, logotypväggen i 06, bento-rutnätet och ikonerna i 08, och den isometriska illustrationen. Hela raden är PRODUCT.md § absences eller TASTE § 5 |
| **`gocanopy`** `entry.md` + `design-language.md` | Ramar in rubriken med två små tracking-öppna monoetiketter, en över med publiken och en under med det tekniska påståendet, så att meningen flankeras av maskinröst i stället för att stöttas av en underrubrik. Motion: en kurva för färg, en annan för transform | Inramningen **roterad 90°**: `Före` vänster, `Efter` höger, så att metadata namnger de två halvorna. Och kurvuppdelningen: cue-opacitet får en bezier, delarens fjäder har ingen bezier alls | Duotonen, skylinen, videon, den klibbiga annonsremsan, pillnavet, och den centrerade rubriken, som split stage förbjuder uttryckligen |
| `gocanopy/fold.webp` + `slices/00–08` (pixlar) | Folden visar inramningen exakt som posten beskriver den, lodrätt. **08 visar något posten inte nämner:** i footern står de två monoetiketterna i stället **vågrätt**, `INTELLIGENCE THAT COMPOUNDS` vänster och `AI-NATIVE FROM DAY ONE` höger, på samma baslinje | Att den vågräta varianten redan finns i källan, alltså är K4:s 90-gradersrotation en läsning av posten och inte en uppfinning ovanpå den. Det är en starkare grund för lånet än entry-texten ensam ger | Duotonen, den neongröna annonsremsan, `Click to play`-kortet, processkorten i 03, och statkorten i 05 |
| **`customer-io`** (wildcard) `entry.md` + `design-language.md` | Iscensätter produktskärmbilden **inne i ett fotograferat rum** för att låna ett livsstilsfotos trovärdighet åt en skärmbild, färgar om enstaka ord i rubriken, och svarar på invändningar i tre små bockar | Exakt en sak, **som avvisning**: postens signaturdrag är att låna trovärdighet. K4 behöver noll lån, eftersom produkten körs i ramen och går att använda. Och varningen mot `meteor` och `border-beam`, som är precis den rörelseklass gaten avvisar | Allt annat. Regnbågsorden, pillknapparna med glödring, bockraden, logotypväggen i 01, chattbubblan i 03 (F-006), ikonkorten i 05, porträttcitaten med procenttal i 07 och 08, och efterlevnadsraden i 09 |

### Vänsterhalvans innehåll och högerhalvan

| Fil | Vad den gör | Vad jag tar | Vad jag lämnar |
|---|---|---|---|
| `sites/before-ai-slop.html` (hela, som kod) | Är kedjans egen antagonist: sticky pill-nav med backdrop-blur, centrerad hero med badge, ett gradientsatt ord, avatarstack, ett div-byggt dashboardkort med SVG-sparkline, sex påhittade ordmärken, tre ikonkort, fyra påhittade tal, centrerad CTA, enradsfooter | **Ingenting formmässigt.** Tre mätvärden: att hela sidan går i Inter (`"Inter": 61`), att den laddar tre externa värdar, och att dess påhittade bevis (`Trusted by 10,000+ teams worldwide`, `10k+`, `99.99%`, `10x`) gör etiketten `En typisk mallsida` till en spärr och inte en bildtext | Varje enskilt drag. Och särskilt frestelsen att karikera den: den skakas inte, faller inte isär, och sidans enda kritik är sex mätta tal |
| `sites/calyx.html` (hela, som kod) | Är högerhalvan: Cardo och PT Mono, elva oklch-värden, noll hexfärger, noll kortformer, fyra Unsplash-fotografier, en typskala 11 → 130 px | De fyra talen liggaren behöver, och kunskapen att filen aldrig redigeras | Dess `reveal`-skript, som sätter `opacity: 0` på varje sektion, rubrik, blockquote, figur och listrad. Det är skälet till att ramen aldrig får scrollas av K4: bara hero-sektionen är avslöjad vid mount |

### Kedjans referenser

| Fil | Vad den gör | Vad jag tar | Vad jag lämnar |
|---|---|---|---|
| `reference-lock.md` | Sätter lockens sju fält, decision ledger med obligatorisk `Memorable detail`-rad, asset-locken, de tre persona-skisserna, och kravet att kategorins fem levande rubriker citeras ordagrant | Alla sju fälten, ledgerformatet, och regeln att media strategy är en **enum** per plats. Och anti-averaging-testerna, särskilt editorial-testet | Det mesta av tier-avsnittet: K4 är inte ett tier-val utan en låst målbild, och lockens roll här är kvalitetsribba snarare än riktningskälla |
| `scroll/devices.md` | Nio devicefamiljer, cue-kontraktet med sina fem regler, playhead-lerpen, lagrade scener, `flow`-defaults, `count`-reglerna, och förbudet att restyla motorns klasser | Cue-kontraktet i sin helhet (särskilt hälsa-formen och att bara sista akten får hålla), `count`-regeln att bara sanna tal räknas, `flow`-defaults 14 px och 620 ms, och regeln att `magnet`, `parallax` och `cue` inte kan dela element | Hela § om lagrade scener och parallaxplan: K4 har noll plan och noll parallax. Och `pan`-avsnittet, som split stage förbjuder |
| `scroll/feel-and-fingerprint.md` | Feeling curve före akterna, en engineered topp, tell-someone-testet, signaturmovets definition, embodiment som krydda, pacing som känsla, och fingerprint-gaten | Att toppen ska ha största span, tystnaden före sig och asset-budgeten. Regeln **en eller två embodiments per sida**, som är varför delaren är sidans enda interaktion. Och att författad tystnad måste stå i BRIEF.md | Trace-tekniken (en ackumulerande spårlinje), dwell-triggad detalj, och velocity-shaping av grain: alla tre skulle ge sidan en andra röst |
| `scroll/pace.md` | `rate = weight / clip_seconds` inom några procent, worldflight-knapparna 0,12 och 0,16, och att damping och vikter fixar olika halvor | Distinktionen, och att en ojämn takt läses som ett fel i sidan. Med **en** akt har K4 ingen rate-spridning alls, vilket är den ena rad i filen som gäller cellen | Hela worldflight-apparaten: inga legs, inga clips, ingen `data-sc-seam`, ingen `data-sc-window` |
| `motion-smoothness.md` | Skiljer de två felen bakom ordet hackigt: värdet stegar mot sidan tappar bilder, med mätdata som visar identisk bildtid och `staircase` 18 mot 0 | Regeln att bespoke rörelse läser `--sc-ps`, mätbaren (`staircase = 0`, `max_step ≤ 3 %`, p95 ≤ 20 ms, båda riktningarna), och varningen att en clip-gräns som stegar syns bättre på en rak lodrät linje än på något annat | Ingenting. Hela filen gäller cellen, eftersom cellens signatur är exakt en clip-gräns på en rak lodrät linje |
| `performance.md` | Budgeten i gate 93, laddningsreglerna, renderingsreglerna och en Never-lista i nio punkter | Hela budgeten, `content-visibility` på a3–a6, fontreglerna, och **Never-raden om iframes monterade vid load**, som är den enda punkt där jag rättar prestandaplanen | Klippbudgeten (K4 har ingen video) och `srcset`-reglerna för bilder under 60 % av viewporten (K4:s två bilder är full-bleed) |
| `lift.md` | Sekvensen som ersätter "kör polish": sju steg, reviewerkontraktet i fem sektioner, försoningsordningen, och stoppvillkoret | Reviewerkontraktets fem sektioner och ordningen tillgänglighet > prestanda > användbarhet > brief > personas. Och stoppvillkoret: kritikern måste skriva **slår** för varje låst referens | Passen som bara körs på ett fynd (`bolder`, `quieter`, `colorize`), eftersom inget fynd finns i R1 |
| `apple-design/SKILL.md` §§ 2–6, 10, 11 | Direkt manipulation med `setPointerCapture` och grabOffset, avbrytbarhet som viktigaste princip, fjädrar i damping och response i stället för mass och stiffness, velocity-handoff, och momentumprojektion | §§ 2, 3, 4 och 5 i sin helhet: grabOffset, alltid animera från presentationsvärdet, damping 1,0 och response 0,35 s, och velocity vid `pointerup`. Plus § 10:s hysteres om 10 px | § 6 momentumprojektion (det finns inga snap-punkter att projicera mot), § 7 symmetriska vägar (delaren har en väg), och § 9 rubber-banding (delarens gränser är 0 och 1 och den ska stanna där, inte studsa) |

### Registret och cellens eget underlag

| Fil | Vad den gör | Vad jag tar | Vad jag lämnar |
|---|---|---|---|
| `wiki/projects/_index/design-fingerprints.md` (alla 141 rader) | 36 byggrader i sex dimensioner plus två läsanvisningar om vad som redan är förbrukat | Verifieringen av § (4), listan över förbrukade nav- och heromönster, och regeln att rader är append-only | Ingenting. Se min kontroll i § Fingerprint |
| `tests/alunix-r8/PRODUCT.md` | Beviskassan, den låsta copyn, § absences och de fem produktprinciperna | Hela § absences som spärr, princip 1 (beviset ska gå att använda) som skäl att Calyx förblir live, och princip 2 som skäl att liggarens tal måste kunna spåras till ett kommando | Ingenting, men princip 2 kräver en ledgerrad för att inte läsas som ett förbud mot liggaren |
| `tests/alunix-r8/concepts-K4.md` (hela, 910 rader) | Arkitektens målbildsgrind: urvalet med poäng, mätningen ordagrant, troplistan, nio skärmar, 36 fingerprint-rader, rörelsen, färg och typ, vad referenserna gör | Allt utom de fyra punkter jag rättar i decision ledger. Särskilt § Mätning, vars två `measure.py`-utfall jag återanvänder utan att köra om dem, eftersom filerna är oförändrade sedan mätningen | Ingenting medvetet. Fyra påståenden rättas med belägg och står som egna ledgerrader |
| `tests/alunix-r8/runs/K4/assets/ASSETS.md` + `credits.json` | Fyra medieplatser, ingen av dem en generate-prompt; kommandoraderna för de sex skärmbilderna; och beläggen för att de ärvda bilderna inte räcker | Asset-lockarna ordagrant, och `generated_material.present: false` som cellens premiss och inte som en begränsning | Inget. Byggaren rör inga assetfiler, och de sex bilderna står som `[needs: shot]` hos lead |

## Byggarens öppna frågor, R1

Fem. Ingen av dem blockerar R2, och varje rad har ett antagande som gäller tills svar samt ett
nästa konkret steg, så att rundan kan fortsätta utan att någon väntar.

| # | Fråga | Antagande tills svar | Nästa konkreta steg om svaret går emot antagandet |
|---|---|---|---|
| **B1** | Lead-instruktionen pekar `select.py` på `BRIEF.md`, arkitekten pekade den på `BRIEF-draft.md`, och bara den andra kan poängsättas. Ska instruktionens sökväg rättas i r9, eller ska ett skelett förses med de fem strukturfälten så att båda vägarna ger samma rad? | Arkitektens rad gäller, båda körningarna står ordagrant i § catalogue-select, och min ledger bär rätt slugar sist | Ingen åtgärd i K4. Frågan gäller harnesset, inte cellen, och ligger bredvid Q11 |
| **B2** | Prestandaplanen kallar vänsterramen fri från externa resurser. Den laddar tre värdar, och Calyx laddar samma tre, alltså två Tailwind-kompilatorer i samma dokument. Godtas det, eller ska vänsterramen degraderas till skärmbild redan innan `perf_probe` mätt något? | Båda ramarna förblir levande tills talet är mätt i R2, och beslutsregeln i § Prestandaplan avgör därefter | Vänsterramen byts mot `demo-*.webp`. Den finns inte i assetlistan i dag, alltså behöver lead skjuta en `before-ai-slop`-bild vid 1440 och 390. Jag begär den inte nu, eftersom talet kan hålla |
| **B3** | `performance.md` § 6 förbjuder en ram monterad vid load; prestandaplanen säger att vänsterramen monteras eagerly *eftersom den är folden*. Jag har löst det med IntersectionObserver plus `requestIdleCallback` efter first paint. Räcker det, eller ska folden visa en skärmbild som byts mot ramen när den laddat? | Min lösning gäller, och kontrollen är att `perf_probe` namnger rubriken som LCP-element | En `<img>` i samma box som byts mot ramen vid `load`. Det kostar en extra medieplats och en asset-lock, och det bryter mot att bara clip-gränsen får röra sig, alltså vill jag undvika det |
| **B4** | Q12 är fortfarande obesvarad. Om Anton säger att *ingen* visad ram får tonas, faller mallsidans mättnadsfall. | Arkitektens antagande gäller: regeln träffar de tre Alunix-exempelsajterna, inte antagonisten | Degraderingen begränsas till rubrikens före-halva, som ligger i K4:s eget lager. Signaturen överlever, eftersom `wght` 500 → 200 och tracking 0 → 0,06 em är den del av degraderingen som bär påståendet. En ledgerrad räcker, ingen omskjutning, ingen ny asset |
| **B5** | De sex demo-skärmbilderna står som `[needs: shot]` hos lead och behövs först i R3 (a3). R2 bygger fold och signaturakt, som inte använder dem. | R2 körs utan dem, och a3 markeras `[needs asset: demo-horai-1440/390, demo-hyperborea-1440/390]` i markupen | Om bilderna dröjer till R3 byggs a3 med rätt boxstorlek och `contain-intrinsic-size` satt från måtten i `ASSETS.md`, så att inflyttningen inte flyttar något. Ingen platshållarbild skrivs |

### Tillagt i R2

| # | Fråga | Antagande tills svar | Nästa konkreta steg om svaret går emot antagandet |
|---|---|---|---|
| **B6** | **Rörelsebaren faller och briefens egen åtgärd namnger fel ram.** Mätt vid 4× CPU: båda ramarna live 66,7 ms p95; **vänsterramen borttagen 66,6 ms**, alltså ingen effekt; **högerramen (Calyx) borttagen 33,4 ms**. Överföringsregeln utlöses inte (1 690 kB mot taket 2 500 kB), och min egen animation kostar ingenting mätbart (identisk p95 med klippningen helt borttagen). Ska Calyx degraderas till en skärmbild för att nå baren? | **Nej, ingendera ramen degraderas.** Att degradera vänsterramen ger noll. Att degradera Calyx skulle offra PRODUCT.md princip 1, beviset ska gå att använda, på en sida vars hela argument är att beviset är verkligt och körbart. Båda förblir levande och talet rapporteras | Om lead väljer talet framför principen: byt **högerramen** mot `demo-calyx-1440.webp` / `demo-calyx-390.webp`, som redan finns vendorade, och skriv om briefens beslutsregel så att den namnger den tunga ramen i stället för den vänstra. Det är en enradsändring i `index.html` plus en ny rad i låset, och det bör i så fall också ändra § Prestandaplan, som i dag pekar på fel ram |
| **B7** | Två av de sex demo-skärmbilderna överskrider `ASSETS.md`:s egna tak: `demo-calyx-1440.webp` 206 966 B mot 150 kB, `demo-calyx-390.webp` 190 200 B mot 120 kB. Båda är reservfiler och används inte av R2 | Talen noteras, filerna rörs inte. Byggaren rör aldrig assetfiler (F-009) | Lead kör om konverteringen med `quality 76` enligt `ASSETS.md` § 3. Blir aktuellt först om B6 besvaras så att en reservbild faktiskt monteras |

**Vad som inte är en öppen fråga.** Rörelsens reservläge (F-011: det finns inget), typsnitten
(Switzer + Reddit Mono, mekaniskt kontrollerade som obrukade), referensvalet (arkitektens rad),
och genereringen (noll material, och skälet är principiellt före praktiskt).
