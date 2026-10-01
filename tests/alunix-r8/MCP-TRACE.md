# MCP-spår — V3e, isolerad körning 2026-09-22

Syftet med sessionen är att mäta hur de två MCP:erna fungerar isolerat, med
design-pluginen och alla design-skills avstängda. Den här filen är spårningen:
varje anrop till `inspo` och `ui-skills`, i ordning, med parametrar, vad som kom
tillbaka och **var det landade**. Ett anrop som inte påverkade något är ett fynd i
sig och redovisas som sådant.

Design-pluginen (`anti-slop-design`) och `frontend-design` är avstängda.
42 design-skills är `off` via `skillOverrides` i `.claude/settings.local.json`.
`DESIGN_HOOKS_DISABLED=1` satt. Verifierat empiriskt: en probe-fil med lila
gradient, Inter och em-dash skrevs utan att någon gate nekade.

---

## 1. `inspo`

| # | Verktyg | Parametrar | Utfall | Landade i |
|---|---|---|---|---|
| i1 | `get_filters` | — | Hela vokabulären: 19 macrostructures, 11 stilar, 24 branscher, de tre mätta axlarna `paperBand`/`displayClass`/`accentHue` + `macrostructureCoverage` | Nej — ren orientering. Bra att den finns; gjorde att jag kunde läsa `axes`-strängarna i senare svar. |
| i2 | `recommend` | brief: *warm print-editorial website for a Swedish web design studio…*, `pageType=landing`, `mode=light`, `detail=standard` | Pick: `feature-stack`. Shortlist: `split-studio` (5 exemplar), `marquee-hero` (4). Evidence över 24 sajter: `paperBand` light 67 %, `displayClass` grotesk-sans **75 %**, `accentHue` warm 42 %. 5 avvikare namngivna. | Pick:en användes **inte** — se fynd 2. Evidence-blocket användes: det sa att grotesk-sans är 75 % av gravitationen i kategorin, vilket är det jag tog ställning mot. |
| i3 | `search_screens` | *editorial print brochure design studio serif typography paper*, `mode=light`, `vibe=warm`, `limit=6`, `detail=concise` | 6 träffar. `christophrauscher-de` (ockra/bläck, serif på rutnät), `humahome-com--sell-html` (terracotta editorial, högkontrast-serif), `houseofhoney-com`, `hay-com`, `brethrendesignco`, `kentcdodds` | Nej — se fynd 1. Riktningen den pekade mot är husets mest förbjudna register. |
| i4 | `get_screen` | `christophrauscher-de` | Autopsy: 50/50-delning, GTAlpina-Light serif mot Faktum sans, #ab5b04 + #2b231d. `axes`: mid / grotesk-sans / warm. | Nej — samma skäl som i3. |
| i5 | `get_screen` | `humahome-com--sell-html` | Autopsy: helbredds hero-block #dcdccb, högkontrast-serif med **ett kursiverat ord** (”love it”), Season Mix + Season Sans. `axes`: light / grotesk-sans / warm. | Nej — det kursiverade ordbytet är exakt det husets gate 89 fäller. |
| i6 | `search_screens` | *design studio showing live client websites as evidence, embedded real sites, studio portfolio*, `industry=agency`, `pageType=landing`, `limit=8`, `detail=standard` | 8 träffar, två med full autopsy. **`nbstudio-co-uk`** — terracotta + djupcharcoal, filterrad, och verk visade som **katalogiserade artefakter med etiketter under**. `emigre-com` (provark som form, i7), `exoape-com` (monumental lowercase display skuren av viewportkanten), `eng-dipsy-team` (typen ÄR bilden). | **Ja — detta är källan till riktningen.** |
| i7 | `find_examples_for_macrostructure` | `catalogue`, `limit=4`, `detail=concise` | 4 träffar, `emigre-com` överst. Bekräftade att ”provarket/uppslagsboken” är en verklig macrostruktur och inte en påhittad form. | **Ja — bekräftade layouten.** |

**Fynd 1 — MCP:n svarar snällt på fel fråga.** mina två första sökningar utgick från
*stil* (”editorial print, serif, warm”), inte från *produkten*. De gav sex träffar
och två fulla autopsier, alla i ett register som husets egna spärrar fäller: gate 89
(cream + serif + kursivt ordbyte + terracotta) och `SKILL.md` rad 61–72 där samma
kombination listas som ett av tre lägen som känns igen som genererade på fläcken.
Ingenting i svaren varnade för det. Verktyget har ingen aning om vilka regler
mottagaren arbetar under, och `recommend`s evidence-block beskriver **kategorins
gravitation**, inte vad som är bra för just den här produkten. Det är användbart,
men bara om man läser det som ett mått på hur många andra som gör samma sak.

**Fynd 2 — `recommend`s `pick` pekade fel, och sa det själv.** Den valde
`feature-stack` för att den var vanligast bland träffarna (4 av toppresultaten) och
skrev rakt ut att shortlisten innehåller runners-up om de passar briefen bättre.
Aktuell produkt är en byrå som säljer *hantverk i första intrycket* och visar tre
levande sajter — `split-studio` låg tvåa med 5 exemplar. Picken är alltså inte en
rekommendation, den är en majoritetsröst. Den bör läsas som sådan.

**Fynd 3 — det som faktiskt fungerade var att söka på problemet, inte på stilen.**
Anrop i6 formulerades som *sidans formproblem* (”visa levande kundsäjter som
bevis, inbäddade”) i stället för som en estetik. Det gav i ett enda anrop både
`nbstudio-co-uk` (katalogiserade artefakter med etiketter — layouten) och
`exoape-com` (monumental typ skuren av kanten — greppet). Det är samma verktyg, samma
budget, och en helt annan träffsäkerhet. Kostnaden var identisk.

**Budget:** 7 anrop. `recommend` 1, `search_screens` 3 (rekommenderat tak är 1–2),
`get_screen` 2, `find_examples_for_macrostructure` 1. Den tredje sökningen var den
som bar; de två första var brus. En ärlig körning hade varit 4 anrop.

---

## 2. `ui-skills`

| # | Verktyg | Parametrar | Utfall | Landade i |
|---|---|---|---|---|
| u1 | `list_skills` | (inget) | **Kraschade på storlek:** 114 390 tecken / 1 842 rader, över gränsen. Texten skrevs till en fil i stället. Ingen trunkering, ingen varning i förväg, inget sätt att begära en sammanfattning. | Nej. Ett tomt `list_skills` är oanvändbart som första anrop. |
| u2 | `list_skills` | `query="design"` | 70 skills, hela registry-poster med `name`, `pathSlug`, `description`, `url`. | Delvis — se fynd 4. |
| u3 | `get_skill` | `name="emilkowalski/emil-design-eng"` | Hela skilldokumentet returnerat: `# Design Engineering`, Initial Response, Animation Decision Framework, Sonner-principerna, Review Checklist-tabellen. Ingen storleksgräns nådd, ingen varning. | **Ja — som bevis, inte som byggmaterial.** Se fynd 4. |
| u4 | `get_skill` | `name="zeke/swiss-design"` | Sex principer, typskala, stencolorit med opacitetshierarki, 8 px-basenhet, 12-kolumnsrutnät, responsiva regler, gotcha-lista, plus fyra referensfiler. | **Ja — ändrade ett beslut i byggspecen.** Se fynd 6. |

**Fynd 6 — ui-skillen kom in mitt i bygget och ändrade ett beslut. Det är mätningens
mest användbara utfall.**

Anropet gjordes **efter** att byggspecen var skriven och byggaren hade börjat. Det var
avsiktligt: riktningen kom från `inspo` (form), hantverket skulle komma från
`ui-skills` (utförande). Vad som hände var att hantverksskillen gick in och ändrade en
**strukturell** detalj, inte en kosmetisk:

| Beslut | Före u4 (min spec) | Efter u4 |
|---|---|---|
| Displayvikt | `geist-700` — tung grotesk i monumentalskala | **`public-sans-300`** — lätt grotesk. Skillens regel: *"Headings: `font-light` (300) or `font-normal` (400). Never bold for headings."* |
| Radavstånd body | inte satt | `max-w-[60ch]` — *"Wider columns hurt legibility"* |
| Sifferkolumner | inte satt | `font-variant-numeric: tabular-nums` |
| Rubrikbrytning | inte satt | `text-wrap: balance` på rubriker, `text-pretty` på brödtext |
| Basenhet | fria `clamp()`-värden | **8 px multipel** — *"All spacing is a multiple of 8"* |

Den tunga displayen var hämtad ur `eng-dipsy-team` (ultrakondenserad svart) och
`exoape-com` (monumental) — båda från `inspo`. Den lätta kom från `ui-skills`. De två
MCP:erna pekade alltså **inte** på samma svar, och skillen hade en regel för varför:
schweizisk typografi sätter rubriker lätta. Det är den enda gången i körningen som ett
anrop från `ui-skills` ändrade något som redan var bestämt, och det är därför värt att
mäta: **`inspo` gav riktningen, `ui-skills` gav en invändning mot den.**

Invändningen gäller. En lätt grotesk i monumentalskala är dessutom ett **större**
avsteg från V3d än en tung — V3d sätter redan tunga rubriker i display-storlek
(`Från samtal till lanserad sida.` i Geist 700). Att byta till lätt skiljer V3e från
V3d på en axel som `inspo`-referenserna inte täckte.

Konsekvens för arbetet: **v1 byggs mot den gamla specen och får behålla den tunga
displayen.** Ändringen körs som en riktad v2 efter pixelgranskningen, så att
skillens bidrag går att se som en före/efter-bild i stället för som ett påstående.
u4 loggas därför med utfall "ändrade specen", inte "landade i v1".

**Övriga regler ur u4 som är billiga att ta med i v2** (de krockar inte med något i
specen): 44×44 px touch-target, `:focus-visible`-ring i stället för `outline: none`,
`color-scheme` och `theme-color` satta, inga raka citattecken och inget `...`
(förekommer i den svenska copyn — kontrolleras), hårt mellanslag mellan värde och
enhet (`26 900 kr`, `96 px`).

**Fynd 7 — `get_skill` saknar storleksgräns och returnerar hela filen.** `u3` och
`u4` gav 20 000 respektive 14 000 tecken utan varning och utan möjlighet att be om
ett utdrag. `list_skills` utan `query` kraschade på 114 390 tecken (u1). Registret
har ingen `describe`-nivå mellan "metadata om 70 skills" och "hela dokumentet".

**Fynd 4 — VERIFIERAT: `ui-skills` serverar samma innehåll som det som stängdes av.**
Detta är den viktigaste observationen i körningen.

Jag jämförde `get_skill("emilkowalski/emil-design-eng")` mot den lokala
`C:\Users\Anton L\.claude\plugins\cache\super-intelligence\...\skills\emil-design-eng\SKILL.md`
(28 005 byte, `off` i `skillOverrides` denna session). **Brödtexten är samma
dokument.** Samma rubriker i samma ordning, samma kodblock, samma tabeller:
`# Design Engineering`, `## Initial Response`, `## Core Philosophy`,
`## The Animation Decision Framework`, `## The Sonner Principles`,
`## Review Checklist`. Enda skillnaden är frontmattern: den lokala kopian har en
lång trigger-lista och `user-invocable: true`, ui-skills-kopian en kort
`description`.

Konsekvensen: **att sätta en skill till `off` i `skillOverrides` stänger av
filen, inte kunskapen.** Samma text finns kvar bakom ett MCP-anrop, och anropet
nekas inte, varnas inte och kostar ingenting att göra. Det gäller inte bara
`emil-design-eng`: registret innehåller även `pbakaus-impeccable`,
`leonxlnx-taste-skill` (`design-taste-frontend`),
`leonxlnx-imagegen-frontend-web`, `leonxlnx-imagegen-frontend-mobile`,
`leonxlnx-image-to-code-skill` och `anthropics-frontend-design` — samtliga
motsvarigheter till skills som står som `off` i den här sessionen.

**Detta är avsiktligt, inte ett fel.** Anton stängde av sina befintliga skills för
att göra testet rättvist: `ui-skills` ska vara nåbar, och frågan är inte *om*
agenten kan nå designkunskap utan **vilka skills den väljer, hur den använder dem,
och när**. Att samma text finns på båda ställena är själva förutsättningen för
mätningen — det är därför utfallet går att jämföra med vad den avstängda kedjan
hade gjort.

Det jag ska redovisa är därför inte läckan utan **urvalet**: vilken post som
valdes, vid vilket tillfälle i bygget, vad den bidrog med, och vilka poster som
förblev ovalda. Mätprotokollet står i §5.

**Fynd 5 — `ui-skills` är ett register, inte ett uppslagsverk, och `inspo` löser en
annan uppgift.** Registret har 70 poster, flera är samma skill under olika konton
(`vercel-labs-web-design-guidelines` och `antfu-web-design-guidelines`;
`anthropics-frontend-design`, `bencium-bencium-innovative-ux-designer` och
`leonxlnx-taste-skill` har i praktiken samma beskrivningstext). `query` matchar mot
`pathSlug`, `name` och `description`, och beskrivningarna är skrivna som *vad
skillen är* ("Comprehensive UI/UX design intelligence with 50+ styles") och inte som
*när den passar*. En fråga som "vilken skill hjälper mig sätta ett provark i papper"
har inget svar i registret.

Arbetsfördelningen som blev tydlig: **`inspo` svarar på form** (layout, struktur,
register — den gav riktningen), **`ui-skills` svarar på hantverk** (hur en enskild
detalj utförs). Ingen av dem svarar på uppgift. I den här körningen behövdes
`inspo` för att komma fram till *vad* som skulle byggas, och `ui-skills` hade varit
rätt verktyg *efteråt*, för detaljerna — vilket är varför u3 inte landade i
byggmaterialet.

---

## 3. Kedjan — från anrop till pixel

```
i6  search_screens  "design studio showing live client websites as evidence"
        │
        ├── nbstudio-co-uk ....... layouten: verk som katalogiserade artefakter
        │                          med etiketter, filterrad, linjerat register
        ├── exoape-com ........... greppet: monumental typ skuren av viewportkanten
        └── eng-dipsy-team ....... typen ÄR bilden; massivt negativt rum
        │
i7  find_examples_for_macrostructure("catalogue")
        │
        └── emigre-com ........... bekräftar formen: provarket som macrostruktur
        │
        ▼
   BYGGSPEC.md §2–§4   register (svalt papper, bläck, EN grön tryckfärg)
                       + layout (monument-hero, numrerat register,
                         provark med etikettremsor)
        │
        ▼
   runs/V3e/index.html
```

Anrop i2–i5 landade inte i bygget. De står kvar i tabellen ovanför för att kedjan
ska gå att granska i efterhand: fyra av sju `inspo`-anrop gav ingenting som gick att
använda.

---

## 4. Byggrundor och pixelgranskning

Kedjan är orkestrerad i rundor. Byggaren är en Sonnet-subagent; **pixelgranskningen
är min egen** och varje fynd nedan är mätt, inte bedömt på känsla.

### Runda 1

Byggaren skrev `runs/V3e/index.html` (49,5 kB) mot `BYGGSPEC.md`.
Byggaren rapporterade två egna fynd: `<figure>`:s webbläsardefault (`1em 40px`) drog
in varje ram 40 px från sin kolumn, och den delade tändningen låg på en
`IntersectionObserver` som tappade element vid hopp — den byttes mot en skroll-linje
plus en `ResizeObserver`.

**Min granskning, mätt:**

| Vad jag mätte | Utfall |
|---|---|
| Sidhöjd 1440 | 9 248 px (V3d: 30 926 px — akterna som pinnades är borta, allt är flöde) |
| Sektioner | `#hero` 66–1221 · `#tes` 1221–1945 · `#process` 1945–3290 · `#case` 3290–7413 · `#pris` 7413–8253 · `#kontakt` 8253–8988 · footer 9117–9248 |
| Konsolfel | inga (Tailwind-CDN-varningen kommer från de **inbäddade** sajterna) |
| Horisontell overflow | 0 |

**Fynd 1 — inbäddningen monteras inte vid hopp.** Vid `scrollTo(0, 3300)` och 20 s
väntan: `iframe[0]` (`calyx.html`) `src: null`, `data-src` kvar — aldrig monterad.
`iframe[1]` (`horai.html`) monterad, 197 noder, 9 906 px innehåll. Vid **gradvis**
skroll monteras båda korrekt. Alla föräldrar synliga, ingen `content-visibility`,
ingen opacitet. Slutsats: felklassen sitter i observatören, inte i ramen — samma
felklass byggaren just fixat för texttändningen, kvar för inbäddningarna.

**Fynd 2 — första skärmen är tom.** Rubriken börjar ~580 px ned i den 900 px höga
första skärmen. Sidans tes är "första intrycket är digitalt"; första intrycket är
tomrum.

**Fynd 3 — accenten läser som länkfärg.** `visitkort` i h1 står i tryckfärgsgrönt och
är sidans mest framträdande ord. Det ser klickbart ut.

**Fynd 4 — påhittad copy.** Prov 03 Hyperborea bär `Konferens, Lund` och tre
liggarrader som är **Calyx** rader, inte Hyperboreas. `Hyperborea` och `Konferens,
Lund` finns inte i V3d:s synliga text.

**Fynd 5 — jag höll på att rapportera ett falskt fel.** Min första mätning skedde
utan att skrolla alls, och konstaterade `src: null` på båda ramarna. Det är **korrekt
lat beteende** — ramen monteras först inom en skärmhöjd. Att jag tog det som en bugg
berodde på att jag mätte vid `scrollY=0` och drog slutsatsen innan jag testat den
väg en läsare faktiskt tar. Fynd 1 står kvar därför att det reproduceras vid **hopp**,
vilket är en verklig läsarväg (ankarlänk, Page Down, återställd position).

**Vad som fungerar:** processregistret (`01`–`07` i grön mono, namn i display,
brödtext till höger, hårlinjer emellan) är riktningen som lyckas. Också: tesen som
numrerad utsaga, provarkets etikettremsa, den tryckta provetiketten, och att grönt
och papper håller sig borta från V3d:s grafit och blå.

### Runda 2 — riktad fix, dispatcherad

Sex fel adresserade: inbäddningarnas montering, herons första skärm, accentens roll,
prov 03 bort och Hyperborea-bilden tillbaka till tesen, typografin och rytmen enligt
`zeke/swiss-design` (lätt display, 8 px-basenhet, `tabular-nums`, `max-w-[60ch]`,
`text-balance`/`text-pretty`, 44 px mål, `:focus-visible`, `color-scheme`), och
kapitelstämpelns styrka. Fixaren är ålagd att mäta om båda felen själv och redovisa
siffrorna.

**Kvar från `u3` (`emil-design-eng`) utan att ännu vara tillämpat:** reglerna för
knapp- och fältillstånd i kontakten (`:active { transform: scale(0.97) }`,
`transition` på exakta egenskaper i stället för `all`, aldrig `scale(0)` som
ingångsläge, ingen animation på tangentbordsutlöst handling). Anropet gjordes som
bevis, inte som byggmaterial — men innehållet visade sig tillämpligt på
interaktionslagret och kontrolleras i runda 2:s pixelgranskning.

### Runda 2 — verifierad av mig

Fixaren hittade **en andra bugg i samma block**, och den förklarar asymmetrin exakt:
monteringen sköts in i en stängning över slingvariabeln `var f`. Låg två ramar i samma
svep pekade båda på den sista — den monterades två gånger (tyst no-op) och den första
aldrig. Observationsfönstret bakas nu in med en IIFE, och monteringen ligger i samma
`update()`-svep som tänder raderna.

**Min oberoende verifiering, inte byggarens siffror:**

| Mätning | Före | Efter |
|---|---|---|
| Hopp till 3300, 6 s → Calyx | `src: null`, 0 noder | **`src` satt, 134 noder, 6 400 px innehåll** |
| Hopp till 3300, 6 s → Hōrai | 197 noder | 197 noder |
| `#hero` | 66–1221 px (rubriken började ~580 px ned) | **72–900 px — exakt första vyn** |
| Sidhöjd 1440 | 9 248 px | 7 516 px |
| Horisontell overflow | 0 | 0 (även 390/414/768/1920 enligt fixaren) |

Heron fungerar nu: lätt grotesk i monumentalskala, bild och provetikett, allt inom en
skärm. Accenten ligger inte längre på `visitkort`. Prov 03 är struket och
Hyperborea-bilden tillbaka i tesen där V3d har den.

**Fynd 8 — den kvarvarande kompositionsdommen, mätt.** I varje prov sträcker rutnätet
inbäddningens ruta till liggarens höjd, men iframen inuti är fast 465 px:

| Prov | `.prov` | figure | iframe | tomt under |
|---|---|---|---|---|
| 01 Calyx | 1 252 px | 996 px | 465 px | **~530 px** |
| 02 Hōrai | 1 451 px | 1 196 px | 465 px | **~730 px** |

En öppen kolumn som inte bär vikt, i sidans huvudsektion. Det bryter mot husets regel
att varje öppen kolumn måste bära något. Åtgärden är motiverad och inte dekorativ: gör
inbäddningen klibbande inom sin ruta så att läsaren kan läsa "Utbudet som prislista"
med den faktiska prislistan levande framför sig. Dispatcherad som runda 3.

### Runda 3 — klibbande inbäddning, verifierad av mig

Åtgärden blev en enda regel i brytpunkten där tvåkolumnsläget deklareras:
`.prov-embed .frame{position:sticky;top:32px}`. Den mest sannolika blockeraren
(`overflow-x: clip` på `.prov` skulle kunna skapa en egen scrollport) föll på mätning:
`clip` skapar ingen rullåda, så fästet mäter mot vyn.

**Min oberoende mätning av iframens `getBoundingClientRect().top` i vyn:**

| Prov | position 1 | position 2 | position 3 | släpp |
|---|---|---|---|---|
| 01 Calyx | 33 | 33 | 33 | −63 |
| 02 Hōrai | 360 | **33** | **33** | −112 |

Båda låser på 33 px och släpper mot rutans nederkant i stället för att följa med vyn
ut. Spegelvändningen i prov 02 beter sig identiskt. Horisontell overflow 0.

**Bonusfynd som fixaren gjorde:** `ō` i `Hōrai` föll till Arial. Orsaken var inte att
typsnittsfilerna saknar makronet — `U+0304` finns i alla tre med GPOS-fäste — utan att
`U+014D` saknades i `unicode-range`, så bokstaven skickades till fallbacken innan
någon komposition hann ske. Insatt i alla tre `@font-face`: 61,72 px, pixelidentisk
med filens egen sammansatta glyf.

### Slutkontroll på den färdiga filen

| Kontroll | Utfall |
|---|---|
| Synliga strängar i V3e som **inte** finns i V3d | **2** — `Er hemsida är` och `nutidens visitkort`, alltså h1 delad i två spann. Elementets text är tecken för tecken identisk. **Noll påhittade strängar.** |
| Strängar i V3d som saknas i V3e | 9 — ritningens måttsatta text (`320`, `768`, `1440`, `7 rem`, `16:9`, `96 px`, `Sektionsritning av processen`, dess `<desc>`) samt hela h1-strängen, som är en artefakt av delningen. Allt utom h1 avsiktligt borttaget med ritningen. |
| Em-dash i synlig text | 0 |
| `border-radius` över 0 | 0 |
| `prefers-reduced-motion` | 0 |
| `will-change` i vila | 0 |
| Horisontell overflow | 0 vid 390/414/768/1440/1920 |
| Inbäddningar vid hopp | båda monterade inom 1 s |

### Boarden

V3e ligger som **femte flik**: `board.json` har riktningen `V3e · Katalogen · provarket`
och `board/cells/V3e-r8/` är kopierad från `runs/V3e/`. Verifierat: `board.html` 200,
`/api/state` listar fem riktningar med `cellsExist: true` för alla, och tangent **5**
byter boarden till `cells/V3e-r8/index.html`.

V3d:s cell uppdaterades samtidigt — den var en fix bakom (`runs/V3d` 23:16 mot cellen
23:08, F1–F5:s a11y-fix saknades). Annars hade boarden dömt en sida som redan var
åtgärdad.

### Vad MCP:erna bidrog med, summerat

| Bidrog | Anrop | Vad |
|---|---|---|
| Riktningen | i6, i7 | Provarket: verk som katalogiserade artefakter med etiketter (`nbstudio-co-uk`), monumental typ skuren av kanten (`exoape-com`), provarket som macrostruktur (`emigre-com`) |
| En invändning mot riktningen | u4 | Lätt display i stället för tung, 8 px-basenhet, `tabular-nums`, `max-w-[60ch]` — ändrade ett beslut som redan var fattat |
| Ingenting | i2, i3, i4, i5, u1, u2 | Två stilformulerade sökningar i ett register husets spärrar fäller; en `list_skills` som kraschade på storlek; ett register som inte går att söka på uppgift |
| Bevis, ej byggmaterial | u3 | Verifierade att avstängda skills finns kvar via MCP:n |

Fyra av sju `inspo`-anrop och två av tre `ui-skills`-anrop gav ingenting som gick in i
bygget. Det som bar var **ett** anrop formulerat som produktens formproblem.

---

## 5. Instruktionerna fanns — i tre lager, och jag läste ett av dem halvt

Upptäckt i efterhand, efter att Anton frågade om källan. `inspo` är `Nutlope/inspo`,
hostad på `https://inspomcp.dev/api/mcp`.

| Lager | Var | Vad det täcker | Läst? |
|---|---|---|---|
| Serverinstruktionerna | injicerade i systemprompten | **5 verktyg** (`recommend`, `search_screens`, `get_filters`, `get_screen`, `get_collection`) + budgetregeln + de två kompositionsreglerna | Ja, delvis |
| `apps/mcp/README.md` | GitHub | **alla verktyg**, argument, `INSPO_MAX_TOKENS`, `INSPO_PROFILE`, `INSPO_IMAGES`, budgetmekanik, `didYouMean` | **Nej** |
| Sajtens `/mcp`-sida | inspomcp.dev | installation, klient-snuttar | **Nej** |

**Det avgörande fyndet:** serverinstruktionerna beskriver fem verktyg. De övriga elva
nämns ingenstans i det lager agenten faktiskt får. Fyra av dem ger **byggmaterial i
stället för referenser** — och det är exakt de fyra som aldrig anropades:

| Verktyg | Vad det ger | Anropat? |
|---|---|---|
| `get_design_system(slug)` | Hel DESIGN.md: riktiga typsnitt, frekvensrankad palett, **CSS-variabler**, typskala, avståndsskala, färgroller | **Nej** |
| `get_reference_jsx(type, id)` | **Kopieringsbar JSX** för en av 68 referenskomponenter | **Nej** |
| `compare(slugs[])` | 2–4 sajter sida vid sida: vad de **delar**, register, typskalor, containerbredd | **Nej** |
| `find_reference_components(type?)` | Index över de 68 kanoniska referenskomponenterna | **Nej** |

Oanvända därutöver: `find_similar`, `get_site_pages`, `list_collections`,
`get_collection`, `find_by_color`, `find_components`. **7 av 16 verktyg användes, alla
ur sök-familjen.**

**Arkivets storlek:** 2 320 sidor över 832 sajter. Jag såg som mest åtta rader per
sökning.

**Budgetmekanik jag inte kände till:** varje listverktyg tar `maxTokens` (vinner över
`INSPO_MAX_TOKENS`); `INSPO_IMAGES=none` ger textsvar där varje resultat fortfarande
bär `autopsy`, `northstar`, palett och typsnitt — modellen "ser" genom text;
`INSPO_PROFILE=lite` skär 15 verktyg till 9. Inspos egen mätning: ett `recommend` är
~10 kB text med bilder av och ~41 kB med miniatyrer på, och resultat **kostar inte en
gång** — de läses om varje efterföljande tur.

**De två kompositionsreglerna** som `recommend` och serverinstruktionerna bär till
varje agent (`heroGuidance`: heron får aldrig svämma över första vyn;
`spacingGuidance`: 80–160 px mellan sektioner, copy i centrerad vadderad kolumn)
returnerades i det första anropet. `heroGuidance` bröts ändå och fick rättas i en egen
runda. Reglerna levereras i svaret och är lätta att läsa förbi.

**Varför detta hör i spårningen:** mätningen skulle visa *vilka skills agenten
använder, hur och när*. Svaret på "vilka" är att verktygsytan är 16 verktyg bred, att
instruktionslagret bara beskriver en tredjedel av den, och att agenten därför använde
den smala familjen — sök och titta — och aldrig den som ger tokens och komponentkälla.
Det är inte slarv. **Det är vad en agent gör när halva verktygsytan är odokumenterad i
det lager den kan se.**

---

## 6. Dokument som hör till den här körningen

| Fil | Vad |
|---|---|
| `MCP-TRACE.md` | Denna fil. Varje anrop, varje fynd, varje mätvärde |
| `INSPO-MCP-INSTRUKTION.md` | Så används MCP:n. Alla verktyg, budget, arbetsflöde, antimönster. **Föreslagen** — bör flyttas till `skills/design/references/` via live |
| `HANDOFF-V3e.md` | Handoff till nästa agent: vad som finns, vad som är bra, diagnosen, vad nästa försök ska göra annorlunda |

---

## 7. Logg — fortsättning

| # | MCP | Verktyg | Parametrar | Utfall | Landade i |
|---|---|---|---|---|---|
| — | — | — | — | — | — |
