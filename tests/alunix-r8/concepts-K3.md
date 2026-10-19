# Alunix r8 — målbildsgrind, cell K3

Skriven av arkitekten 2026-09-09. Denna fil äger **bara** K3. Lead slår ihop V3c, K3 och K4
till `concepts.md`; den här filen skrivs aldrig in i den av mig.

---

## catalogue-select

`python scripts/catalogue/sweep_raw.py` kördes om av mig innan urvalet:

```
sweep: rent - varje kalla under raw/ och processed/ har en post (0 ignorerade).
EXIT=0
```

`python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K3/BRIEF-draft.md --k 4 --wildcard --explain`,
hela utdatan ordagrant:

```
Brief: tests\alunix-r8\runs\K3\BRIEF-draft.md  ->  5 poster

   13  squarespace              modern clean           chaptered editorial
       +3 register | +3 grammatik | +2 category2 | +1 mode | +2 auktoritet | +2 fritext (accent, surface)
   11  aevi-wellness            modern clean           chaptered editorial
       +3 register | +3 grammatik | +2 category2 | +1 mode | +2 fritext (accent, editorial)
   10  beautiful                warm photographic      chaptered editorial
       +3 grammatik | +2 category2 | +1 mode | +4 fritext (accent, category, mono, per)
   10  insign                   modern clean           chaptered editorial
       +3 register | +3 grammatik | +2 category | +1 mode | +1 fritext (per)
   10  mode                     modern clean           split stage
       +3 register | +2 category2 | +1 mode | +2 auktoritet | +2 fritext (accent, mode) | wildcard: utanfor kategorin

Mediastrategi ur posternas egna falt (Photo search) - locken ska inte gissa:
  - squarespace: Unsplash first, Pexels second. - "candid documentary portrait natural light" - "small business owner at work authentic" - "creative studio c
  - aevi-wellness: Unsplash first, Pexels second. - "skincare bottles overlapping flat lay natural light" - "dropper bottle apothecary product close up" - "min
  - beautiful: Unsplash first, Pexels second. - "kitchen countertop natural light warm styling" - "ceramic kitchenware wooden counter lifestyle" - "breakfa
  - insign: Unsplash first, Pexels second. - "tablet mockup website design display" - "phone mockup app interface hand" - "branded delivery van signage"
  - mode: Unsplash first, Pexels second. - "team collaborating desk candid natural light" - "coworkers reviewing screen office documentary" - "data an

catalogue-select skriven: squarespace, aevi-wellness, beautiful, insign, mode  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Avvikelse mot målbildens förväntan, och varför raden ändå gäller.** Planens § 7.5 gissade
`caractere-bois`, `hyperborea`, `wild`, `garden-eight`, `tidvatten`. Ingen av dem föll ut.
Orsakerna är mekaniska och kontrollerade i `index.json`:

- `hyperborea` och `tidvatten` står i `select.py`s `OWN_SITES` och poängsätts negativt —
  de är kedjans egen output, inte referens. Det är avsiktligt och rätt.
- `caractere-bois` är `editorial print` + `gallery/catalog`; målbilden låser själv
  `modern clean` + `chaptered editorial`, så posten får noll på de två tyngsta axlarna.
- `garden-eight` är `editorial print` + `typographic poster` — samma sak.
- `wild` är `modern clean` + `chaptered editorial` + `portfolio` och ligger strax under
  strecket (9 + fritext mot `insign`s 10). Den föll på ett poäng, inte på en princip.

`catalogue-first.md` § 5 gör skriptets rad till den som referensgolvet läser, och § 7 säger
att en tom eller svag träff ska mötas med bredare fråga, inte med minnesarbete. Träffen är
varken tom eller svag. **De fem valda posterna är alltså cellens låsta referenser.** Jag har
läst `caractere-bois` och `wild` som *icke-låsta* jämförelser är tillåtna (r7-promptens rad
"Katalogens övriga poster behöver du inte läsa, men inget förbjuder det") — men de får ingen
rad i reference-locken och ingen rad i "vad cellen måste slå", eftersom en referens som inte
är vald inte får styra bygget. Frågan om planens förväntningslista ska rättas ligger som Q8
i `QUESTIONS.md`.

---

## Lästa referenser

Tre rader per fil: vad den gör · vad jag tar · vad jag lämnar.

### squarespace (primär)

- `entry.md` (hela, inkl. § Motion och § Reference lock) — deklarerar "0 % colourfulness by
  design": sex tokens, alla svarta, vita eller grå, och en uttalad regel att kromatisk färg
  aldrig introduceras på marknadsföringsytan; all mättnad reserveras för användarens egna
  sajter. Clarkson kör hela systemet i vikt 300 vid 60–70 px med −0,05 till −0,06 em.
  **Tar:** reservationen som *struktur* — den enda kromatiska färgen på arket är den ena
  blå, och det enda mättade i bild är kundsajten inne i den ritade öppningen.
  **Lämnar:** achromatisk palett (K3:s papper och bläck är kalla men kromatiska), 0 px-radie
  på knappar (K3 har inga knappar), dokumentärfoto som hero.
- `fold.webp` — fullbleed dokumentärvideo (en frisör), vikt 300-rubrik centrerad i bilden,
  vit skarp knapp, och tre kundsajter som lutande plattor längs nederkanten.
  **Tar:** att kundsajterna är det enda färgstarka i vyn. **Lämnar:** centrerad hero, lutande
  plattor (kortgest), fotot som grund.
- `slices/00–08.webp` — svarta och vita band som växlar utan grå övergång; ett svart
  statband (14M+ / $36B+ / 200+) i vikt 300 vid ~80 px med små versaletiketter under;
  pill-flikar som filter; en accordion med hårlinjer och `+`-tecken; en helsvart footer.
  **Tar:** statbandets form (displaygrad, liten etikett, linjal under) och hårlinje-accordion
  som strukturspråk. **Lämnar:** siffrornas *innehåll* (Alunix har inga sådana tal —
  TASTE § 4.9), pill-flikarna, avatarstacken, partikelsfären i avslutet.
- `extract/squarespace-com-design-language.md` — Motion Language: feel "mixed",
  scroll-linked ja; fem varaktigheter 100–750 ms; två egna kurvor dominerar (216 använd\
  ningar), och en `steps(1, start)` förekommer 49 gånger, alltså en diskret, icke-inter\
  polerad tickning. Material Language: `flat`, avg saturation 0,126, max radie 100 px.
  **Tar:** `steps()`-tickningen som idé för måttsiffrornas uppräkning — en måttsiffra ska
  landa på ett heltal, inte glida. **Lämnar:** de nio gradienterna, de fem box-shadows,
  radie 30/50/100 px.

### insign (sekundär, samma kategori och samma land)

- `entry.md` — svensk fullservicebyrå: tre tjänster som tre helbreda, fullmättade färgband
  (chartreuse, lavendel, orange) så att paletten *är* navigationen; allt utanför banden
  hålls vitt eller nästan svart; bevisen varieras i format (siffror, ansikten, datum).
  **Tar:** principen att navigationen bärs av ett enda konsekvent system som läses före
  texten. **Lämnar:** att systemet är färg (K3 navigerar med ritade symboler), och hela
  bevisapparaten — betygschip, 180+ omdömen, teamgrid, logotypvägg: Alunix har inget av det
  och får inte hitta på det (PRODUCT.md § absences).
- `fold.webp` + `slices/00–07.webp` — vit hero med serif-logotyp och en grotesk rubrik i två
  rader, sedan en mosaikremsa av kundarbeten, tre färgband med varsin liten enhetsbild,
  projektarkiv, ett mörkt statband (5.0/5.0 · 180+ · 2002) över ett kontorsfoto, sex svartvita
  porträtt, nyhetsremsa, mörk kontaktsektion med fyra pill-knappar.
  **Tar:** att varje tjänst får exakt *en* konkret bild av en verklig leverans, aldrig en ikon.
  **Lämnar:** färgbanden, pillformerna, porträttrutnätet, betygschipet, logotypremsan, och
  rubriken som bryts mitt i ordet ("Webbdesig / n") — posten flaggar det själv.
- `extract/insign-se-design-language.md` — Motion: feel "springy", `ease` på 121 ställen,
  en enda overshoot-kurva `cubic-bezier(0.68,-0.55,0.265,1.55)`, plus `fadeIn`,
  `ball-scale-multiple` och `dipi_fade` — alltså stock-chrome ur en WordPress-byggare, inte
  ett författat system. Brand Voice: neutral ton, tredje person.
  **Tar:** varningen — en sida vars rörelse består av bibliotekets keyframes läser som mall.
  Varje rörelse i K3 är författad och namngiven i device-tabellen. **Lämnar:** overshoot
  helt (fjädring hör inte hemma på ett ritark), och tredje person (Alunix röst är vi-form).

### aevi-wellness (sekundär)

- `entry.md` — nästan akromatiskt system med exakt en kromatisk accent reserverad för en enda
  knapp; *varje* textstorlek från 10 px bildtext till 54 px display kör vikt 300, så hierarkin
  bärs av storlek och radavstånd i stället för vikt; elevation är förbjuden rakt av, djupet
  kommer från växlande band och hårlinjer i bläck eller pulverblått.
  **Tar:** hårlinjen som *enda* strukturmedel och det uttryckliga skuggförbudet.
  **Lämnar:** enviktssystemet (K3 behöver två vikter för att skilja utrop från måttsiffra),
  pill-knappen, och den fullbleed produktfotografin som hela systemet vilar på.
- `fold.webp` — ordmärket AEVI satt som ett översiktligt genomskinligt lager ovanpå
  produktfotot, versal underrubrik i vikt 300, en tunn outlinad pill, och en pulverblå
  presslogorad direkt under folden. **Tar:** ingenting av kompositionen. **Lämnar:** ordmärket
  som vattenstämpel, presslogoraden (Alunix har inga presslogotyper), fotot som grund.
- Posten har varken `slices/` eller `extract/` (`extract: none`, `origin: refero`), vilket
  betyder att dess § Motion är **inferred**, inte uppmätt. Jag behandlar den därför som en
  yt- och strukturkälla, aldrig som en rörelsekälla.

### beautiful (sekundär)

- `entry.md` — gräddlinne som canvas överallt i stället för vitt; korallen ransonerad till en
  bokstavlig regel, "ett korallmoment per viewport", vilket är granskningsbart; radie har
  exakt två värden (999 px = klickbart, 0 px = innehåll) och 1 px svart hårlinje ersätter
  både ram och skugga; tracking *öppnar* när graden växer, tvärtemot konventionen.
  **Tar:** den granskningsbara accentregeln, ordagrant överförd: ett blått moment per
  viewport, och det momentet är alltid en sann måttsiffra. **Lämnar:** cream (K3:s papper är
  kallt, AB09-lärdomen och lead-låset), pillformerna, den centrerade logotypen, och den
  öppnande trackingen (måttsatt typografi vill ha stram tracking).
- `fold.webp` — centrerad serif-logotyp flankerad av svartkantade nav-piller, asymmetrisk
  hero 60/40 med produktfoto till vänster och en korallpill till höger, allt på gräddlinne.
  **Tar:** ingenting av kompositionen. **Lämnar:** hela pillspråket och produktfotot.
- Posten saknar `slices/` och `extract/`. Samma behandling som aevi: yta och regel, inte rörelse.

### mode (wildcard, `split stage`, utanför kategorin)

- `entry.md` — inhägnar accenten till exakt en komponenttyp ("the only filled button color in
  the system"), och bygger djup ur en färgstack sage → forest → chartreuse i stället för
  skugga; serifen är låst till 36 px och uppåt i en enda vikt, med tracking som skärps med
  graden. **Tar:** inhägnadsprincipen, skärpt ett steg: K3 inhägnar accenten till en
  *innehållstyp* (en sann uppmätt siffra), inte till en komponent — en komponentregel kan
  drifta när en ny komponent uppstår, en innehållsregel kan inte. **Lämnar:** färgstacken,
  serifen, 16 px-radien, och hela chartreusen.
- `fold.webp` + `slices/00–10.webp` — mörkgrön grund, rubriken satt i chartreusegula
  pratbubbleformer som överlappar ett dokumentärt teamfoto, ett mörkt statkort ("8.2K"), en
  isometrisk lagerillustration med färgkodad teckenförklaring, logotypvägg, citatkort med
  porträtt, och en footer där ordmärket sätts i jättegrad.
  **Tar:** exakt en sak — den färgkodade teckenförklaringen bredvid lagerillustrationen är
  ett *legend*-mönster som gör bilden läsbar utan bildtext. K3:s marginallegend är samma idé,
  ritad i stället för färgad. **Lämnar:** allt annat: bubbelformerna, statkortet, teamfotot,
  logotypväggen, citatkortet.
- `extract/mode-com-design-language.md` — Motion: feel "springy", `ease` 102 gånger, en
  overshoot `cubic-bezier(0.75,0,0.29,1.01)`, en `scroll`-keyframe (translateX 0 → −100 %,
  alltså en marquee). Design System Score 83/100, med "4 font families" och "75 % av CSS
  oanvänd" som egna anmärkningar. **Tar:** varningen mot fyra typsnittsfamiljer — K3 kör två.
  **Lämnar:** overshoot, marquee, och de två box-shadows.

### Anti-referens: `sites/before-ai-slop.html`

Läst som kod, 155 rader. Vad den gör: sticky flytande pill-nav med `backdrop-blur`; centrerad
hero med badge-rad (`inline-flex … rounded-full` med en pulserande prick), ett gradient-satt
ord mitt i rubriken (`.grad-text`, `#1E40AF → #6366F1`), två pill-CTA, en avatarstack av fyra
gradientcirklar; till höger ett **div-byggt "Dashboard preview"-kort** med fyra påhittade
stat-tiles (51 %, 16 %, 17, 1,8 %) och en SVG-sparkline; sedan "Trusted by teams at" med sex
påhittade ordmärken, tre likadana ikonkort med emoji i gradientrutor, ett fyrfältsstatband,
en centrerad CTA och en enradsfooter.

**Vad K3 gör i stället, punkt för punkt:** ingen topprad alls (navigationen är en ritad legend
i marginalen) · ingen badge, ingen pill, ingen gradient, ingen avatar · **ingen låtsasyta
någonstans** — det enda "gränssnitt" som syns på sidan är en riktig Alunix-exempelsajt i en
`<iframe>` på samma origin, och ritningen är uttryckligen inte en UI-mock: den har konturer,
måttlinjer och utrop, aldrig en låtsasknapp, aldrig en låtsasetikett, aldrig lorem · inga
påhittade tal (varje siffra på sidan är 320, 768, 1440, `7 rem`, `96 px`, `16:9`, 26 900,
38 900 eller `Pris vid förfrågan`) · ingen logotypvägg och inga kunder utöver de tre
exempelsajterna · tre tjänster som hårlinjerader i en liggare, aldrig tre kort · tre paket som
en stycklista i en ritad ram, aldrig tre priskort med "populärast" · avslutet är ett
specifikationsblad som blir stilla, aldrig en centrerad CTA som rinner ut i en copyrightrad.

---

## K3 · "Ritningen"

### (1) Auktoritet och vad som viker

**Auktoriteten är ytan** — kallt ritpapper och ett bläck (TASTE § 1 rad 3): allt djup på sidan
kommer av hårlinjer, ton på ton och överlapp mellan ritade lager, aldrig av kort eller skuggor.

**Vad viker, en mening var.** *Typen* viker: den är medelstor, max ~72 px, i två vikter, och
den enda typ som får displaygrad är måttsiffrorna som hör till ritningen. *Bilden* viker till
noll: det finns inga fotografier på sidan, och de tre exempelsajterna visas levande *inuti*
ritade öppningar, aldrig fullbleed och aldrig som skärmbildsplattor ovanpå något. *Färgen*
viker: ett papper, ett bläck och exakt en kromatisk accent som gör exakt en sak. *Rörelsen*
viker överallt utom i signaturakten a1, där den enligt TASTE § 4.8:s r6-precisering är
auktoriteten och typ och innehåll i sin tur viker för den.

### (2) Troplistan

TASTE § 5 punkt för punkt, plus F-006 och gate 47/79.

| Trop | Status i K3 |
|---|---|
| Ikongrid | **Frånvarande.** Tjänsterna 01–03 är hårlinjerader i en liggare; ingen ikon finns i bygget. |
| Gradient-mesh | **Frånvarande.** Grunden är en plan oklch-färg plus en procedurell papperstextur utan färgövergång; ingen `linear-gradient`, ingen `radial-gradient`, ingen mesh. |
| Glasmorfism | **Frånvarande.** Noll `backdrop-filter`, noll halvgenomskinliga paneler. Uttryckligen dödad av F-006. |
| Centrerad hero med badge-rad | **Frånvarande.** Heron är vänsterställd på ett ark med titelblock i övre vänstra hörnet; ingen badge, ingen pill, ingen underrad med prickar. |
| Lila/indigo-accent | **Frånvarande.** Enda accenten är `#1E5E9C`, hue ≈ 252 — Alunix eget Tier 1-bevis, inte en indigoglöd. |
| Skuggade 8 px-kort | **Frånvarande.** Noll `box-shadow` i hela filen, och radien är 0 överallt utom den ritade ramens hörnradier som är 0 de också. Ramar är ritade linjer, inte kort. |
| Stockfoto av leende team | **Frånvarande.** Noll fotografier, noll människor, noll ansikten (Hyperborea-precedensen plus `generation.md` § 8). |
| "h1 48 / h2 32"-skala | **Frånvarande.** Skalan är 5×+ enligt TASTE § 2.4: display 72 px (måttsiffror) mot brödtext 15 px; mellannivån 32 px existerar inte, mellanrubriker är utrop i 12 px mono med tracking. |
| Dekorativa blobbar | **Frånvarande.** Varje sluten form på arket är en kontur som betyder något (en sektion, en öppning, en marginal); inget ritas som dekoration. |
| Tre lika feature-kort | **Frånvarande.** Tre tjänster = tre rader i en liggare med olika radlängd; tre paket = tre rader i en stycklista med ledarpunkter. Aldrig tre lådor bredvid varandra. |
| **F-006** — glaskort, dashboard-över-foto, "live"-punkter, telemetri-chrome | **Frånvarande.** Inget glas, ingen dashboard, ingen live-prick, ingen procentavläsning, ingen statuschip. Cellen har ingen `Live surface`-grammatik och får inte låna dess chrome. |
| **Gate 47** — omritat chrome (webbläsarfält, telefonram) | **Frånvarande.** Exempelsajterna visas i en `<iframe>` utan ritad webbläsarram, utan flikrad, utan URL-fält och utan telefonbezel. Den ritade konturen runt en sajt är en **måttsatt öppning i ritningen**, inte en enhetsram: den bär måttlinjer och ett utrop, den bär aldrig en trafikljusprick eller en adressrad. |
| **Gate 79** — div-byggd låtsas-UI | **Frånvarande, och detta är cellens känsligaste punkt.** Regeln som gäller i R2/R3: **ritningen får rita form, aldrig innehåll.** Tillåtet i SVG: konturer, måttlinjer med pilspetsar, hjälplinjer, snittmarkeringar, skrafferingar och utrop som anger ett mått eller ett namn på en zon (`fold`, `marginal`, `spalt`). Förbjudet i SVG: rektanglar som föreställer knappar, textblock som föreställer text (ingen lorem, inga grå staplar som ska "vara" text), ingen navrad, inget formulär, ingen graf, ingen sparkline, ingen siffra som inte är ett verkligt mått. **Kontrollen:** varje `<rect>`/`<path>` i ritningen ska kunna namnges som "kontur", "måttlinje", "hjälplinje", "skraffering" eller "utrop" — kan den inte det ska den bort. Arkitektens F-007-kontroll i runda 2 läser folden som pixlar och prickar av detta bild för bild. |

### (3) Ett displayelement per skärm (1440 × 900)

Elva skärmar. Ett displayelement var, namngivet. Allt annat i vyn går ner ett steg i grad,
vikt eller mättnad (F-003).

| # | Akt / p | Displayelementet | Vad som viker i samma vy |
|---|---|---|---|
| s1 | a1, p 0–0,12 | **Titelblocket** i arkets övre vänstra hörn (`ALUNIX` · `SEKTION A–A` · `SKALA 1:1`), satt i mono | Arket är annars tomt: författad tystnad före toppen |
| s2 | a1, p 0,12–0,55 | **Sektionskonturen** som ritar sig, en enda linje åt gången | Titelblocket faller till 12 px mono; inga utrop ännu |
| s3 | a1, p 0,55–0,78 | **Måttkedjan** `320 · 768 · 1440` i displaygrad, i blått | Konturen står stilla och går ner till hårlinjevikt |
| s4 | a1, p 0,78–1,0 | **Den fyllda öppningen**: Calyx fold monterad innanför konturen, bläcket kvar som ram | Måttsiffrorna faller till 12 px mono i marginalen |
| s5 | a2 | **Kapitelrubriken** `VI BYGGER ERT VARUMÄRKE.` | Legenden i marginalen dämpas till hårlinje |
| s6 | a3 plate 1 | **Calyx-platen**: ritad ram, hela sidan levande innanför | Rubrikraden ovanför är 12 px mono-etikett |
| s7 | a3 plate 2 | **Hōrai-platen** | Samma |
| s8 | a3 plate 3 | **Hyperborea-platen** | Samma |
| s9 | a4 | **Tjänstenamnen** `Design` / `Utveckling` / `System`, ett per rad, radhöjd `96 px` utropad i marginalen | Underraderna 15 px, radnumren 01–03 i 12 px mono |
| s10 | a5 | **Priskolumnen** `26 900` / `38 900` / `Pris vid förfrågan`, i bläck, inte i blått | Paketraderna 15 px med ledarpunkter |
| s11 | a6 | **`Alla har rätt till bra design.`** innanför den ritade ramen | `kontakt@alunix.se` som 15 px mailto under raden |

### (4) Fingerprint

**Cellens egen rad**, i registrets sex dimensioner:

| Dimension | K3 |
|---|---|
| Grammatik | Chaptered editorial |
| Nav | Ritad teckenförklaring i vänstermarginalen, sticky, ingen topprad alls: fem rader med symbolprov (hårlinje, måttpil, skraffering) plus kapitelnamn, och en ledarlinje som *ritas* från den aktiva raden ut till kapitlets egen kontur |
| Hero-device | En måttsatt sektionsritning av en webbsida i inline-SVG som ritar sig själv ur `stroke-dashoffset` drivet av `--sc-ps` i en pinnad akt, span 2,4; måttsiffrorna räknas upp till sanna värden; akten slutar med att Calyx fold maskas in i den öppning bläcket just ritat |
| Aktform | 6 akter, ~13 vh: `pin` 2,4 → `kinetic` lines → `reveal` ×3 → `flow`+`in` → `count` → `reveal` (avslut). Noll `scrub`, noll `drift`, noll `pan`, noll pekar-devices |
| Avslut | Ett specifikationsblad på samma kalla papper: paketen som stycklista med ledarpunkter och sanna priser, manifestraden och en mailto, allt inuti en ritad ram vars linjer dras in sist; ingen inversion, sidan slutar stilla |
| Signatur | *Ritningen blir sidan*: konturen ritas, den riktiga kundsidan maskas in i öppningen konturen skapat, bläcket står kvar som ram |

**Gaten mot alla 36 byggrader i registret.** `≠` = skiljer sig, `=` = delad. Summan räknar
antal `≠` av sex. Kravet är ≥ 4/6 mot **varje** rad.

| registerrad | grammatik ≠? | nav ≠? | hero ≠? | aktform ≠? | avslut ≠? | signatur ≠? | summa |
|---|---|---|---|---|---|---|---|
| Calyx | `=` båda chaptered editorial | ≠ marginallegend utan topprad vs statiskt border-b-huvud i 3 kolumner | ≠ självritande SVG-sektion vs fullbleed botaniskt foto med scrim | ≠ 6 motorakter med pin 2,4 vs 8 handrullade sektioner med fotoduo och immersion | ≠ ritad specifikation på papper vs mörkinverterad mailto i jättekursiv | ≠ ritningen blir sidan vs ingen (bara IO-fade) | **5/6** |
| Hōrai | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad bar som mörkblurrar | ≠ ritning vs fullbleed JS-parallaxfoto med jätteordmärke | ≠ pin+kinetic+reveal+flow+count vs scrubbat citatkapitel | ≠ specifikation vs mörk sektion med book.horai.se i jättegrad | ≠ vs bell-curve-scrubbat citat | **6/6** |
| Hyperborea | `=` båda chaptered editorial | ≠ marginallegend, ingen topprad vs sticky header under edition strip med amber CTA-pill | ≠ måttsatt ritning som ritar sig vs statiskt lagrat sol- och skyline-SVG | ≠ motordriven pin 2,4 + count vs 8 sektioner, marquee, ingen motor | ≠ specifikation i ritad ram vs mörk kolofon "write us a letter" | ≠ vs ingen (sol-diskarna är ett system, inte en interaktion) | **5/6** |
| Tidvatten | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad bar med "Bli medlem"-länk | ≠ ritning vs fullbleed havsfoto med ordmärket satt över hela ramen | ≠ 6 akter utan scrub vs 7 sektioner med pinnat gradscrub | ≠ specifikation på papper vs mörk inverterad mailto i jättegrad | ≠ vs två temperatursiffror som konvergerar | **6/6** |
| Vintergatan | `=` båda chaptered editorial | ≠ marginallegend vs statiskt huvud under edition strip, centrerat ordmärke | ≠ ritning vs typ satt direkt i fotografiet | ≠ 6 akter, ~13 vh vs 11 sektioner med pinnad ordavslöjning | ≠ specifikation vs mörk sektion med kursiv mailto och öppettider | ≠ vs tre ord som förgylls i sekvens | **5/6** |
| Vinterspelen | `=` chaptered editorial (gallery-inflekterad, men samma familj) | ≠ marginallegend vs sticky header med ljuslågemärke och biljettknapp | ≠ ritning vs delat anslag med en inramad målning | ≠ 6 akter utan scenbyte vs 10 sektioner med pinnat kulissbyte | ≠ specifikation i ritad ram vs papperssektion "resan" som matar en mörk 3-kolumnsfooter | ≠ vs sex kulissremsor i vågrörelse | **6/6** |
| before-ai-slop | ≠ chaptered editorial vs ingen av de åtta | ≠ marginallegend vs sticky flytande pill med backdrop-blur | ≠ ritning vs centrerad split med badge, gradientord och div-byggt dashboardkort | ≠ 6 koreograferade akter vs 7 statiska sektioner utan en enda reveal | ≠ specifikation som blir stilla vs centrerad CTA och enradsfooter | ≠ vs ingen alls | **6/6** |
| r1 K1 Svart scen och vit sal | ≠ chaptered editorial vs rhythmic cutlist | ≠ marginallegend vs minimal fixerad toppremsa med ordmärke och mailto | ≠ ritning på kallt papper vs mörk scen med en ljuspöl i fotot | ≠ 6 motorakter vs 4 hårda klipp utan motor | ≠ specifikation vs vit sal med mailto i displaygrad | ≠ vs tre demorutor som lyfter med underglöd | **6/6** |
| r1 K2 Tjänsteledger | ≠ chaptered editorial vs split stage | ≠ marginallegend vs sticky vänsterskena med roterat ordmärke | ≠ ritning vs vitt papper med jättefråga i grotesk och en solid ink-knapp | ≠ 6 akter vs 3 sektioner med fast vänsterspalt | ≠ ritad ram vs mörkt band med systemtexturlinje och tre färgprickar | ≠ vs kapitelfärg som fördjupas via color-mix | **6/6** |
| r1 K3 Instrument | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs kickerremsa utan nav | ≠ ritning vs displaypåstående på onyx med ett blått handlingsord | ≠ 6 akter med pin vs 5 sektioner på en värdestegsgrund | ≠ specifikationsblad vs en enda påståenderad | ≠ vs siffror som räknar upp med linjal under | **6/6** |
| r1 K4 Journal | `=` båda chaptered editorial | ≠ marginallegend med symbolprov vs enkel toppkickerrad med ordmärke och mailto | ≠ självritande måttritning vs vikt-300-serifrubrik med en atmosfärsplate bredvid | ≠ 6 motorakter, ~13 vh vs 4 handrullade romerska kapitel | ≠ stycklista med sanna priser i ritad ram vs tryckt kolofon som krediterar typsnitt, foto och person | ≠ vs `NN / 03`-räknare på varje plate | **5/6** |
| r1 K5 Affisch | ≠ chaptered editorial vs gallery/catalog | ≠ marginallegend vs textnav i foldens underkant | ≠ ritning vs ordmärket i viewportbredd på en flat färg | ≠ 6 akter vs 3 numrerade helbreda plates | ≠ specifikationsblad vs kontakt som en enda rad | ≠ vs ordmärket som fast bakgrundslager | **6/6** |
| r1 K6 Kortlek | ≠ chaptered editorial vs live surface | ≠ marginallegend vs fixerad flytande pill | ≠ ritning vs solfjäder av tre skärmbilder som foldens huvudobjekt | ≠ 6 akter vs 4 sektioner i drift-parallaxfamiljen | ≠ ritad ram vs ingen egen avslutsform alls | ≠ vs kortleken som blandas om på scroll | **6/6** |
| r2 R1 Squarespace scen | ≠ chaptered editorial vs rhythmic cutlist | ≠ marginallegend vs svart topprad med spökknapp | ≠ ritning vs fullbleed mörkt spotlightfoto med centrerad rubrik | ≠ 6 akter med pin vs 5 helbreda band med hårda klipp, ingen pin | ≠ specifikation vs vit sal med mailto i 72 px | ≠ vs rutor som glider in underifrån | **6/6** |
| r2 R2 Vit remsa | `=` båda chaptered editorial | ≠ marginallegend utan topprad vs vit topprad plus pill-filterrad under heron | ≠ ritning vs vitt typband utan bild | ≠ 6 akter, ~13 vh vs 5 sektioner med mörka projektkort | ≠ ritad specifikation vs tyst vitt kontaktblock utan kolofon | ≠ vs pill-flikar som `:target`-markerar rätt kort | **5/6** |
| r2 R3 Färgband | `=` båda chaptered editorial | ≠ marginallegend med symbolprov vs vit topprad med seriflogotyp och fyra länkar | ≠ måttritning vs vit grund med gemen grotesk rubrik och ingen bild alls | ≠ 6 motorakter vs mosaikremsa plus tre mättade tjänsteband | ≠ specifikation på papper vs mörkt band med manifestrad och mailto | ≠ vs färgbanden som *är* tjänsterna | **5/6** |
| r2 R4 Numrerad process | `=` båda chaptered editorial | ≠ marginallegend, ingen topprad vs mörk topprad med tre länkar och en blå pill-CTA | ≠ ritning på kallt papper vs fullbleed mörkt texturfoto med komprimerad tung rubrik | ≠ 6 akter med pin och count vs 4 sektioner med 01–05 i schweizisk rytm | ≠ ritad specifikation vs mörkt band plus en pill | ≠ vs mono-numren 01–05 som genomgående spår | **5/6** |
| r2 R5 Konsolram | ≠ chaptered editorial vs split stage | ≠ ritad marginallegend vs konsolram med versionstagg, klocka och hörnmärken | ≠ ritning vs ordmärket i en konsolram över ett gråskalefoto | ≠ 6 akter vs 3 sektioner | ≠ specifikation vs vitt block med jätterubrik | ≠ vs hörnmärken fixerade i viewporten | **6/6** |
| r2 R6 Affischordmärke | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs fixerad minimal rad med cirkelmärke och kontaktpill | ≠ ritning vs ordmärket i viewportbredd med ett fullbleed dokumentärfoto under | ≠ 6 akter vs 5 sektioner utan motor | ≠ ritad ram med stycklista vs off-white kolofon som stänger på mailto som text | ≠ vs tre 12 px färgprover, ett per demorad | **6/6** |
| r3 build (R5+R6) | ≠ chaptered editorial vs split stage | ≠ marginallegend vs fyra fasta hörnmärken som enda chrome | ≠ en ritning vs två heron sida vid sida | ≠ 6 akter med pin vs 9 rena flow-akter i två parallella spalter | ≠ ett specifikationsblad vs Calyx-ram och prisruta som stänger samtidigt i två spalter | ≠ vs sömlinjen som dras från det dockade märket | **6/6** |
| r4 M1 Kontinuerlig grund | ≠ chaptered editorial vs continuous world (lös läsning) | ≠ ritad marginallegend vs tunn topprad som scrollar bort | ≠ ritning vs en helbred levande Tidvatten-iframe som hela första akten | ≠ 6 akter med pin, kinetic och count vs 8 rena flow-akter över en fast grund | ≠ ritad specifikation vs Calyx-ram och prisruta, avsiktligt osynkade | ≠ vs +50 vh-förskjutningen som låter grunden lysa igenom | **6/6** |
| r4 M2 Kapitel med pinnad scen | `=` båda chaptered editorial | ≠ upprätt ritad legend med symbolprov och ledarlinje vs fast folio `0X/05` plus roterad kapitelskena | ≠ självritande måttritning på kallt papper vs ett stilla konsoltitelkort över en gråskalegrund | ≠ 6 akter (pin 2,4, kinetic, reveal ×3, flow, count) vs 3 motorakter (pin 3,2 och två flow) i fem kapitel | ≠ ritad specifikation med stycklista på papper vs inverterad prisruta ensam i kapitel 05 | ≠ vs kapitelskenan som scrollhuvud (`-scrollY` på inre spår) | **5/6** |
| r4 M3 Galleri med rail | ≠ chaptered editorial vs gallery/catalog | ≠ marginallegend vs indexnav med fyra mono-hopplänkar | ≠ ritning vs affischordmärke staplat över konsolkortet | ≠ 6 akter utan pan vs 6 akter med en inbäddad horisontell `pan`-rail span 4,2 | ≠ specifikation i ritad ram vs en prisruta som katalogens sista objekt | ≠ vs ordskrubben med SVG-tråd i marginalen | **6/6** |
| r5 V1 Dokumentär band | ≠ chaptered editorial vs continuous world | ≠ marginallegend vs ärvd tunn topprad som scrollar bort | ≠ ritning vs band med krämpanel 38 % och färgfoto 62 % | ≠ 6 akter med pin vs 8 rena flow-akter | ≠ ritad specifikation vs ärvd Calyx-ram och prisruta, osynkade | ≠ vs krämpanelen som växer över fotot | **6/6** |
| r5 V2 Cinematisk tvätt | ≠ chaptered editorial vs continuous world | ≠ marginallegend vs ärvd tunn topprad | ≠ ritning vs fullbleed ljusstrålefoto under en svart tvätt | ≠ 6 akter, ingen drift vs 9 akter med drift och parallax | ≠ ritad specifikation vs Hyperborea-ram och prisruta, osynkade | ≠ vs tvättlyftet i en rad CSS | **6/6** |
| r5 V3 Plåt i grunden | ≠ chaptered editorial vs continuous world | ≠ marginallegend vs ärvd tunn topprad | ≠ ritning vs inramad plåt med hårlinje på mörk grund och affischrubrik ovanför | ≠ 6 akter vs 8 flow-akter i två spalter | ≠ ritad specifikation vs Calyx-ram och prisruta, osynkade | ≠ vs ljuspölen som vandrar via object-position | **6/6** |
| r5 V3b Plåt i grunden, polerad | ≠ chaptered editorial vs continuous world | ≠ marginallegend vs ärvd tunn topprad | ≠ ritning vs samma inramade ljuspölsplåt, kapad till en fold | ≠ 6 akter med pin och count vs 8 flow-akter | ≠ ritad specifikation vs ärvd Calyx-ram och prisruta | ≠ vs samma ljuspölsvandring | **6/6** |
| r6 A-K1 Skymning (native) | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs minimal fixerad topbar som växlar över grunderna | ≠ ritning vs fullbleed blåtimmesfoto med ljus serifrubrik | ≠ 6 akter utan zoom vs CSS-dolly skala 1 → 22 och pinnad iframe-avslöjning | ≠ ritad specifikation vs nattfoto som landar och håller | ≠ vs kameran som flyger in i ett fönster | **6/6** |
| r6 A-K2 Affischen (native) | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs tryckt topprad med tickande klocka | ≠ ritning vs ordmärket brutet ALU / NIX med fönster i bokstävernas punsar | ≠ 6 akter vs 7 akter med 320 vh pinnad hero | ≠ ritad specifikation vs bläckark som rullas ner med clip-path | ≠ vs bildremsan som passerar genom bokstäverna | **6/6** |
| r6 A-K3 Konsolen (native) | ≠ chaptered editorial vs live surface | ≠ marginallegend vs app-chrome med 56 px bar och tre numrerade flikar | ≠ ritning vs fullbleed skrivbordsfoto med glaskort som läser tillstånd | ≠ 6 akter vs 6 akter med iframe-scrollTop-växling | ≠ ritad specifikation vs riktigt inmatningsfält som öppnar mailto | ≠ vs scrollen som driver kundsajten i ramen | **6/6** |
| r6 B-K1 Skymning (kedjan) | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad bar som byter grund per akt | ≠ ritning vs blåtimmesfoto med retuscherad skylt och ljus serifrubrik | ≠ 6 akter vs handrullad lerpad zoom utan kit-pin | ≠ ritad specifikation vs nattfoto som öppnas med clip-path | ≠ vs kameran in i ett riktigt tänt fönster | **6/6** |
| r6 B-K1-nogate | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad bar plus separat nav i ramen med toggle-knapp | ≠ ritning vs blåtimmesfoto där målfönstret redan syns i vila | ≠ 6 akter vs 6 akter med 3,8 vh heroloop | ≠ ritad specifikation vs andra nattfotot som håller stilla | ≠ vs samma zoom men med opt-in-ram | **6/6** |
| r6 B-K2 Affischen (kedjan) | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs tunn topprad med `Intl`-klocka | ≠ ritning vs ALU / NIX i variabel Archivo 900 med bildpanel bakom bokstäverna | ≠ 6 akter vs 7 akter med pinnad bildremsa 0 → 55 % | ≠ ritad specifikation vs bläckblock rullat med clip-path till sidans slut | ≠ vs panelglid plus andande block | **6/6** |
| r6 B-K3 Konsolen (kedjan) | ≠ chaptered editorial vs live surface | ≠ marginallegend vs 56 px app-bar med statuschip | ≠ ritning vs dagsljusfoto med krämslöja och glaskort | ≠ 6 akter vs 6 akter med 1:1 scrollTop-mappning | ≠ ritad specifikation vs mörkt avslut med riktigt textfält | ≠ vs besökaren som provkör kundsajtens scroll | **6/6** |
| r7 B-K1 Skymning v2 | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad topbar med logotypväxling och etikettslot | ≠ ritning i inline-SVG vs 100-bilders förrenderad dolly på `canvas[data-sc-sequence]` | ≠ 6 akter, ingen sekvens vs 4 motorakter med pin span 5,0 | ≠ ritad specifikation vs nattfoto som `reveal` plus färgdrift | ≠ vs kameraåkning som blir en levande sida via `window-track.json` | **6/6** |
| r7 B-K2 Affischen v2 | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs tunn topprad med klocka och stad | ≠ ritning vs bild maskad genom bokstävernas uppmätta öppningar plus en svartvit plate | ≠ 6 akter vs 5 akter med pin span 3 och diskret radhöjdssteg | ≠ ritad specifikation på oförändrat papper vs grunden som driftar från papper till bläck | ≠ vs papper bakom masken plus andande block | **6/6** |

**Lägsta summa: 5/6**, mot nio rader — Calyx, Hyperborea, Vintergatan, Vinterspelen, r1 K4,
r2 R2, r2 R3, r2 R4 och r4 M2 — och i samtliga fall är den delade dimensionen *grammatik*,
som målbilden själv låser. Ingen rad faller under 4/6.

**Vad jag bytte i planen, och varför.** Ingen ändring krävdes av gaten; alla ändringar nedan
har andra källor.

1. **Referensvalet.** Målbildens förväntade slugs ersattes av `select.py`s faktiska rad
   (`squarespace`, `aevi-wellness`, `beautiful`, `insign`, `mode`). Källa:
   `catalogue-first.md` § 5 — urvalet ska komma ur katalogen, inte ur minnet. Skälen per
   utesluten slug står i § catalogue-select ovan.
2. **Toppen och signaturen slogs ihop till en enda akt.** Målbilden namnger a1 (pin 2,4) som
   toppen *och* lägger "konturen ritas, sedan tonar den riktiga sajten in" i a3. Källa:
   `feel-and-fingerprint.md` § The tell-someone test — "if the tell-someone sentence and the
   signature move point at different moments, one of them is decoration", och § The peak —
   "a page with three peaks has none". Åtgärd: a1 innehåller hela signaturen (linjen ritas →
   måtten räknas → Calyx fold maskas in i öppningen), och a3:s tre plates degraderas
   avsiktligt till kortare `reveal`-akter utan count och utan pin. Toppen ligger kvar där
   målbilden satte den.
3. **Kapitelrubrikens form.** Målbilden citerar `Vi bygger ert varumärke.`; r7-promptens
   § Alunix, fakta anger den ordagranna strängen som `VI BYGGER ERT VARUMÄRKE.`. Källa:
   copy-gate — ordagrann copy bevaras. Versalformen gäller. Se Q9.
4. **a5 tappade `flow`.** Målbilden skriver `flow+in` (liggaren) följt av `count+flow`
   (specifikationen), vilket sätter samma familj två gånger i rad. Källa: `devices.md`
   § device kit — "never the same one twice running". Åtgärd: a5 är `count` (med `parallax`
   på marginalspalten, vilket chaptered editorial uttryckligen lutar sig mot), a6 är `reveal`.
5. **Assetvägen.** Higgsfield är ute (lead mätte `balance` = 0 credits, free plan,
   2026-09-09). Källa: planens § 10.6 fallback steg 3. Papperstexturen blir procedurell
   SVG/CSS och de ritade elementen handförfattad inline-SVG. Se `runs/K3/assets/ASSETS.md`.
6. **Reduced motion utgår.** r7-briefens fält "Reduced motion-planen" finns inte i K3:s
   skelett. Källa: F-011.

### (5) Rörelse

**Motion-tes.**

- **Focal.** Ögat ska följa **linjespetsen** — den punkt där konturen just nu ritas. Allt
  annat i vyn står stilla medan den rör sig. När linjen är klar flyttas fokus en gång, till
  måttkedjan, och en gång till, till öppningen som fylls. Tre fokusskiften i hela akten.
- **Continuity.** Ritordningen är en enda obruten hand: yttre kontur → hjälplinjer →
  måttlinjer → utrop. Ingenting hoppar in i vy, ingenting tonar in ur intet; varje element
  har en startpunkt på arket som redan var synlig som en linjeände. Öppningen som fylls är
  samma rektangel som konturen ritade, inte en ny ruta ovanpå (F-010).
- **Feedback.** Scrollen *är* pennan: 1 % scroll = 1 % ritad linje, båda riktningarna,
  ingen låsning, ingen hijack utöver motorns egen pin. Att scrolla uppåt suddar linjen i
  exakt omvänd ordning. Marginallegendens ledarlinje dras när ett kapitel blir aktivt — det
  är sidans enda hover-oberoende statuskvittens.
- **Budget.** Ritningen är **en** `<svg>` med ≤ 60 `path`/`line`-element och ett enda
  `stroke-dashoffset`-uttryck per bana, alla drivna av **`--sc-ps`** via `calc()` i CSS —
  ingen per-frame JS-skrivning per bana. `will-change: stroke-dashoffset` sätts bara medan
  `0 < ps < 1`. Två typsnittsfiler, båda variabla, båda preloadade, tak 300 kB totalt.
  Iframes monteras via IntersectionObserver, `loading="lazy"`, aldrig fler än en igång
  samtidigt. Måltal (F-014, `motion-smoothness.md` § The bar, vid 4× CPU): `staircase = 0`,
  `max_step ≤ 3 %`, bildtid p95 ≤ 20 ms, noll frames > 33 ms, båda scrollriktningarna mätta.

**Feeling curve** — en känsla per akt, orsaken i andra kolumnen, aldrig två lika i rad.

| # | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| a1 | **Fascination** ← TOPPEN | Ett tomt kallt ark håller stilla i 0,12 av akten, sedan börjar en enda linje färdas, en sidas anatomi växer fram ur ingenting, måtten landar på sina riktiga tal, och öppningen linjen just ritat fylls av en verklig webbplats |
| a2 | **Beslutsamhet** | Kapitelrubriken anländer rad för rad under en linjal som dras samtidigt |
| a3 | **Tillit** | Tre riktiga sajter, en i taget, var och en innanför sin egen ritade ram, i en grad där man kan läsa dem |
| a4 | **Klarhet** | Tre rader, tre ord, en utropad radhöjd `96 px`, ingenting annat i vyn |
| a5 | **Trygghet** | Priserna kommer in som en stycklista och räknas upp till 26 900 och 38 900, med ledarpunkter fram till kolumnen |
| a6 | **Ro** | Ramens fyra linjer dras in runt manifestraden och sidan slutar röra sig |

**Författad tystnad** (måste stå i BRIEF.md så `scroll_verify.py`s `blankBands` inte larmar
falskt): de första 0,12 av a1 är ett medvetet nästan tomt ark med bara titelblocket. Det är
tystnaden före toppen, inte död scroll.

**Tell-someone-meningen.** *"Det är sajten där man ser hemsidan ritas som en ritning, och sen
blir ritningen sidan på riktigt."*

**Device-tabell.** Fem familjer (`pin`, `kinetic`, `reveal`, `flow`, `count`), aldrig samma
två i rad, noll `scrub`, noll pekar-devices. Kolumnen **läser** anger vad varje rörlig sak
läser: `--sc-ps` för allt ögat ser förflytta sig, `--sc-p` bara för cue-opacitet, och
"motorns egen" där motorn själv äger transformen (F-014 regel 1).

| Akt | Sektion | Device (familj) | Span / cue | Vad som rör sig | Läser | Varför just denna |
|---|---|---|---|---|---|---|
| a1 | Ritningen | `pin` (+ `count` staplad) | span 2,4 · dwell 0,35 · cue `0 1 0 0` (greet och håll, ground finns) | `stroke-dashoffset` på varje kontur, hjälplinje och måttlinje; `mask-position`/`clip-path` på öppningen som fylls | **`--sc-ps`** (ritningen, masken); `--sc-p` (utropens opacitet); motorns egen (`count`) | Ramen måste hålla stilla medan en enda idé korsar den — `grammars.md`, pin |
| a2 | Tesen | `kinetic` lines | cue `0.1 0.9 0.15 0.4` | Rubrikens rader ur en mask; linjalen under dem | motorns egen (raderna); **`--sc-ps`** (linjalens `scaleX`) | En kinetisk rubrik per akt, rader nästan alltid rätt — `devices.md` § 5 |
| a3 | Tre plates | `reveal` ×3, riktning `up` | `data-sc-reveal-at="0.15 0.55"` per plate | Ramkonturen ritas, sedan wipeas sajten fram innanför den | **`--sc-ps`** (konturen och wipe-masken) | `clip-path`-wipe = tillståndsbyte; `iris` sparas och används inte alls på sidan |
| a4 | Liggaren 01–03 | `flow` + `in` | stagger 70 ms, reducerad blockpadding (akten följer inte direkt på en pin, men ligger nära) | Tre rader stiger 14 px och tonar in | `--sc-p` (opacitet); motorns egen (14 px-lyftet) | Administrativt innehåll komprimeras, aldrig pinnas — `feel-and-fingerprint.md` § Pacing |
| a5 | Specifikationen | `count` (+ `parallax` på marginalspalten, rate 0,4) | `data-sc-count-at="0.1 0.5"`, 1,4 s, cubic ease-out | Prissiffrorna räknar; marginallegenden driver långsammare än spalten | motorns egen (`count`); **`--sc-ps`** (parallaxen) | Endast sanna tal får en count — `devices.md` § 7; parallax i en spalt är chaptered editorials egen |
| a6 | Avslutet | `reveal` (sidans sista akt) | cue `0.25` (ett värde: sista akten måste hålla) | Ramens fyra linjer dras in i ordning: överkant, höger, underkant, vänster | **`--sc-ps`** | Avslutet ska lösa upp, inte tona ut — `feel-and-fingerprint.md` § The peak |

**Embodiment, en enda** (`feel-and-fingerprint.md` § Being in it: "one or two per page"):
dwell-triggad detalj i a1. Står `--sc-ps` stilla över några frames medan akten är pinnad,
ritas ett extra utrop in i marginalen — spaltavståndet `7 rem` — som aldrig behövdes för att
förstå ritningen. Belöning för att stanna. Inget annat på sidan reagerar på besökaren.

**Rejected-lista** (`find-animation-opportunities`-gaten, fyra frågor per kandidat).

| Kandidat | Frekvens | Syfte | Hastighet | Funktion | Dom |
|---|---|---|---|---|---|
| Tilt på de tre plates vid hover | Varje pekarpassage, alltså mycket ofta | Dekor | ~150 ms | Ingen — och den får ramen att läsa som ett kort i stället för som papper | **Avvisad.** TASTE § 2.3 (aldrig kort), `devices.md` § 9 (tilt konkurrerar dessutom om `transform` med cue) |
| Spotlight som följer pekaren över arket | Konstant | Atmosfär | Kontinuerlig | Ingen | **Avvisad.** Chaptered editorial förbjuder `spotlight` uttryckligen; TASTE § 5 (spotlight noll i materialet) |
| Marquee med de tre exempelsajternas namn | Alltid, i loop | Fylla tomrum | Långsam loop | Ingen; Hyperborea äger redan marquee i registret | **Avvisad.** Fingerprint + TASTE § 3 (marquee hör till consumer-brand och ingen annanstans) |
| Ritrutnät som "andas" bakom allt | Alltid | "Liv" | ~8 s loop | Ingen | **Avvisad.** TASTE § 3 product-focused: "Rörelse: subtil, aldrig breathing". Texturen rastreras en gång och animeras aldrig |
| Magnetisk mailto i avslutet | Vid varje pekarnärmande | Dra blicken till handlingen | ~200 ms | Marginell; grammatiken förbjuder `magnet` | **Avvisad.** `grammars.md`, chaptered editorial bans |
| Ledarlinjen som ritas från legenden till aktivt kapitel | Fem gånger per besök | Säger vilket kapitel som är på skärmen | ~240 ms | **Ja — det är navigationen** | **Behållen.** Den är sidans nav, inte en effekt |

**Delight-tes, en mening.** *Ritningen blir sidan*: samma rektangel som bläcket nyss ritade
fylls med en levande webbplats medan bläcket står kvar som ram, så att besökaren ser
ritningen och det byggda vara samma sak.

### (6) Färg och typ

**Färgstrategi: Restrained.** Den fysiska scenen, i en mening: *ett A2-ark kallt blågrått
ritpapper på ett jämnt upplyst bord, ritat i mörkt petrolbläck, där bara måttsiffrorna är
inkade i en enda blå.*

Namngiven referens för strategin (brand.md: "unnamed ambition becomes beige"):
**Squarespace 0 %-colourfulness, flyttad ett hack** — Squarespace reserverar all mättnad för
användarens egna sajter och håller marknadsföringsytan akromatisk; K3 håller arket
enkromatiskt-kallt och släpper in **exakt ett** kromatiskt värde, inhägnat till en
innehållstyp. Att detta är Restrained och inte Committed är ett medvetet val mot brand.md:s
varning för det timida: mängden *linje* på arket är hög, tätheten är hög, och en drench på ett
ritark vore en osanning om vad en ritning är.

**Föreslagna tokens** (byggaren får skärpa värdena mot uppmätt kontrast, aldrig flytta rollen):

| Token | Värde | Roll |
|---|---|---|
| `--paper` | `oklch(0.95 0.012 230)` | Arket. Kallt, låg chroma, *inte* cream (AB09-lärdomen, låst av lead) |
| `--paper-fold` | `oklch(0.925 0.018 230)` | Andra arket: bara i a3:s plate-marginaler och a6:s ram, som materialbyte mellan akter (TASTE § 4.5) |
| `--ink` | `oklch(0.30 0.055 245)` | Bläcket: all typ, alla bärande konturer. Mörk petrol/ultramarin |
| `--ink-hair` | `oklch(0.52 0.035 240)` | Hjälplinjer, måttlinjer, skrafferingar. Aldrig typ |
| `--blue` | `oklch(0.47 0.13 252)` (= `#1E5E9C`) | **Enda accenten.** Bara måttsiffror i displayskala. Aldrig en yta, aldrig en länk, aldrig en ram |

Rollregler, formulerade så att de går att granska: *ett blått moment per viewport*
(beautiful-regeln, ordagrant övertagen), och *det momentet är alltid en sann uppmätt siffra*
(mode-inhägnaden, skärpt från komponent till innehållstyp). Noll `box-shadow`, noll
`backdrop-filter`, noll gradient, radie 0 överallt.

Kontrast som byggaren måste mäta, inte anta: `--ink` på `--paper` ≈ ΔL 0,65 (godkänt med bred
marginal); `--blue` på `--paper` ligger nära AA-gränsen för normal text och används därför
**bara** i displaygrad — kör `contrast_over_media.py --url` per grund i R3 och skriv siffran
i NOTES.md.

**Typsnitt — brand.md:s fyra steg, utförda.**

1. **Tre varumärkesord, fysiska objekt-ord:** *uppmätt · handrullad · kall.* (Inte "modern",
   inte "elegant". Objektet är ett arkitektritat snitt på blått ritpapper.)
2. **Reflexlistan, alltså de tre jag skulle gripa efter först:** Inter, Space Grotesk,
   IBM Plex Sans/Mono. **Alla tre avvisade** — de står i brand.md:s reflex-reject-lista och
   dessutom i r1–r7-listan.
3. **Katalogen, med objektet i huvudet:** ritningens titelblock, stencilbokstäverna i en
   måttsatt sektion, en verkstadsritnings utrop. Det pekar mot grotesker med mekaniskt,
   mallritat drag och mot en mono som är ritad för teknik, inte för kod-nostalgi.
4. **Korskontroll:** förstavalen sammanfaller inte med reflexen — annars börjar om.

**Förbjudet** (reflexlistan + allt använt i r1–r7): Fraunces · Newsreader · Lora · Crimson ·
Crimson Pro · Crimson Text · Playfair Display · Cormorant · Cormorant Garamond · Syne ·
IBM Plex Mono · IBM Plex Sans · IBM Plex Serif · Space Mono · Space Grotesk · Inter · DM Sans ·
DM Serif Display · DM Serif Text · Outfit · Plus Jakarta Sans · Instrument Sans ·
Instrument Serif · Geist · Geist Mono · JetBrains Mono · Public Sans · Familjen Grotesk ·
Literata · Fragment Mono · Hanken Grotesk · Archivo · Figtree · Cardo · PT Mono · Cinzel ·
Vollkorn · Italiana · Bricolage Grotesque · Manrope · Schibsted Grotesk · Bodoni Moda ·
Noto Serif JP.

**Röst — grotesk med teknisk karaktär. Fem kandidater, rangordnade.**

| # | Snitt | Källa | Varför den passar objektet | Risk |
|---|---|---|---|---|
| **1** | **Chivo** (Omnibus-Type) | Google Fonts, variabel | Vågrätt avskurna terminaler och kvadratiska bukter — bokstäverna läser som dragna med vinkelhake, inte som humanistiska. Äkta 300 och 700 i samma variabla fil, så hela vikthierarkin kostar en fil | Kan läsa som neutral neo-grotesk i små grader; motverkas med stram tracking i display |
| 2 | **General Sans** (Indian Type Foundry, Fontshare) | Fontshare, variabel | Nära geometrisk, mycket jämn färg i text, tydliga öppningar — ett ritbords-neutralt snitt utan mall-doft | Neutraliteten är också dess svaghet: mindre karaktär i 72 px |
| 3 | **Sora** (Jonny Pinhorn) | Google Fonts, variabel | Geometriskt-tekniskt, låga kontraster, mycket rena bågar; sitter bra ihop med en mono | Något kall även i brödtext, vilket kan bli enformigt över hela sidan |
| 4 | **Anybody** (Etcétera) | Google Fonts, variabel bredd | Breddaxeln gör att utrop kan komprimeras som i ett titelblock utan att byta snitt | Karaktärsstark nog att konkurrera med ritningen om uppmärksamheten |
| 5 | **Darker Grotesque** | Google Fonts, variabel | Hög x-höjd och smala former, effektiv i marginallegendens trånga spalt | Displaygraderna blir smalare än ritningens luft vill ha |

**Förstavalet, motiverat enligt de fyra stegen:** **Chivo**. Steg 1:s ord är *uppmätt,
handrullad, kall* — Chivos vågrätt avskurna terminaler och kvadratiserade bukter är precis den
mallritade känslan, och den behåller den i 72 px. Steg 2: den står inte på någon av
förbudslistorna. Steg 3: det fysiska objektet är ett titelblock, inte en tidskriftsrubrik, och
Chivo är ritad för rubriker med stark viktkontrast inom en familj, vilket är exakt vad ett
titelblock gör. Steg 4: den sammanfaller inte med reflexen (Inter / Space Grotesk / Plex).
Praktiskt: en variabel fil täcker 300–700 och håller typsnittsbudgeten (≤ 3 filer, ≤ 300 kB,
`performance.md` § 1).

**Register — mono. Fem kandidater, rangordnade.**

| # | Snitt | Källa | Varför | Risk |
|---|---|---|---|---|
| **1** | **Martian Mono** (Evil Martian) | Google Fonts, variabel bredd | Ritad för tekniska gränssnitt, med bred, stencilaktig ton som läser som påstämplade siffror på en ritning; breddaxeln låter måttsiffrorna sättas brett i displaygrad och smalt i marginalen utan snittbyte | Tung färg; får aldrig sättas i löpande text |
| 2 | **Chivo Mono** (Omnibus-Type) | Google Fonts, variabel | Perfekt metrisk syskonskap med förstavalet i röstrollen | Samma superfamilj kan läsa som *ett* snitt och därmed försvaga registerkontrasten |
| 3 | **Spline Sans Mono** | Google Fonts, variabel | Lugn, smal, mycket läsbar i 11–13 px etiketter | Mindre karaktär i displaygrad, vilket accenten behöver |
| 4 | **Azeret Mono** | Google Fonts, variabel | Kantig och mekanisk, stark i siffror | Egensinnig nog att slåss med ritningen |
| 5 | **Sometype Mono** | Fontshare | Varm och rundad mono med gott siffermaterial | Värmen drar åt fel håll mot ett kallt ark |

**Förstavalet:** **Martian Mono**, i register-rollen och ingen annan: måttsiffror, utrop,
folio, radnummer 01–03, ledarpunkter, titelblockets fält. Rollerna korsar aldrig (TASTE
§ 4.2): Chivo sätter aldrig ett mått, Martian Mono sätter aldrig en rubrik eller brödtext.

**Krock-hantering (lead löser ur listorna).** Om K4 väljer Chivo tar K3 General Sans; om K4
väljer Martian Mono tar K3 Spline Sans Mono (inte Chivo Mono, eftersom superfamiljerisken
kvarstår oavsett).

### (7) Vad referenserna gör som cellen måste slå

| Låst referens | Vad den gör | Vad K3 måste göra bättre |
|---|---|---|
| **squarespace** (primär) | Deklarerar 0 % colourfulness och reserverar all mättnad för kundernas egna sajter, med vikt 300 vid 60–70 px på ett fullbleed dokumentärfoto | Göra reservationen strukturell i stället för bara kromatisk: det enda mättade i vyn är kundsajten *inne i den ritade öppningen*, och det enda kromatiska på arket är en sann måttsiffra. Squarespace visar kundsajter som lutande plattor bredvid heron — K3 visar dem i det hål bläcket ritade, vilket är det Squarespace inte gör |
| **insign** (sekundär) | Låter tre fullmättade färgband *vara* navigationen, så tjänsten känns igen på färg före text; varierar bevisformaten | Navigera med ritade symboler i stället för färg — legendens hårlinje, måttpil och skraffering säger vilket kapitel som är aktivt utan en enda färg — och slå insigns bevisapparat genom att inte ha någon: tre riktiga sajter, inga betyg, inga omdömen, ingen teamgrid |
| **aevi-wellness** (sekundär) | Hårlinjen är enda strukturmedlet, skugga är förbjuden, djup kommer ur bandväxling | Ge hårlinjen betydelse: i aevi är den en ram, i K3 är varje linje antingen en kontur, en måttlinje, en hjälplinje eller en ledare, och en linje utan sådan roll får inte ritas |
| **beautiful** (sekundär) | Ransonerar accenten till en granskningsbar regel: ett korallmoment per viewport | Behålla regelns granskningsbarhet men flytta den till en hårdare grund: ett blått moment per viewport **och** momentet måste vara ett verkligt uppmätt tal, vilket gör regeln omöjlig att drifta in i dekor |
| **mode** (wildcard) | Inhägnar accenten till en komponenttyp (enda fyllda knappen) och bygger djup ur en färgstack utan skugga; färgkodad teckenförklaring gör en illustration läsbar | Skärpa inhägnaden från komponent till innehållstyp, och göra legenden till sidans nav i stället för en bildtext — mode:s legend förklarar en bild, K3:s legend styr sidan |
| **before-ai-slop** (anti-referens) | Bygger ett låtsas-dashboard av `<div>`, sätter ett gradientord i rubriken och möblerar med badge, pill, logotypvägg och tre ikonkort | Aldrig rita innehåll. Ritningen ritar form: kontur, mått, utrop. Varje siffra på sidan är sann. Den enda ytan som visar ett gränssnitt är ett riktigt gränssnitt |

### (8) Rut-testet

**Kategorins default för "digital byrå", tre rader, hållen utanför:**

1. Centrerad hero med en badge-rad ovanför, ett gradientfärgat ord mitt i rubriken, två
   pill-CTA och en avatarstack, över en vit-till-lila grund, med ett dashboardkort till höger.
2. Logotypvägg av kundmärken, tre likadana ikonkort för tjänsterna, ett statband med fyra tal,
   tre priskort där ett bär "populärast".
3. Teamporträtt i rutnät, omdömeskarusell med stjärnor, kontaktformulär, och ett mörkt
   CTA-band som avslutning.

**Var målbilden möter defaulten, och vad som ändras:**

| Punkt där K3 riskerar att sammanfalla | Vad som ändras |
|---|---|
| Tre tjänster i rad (01–03) = samma *form* som tre ikonkort | Tre hårlinjerader i en liggare på ett ark, olika radlängd, radhöjden `96 px` utropad i marginalen. Aldrig tre lådor, aldrig en ikon, aldrig lika bredd |
| Tre paket med priser = samma *form* som tre priskort | En stycklista i **en** ritad ram: rad, ledarpunkter, en kolumn med figurer. Ingen ram runt varje pris, ingen "populärast", ingen jämförelsetabell |
| Att visa kundarbete = samma *form* som logotypvägg eller projektgrid | Tre plates, en i taget, varje plate en **levande** sajt innanför en ritad, måttsatt öppning, etiketterad med de ordagranna raderna. Noll logotyper, noll kundnamn utöver de tre sajterna |
| Sticky topprad med länkar och en CTA-knapp = kategorins reflex | Ingen topprad alls. Navigationen är en ritad teckenförklaring i marginalen, och kontakten är en mailto i löpande text i avslutet |
| "Vi är bäst"-bevis (betyg, antal projekt, år i branschen) | Existerar inte i K3. PRODUCT.md § absences förbjuder dem, och `devices.md` § 7 förbjuder en count utan verifierad siffra. De enda tal på sidan är mått och priser |
| Ett dashboard/produktkort i heron som visar "verktyget" | Heron visar en **ritning**, inte ett gränssnitt. Gate 47/79-kontrollen i troplistan är den mekaniska spärren |

---

## Öppet

- **Q8** (`QUESTIONS.md`): planens § 7.5-lista över förväntade katalogposter för K3 stämmer
  inte med `select.py`s deterministiska utfall. Antagande tills svar: skriptets rad gäller.
- **Q9** (`QUESTIONS.md`): tesrubrikens form, versal eller gemen. Antagande tills svar:
  `VI BYGGER ERT VARUMÄRKE.`, den ordagranna strängen ur r7-promptens § Alunix, fakta.
- **Q10** (`QUESTIONS.md`): de fem live-rubrikerna i kategorin kunde inte hämtas i den här
  sessionen (ingen webbsökning tillgänglig här). Fältet står som `[needs: live-rubriker]` i
  `runs/K3/BRIEF.md` och byggaren fyller det i R1.
