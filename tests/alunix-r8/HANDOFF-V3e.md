# Handoff — V3e, nytt försök

Skriven 2026-09-22. Läses tillsammans med `INSPO-MCP-INSTRUKTION.md` (som förklarar
varför första försöket blev vad det blev) och `MCP-TRACE.md` (som spårar varje anrop).

**Läs det här dokumentet innan du rör V3e.** Det finns ett bygge som fungerar och som
det är frestande att "förbättra". Det är fel väg. Läs § 4 först.

---

## 1. Uppdraget

Antons beställning: *"generera en helt ny reimagination av v3d i en ny flik, den ska
förmedla samma typ av budskap och showcase men i en annan visuell tappning, gör det
enkelt med samma textinnehåll, ta endast bort de delar som inte längre är relevanta
eller passar in i upplägget."*

Beställningen är alltså **inte** "byt färg och typsnitt på V3d". Den är en
reimagination: samma budskap, samma bevis, en annan **visuell idé**.

---

## 2. Vad som finns på disk

| Sökväg | Vad |
|---|---|
| `tests/alunix-r8/runs/V3d/index.html` | **V3d**, originalet. 256 kB, R24 + F1–F5. Publicerad: `oloflun/alunix`, live `https://alunix-three.vercel.app` |
| `tests/alunix-r8/runs/V3e/index.html` | **V3e**, första försöket. 55 kB. Provarket |
| `tests/alunix-r8/runs/V3e/BYGGSPEC.md` | Specen V3e byggdes mot |
| `tests/alunix-r8/runs/V3e/RAPPORT.md` | Byggarnas rapporter, runda 1–3 |
| `tests/alunix-r8/runs/V3e/{assets,scroll}/` | Ärvda från V3d: tre woff2 (Geist 700, Geist Mono 400, Public Sans 300) + scrollcraft |
| `tests/alunix-r8/board/board.json` | Fem riktningar: V3c, V3d, K3, K4, **V3e** |
| `tests/alunix-r8/board/cells/V3e-r8/` | V3e:s boardcell |

**Sidan kan inte öppnas med `file://`** — den refererar repo-absoluta sökvägar
(`/sites/calyx.html`, `/tests/alunix-concepts-r3/build/assets/...`). Den måste
serveras från repo-roten.

```bash
# fristående
python skills/design/scripts/serve.py --port 3305 --root .
#   http://127.0.0.1:3305/tests/alunix-r8/runs/V3e/index.html

# boarden (en cell i taget, full bredd — husets regel för en dom)
python skills/design/scripts/board.py tests/alunix-r8/board --port 4626 --fallback-root . --single
#   http://127.0.0.1:4626/board.html     tangent 1-5 byter riktning
```

**Kör alltid genom `serve.py`, aldrig `python -m http.server`** — den senare kör
HTTP/1.0 och tappar WebP under Chromium på Windows.

---

## 3. Vad V3e gör bra och som ska bevaras

Detta är inte värdelöst. Det är hantverket utan idén.

- **Copy-pariteten är verifierad, inte påstådd.** V3e:s synliga text skiljer sig från
  V3d:s i exakt två strängar, båda halvor av h1. Noll påhittad text, noll tappad.
  Verktyget finns: `copy_diff.py` (BeautifulSoup, filtrerar `<script>`/`<style>` och
  **kommentarer** — utan kommentarfiltreringen blir diffen värdelös).
- **Inbäddningarna fungerar.** Calyx och Hōrai laddas lat men monteras garanterat vid
  hopp, ankarlänk, Page Down och återställd scrollposition. Mekanismen: monteringen
  ligger i samma `update()`-svep som tänder raderna, inte i en egen
  `IntersectionObserver`. En observatör **tappar element vid hopp** — det var buggen.
- **Den klibbande inbäddningen.** `.prov-embed .frame{position:sticky;top:32px}`.
  Läsaren kan läsa "Utbudet som prislista" med den faktiska prislistan framför sig.
  Låser på 33 px, släpper mot rutans kant. Det är ett bra grepp — men det är
  *interaktion*, inte komposition.
- **Den tonala inversionen.** Priset: en enda mörk platta inne i pappersarket, ljus
  displayrubrik, tre rader som liggare med högerställda tabelldiffer. Sidans bästa
  sektion.
- **Verifieringslagret.** Playwright-skripten som mäter sida, sektioner, inbäddningar
  och horisontell overflow. Skriv egna eller låna ur `MCP-TRACE.md` § 4.

---

## 4. Diagnosen — och varför du inte ska "förbättra" V3e

V3e är ett **typografiskt dokument**, inte en komposition. Anton fällde det:

> *"Du har ju bara tagit texten och alla bilder, till och med visitkortet som var en
> del av själva designen på den förra sidan och bara lagt allt som en enda textbaserad
> sida med bilder på exempelsidorna och lite scroll-effekter, INGET av de slående
> designelement eller invecklade designer och layouter som finns bland referenserna."*

Mätt, på den färdiga sidan:

| Mått | Värde |
|---|---|
| Sidhöjd 1440 | 7 516 px |
| **Bildyta** | **4,3 %** av sidans yta (två foton: 635×454 och 525×328) |
| **Bakgrundsfärger** | **3**, varav två är samma nästan-svarta → i praktiken **två ytor** |
| **Fullbredds-element som är visuella** | **0** (de 37 träffarna på ≥90vw är `html`, `body`, `main`, omslag) |

Orsakerna, i ordning:

1. **Register byttes, komposition behölls.** Papper i stället för grafit, grönt i
   stället för blått, lätt i stället för tungt. Det är att byta kläder på samma
   dokument.
2. **Specen innehöll ingen visuell idé.** `BYGGSPEC.md` handlar till ~90 % om
   copy-paritet, gates, sektionsordning och kolumnmått, och till ~5 % om visuella
   grepp. En spec som föreskriver rutnät, hårlinjer och numrering producerar ett
   rutnät med hårlinjer och numrering.
3. **Referenserna öppnades aldrig.** Riktningen fastställdes ur en 384 px miniatyr av
   `nbstudio-co-uk` och en rad `northstar`. `get_screen` kördes på de två referenser
   som sedan förkastades, och på noll av dem som bar.
4. **Tre rundor, alla korrigerande.** Inbäddningen laddade inte, heron var tom,
   inbäddningen behövde fäste. Ingen runda ställde en designfråga.
5. **Visitkortet.** V3d:s enda hantverksobjekt — ett kort med motiv och logga som
   vänder sig 180° — blev **fyra rader monospace**. Strängarna bevarades, saken
   förstördes. Det är felet i miniatyr.

**Slutsats: gör ett nytt bygge, inte en fjärde runda på V3e.** En fjärde runda hade
fortsatt putsa ett dokument. Behåll copyn, mekaniken och verifieringslagret; kasta
kompositionen.

---

## 5. Vad nästa försök ska göra annorlunda

**Läs `INSPO-MCP-INSTRUKTION.md` först.** Kortversionen:

1. **Formulera briefen som sidans formproblem.** Inte "varm editorial". V3d:s
   formproblem är: *hur visar man två levande, främmande sajter inuti en sida utan att
   ramen konkurrerar ut dem, och hur visar man tre verks skilda identiteter på en sida
   som ändå har en egen?* Det var den frågan som gav de användbara referenserna.
2. **Kör de verktyg som ger byggmaterial, inte bara referenser.** `compare` på
   kandidaterna innan riktningen låses. `get_design_system` på den valda — **riktiga
   tokens, inte gissade**. `get_reference_jsx` för de sektioner som ska byggas. Ingen
   av dessa anropades i första försöket.
3. **Öppna varje referens med `get_screen`.** En miniatyr är inte en referens.
4. **Skriv en spec som bär en visuell idé i första stycket.** Om specen inte kan
   sammanfattas i en mening som beskriver ett *grepp* — inte en palett, ett grepp —
   är den inte färdig. Exempel på vad ett grepp är: `exoape-com`: monumental typ över
   en helskärmsbild, skuren av viewportkanten, med spänning i överlappet.
   `christophrauscher-de`: en hård 50/50-diptyk mellan en varm bildyta och en mörk
   typsyta. `dversostudio-io`: ett jättelikt konturordmärke som arkitektonisk stomme
   bakom figurerna.
5. **Behåll det som är svårt och som redan fungerar:** copy-pariteten, de levande
   inbäddningarna, den klibbande läsningen, den enda tonala inversionen. De är
   lösningar på riktiga problem.
6. **Läs `heroGuidance` och `spacingGuidance` som krav.** De kom i första
   `recommend`-svaret och bröts ändå.
7. **Budget:** max två `search_screens`. Mät med `maxTokens` om kontexten är trång.

---

## 6. Riktningen första försöket valde, och varför den inte räcker

Provarket: en numrerad, linjerad katalog på svalt papper där varje verk står som
sig självt. Formen är hämtad från `nbstudio-co-uk` och `emigre-com`.

**Formen är rimlig. Utförandet är ett dokument.** `emigre-com` är ett rutnät av
*färgade provplattor*; V3e har noll plattor. `nbstudio` visar *objekt* — fotograferade
boguppslag med etiketter; V3e visar *textrader* med ett iframe bredvid. Provarket som
metafor kräver **ting**, och ting är precis vad sidan saknar.

Om du behåller provarks-idén: gör proven till **objekt**. Rutnät, plattformar, färg,
beskärning, överlapp. Inte en tabell.

---

## 7. Referenser första försöket hade i handen

| Slug | Vad den är | Användes |
|---|---|---|
| `nbstudio-co-uk` | Byrå, terracotta + charcoal, filterrad, verk som katalogiserade artefakter med etiketter | Endast miniatyr |
| `emigre-com` | Typprovark: rutnät av färgade provplattor | Endast miniatyr |
| `exoape-com` | Monumental lowercase display över helsidesfoto, skuren av kanten | Autopsi, greppet togs halvt |
| `dversostudio-io` | Jättelikt konturordmärke som stomme bakom 3D-figurer, rutnät över | Autopsi, oanvänd |
| `eng-dipsy-team` | Typen ÄR bilden; enormt negativt rum med komposition | Autopsi, halvt |
| `christophrauscher-de` | 50/50-diptyk, ockra bild mot mörk typsyta, serif mot sans | **Full autopsi, oanvänd** |
| `humahome-com--sell-html` | Helbredds hero-block, högkontrast-serif, asymmetriskt negativt rum | **Full autopsi, oanvänd** |
| `houseofhoney`, `hay-com`, `generalcondition-com`, `synthesis-partners`, `brethrendesignco`, `kentcdodds` | — | Endast northstar |

Öppna dem med `get_screen` och `get_design_system`. De är arkivets egna svar på
frågan; de är inte uttömda.

---

## 8. Ramar och spärrar

- **Designkedjan är avstängd i den här testmiljön.** `anti-slop-design`- och
  `frontend-design`-pluginen är `false`, 42 skills `off` via `skillOverrides` i
  `.claude/settings.local.json`, och `DESIGN_HOOKS_DISABLED=1` är satt.
  `design-gate.py` är **inte inkopplad någonstans** — verifierat mot `hooks.json` och
  alla settings-filer, och empiriskt med en probe-fil som bar lila gradient, Inter,
  8 px-radius och em-dash utan att något nekade. Husets gates gäller alltså **som
  omdöme, inte som spärr**; de måste läsas och följas aktivt.
- **Husets förbjudna register** (läs `skills/design/references/gates.md` 89–99):
  cream/ivory + överdimensionerad serif + kursivt ordbyte + terracotta i kombination ·
  lila/indigo-accent · gradient-mesh · glasmorfism · tre lika feature-kort · 8 px-radius
  på allt · hårlinjegrid som ren dekoration · **em-dash i synlig text, noll tolerans** ·
  beskrivande mikrotexter.
- **Omvänd varning:** att undvika de förbjudna registren är *inte* att välja ett
  register. Första försöket lade sin uppmärksamhet på vad som inte fick göras och
  glömde bestämma vad som skulle göras. Det är därför sidan är tom på grepp.
- **Rörelse spelar alltid upp** (F-011): ingen `prefers-reduced-motion`-gata, inget
  statiskt reservdokument.

---

## 9. Copyn

Källan är `runs/V3d/index.html`. Den är facit — **inte** `COPY-V3d-*.md`, som är
copy-gate-protokoll och är stale på två punkter (R24 ändrade två strängar utan att
filen uppdaterades).

Sektionsordning i V3d, som beställningen vill behålla: hero → tes (fyra meningar) →
process (sju steg) → Exempelcase → Calyx → Hōrai → pris (tre rader) → kontakt →
footer.

Känsliga strängar: `SEO‑optimering` bär **U+2011** (non-breaking hyphen), inte ett
vanligt bindestånd. `Eller mejla oss direkt på kontakt@alunix.se` är R24:s form.

**Hyperborea** förekommer i V3d som **bild i tesen**, inte som case. Ge det inte egna
liggarrader — första försöket hittade på etiketten `Konferens, Lund` och lånade
Calyxs rader till prov 03. Det togs bort.

---

## 10. Öppna frågor till Anton

1. **Är "provarket" rätt metafor att behålla, eller ska nästa försök öppna
   referenserna utan en förvald form?** Första försöket fastställde formen innan
   referenserna var öppnade.
2. **Hur många rundor får ett försök kosta?** Första försöket lade tre rundor på
   defekter och noll på design.
3. **Ska V3e ligga kvar på boarden som femte flik** medan ett nytt försök byggs, eller
   ska den bort? Den är dömd och kan förvirra en framtida bedömning.
