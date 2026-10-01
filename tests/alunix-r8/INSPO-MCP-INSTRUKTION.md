# Så används Inspo-MCP:n

Skriven 2026-09-22 efter en körning där MCP:n användes fel och resultatet blev därefter.
Underlaget är `apps/mcp/README.md` i `Nutlope/inspo` samt vad som faktiskt hände i
körningen (spårat i `MCP-TRACE.md`). Avsedd att läsas **innan** första anropet.

**Status: föreslagen.** Dokumentet ligger i `tests/alunix-r8/` eftersom det är där
beviset finns. Det bör flyttas till `skills/design/references/inspo-mcp.md` via live
(`~/.agents/skills/design/references/`) så att designkedjan läser det — inte till
repots spegel först, enligt regeln i `GOALS.md` delmål 5.

---

## 1. Vad servern är

`https://inspomcp.dev/api/mcp`, HTTP-transport, `Nutlope/inspo`, MIT.

- **Arkivet: 2 320 sidor över 832 riktiga sajter**, desktop och mobil, med paletter,
  typsnitt, detekterad teknik och en **fold-för-fold-autopsi** per sida.
- **68 referenskomponenter** (hero, pricing, nav, footer, CTA, testimonial,
  logo-cloud, FAQ, stat, features) — var och en parad med en namngiven macrostruktur,
  med **kopieringsbar JSX**.
- **En DESIGN.md per sajt**, byggd ur DOM:en: semantiska färgroller, typskala,
  avståndsskala, CSS-variabler, containerbredd.
- Alla verktyg är read-only. Enda utgående anropet är `get_design_system(live:true)`,
  som går genom en SSRF-vakt begränsad till publika namngivna värdar.

---

## 2. De tre instruktionslagren — och att bara ett når agenten

| Lager | Var | Vad det täcker |
|---|---|---|
| Serverinstruktionerna | injicerade i agentens systemprompt | **5 verktyg** + en budgetregel + de två kompositionsreglerna |
| `apps/mcp/README.md` | GitHub, `Nutlope/inspo` | **alla 16 verktyg**, argument, env-variabler, budgetmekanik |
| Sajtens `/mcp`-sida | inspomcp.dev | installation, klient-snuttar |

**Detta är den viktigaste raden i dokumentet:** serverinstruktionerna beskriver
`recommend`, `search_screens`, `get_filters`, `get_screen` och `get_collection`.
De övriga elva — inklusive de två som ger *byggmaterial* i stället för *referenser* —
nämns inte där. En agent som bara läser sin egen systemprompt får alltså en bild av
verktyget som "sök och titta", och missar hela lagret som ger designsystem och
komponentkällkod.

I körningen 2026-09-22 användes **7 av 16** verktyg, samtliga ur sök-familjen.

---

## 3. Verktygen, och när de ska användas

### Ingången

| Verktyg | När |
|---|---|
| `get_filters()` | **Kallt, en gång, först.** Noll argument. Returnerar varje giltigt enum-värde (stilar, branscher, macrostructures, vibes, sidtyper, `paperBand`/`displayClass`/`accentHue`). Utan detta gissar agenten argument och får tomma svar. |
| `recommend(brief, …)` | **Startpunkten.** "One-call moodboard": macrostruktur-pick + shortlist, 5 exempel, upp till 3 matchande referenskomponenter, palettförslag, ett `evidence`-paket, samt `heroGuidance` och `spacingGuidance`. |

**Läs `recommend` rätt.** Dess `pick` är en **majoritetsröst**, inte en
rekommendation: den väljer den vanligaste macrostrukturen bland träffarna och säger
själv att shortlisten bär runners-up. `evidence`-blocket beskriver **kategorins
gravitation** — hur många andra som gör samma sak — vilket är ett mått att ta
ställning till, inte ett mål att matcha. I körningen 2026-09-22 valde `recommend`
`feature-stack` ("vanligast, 4 av toppresultaten") för en byrå som säljer hantverk i
första intrycket; rätt svar låg tvåa i shortlisten.

### Sökningen — formulera problemet, inte stilen

| Verktyg | När |
|---|---|
| `search_screens(query, …)` | Bred sökning med filter. |
| `find_by_color(hex, tolerance?)` | När briefen namnger en varumärkesfärg. OKLAB-avstånd, så "nära" betyder samma färjfamilj. |
| `find_examples_for_macrostructure(name)` | När formen är vald och du vill se den utförd. |
| `find_similar(slug)` | En sajts visuella och strukturella grannar. |
| `get_site_pages(siteSlug?)` | En sajts sidor i läsordning — hur en riktig produkt sekvenserar sina sidor. Utan argument: katalogen över flersidiga sajter. |
| `list_collections()` / `get_collection(slug)` | Redaktörskurerade teman. |
| `find_components(type, …)` | Verkliga komponentbeskärningar ur sajter. |

**Den viktigaste lärdomen om sökningen.** `search_screens` svarar på *form*, inte på
*stil*. En fråga formulerad som estetik ("varm editorial, serif, papper") gav sex
träffar i ett register husets egna spärrar fäller. En fråga formulerad som
**sidans formproblem** ("visa levande kund­sajter som bevis, inbäddade") gav i ett
enda anrop både layouten och greppet. Samma verktyg, samma budget, helt olika utbyte.

Formulera briefen som *vad sidan ska göra och vilket problem den löser*, inte som en
stämning.

### Byggmaterialet — det jag missade

| Verktyg | När | Varför det avgör |
|---|---|---|
| `get_design_system(slug, live?)` | Så snart en referens är vald | Hela DESIGN.md: riktiga typsnitt, frekvensrankad palett, CSS-variabler, typskala, avståndsskala, färgroller. Detta är **tokens**, inte en bild. Standard `live:true` kompletterar tunna poster med en färsk hämtning; `live:false` hoppar över nätverksanropet. |
| `find_reference_components(type?, macro?)` | När en sektion ska byggas | Index över de 68 kanoniska referenskomponenterna. |
| `get_reference_jsx(type, id)` | Direkt efter | **Fullständig, kopieringsbar JSX** för en komponent, med stämpel som namnger macrostruktur, tema och tillstånd. |
| `compare(slugs[])` | När 2–4 referenser är valda, **före** riktningsbeslutet | Delad palett, typsnitt, macrostruktur, läge, stiltaggar, typ-/avstånds-/radieskalor och containerbredd — plus **vad de delar**. Triangulerar en husstil ur några referenser. Detta är verktyget för att avgöra om referenserna pekar åt samma håll eller motstridigt. |

`compare` och `get_design_system` är de två som gör skillnad mellan "jag såg en bild
av en sajt" och "jag har sajtens tokens".

---

## 4. Budget

Resultat **kostar inte en gång**: de stannar i konversationen och läses om varje
efterföljande tur. Inspos egen mätning: cache-läsningar gick 3,3× cache-skrivningar.
Storlekar de anger: **ett `recommend`-anrop är ~10 kB text med bilder av och ~41 kB
med miniatyrer på.**

Tre rattar, i ordning:

1. **Färre, bättre riktade anrop.** Den billigaste hävstången. Budgetregeln i
   serverinstruktionerna: *ett `recommend`, en eller två `search_screens`, sedan
   `get_screen` på de tre till fem referenser du behåller är en komplett studie.*
2. **`images=none`.** `INSPO_IMAGES` = `thumbs` (standard) eller `none`.
   `none` ger textsvar utan inbäddade bilder. **Varje resultat bär fortfarande
   `autopsy`-texten, `northstar`, palett och typsnitt** — modellen "ser" genom text.
   På `images=none` returnerar listsverktygen en slimmad form
   (`northstar` + palett + typsnitt); be då om `detail:"full"` eller anropa
   `get_screen` för hela autopsin. Använd `none` när harnesket tappar MCP-bilder
   eller modellen är text-only.
3. **`maxTokens`.** Varje listverktyg tar ett per-anrop `maxTokens` som vinner över
   env-variabeln `INSPO_MAX_TOKENS` (300–200 000). Mekanik: resultatet formateras
   först koncist, sedan droppas den rankade svansen, sedan miniatyrerna, tills svaret
   ryms. **Toppresultatet och varje skalärt fält (tips, filter, hero-vägledning)
   överlever alltid**, och trimmade svar bär en `budgetNote` som säger hur många
   poster som föll bort. På den hostade endpointen: `?maxTokens=` i URL:en.

**`INSPO_PROFILE`**: `full` (15 verktyg) eller `lite` (9: `recommend`,
`search_screens`, `get_screen`, `get_design_system`,
`find_examples_for_macrostructure`, `find_reference_components`,
`get_reference_jsx`, `get_site_pages`, `get_filters`). Små modeller väljer verktyg
säkrare ur en kort lista. Claude Code får `full` + `thumbs` som standard; env-variabler
vinner alltid. Den stateless HTTP-transporten kan inte läsa klientnamnet, så
text-only-harnesk måste välja ned explicit:
`https://inspomcp.dev/api/mcp?profile=lite&images=none`.

---

## 5. De två kompositionsreglerna som följer med varje svar

`recommend` och serverinstruktionerna bär två regler till varje agent. De är mätta ur
arkivet, inte påhittade.

- **`heroGuidance`**: komponera heron så att den ryms i första vyn (~1280×800 /
  `100svh`) — **den får aldrig svämma över.** Detta dödar det vanligaste
  "AI-byggd sida"-felet: en överdimensionerad hero som skärs av under vikningen.
- **`spacingGuidance`**: separera sektioner med verkligt blockutrymme —
  produktionssajter ligger på **80–160 px mellan sektioner** — och håll all copy i en
  centrerad, vadderad kolumn. Detta dödar det näst vanligaste: sektioner som kläms
  ihop till ett block, eller text som nuddar viewportkanten.

**Dessa regler levereras i svaret och ignoreras lätt.** I körningen 2026-09-22
returnerades båda i det första `recommend`-anropet, och `heroGuidance` bröts ändå:
rubriken hamnade ~580 px ned i första vyn och fick rättas i en egen runda.
Läs dem som krav, inte som tips.

---

## 6. Arbetsflöde

```
1. get_filters()                     en gång, för att kunna argumenten
2. recommend(brief)                  briefen = produktens formproblem, inte en stil
   └─ läs evidence som gravitation, pick som majoritetsröst
3. search_screens(...)               1–2 st, bara för att fylla på shortlisten
4. compare([...])                    när 2–4 kandidater finns: vad delar de?
5. get_screen(...)                   den fulla autopsin på de 3–5 du behåller
6. get_design_system(slug)           TOKENS för den du bygger från — inte en bild
7. find_reference_components + get_reference_jsx   för de sektioner som ska byggas
   └─ FÖRST HÄR är du redo att skriva en byggspec
```

Steg 4, 6 och 7 är de som hoppas över. Ett bygge som går direkt från steg 5 till
byggspec har sett *bilder av sajter* men har inga tokens, ingen komponentkälla och
ingen analys av om referenserna ens pekar åt samma håll.

---

## 7. Antimönster — allt detta hände i en och samma körning

1. **Sök på stil i stället för på problem.** Gav sex träffar i ett register husets
   spärrar fäller. Två av tre sökningar gick till spillo.
2. **Hämta autopsier på fel referenser.** Fyra av sju anrop gick till kandidater som
   redan förkastats; noll gick till dem som bar riktningen.
3. **Bygg på miniatyrer.** Riktningen fastställdes ur en 384 px miniatyr och en rad
   `northstar` — referensen öppnades aldrig med `get_screen`.
4. **Hoppa över `compare`.** Ingen kontroll av om referenserna delade ett register
   eller pekade motstridigt.
5. **Hoppa över `get_design_system`.** Noll tokens hämtades. Palett, typskala och
   avståndsskala hittades på.
6. **Hoppa över `get_reference_jsx`.** Noll komponentkällkod lästes.
7. **Överskrid budgeten.** Tre `search_screens` mot taket på två.
8. **Ignorera `heroGuidance`.** Regeln låg i kontexten från första anropet och bröts.
9. **Behandla `recommend`s `pick` som en rekommendation.** Den är en majoritetsröst.

Utfallet av alla nio samtidigt: en sida med **4,3 % bildyta, tre bakgrundsfärger
(varav två samma nästan-svarta) och noll fullbredds-element** — ett typografiskt
dokument, inte en komposition. MCP:n hade gett materialet; agenten frågade aldrig
efter det.

---

## 8. Kort checklista före första anropet

- [ ] Är briefen formulerad som **sidans formproblem**, inte som en stämning?
- [ ] Har `get_filters()` körts så att argumenten är giltiga?
- [ ] Är antalet sökningar ≤ 2?
- [ ] Har `compare` körts på kandidaterna **innan** riktningen låstes?
- [ ] Har `get_design_system` hämtats på den valda referensen — riktiga tokens, inte
      gissade?
- [ ] Har minst en `get_reference_jsx` lästs för de sektioner som ska byggas?
- [ ] Är `heroGuidance` och `spacingGuidance` lästa som **krav**?
- [ ] Ligger `maxTokens`/`images` satt om kontextfönstret är trångt?
- [ ] Är varje hämtad referens **öppnad med `get_screen`**, inte bara sedd som
      miniatyr?
