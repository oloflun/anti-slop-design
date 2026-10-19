# V3e · Katalogen · provarket — rapport

Sidan serveras på `http://127.0.0.1:3305/tests/alunix-r8/runs/V3e/index.html`.
Alla siffror nedan är uppmätta i Chromium (Playwright 1.63, headless) mot den
servern, inte lästa ur koden.

Filen har gått genom tre riktade pass. **Tredje passet står först** och är det
som gäller; de två tidigare ligger kvar orörda under sina egna rubriker som
historik.

| Pass | Vad det gjorde | Avsnitt |
|---|---|---|
| Tredje (2026-09-22) | Inbäddningen klibbar i sin ruta; `ō` i `Hōrai` tillbaka i husets typsnitt | § T1, § T2 |
| Andra (2026-09-22) | Sex fel från granskningslistan, plus två egna | § Andra passet, FEL 1–6 |
| Första | Sidan byggd | (ingen rapport i den här filen) |

---

# Tredje passet

## T1 — inbäddningen står still medan liggaren går förbi

**Felet.** I varje prov sträcker rutnätet båda kolumnerna till samma höjd, men
ramen är sin egen proportion och alltså mycket lägre än sin ruta. Mätt före:

| Prov | `.prov` | `figure` | `.frame` | `iframe` | Tomt under ramen |
|---|---|---|---|---|---|
| 01 Calyx | 1 252 px | 996 px | 467 px | 465 px | **529 px** |
| 02 Hōrai | 1 451 px | 1 196 px | 467 px | 465 px | **729 px** |

En öppen kolumn i sidans huvudsektion, utan någon vikt. Läsaren som kom till
"Utbudet som prislista" hade ingenting framför sig.

**Åtgärd.** En regel, i den brytpunkt där tvåkolumnsläget deklareras:

```css
.prov-embed .frame{position:sticky;top:32px}
```

32 px är på 8 px-enheten och ligger under varje överkant: topline rullar bort
och lägger ingenting över vyn. Ingen `position: fixed`, ingen `will-change`
(ordet förekommer nu **0** gånger i `index.html`), ingen ny rörelse — sticky är
layout. 32 valdes framför 24 med liggaren mätt: vid 1 440×900 står ramen då
mellan 32 och 499, alltså 401 px kvar av vyn under den, och Calyx fem
liggarrader mäter 172,8 / 225,4 / 199,1 / 199,1 / 199,1 px. De två första
(summa 398,2 px) ryms alltså precis under ramen, vilket är den arbetsyta
läsaren behöver för att kunna följa en rad medan den läses.

**`overflow` behövde inte röras.** `.prov` har `overflow-x: clip` sedan andra
passet. `clip` skapar ingen rullåda och därför ingen egen scrollport, så fästet
mäter mot vyn. Det är kontrollerat, inte antaget: samma mätning med regeln
orörd ger fästet.

**Mätt, efter** (1440×900):

| Prov | `.prov` | `figure` | `.frame` | `iframe` | `position` | `top` | Tomt under ramen |
|---|---|---|---|---|---|---|---|
| 01 Calyx | 1 252 px | 996 px | 467 px | 465 px | `sticky` | `32px` | 529 px |
| 02 Hōrai | 1 451 px | 1 196 px | 467 px | 465 px | `sticky` | `32px` | 729 px |

Tomrummet är detsamma — det är fördelningen som är ny. Rutan är lika hög, men
ramen följer med genom den i stället för att lämna den, så ytan under ramen är
inte längre en tom kolumn: den är ramens väg genom rutan, och den passerar
under läsaren i stället för att stå still.

**Att ramen står still.** `iframe`:ns `getBoundingClientRect().top` vid tre
skrollpositioner inuti klibbfönstret, plus en vid släppet:

| Prov | `scrollY` | `iframe.top` | `.frame.top` | `.frame.bottom` | rutan `.bottom` | slack |
|---|---|---|---|---|---|---|
| 01 | 3 300 | **33** | 32 | 499 | 1 003 | 504 |
| 01 | 3 500 | **33** | 32 | 499 | 803 | 304 |
| 01 | 3 750 | **33** | 32 | 499 | 553 | 54 |
| 01 | 3 850 | −13 | −14 | 453 | 453 | **0** |
| 02 | 4 560 | **33** | 32 | 499 | 1 194 | 695 |
| 02 | 4 850 | **33** | 32 | 499 | 904 | 405 |
| 02 | 5 200 | **33** | 32 | 499 | 554 | 55 |
| 02 | 5 300 | −12 | −13 | 454 | 454 | **0** |

Top står på 33 px genom hela fönstret — samma tal i alla tre mätningarna, i
båda proven. Vid släppet är slacket **0**: ramens nederkant och rutans
nederkant är samma linje, alltså har ramen stannat mot rutan och följer med
den ut i stället för att följa vyn vidare. Det spegelvända provet (02) beter
sig identiskt; spegelvändningen rör bara kolumnordningen och har ingenting med
fästet att göra, vilket är mätt och inte antaget.

**Var regeln gäller.** Vid 901 px och uppåt är `position` = `sticky`,
`top` = `32px`, och rutan är 1 381–1 593 px mot ramens 292–498 px. Vid 900 px
och nedåt är `position` = `relative`, `top` = `0px` — där är rutan och ramen
samma höjd (438 px vid 390, 1 013 px vid 900), och ett fäste hade varit ett
no-op. Regeln bor därför i den brytpunkt där den har något att mäta mot.

**Mjukt.** Skroll genom båda proven (2 900 → 5 600, 4,2 s, ramarna
färdigladdade före mätningen), klibb på och av i samma fil, varvat:

| CPU | | p50 | p95 | p99 | > 50 ms | långa tasks |
|---|---|---|---|---|---|---|
| 1× | klibb på | 16,7 / 16,7 / 16,7 | 16,8 / 16,8 / 33,3 | 16,8 / 16,8 / 50,1 | 0 / 0 / 3 | 0 / 0 / 1 (104 ms) |
| 1× | klibb av | 16,7 / 16,7 / 16,7 | 16,7 / 16,8 / 33,3 | 16,8 / 16,8 / 50,0 | 0 / 0 / 2 | 0 / 0 / 1 (90 ms) |
| 4× | klibb på | 16,7 i alla tre | 33,4 i alla tre | 50,0 / 83,3 / 66,6 | 1 / 3 / 2 | 1 / 4 / 3 |
| 4× | klibb av | 16,7 i alla tre | 33,4 i alla tre | 50,0 / 50,0 / 50,1 | 1 / 2 / 5 | 3 / 3 / 4 |

Vid 1× är de två konfigurationerna identiska i p50 och p95; de enstaka långa
taskarna ligger inom körvariationen och växlar inte med konfigurationen. Vid 4×
är hela sidan (inklusive två levande sajter i ramar) mättad; p50 och p95 är
identiska konfigurationerna emellan, och ordningen i >50 ms-kolumnen växlar
mellan varven.

Ett direktprov letar efter en kostnad som bildrutemätningen är för trubbig att
se: 240 skrollsteg med **tvingad** layout mellan varje steg (240
`offsetHeight`-läsningar), tolv varvade block i samma sida. Median **2,05 ms
med klibb mot 1,30 ms utan**, alltså 0,75 ms över 240 steg = **3 µs per steg**.
Riktningen är konsekvent (klibb högst i 9 av 12 block), så det är en verklig
merkostnad och inte brus — men 3 µs är 0,02 % av en bildruta på 60 Hz, och
provet mäter en väg sidan aldrig går: en tvingad synkron layout direkt efter en
programmerad skroll. Den vägen sidan faktiskt går är skrollen läsaren gör, och
den mäts i tabellen ovan. Ingen hopsamlad layout, ingen per-skroll-läsning.

**Horisontell overflow mätt efter, fem bredder:**

| Bredd | `scrollWidth` | `clientWidth` | Overflow |
|---|---|---|---|
| 390 | 390 | 390 | **0** |
| 414 | 414 | 414 | **0** |
| 768 | 768 | 768 | **0** |
| 1 440 | 1 440 | 1 440 | **0** |
| 1 920 | 1 920 | 1 920 | **0** |

`overflow-x: clip` på `.prov` är alltså kvar och gör fortfarande sitt arbete: vid
390 och 414 sticker liggarens svep ut 18 px utanför vyn och klipps, utan att
sidan går att skrolla i sidled.

**Inbäddningarna monterar fortfarande.** Färsk laddning, `scrollTo(0, 3300)`,
6 s:

| Ram | `src` | `data-src` | Noder | `title` | `loading` |
|---|---|---|---|---|---|
| calyx | `/sites/calyx.html` | borta | **134** | ordagrant | `lazy` |
| horai | `/sites/horai.html` | borta | **197** | ordagrant | `lazy` |

Vid `load`, före allt: ingen `src` satt, båda `data-src` kvar, 0 noder.
Laziness intakt.

**Konsol.** 0 fel. Två varningar, båda `cdn.tailwindcss.com should not be used
in production`, och båda kommer inifrån de inbäddade sajterna — inte ur den
här filens kod. Inga `requestfailed`.

---

## T2 — `ō` i `Hōrai` är tillbaka i husets typsnitt

**Felet var verkligt, och mekanismen var en annan än den såg ut.** Mätt i
webbläsaren på husets egen familjelista
(`Geist, "Geist Fallback", system-ui, sans-serif`) före ändringen:

| | Bredd på `ō` vid 100 px em |
|---|---|
| husets lista | **61,19 px** |
| Geist 700 ur filen, utan `unicode-range` | 61,72 px |
| Arial | 61,00 px |

61,19 = Arial × 1,003, alltså `Geist Fallback` (`size-adjust:100.3%`). `ō` stod
alltså i Arial mitt i en Geist-rubrik, precis som den förra rapporten sa.

**Men filerna saknar inte makronet.** `fontTools` på de tre woff2-filerna:
ingen av dem har U+014D i sin cmap (225 mappade kodpunkter, `U+014D SAKNAS` i
alla tre), men **alla tre har U+0304** (kombinerande makron) och ett GPOS som
fäster det på basbokstaven. Textmotorn sätter alltså ihop `ō` ur `o` + `U+0304`
ur samma fil. Kontrollmätt per fil: `U+014D` blir pixelidentisk med
`o`+`U+0304`, och marken är **inte** Arial:s — `o`+`U+0304` skiljer sig från
Arials `o`+`U+0304` i alla tre, alltså är det filens egen makron som ritas.

**Åtgärden** är därför att låta `U+014D` stå i `unicode-range` för de tre
`@font-face`-reglerna. Det är intervallet som avgör om snittet får användas för
tecknet över huvud taget; utan tecknet i listan skickas bokstaven vidare till
nästa familj innan textmotorn hinner sätta ihop något.

```diff
-  unicode-range:U+0000-00FF,U+0131,U+0152-0153,…
+  unicode-range:U+0000-00FF,U+0131,U+014D,U+0152-0153,…
```

**Mätt, efter** (`ō` i samma familjelista, samma sida):

| Kontroll | Före | Efter |
|---|---|---|
| Bredd på `ō` vid 100 px em | 61,19 px (`Geist Fallback`) | **61,72 px** (`Geist`, egen komposition) |
| `ō` pixelidentisk med `o`+`U+0304` ur husets lista | nej | **ja** |
| `ō` pixelidentisk med Arial:s `ō` | ja | **nej** |

Breddskillnaden är 0,53 px per 100 px em. I provnamnet (43,2 px) flyttar det
`ō` med 0,23 px; rubrikens radbrytning står still, och overflow är 0 på alla
fem bredder efter ändringen.

Formuleringen i den förra rapportens Osäkert-avsnitt ("Fixas med ett intervall
i en `@font-face`") var alltså rätt om åtgärden men fel om orsaken: glyfen
saknas i filen och lösningen bygger på att textmotorn komponerar den. Det
står nu också som kommentar vid `@font-face`-blocken.

**Visuellt granskat.** Provnamnet `Hōrai` avbildat för sig, och de tre filerna
sida vid sida vid 230 px em: makronet ligger över `o`, i filens egen form och
vikt, och `o`:et inuti `ō` är samma runda `o` som ordet i övrigt. Ingen Arial i
rubriken.

---

## Självkontroll, tredje passet

| Kontroll | Utfall |
|---|---|
| Filstorlek / rader | 55 163 byte / 1 020 rader (före passet: 53 279 / 995) |
| Ändrade filer i repot | **2**: `runs/V3e/index.html` och den här rapporten. Ingenting annat; kontrollerat med filfilter över repot, inte antaget. |
| Copy-paritet mot `runs/V3d/index.html` | oförändrad: samtliga synliga rader ordagranna, utom den ärvda hero-bildtexten (V3d:s `img[alt]`) |
| Em-dash U+2014 i synlig text | 0 |
| U+2011 i `SEO-optimering` | bevarad, `&#8209;`, samma form som V3d |
| Rak citattecken / `...` | 0 / 0 |
| `border-radius` i CSS | en deklaration, värdet `0` |
| `prefers-reduced-motion` | 0 |
| `outline:none` | 0 |
| `position:fixed` i CSS | 0 |
| `will-change` i hela filen | **0** (`getComputedStyle` på ramen: `will-change: auto`) |
| `var(--accent)` | 4 regler, alla katalognummer eller provets regel |
| `iframe` | `data-src` + `loading="lazy"` + `title` ordagrant, båda |
| Horisontell overflow 390/414/768/1440/1920 | 0 px på alla fem |
| Konsolfel | 0 i varje körning |
| Visuellt granskat (mina egna skärmbilder) | prov 01 klibbande, prov 02 klibbande och spegelvänt, båda släppen, 1 024 px, 768 px, 390 px, samt `Hōrai`-rubriken för sig |

---

# Andra passet

Riktad andra pass på `runs/V3e/index.html`. Filen är omskriven i sin helhet
(markup, CSS och skript) men copyn är orörd. Ingenting annat i repot är rört.

---

## FEL 1 — inbäddningarna monteras nu vid hopp

**Åtgärd.** `IntersectionObserver`-monteringen är borta. Ramarna går genom
samma skroll-linje som tändningen: `mountDue()` ligger sist i `update()`,
alltså i samma `requestAnimationFrame`-svep som tänder raderna, och körs av
`scroll`, `resize`, `ResizeObserver` på `body` och `document.fonts.ready`.
Ramen monteras när dess `getBoundingClientRect().top < innerHeight * 2`
(en dryg skärm i förväg, samma avstånd som `rootMargin: '100% 0px'` gav).
Lazy-avsikten ligger kvar: vid `load` är ingen ram inom två vyhöjder, alltså
hämtas ingen sajt. Skrivningen ligger fortfarande i en ledig lucka
(`requestIdleCallback`, timeout 600 ms), och listan krymper när ramarna
monterats så att arbetet går mot noll.

**En andra bugg i samma block.** Den gamla koden sköt in monteringen i en
stängning över slingvariabeln `var f`. Låg två ramar i samma svep pekade båda
stängningarna på den **sista** ramen: den monterades två gånger (idempotent,
alltså en tyst no-op) och den första monterades aldrig. Fönstret bakas nu in i
anropet med en IIFE.

**Mätt, före** (originalfilen, `window.scrollTo(0, 3300)`, 6 s):

| Ram | `src` | `data-src` | Noder i `contentDocument.body` |
|---|---|---|---|
| `iframe[0]` calyx | `null` | `/sites/calyx.html` kvar | 0 |
| `iframe[1]` horai | `/sites/horai.html` | borta | 197 |

**Mätt, efter** — samma körning:

| Ram | `src` | `data-src` | Noder |
|---|---|---|---|
| `iframe[0]` calyx | `/sites/calyx.html` | borta | **134** |
| `iframe[1]` horai | `/sites/horai.html` | borta | **197** |

**Mätt, efter, alla tre vägarna:**

| Väg | Resultat |
|---|---|
| `scrollTo(0,3300)` direkt efter load, 6 s | båda `src` satta, 134 / 197 noder |
| hopp 0 → 5000 → 3300 (3 s per steg) | vid 0: ingen monterad (`src: null`, `data-src` kvar) · vid 5000: båda monterade · vid 3300: båda monterade |
| gradvis skroll 0 → 5000 i 200 px-steg | båda monterade |
| vid `load`, före allt | båda omonterade — laziness intakt |

`loading="lazy"` och `title` står kvar ordagrant på båda. Inga konsolfel i
någon av körningarna.

---

## FEL 2 — heron är komplett inom första skärmen

**Åtgärd.** `.hero-clip` är nu en flexkolonn med
`min-height: calc(100svh - var(--topline-h))`. Rubriken ligger först i
kolonnen, provraden (`.hero-row`) har `flex: 1 1 auto` och tar resten, bildens
ram har `flex: 1 1 auto` med `max-height: 480px`, etiketten är
bottenankrad (`align-self: end`). Ingen `overflow: hidden`, ingen negativ
marginal, ingen `--crop`. Rubriken skärs alltså inte längre av nederkanten —
se "Osäkert" nedan, det är den enda punkten där jag gått emot en formulering i
uppdraget.

**Mätt vid 1440×900, efter `load`:**

| Mått | Före | Efter |
|---|---|---|
| `#hero` topp → botten | 66 → 1221 | **72 → 900** |
| `#hero` höjd | 1155 px | **828 px** = 900 − 72, alltså exakt första vyn |
| `#hero`-rubrikens `offsetTop` | 640 | **72** |
| `#hero`-rubrikens `rect.top` | 640 | **72** |
| rubrikens `rect.bottom` | 932 | **363,4** |
| rubrikens höjd | 291 px | **291,4 px** |
| rubrikens typsnitt | Geist 700, 158,4 px | **Public Sans 300, 158,4 px** |
| bevisbildens ram | 954 → 1221 (under vikningen) | **411,4 → 867,8** (637,2 × 456,4) |
| bildtextens underkant | — | **900** |
| provetiketten | 1070 → 1221 (under vikningen) | **699,5 → 900** |

Alltså: rubrik, bevisbild, bildtext och provetikett ligger samtliga inom
0–900 px. Tomrummet ovanför rubriken är **0 px** (rubriken börjar 72 px ned,
direkt under öppningsraden). Den gamla mätningen hade 568 px tomrum ovanför
rubriken; nu är samma tal 0.

**Sektionshöjder vid 1440×900** (topp, höjd): `#hero` 72/828 · `#tes` 900/857 ·
`#process` 1757/1160 · `#case` 2917/2837 · `#pris` 5754/804 · `#kontakt`
6558/733. Dokumenthöjd 7516 px (före passet: 9248 px med tre prov).

**Övriga bredder**, samma fyra element inom vyn: 390×844 → hero 788 px, rad
botten 201, etikett botten 711, bildram 197 px · 768×1024 → hero 968, etikett
botten 889 · 1920×1080 → hero 1008, etikett botten 1080, bildramen tar i
`max-height`-taket 480 px.

---

## FEL 3 — accenten borta ur h1

**Åtgärd.** `<span class="accent">` är borta ur `nutidens visitkort`, och
`.accent`-klassen med den. Ordet står i bläck.

**Kontrollmätt i webbläsaren** — accentfärgen `oklch(0.45 0.13 158)` förekommer
nu i exakt fyra CSS-regler, alla i de två tillåtna rollerna:

| Regel | Roll |
|---|---|
| `.num{color:var(--accent)}` | katalognumren |
| `html.js .tes-row.is-in .num` | katalognumren, tänd rad |
| `.reg-row.is-in/.is:hover/.is:focus-within .num` | katalognumren |
| `.prov.is-current .prov-rule` | den regel som markerar aktuellt prov |

Ingen accent i display-skala någonstans. `--accent-lit` är struken (den hade
ingen konsument).

---

## FEL 4 — prov 03 struket, Hyperborea flyttat till tesen

**Åtgärd.** Hela `<article id="case-hyperborea">` är borta, med sin etikett,
sitt katalognummer och sina tre liggarrader. Kvar står `01 Calyx` och
`02 Hōrai`. Hyperborea-bilden
(`/tests/alunix-concepts-r3/build/assets/demo-hyperborea.webp`, `alt`
`Startsidan för Hyperborea, en konferens i Lund`) står nu i `#tes`, i
högerkolumnen (rutnätets kolumn 8–13) med `align-self: end`, i en tunn ram och
med `loading="lazy"` — samma plats och samma form som V3d ger den
(`.thesis-figure > .thesis-photo-box`, `aspect-ratio: 16/10`, ingen bildtext).

**Strängarna borta ur synlig text.** `Hyperborea`: nej. `Konferens, Lund`:
nej. Båda kontrollerade mot `BeautifulSoup`-extraherad synlig text, noll
träffar. Rå förekomst i filen: `Hyperborea` 2 gånger — i bildens sökväg
`demo-hyperborea.webp` och i dess `alt`. `Konferens, Lund` 0 gånger.

**Om den avvägningen.** `alt`-texten innehåller ordet, och uppdraget ger den
ordagrant i samma mening som det säger att strängarna ska bort. Jag har läst
kravet som *synlig* text: `alt` renderas aldrig, den är dessutom föreskriven
av BYGGSPEC §6.9 ("återanvänd exakt") och den är bildens enda namn — V3d har
av samma skäl ingen bildtext till plåten. Ingen bildtext är hittad på i V3e
heller.

**Om provenansen, för protokollet.** De tre rader som prov 03 bar
(`Fotot bär rubriken`, `En serif för allt man läser`, `Färgen finns redan i
bilderna`) finns inte i `tests/alunix-r8/concepts.md`, och inte i någon annan
Hyperborea-källa i repot. De finns ordagrant i `runs/V3d/index.html` — som
**Calyx** liggarrader. Prov 03 tillskrev alltså Calyx designresonemang till
Hyperborea. Det var fabrikation, och det är borta.

**Copyn är oförändrad i övrigt.** Varje synlig rad i V3e är kontrollmätt mot
`runs/V3d/index.html` med `BeautifulSoup`: samtliga finns ordagrant, utom en —
`En ljuspöl faller diagonalt över ett mörkt scentyg`, som är V3d:s `img[alt]`
för hero-bilden och som BYGGSPEC §4.2 uttryckligen vill ha som synlig
mono-bildtext. Den avvikelsen är ärvd från första passet, inte införd här.
U+2011 i `SEO&#8209;optimering` står kvar i samma form som i V3d (`&#8209;`,
en förekomst i vardera filen).

---

## FEL 5 — typografi och rytm

| Punkt | Åtgärd | Kontrollmätt |
|---|---|---|
| 1. Lätta rubriker | `h1,h2,h3,h4` sätts i `--f-body` med `font-weight: 300`. `geist-700` finns bara kvar hos `.prov-name`. | `h1`, `.h2`, `.reg-name`, `.led-name`, `.tes-line`, `.lead`, `body` = Public Sans / 300. `.prov-name` = Geist / 700. Inga andra. |
| 2. 8 px-basenhet | Nya token `--ry: 96px`, `--ry-lg: 128px`; alla vertikala värden omskrivna till 8-multiplar | `--ry` 96 · `.prov` 128 · `.tes-row` 40/40 · `.reg-row` 24/24, radgap 8 · `.led-row` 24/24, radgap 8 · `.prov-strip` 0/24 · `.prov-body` 40 över, 40 radgap · `.price-row` 24/24 · `.price-reg` 48 över · `.plate-dark` 96/96 · `.contact-form` gap 32 · `.contact-label` 64 över · `.close-in` 40/40 · `.proc-head` 32 under · `.chapter` 16 under · `.hero-row` 48 över. Alla tal delbara med 8. |
| 3. `tabular-nums` | Satt som ärvd egenskap på `.num,.lab,.mono,.tes-row,.reg-row,.led-row,.price-reg,.prov-strip` | `tabular-nums` läses ut på `.num`, `.price-label`, `.price-value`, `.reg-row`, `.led-row` |
| 4. Brödtext 60ch | Ny token `--measure: 60ch`, använd på all löpande text | 7 konsumenter: `.lead`, `.reg-desc`, `.led-text`, `.plate-ingress`, `.contact-lead`, `.contact-status`, `.price-label` |
| 5. `text-wrap` | `balance` på rubriker (ärvt), `pretty` på `p` | `.h2` = `balance`, `p` = `pretty` |
| 6. 44×44 träffyta | Ny klass `.tap` (inline-flex, `min-height/min-width: 48px`), plus `min-height: 48px` på etikettens fyra rader och på knappen | `kontakt@alunix.se` 151×48 · `Boka ett möte` 416×49 · `Skicka` 119×48 · `Efter mejla oss direkt på kontakt@alunix.se` 382×48. 48 px valt framför 44 för att det ligger på 8 px-enheten och ändå klarar kravet. |
| 7. `:focus-visible` | Global ring `2px solid var(--ink)`, offset 3 px, orörd. Fältreglerna sätter ingen `outline` alls — fältets markering är underlinjen som går från hårlinje till bläcklinje | `outline:none` förekommer **0** gånger i filen; `:focus-visible` 2 gånger |
| 8. Meta | `color-scheme` = `light`, `theme-color` = **`#f3f4f6`** | `#f3f4f6` är den faktiskt målade pappersfärgen, samplad ur skärmbilden: pixel rgb (243, 244, 246). Den gamla `#f5f6f8` var fel. Faviconens `fill` är ändrad till samma värde. |
| 9. Citattecken och `...` | Kontrollerat | Rak `"`: 0 · rak `'`: 0 · `...`: 0 · em-dash U+2014: 0 · en-dash U+2013: 0. `…` i `Öppnar…` är U+2026 och står kvar. |

Rytmen går ned ett steg på telefon men stannar på 8: `--ry: 64px`,
`--ry-lg: 80px`, `--topline-h: 56px`, `.plate-dark` 48/24, `.hero-row` 32,
`.tes-fig` 40.

Övrigt som följde med typografibytet: rubrikradens höjd är nu fast
(`--topline-h: 72px`, telefon 56 px) i stället för `clamp(56px, 4.6vw, 74px)`,
eftersom hero-rutan mäter första vyn mot den och en rad som ändrar höjd med
textstorleken hade flyttat mätningen med sig. Preloaden är bytt från
`geist-700` till `geist-mono-400`: monon står i första vyn (öppningsraden och
etiketten), den tunga vikten används först nere vid proven.
Hero-bilden har `fetchpriority="high"` i stället för `loading="lazy"` — den
ligger nu bevisligen inom första vyn, och en sen bild där motbevisar herons
egen tes. De två inbäddningarna har kvar `loading="lazy"`.

---

## FEL 6 — kapitelstämpeln

**Åtgärd.** `EXEMPELCASE` står nu i 1 rem (var 0,75 rem) med
`letter-spacing: .26em` (var .14em) och i fullt bläck (var apparatgradens
dämpade), och regeln under den är dragen i bläck i **2 px** (var hårlinje i
1 px). Avståndet ned till stämpelns regel är 16 px. Den är fortfarande en
stämpel: samma versala mono, ingen accent, ingen rubrikvikt, ingen
rubrikstorlek. Ingen ny sträng är införd.

---

## Två fel som inte stod i listan, som jag ändå fixade

**1. Hōrai-spegeln var trasig.** Den spegelvända liggaren låg i praktiken
*under* inbäddningen i stället för bredvid, med en tom vänsterkolumn över sig.
Orsaken är rutnätets sparsamma automatplacering: ett objekt vars kolumnstart
pekar bakåt i källordningen flyttas till nästa rad, och liggaren
(`grid-column: 1/6`) står efter inbäddningen (`grid-column: 6/13`) i markup.
Båda barnen har nu `grid-row: 1`, så bara kolumnerna speglas.

Mätt efter (`window.scrollTo(0, 3300)`): Calyx inbäddning x 72 / liggare
x 841, båda y 6 · Hōrai inbäddning x 583 / liggare x 110, båda y 1259.
Bredder 747 och 527 i båda ark. Före åtgärden låg Hōrais liggare på y 780 mot
inbäddningens y 273.

**2. Sidan gick att skrolla i sidled på telefon.** Set-piecen glider in i sina
rutor från varsitt håll (`translate3d(±2.4rem)` = ±38,4 px), och under ca
440 px är arkets sidmarginal mindre än svepet. `document.documentElement.
scrollWidth` var 408 mot `innerWidth` 390 — 18 px horisontell skroll på varje
telefon. `.prov` har nu `overflow-x: clip` (klipper utan att skapa en
skrollcontainer). Vid stillastående läge är förskjutningen noll, så ingenting
syns av klippningen. Mätt efter: `scrollWidth − innerWidth` = **0** vid 390,
414, 768, 1440 och 1920.

---

## Självkontroll

| Kontroll | Utfall |
|---|---|
| Parsar med `html.parser`, `lxml`, `html5lib` | OK, alla tre |
| Filstorlek / rader | 53 279 byte / 995 rader (mätt i andra passet; efter tredje: 55 163 byte / 1 020 rader) |
| `<section id>` | hero, tes, process, case, pris, kontakt — alla sex |
| Dubbletter av `id` | inga (20 id) |
| Em-dash U+2014 i synlig text | 0 |
| U+2011 (`&#8209;`) i `SEO-optimering` | bevarad, 1 förekomst, samma form som V3d |
| Rak citattecken / `...` i synlig text | 0 / 0 |
| `border-radius` i CSS | exakt en deklaration, värdet `0` |
| `prefers-reduced-motion` | 0 |
| `outline:none` | 0 |
| `var(--accent)` | 4 regler, alla katalognummer eller provets regel |
| `var(--sc-p)` i rörelseegenskaper | 0 (`--sc-ps` används) |
| Interna spår (`PLAN`, `Astra`, `Target`, `gate`, `TASTE`, `C-8`, `COPY-V3d`, `cell V3c`, `F-0`, `data-preview`, `?preview=`) | 0 var |
| Iframes | `data-src` + `loading="lazy"` + `title` ordagrant, båda |
| `loading="lazy"` på bilder | tes-plåten ja; hero-bilden `fetchpriority="high"` (se ovan) |
| Copy-paritet mot V3d | samtliga synliga rader ordagranna, utom den ärvda hero-bildtexten |
| Horisontell overflow 390/414/768/1440/1920 | 0 px på alla fem |
| Konsolfel | inga, i någon körning |

Granskat visuellt (mina egna skärmbilder, 1440×900 och 390×844, hela sidan
plus varje sektion för sig, samt hopp mitt i sidan): hero, tesen med plåten,
processregistret, kapitelstämpeln, båda proven med sina inbäddningar,
prisplattan, kontakten och sidfoten.

---

## Osäkert

- **Skärningen i heron.** Uppdraget säger att rubriken "gärna" får möta
  nederkanten och skäras av, men kräver samtidigt att rubrik, bevisbild och
  provetikett **alla** ryms i första vyn. De två går inte ihop så länge
  bilden och etiketten står under rubriken, vilket BYGGSPEC §4.2 säger att de
  ska. Jag valde det hårda kravet: ingen skärning, allt inom vyn, rubriken
  direkt under öppningsraden. Vill man ha skärningen tillbaka är det
  `overflow: hidden` på rubrikens rad plus en negativ marginal — men då
  hamnar bilden och etiketten under vikningen igen.
- **Provnamnens storlek.** FEL 5.1 kallar `Calyx` och `Hōrai` "de små
  provnamnen" och vill behålla `geist-700` bara där. De står kvar i en
  etikettgrad (`clamp(1.7rem, 3vw, 2.8rem)` = 43,2 px vid 1440), ned från
  `clamp(1.9rem, 3.6vw, 3.4rem)` = 51,8 px. Skälet: med alla rubriker nu
  lätta hade ett tungt namn i 51,8 px blivit sidans tyngsta rubrik och
  motsagt viktkontrasten. 43,2 px ligger strax över liggarens egna radnamn
  (36 px) och långt under sektionsrubriken (63 px). Är "små" menat bokstavligt
  är en rad att ändra.
- **Etikettens nederkant i heron** står exakt på vikningen (900 px): etikettens
  sista hårlinje, bildtextens underkant och bildramens underkant möter alla
  900-linjen. Det är avsiktligt — heron fyller första vyn — men just den sista
  hårlinjen ligger alltså mindre än en pixel från kanten och syns först när
  man skrollar.
- **`overflow-x: clip` på `.prov`** är min lösning på sidoöversvämningen, inte
  föreskriven. Den klipper vid arkets egen kant och rör ingenting i
  stillastående läge, men en noggrannare lösning vore att korta svepet på
  smala bredder i stället.
- **`ō` i `Hōrai`** föll tillbaka på Arial: `unicode-range`
  (U+0000-00FF, U+0131, U+0152-0153 …) täckte inte U+014D. Ärvt ordagrant från
  V3d, inte infört här. **Löst i tredje passet** — se § T2. Åtgärden var rätt,
  orsaken var en annan: glyfen finns inte i filen, den komponeras av
  formgivaren ur `o` + U+0304, och det är intervallet som avgör om snittet får
  användas för tecknet.
- **Full-bild-skärmbilder lurar.** Proven tonar in via `--sc-ps`, som är 0 när
  arket ligger under vyn. En `full_page`-bild tagen vid `scrollY 0` visar
  därför `#case` tomt. Det är rörelsens avsedda utgångsläge, inte ett fel —
  men den som tar en helsidesbild rakt efter load ser ett tomt kapitel.
