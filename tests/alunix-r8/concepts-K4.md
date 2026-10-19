# Alunix r8 — målbildsgrind, cell K4

Skriven av arkitekten 2026-09-09/10. Denna fil äger **bara** K4. Lead slår ihop V3c, K3 och
K4 till `concepts.md`; den här filen skrivs aldrig in i den av mig.

Målbilden är `tests/alunix-r8/malbilder/K4.md` (planens § 7.5, ordagrant) och den är
utgångspunkten. Varje avvikelse står utskriven med källa i § (4) *Vad jag bytte i planen*.

---

## catalogue-select

`python scripts/catalogue/sweep_raw.py` kördes om av mig innan urvalet:

```
sweep: rent - varje kalla under raw/ och processed/ har en post (0 ignorerade).
EXIT=0
```

`python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K4/BRIEF-draft.md --k 4 --wildcard --explain`,
hela utdatan ordagrant:

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

**Avvikelse mot målbildens förväntan, mekaniskt kontrollerad i `index.json`.** Till skillnad
från K3 föll **tre av fem** förväntade slugar faktiskt ut: `paper` (14, högst av alla),
`harkcap` (12) och `mode` (12). Två föll bort. Poängen nedan är körda med samma funktioner
som skriptet självt (`select.score` mot samma brief och samma `prior_primaries`), inte
uppskattade:

| Förväntad slug | Poäng | Registerfält i `index.json` | Varför den föll bort |
|---|---|---|---|
| `paper` | **14** | `modern clean` · `split stage` · `product-focused` / `editorial` | Föll inte bort. Högsta poäng i hela katalogen mot den här briefen. Primär referens |
| `harkcap` | **12** | `modern clean` · `split stage` · `institutional` | Föll inte bort |
| `mode` | **12** | `modern clean` · `split stage` · `product-focused` / `editorial` | Föll inte bort |
| `future-fur` | 11 | `modern clean` · `split stage` · `consumer-brand` | **Ett poäng under k=4-strecket.** Fyra poster ligger på 12 eller mer, så `--k 4` skär av vid 12. Den var dessutom kandidat till wildcard-platsen (kategorin `consumer-brand` ligger utanför briefens `portfolio`), men wildcard-slingan går igenom `ranked` som är sorterad `(-poäng, slug)`, och vid oavgjort 11 kommer `customer-io` före `future-fur` alfabetiskt. Den föll alltså på en bokstav, inte på en princip |
| `dovetail` | 8 | `editorial print` · `split stage` · `institutional` / `editorial` | **Sex poäng under strecket.** Registret är `editorial print`, inte `modern clean`, så den tappar hela `+3 register`; kategorierna är `institutional` / `editorial` mot briefens `portfolio` / `product-focused`, så den tappar hela `+2 category`. Den fick `+3 grammatik | +1 mode | +4 fritext (accent, flat, nav, pill)`. Målbilden låser själv `modern clean`, alltså är det målbildens eget lås som stänger ute den |

**Skillnaden mot K3 är värd att notera:** K3:s förväntade lista föll helt, K4:s föll till 60 %
rätt. Orsaken är att K4:s målbild deklarerar `split stage`, vilket är en ovanlig grammatik i
katalogen, medan K3:s `chaptered editorial` är den vanligaste. Ingen av K4:s förväntade slugar
ligger i `OWN_SITES` (det var K3:s problem), så den mekanismen spelar ingen roll här.

`catalogue-first.md` § 5 gör skriptets rad till den referensgolvet läser. **De fem valda
posterna är cellens låsta referenser.** `future-fur` och `dovetail` får ingen rad i
reference-locken och ingen rad i § (7) — en referens som inte är vald får inte styra bygget.
Frågan om planens förväntningslista ska rättas ligger som **Q11** i `QUESTIONS.md`.

---

## Lästa referenser

Tre rader per fil: vad den gör · vad jag tar · vad jag lämnar.

**Vad jag faktiskt öppnade som pixlar** (jag redovisar det exakt i stället för att påstå
fullständighet): `fold.webp` för alla fem posterna, plus `paper/slices/00, 03, 06, 09`,
`harkcap/slices/02, 04, 08, 11`, `mode/slices/05`, `gocanopy/slices/04`,
`customer-io/slices/03`. Övriga slices är inte lästa och ingen digest nedan påstår något om
dem. Texten är läst i sin helhet för alla fem `entry.md` inklusive § Motion och
§ Reference lock, samt `extract/*-design-language.md` § Motion Language och § Material Language
för alla fem.

### paper (primär, 14 poäng)

- `entry.md` (hela, inkl. § Motion och § Reference lock) — bygger hela sidan på **tvåtons\
  rubriken**: identiska Matter-metriker (samma grad, samma vikt 400, samma tracking) delade på
  två fyllnadsfärger, bläck `#181818` på första raden och skiffer `#83837e` på fortsättningen,
  och posten är uttrycklig om att blanda grader eller snitt mellan raderna förstör devicen.
  Den enda kromatiska accenten, studioblått `#5d8cd7`, är inhägnad till märket och
  kodsyntax — aldrig en knapp, aldrig en länk, aldrig stor text — och den fyllda CTA:n är
  alltid neutralt bläck. Trelagersskuggan är reserverad **enbart** för produktskärmbilden;
  marknadsföringskort hålls platta med 1 px hårlinje.
  **Tar:** tvåtonsdevicen ordagrant som foldens rubrikform, och inhägnadsprincipen flyttad ett
  hack: K4:s enda kromatiska värde bor på **ett enda geometriskt objekt**, delaren, som
  samtidigt är sidans nav, dess chrome och dess signatur.
  **Lämnar:** krämkanvasen (K4:s papper är varmt men inte kräm), radie 4/8/12–24 px (K4 kör
  radie 0), trelagersskuggan helt (K4 har noll `box-shadow`), och det isometriska
  linjerastret i hörnet.
- `fold.webp` (pixlar) — krämgrund, ordmärke vänster med fem gemena textlänkar och `sign up`
  höger; rubriken vänsterställd i tre rader där rad 1 är bläck och rad 2–3 är skiffer; en
  fylld mörk knapp bredvid en spöklänk; under folden ett elevat produktfönster med
  trafikljusprickar, filträd och egenskapspanel; ett svagt isometriskt raster i övre höger.
  **Tar:** att rubrikens tvåtonsbrytning ligger på en *semantisk* gräns, inte en radbrytning.
  **Lämnar:** hela topplänkraden, den fyllda knappen, trafikljusprickarna (gate 47).
- `slices/00, 03, 06, 09` (pixlar) — 00 är folden med de tre mobilartboardsen synliga inne i
  produktfönstret; 03 och 06 visar samma produktfönster i två tillstånd med en överlappande
  terminalpanel och en macOS-liknande dock; 09 är avslutet: två textkolumner med `build log →`
  och `read the announcement →`, sedan en footer där ordmärket `Paper` ligger i jättegrad som
  ett nästan osynligt präglat lager bakom `© 2026` och `team@paper.design`.
  **Tar:** avslutets form — sidan slutar på en textrad och en adress, inte på en CTA-remsa.
  **Lämnar:** det präglade jätteordmärket i footern, docken, och hela produktfönstret
  (K4:s "produktfönster" är två riktiga sajter, inte ett ritat).
- `extract/paper-design-design-language.md` — Motion Language: feel `springy`, scroll-linked
  `yes`, fyra varaktigheter 100/300/500/800 ms, en snabbt avtagande `cubic-bezier(0.16,1,0.3,1)`
  i 32 bruk och en äkta overshoot `cubic-bezier(0.34,1.3,0.64,1)` i 5 bruk. Material Language:
  `flat`, avg saturation 0,226, shadow blur 0 px, max radie 9999 px, `backdrop-filter` nej,
  6 gradienter.
  **Tar:** `cubic-bezier(0.16,1,0.3,1)` som cue-kurva; den är rätt familj för ett kritiskt
  dämpat system. **Lämnar:** overshoot-kurvan helt (spring damping 1,0 betyder per definition
  ingen översläng), radie 9999 px, och de sex gradienterna.

### harkcap (sekundär, 12 poäng, `split stage`)

- `entry.md` — låter **ett enda renderat objekt** bära hela auktoriteten och håller rubriken
  liten i förhållande till det; kör hela sidan på en grotesk i alla grader så att typen aldrig
  konkurrerar; återvänder till heroобjektets exakta material **en gång**, för talen
  (2013 / $2.1B+ / 70+ / 4 lagda över en närbild av samma glas); och håller lagets identitet
  **undanhållen tills hover** — en lista med grå namn där raden under pekaren blir helsvart och
  ett porträtt tonar in bredvid. Postens egen § What to leave är hård mot sig själv: objektet
  "carries no explicit metaphor tied to NAV financing".
  **Tar:** undanhållandet som princip, flyttat från pekare till berättelse — K4 undanhåller
  inte identiteten hos en person utan **halva argumentet**: "efter"-sidan finns hela tiden på
  skärmen men blir inte hel förrän delaren passerat.
  **Lämnar:** 3D-renderingen (K4 har noll genererat material), talen över glaset (Alunix har
  inga sådana tal, PRODUCT.md § absences), hela laget, och `Click to Expand`-navet.
- `fold.webp` (pixlar) — nästan hela viewporten är ett blågrått glasblock i studioljus;
  ordmärket uppe till vänster, en halvgenomskinlig blå navpanel uppe till höger med
  `+ Click to Expand` och tre länkar, och rubriken `Pioneers in NAV financing` i vitt, lågt
  till vänster, satt **litet** mot objektet.
  **Tar:** proportionen — objektet stort, typen liten. K4:s objekt är två sajter, typen är en
  rad. **Lämnar:** hela panelnavet, glaset, den blå duotonen.
- `slices/02, 04, 08, 11` (pixlar) — 02: vit yta, två grå knappkort (`Our Story`, `Our Solutions`),
  en prickmärkt kicker `● Core Stats` och sedan statbandet lagt direkt på glasnärbilden;
  04: hover-listan med tolv namn i ljusgrått, `Emily Oppenheimer` i helsvart och ett porträtt
  centrerat över listan; 08: nyhetslistan med `News`/`Insights`-chips, datumrader och pilar,
  plus ett mörkblått fyllt kort `Explore More News & Insights`; 11: avslutet, glaset igen och
  sedan en helsvart footer i tre kolumner.
  **Tar:** exakt en sak — att en **lista med hårlinjer mellan raderna** kan bära ett helt
  avsnitt utan ett enda kort. K4:s skillnadsliggare är samma form.
  **Lämnar:** chipsen, det fyllda blå kortet, den svarta footern, porträtten.
- `extract/harkcap-com-design-language.md` — Motion: feel `smooth`, scroll-linked `yes`,
  varaktigheter 1 ms / 200 ms / 300 ms, nästan allt på ren `ease` (186 bruk), plus
  `--transition-smooth: all 400ms ease-out`. Material: `flat`, avg saturation 0,32,
  shadow profile `none`, 0 gradienter, `backdrop-filter` nej.
  **Tar:** `shadow profile: none` och `0 gradienter` som bevis på att ett tungt visuellt hero
  inte behöver ett enda djupknep under sig. **Lämnar:** `transition: all` (uttryckligen
  förbjuden i `performance.md`), och 1 ms-tillståndet.

### mode (sekundär, 12 poäng, `split stage`)

- `entry.md` — inhägnar accenten till **exakt en komponenttyp** ("the only filled button
  color in the system"), låser serifen till 36 px och uppåt i en enda vikt, ökar den negativa
  trackingen med graden (−0,72 px till −2,98 px), delar radien i exakt två roller (4 px
  klickbart, 16 px innehållande) och bygger djup ur en färgstack sage → forest → chartreuse
  i stället för skugga.
  **Tar:** inhägnadsprincipen, skärpt från komponent till **objekt**: `#1E5E9C` finns bara på
  delaren, och delaren är ett objekt som existerar exakt en gång på sidan. En komponentregel
  kan drifta när en ny komponent uppstår; ett objekt som bara finns en gång kan inte drifta.
  Tar också regeln att tracking skärps med graden.
  **Lämnar:** färgstacken, serifen, chartreusen, båda radievärdena, och `Signature move`
  (det mörkgröna statkortet med `8.2K`) helt: det är ett kort, och talet är inte Alunix.
- `fold.webp` + `slices/05` (pixlar) — mörkgrön grund, en vit navpanel med två pillknappar
  ovanpå; rubriken satt i tre överlappande chartreusegula pratbubbleformer; ett dokumentärt
  teamfoto och ett skärmfoto under; ett mörkgrönt statkort `8.2K ▲12.16%` med ett stapeldiagram;
  05 visar en isometrisk lagerillustration med färgkodad teckenförklaring
  (`TRANSFORMATION` / `WAREHOUSE` / `INGESTION` / `RAW DATA`) och därunder en logotypvägg
  (Atlassian, Bloomberg, Canva, Imperfect, Zillow).
  **Tar:** ingenting av kompositionen. **Lämnar:** bubbelformerna, teamfotot, statkortet,
  stapeldiagrammet, logotypväggen — hela raden är PRODUCT.md § absences.
- `extract/mode-com-design-language.md` — Motion: feel `springy`, `ease` 102 bruk, fem
  varaktigheter 150 ms–1 s, en overshoot `cubic-bezier(0.75,0,0.29,1.01)` i 3 bruk, en
  `scroll`-keyframe (marquee). Material: `flat`, avg saturation 0,425, max radie 50 px,
  1 gradient. Design System Score-anmärkningar: "4 font families", "75 % av CSS oanvänd".
  **Tar:** varningen mot fyra typsnittsfamiljer — K4 kör två, roller som aldrig korsas.
  **Lämnar:** overshoot, marquee (Hyperborea äger den i registret), och radie 50 px.

### gocanopy (sekundär, 12 poäng, ny mot målbildens lista)

- `entry.md` — duotonar en kategoridefault-bild (skyline) i produktens egen accentfärg så att
  ett välkänt auktoritetsmotiv dras in i varumärkets palett; använder en mono **enbart** för
  system-status-etiketter i versal och öppen tracking; gör hero-videon **klick-för-att-spela**
  i stället för autoplay; och bryter från heroets mörka fotografiska register till en ljus,
  ren sektion för processförklaringen, med motiveringen att stämning och klarhet är olika jobb.
  Signature move: att **rama in rubriken med två små monoetiketter**, en ovanför som anger
  publiken och en under som anger det tekniska påståendet, så att meningen flankeras av
  maskinröst i stället för att stöttas av en underrubrik.
  **Tar:** inramningen, roterad 90°. K4:s två monoetiketter `Före` och `Efter` sitter till
  **vänster och höger** om rubriken i stället för över och under, så att metadata namnger de två
  halvorna i stället för att flankera ett påstående. Det är exakt två monoetiketter på hela
  sidan, vilket håller målbildens tak (≤ 4).
  **Lämnar:** duotonen, skylinen, videon, den klibbiga annonsremsan, pillnavet.
- `fold.webp` + `slices/04` (pixlar) — folden är ett skymningsfoto av Chicagos skyline under
  en teal duoton, med ett flytande pill-nav i toppen, en outlinad monoetikett
  `PURPOSE-BUILT FOR INSTITUTIONAL REAL ESTATE INVESTORS`, en serifrubrik i två rader, en andra
  monoetikett `AI-NATIVE FROM DAY ONE`, och ett videokort med `Click to play`; nederst en
  neongrön annonsremsa. 04 visar en mörkgrön sektion med rubriken `Evidence from institutional
  investors` centrerad och ett svagt kort med `Decision-ready intelligence`.
  **Tar:** ingenting av kompositionen. **Lämnar:** duotonen, pillnavet, annonsremsan, videon,
  och den centrerade rubriken (split stage förbjuder centrerad copy uttryckligen).
- `extract/gocanopy-tech-design-language.md` — Motion: feel `responsive`, scroll-linked `yes`,
  tre varaktigheter 150/300/500 ms, `cubic-bezier(0.4,0,0.2,1)` (8 bruk) för färg och
  `cubic-bezier(0,0,0.2,1)` (16 bruk) för transform/scale/rotate, **noll keyframes** i
  stilmallen. Material: `flat`, avg saturation 0,384, shadow blur 0 px, max radie 16 px,
  0 gradienter.
  **Tar:** uppdelningen — en kurva för färg, en annan för förflyttning. K4 använder samma
  uppdelning: cue-opacitet får `cubic-bezier(0.16,1,0.3,1)`, delarens fjäder är kritiskt
  dämpad och har ingen bezier alls. **Lämnar:** radie 16 px.

### customer-io (wildcard, `live surface`, utanför kategorin)

- `entry.md` — låter rubriken göra varumärkesarbetet genom att färga om enstaka ord i
  produktens accentpalett; **iscensätter produktskärmbilden inne i ett fotograferat rum**
  (dashboard på ett verkligt skrivbord med växter och dagsljus) för att låna ett livsstilsfotos
  trovärdighet åt en skärmbild; svarar på invändningar i tre små bockar under CTA:n; och visar
  två produktytor i samma skärmbild för att hävda en andra förmåga utan ett andra hero.
  **Tar:** exakt en sak, som **avvisning**. Postens signaturdrag är att *låna* trovärdighet åt
  en skärmbild. K4 behöver inte låna någon: produkten körs live i ramen och går att använda
  (PRODUCT.md princip 1). Den posten är cellens tydligaste "vad vi slår".
  **Lämnar:** regnbågsorden i rubriken, pillknapparna, bockraden, logotypväggen, chattpanelen.
- `fold.webp` + `slices/03` (pixlar) — vit grund, topprad med två pillknappar varav en har en
  grön glödring; rubriken i två rader mörkt petrol; två pillknappar och tre grå bockar
  (`14-day free trial` · `No credit card required` · `Cancel anytime`); under folden ett
  produktfönster iscensatt i ett suddigt dagsljusrum. 03 visar en femdelad mörk bildremsa med
  produktnamn i nederkant, sedan en sektion `Meet your AI Agent` med en chattbubbla över ett
  grynigt beige fält.
  **Tar:** ingenting av kompositionen. **Lämnar:** allt: pillarna, glödringen, bockraden,
  bildremsan, chattbubblan (F-006).
- `extract/customer-io-design-language.md` — Motion: feel `responsive`, scroll-linked `yes`,
  två varaktigheter 200/400 ms, ease-out-familjen `cubic-bezier(0.19,1,0.22,1)` i 184 bruk;
  keyframes lutar åt ambient dekor (`marquee`, `text-gradient`, `shine`, `meteor`,
  `border-beam`). Material: `flat`, avg saturation **0,627** (högst av de fem), max radie 6 px.
  **Tar:** varningen. `meteor` och `border-beam` är precis den klass av rörelse
  `find-animation-opportunities`-gaten avvisar: hög frekvens, noll funktion.
  **Lämnar:** hela keyframe-uppsättningen.

### Anti-referens, som är **innehåll** på den här sidan: `sites/before-ai-slop.html`

Här skiljer sig K4 från alla andra celler i kedjan: anti-referensen står inte bredvid bygget,
den **körs live på vänstra halvan av folden**, ärligt etiketterad `En typisk mallsida`. Det är
avsiktligt och etiketterat, aldrig en påhittad kund.

Läst som kod och mätt, inte beskriven ur minnet (kommandon och utdata i § Mätning nedan):
sticky flytande pill-nav med `backdrop-blur`; centrerad hero med badge-rad, ett gradientsatt
ord mitt i rubriken (`.grad-text`, `#1E40AF → #6366F1`), två pill-CTA, en avatarstack av fyra
gradientcirklar; till höger ett **div-byggt "Dashboard preview"-kort** med fyra påhittade
stat-tiles och en SVG-sparkline; sedan sex påhittade ordmärken, tre ikonkort, ett
fyrfältsstatband, en centrerad CTA och en enradsfooter. Sju hexfärger, 20 `rounded-*`,
8 gradienter, **noll fotografier**.

**Vad K4 gör i stället, punkt för punkt:** ingen topprad alls (delaren är chromen) · ingen
badge, ingen pill, ingen gradient, ingen avatar i **K4:s eget lager** · ingen låtsasyta
någonstans — de enda gränssnitt som syns på sidan är riktiga gränssnitt, ett av dem är
antagonisten själv och det är utskrivet · inga påhittade tal: varje siffra i skillnadsliggaren
är mätt ur de två filerna på disk, och varje annan siffra är `26 900`, `38 900` eller `01–03` ·
ingen logotypvägg, inga kunder utöver de tre exempelsajterna · tre tjänster som rader i en
liggare, aldrig tre kort · tre paket som en stycklista, aldrig tre priskort · avslutet är en
kollaps till en kolumn på varmt papper, aldrig en centrerad CTA som rinner ut i en copyrightrad.

---

## Mätning

Skillnadsliggaren i § (5) och i `runs/K4/BRIEF.md` bygger **bara** på tal jag mätt själv.
TASTE § 4.9: siffror får vara textur bara om de är sanna.

Servern startades från repo-roten enligt PRODUCT.md § Operating Context:

```
python "C:/Users/Anton L/.claude/skills/design/scripts/serve.py" --port 3399 --root .
```

### `measure.py` mot mallsidan, ordagrant

```
python "C:/Users/Anton L/.claude/skills/design/scripts/measure.py" http://localhost:3399/sites/before-ai-slop.html
```

```json
{
  "http://localhost:3399/sites/before-ai-slop.html": {
    "height": 2016,
    "textElements": 61,
    "distinctFontSizes": 9,
    "fontSizeRange": [
      12,
      60
    ],
    "topSizes": [
      60,
      48,
      36,
      30,
      20,
      18,
      16,
      14
    ],
    "distinctTextColors": 9,
    "distinctWeights": 4,
    "families": {
      "Inter": 61
    },
    "serifTextElements": 61,
    "accentTextElements": 0,
    "accentAtDisplayScale": 0,
    "hairlineRules": 12,
    "distinctBackgrounds": 8,
    "contentLeft": 0,
    "contentRight": 1440,
    "contentWidthUsed": 1440,
    "images": 1
  }
}
```

### `measure.py` mot Calyx, ordagrant

```
python "C:/Users/Anton L/.claude/skills/design/scripts/measure.py" http://localhost:3399/sites/calyx.html
```

```json
{
  "http://localhost:3399/sites/calyx.html": {
    "height": 5020,
    "textElements": 68,
    "distinctFontSizes": 11,
    "fontSizeRange": [
      11,
      130
    ],
    "topSizes": [
      130,
      101,
      88,
      54,
      51,
      36,
      30,
      24
    ],
    "distinctTextColors": 4,
    "distinctWeights": 1,
    "families": {
      "PT Mono": 33,
      "Cardo": 35
    },
    "serifTextElements": 35,
    "accentTextElements": 0,
    "accentAtDisplayScale": 0,
    "hairlineRules": 10,
    "distinctBackgrounds": 2,
    "contentLeft": 32,
    "contentRight": 1408,
    "contentWidthUsed": 1376,
    "images": 0
  }
}
```

### Kompletterande källräkning, ordagrant

`measure.py` räknar inte kort, gradienter eller fotografier. De talen kommer ur en
deterministisk räkning i de två filerna:

```
python -c "
import re
for f in ['sites/before-ai-slop.html','sites/calyx.html']:
    t=open(f,encoding='utf-8').read()
    hexes=set(x.lower() for x in re.findall(r'#[0-9A-Fa-f]{6}\b',t))
    ok=set(re.findall(r'oklch\([^)]*\)',t))
    print('==',f)
    print('   distinkta hexfarger:',len(hexes), sorted(hexes))
    print('   distinkta oklch-varden:',len(ok))
    print('   shadow-utiliteter:',re.findall(r'[a-z-]*shadow-[a-z0-9\[\]_.,()#/-]*',t))
    print('   rounded-utiliteter:',sorted(set(re.findall(r'rounded-[a-z0-9]+',t))))
    print('   kortformer rounded-(lg|xl|2xl|3xl):',len(re.findall(r'rounded-(?:xl|2xl|3xl|lg)',t)))
"
```

```
== sites/before-ai-slop.html
   distinkta hexfarger: 7 ['#1e40af', '#1f2937', '#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#fbfaf7']
   distinkta oklch-varden: 0
   shadow-utiliteter: ['shadow-sm', 'shadow-xl']
   rounded-utiliteter: ['rounded-2xl', 'rounded-full', 'rounded-lg']
   kortformer rounded-(lg|xl|2xl|3xl): 8
== sites/calyx.html
   distinkta hexfarger: 0 []
   distinkta oklch-varden: 11
   shadow-utiliteter: ['drop-shadow-[0_2px_30px_rgba(0,0,0,0.5)]']
   rounded-utiliteter: []
   kortformer rounded-(lg|xl|2xl|3xl): 0
```

Gradienter och fotografier, samma metod:

```
before-ai-slop.html:  gradient 8  (2 varumarkesfyllningar .grad/.grad-text,
                                   4 avatarcirklar bg-gradient-to-br,
                                   2 <linearGradient> i den falska sparklinen)
                      url() 1     (url(#g), referens till sparklinens gradient)
                      <img> 0     picture 0   srcset 0   unsplash 0
calyx.html:           gradient 2  (bada ar scrim over foto: en bakgrundsscrim,
                                   en bg-gradient-to-b fran ink/10)
                      url() 5     (1 data:image/svg+xml grain + 4 Unsplash-fotografier)
                      <img> 0     picture 0   srcset 0   unsplash 5
```

**En rad som målbilden namnger men mätningen inte bär.** Målbilden räknar upp `hårlinjer` som
en skillnadsrad. `measure.py` säger `hairlineRules` **12 för mallsidan och 10 för Calyx** —
alltså fler hårlinjer på den sida vi argumenterar emot. Raden är därför **struken ur
skillnadsliggaren**. Källa: TASTE § 4.9 och lead-instruktionens "sanna, mätta skillnader
bara". Att behålla den och vända på tolkningen vore precis den sortens tal-som-textur regeln
finns för att stoppa. Ersättningsraden är `Sidmarginal vid 1440`, som är mätt och entydig
(`contentWidthUsed` 1440 mot 1376, alltså 0 px mot 32 px gutter).

---

## K4 · "Före/Efter"

### (1) Auktoritet och vad som viker

**Auktoriteten är produkten** — de två sajterna som objekt, ofria i mitten av ramen
(TASTE § 1 rad 4): argumentet är inte en mening om design, det är två färdiga webbplatser i
samma rektangel, och besökaren avgör själv.

**Vad viker, en mening var.** *Typen* viker: den är nästan tyst, en enda rad i lässtorlek+
tvärs över sömmen plus två monoetiketter, och den enda typ som får displaygrad efter folden är
skillnadsliggarens mätta tal och de tre sista rubrikerna. *Bilden* viker till noll: det finns
inga fotografier i K4:s eget lager, och all fotografi som syns tillhör de sajter som visas.
*Färgen* viker: ett varmt papper, ett varmt bläck och exakt en kromatisk accent som bara får
finnas på delaren. *Rörelsen* viker överallt utom i a1, där den enligt TASTE § 4.8:s
r6-precisering är auktoriteten i set-piece-akten och typ och innehåll viker för den.

### (2) Troplistan

TASTE § 5 punkt för punkt, plus F-006 och gate 47/79. **Statusen gäller K4:s eget lager.** Det
som syns inuti `sites/before-ai-slop.html` är antagonistens egenskaper, inte K4:s, och är
utskrivet som sådant på skärmen.

| Trop | Status i K4 |
|---|---|
| Ikongrid | **Frånvarande.** Tjänsterna 01–03 är tre rader ur en mask i a4; ingen ikon finns i K4:s eget lager. |
| Gradient-mesh | **Frånvarande.** Grunden är en plan varm oklch-färg. Noll `linear-gradient`, noll `radial-gradient`, noll mesh i K4:s CSS. Antagonistens åtta gradienter är mätta och skrivs ut som ett tal i skillnadsliggaren, inte imiterade. |
| Glasmorfism | **Frånvarande.** Noll `backdrop-filter`, noll halvgenomskinliga paneler. Uttryckligen dödad av F-006. Delaren är en opak hårlinje, inte en glasremsa. |
| Centrerad hero med badge-rad | **Frånvarande, och dubbelt spärrad.** Rubriken är sömankrad och vänsterviktad, aldrig centrerad; `grammars.md` split stage förbjuder centrerad copy uttryckligen. Ingen badge, ingen pill, ingen prickrad. |
| Lila/indigo-accent | **Frånvarande.** Enda accenten är `#1E5E9C` = `oklch(0.47 0.13 252)`, Alunix eget Tier 1-bevis. Antagonistens `#6366F1` och `#8B5CF6` finns bara inuti dess egen ram och räknas i liggaren. |
| Skuggade 8 px-kort | **Frånvarande.** Noll `box-shadow` och radie 0 överallt i K4:s lager. Skillnadsliggaren är hårlinjerader, aldrig kort (harkcap-formen). |
| Stockfoto av leende team | **Frånvarande.** Noll fotografier, noll människor, noll ansikten i K4:s lager. Hela `harkcap`-postens porträttmekanik är avvisad. |
| "h1 48 / h2 32"-skala | **Frånvarande.** Skalan är ≥ 5× enligt TASTE § 2.4: display ~112 px (avslutsrubriken och liggarens tal) mot brödtext 15 px; mellannivån 32 px existerar inte, mellanrubriker är monoetiketter i 11 px med tracking. |
| Dekorativa blobbar | **Frånvarande.** Den enda formen i K4:s lager utöver typ är delarens hårlinje, och den är sidans nav. Inget ritas som dekoration. |
| Tre lika feature-kort | **Frånvarande.** Tre tjänster = tre rader i olika längd; tre paket = en stycklista med ledarpunkter. Aldrig tre lådor bredvid varandra, aldrig "populärast". |
| **F-006** — glaskort, dashboard-över-foto, "live"-punkter, telemetri-chrome | **Frånvarande i K4:s lager, och detta är den känsligaste punkten i cellen.** Antagonisten *innehåller* ett div-byggt dashboardkort. K4 får därför aldrig visa ett eget tal om delarens läge, aldrig en procentavläsning, aldrig en statuschip, aldrig en live-prick, aldrig en etikett som säger vilket läge sidan är i. **Kontrollen i R2/R3:** varje element i K4:s eget lager ska kunna namnges som *rubrik*, *monoetikett*, *liggarrad*, *hårlinje* eller *delare*. Kan det inte det ska det bort. |
| **Gate 47** — omritat chrome (webbläsarfält, telefonram) | **Frånvarande.** De två sajterna monteras som `<iframe>` utan ritad webbläsarram, utan flikrad, utan URL-fält, utan trafikljusprickar och utan telefonbezel. Delaren är en linje mellan två ytor, inte en ram runt någon av dem. `paper`-postens produktfönster med trafikljusprickar är uttryckligen lämnat. |
| **Gate 79** — div-byggd låtsas-UI | **Frånvarande.** K4 bygger noll gränssnitt. Varje gränssnitt på skärmen är en riktig fil som serveras från samma origin. Skillnadsliggaren är typografi, inte en graf, inte en sparkline, inte ett stapeldiagram — `mode`s statkort och `customer-io`s chattpanel är båda avvisade av det skälet. |
| **Jämförelseslider-klichén** (K4:s egen tillagda rad) | **Neutraliserad, på fyra mekaniskt kontrollerbara sätt.** (a) **Ingen affordans ritas:** ingen knopp, ingen ikon, ingen dubbelpil, ingen "dra"-text. Träffytan är 44 px bred och osynlig, och `cursor: col-resize` är hela affordansen (gate 88 + `apple-design` § fine pointer). (b) **Delaren är inte en widget, den är sidans chrome:** den är hela navigationen, den enda beständiga formen och det enda kromatiska värdet — en jämförelseslider är en komponent i en sida, K4:s delare *är* sidan. (c) **Den återgår aldrig till mitten.** En slider är en leksak som nollställer sig; K4:s delare har ett mål som ägs av scrollpositionen, och ett släpp lämnas vidare till det målet, inte till 50 %. (d) **Före-sidan är ärligt märkt.** Klichén bygger nästan alltid på ett påhittat "före" som är gjort fult med flit; här är "före" en verklig fil i repot, etiketterad `En typisk mallsida`, och varje påstående om den är ett mätt tal med kommandot utskrivet. |

### (3) Ett displayelement per skärm (1440 × 900)

Nio skärmar. Ett displayelement var, namngivet. Allt annat i vyn går ner ett steg i grad, vikt
eller mättnad (F-003).

Målbilden räknar sex skärmar (s1–s6). Jag delar den pinnade akten i tre skärmar, eftersom
2,4 spans vid 1440 × 900 är tre distinkta vyer som var och en måste kunna skärmbildas och
granskas var för sig, och lägger till tjänsteliggaren som egen skärm eftersom aktlistan
innehåller den men skärmlistan inte gör det. Källa: F-007 (målbildskontrollen körs skärm för
skärm, så varje granskningsbar vy måste finnas i listan).

| # | Akt / ps | Displayelementet | Vad som viker i samma vy |
|---|---|---|---|
| s1 | a1, ps 0–0,10 | **Tvåtonsrubriken** `Er hemsida är nutidens visitkort`, en rad, satt tvärs över sömmen: dämpad `--ink-2` över "före", `--ink` över "efter" | De två sajterna står helt stilla; `Före` / `Efter` som 11 px monoetiketter vid var sin sida av rubriken |
| s2 | a1, ps 0,10–0,68 | **Delaren** — den lodräta hårlinjen med `#1E5E9C`, på väg vänsterut | Rubrikens före-halva tunnas (`wght` 500 → 200) och tracking öppnar; mallsidans mättnad faller |
| s3 | a1, ps 0,68–1,0 | **"Efter"-ytan**: Calyx live, hel, fyller ramen | Rubriken faller till en 11 px monoetikett i övre vänstra hörnet; delaren har lämnat ramen |
| s4 | a2 | **Skillnadsliggarens tal** i displaygrad, ett par per rad, avdelade av hårlinjer | Tesraden `VI BYGGER ERT VARUMÄRKE.` sitter som löphuvud i 15 px; radetiketterna i 11 px mono |
| s5 | a3 objekt 1 | **Hōrai** som full-bleed objekt | Bildtexten `Exempelsida: Hōrai, Asian fusion-koncept` i 11 px mono i underkanten |
| s6 | a3 objekt 2 | **Hyperborea** som full-bleed objekt | Samma |
| s7 | a4 | **Tjänstenamnen** `Design` / `Utveckling` / `System`, en per rad, olika radlängd | Radnumren 01–03 i 11 px mono; underraderna i 15 px |
| s8 | a5 | **Priskolumnen** `26 900` / `38 900` / `Pris vid förfrågan`, i bläck, aldrig i blått | Paketraderna i 15 px med ledarpunkter fram till kolumnen |
| s9 | a6 | **`Alla har rätt till bra design.`** i displayskala, vänsterställd | `kontakt@alunix.se` som 15 px mailto under raden |

### (4) Fingerprint

**Cellens egen rad**, i registrets sex dimensioner:

| Dimension | K4 |
|---|---|
| Grammatik | Split stage |
| Nav | **Ingen bar, ingen meny, ingen pill, inget ordmärke i toppen: delaren är chromen.** En enda lodrät hårlinje som löper hela viewporthöjden, i bläck med `#1E5E9C` som sitt enda kromatiska värde; den är sidans enda beständiga form, dess enda gripbara element (`cursor: col-resize`, 44 px osynlig träffyta, ingen knopp, ingen ikon, ingen text) och dess enda navigation. `kontakt@alunix.se` står som 15 px text i "efter"-halvans övre högra hörn |
| Hero-device | **Två levande sajter i samma 1440 × 900-ruta**, staplade som två lager och åtskilda av en clip-gräns vid `--split`: `sites/before-ai-slop.html` underst, ärligt etiketterad `En typisk mallsida`, Calyx överst; över båda en enradig tvåtonsrubrik som korsar sömmen, dämpad över "före" och bläck över "efter" (paper.design-devicen). Ingen av ramarna transformeras eller skalas någonsin: bara clip-gränsen flyttas |
| Aktform | 6 akter, 9 skärmar: `pin` span 2,4 dwell 0,22 (delaren tippar, toppen) → `reveal` **per sida** (skillnadsliggaren, vänsterfiguren wipeas från vänster, högerfiguren från höger) → `flow`+`in` (Hōrai och Hyperborea som full-bleed objekt) → `kinetic` lines (tjänsterna) → `count` (paketen) → `reveal` (avslutet). Noll `pan`, noll `drift`, noll `spotlight`, noll `magnet`, noll `scrub` |
| Avslut | **Kollapsen till en kolumn.** Delaren har lämnat ramen åt vänster, "efter"-ytan fyller hela bredden, `Alla har rätt till bra design.` står i displayskala vänsterställd på varmt papper, `kontakt@alunix.se` som mailto under. Ingen inversion, ingen mörk CTA-remsa, ingen kolofon, ingen footerrad, och avsiktligt osymmetriskt (split stage förbjuder symmetriskt avslut) |
| Signatur | ***Delaren tippar.*** En enda lodrät gräns som besökaren både skrollar och drar: scrollen äger målvärdet, pekaren får sätta ett eget värde, och släppet lämnas vidare till målvärdet genom en kritiskt dämpad fjäder (damping 1,0, ingen översläng), avbrytbar mitt i rörelsen med behållen position och hastighet. Samtidigt **degraderas rubrikens före-halva av delaren**: `wght` faller 500 → 200 och `letter-spacing` öppnar 0 → 0,06 em längs `--sc-ps`, så paper.design-devicen (identiska metriker, bara färgen skiljer) som gäller vid ps = 0 bryts sönder av rörelsen |

**Gaten mot alla 36 byggrader i registret** (`wiki/projects/_index/design-fingerprints.md`,
7 exempelsajter + 29 Alunix-rader). `≠` = skiljer sig, `=` = delad. Summan räknar antal `≠` av
sex. Kravet är ≥ 4/6 mot **varje** rad, kontrollerat rad för rad, aldrig medelvärde.

| registerrad | grammatik ≠? | nav ≠? | hero ≠? | aktform ≠? | avslut ≠? | signatur ≠? | summa |
|---|---|---|---|---|---|---|---|
| Calyx | ≠ split stage vs chaptered editorial | ≠ delaren som enda chrome vs statiskt border-b-huvud i 3 kolumner | ≠ två levande sajter i en clip-split vs fullbleed botaniskt foto med scrim | ≠ 6 motorakter med pin 2,4 vs 8 handrullade sektioner | ≠ kollaps till en kolumn på varmt papper vs mörkinverterad mailto i jättekursiv | ≠ delaren tippar vs ingen (bara IO-fade) | **6/6** |
| Hōrai | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad bar som mörkblurrar | ≠ clip-split av två sajter vs fullbleed JS-parallaxfoto med jätteordmärke | ≠ pin+reveal+flow+kinetic+count vs scrubbat citatkapitel | ≠ kollaps till en kolumn vs mörk sektion med book.horai.se i jättegrad | ≠ vs bell-curve-scrubbat citat | **6/6** |
| Hyperborea | ≠ split stage vs chaptered editorial | ≠ ingen topprad alls vs sticky header under edition strip med amber CTA-pill | ≠ två sajter i clip-split vs statiskt lagrat sol- och skyline-SVG | ≠ 6 akter med pin och count vs 8 sektioner, marquee, ingen motor | ≠ kollaps vs mörk kolofon "write us a letter" | ≠ vs ingen (sol-diskarna är ett system, inte en interaktion) | **6/6** |
| Tidvatten | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad bar med "Bli medlem"-länk | ≠ två sajter i clip-split, noll eget foto vs fullbleed havsfoto med ordmärket över hela ramen | ≠ 6 akter utan scrub vs 7 sektioner med pinnat gradscrub | ≠ kollaps till en kolumn på papper vs mörk inverterad mailto i jättegrad | ≠ **en** gräns som färdas i **en** riktning, driven 1:1 av scroll och pekare, vs **två** tal som glider in från motsatta kanter och konvergerar på en bell-curve-scrub | **6/6** |
| Vintergatan | ≠ split stage vs chaptered editorial | ≠ delaren vs statiskt huvud under edition strip, centrerat ordmärke | ≠ två sajter i clip-split vs typ satt direkt i fotografiet | ≠ 6 akter vs 11 sektioner med pinnad ordavslöjning | ≠ kollaps vs mörk sektion med kursiv mailto och öppettider | ≠ vs tre ord som förgylls i sekvens | **6/6** |
| Vinterspelen | ≠ split stage vs chaptered editorial med gallery-inflektion | ≠ delaren vs sticky header med ljuslågemärke och biljettknapp | ≠ två levande sajter vs delat anslag med en inramad målning | ≠ 6 akter utan scenbyte vs 10 sektioner med pinnat kulissbyte | ≠ kollaps till en kolumn vs papperssektion "resan" som matar en mörk 3-kolumnsfooter | ≠ vs sex kulissremsor i vågrörelse | **6/6** |
| before-ai-slop | ≠ split stage vs ingen av de åtta | ≠ delaren som chrome vs sticky flytande pill med backdrop-blur | ≠ två riktiga sajter i clip-split vs centrerad split med badge, gradientord och div-byggt dashboardkort | ≠ 6 koreograferade akter vs 7 statiska sektioner utan en enda reveal | ≠ kollaps till en kolumn vs centrerad CTA och enradsfooter | ≠ vs ingen alls | **6/6** |
| r1 K1 Svart scen och vit sal | ≠ split stage vs rhythmic cutlist | ≠ delaren vs minimal fixerad toppremsa med ordmärke och mailto | ≠ två sajter i clip-split på varmt papper vs mörk scen med en ljuspöl i fotot | ≠ 6 motorakter vs 4 hårda klipp utan motor | ≠ kollaps på varmt papper vs vit sal med mailto i displaygrad | ≠ vs tre demorutor som lyfter med underglöd | **6/6** |
| r1 K2 Tjänsteledger | `=` båda split stage | ≠ delaren som enda chrome, ingen bar och inget ordmärke vs sticky vänsterskena med roterat ordmärke, tre länkar och mailto | ≠ två levande sajter under en tvåtonsrubrik vs vitt papper med jättefråga i grotesk och en solid ink-knapp | ≠ 6 motorakter med pin 2,4 vs 3 sektioner med fast vänsterspalt och färgbyte per kapitel | ≠ kollaps till en kolumn på varmt papper vs mörkt band med systemtexturlinje och tre färgprickar | ≠ delaren tippar vs kapitelfärg som fördjupas via color-mix | **5/6** |
| r1 K3 Instrument | ≠ split stage vs typographic poster | ≠ delaren vs kickerremsa utan nav | ≠ två sajter i clip-split vs displaypåstående på onyx med ett blått handlingsord | ≠ 6 akter med pin vs 5 sektioner på en värdestegsgrund | ≠ kollaps till en kolumn vs en enda påståenderad | ≠ vs siffror som räknar upp med linjal under | **6/6** |
| r1 K4 Journal | ≠ split stage vs chaptered editorial | ≠ delaren vs toppkickerrad med ordmärke och mailto | ≠ två levande sajter vs vikt-300-serifrubrik med en atmosfärsplate bredvid | ≠ 6 akter, pin 2,4 vs 4 handrullade romerska kapitel | ≠ kollaps till en kolumn vs tryckt kolofon som krediterar typsnitt, foto och person | ≠ vs `NN / 03`-räknare på varje plate | **6/6** |
| r1 K5 Affisch | ≠ split stage vs gallery/catalog | ≠ delaren vs textnav i foldens underkant | ≠ två sajter i clip-split vs ordmärket i viewportbredd på en flat färg | ≠ 6 akter vs 3 numrerade helbreda plates | ≠ kollaps till en kolumn vs kontakt som en enda rad | ≠ vs ordmärket som fast bakgrundslager | **6/6** |
| r1 K6 Kortlek | ≠ split stage vs live surface | ≠ delaren vs fixerad flytande pill | ≠ två sajter live i clip-split vs solfjäder av tre skärmbilder | ≠ 6 akter vs 4 sektioner i drift-parallaxfamiljen | ≠ kollaps till en kolumn vs ingen egen avslutsform alls | ≠ vs kortleken som blandas om på scroll | **6/6** |
| r2 R1 Squarespace scen | ≠ split stage vs rhythmic cutlist | ≠ delaren vs svart topprad med spökknapp | ≠ två sajter i clip-split vs fullbleed mörkt spotlightfoto med centrerad rubrik | ≠ 6 akter med pin vs 5 helbreda band med hårda klipp, ingen pin | ≠ kollaps på varmt papper vs vit sal med mailto i 72 px | ≠ vs rutor som glider in underifrån | **6/6** |
| r2 R2 Vit remsa | ≠ split stage vs chaptered editorial | ≠ delaren vs vit topprad plus pill-filterrad under heron | ≠ två levande sajter vs vitt typband utan bild | ≠ 6 akter med pin vs 5 sektioner med mörka projektkort | ≠ kollaps till en kolumn vs tyst vitt kontaktblock | ≠ vs pill-flikar som `:target`-markerar rätt kort | **6/6** |
| r2 R3 Färgband | ≠ split stage vs chaptered editorial | ≠ delaren vs vit topprad med seriflogotyp och fyra länkar | ≠ två sajter i clip-split vs vit grund med gemen grotesk rubrik och ingen bild alls | ≠ 6 motorakter vs mosaikremsa plus tre mättade tjänsteband | ≠ kollaps på varmt papper vs mörkt band med manifestrad och mailto | ≠ vs färgbanden som *är* tjänsterna | **6/6** |
| r2 R4 Numrerad process | ≠ split stage vs chaptered editorial | ≠ delaren vs mörk topprad med tre länkar och en blå pill-CTA | ≠ två sajter i clip-split vs fullbleed mörkt texturfoto med komprimerad tung rubrik | ≠ 6 akter med pin och count vs 4 sektioner med 01–05 i schweizisk rytm | ≠ kollaps till en kolumn vs mörkt band plus en pill | ≠ vs mono-numren 01–05 som genomgående spår | **6/6** |
| r2 R5 Konsolram | `=` båda split stage | ≠ **en naken hårlinje** som är sidans enda chrome vs **en konsolram** med versionstagg, levande klocka och fyra hörnmärken (K4 får per F-006 aldrig visa ett tillstånd om sig själv, vilket är precis vad konsolramen gör) | ≠ två riktiga sajter i clip-split vs ordmärket inne i en konsolram lagd över ett gråskalefoto | ≠ 6 motorakter med pin 2,4 vs 3 sektioner utan motor | ≠ kollaps till en kolumn på varmt papper vs vitt block med en jätterubrik | ≠ en gräns som färdas vågrätt och kan gripas vs hörnmärken som står fixerade i viewporten | **5/6** |
| r2 R6 Affischordmärke | ≠ split stage vs typographic poster | ≠ delaren vs fixerad minimal rad med cirkelmärke och kontaktpill | ≠ två sajter i clip-split vs ordmärket i viewportbredd med fullbleed dokumentärfoto under | ≠ 6 akter vs 5 sektioner utan motor | ≠ kollaps till en kolumn vs off-white kolofon som stänger på mailto som text | ≠ vs tre 12 px färgprover, ett per demorad | **6/6** |
| r3 build (R5+R6) | `=` båda split stage | ≠ delaren, som är **en rörlig gräns mellan två ytor**, vs fyra **fasta hörnmärken** i viewportens hörn | ≠ två **främmande** sidor renderade hela i samma ruta, utan en enda Alunix-komposition i folden vs **två egna heron** sida vid sida (konsolkort över gråskalefoto till vänster, Tidvatten-iframe till höger) med logotypmärket dockat på sömmen; K4 har inget märke på sömmen | ≠ 6 akter med `pin` 2,4 vs 9 rena `flow`-akter och aldrig pin | ≠ kollaps till **en** kolumn vs Calyx-ram och prisruta som stänger samtidigt i **två** spalter | ≠ delaren färdas **vågrätt** över hela bredden, driven av scroll **och** pekare, kritiskt dämpad, och degraderar rubrikens ena halva vs sömlinjen som **växer lodrätt** via `scaleY` ur ett dockat märke, utan pekare och utan följd för någon annan del av sidan | **5/6** |
| r4 M1 Kontinuerlig grund | ≠ split stage vs continuous world | ≠ delaren vs tunn topprad som scrollar bort | ≠ två sajter i en clip-split vs en helbred levande Tidvatten-iframe som hela första akten | ≠ 6 akter med pin, kinetic och count vs 8 rena flow-akter över en fast grund | ≠ kollaps till en kolumn vs Calyx-ram och prisruta, avsiktligt osynkade | ≠ vs +50 vh-förskjutningen som låter grunden lysa igenom | **6/6** |
| r4 M2 Kapitel med pinnad scen | ≠ split stage vs chaptered editorial | ≠ delaren vs fast folio `0X/05` plus roterad kapitelskena | ≠ två sajter i clip-split vs ett stilla konsoltitelkort över en gråskalegrund | ≠ 6 akter, pin 2,4 dwell 0,22 vs 3 motorakter med pin 3,2 i fem kapitel | ≠ kollaps till en kolumn vs inverterad prisruta ensam i kapitel 05 | ≠ vs kapitelskenan som scrollhuvud (`-scrollY` på inre spår) | **6/6** |
| r4 M3 Galleri med rail | ≠ split stage vs gallery/catalog | ≠ delaren vs indexnav med fyra mono-hopplänkar | ≠ två sajter i clip-split vs affischordmärke staplat över konsolkortet | ≠ 6 akter med **noll** `pan` (split stage förbjuder den) vs 6 akter vars spine är en inbäddad horisontell `pan`-rail span 4,2 | ≠ kollaps till en kolumn vs en prisruta som katalogens sista objekt | ≠ vs ordskrubben med SVG-tråd i marginalen | **6/6** |
| r5 V1 Dokumentär band | ≠ split stage vs continuous world | ≠ delaren vs ärvd tunn topprad som scrollar bort | ≠ två levande sajter vs band med krämpanel 38 % och färgfoto 62 % | ≠ 6 akter med pin vs 8 rena flow-akter | ≠ kollaps till en kolumn vs ärvd Calyx-ram och prisruta, osynkade | ≠ delaren som gräns mellan två **sidor** vs krämpanelen som växer över ett **foto** | **6/6** |
| r5 V2 Cinematisk tvätt | ≠ split stage vs continuous world | ≠ delaren vs ärvd tunn topprad | ≠ två sajter i clip-split vs fullbleed ljusstrålefoto under en svart tvätt | ≠ 6 akter, ingen drift vs 9 akter med drift och parallax | ≠ kollaps till en kolumn vs Hyperborea-ram och prisruta, osynkade | ≠ vs tvättlyftet i en rad CSS | **6/6** |
| r5 V3 Plåt i grunden | ≠ split stage vs continuous world | ≠ delaren vs ärvd tunn topprad | ≠ två sajter i clip-split vs inramad plåt med hårlinje på mörk grund | ≠ 6 akter vs 8 flow-akter i två spalter | ≠ kollaps till en kolumn vs Calyx-ram och prisruta, osynkade | ≠ vs ljuspölen som vandrar via object-position | **6/6** |
| r5 V3b Plåt i grunden, polerad | ≠ split stage vs continuous world | ≠ delaren vs ärvd tunn topprad | ≠ två sajter i clip-split vs samma inramade ljuspölsplåt, kapad till en fold | ≠ 6 akter med pin och count vs 8 flow-akter | ≠ kollaps till en kolumn vs ärvd Calyx-ram och prisruta | ≠ vs samma ljuspölsvandring | **6/6** |
| r6 A-K1 Skymning (native) | ≠ split stage vs filmic one-shot | ≠ delaren vs minimal fixerad topbar som växlar över grunderna | ≠ två sajter i clip-split vs fullbleed blåtimmesfoto med ljus serifrubrik | ≠ 6 akter utan zoom vs CSS-dolly skala 1 → 22 och pinnad iframe-avslöjning | ≠ kollaps till en kolumn på varmt papper vs nattfoto som landar och håller | ≠ en gräns som färdas i **bildplanet** vs en kamera som flyger **in i** ett fönster | **6/6** |
| r6 A-K2 Affischen (native) | ≠ split stage vs typographic poster | ≠ delaren vs tryckt topprad med tickande klocka | ≠ två sajter i clip-split vs ordmärket brutet ALU / NIX med fönster i bokstävernas punsar | ≠ 6 akter vs 7 akter med 320 vh pinnad hero | ≠ kollaps till en kolumn vs bläckark som rullas ner med clip-path | ≠ vs bildremsan som passerar genom bokstäverna | **6/6** |
| r6 A-K3 Konsolen (native) | ≠ split stage vs live surface | ≠ delaren vs app-chrome med 56 px bar och tre numrerade flikar | ≠ två sajter samtidigt i samma ruta vs fullbleed skrivbordsfoto med glaskort som läser tillstånd | ≠ 6 akter vs 6 akter med iframe-scrollTop-växling | ≠ kollaps till en kolumn vs riktigt inmatningsfält som öppnar mailto | ≠ besökaren flyttar **gränsen mellan** två sidor vs besökaren driver **innehållet i** en sida | **6/6** |
| r6 B-K1 Skymning (kedjan) | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad bar som byter grund per akt | ≠ två sajter i clip-split vs blåtimmesfoto med retuscherad skylt och ljus serifrubrik | ≠ 6 akter med kit-pin vs handrullad lerpad zoom utan kit-pin | ≠ kollaps till en kolumn vs nattfoto som öppnas med clip-path | ≠ vs kameran in i ett riktigt tänt fönster | **6/6** |
| r6 B-K1-nogate | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad bar plus separat nav i ramen med toggle-knapp | ≠ två sajter i clip-split vs blåtimmesfoto där målfönstret redan syns i vila | ≠ 6 akter vs 6 akter med 3,8 vh heroloop | ≠ kollaps till en kolumn vs andra nattfotot som håller stilla | ≠ vs samma zoom men med opt-in-ram | **6/6** |
| r6 B-K2 Affischen (kedjan) | ≠ split stage vs typographic poster | ≠ delaren vs tunn topprad med `Intl`-klocka | ≠ två sajter i clip-split vs ALU / NIX i variabel Archivo 900 med bildpanel bakom bokstäverna | ≠ 6 akter vs 7 akter med pinnad bildremsa 0 → 55 % | ≠ kollaps till en kolumn vs bläckblock rullat med clip-path till sidans slut | ≠ vs panelglid plus andande block | **6/6** |
| r6 B-K3 Konsolen (kedjan) | ≠ split stage vs live surface | ≠ delaren vs 56 px app-bar med statuschip | ≠ två sajter i clip-split vs dagsljusfoto med krämslöja och glaskort | ≠ 6 akter vs 6 akter med 1:1 scrollTop-mappning | ≠ kollaps till en kolumn vs mörkt avslut med riktigt textfält | ≠ besökaren flyttar en **gräns** vs besökaren provkör en **sidas scroll** | **6/6** |
| r7 B-K1 Skymning v2 | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad topbar med logotypväxling och etikettslot | ≠ två sajter live i clip-split vs 100-bilders förrenderad dolly på `canvas[data-sc-sequence]` | ≠ 6 akter, pin span 2,4 vs 4 motorakter med pin span 5,0 | ≠ kollaps till en kolumn vs nattfoto som `reveal` plus färgdrift | ≠ vs kameraåkning som blir en levande sida via `window-track.json` | **6/6** |
| r7 B-K2 Affischen v2 | ≠ split stage vs typographic poster | ≠ delaren vs tunn topprad med klocka och stad | ≠ två sajter i clip-split vs bild maskad genom bokstävernas uppmätta öppningar | ≠ 6 akter vs 5 akter med pin span 3 och diskret radhöjdssteg | ≠ kollaps till en kolumn på oförändrat varmt papper vs grunden som driftar från papper till bläck | ≠ vs papper bakom masken plus andande block | **6/6** |

**Lägsta summa: 5/6**, mot tre rader — **r1 K2 Tjänsteledger**, **r2 R5 Konsolram** och
**r3 build (R5+R6)** — och i alla tre fallen är den delade dimensionen *grammatik*, som
målbilden själv låser. Ingen rad faller under 4/6, och ingen rad delar mer än en dimension.

De tre split stage-raderna är också de enda i registret som kan kollidera, och de kollisioner
som ligger närmast till hands är avvärjda i formuleringen, inte i ordvalet:

- **r2 R5:s konsolram** och K4:s delare är båda "chrome i stället för en bar". Skillnaden är
  materiell och kontrollerbar: konsolramen *rapporterar ett tillstånd* (version, klocka,
  hörnmärken), vilket F-006 uttryckligen förbjuder K4 att göra. K4:s delare rapporterar
  ingenting; den är en gräns.
- **r3 builds sömlinje** och K4:s delare är båda en lodrät linje i en tvådelad komposition.
  Skillnaden är riktning, drivning och följd: r3:s linje **växer lodrätt** ur ett dockat märke
  via `scaleY`, är enbart scrolldriven och påverkar ingenting annat; K4:s linje **färdas
  vågrätt** över hela bredden, är både scroll- och pekardriven, och dess läge är det som
  degraderar rubrikens ena halva och som avgör hur mycket av varje sajt som syns.

**Extra tabell: K4 mot K3.** K3:s låsta värden är hämtade ur `concepts-K3.md` § (4) och § (6).
Sex dimensioner plus två: temperatur och typsnitt.

| Dimension | K3 | K4 | ≠? |
|---|---|---|---|
| Grammatik | Chaptered editorial | Split stage | **≠** |
| Nav | Ritad teckenförklaring i vänstermarginalen, sticky, fem rader symbolprov plus en ledarlinje som ritas till aktivt kapitel | Ingen marginal, ingen legend, inget symbolprov: en enda lodrät gräns i bildens mitt som är hela chromen, plus en mailto i övre högra hörnet | **≠** |
| Hero-device | En måttsatt sektionsritning i inline-SVG som ritar sig själv ur `stroke-dashoffset`; sajten maskas till sist in i öppningen bläcket ritat | Två färdiga, levande sajter som båda finns på skärmen från första bildrutan; ingenting ritas, ingenting byggs upp, gränsen mellan dem flyttas | **≠** |
| Aktform | 6 akter: `pin` 2,4 dwell 0,35 → `kinetic` → `reveal` ×3 (tre plates i följd) → `flow`+`in` → `count` → `reveal`. Noll `pan`, noll pekar-devices | 6 akter: `pin` 2,4 dwell 0,22 → `reveal` **per sida** (tvåriktad, en device K3 inte använder) → `flow`+`in` → `kinetic` → `count` → `reveal`. Ryggraden är en enda obruten upplösning, inte ett galleri av tre plates; a1 bär dessutom en pekardriven, avbrytbar bespoke-rörelse, vilket K3:s pin uttryckligen inte gör | **≠** (tunnaste raden i tabellen, se not) |
| Avslut | Ett specifikationsblad på kallt papper: stycklista med ledarpunkter inuti en ritad ram vars linjer dras in sist | En kollaps till en kolumn på varmt papper: ingen ram, inga linjer dras, ytan bara fylls och rubriken landar | **≠** |
| Signatur | *Ritningen blir sidan*: en kontur ritas och den riktiga sidan maskas in i öppningen | *Delaren tippar*: två färdiga sidor konkurrerar om samma rektangel och en gripbar gräns avgör | **≠** |
| **Temperatur** | Kallt: `--paper` `oklch(0.95 0.012 230)`, hue 230 | Varmt: `--paper` `oklch(0.957 0.013 85)`, hue 85 | **≠** 145° isär i hue, samma låga chroma. Ingen av dem är kräm |
| **Typsnitt** | Chivo (röst) + Martian Mono (register) | Switzer (röst) + Reddit Mono (register) | **≠** Noll överlapp, och K4 rör ingen av K3:s fyra reservval |

**8/8. Not om aktformraden:** det är tabellens tunnaste rad, eftersom båda cellerna öppnar med
`pin` span 2,4 och båda innehåller `flow`, `count` och `reveal`. Jag flyttar inte span 2,4,
eftersom målbilden låser den och gaten inte faller. Skillnaden jag hävdar är strukturell och
kontrollerbar i markupen: K3 har tre `reveal`-akter i följd och en `kinetic` rubrik tidigt;
K4 har noll `reveal` i följd, en tvåriktad `reveal`, `kinetic` sent, och en pekardriven
bespoke-rörelse i pin-akten. Lead bör läsa raden som den svagaste punkten i cellen och kan när
som helst be mig byta `dwell` eller aktordningen om den ska vara starkare.

**Vad jag bytte i planen, och varför.** Ingen ändring nedan tvingades fram av att gaten föll
under 4/6 — gaten håller på 5/6 som lägst. Alla ändringar har andra källor, som står utskrivna.

1. **`pan` ströks och ersattes.** Min första aktplan lade Hōrai och Hyperborea i en vågrät
   `pan`-akt, som en fortsättning på den axel delaren just lämnat. Källa som stoppade det:
   `scroll/grammars.md`, raden för **Split stage**, kolumnen *Bans*: `pan`, `spotlight`,
   `magnet`, > 1 `scrub`, `drift`. Åtgärd: a3 är `flow` + `in` med stagger. Det håller
   målbildens "i tur och ordning" och kostar ingenting.
2. **`flow` (paketen) blev `count`.** Målbilden skriver `flow` (liggaren 01–03) följt av
   `flow` (paketen), vilket sätter samma familj två gånger i rad. Källa: `devices.md`
   § device kit, "never the same one twice running". Åtgärd: a4 är `kinetic` lines
   (tjänsterna, tre rader ur en mask) och a5 är `count` (paketen). `count` är dessutom en av
   split stages tre egna lutningar, formulerad som **real `count`** — och Alunix har exakt två
   sanna tal, `26 900` och `38 900`, vilket `devices.md` § 7 kräver.
3. **Tesraden fick en plats.** Målbildens aktlista för K4 nämner aldrig
   `VI BYGGER ERT VARUMÄRKE.`, men strängen står i PRODUCT.md:s låsta copy-lista och lead
   bekräftar versalformen. Källa: copy-gate (ordagrann copy bevaras) + PRODUCT.md
   § Brand Commitments. Åtgärd: raden är a2:s löphuvud, satt i 15 px över skillnadsliggaren,
   alltså på den yta argumentet just vunnit. Den får ingen egen akt, eftersom en tredje topp
   är ingen topp (`feel-and-fingerprint.md` § The peak).
4. **`dwell` sänktes från K3:s 0,35 till 0,22.** Källa: `feel-and-fingerprint.md` § Pacing och
   F-002. K3:s pin öppnar med ett medvetet tomt ark; K4:s fold är redan full av innehåll vid
   ps = 0 och behöver ingen tystnad före toppen, bara en kort stillhet så att besökaren hinner
   se att det är två sidor.
5. **Skärmlistan växte från 6 till 9.** Källa: F-007, som körs skärm för skärm. Se § (3).
6. **`hårlinjer` ströks ur skillnadsliggaren.** Källa: TASTE § 4.9 och den egna mätningen:
   `hairlineRules` 12 mot 10, alltså tvärtemot vad målbilden antar. Ersatt av
   `Sidmarginal vid 1440`, som är mätt och entydig. Se § Mätning.
7. **Hōrai och Hyperborea visas som skärmbilder, inte som live-ramar.** Källa: målbilden själv
   (den kallar dem "full-bleed **objekt**", inte ramar) plus `performance.md` § 1: fyra
   samtidiga iframes är inte försvarbart inom 2,5 MB. Calyx förblir live, så PRODUCT.md
   princip 1 ("beviset ska gå att använda") är uppfylld på sidan. Se § Prestandaplan i
   `runs/K4/BRIEF.md`.
8. **Referensvalet.** Målbildens fem förväntade slugar ersattes av `select.py`s faktiska rad.
   Tre av fem stämde; `future-fur` och `dovetail` föll och skälen är utskrivna i
   § catalogue-select. Källa: `catalogue-first.md` § 5.
9. **Assetvägen: ingen generering.** Higgsfield är ute (lead mätte `balance` = 0 krediter,
   free plan, 2026-09-09). Källa: planens § 10.6 fallback steg 3. **K4 behövde ändå inget
   genererat material**, och skälet är principiellt, inte praktiskt: cellens hela premiss är
   att allt som visas är verkligt och mätbart. En genererad bild på den här sidan vore ett
   påhittat objekt i en sida vars argument är att den inte hittar på något. Material som letar
   efter en användning är inte tillåtet. Se `runs/K4/assets/ASSETS.md` och `NOTES.md`.
10. **Reduced motion utgår.** Fältet "Reduced motion-planen" finns inte i K4:s skelett.
    Källa: F-011.

### (5) Rörelse

**Motion-tes.**

- **Focal.** Ögat ska följa **delaren**, och bara den. Under hela a1 står allt annat i vyn
  helt stilla: de två sajterna rör sig inte en pixel, rubriken flyttar sig inte, kickerna
  flyttar sig inte. Det enda som ändrar läge är en lodrät linje. Ett enda fokusskifte i hela
  akten, vid ps ≈ 0,68, när linjen lämnar ramen och blicken faller på ytan som blev kvar.
- **Continuity.** Ingenting tonar in ur intet och ingenting hoppar in i vy. Båda sajterna är
  redan där vid ps = 0; det som ändras är hur mycket av var och en som är synlig. Delaren
  startar i mitten där den redan syntes, färdas monotont åt ett håll och lämnar ramen — den
  vänder aldrig, den studsar aldrig, den nollställs aldrig. Rubriken är samma rad hela vägen;
  den byter bara vikt och tracking på sin ena halva. Det som fyller ramen vid ps = 1 är
  **samma** Calyx-ram som stod till höger vid ps = 0, inte en ny ruta ovanpå (F-010).
- **Feedback.** Scrollen *är* handen på delaren: 1 % scroll = 1 % förflyttning, båda
  riktningarna, ingen låsning, ingen hijack utöver motorns egen pin. Pekaren får samma
  auktoritet: `pointerdown` på den 44 px breda osynliga träffytan tar över värdet direkt och
  1:1, `pointermove` skriver det, `pointerup` lämnar tillbaka det till scrollens värde genom en
  **kritiskt dämpad fjäder (damping 1,0)**, seedad med pekarens hastighet vid släppet
  (velocity-handoff). Rörelsen är **avbrytbar**: ett nytt `pointerdown` mitt i återgången tar
  vid i det läge och den hastighet fjädern hade — den nollställer inte och den hoppar inte.
  Det som målas är alltid fjäderns utvärde, aldrig pekarens råa x (`apple-design`
  § presentationsvärde). Att scrolla uppåt drar tillbaka delaren i exakt omvänd ordning.
- **Budget.** **En** `pin` på hela sidan, span 2,4, dwell 0,22. Den bespoke rörelsen är
  **ett** tal, `--split`, skrivet en gång per bildruta av **en** rAF-loop som stannar av sig
  själv i vila; `--split` driver tre `calc()`-uttryck i CSS (clip-gränsen, rubrikhalvans
  `font-variation-settings`/`letter-spacing`, mallsidans `filter: saturate()`) och noll
  layoutläsningar. Ingen `transition: all`, ingen `backdrop-filter`, ingen `filter` på något
  utom mallsidans wrapper. `will-change` sätts bara på delaren och på wrappern medan
  `0 < ps < 1`, aldrig i vila. Två typsnittsfiler, båda variabla, båda självhostade som
  `.woff2`, tak 300 kB. Iframes monteras via IntersectionObserver med `loading="lazy"`.
  Måltal (F-014, `motion-smoothness.md` § The bar, vid 4× CPU): `staircase = 0`,
  `max_step ≤ 3 %`, bildtid p95 ≤ 20 ms, noll frames > 33 ms, båda scrollriktningarna mätta,
  och `motion_probe` körd med **både** `--wheel 20:120` och `--wheel 100:60`.

**F-014, uttryckligt.** Allt ögat ser förflytta sig läser `--sc-ps`, aldrig rå `--sc-p`:
clip-gränsen, rubrikhalvans vikt och tracking, liggarradernas wipe, `kinetic`-radernas mask.
Endast cue-opacitet läser `--sc-p`. `--split` beräknas ur `--sc-ps` plus pekarens offset och
publiceras som ett registrerat `<number>` av samma slag som `sc-smooth.js` publicerar
`--sc-ps`, så att CSS kan interpolera det. `motion-smoothness.md` § Fault 1 är läst: den
lerpade fjädern löser fel 1, och prestandaplanen i BRIEF:en löser fel 2. De är olika fel och
båda mäts.

**Feeling curve** — en känsla per akt, orsaken i andra kolumnen, aldrig två lika i rad.

| # | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| a1 | **Tillfredsställelse** ← TOPPEN | Två färdiga webbplatser står emot varandra i samma ruta, och sedan trycks den ena bokstavligen ut ur bild av den andra medan besökarens egen hand kan ta tag i gränsen och skjuta på |
| a2 | **Skärpa** | Känslan blir ett tal: sex mätta par i displaygrad, avdelade av hårlinjer, var och en avslöjad från sin egen sida |
| a3 | **Tillit** | Två sajter till, hela, i full bredd, en i taget, i en grad där man ser att de är riktiga |
| a4 | **Klarhet** | Tre ord, tre rader, olika längd, ingenting annat i vyn |
| a5 | **Trygghet** | Priserna räknas upp till 26 900 och 38 900, och det tredje står utskrivet i klartext i stället för att gömmas |
| a6 | **Ro** | En rad och en adress på ett papper som slutar röra sig |

**Författad tystnad** (måste stå i BRIEF.md så `scroll_verify.py`s `blankBands` inte larmar
falskt): de första 0,10 av a1 är avsiktligt orörliga — båda sajterna står helt stilla medan
besökaren läser rubriken. Det är stillheten före toppen, inte död scroll. Den är kortare än
K3:s (0,12) eftersom vyn redan är full av innehåll.

**Tell-someone-meningen.** *"Det är sajten där den dåliga hemsidan bokstavligen trycks ut ur
bild av den bra, och man kan ta tag i gränsen och skjuta på själv."*

**Device-tabell.** Fem familjer (`pin`, `reveal`, `flow`, `kinetic`, `count`), aldrig samma två
i rad, noll `pan`, noll `drift`, noll `spotlight`, noll `magnet`, noll `scrub` — alla fem
förbjudna av split stage. Kolumnen **läser** anger vad varje rörlig sak läser: `--sc-ps` för
allt ögat ser förflytta sig, `--sc-p` bara för cue-opacitet, och "motorns egen" där motorn
själv äger transformen (F-014 regel 1).

| Akt | Sektion | Device (familj) | Span / cue | Vad som rör sig | Läser | Varför just denna |
|---|---|---|---|---|---|---|
| a1 | Delaren | `pin` (+ bespoke `paintSplit`) | span 2,4 · dwell 0,22 · cue `0 1 0 0` (hälsa och håll, ground finns) | `clip-path: inset()` på "efter"-lagret; delarens `translateX`; rubrikhalvans `font-variation-settings` och `letter-spacing`; mallsidewrapperns `saturate()` | **`--sc-ps`** via `--split` (allt ovan); `--sc-p` (kickernas opacitet) | Split stages egen lutning är ordagrant "`pin` with divider"; ramen måste hålla stilla medan en enda idé korsar den |
| a2 | Skillnadsliggaren | `reveal` **per sida** | `data-sc-reveal-at="0.12 0.5"`, riktning `left` på före-kolumnen och `right` på efter-kolumnen | `clip-path`-wipe per tal, från sin egen sida in mot hårlinjen | **`--sc-ps`** | Split stages andra lutning är ordagrant "`reveal` per side"; att varje tal kommer från sin egen halva håller argumentets geometri levande efter att delaren är borta |
| a3 | Hōrai, Hyperborea | `flow` + `in` | stagger 90 ms, full blockpadding | De två objekten stiger 14 px och tonar in, ett i taget | `--sc-p` (opacitet); motorns egen (14 px-lyftet) | Efter upplösningen får full-bleed förekomma; objekten ska passera, inte pinnas (`feel-and-fingerprint.md` § Pacing) |
| a4 | Tjänsterna 01–03 | `kinetic` lines | cue `0.1 0.9 0.15 0.4` | Tre rader ur en mask, en i taget | motorns egen (raderna); **`--sc-ps`** (radnumrens hårlinje) | En kinetisk rubrik per sida, och rader är nästan alltid rätt form för den (`devices.md` § 5) |
| a5 | Paketen | `count` | `data-sc-count-at="0.1 0.5"`, 1,4 s, cubic ease-out | `26 900` och `38 900` räknar upp; `Pris vid förfrågan` skrivs, den räknar inte | motorns egen | Split stages tredje lutning är ordagrant "real `count`"; endast sanna tal får en count (`devices.md` § 7) |
| a6 | Avslutet | `reveal` (sidans sista akt) | cue `0.25` (ett värde: sista akten måste hålla) | Avslutsrubriken wipeas fram vänsterifrån, en gång | **`--sc-ps`** | Avslutet ska lösa upp, inte tona ut (`feel-and-fingerprint.md` § The peak) |

**Embodiment, en enda** (`feel-and-fingerprint.md` § Being in it: "one or two per page"):
**delaren är gripbar.** Det är sidans enda interaktion och den är dess signatur. Ingenting
annat på sidan reagerar på besökaren — ingen hover-lyft, ingen magnet, ingen tilt, ingen
pekarföljare. Att lägga till en andra embodiment vore att ge sidan två röster; målbildens egen
regel är att delaren är den enda formen som är sidans.

**Rejected-lista** (`find-animation-opportunities`-gaten, fyra frågor per kandidat: frekvens,
syfte, hastighet, funktion).

| Kandidat | Frekvens | Syfte | Hastighet | Funktion | Dom |
|---|---|---|---|---|---|
| Delaren snäpper tillbaka till 50 % när pekaren släpps | Varje släpp, alltså ofta | "Ordning" | ~300 ms | Ingen, och den motarbetar berättelsen: sidans hela argument är att balansen ska tippa, inte återställas | **Avvisad.** `apple-design` § velocity handoff: släppet lämnas vidare till det värde scrollen äger, aldrig till en godtycklig mittpunkt |
| Ett handtag med två pilar, en knopp eller texten "dra" på delaren | Alltid synligt | Affordans | Statisk | Ingen; `cursor: col-resize` bär affordansen | **Avvisad.** Gate 88 (varje scroll-cue) och lead-instruktionens uttryckliga förbud |
| Hover-lyft eller bakgrundstoning på skillnadsliggarens rader | Varje pekarpassage | Dekor | ~150 ms | Ingen, och den får raden att läsa som ett kort | **Avvisad.** TASTE § 2.3 (aldrig kort) och `devices.md` § 9 |
| Mallsidan "faller isär", skakar eller får sina element att glida ur läge | En gång per besök | Skämt | ~800 ms | Ingen, och den förvandlar en ärlig anti-referens till en karikatyr | **Avvisad.** Copy-gate och TASTE § 4.9: sidan får bara påstå det den mätt. Ett tal som säger 9 mot 4 är starkare än en animation som säger "ful" |
| Delaren rör sig av sig själv i vila, som en autospelande demo | Konstant loop | "Liv" | ~4 s loop | Ingen | **Avvisad.** TASTE § 3 product-focused, "Rörelse: subtil, aldrig breathing", och F-002: målet i vila får inte förhandsvisa slutläget |
| Marquee med de tre exempelsajternas namn | Alltid, i loop | Fylla tomrum | Långsam loop | Ingen; Hyperborea äger redan marquee i registret | **Avvisad.** Fingerprint + TASTE § 3 (marquee hör till consumer-brand) |
| Spotlight eller magnet på avslutets mailto | Vid varje pekarnärmande | Dra blicken till handlingen | ~200 ms | Marginell | **Avvisad.** `grammars.md`, split stage bans: `spotlight`, `magnet` |
| **Delaren som scroll- och pekardriven gräns** | Hela a1, sidans topp | Det **är** argumentet | 1:1 med hand och hjul | **Ja: den är sidans nav, dess chrome och dess signatur på en gång** | **Behållen.** Split stages egen lutning, ordagrant |
| **Rubrikens före-halva som degraderas längs delaren** | En gång per besök, längs a1 | Gör påståendet synligt i typen själv i stället för i en mening om typen | Bunden till delaren, ingen egen varaktighet | **Ja: den är påståendet, demonstrerat** | **Behållen.** Den bryter paper.design-devicen med avsikt, vilket är det enda sättet att slå en referens man har lånat |

**Delight-tes, en mening.** *Delaren tippar*: besökaren får ta tag i gränsen mellan den sida hen
har och den sida hen kunde ha, känner att den ger efter, släpper — och gränsen fortsätter dit
scrollen redan var på väg, så att den dåliga sidan trycks ut ur bild av den bra.

### (6) Färg och typ

**Färgstrategi: Restrained.** Den fysiska scenen, i en mening: *två utskrifter av samma format
ligger kant i kant på ett varmt pappersark under jämnt ljus, och ett enda blått streck markerar
var den ena slutar och den andra börjar.*

Namngiven referens för strategin (brand.md: "unnamed ambition becomes beige"):
**paper.design:s färginhägnad, flyttad ett hack.** Paper hägnar in sitt enda blå till
märket och kodsyntax, aldrig till en knapp eller en länk; K4 hägnar in sitt enda blå till
**ett enda geometriskt objekt** som existerar exakt en gång på sidan, delaren. Att det är
Restrained och inte Committed är ett medvetet val: sidan är redan full av färg, men all den
färgen tillhör de två sajter som visas. K4:s eget lager måste vara nästan färglöst, annars
konkurrerar det med sitt eget bevis, och då finns det två auktoriteter i vyn (TASTE § 1).

**Föreslagna tokens** (byggaren får skärpa värdena mot uppmätt kontrast, aldrig flytta rollen):

| Token | Värde | Roll |
|---|---|---|
| `--paper` | `oklch(0.957 0.013 85)` | Arket. **Varmt**, hue 85, låg chroma. Inte kräm, inte gräddlinne, och 145° från K3:s hue 230 |
| `--paper-2` | `oklch(0.928 0.018 78)` | Andra arket: bara i a2:s liggarrännil och a6:s grund, som materialbyte mellan akter (TASTE § 4.5) |
| `--ink` | `oklch(0.26 0.021 62)` | Bläcket: rubrikens "efter"-halva, liggarens tal, priserna, avslutsraden. **Varmt** nästan-svart, aldrig ett kallt `#111` på varmt papper |
| `--ink-2` | `oklch(0.62 0.014 70)` | Rubrikens "före"-halva och kickernas dämpade ton. Endast displaygrad och 11 px mono, aldrig brödtext |
| `--hair` | `oklch(0.80 0.010 78)` | Hårlinjer i skillnadsliggaren och under tjänsteraderna. Aldrig typ |
| `--blue` | `oklch(0.47 0.13 252)` (= `#1E5E9C`) | **Enda accenten. Bara delaren.** Aldrig en yta, aldrig en länk, aldrig en ram, aldrig ett tal, aldrig en knapp |

Rollregler, formulerade så att de går att granska: *accenten finns på exakt ett objekt, och
det objektet existerar exakt en gång på sidan* (mode-inhägnaden, skärpt från komponenttyp till
objekt) och *accenten är aldrig text* (paper-regeln, ordagrant övertagen: blått får aldrig
sättas som stor text eller som en länk). Noll `box-shadow`, noll `backdrop-filter`, noll
gradient, radie 0 överallt i K4:s eget lager.

Kontrast som byggaren måste mäta, inte anta: `--ink` på `--paper` ≈ ΔL 0,70, godkänt med bred
marginal. **`--ink-2` på `--paper` är den kritiska:** den ligger nära AA-gränsen och används
därför bara i displaygrad (rubrikens före-halva) och i 11 px mono med tracking, aldrig i
brödtext — kör `contrast.py` per par i R3 och skriv siffran i NOTES.md. `--blue` mäts inte mot
text alls, eftersom den aldrig sätter text; den mäts som yta mot `--paper` så att delaren syns
som en linje, inte som en skugga.

**Typsnitt — brand.md:s fyra steg, utförda.**

1. **Tre varumärkesord, fysiska objekt-ord:** *jämförd · tryckt · varm.* (Inte "modern", inte
   "premium". Objektet är två utskrifter kant i kant på ett varmt ark.)
2. **Reflexlistan, alltså de tre jag skulle gripa efter först:** Inter, Geist, Instrument Sans.
   **Alla tre avvisade** — de står på brand.md:s reflex-reject-lista och dessutom i
   r1–r7-listan. `before-ai-slop.html` kör dessutom hela sidan i Inter (mätt: `"Inter": 61`),
   så Inter är i den här cellen bokstavligen antagonistens typsnitt.
3. **Katalogen, med objektet i huvudet:** foldens rubrik är **en enda rad i två fyllnadsfärger
   med identiska metriker**. Devicen fungerar bara om snittet är så jämnt i färg att
   färgbrytningen är den enda händelsen på raden (paper-postens egen varning: blanda inte
   grader eller snitt). Det pekar mot en mycket jämn, karaktärssvag neo-grotesk — och den
   måste dessutom ha en **äkta viktaxel med lång väg**, eftersom rubrikens ena halva ska falla
   från 500 till 200 medan besökaren ser på.
4. **Korskontroll:** förstavalet sammanfaller inte med reflexen, det står inte i K3:s
   förbudslista, och det är inte K3:s val eller något av K3:s fyra reservval.

**Förbjudet** (lead-instruktionens lista, K3:s val, samt allt använt i r1–r7 och i
`sites/`): Chivo · Martian Mono · Fraunces · Newsreader · Lora · Crimson · Crimson Pro ·
Crimson Text · Playfair Display · Cormorant · Cormorant Garamond · Syne · IBM Plex Mono ·
IBM Plex Sans · IBM Plex Serif · Space Mono · Space Grotesk · Inter · DM Sans ·
DM Serif Display · DM Serif Text · Outfit · Plus Jakarta Sans · Instrument Sans ·
Instrument Serif · Geist · Geist Mono · JetBrains Mono · Public Sans · Familjen Grotesk ·
Literata · Fragment Mono · Hanken Grotesk · Archivo · Figtree · Cardo · PT Mono · Cinzel ·
Vollkorn · Italiana · Bricolage Grotesque · Manrope · Schibsted Grotesk · Bodoni Moda ·
Noto Serif JP. **Undviks dessutom** (K3:s reservkedja): Chivo Mono · General Sans · Sora ·
Spline Sans Mono.

Kontrollerat mekaniskt, inte antaget: `grep -rohiE "family=[A-Za-z+0-9]+" tests/alunix-*/
--include=*.html | sort -u` ger exakt de snitt som faktiskt laddats i r1–r7, och varken
Switzer, Onest, Host Grotesk, Satoshi, Anek Latin, Reddit Mono, Sono, Red Hat Mono,
Azeret Mono eller Sometype Mono finns i den listan. Ingen cell i r1–r7 länkar till Fontshare
över huvud taget.

**Röst — grotesk. Fem kandidater, rangordnade.**

| # | Snitt | Källa | Varför den passar objektet | Risk |
|---|---|---|---|---|
| **1** | **Switzer** (Indian Type Foundry) | Fontshare, variabel `wght` 100–900 | Extremt jämn färg i text och en ovanligt komplett viktaxel. Jämnheten är precis vad tvåtonsdevicen kräver: när metrikerna är identiska och bara fyllnadsfärgen skiljer får snittet inte ha någon egen händelse på raden. Och 100–900 ger rubrikhalvans degradering 500 → 200 gott om väg utan att någonsin nå axelns ände | Neutraliteten kan läsas som Inter-nära; motverkas av att den bara sätter **en** rad på hela sidan, i displaygrad, och att den raden alltid är tvåtonad |
| 2 | **Onest** | Google Fonts, variabel `wght` 100–900 | Samma axelbredd som Switzer men med lite varmare terminaler, vilket rimmar med det varma papperet. Enklare att vendora (Google Fonts) om Fontshare-vendoringen krånglar | Värmen i snittet plus värmen i papperet blir två värmekällor; TASTE § 1 vill ha en |
| 3 | **Host Grotesk** | Google Fonts, variabel `wght` 300–800 | Samtida grotesk med tydlig egen karaktär i displaygrad och full kursivaxel | Axeln stannar vid 300, så degraderingen 500 → 200 får inte plats; skulle behöva skrivas om till 700 → 300 |
| 4 | **Satoshi** | Fontshare, variabel `wght` 300–900 | Geometriskt neutral, mycket ren i stora grader, sitter bra ihop med en mono | Samma axelproblem som Host Grotesk, och den är närmare "SaaS-default" än jag vill vara på en sida som argumenterar mot SaaS-default |
| 5 | **Anek Latin** | Google Fonts, variabel `wdth` 75–125 + `wght` 100–800 | Breddaxeln skulle kunna låta rubriken komprimeras när halvan degraderar, alltså en andra degraderingsdimension utan snittbyte | Två axlar i rörelse samtidigt är svårt att hålla smakfullt, och breddaxeln flyttar sömmens position, vilket bryter continuity |

**Förstavalet, motiverat enligt de fyra stegen:** **Switzer**. Steg 1:s ord är *jämförd,
tryckt, varm* — jämförelsen kräver att de två halvorna av raden är mätbart identiska, och
Switzer är ritad för att inte ha någon egen händelse. Steg 2: den står inte på någon
förbudslista och är inte K3:s val eller reserv. Steg 3: det fysiska objektet är två utskrifter
kant i kant, inte en tidskriftsrubrik; ett snitt med karaktär skulle konkurrera med det bevis
som ligger under raden. Steg 4: den sammanfaller inte med reflexen (Inter / Geist /
Instrument Sans). Praktiskt: en variabel `.woff2` täcker 100–900 och håller typsnittsbudgeten
(≤ 3 filer, ≤ 300 kB, `performance.md` § 1). **Reservval om Fontshare-vendoringen faller:
Onest**, med en rad i decision ledger.

**Register — mono. Fem kandidater, rangordnade.** Rollen är liten och exakt: två kickers
(`Före` / `Efter`), skillnadsliggarens radetiketter, radnumren 01–03 och de tre bildtexterna.
Aldrig en rubrik, aldrig brödtext.

| # | Snitt | Källa | Varför | Risk |
|---|---|---|---|---|
| **1** | **Reddit Mono** | Google Fonts, variabel `wght` 200–900 | Ritad för läsning snarare än för kod, mycket jämn färg och entydiga siffror i 11 px med öppen tracking. Den läser som en etikett på ett tryckark, inte som en terminal, vilket är rätt för en sida vars ämne är två utskrifter | Liten karaktär i 11 px; motverkas av tracking 0,18 em och versal sättning |
| 2 | **Red Hat Mono** | Google Fonts, variabel `wght` 300–700 | Lugn, smal, mycket tydliga siffror; sitter neutralt bredvid en neutral grotesk | Ännu mindre karaktär än Reddit Mono |
| 3 | **Azeret Mono** | Google Fonts, variabel `wght` 100–900 | Kantig och mekanisk, stark i siffror, bred axel | K3 har den som fjärde reservval; att ta den kostar K3 ingenting (K3:s kedja är Martian Mono → Spline Sans Mono) men minskar K3:s marginal |
| 4 | **Sometype Mono** | Fontshare | Varm och rundad mono med gott siffermaterial, och värmen rimmar med papperet | Samma "två värmekällor"-invändning som Onest; dessutom K3:s femte reservval |
| 5 | **Sono** | Google Fonts, variabel `wght` 200–800 + `MONO`-axel | `MONO`-axeln låter etiketterna gå från proportionella till monospacade, vilket vore en fin teknisk detalj | En axel som ingen ser är en axel som inte är värd sin filstorlek |

**Förstavalet:** **Reddit Mono**, i register-rollen och ingen annan. Rollerna korsar aldrig
(TASTE § 4.2): Switzer sätter aldrig en etikett eller ett radnummer, Reddit Mono sätter aldrig
en rubrik, en brödtext eller ett pris.

**Krock-hantering mot K3.** K3:s val är **Chivo** (röst) och **Martian Mono** (register), och
dess reservkedja är General Sans → Sora → Anybody → Darker Grotesque respektive
Chivo Mono → Spline Sans Mono → Azeret Mono → Sometype Mono. **K4 rör ingen av dem.**
Switzer och Reddit Mono står varken som val eller som reserv i K3, så K3:s kedja är intakt och
K3:s egen krockregel ("om K4 väljer Chivo tar K3 General Sans; om K4 väljer Martian Mono tar
K3 Spline Sans Mono") **utlöses inte**. Skulle lead byta K4:s förstaval till reservkedjans
tredje eller fjärde plats (Azeret Mono, Sometype Mono) trampar K4 in i K3:s reserver, och då
måste K3 informeras med en rad i båda cellernas ledger.

### (7) Vad referenserna gör som cellen måste slå

| Låst referens | Vad den gör | Vad K4 måste göra bättre |
|---|---|---|
| **paper** (primär) | Delar en rubrik på två fyllnadsfärger med identiska metriker, och hägnar in sitt enda blå till märket och kodsyntax, aldrig till knapp eller länk | Ge de två tonerna en **betydelse**: hos Paper är brytningen retorisk (påstående mot fortsättning), hos K4 markerar den var den ena webbplatsen slutar och den andra börjar. Och sedan **förstöra devicen med avsikt**: när delaren passerar tunnas före-halvan och tappar sin identiska metrik, vilket är det enda sättet att låna en referens och ändå äga den. Paper:s device är statisk; K4:s konsumeras av berättelsen |
| **harkcap** (sekundär) | Undanhåller identitet tills pekaren är på plats (hover-reveal roster) och låter ett enda renderat objekt bära hela auktoriteten, med postens egen anmärkning att objektet saknar metafor | Flytta undanhållandet från pekaren till berättelsen, så att det händer även för den som aldrig hovrar: "efter"-sidan finns på skärmen från första bildrutan men blir inte hel förrän delaren passerat. Och ha ett objekt som **är** metaforen i stället för att sakna en: objektet är den sida kunden faktiskt kan köpa |
| **mode** (sekundär) | Hägnar in accenten till en komponenttyp och bygger ett mörkgrönt statkort kring `8.2K` med ett stapeldiagram | Skärpa inhägnaden från komponenttyp till **objekt** (delaren finns exakt en gång, en komponenttyp kan förökas), och slå statkortet genom att inte ha något: samma sorts tal, samma displaygrad, men mätta ur två filer på disk, med kommandot utskrivet, i en hårlinjeliggare utan ett enda kort |
| **gocanopy** (sekundär) | Ramar in rubriken med två små monoetiketter, en över med publiken och en under med det tekniska påståendet, så att meningen flankeras av maskinröst | Rotera inramningen 90°: `Före` till vänster, `Efter` till höger, så att metadata **namnger de två halvorna** i stället för att stötta ett påstående. Två etiketter, inte fler, och de säger bara vad man tittar på — aldrig ett värdeomdöme, aldrig ett tillstånd |
| **customer-io** (wildcard) | Iscensätter en produktskärmbild inne i ett fotograferat rum för att låna livsstilsfotots trovärdighet åt en skärmbild | Behöva noll lån. Produkten ligger inte i ett foto av ett rum, den körs i ramen och går att använda med musen (PRODUCT.md princip 1). Där customer.io lånar trovärdighet visar K4 upp den, och det är den enda referens i uppsättningen som cellen slår genom att **ta bort** ett steg |
| **before-ai-slop** (anti-referens, och här: innehåll) | Bygger ett låtsas-dashboard av `<div>`, gradientsätter ett ord i rubriken och möblerar med badge, pill, logotypvägg och tre ikonkort | Aldrig citera ett enda av dess drag i sitt eget lager, och aldrig påstå något om den som inte är mätt. Att visa den ärligt och sätta sex sanna tal bredvid den är ett hårdare argument än varje adjektiv, och det är kontrollerbart av vem som helst med kommandoraderna i § Mätning |

### (8) Rut-testet

**Kategorins default för "digital byrå", tre rader, hållen utanför:**

1. Centrerad hero med en badge-rad ovanför, ett gradientfärgat ord mitt i rubriken, två
   pill-CTA och en avatarstack, över en vit-till-lila grund, med ett dashboardkort till höger.
2. Logotypvägg av kundmärken, tre likadana ikonkort för tjänsterna, ett statband med fyra tal,
   tre priskort där ett bär "populärast".
3. Teamporträtt i rutnät, omdömeskarusell med stjärnor, kontaktformulär, och ett mörkt
   CTA-band som avslutning.

Kategorin har dessutom en fjärde default som gäller specifikt Sverige, och den är hämtad, inte
gissad: **de fem levande rubrikerna i § *Fem live-rubriker* i `runs/K4/BRIEF.md`** säger fyra
gånger av fem bara vad företaget är och var det ligger. Alunix ordagranna rubrik säger i
stället något om läsaren. Ingen ny rubrik i K4 får falla tillbaka till formen
"substantiv plus ort".

**Var målbilden möter defaulten, och vad som ändras:**

| Punkt där K4 riskerar att sammanfalla | Vad som ändras |
|---|---|
| En före/efter-slider är i sig ett byrå-default, ofta med handtag och "dra mig" | Fyra mekaniska motmedel, utskrivna i troplistans sista rad: ingen ritad affordans, delaren är sidans chrome och inte en komponent i den, den återgår aldrig till mitten, och "före" är en verklig etiketterad fil i repot |
| Ett dashboardkort i heron = kategorins reflex, och antagonisten har ett | K4 bygger noll gränssnitt. Varje gränssnitt på skärmen är en fil som serveras. Gate 47/79-kontrollen i troplistan är den mekaniska spärren, och K4:s eget lager får bara innehålla rubrik, monoetikett, liggarrad, hårlinje och delare |
| Tre tjänster i rad (01–03) = samma *form* som tre ikonkort | Tre rader ur en mask, olika radlängd, ett radnummer i 11 px mono i marginalen och en hårlinje under. Aldrig tre lådor, aldrig en ikon, aldrig lika bredd |
| Tre paket med priser = samma *form* som tre priskort | En stycklista med ledarpunkter fram till en prisokolumn. Ingen ram runt något pris, ingen "populärast", ingen jämförelsetabell, och `Pris vid förfrågan` skrivs i klartext i stället för att gömmas bakom en knapp |
| Att visa kundarbete = samma *form* som logotypvägg eller projektgrid | Calyx live i folden, Hōrai och Hyperborea som två full-bleed objekt, ett i taget, med de ordagranna bildtexterna. Noll logotyper, noll kundnamn utöver de tre sajterna |
| Sticky topprad med länkar och en CTA-knapp | Ingen topprad alls. Navigationen är delaren, och kontakten är en mailto i löpande text |
| Ett mörkt CTA-band som avslutning | Avslutet ligger på samma varma papper som resten av sidan och är avsiktligt osymmetriskt. Ingen inversion, ingen knapp, ingen footerrad |
| Siffror som "bevis" (betyg, antal projekt, år i branschen) | Existerar inte. PRODUCT.md § absences förbjuder dem. Varje tal på sidan är antingen mätt ur en fil på disk med kommandot utskrivet, eller `26 900`, `38 900` eller `01–03` |

---

## Öppet

- **Q11** (`QUESTIONS.md`): planens § 7.5-lista över förväntade katalogposter för K4 stämmer
  till 60 % med `select.py`s deterministiska utfall; `future-fur` föll på ett poäng och en
  alfabetisk tiebreak, `dovetail` på sitt register. Antagande tills svar: skriptets rad gäller.
- **Q12** (`QUESTIONS.md`): PRODUCT.md § Operating Context säger "en ram som visats får aldrig
  transformeras eller tonas efteråt", men K4:s signatur kräver att mallsidans mättnad faller.
  Antagande tills svar: regeln gäller de **tre Alunix-exempelsajterna**, inte antagonisten, och
  ingen ram transformeras eller skalas någonsin.
- **Q13** (`QUESTIONS.md`): demo-skärmbilderna i `tests/alunix-concepts-r3/build/assets/` är
  daterade 2026-09-04 och de tre sajtfilerna ändrades 2026-09-09 (F-011-borttagningen av
  `prefers-reduced-motion`-blocken, okommitterat i arbetskatalogen). Antagande tills svar:
  skärmbilderna ska skjutas om innan de används.
