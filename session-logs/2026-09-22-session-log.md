# Session Log — 2026-09-22

## Session Summary

F1–F5 på Alunix V3d byggdes, mättes och verifierades, med en grundorsak som
motsade föregående sessions slutsats: kapitelrubriken skars inte av sin egen
ruta utan av arkets opaka sticky-plan. Ruttgapet — projektets egen mätpunkt 2 —
drevs till noll genom att både `a11y-audit` och `review-animations` faktiskt
laddades och kördes, vilket gav ett HIGH-fynd (kontrast på en etikett över en
vandrande blå yta) som jag först avskrev och sedan fick tillbaka av mätningen.
Sidan gjordes därefter självständig, lades i ett nytt privat GitHub-repo och
publicerades live på Vercel.

## What Changed

### Files Created
- `tests/alunix-r8/runs/V3d/shots/lead-r24f/probe.py` — mäter F3/F4/F5 i riktig hjulscroll: klippande förfader, siffra→etikett-avstånd, spaltbredd och radantal.
- `tests/alunix-r8/runs/V3d/shots/lead-r24f/verify.py` — overflow-svep över fem bredder, dubblett-id, konsol och nätverk.
- `tests/alunix-r8/runs/V3d/shots/lead-r24f/{baseline,after,final}.json` + 45 skärmbilder — bevisen, tagna före och efter varje ändring.
- `tests/alunix-r8/runs/V3d/reviews/a11y-r24f.md` — tillgänglighetsgranskningen, åtta pass, dom `Approve`. CARL-kontrollen mot `tests/a11y/broken.html` redovisad först.
- `.impeccable/a11y-debt.md` — skuldboken, två åtta-fälts-ADR:er (`navigation`-landmärket, och `contrast.py`s hårdkodade URL).
- `~/.claude/projects/.../scratchpad/commit-msg.txt` — commitmeddelandet i UTF-8, för att `git commit -F` inte skulle tappa svenska tecken.

### Files Modified
- `tests/alunix-r8/runs/V3d/index.html` — de fem åtgärderna (se Beslut) plus `vercel.json`-arbetet i ett annat repo. Ändringarna committades av den andra sessionen som `395ec27`.
- `tests/alunix-r8/runs/V3d/NOTES.md` — F1–F5 med mätvärden före/efter, ruttgapets stängning, a11y-fyndet, animeringsgranskningen.
- `GOALS.md` — ändringsloggen fick en rad för publiceringen.
- `memory/MEMORY.md` — två nya poster (Vercel-fällan, git-fällorna), tre konsoliderade, två avlastade till warm.
- `memory/USER.md` — en ny preferens (självständighet utan ändring; repo heter som katalogen).
- `memory/MEMORY-FULL.md` — avlastningssektion för 2026-09-22.

### Files Moved/Deleted
- Inget raderat. Alunix-sidan kopierades (inte flyttades) till `C:\Users\Anton L\alunix`, och `index.html` där är byte-identisk med cellen i `anti-slop-design` — bevisat med `cmp`.

## Decisions Made

- **F3:s grundorsak: `.process-stick`, inte rubrikens ruta.** Föregående session misstänkte `background-clip`; `titelklipp.py` mätte `lost_px 0`, alltså hela glyfer. Den verkliga orsaken är att stämpelrutan hänger under landningslinjen och stack ut 133px nedanför kapitlets box — och den ytan ägs av arkets sticky-plan med `z-index:2` och opak bakgrund. Kapitlet får nu sin höjd ur tal JS redan skriver (`--dn + --stamp-h`), inte ett nytt hårdkodat värde. Valdes för att ingen ny variabel behövdes och för att `max()` lämnar mobilen orörd (0px tillväxt, mätt).
- **F5 kostar arket 2,2 % vw, och det skrivs ner.** Spalten och arket delar railytan. Textspalten 409,9 → 475,8px (+16 %), arket 68,8 % → 66,6 % vid 1920 och 67,8 % → 64,4 % vid 1440. 68,8 % står bokfört i handoffen som accepterat; ändringen gjordes på Antons order ("det är spalten som är fel") och är nu bokförd i NOTES.
- **`a11y_scan`s kontrastfynd var äkta, min första mätning var falskt grön.** Jag mätte `.process-kicker` på ett fast scrolläge: 7,38:1. Rätt svar är 3,64:1, för marken vandrar (`.tes-plane` går från accentblått till skiffer). Fixen byter till `--ink`, husets egen token, 5,99:1 i värsta läget. Lärdomen är M3:s: en mätning i ett läge är inte en mätning.
- **Strukturen för en självständig sida: vendera på de befintliga sökvägarna.** Anton sa "utan att ändra något". I stället för att skriva om sex absoluta sökvägar kopierades beroendena in på exakt de stigar sidan redan frågar efter, så `index.html` förblev byte-identisk. Alternativet (relativa sökvägar) hade ändrat filen.
- **Vercel-inställningen ligger i repot, inte i dashboarden.** `update_project` via Vercel-MCP gav 403 forbidden. `vercel.json` + `.vercelignore` gör samma sak och följer med koden.
- **Juli-appen raderas inte.** Anton har inte sagt ja, och radering kräver hans ord. Den ligger kvar, byggs inte, och dess källfiler publiceras inte.

## Context & Discussion

- **Anton om F1:** *"Jag menade framsidan på visitkortet, den med motiv och logga."* Baksidan låg i kontaktsektionen; framsidan är nu ljuspölsfotot med märket i övre vänstra hörnet, lånat som `<use href="#alunix-mark-path"/>` — en kopia hade gett dubbelt id och kolliderat med herons `setFace`-JS.
- **Rubriken i kontaktsektionen hade ingen CSS-regel alls.** Uppmätt `font-family: "Public Sans"`, `font-size: 24px` — webbläsarens egen h2-default. Det är inte en smakfråga: TASTE § 4.6 förbjuder mellannivån.
- **Kontaktkortets bild fick `transform:none`.** Herons ljuspölsvandring är avsiktligt avstängd där — ett visitkort står stilla och är inte en andra levande heron-instans. Det var den enda rörelsenära ändringen F1–F5 gjorde.
- **Kedjan har nu kört hela sin egen procedur.** a11y-audit och review-animations laddades och följdes; deras script kördes mot `tests/a11y/broken.html` först, så deras tystnad mot cellen är ett utfall och inte en frånvaro av mätning.
- **Antons order om publiceringen:** först "kommitta sidändringarna till alunix-site", sedan korrigerat till att repot ska heta *enbart* `alunix`, sedan "gör vad som krävs för att göra v3d självständig i sin nuvarande form utan att ändra något och lägg den som sidan för alunix i repot".
- **Jag gjorde två fel och rättade båda.** (1) Jag pushade `~/alunix` — en Next.js-prototyp från 30 juli — efter att ha sett att det var två olika artefakter, men utan att göra motsägelsen blockerande eller kontrollera commit-datumen. Pushen var ofarlig men svarade inte på beställningen. (2) `git commit --amend` utan pathspec svalde hela indexet och drog in den andra sessionens 18 staged filer. Inget var pushat; jag backade och gjorde om med pathspec.
- **Frame-tiden faller på hela sidan, och det är inte F1–F5.** `motion_probe` på `#process`: staircase 0, max_step 0,46 % — utjämningen är ren. Men p95 är 116,7 ms. Differentialen mot en orörd akt avgör: `section.hero` ger p95 100,1 ms och 495 långsamma bildrutor. Sidans prestandaskuld (sex inbäddade ramar i ett 25 000px-dokument) är kvar och omätt härifrån.

## Open Threads

- **`design-rework-v3` finns bara på den här disken.** Grenen är 29 commits före `origin/main` och finns inte på GitHub — allt septemberarbete, hela V3d och designsystemets omarbetning, är opushat. Kräver Antons uttryckliga beslut; repot är publikt.
- **Juli-appen i `oloflun/alunix` ligger kvar** i `app/`, `components/`, `lib/`. Byggs inte och publiceras inte, men finns. Radering kräver Antons ord (reversibel via git-historiken `8513b93`).
- **F6 och F7 är orörda** — de stora fyrkantiga blocken och den hårda vågräta skarven i blå→ritning-övergången. De låg utanför F1–F5-beställningen.
- **Plan 067 § Verification är fortfarande en obetald skuld.** Den har aldrig körts.
- **`<nav>`-landmärket saknas i sidhuvudet** (3 av 4 minimilandmärken). Två taggar; ligger som daterad skuld i `.impeccable/a11y-debt.md` till 2026-12-20 och kräver Antons ja för att skrivas av.
- **`design/scripts/contrast.py` har hårdkodad URL** (`localhost:3055`, rad 77) och tar inget argument. Kunde inte köras som a11y-audit föreskriver; ersatt av egen pixelmätning. Värd att laga.
- **`BLOCKS.md` är 25 293 tecken mot filens egen `limit: 3000`.** Pre-existerande, inte denna sessions verk. Kräver ett medvetet beslut om avlastning, inte en tyst städning.
- **`MEMORY.md` står på 92 % och `USER.md` på 98 % efter årets avlastning.** Allt som återstår är levande driftvillkor; att tvinga dem under 80 % hade inneburit att avlasta en aktiv begränsning.
- **Ett `IMG` (`demo-hyperborea.webp` i tesakten) sticker 5px utanför vid 768.** Når inte dokumentet (`scrollWidth` 768 = vw), ligger utanför F1–F5.

## Cross-Project Handoffs

Ingen handoff skriven. `oloflun/alunix` är ett nytt repo utan egen hubb; det bör
registreras som projekt (hubb + `GOALS.md`) om det ska bli mer än en publicerad
sida. Ingen `Outgoing/`-post behövs för det.

## Current State After This Session

V3d är byggd, granskad och publicerad: **live på `https://alunix-three.vercel.app`**,
verifierad i renderingen (45 svar, noll 4xx/5xx), och källan ligger i det privata
repot `oloflun/alunix` med sidan självständig i roten. F1–F5 är åtgärdade och
mätta; F6/F7 och plan 067 § Verification är kvar som skuld. Ruttgapet — projektets
egen mätpunkt 2 — är noll för sessionen. Nästa session bör avgöra om
`design-rework-v3` ska pushas (29 commits finns bara lokalt) och därifrån ta F6/F7
och plan 067 § Verification.

<!-- session-state
date: 2026-09-22
type: design-iteration + release
files_created:
  - tests/alunix-r8/runs/V3d/shots/lead-r24f/probe.py
  - tests/alunix-r8/runs/V3d/shots/lead-r24f/verify.py
  - tests/alunix-r8/runs/V3d/reviews/a11y-r24f.md
  - .impeccable/a11y-debt.md
  - session-logs/2026-09-22-session-log.md
files_modified:
  - tests/alunix-r8/runs/V3d/index.html
  - tests/alunix-r8/runs/V3d/NOTES.md
  - GOALS.md
  - memory/MEMORY.md
  - memory/USER.md
  - memory/MEMORY-FULL.md
decisions_made: 6
open_threads: 10
handoffs_pending: []
priority_changes: true
status_updated: true
goals_updated: yes
next_session_focus: "Avgor om design-rework-v3 ska pushas (29 commits finns bara lokalt), och ta F6/F7 samt plan 067 § Verification"
session-state -->
