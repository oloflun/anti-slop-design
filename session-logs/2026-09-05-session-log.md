# Session Log — 2026-09-05

## Session Summary

Körde hela anti-slop-design v3-kedjan på ett riktigt kundbygge (Alunix, Antons egen byrå)
över fem rundor — r3 (slå ihop två valda koncept till en sida), r4 (tre strukturella
remixer), r5 (tre varianter av vinnaren, sedan en polerrunda) — varje runda byggd av
Sonnet-subagenter och verifierad på pixlar av mig, inte genom att lita på agenternas
rapporter. Utöver det: en riktig bugg rättad i produktionsdemot `sites/horai.html`,
bake-off-boarden (`board.py`) omskriven efter att Anton tyckte den var för trång, och
den valda V3-byggen fryst som referens innan ett sista proportionstest på den polerade
V3b.

## What Changed

### Files Created
- `tests/alunix-concepts-r3/` — brief.md, targets.md, verdict.md, compare.py,
  `build/index.html` (R5+R6 kombinerade enligt Antons mobilfoto-mosaik),
  `build/tidvatten-hero.html` (Tidvattens fold med byråns rubrik), `build/NOTES.md`,
  skärmbilder.
- `tests/alunix-concepts-r4/` — brief.md, contract.md, board.json, shootgrid.py,
  `cells/M1-chain/` (kontinuerlig grund), `cells/M2-chain/` (kapitel med pinnad scen),
  `cells/M3-chain/` (galleri med rail), verdict.md, final-remixes.png.
- `tests/alunix-concepts-r5/` — brief.md, contract.md, board.json, shootgrid.py,
  `cells/V1-chain/` (dokumentärt band), `cells/V2-chain/` (cinematisk tvätt),
  `cells/V3-chain/` (plåt i grunden, den valda riktningen), `cells/V3b-chain/` (V3
  polerad efter Antons två rättningar + min kritikerrunda), `reference/V3-baseline/`
  (fryst, orörd kopia av V3 för framtida jämförelse), verdict.md, compare-v3-v3b.png,
  horai-check.png, final-variants.png.

### Files Modified
- `sites/horai.html` — den delade Hōrai-demosajten, inbäddad live i Alunix-koncepten.
  Navloggan kolliderade med jätterubriken vid ramens bredd; döljs nu medan heron syns
  och kommer tillbaka exakt när den mörka scrollade bannern dyker upp (en
  IntersectionObserver, inte två separata trösklar som förut). Öppettidsstycket är nu
  helt vitt (var 85 % opacitet, oläsligt på sina ställen). Hittade och rättade en riktig
  bugg under verifieringen: den scrollade bannerns mörka bakgrund renderades aldrig
  eftersom Tailwinds play-CDN inte genererar utility-klasser som läggs till via
  `classList` vid körning — en statisk CSS-regel är den riktiga fixen.
- `~/.agents/skills/design/scripts/board.py` (den levande skillen; speglas till
  `skills/design/scripts/board.py` i detta repo) — mallen omskriven. Antons klagomål:
  tvåspaltsläget tog för mycket vertikal plats och tvingade en låst halv-halv-delning
  även när bara en riktning behövde granskas. Ny layout: en 32 px topplist med
  riktningsflikar, en cell i full bredd/höjd som standard, jämförelseläge bara på
  begäran (knapp eller tangent `p`), betyg/kommentar/remix flyttat till en utfällbar
  panel (tangent `f`) i stället för ett permanent fält längst ner. Lade även till
  `--fallback-root`, eftersom boardens egen HTTP-server bara serverade sin
  sessionsmapp och varje cell som pekar på `/sites/...` eller en annan repo-absolut
  sökväg gav 404 — celler löser nu de sökvägarna mot repo-roten.
- `.claude/launch.json` — lade till `alunix-board-r4` (port 4622) och
  `alunix-board-r5` (port 4623).
- `plans/2026-09-03-design-rework-v3.md` — steg 21–24 loggade (r3 till V3b), "In
  Progress" uppdaterad till Antons jämförelse V3 mot V3b.
- `GOALS.md` — ny changelog-rad: punkten under "Next Steps" ("en skarp designsession
  på ett riktigt kundprojekt, route gap = 0") hände den här sessionen, men route gap
  nådde **inte** noll — `emil-design-eng`, `imagegen-frontend-web` och `impeccable
  layout` pekades ut av routern varje session utan att någonsin laddas, på ett bygge
  som aldrig behövde något av de tre. Flaggat som en egen undersökning (äkta lucka
  mot falska positiva som intent-korpuset inte täcker).
- `anti-slop-design.md` (projekthubben) — nytt avsnitt som sammanfattar
  Alunix-bygget och dess route-gap-fynd; `updated:` satt till 2026-09-05.

### Files Moved/Deleted
Inget.

## Decisions Made

- **Slå ihop två finalistkoncept till en sida, inte välj en vinnare.** Antons
  mobilfoto visade R5 och R6 staplade som en mosaik; i stället för att tolka det som
  återkoppling att välja mellan dem byggde r3 exakt den kombinationen som en riktig
  sida. Skäl: mosaiken var i sig en instruktion, inte ett exempel.
- **Boardens gränssnitt skrevs om helt, inte lappades.** Antons klagomål ("för
  stökigt, kan inte låsas till halvskärm eftersom innehållet ser olika ut") pekade ut
  ett strukturellt problem med den ständiga tvåspaltslayouten, inte ett stilproblem —
  en omskrivning av mallen var billigare än att försöka bevara den gamla DOM-formen.
- **Frys V3 som orörd referens innan fler ändringar på dess efterföljare V3b.** När
  Anton bad om att jämföra "den polerade versionen" mot "originalet" skulle en
  fortfarande redigerbar `cells/V3-chain/` göra den jämförelsen opålitlig. Kopierad
  ordagrant till `reference/V3-baseline/` med en README som säger att den aldrig får
  redigeras.
- **Testa att återställa V3b:s hero-platta till `aspect-ratio:16/9`, acceptera
  konsekvensen.** Polerrundan hade bytt plattan från ett bildförhållande
  (visitkortsproportioner, som V3) till en fast höjdklamp så att hela heron fick plats
  i en skärm. Anton bad om att testa originalets proportioner; gjort, och det ärliga
  priset (heron ryms inte längre i en enda 1440×900-skärm, precis som V3 ursprungligen
  inte gjorde) är noterat i verdict.md i stället för dolt.
- **Synka inte `board.py`-ändringen till `super-intelligence`.** `.carl/upstream.json`
  finns och skulle normalt utlösa en automatisk robocopy av `~/.agents/skills/` in i
  super-intelligence-paketet. Hoppat över medvetet: avknoppningen 2026-09-04
  (super-intelligence CHANGELOG 0.10.0) flyttade hela `design`-skillen UT ur
  super-intelligence och in i sitt eget `anti-slop-design`-plugin, specifikt för att
  den skulle sluta distribueras via det paketet. Att synka tillbaka skulle återinföra
  det som just togs bort. Rätt spegelmål — det här repots egen
  `skills/design/scripts/board.py` via `scripts/sync-from-live.py` — var redan
  uppdaterat (commit `7503466`). Noterat till Anton: `super-intelligence/skills/`
  listar fortfarande en `design/`-mapp trots att 0.10.0-changelogen påstår att den togs
  bort — inte rört den här sessionen, flaggat som en öppen fråga nedan.

## Context & Discussion

- Varje runda följde samma disciplin: en Sonnet-subagent bygger och rapporterar att
  det är klart, sedan renderar jag sidan själv och läser skärmbilderna som pixlar, och
  godkänner bara rundan efter att ha sett de rapporterade fixarna faktiskt synas. Flera
  rundor (r3, r4, r5, V3b) behövde en andra eller tredje fixomgång eftersom en agents
  egen verifiering påstod att något var fixat när det mätbart inte var det (t.ex. en
  CSS-specificitetsbugg som gjorde Hyperborea-plattans "bleed"-signaturdrag helt
  osynligt medan NOTES.md kallade det verifierat). Det här mönstret — lita på
  renderingen, inte rapporten — höll som rätt standard genom hela sessionen.
- Antons två avbrott mitt i sessionen (mitt i ett `/model`-kommando, och
  boardklagomålet) hanterades båda genom att pausa det pågående byggspåret, rätta
  avbrottets orsak direkt, och sedan återuppta — inget arbete tappades eller
  ignorerades tyst.
- Hook-ledgern (`.impeccable/design-session.jsonl`) användes som facit för om
  copy-kedjan faktiskt fyrade, inte agenternas egna rapporter — det fångade en riktig
  lucka i en tidig r3-runda där en agent påstod sig ha kört `copywriting` och
  `humanizer-svenska` men ledgern visade ingetdera.

## Open Threads

- **Antons jämförelse V3 mot V3b är nästa steg.** Boarden ligger på
  `http://127.0.0.1:4623/board.html` — riktning 1 är den frysta V3, riktning 2 är V3b
  med 16:9-plattetestet applicerat. Vilken han än föredrar, eller en ny anmärkning,
  tar tråden vidare.
- **Route-gap-undersökningen.** `emil-design-eng`, `imagegen-frontend-web` och
  `impeccable layout` pekades ut som olästa starka routes i praktiskt taget varje
  stop-hook-rapport den här sessionen, på byggen som inte rimligen behövde något av de
  tre. Värt en kort session för att avgöra om routern är överkänslig på just dessa tre.
- **`super-intelligence/skills/design/` finns fortfarande** trots att 0.10.0-changelogen
  påstår att designskillen flyttades ut helt — inte undersökt eller rört den här
  sessionen; flagga till Anton innan man antar att antingen changelogen eller
  mapplistningen är fel.
- Oförändrat sedan tidigare: Unsplash-API-nyckeln väntar fortfarande (Antons egen
  ansökan) — Alunix fotopoolen använde fyra tidigare hämtade bilder i stället för en ny
  sökning; push av `super-intelligence` (grenen `design-system-v2`) och uppdatering av
  plugin-cachen väntar fortfarande på Antons go-ahead; merge/push av
  `anti-slop-design`s gren `design-rework-v3`, likaså; loggning av v3-besluten i CARL
  DESIGN-domänen, inte gjort än.
- Liten kosmetisk anmärkning jag flaggade till Anton men han svarade inte på: kickern
  "FILOSOFI" sitter tätare mot sin rubrik i V3b:s prisruta än den gjorde i V3, en
  bieffekt av att enhetliggöra paddingskalan över alla paneler — inte rättad, eftersom
  han gick direkt vidare till platteproportionstestet i stället.

## Cross-Project Handoffs

Inga den här sessionen. Alunix-koncepten ligger helt inom `anti-slop-design`s
`tests/`-mapp som designutforskning; inget skrevs till ett riktigt Alunix-projektrepo,
och Anton har inte bett om det än.

## Current State After This Session

Tre byggrundor djupt in i ett riktigt kundprojekt, med två levande kandidater på
r5-boarden (V3, fryst, mot V3b med ett proportionstest applicerat) som väntar på
Antons omdöme. Designsystemet självt bevisade att dess mekanik (reference lock,
känslokurva, fingerprint-gate, arm/disarm-hookkedjan) håller under upprepad verklig
iteration, men en fråga är värd en egen session: routern pekar ut samma tre skills som
luckor i varje rapport oavsett om bygget har någon användning för dem. `board.py`s
omskrivning är live och speglad; inget har pushats till någon remote.

<!-- session-state
date: 2026-09-05
type: design-build-client-iteration
files_created:
  - tests/alunix-concepts-r3/
  - tests/alunix-concepts-r4/
  - tests/alunix-concepts-r5/
files_modified:
  - sites/horai.html
  - skills/design/scripts/board.py
  - .claude/launch.json
  - plans/2026-09-03-design-rework-v3.md
  - GOALS.md
  - anti-slop-design.md
decisions_made: 5
open_threads: 6
handoffs_pending: []
priority_changes: false
status_updated: true
goals_updated: yes
next_session_focus: "Antons V3-vs-V3b-omdöme på r5-boarden (port 4623); om tid finns, undersök route-gap-mönstret för emil-design-eng/imagegen-frontend-web/impeccable-layout."
session-state -->
