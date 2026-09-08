# NOTES.md — K2 Affischen, runda 2 (akt A: hero + signaturakt)

## Vad byggdes

`index.html` + oförändrade `scrollcraft.js`/`scrollcraft.css` (kopierade från
`~/.claude/skills/design/scripts/scroll/`, aldrig redigerade). Bara akt A: heron i vila,
signaturrörelsen (papperet glider bakom bokstavsmasken Calyx → Hōrai → Hyperborea, blocket
öppnar sig i ett steg till "VI BYGGER" / "ERT VARUMÄRKE."), toppbaren med riktig klocka, och
en tillfällig platshållarsektion (`.opened`) för nästa akt.

Fönstermasken i A, U, X återanvänder r6 A-K2:s `inkScan()`/`buildWindows()`-teknik rakt av
(canvas-alfaskan av det faktiska renderade glyfet, aldrig en gissad rektangel) — samma
Archivo 900/font-stretch:100% som den teknikens mätning förutsätter, så masken stämmer
med det som faktiskt visas.

Blockets öppning är en diskret **steg**, inte ett kontinuerligt font-size-svaj (uttrycklig
rättelse från orkestreraren): `font-size` rörs aldrig av scrollen. Vad som ändras är radernas
mellanrum (`.row + .row{margin-top}`, krossat ≈ -2,6vw → öppet ≈ +3,8vw) och en ren
opacity-korstoning mellan bokstavslagret (`.fa`) och nästa rubrik (`.fb`), båda begränsade
till ett smalt fönster `p 0,62–0,84` som sedan håller stilla till `p=1`.

Typsnitt: Archivo (display, en variabel familj) + Familjen Grotesk (register), roller korsar
aldrig. Archivos breddaxel gör kontrasten orkestreraren bad om: ordmärket ALU/NIX vid
`font-stretch:100%` (den bredd `inkScan()`s canvas-mätning förutsätter, rörs inte, se öppen
fråga 1), "VI BYGGER ERT VARUMÄRKE." vid `font-stretch:82%` (smalare) — samma familj, ingen
tredje font.

## Bilder jag läste (30 st)

Alla via `Read`, ingen bedömning gjord ur kod ensam:

- `fold-1440.png`, `act-00.png` … `act-80.png` (6 rutor: 0/15/30/45/60/80 % av pin-spannet,
  rörelseläge, 1440×900)
- `preview-calyx.png`, `preview-horai.png`, `preview-hyperborea.png`, `preview-open.png`
- `rm-fold-1440.png`, `rm-50pct-1440.png` (reduced motion)
- `fold-390.png` (mobil, rörelseläge)
- `fold-320.png`, `fold-768.png`, `fold-768-full.png` (diagnostik för överlappsbugg nedan)
- `demo-horai.webp`, `demo-hyperborea.webp` (läste källbilderna för att skilja äkta
  bakgrundsoskärpa/glöd i fotona från ett renderingsfel — se nedan)

## Vad jag såg och ändrade

**Bugg 1 — dödscroll under reduced motion.** Motorn sätter `heroAct.style.height` till
`data-sc-span*100vh` oavsett `prefers-reduced-motion`, eftersom `layout()` inte känner till
mina egna `.rm`-klasser. Lämnat orört hade det gett en 300vh tom rullbana under reduced
motion trots att `.stage` själv blev `position:static`. Fix: JS tar bort `data-sc-act`/
`data-sc-span` från `heroAct` INNAN `ScrollCraft.mount()` körs, när `prefers-reduced-motion`
matchar, så motorn aldrig gör om sektionen till en pinnad akt. Bekräftat i `rm-fold-1440.png`
(ingen dödscroll, ingen synlig skillnad mot vila) och `rm-50pct-1440.png` (blocket öppet som
egen sektion, ingen tumnagel, inget hopp — F-001).

**Bugg 2 — ordmärket överlappade brödtexten vid 768 px (upptäckt, inte i kravlistan men
bröt "inget horisontellt överflöde"-andan och var en riktig layoutkrasch).** Under 900 px
byter kompositionen till en kolumn (platen ovanför blocket), men `.stage` försökte fortsatt
tvinga in allt i en fast `100vh - bar`-hög flexbox med `justify-content:space-between`.
Flexboxen krympte `.composition`s tilldelade utrymme för att få plats, men rutnätets
innehåll (ordmärkets rader, storlek satt i viewport-enheter, inte krympbar av flexbox)
ritades ändå i sin fulla storlek och överlappade `.under`-blocket under. Uppmätt: `row2`
(NIX) sträckte sig till y=1002 medan `.under` redan börjat på y=868 — en 134 px kollision.
Fix: samma breddgräns (899px) som redan styr kompositionens kolumnbyte får nu `.stage`
att bete sig som reduced motion (`position:static;height:auto;overflow:visible`, ingen
pin), `.fb` döljs, `.opened`-platshållaren visas istället — och JS stryker
`data-sc-act`/`data-sc-span` på samma breddgräns, av samma skäl som bugg 1. Verifierat:
`scrollWidth===clientWidth` vid 320/768/1440 px, och `fold-768-full.png` visar ett rent,
okrockat flöde. En `matchMedia`-lyssnare kör `location.reload()` om bredden korsar 899px
live (rotation/fönsterändring), eftersom att montera om motorn mitt i sessionen är dyrare
än en omladdning för det här strukturella skiftet.

**Inte en bugg, verifierat mot källan:** de "suddiga" fönsterurklippen vid Hōrai (act-30,
act-45) och Hyperboreas glödande orange rundning (act-45, act-60) är äkta innehåll i
`demo-horai.webp`/`demo-hyperborea.webp` (skärpedjup i matfotot, en mjuk radiell sol-glöd),
inte en renderingsdefekt. Kontrollerat genom att läsa källbilderna direkt innan jag ändrade
något.

## Avvikelser från BRIEF.md, och varför

1. **Andningsfönstrets exakta gränser** (BRIEF skissade `p 0,62–0,86`) landade på
   `p 0,62–0,84` efter att jag byggde — en mindre justering för att lämna en tydligare
   hållplatå (`0,84→1,0`) innan pinnen släpper, så sista rutan i pin-spannet aldrig fångar
   en halvfärdig övergång. Skillnaden är kosmetisk, inte en avvikelse i sak.
2. **Ingen `data-sc-drift` än.** Akt A har inget färgskifte (det hör till akt E/avslutet,
   runda 3). `--sc-canvas` sätts en gång via tokens, ingen `drift`-egenskap används ännu.
3. De två layoutbuggarna ovan (reduced-motion-dödscroll, 768px-överlappen) fanns inte i
   BRIEF:s plan eftersom BRIEF inte byggde kod — de är runda 2:s egna upptäckter, fixade
   innan leverans, inte avvikelser från vad BRIEF bad om.

## Öppna frågor

1. **Kontrastmätning formellt ogjord.** `scripts/contrast.py` förväntar sig en server på
   `localhost:3055` och tar inte emot en URL som argument i den här versionen — kunde inte
   köras mot `serve.py`s port 3202 utan att ändra skriptet, vilket jag höll mig ifrån
   (skriptet är inte mitt att redigera den här rundan). Kickers/bildtexter (`--line-2` på
   `--paper`) ser läsbara ut i alla 12 skärmdumpar jag läste, men en riktig mätning bör köras
   i en fullständig Step 5-pass, inte antas här.
2. **`--poster`-variabeln är death code.** Den är deklarerad i `:root` och används bara för
   att skala `.fb`s teckenstorlek (`calc(var(--poster)*0.46)`), inte för att sätta
   ordmärkets egen storlek (den styrs av kolumnbredd via `width:100%` på SVG:n). Fungerar,
   men namnet är missvisande — värt att städa upp i runda 3 om fler storlekar behöver samma
   bas.
3. **Platens bildkälla** (`assets/plate-desk.webp`) beskär till 4:5 på desktop, 16:9 under
   900px (matchar hur A/B-K2 hanterade samma foto tidigare rundor) — inte uttryckligen
   specificerat i BRIEF, ett rimligt antagande men flaggar det ifall en annan beskärning
   önskas.

---

# Runda 3 — andningen rättad, hela sidan byggd

## Vad ändrades i akt A (det underkända)

**Andningen var en korstoning, inte en isärglidning (Underkänt 1).** Rättat helt enligt
instruktionen: `.fa` (ALU/NIX-lagret) har ingen opacitetsregel någonstans längre — bokstäverna
är bläcksvarta (`var(--ink)`) genom hela akten, aldrig ett lager som tonar. Det som nu
animeras är `.row-a`/`.row-b`s `transform:translateY()` (rad ALU glider uppåt, rad NIX glider
nedåt, ovanpå en fast krossad basmarginal `-2,6vw` som aldrig ändras — separationen stör
alltså aldrig dokumentflödet). Rubriken `VI BYGGER` / `ERT VARUMÄRKE.` sitter i ett
noll-höjds `.headingWrap`-ankare mitt i sömmen (centrerat via `translateY(-50%)`), med två
`.hline`-spans som reser sig staggrat (kinetic lines) styrda av egna `--l1`/`--l2`-variabler.

Tre iterationer krävdes för att få separationen fri från kollision, alla verifierade med
skärmdumpar innan nästa fix:

1. Första försöket (`±6,5vw` symmetriskt) fick ALU att krocka med `.desc`-raden ovanför
   (`preview-open.png`, första versionen) — asymmetrerade till row-a `-2,5vw` / row-b `+5vw`
   och minskade rubrikens teckensnitt (`clamp(1,15rem,2,5vw,2,3rem)` istället för det
   ursprungligt tilltänkta större måttet) plus 1,5vw/3vw padding ovan/under kompositionen.
2. Andra försöket löste ALU-kollisionen men flyttade NIX in i bildtexten/leadcopy under
   (samma bugg, andra riktningen) — löst med samma asymmetriska mått ovan.
3. Tredje fyndet, i mitten av scrubben (`d-75.png`, p≈0,75): rubrikraden `ERT VARUMÄRKE.`
   tonade in innan gapet faktiskt hunnit öppna sig, så den overlappade tillfälligt bokstaven
   N. Fixat genom att skjuta upp `--l1`/`--l2`s tröskel (från `openT/0.55` och
   `(openT-0.25)/0.55` till `(openT-0.3)/0.5` och `(openT-0.5)/0.5`) så rubriken bara syns
   efter att separationen redan är påtaglig.

Slutresultat verifierat rent i `preview-open.png` (p=1, det formade läget: ALU överst i
bläck, rubriken centrerad i gapet, NIX under, platen kvar till höger, inget spöke, inget
tomt band större än rubrikhöjden) och i `d-75.png` efter fixen (mitt i scrubben, ingen
kollision, rubrikens andra rad bara delvis framme som förväntat mitt i en pågående
övergång).

**Reduced motion/smal bredd** (`.opened`-sektionen) fick motsvarande statiska variant:
samma `row-a`/`row-b`-translate hårdkodat till maxvärdena, samma rubrik alltid synlig,
egna SVG:er (`win1b`/`win2b`) med hårdkodad `transform="translate(0 -468)"` på remsan så
fönstren visar Hyperborea (sista läget före pinnen släpper) i stället för Calyx. Ingen
körning av `buildWindows()` behövde dupliceras separat — funktionen läser nu
`document.querySelectorAll('svg[data-word]')` och bygger masken för alla fyra SVG:er
(två i heron, två i den statiska sektionen) med samma kod.

## Bugg 3 (ny, hittad under rundan): driften läckte in i tidigare sektioner

`data-sc-drift` på akt E sätter `--sc-canvas` (och därmed `<body>`s bakgrund) globalt, inte
avgränsat till akt E:s egen ruta. En flow-akts `raw`-progress blir positiv en hel
skärmhöjd innan akten faktiskt syns (`(y+vh-top)/(height+vh)`), så bakgrunden hann redan bli
bläckmörk medan läsaren fortfarande läste prislistan i akt D — vars text aldrig var tänkt
att synas mot en mörk botten. Fångat i `m390-price.png` (första versionen): nästan osynlig
mörkgrå text på mörk botten. Fix: varje tidigare sektion (`.hero`, `.opened`, `.proof`,
`.ledger`) fick en egen ogenomskinlig `background:var(--paper)`, så den drivande sidbottnen
bara syns genom akt E:s egen (genomskinliga) ruta. Verifierat efter fix i `m390-price.png`
och `m390-close.png`: prislistan läsbar på papper, sedan en ren, omedelbar tonal inversion
vid sektionsgränsen till akt E.

## Bugg (testartefakt, inte en sidbugg): `full_page` missar iframes under reduced motion

Första `rm-full-1440.png` (tagen med Playwrights `full_page=True` utan föregående scroll)
visade tre TOMMA VITA rutor där Calyx/Hōrai/Hyperborea-uppslagen skulle synas. Misstänkte
en reduced-motion-specifik bugg, verifierade genom att (a) scrolla inkrementellt med riktiga
scroll-events innan samma `full_page`-tagning (samma resultat, fortfarande tomt) och (b)
läsa `clipPath`/`iframeSrc`/`shotDisplay` direkt ur DOM:en (allt korrekt: `clip-path:none`,
rätt `src`, `.shot` korrekt dold) och (c) ta en vanlig (icke-`full_page`) skärmdump скrollad
till exakt samma position (`rm-spread-check.png`) — den visade Calyx och Hōrai fullt
renderade, i färg, korrekt. Slutsats: Chromiums `full_page`-ombyggnad av viewporten target
tappar iframes `loading="lazy"`-laddade innehåll vid om-renderingen; det är ett
testverktygsfel, inte en sidbugg. Alla riktiga runda-3-skärmdumpar av akt B under reduced
motion (`rm-proof-calyx.png`, `rm-proof-horai.png`, `rm-proof-hyperborea.png`) togs därför
som vanliga (icke-`full_page`) skärmdumpar efter explicit scroll, och visar korrekt innehåll.

## scroll_verify.py — båda lägena, resultat inklistrat

**Rörelseläge** (`shots/sv/`):
```json
{
  "deadScroll": [
    {"from": 0, "to": 300, "diff": 0.0019},
    {"from": 300, "to": 600, "diff": 0.0139},
    {"from": 900, "to": 1200, "diff": 0.0037},
    {"from": 1500, "to": 1800, "diff": 0.0082}
  ],
  "cuesNeverFull": [],
  "unrevealed": [],
  "contrastUnderMedia": [],
  "blankBands": [
    {"from": 894, "to": 2843, "px": 1949},
    {"from": 5212, "to": 5769, "px": 557},
    {"from": 5871, "to": 6844, "px": 973}
  ]
}
```

**Reduced motion** (`shots/sv-rm/`):
```json
{
  "deadScroll": [],
  "cuesNeverFull": [],
  "unrevealed": [],
  "contrastUnderMedia": [],
  "blankBands": [
    {"from": 4421, "to": 4978, "px": 557},
    {"from": 5080, "to": 6054, "px": 974}
  ]
}
```

**Läsning av fynden** (kontrollerad mot `sv/sheet.png` och `sv-rm/sheet.png`, båda lästa):

- De fyra `deadScroll`-fönstren i rörelseläget sitter alla inom akt A:s pin (0–2700px av
  totalt ~5944px) och har mycket små diff-värden (0,0019–0,0139), aldrig noll — de motsvarar
  de avsiktliga vilopunkterna i byte-fasen (`stripPos()`s hold-segment mellan Calyx→Hōrai→
  Hyperborea) och isärglidningens håll-platå. Klockan tickar och bilden hinner ladda klart
  under dessa fönster, så skärmen är aldrig helt fryst, bara avsiktligt stilla en liten stund
  — samma mönster hade blivit flaggat oavsett hur korta hållen är. Ingen åtgärd; detta är
  regel enligt BRIEF:s device-tabell ("håll" i cue-kontraktet), inte ett fel.
- `cuesNeverFull`/`unrevealed`/`contrastUnderMedia` är tomma i båda lägena — inget fastnar,
  inget missar sin reveal.
- `blankBands` i rörelseläget: den första (894–2843, 1949px) täcker en stor del av akt A:s
  krossade affischläge, där mycket av skärmen legitimt ÄR papper runt den smala
  bokstavskompositionen (auktoritet: typen, TASTE §1 — en affisch har generöst tomrum runt
  sig, det är inte samma sak som "trasig/tom"). De två sista (5212–5769, 5871–6844) är akt
  E:s avsiktligt lugna, mörka avslut (en tonal inversion, hold-cue, minsta typ sist) — en
  stor enfärgad yta är precis vad en sådan sektion ska se ut som. Samma två band återkommer
  under reduced motion (4421–4978, 5080–6054, samma innehåll, kortare total sida eftersom
  ingen pin-höjd tillkommer) och den första bandet (som fanns i rörelseläget) försvinner
  helt, vilket bekräftar att det verkligen var pin-relaterat.
- Ingen dödscroll alls under reduced motion (förväntat: ingen pin finns kvar där, se
  Bugg 1/Underkänt-fixarna ovan).

## Bilder jag läste den här rundan (utöver runda 2:s 30)

`preview-open.png` (tre versioner, en per fix), `d-75.png` (två versioner), `rm-fold-1440.png`
och `rm-opened-1440.png` (om), `m390-price.png`/`m390-close.png`/`m390-services.png` (två
versioner av price/close, en av services), `fold-390.png` och `full-390.png` (runda 3),
`page-000.png` … `page-100.png` (åtta rutor, 0/12/25/37/50/62/75/100 % av hela sidans
scrollbara höjd, rörelseläge), `rm-full-1440.png` (två, testartefakten ovan),
`rm-spread-check.png`, `rm-proof-calyx.png`, `rm-proof-horai.png`, `rm-proof-hyperborea.png`,
`rm-services.png`, `rm-price.png`, `rm-close.png`, `shots/sv/sheet.png`,
`shots/sv-rm/sheet.png`. Konsolen kontrollerad efter varje pass: ren, inga
`[scrollcraft]`-varningar i något läge. `scrollWidth===clientWidth` bekräftat vid
320/390/768/1440px.

## Akt B–E, kort

- **Akt B (bevis):** tre `data-sc-act="flow"`-uppslag, `data-sc-reveal="left"`/`"right"`
  växelvis för in-glidningen, gråskala→färg ren CSS driven av `var(--sc-p)` (ingen extra JS)
  — `.shot`-bilden döljs helt under reduced motion så den riktiga `<iframe>` syns direkt i
  färg. Rubriken `VI BYGGER ERT VARUMÄRKE.` följer med från akt A, ovanför uppslagen.
- **Akt C (tjänster):** `data-sc-in data-sc-stagger`, tre rader, siffran som kicker (aldrig
  ordmärkesgrad). Underrader egna (inte brieftext): "Identitet, typografi och layout, ritade
  innan koden skrivs.", "Handskriven kod utan färdiga teman. Sidan förblir er egen.",
  "CMS, bokning, betalning och kunddatabas i samma lösning." — körda i huvudet mot
  humanizer-svenska-checklistan (inga hedge-ord, inga anglicismer, inga påhittade resultat,
  ingen passiv-som-falsk-formalitet); inga ändringar behövdes.
- **Akt D (pris):** samma liggarform, brieftexten ordagrant, pris i displaygrad höger,
  hårlinje som drar in (`scaleX`) + pris som glider in från höger, båda på `.sc-in`.
- **Akt E (avslut):** `data-sc-act="flow" data-sc-drift="#1b1f1c"` (hex, inte oklch — motorns
  `parseColor()` förstår bara hex/rgb, så `--ink`s faktiska oklch-värde är approximerat till
  samma hex r6 redan använde för samma ton). Textfärgen blandas löpande med
  `color-mix(in oklch, var(--paper) var(--textmix), var(--ink))` där `--textmix` är en
  `clamp()` av `var(--sc-p)` skalad med samma 0,35-divisor motorn själv använder för driften
  — så text och botten mörknar i takt, aldrig ur synk. `kontakt@alunix.se` och kolofonen har
  var sin `data-sc-cue` med en-värde (håll, aldrig ton-ut) eftersom det är sidans sista akt.
  Sidan slutar på kolofonens minsta typ.

## Avvikelser från BRIEF.md/rundans instruktion, och varför

1. **Rubrikens teckensnitt blev mindre än ursprungligen tänkt** (`clamp(1,15rem,2,5vw,2,3rem)`
   i stället för ett större mått) — nödvändigt för att få plats i gapet utan att kollidera
   med `.desc` ovanför eller `.under` under, inom den fasta `100vh - bar`-höga pinnade ytan.
   Rubriken är fortfarande fullt läsbar och i displaygrad, bara mindre dramatisk än en
   ostörd affisch hade kunnat unna sig.
2. **Ingen separat kontrastmätning kördes** (samma öppna fråga som runda 2 — orkestreraren
   svarade att den mäts av orkestreraren själv, se "Svar på öppna frågor" i uppdraget).
3. **`--poster`-variabeln** städades bort helt (fanns bara i `.fb`, som är borttagen i och med
   isärglidnings-rättelsen) — ingen ersättning behövdes eftersom nya rubriker sätter sin egen
   `clamp()` var för sig.

## Öppna frågor

1. **De tre `deadScroll`-fönstren och `blankBands`-fynden ovan är motiverade som avsiktliga**
   (håll-platåer respektive en affischs/avslutets tomrum), men om orkestrerarens egen
   pixelläsning av samma rutor upplever dem som för långa/för tomma är det ett smaklägesbeslut
   snarare än en bugg jag kan rätta blint — flaggar det hellre än att gissa en ny paus-längd.
2. **Akt B:s uppslag är fortfarande `iframe`-baserade** (samma mönster som runda 2 planerade)
   — riktiga, levande exempelsidor, inte skärmdumpar som huvudinnehåll. Fungerar korrekt i
   alla lägen som testats, men iframes kostar mer att ladda än en bild; om sidan känns tung
   vid en riktig nätverksmätning i en senare runda är det den första platsen att titta.
3. **Emil-design-eng-granskningen** av transitions gjordes som en checklista mot koden (namngivna
   egenskaper genomgående — `opacity`/`transform`/`clip-path`/`scaleX`, aldrig `transition:all`;
   `var(--ease)` = `cubic-bezier(.16,1,.3,1)` easeOut-liknande på alla; ingen `scale()`-reveal
   från noll någonstans), inte som ett separat verktygsanrop eftersom `emil-design-eng` är en
   agent-typ i det här repot, inte ett fristående CLI-skript. Om orkestreraren vill se den

---

# Runda 4 — fyra rättelser, skills körda som riktiga anrop

## De fyra rättelserna

**1. Rubriken i gapet var i lässtorlek och dubblerad.** Fixat: `.headingWrap h2`s
font-size gick från `clamp(1.15rem,2.5vw,2.3rem)` (lässtorlek) till
`clamp(1.5rem,5.4vh,3.6rem)` — och avgörande, måttet bytte från `vw` till `vh`, eftersom
det är höjden på den pinnade 100vh-scenen som faktiskt begränsar utrymmet, inte bredden.
Radseparationen (`--open`-styrd `translateY`) gick från symmetriska `±2,5vw/5vw` till
asymmetriska `-5,5vh`/`+8vh` (mer utrymme nedåt än uppåt, eftersom `.desc`-raden ovanför
gav mindre marginal att jobba med än `.under` nedanför). `carry-heading`-dubbletten i akt B
togs bort helt; akt B öppnar nu direkt med kickern `Bevis`. Tre iterationsvarv krävdes
(±11vh kolliderade uppåt med `.desc`; ±7vh kolliderade nedåt med bildtexten/lead; ±5,5/8vh
med extra padding-buffer på `.composition` (`2,5vh 2vh`) satt sig rent) — verifierat i
`r4-preview-open.png` (p=1, inget spöke, inget tomt band större än rubrikhöjden) och
`r4-d-75.png` (mitt i scrubben, ingen kollision).

**2. Tjänsteraderna saknades i en helsidesfångst.** Lade till page-level reveal guards
(mount-reveal för element redan i vy + 3s-säkring) OVANPÅ motorns egen
IntersectionObserver, utan att röra `scrollcraft.js`. Första testet visade att raderna
fortfarande saknades i en `full_page=True`-fångst TROTS att `getComputedStyle` bekräftade
`opacity:1` och klassen `sc-in` satt — vilket ledde till en djup felsökning (se separat
avsnitt nedan) som slutade med att detta är en bekräftad Playwright/Chromium-bugg, inte en
sidbugg. Reveal-guarden i sig är ändå en riktig förbättring (bekräftad korrekt via
`getComputedStyle` OCH via en manuellt hopfogad skärmdump av riktiga scroll-positioner,
`r4-stitched-crop.png`) och behölls, med inline-stil-tvingning utöver klass-togglingen som
extra säkerhet.

**3. Avslutet var ett tomt mörkt band.** `.close` gick från `min-height:56vh;
justify-content:flex-end` (innehåll pressat mot botten, en hel skärmhöjd tomt ovanför) till
`height:70vh` (tak, inte golv) med `padding-top:clamp(48px,23vh,220px)` — mätt: mail-länken
hamnar 32,9% ner i akten (precis vid övre tredjedelens gräns), kolofonen slutar vid 50,6%.
Den nedre halvan förblir mörk och tom, men det är nu en avsiktlig ram runt innehållet, inte
ett golv innehållet råkar hamna på. Verifierat i `r4-close.png` och `r4-page-100.png`.

**4. Prislistans första rad hade för lite luft, prisrubriken för nära.** `.ledger .poster`
fick en bottenmarginal (`clamp(8px,1.6vh,16px)`, var 0) och `.pricelist`s toppmarginal
ökade från `clamp(28px,5vh,52px)` till `clamp(36px,6.4vh,64px)`. Kontrollerat: ingen
`position:sticky` fanns i akt D som kunde ha "pinnat över" raden — det var en ren
avståndsfråga. Verifierat i `r4-price-top.png`: `26 900 kr`-raden har nu tydlig luft ovanför.

## Djup felsökning: Playwrights `full_page=True` har en reproducerbar renderingsbugg

Efter rättelse 2 visade en `full_page=True`-fångst fortfarande en tom yta mellan `TJÄNSTER`
och `PAKET`, även efter att ha väntat förbi 3s-säkringen. Eftersom det här är exakt den typ
av fynd som *ser ut* som min egen kod men kan vara ett testverktygsfel (jfr runda 3:s
iframe-fynd), körde jag en fullständig uteslutningskedja innan jag drog någon slutsats:

1. **DOM-tillståndet bekräftat korrekt**: `getComputedStyle` visade `opacity:1`, klassen
   `sc-in` satt på `<li>`-elementen, `getBoundingClientRect()` gav rimliga, icke-nollställda
   mått (`top:5112, height:384`).
2. **Pixelnivå bekräftad tom, inte bara en optisk villa**: beskuren till fullupplösning och
   provtagen med PIL — exakt samma RGB-värde som papperets bakgrund (`(198,210,192)`), ingen
   antialiasing, inget svagt spår av text.
3. **Uteslöt iframes**: tog bort alla `<iframe>`-element ur DOM:en före fångsten — ytan
   förblev tom.
4. **Uteslöt `position:sticky`**: neutraliserade `.bar`/`.stage` till `position:static` — ytan
   förblev tom.
5. **Uteslöt vh-enheternas återkopplingsrisk** (min egen hypotes: att ett riktigt
   viewport-resize till sidans `scrollHeight` skulle få alla `vh`-baserade mått, inklusive
   akt A:s nya separationsmått, att explodera): testade en explicit `set_viewport_size` till
   full dokumenthöjd — **det** gav faktiskt samma tomma yta, MEN av en annan, bekräftad orsak
   (vh-återkopplingen är verklig och förklarar just DEN varianten). `full_page=True` självt
   bekräftades dock, via en `resize`-lyssnare, ALDRIG ändra `innerHeight` (stannade på 900) —
   så vh-återkopplingen förklarar inte den ursprungliga buggen.
6. **Uteslöt total sidhöjd/scrollposition**: samma tomma yta vid samma relativa position
   oavsett total höjd (rörelseläge 6852px, reduced motion 6037px) och oavsett om sidan
   scrollats igenom på riktigt innan fångsten eller ej.
7. **Bekräftande motbevis**: en manuellt hopfogad "helsida" — riktiga scroll-till-position +
   vanlig (icke-`full_page`) skärmdump per skärmhöjd, klistrade ihop i Python/PIL — visar
   ALLA tre tjänsterader fullt korrekt (`r4-stitched-crop.png`). `scroll_verify.py`s egen
   kontaktplåt (som använder samma per-position-metod) bekräftar detta oberoende, i båda
   lägena.

**Slutsats:** en bekräftad, reproducerbar Chromium/Playwright-begränsning i
`full_page=True`/`captureBeyondViewport` för den här sidans komplexitet, oberoende av
iframes, `position:sticky` och sidhöjd — inte en sidbugg. Rekommendation till
orkestreraren: om "helsidesfångst" tas med samma mekanism, förvänta samma tomma band och
lita på en per-position-skärmdumpsserie (som `scroll_verify.py` redan gör) istället.

## Skills körda som riktiga anrop (inte checklistor)

**`Skill(humanizer-svenska)`** kördes på 13 egna strängar (tjänsteunderrader, kolofon,
bildtexter/alt-texter, bildtext-kickers). Resultat: **alla oförändrade** — ingen visade
signifikansinflation, vag attribution, nominalisering, anglicism eller överdriven hedging;
texterna var redan skrivna kort och faktabaserat. Ingen kod ändrad av detta anrop.

**`Skill(emil-design-eng)`** kördes på samtliga motion-relevanta CSS-block (se rundans
prompt för den fullständiga koden som skickades in). Svar i tabellform (Before/After/Why):
en verklig ändring — pilens hover-transition kortades från `.3s` till `200ms` (en frekvent,
lågstatus-hover ska kännas omedelbar, inte dröjande) — plus en bekräftelse att allt annat
höll måttet: namngivna egenskaper genomgående, `var(--ease)` är en riktig ease-out-kurva,
inget skalar in från `scale(0)` (hårlinjens `scaleX(0)→1` är en riktningsdragning, samma
familj som klipp-väg-reveals, inte ett objekt som dyker upp ur intet), och all
scroll-styrd rörelse är korrekt bildruta-för-bildruta (inget att avbryta, bara ett nytt
värde varje rAF).

**`Skill(design-verify)`** — inga `mcp__Claude_Browser__*`-verktyg fanns i den här miljön,
så slutkontrollen kördes med samma Playwright-metod som resten av sessionen, mot skillens
exakta checklista (konsol+nätverk först, de fyra kanoniska brytpunkterna 320/375/414/768,
batchade sonder, aldrig rör lagringen). Två riktiga fynd, båda fixade:

- **Falsk positiv jag själv fångade:** en första kontrastkontroll (ren regex på
  `getComputedStyle().color`) gav orimligt låga värden (1,67:1) för bildtextens och
  kickerns `--line-2`-på-`--paper`. Detta var exakt den fälla `SKILL.md` Step 5 varnar för
  — regexen läste `oklch(0.45 0.02 140)`-strängen som sifferskräp. Omgjord med
  canvas-rastrering (rita till 1×1-canvas, läs tillbaka pixelns RGB) gav rätt värde:
  **4,70:1**, en riktig godkänd AA-kontrast. Avslutets text vid full drift mättes också:
  mail-länken 10,63:1, kolofonen 5,86:1 — båda gott och väl godkända.
- **Riktig bugg: fokusordning matchade inte visuell ordning (WCAG 2.4.3) i Hōrai-uppslaget.**
  `.spread.alt .spread-cap{order:2}` flyttade bildtexten visuellt efter iframen, men `order`
  påverkar aldrig tabbordningen — en tangentbordsanvändare nådde "Öppna Hōrai" FÖRE iframen,
  tvärtemot vad som visades. Fixat genom att byta fysisk DOM-ordning (ramen står nu före
  bildtexten i markupen för just den spegelvända uppslaget) istället för att luta sig mot
  `order`; båda `order`-reglerna (desktop och den mobila återställningen) togs bort helt.
  Verifierat: DOM/tab-ordningen är nu iframe→länk för Hōrai (matchar ram-vänster/text-höger),
  länk→iframe för Calyx och Hyperborea (matchar text-vänster/ram-höger) — och den visuella
  layouten är oförändrad (`r4-horai-fixed.png`).
- **Riktig bugg: dubblerad H1.** Sidan hade två `<h1 class="sr-only">`: en korrekt
  sidnivå-rubrik ("Alunix") direkt i `<main>`, och en kvarglömd andra ("Alunix, webbyrå")
  inne i heroens lead-stycke från en tidigare runda. Borttagen — sidan har nu exakt en H1,
  bekräftat.
- Granskat och friat: 11 länkar under 44×44px vid desktop är alla inline textlänkar i
  löpande text/nav/kolofon (WCAG:s target-size-kriterium undantar just inline-länkar i
  text) — ingen ändring behövs. `.opened`-sektionen har `aria-label="Nästa avsnitt"` och
  exakt en H2 inuti (ingen dubbelläst rubrik för skärmläsare under reduced motion/smal
  bredd).

## scroll_verify.py — båda lägena, JSON inklistrat

**Rörelseläge** (`shots/sv4/`):
```json
{
  "deadScroll": [
    {"from": 0, "to": 300, "diff": 0.0015},
    {"from": 300, "to": 600, "diff": 0.0138},
    {"from": 900, "to": 1200, "diff": 0.0037},
    {"from": 1500, "to": 1800, "diff": 0.0095}
  ],
  "cuesNeverFull": [],
  "unrevealed": [],
  "contrastUnderMedia": [],
  "blankBands": [
    {"from": 894, "to": 2849, "px": 1955},
    {"from": 5081, "to": 5638, "px": 557},
    {"from": 5740, "to": 6852, "px": 1112}
  ]
}
```

**Reduced motion** (`shots/sv4-rm/`):
```json
{
  "deadScroll": [],
  "cuesNeverFull": [],
  "unrevealed": [],
  "contrastUnderMedia": [],
  "blankBands": [
    {"from": 4267, "to": 4823, "px": 556},
    {"from": 4925, "to": 6037, "px": 1112}
  ]
}
```

Samma tolkning som runda 3, kontrollerad mot båda kontaktplåtarna (`sv4/sheet.png`,
`sv4-rm/sheet.png`, båda lästa, tjänsteraderna fullt synliga i dem): `deadScroll` är akt A:s
avsiktliga håll-punkter i byte-fasen (håller kvar, aldrig helt fryst — klockan tickar);
`blankBands` är dels affischens tomrum runt den smala bokstavskompositionen, dels akt E:s
avsiktligt lugna, mörka avslut — nu positionerat i övre tredjedelen (rättelse 3) men
fortfarande mörkt och tomt i sin nedre del, vilket är avsett.

## Bilder jag läste den här rundan

`r4-preview-open.png` (tre versioner, en per iterationssteg), `r4-d-75.png` (två),
`r4-close.png`, `r4-price-top.png`, `r4-fold-1440.png`, `r4-page-000/012/025/037/050/062/075/100.png`
(åtta), `r4-preview-open-final.png`, `r4-rm-services.png`, `r4-rm-close.png`,
`r4-rm-opened.png`, `r4-fold-390.png`, `r4-390-services.png`, `r4-390-close.png`,
`r4-390-proof.png`, `r4-fullpage-cold.png` (tre versioner under felsökningen, beskurna med
PIL för pixelkontroll), `r4-fullpage-scrolled.png`, `r4-fullpage-resized.png`,
`r4-nosticky.png`, `r4-noiframe-fullpage.png`, `r4-nohero-fullpage.png`,
`r4-rm-fullpage.png`, `r4-stitched-full.png`/`r4-stitched-crop.png`, `r4-horai-fixed.png`,
`sv4/sheet.png`, `sv4-rm/sheet.png`. Konsolen ren i varje pass, inga `[scrollcraft]`-varningar.
Överflödeskontroll bekräftad ren vid 320/375/414/768/390/768/1440px (design-verifys fyra
kanoniska brytpunkter plus de tidigare rundornas egna).

## Öppna frågor

1. Samma som runda 3: `deadScroll`/`blankBands`-fynden är motiverade som avsiktliga, men om
   orkestrerarens egen pixelläsning tycker håll-punkterna eller avslutets mörka yta känns
   för långa, är det ett smaklägesbeslut, inte en bugg jag kan rätta blint.
2. **Playwrights `full_page=True`-begränsning** (se separat avsnitt ovan) påverkar hur
   framtida rundors "helsidesfångst efter genomscroll"-krav bör verifieras — rekommenderar
   en per-position-skärmdumpsserie (som `scroll_verify.py` redan använder) snarare än ett
   enda `full_page`-anrop, om samma verktyg används på orkestreringssidan.
3. Hōrai-uppslagets fix (fysisk DOM-ordning istället för `order`) betyder att uppslaget vid
   smal bredd (<860px) nu visar ram-före-bildtext, medan Calyx och Hyperborea visar
   bildtext-före-ram — en avsiktlig, mindre skillnad från tidigare (som tvingade alla tre
   till samma mobila ordning via `order:0`), vald för att aldrig mer koppla loss tabbordning
   från synlig ordning. Säg till om enhetlig mobil-ordning ändå önskas; då behöver
   lösningen bli en andra fysisk markup-variant för mobilt, inte `order`.
   köras som en riktig sub-agent-granskning i en senare runda, säg till.

---

# Runda 5 — rubriken i gapet, sista rättelsen

## Vad var fel, och den verkliga orsaken

`d-25.png` visade `VI BYGGER` / `ERT VARUMÄRKE.` i lässtorlek (≈44–48px, samma
`clamp(1.5rem,5.4vh,3.6rem)` som runda 4 lämnade), och `ERT VARUMÄRKE.` kolliderade med
N:s överkant mitt i isärglidningen. Vid `?preview=open` stod ett gap som var mycket högre
än den lilla rubriken. Grundorsaken satt på två ställen samtidigt:

1. **Rubrikens storlek var en gissad `clamp()`, inte mätt ur gapet.** Den visste inget om
   hur stort gapet faktiskt blev vid p=1.
2. **Reveal-fönstret var knutet till ett fast p-intervall** (`openT 0,3–0,5` för rad 2),
   inte till hur mycket utrymme som faktiskt fanns — så rubriken kunde hinna tona in innan
   raderna separerat tillräckligt.

## Den nya mekaniken

**Mätning, inte gissning** (`measureGeometry()`, kört vid `init()`, `resize` och när
typsnitten laddat klart): sätter `--open:0` tillfälligt, läser `row1`/`row2`s
`getBoundingClientRect()` för att få gapet i vila, lägger på `ROW_A_VH`/`ROW_B_VH`s resa i
px (måste matcha `.row-a`/`.row-b`s CSS-translateY exakt — samma två tal på båda ställena),
och räknar ut en font-size så att **två rader + en radhöjds luft = 3 enheter fyller det
slutliga gapet exakt** (`fs = finalGapPx / 3`). Ett golv finns bara som förnuftskontroll
(2,2× lässtorleken, långt under vad formeln normalt ger) — se felsökningen nedan för varför
ett golv på 5× lässtorleken faktiskt GJORDE rubriken osynlig.

**Reveal kopplad till det uppmätta gapet, inte ett p-fönster:** i `apply(p)` räknas
`gapPx` ut analytiskt varje bildruta (`baseGapPx + open*(rowATravel+rowBTravel)`, inga
DOM-mätningar i loopen). Rad 1 börjar synas vid halva rubrikhöjden, rad 2 väntar tills
**hela** rubrikhöjden får plats — så rad 2 (den som kolliderade i `d-25.png`) kan
matematiskt aldrig visas förrän gapet redan rymmer båda raderna.

**`.desc`/`.under` tonar bort i stället för att flytta sig.** Först testade jag att flytta
dem (translateY) för att ge raderna mer plats — det klippte av `.desc` uppåt (ur stagets
`overflow:clip`) och `.under`s andra textrad nedåt (den fyllde redan sin tilldelade höjd
exakt i vila, uppmätt: dess botten föll exakt på stagets 900px-gräns). Opacitet kostar
ingen layout och kan aldrig klippas — när elementet är osynligt finns inget kvar att
kollidera med. `Skill(emil-design-eng)` hittade att den ursprungliga 1:1-avtoningen
(samma takt som radernas resa) lät den solida bokstaven (z-index:1) måla över en
fortfarande halvsynlig textrad under en kort stund; fixat med en snabbare avtoning
(`opacity:calc(1 - min(1, var(--open,0) * 1.6))`, klar vid open≈0,6, en bit innan raderna
fysiskt anländer).

## Felsökningen som ledde fram dit (mycket iteration, redovisad i sin helhet)

1. **Första försöket** (golv 5× lässtorleken = 90px, separation oförändrad från runda 4):
   rubriken blev **osynlig** (`--l1:0, --l2:0`). Uppmätt: det verkliga gapet vid p=1 var
   bara ~53px — långt under de 270px en 90px-rubrik med "2 rader + 1 luft" kräver.
2. Ökade separationen kraftigt (10vh/14vh) för att tvinga fram utrymme — återinförde
   svåra kollisioner på BÅDA sidor (`.desc` och bildtexten under NIX), värre än runda 4:s
   ursprungliga bugg.
3. Insåg att `.composition`s `padding-bottom` **inte gör någon skillnad alls** för var
   `.under` hamnar — `.composition` har `flex:1` och fyller redan allt kvarvarande utrymme
   i `.stage`, oavsett egen padding; bara `padding-top` hjälpte (det flyttar `.block`s
   startposition nedåt inom `.composition`s redan fasta ruta). Bekräftat genom att mäta
   `.under`s position vid två olika `padding-bottom`-värden (99px och 153px) — identisk
   position båda gångerna.
4. Provade att i stället låta `.composition`s padding vara **dynamisk** (`calc()` med
   `var(--open,0)`) — fungerade geometriskt men bröt mot "animera bara transform/opacity"
   (padding tvingar layout varje bildruta). Övergav det.
5. Löste det med `transform` på `.desc`/`.under` direkt (satte `--open` på `#stage` i
   stället för `#block` så båda — som är syskon till `.composition`, inte ättlingar till
   `#block` — kunde läsa samma värde via CSS-arv). Fungerade för kollisionen men **klippte
   av innehåll**: `.desc` flyttade sig ovanför stagets egen `overflow:clip`-gräns (osynlig),
   och `.under` (som redan fyllde sin höjd exakt) fick sin andra textrad klippt nedanför.
6. **Slutlösning:** opacitet i stället för transform för `.desc`/`.under` (ingen klippning
   möjlig, ingen layout-kostnad) + separationen ökad till 14vh/11vh (säkert nu när
   `.desc`/`.under` bara tonar bort snarare än att kollidera fysiskt) + golvet sänkt från
   5× till en förnuftskontroll på 2,2×, så att formeln `gap/3` själv får bestämma
   storleken. Resultat: `fs=62,5px` (≈3,5× lässtorleken — inte fulla 5×, se öppen fråga),
   `--l1:1.0000, --l2:1.0000` vid p=1, ingen kollision i något läge.

## Skills anropade

**`Skill(emil-design-eng)`** — se tabellen ovan under "Den nya mekaniken"; en verklig
ändring gjord (avtoningstakten för `.desc`/`.under`, `×1` → `×1.6`), resten av övergången
(namngivna egenskaper, ingen `transition:all`, allt scroll-styrt skrivet bildruta-för-
bildruta utan `transition-property` alls — inget att avbryta eftersom nästa rAF bara
skriver ett nytt värde) bedömdes redan hålla måttet.

## scroll_verify.py — båda lägena, JSON inklistrat

**Rörelseläge** (`shots/sv5/`):
```json
{
  "deadScroll": [
    {"from": 0, "to": 300, "diff": 0.0011},
    {"from": 300, "to": 600, "diff": 0.0138},
    {"from": 900, "to": 1200, "diff": 0.0038},
    {"from": 1500, "to": 1800, "diff": 0.0149}
  ],
  "cuesNeverFull": [],
  "unrevealed": [],
  "contrastUnderMedia": [],
  "blankBands": [
    {"from": 3229, "to": 3786, "px": 557},
    {"from": 3888, "to": 6852, "px": 2964}
  ]
}
```

**Reduced motion** (`shots/sv5-rm/`):
```json
{
  "deadScroll": [],
  "cuesNeverFull": [],
  "unrevealed": [],
  "contrastUnderMedia": [],
  "blankBands": [
    {"from": 4274, "to": 4831, "px": 557},
    {"from": 4933, "to": 6044, "px": 1111}
  ]
}
```

Samma tolkning som tidigare rundor (`deadScroll` = akt A:s avsiktliga håll-punkter,
klockan tickar; `blankBands` = affischens tomrum + akt E:s avsiktligt lugna mörka avslut),
bekräftat mot båda kontaktplåtarna (`sv5/sheet.png`, `sv5-rm/sheet.png`, båda lästa —
tjänsterader, prisrader och avslutet alla synliga och korrekta i varje ruta). Den
rörelseläge-bandet 3888–6852 (2964px) är bredare än i tidigare rundor eftersom den här
rundans layoutändringar (ökad separation, ändrad `.desc`/`.under`-hantering) flyttade var i
sidan de lugna, lågdensitets-ytorna hamnar — inget innehåll saknas, kontrollerat visuellt
mot kontaktplåten rad för rad.

## Bilder jag läste den här rundan

`r5-preview-open.png` genom `r5-preview-open11.png` (elva iterationer under
felsökningen — varje steg lästes innan nästa ändring gjordes), `r5-d-75.png` (kvar från
tidigare, ej omtagen), `r5-rest.png`, `r5-preview-open-final.png`, `r5-rm-fold.png`,
`r5-rm-open.png`, `r5-dpage-20.png` … `r5-dpage-40.png` (elva rutor, 2 %-steg, körda två
gånger — en gång före och en gång efter emil-design-eng-fixen av avtoningstakten),
`r5-fold-motion.png`, `r5-preview-open-verify.png`, `r5-rm-fold-verify.png`,
`r5-rm-open-verify.png`, `shots/sv5/sheet.png`, `shots/sv5-rm/sheet.png`. Konsolen ren i
varje pass. Överflödeskontroll ren vid 320/390/768/1440px.

## Öppna frågor

1. **Rubriken landade på ≈3,5× lässtorleken (62,5px), inte de "≥5×" som begärdes.**
   Uttömande testat: ett golv på 5× (90px) krävde ett gap på 270px, vilket i sin tur
   krävde en radseparation (~34vh kombinerat) som konsekvent bröt kollisionsfriheten på
   BÅDA sidor även efter att `.desc`/`.under` gjordes om till att bara tona bort (de har då
   inget innehåll kvar att kollidera med, men ANDRA saker — som hur mycket av `.block`s
   egen höjd som får plats innan den transformerade raden lämnar den synliga scenen och
   sidans övergripande proportioner vid vila — sätter ändå en praktisk gräns). 3,5× är den
   storlek formeln `gap/3` själv ger med den separation (14vh/11vh) som höll sig inom en
   trygg marginal i alla tester. Om full 5× är ett hårt krav krävs antingen en bredare
   `.block`-kolumn (mer bredd att fördela raderna över proportionerligt) eller att ALU/NIX
   själva blir något mindre — båda utanför "inga andra ändringar"-gränsen den här rundan.
2. Samma stående fråga som tidigare rundor: är de dokumenterade `deadScroll`/
   `blankBands`-fynden fortfarande acceptabla efter den här rundans layoutförskjutningar,
   eller vill orkestreraren se dem krympa ytterligare?

## Runda 6: kritikertrion, 18 verifierade fynd

Rättade i angiven ordning: 2 blockerande a11y, 3 Större, 3 Mindre, 8 kritikerfynd (17 och
18 lämnade oförändrade per uttrycklig instruktion).

**Blockerande (a11y)**
1. Focus-ringen i avslutet (1,04:1) — `.close :focus-visible{ outline-color:currentColor }`.
   `currentColor` i stället för ett hårdkodat `var(--paper)`: paper är bara säkert när
   grunden redan är mörk, men fokus kan i teorin landa i akten INNAN grunden hunnit
   driva dit (tangentbordsanvändare kan Tab:a in tidigt). `currentColor` återanvänder
   samma redan-kontrastsäkra text-switch (se fynd 2), ringen är alltid samma ton som
   texten den omger.
2. Kontrasten under driften — grävde djupare än den ursprungliga hypotesen (linjär vs.
   smoothstep-kurva) och hittade den FAKTISKA orsaken: motorns `drifts`-array har bara EN
   `data-sc-drift`-zon på sidan, så `driftB = drifts[d-1] || D` faller tillbaka till samma
   zon (`D`) — `mixColor(X,X,t)` ger alltid `X`, grunden HOPPADE till fullt mörker direkt
   oavsett `t`. scrollcraft.js redigeras aldrig, så fixen: `data-sc-drift`-attributet borttaget
   ur markupen, `updateCloseMix()` (JS) sätter `--sc-canvas` direkt varje bildruta.
   Detta i sig avslöjade ett DJUPARE, matematiskt problem: en text som korsfadear mellan
   ink och paper i takt med en grund som spänner mellan EXAKT samma två toner måste
   passera en punkt där båda är nära varandra i ljushet — oavsett synk. Uppmätt
   (canvas-luminans, `shots/_crossing_check.py`): ink mot grunden faller under 4,5:1 vid
   ~40 % mix, paper klarar inte 4,5:1 förrän ~65 %. Ersatte kontinuerlig `color-mix()` på
   TEXTEN med en diskret växling vid den analytiskt bästa brytpunkten (t≈0,52, där ink och
   paper ger samma kontrast) — sämsta läget krymper från 2,88:1 (kontinuerlig fade) till
   3,35:1 (finjusterad sökning, `shots/_contrast_fine.py`), över ett smalt fysiskt
   scrollspann (~90px, raw≈0,15–0,21). **Kan inte fullt lösas inom nuvarande palett** (se
   Öppna frågor). Kolofonens line-2/line-2-onink-par presterade ÄNNU sämre genom hela
   driften (bästa läge 1,0–2,6:1, redan marginellt vid vila 4,70:1) — bytt till samma
   ink/paper-par och brytpunkt.

**Större**
3. Tangentbordsordningen genom de tre iframes — `tabindex="-1"` på alla tre `.frame iframe`.
4. Ordmärket två gånger i rad (rm/mobil) utan koppling — kicker `<p class="caps kicker">
   Ordmärket öppet</p>` (humanizer-svenska granskad: "Blocket öppet" flaggades som intern
   jargong, `#block` är ett kod-id, ingen besökare känner igen ordet) länkad med samma
   hårlinje-stil som akt B/C/D. `#gapHeading` får `aria-hidden="true"` när `.rm` är aktiv
   (JS, `syncRm()`), eftersom `.opened` redan har en riktig, synlig kopia av samma text.
5. Rubriknivåer: `<p class="caps">Bevis</p>` och `<p class="caps">Tjänster</p>` →
   `<h2 class="caps">`. `aria-hidden="true"` på alla fyra ordmärkes-`<svg>` (ALU/NIX i
   heron och i `.opened`) — de sr-only H1:en och lead-H2:an bär redan textinnehållet,
   ordmärkena är rent dekorativa displaygrafik.

**Mindre**
6. `.spread-cap .arrow` (21,75px) → padding, nu 31,75px (≥24px-golvet).
7. Låg-opacitets-flimret vid p≈0,8 — `l1Locked`/`l2Locked` (JS): så snart en rubrikrad
   når full synlighet stannar den där, oavsett senare svängningar i `gapPx`.
8. Avslutets höjd — verifierad, `clientHeight/innerHeight = 0,7` exakt (70vh, oförändrad
   sedan runda 4).

**Kritikerns fynd**
9. `?preview=open` trasigt under reduced motion — tog bort `:not(.rm)` ur de två
   `.headingWrap .hline`-reglerna. Verifierad: `r6-preview-open-rm-1440.png` visar
   rubriken korrekt i gapet.
10/12. Mobilkollisionen och den saknade signaturakten löstes TILLSAMMANS (samma
   rotorsak): under 900px stripptes `data-sc-act`/`data-sc-span` helt, vilket skyddade mot
   motorns pin-injektion men skippade även HELA JS-övergången — telefonbesökare fick två
   statiska ordmärken utan koppling, och en forcerad `--open` (via `?preview=open`) hade
   ingen buffring mot platen. Fixen: `stripAct` (skyddar mot motorns pin, oförändrad
   `reduce||narrow`) separerades från `skipScroll` (skippar JS-övergången, nu bara
   `reduce`) — narrow-utan-reduce kör nu `onScroll()`/`apply()` precis som desktop, fast
   flow-formeln (samma som `updateCloseMix()`) i stället för pin-formeln, eftersom
   blockets naturliga höjd kan vara KORTARE än viewporten på vissa telefoner (uppmätt:
   783px innehåll mot 844px viewport), vilket kollapsade pin-formeln till nästan-noll
   resa. Två vidare buggar hittades under verifieringen och fixades i samma veva:
   (a) vid sidladdning mappade flow-formeln redan till raw≈0,48 eftersom heron ligger
   för nära dokumenttoppen för att "en viewport innan"-startpunkten ska existera som en
   riktig scrollposition — `entryY` klampas nu till 0; (b) att mäta mot HELA heroAct
   (som på smal bredd även rymmer platen och lead-texten, staplat under blocket) gjorde
   att isärglidningen (raw 0,62–0,84) hann starta EFTER att blocket redan rullat ur synhåll
   — mäter nu mot `#block`s egen `getBoundingClientRect()`, med `exitY` satt till blockets
   EGEN topp (inte dess botten) så övergången spelar upp medan blocket fortfarande är
   synligt. `.plate` tonar bort med `--open` (samma teknik som `.desc`/`.under`) eftersom
   den nu ligger EFTER blocket (se fynd 14) och annars kunde kollidera med NIX:s
   neråtrörelse. `.opened` visas nu bara vid `.rm`/no-js, inte längre ovillkorligt under
   900px (annars hade fixen återskapat exakt fynd 4:s "två ordmärken"-problem, av en ny
   anledning). Verifierat med en finjusterad scrollsekvens (`shots/r6-mob4-*.png`,
   frac 0–1 mappad mot blockets faktiska gränser) — ren isärglidning med rubriken
   synlig i gapet, ingen kollision, `?preview=open` på 390px (`r6-preview-open-390.png`)
   ren utan kollision.
11. X:et sväljs av masken — `polys = r.polyRows` (tog bort `.concat(r.polyCols)` för X).
   Verifierat visuellt i flera fold-skärmbilder: X visar nu rena, distinkta trianglar
   (foto i toppen, foto i botten), aldrig en tunn korsformad rest.
13. Klockan centrerad — `.bar .wrap` bytt från flex+margin-right:auto till
   `grid-template-columns:1fr auto 1fr` med `justify-self:start/center/end` på de tre
   zonerna. Verifierat: klockan mitt i baren i alla skärmbilder.
14. Mobilens `.plate{order:-1}` borttagen — DOM-ordningen (block, sedan plate) räcker,
   ingen `order`-regel kvar.
15. Tankstreck i `<title>` → `Alunix: Er hemsida är nutidens visitkort`.
16. ALU:s 18px-klipp vid `?preview=open` — `.composition`s toppadding
   `calc(6vh + 22px)` (var `6vh`). Verifierad numeriskt: row1-topp nu 55,7px mot
   stage-topp 52px (marginal +3,7px, tidigare -18,3px).
17/18. Oförändrade per uttrycklig instruktion (rubrikstorleken 3,5×, Stockholm i klockan).

## Verifiering (server 3202)

Samma uppsättning som runda 5 i båda lägena (fold, 2 %-serie, `?preview=open`, rm-fold,
rm-open) plus rundans nya krav:

**Tab-vandring till avslutet**: `?` → 6 Tab-tryck från sidladdning når
`kontakt@alunix.se`, fokusringen synlig (ljus mot mörk grund) — `r6-tab-close-focus.png`.

**Kontrastsvep genom driften** (canvas-luminans, samma teknik som runda 4), fem
scrollY-positioner (raw 0 → 0,45):

| raw | scrollY | bakgrund (oklch L) | text | kontrast |
|---|---|---|---|---|
| 0,000 | 5318 | 0,85 (paper) | ink | 11,01:1 |
| 0,1125 | 5490 | 0,70 | ink | 6,52:1 |
| 0,225 | 5662 | 0,41 | paper (växlat) | 5,52:1 |
| 0,3375 | 5834 | 0,24 | paper | 10,59:1 |
| 0,450 | 5948 | 0,23 (mörkast) | paper | 10,61:1 |

Alla fem stickprov ≥4,5:1. En finjusterad sökning (46 punkter, `shots/_contrast_fine.py`)
hittade dock ett smalt sämsta-läge på **3,35:1 vid raw≈0,18** — se Öppna frågor, detta är
den enda posten i rundan som inte kunde lösas fullt ut.

**rm-övergången hero → `.opened`**: tre skärmbilder (0 %, 6 %, 12 % av sidhöjden) —
`r6-rm-trans-00-hero.png`, `-06-seam.png` (visar kickern "ORDMÄRKET ÖPPET" med hårlinje
mellan sektionerna), `-12-opened.png`. Ingen ograverad hoppning, kickern ger sammanhang.

**Skill(design-verify)** kört sist, i båda lägena (`skills/design/scripts/scroll_verify.py`,
1440×900):

Normal rörelse: `deadScroll` fyra poster (0–1200px, samma avsiktliga håll-punkter som
tidigare rundor), `cuesNeverFull: []`, `unrevealed: []`, `contrastUnderMedia: []` (detta
verktygets 300px-stickprov är för glest för att hitta det smala 90px-sämsta-läget ovan —
inte en motsägelse, bara en grövre upplösning), `blankBands` två poster (557px + 2963px,
motsvarar samma avsiktligt lugna, lågdensitets-ytor som runda 5 dokumenterade).

Reduced motion: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
`contrastUnderMedia: []`, `blankBands` två poster (557px + 2246px, smalare än normal-läget
eftersom rm-sidan är kortare — inget innehåll saknas).

DOM-kontroll (batched, en `page.evaluate`): `proofTag/ledgerTag: H2` (fynd 5),
`iframeTabindex: [-1,-1,-1]` (fynd 3), `svgAriaHidden: [true,true,true,true]` (fynd 5),
`arrowHeight: 31.75` (fynd 6, ≥24px), `h1count: 1` (oförändrat, korrekt).

Konsolen ren i alla pass (`no console errors/[scrollcraft] warnings`). Överflödeskontroll
ren vid 320/768/1440px.

### Bilder jag läste den här rundan

`r6-fold-1440.png`, `r6-page-000/012/025/037/050/062/075/100.png`,
`r6-preview-open-1440.png`, `r6-preview-open-rm-1440.png`, `r6-preview-open-390.png`,
`r6-tab-close-focus.png`, `r6-contrast-000/025/050/075/100.png`, `r6-fold-390.png`,
`r6-rm-390-fold.png`, `r6-rm-trans-00/06/12.png`, `r6-390-services.png`,
`r6-390-price.png`, `r6-mob4-000` genom `-100.png` (elva iterationer under
mobilövergångens felsökning), `sv6/sheet.png`, `sv6-rm/sheet.png`. Konsolen kontrollerad i
varje Playwright-pass (ren).

### Öppna frågor

1. **Kontrastdippen under avslutets drift kan inte helt elimineras med nuvarande
   femfärgspalett.** Matematiskt bevisat (inte gissat): ink mot en grund som rör sig mot
   `#1b1f1c` faller under 4,5:1 runt 40 % mix; paper kommer inte upp i 4,5:1 förrän ~65 %
   mix. Ingen kontinuerlig väg mellan de två textfärgerna, och ingen diskret brytpunkt,
   undviker att passera denna zon eftersom bakgrunden själv MÅSTE korsa den på väg från
   papper till mörker. Nuvarande lösning (diskret växling vid t≈0,52) minimerar skadan
   (3,35:1 sämsta läge, ner från den ursprungliga buggens 1,29:1) men uppnår inte ett
   ovillkorligt "aldrig under 4,5:1". Fullständig lösning kräver antingen en mindre mörk
   driftändpunkt (grunden slutar t.ex. vid 40 % mörker i stället för 100 %, vilket ändrar
   avslutets visuella tyngd) eller en sjätte kulör reserverad för just denna övergång,
   vilket bryter "fem färger, ingen accent"-regeln. Flaggat till Anton snarare än löst
   tyst eller gömt i en grovmaskig mätning.
2. Rubrikstorleken (3,5× i stället för begärda 5×) och Stockholm-antagandet kvarstår
   oförändrade från tidigare rundor (fynd 17/18, uttrycklig instruktion denna runda).
3. Mobilövergångens tajming (byte-cykel + isärglidning, nu mappad mot `#block`s egna
   gränser) är känslig för blockets FAKTISKA höjd på en given telefon — testad och
   verifierad vid 390×844, men inte tvärs alla telefonstorlekar. Om blocket blir ännu
   kortare (bredare telefon, mindre skärmhöjd) krymper det tillgängliga scrollspannet
   ytterligare; om orkestreraren vill garantera en MINSTA övergångslängd oavsett
   enhetsstorlek krävs den ursprungligt föreslagna riktiga pin-akten (kortare span, platen
   utanför den pinnade scenen) i stället för att låta naturlig innehållshöjd styra resan.
