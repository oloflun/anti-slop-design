---
type: goals
project_slug: anti-slop-design
updated: 2026-09-03
updated_by: claude
---

# Mål — Anti-Slop Design

## Vad projektet är och för vem

Det här är ett designsystem för Antons AI-assistent, inte en webbplats. När man ber
en AI bygga en sida får man nästan alltid samma sida tillbaka: samma typsnitt, samma
tre kort med ikoner, samma gradient. Repot innehåller regelverket och de
automatiska spärrar som gör att det inte händer — en **skill** (en instruktionsfil
som assistenten läser när den ska göra något visuellt) plus åtta **hookar** (små
skript som Claude Code kör automatiskt före och efter varje filändring och som kan
stoppa en ändring som bryter mot reglerna).

Grundregeln är en enda mening: *varumärket bestämmer riktningen, färdiga skills
bidrar med hantverket, färdiga teman är sista utvägen.* Allt systemet finns för att
förhindra är att en specialistskill målar om kundens varumärke i sin egen palett.

Användaren är Anton själv och varje Claude-session han kör — hookarna ligger inlagda
i `~/.claude/settings.json` och fyrar i alla projekt. Repot är samtidigt publikt på
GitHub (`oloflun/anti-slop-design`) och har en demosajt på Vercel med sju byggda
exempelsidor, så det fungerar också som ett skyltfönster.

## Vad "klart" betyder

**Inte bestämt än.** Det finns ingen skriven definition av när det här projektet är
färdigt, och det ser inte ut som en produkt med ett slutdatum utan som ett system
som underhålls så länge Anton designar med AI. Det som *finns* är tre mätpunkter som
projektet självt har infört, och de går att observera:

1. **`python verify-design-system.py` går igenom.** 80 mekaniska kontroller av att
   installationen, hook-inkopplingen, routingtabellen och kontraktsspärrarna hänger
   ihop. Senaste noteringen i hubbdokumentet: 80/80.
2. **Gapet mellan "utpekad skill" och "laddad skill" är noll.** Varje session skriver
   en rapport. Hookar kan injicera text och stoppa skrivningar, men de kan inte ladda
   en skill — bara modellen kan det. Därför mäts hur ofta systemet pekade ut rätt
   skill och ingenting laddade den. Det talet ska vara noll.
3. **Blindtestet.** Tre färska underagenter fick var sitt uppdrag utan dialog och
   utan iteration, och Anton bedömde att alla tre höll referensnivå på första
   försöket. Det gjordes 2026-08-01 och är det närmaste ett godkännandeprov
   projektet har.

Se öppen fråga 1 — utan ett svar på vad "klart" är blir de här tre bara
hälsokontroller, inte ett mål.

## Delmål i ordning

- [x] 1. Version 1: en router-skill, en granskning av 32 installerade designskills,
      och tre färdiga sajter som bevis (Calyx, Hyperborea, Hōrai).
      *(Bevis: `README.md`, `AUDIT.md`, `sites/`.)*
- [x] 2. Version 2 (2026-07-28): flytta spärrarna från promptgräns till
      redigeringsgräns, eftersom guidningen förr injicerades en gång per prompt och
      hann glömmas bort under en byggtur på sextio verktygsanrop.
      *(Bevis: `.claude/hooks/`, commit `1b0c136`.)*
- [x] 3. Omarbetningen 2026-08-01: "hantverksgolvet" flyttas in i själva skillen i
      stället för att pekas ut i 120 externa filer, ett **register** (editorial
      tryck / filmiskt mörkt / illustrerat mörkt / modernt rent / varmt fotografiskt
      / historiskt konstnärligt) ska namnges *innan* koden skrivs, och Stop-hooken
      börjar faktiskt blockera en avslutad designsession där ingen bild lästs efter
      sista UI-ändringen.
      *(Bevis: `plans/2026-07-31-what-actually-made-the-difference.md`, commits
      `c3f4dcb` … `bc61c44`, sju sajter i `sites/`.)*
- [x] 4. De två nya hookarna når befintliga installationer.
      Hubbdokumentet listar detta som öppet, men **det stämmer inte längre**:
      `install.mjs` rad 351/354 och `upgrade.mjs` rad 78/81 i `super-intelligence`
      skriver in `design-vision-track.py` och `design-session-start.py`, och alla
      åtta hookarna ligger inlagda i `~/.claude/settings.json`. Punkten kan strykas
      ur hubben.
- [x] 5. **Bestäm vilken kopia som är original och synka.** Beslutat 2026-09-03 (2A): det
      som körs är kanoniskt (vaultens `.agents/skills`, `super-intelligence/hooks`), repot
      är spegel via `scripts/sync-from-live.py`; verify-checken "repo == live" bevakar det.
      *(Ursprunglig text:)* `skills/design/SKILL.md`
      i repot är 471 rader, den som faktiskt körs
      (`~/.agents/skills/design/SKILL.md`) är 510, och en diff mellan dem är 983
      rader. Referensmappen skiljer sig också (43 mot 44 filer). Det publika repot
      visar alltså inte längre det system som är i drift.
- [x] 6. `hallmark` har `disable-model-invocation: true` sedan 2026-09-03 (kvar, anropbar med namn). Avgör vad som händer med `hallmark`. Enligt hubben konkurrerar den skillen
      fortfarande med `design` om att fyra automatiskt, trots att dess 105
      referensfiler redan är inflyttade här.
- [x] 7. Lagat 2026-09-03 (`$impeccable init`). Ta bort det trasiga beroendet i `polish`, som fortfarande pekar på
      `/teach-impeccable` — ett namn från version 3 som inte finns.
- [ ] 8. Avgör vad `AUDIT.md` ska vara. Hubben märker den som inaktuell och ersatt
      av `skill-orchestration.md`, men den är samtidigt en av tre länkar högst upp i
      den publika README:n.

## Planerade funktioner

### Beslutat

- **Åtta hookar som spärrar vid varje redigering, inte vid varje prompt.** Detta är
  hela poängen med version 2 och ligger inkopplat och i drift.
- **`design-gate.py` är den enda hårda spärren.** Övriga hookar föreslår; den här
  nekar en skrivning som bryter kontraktet. Det är ett medvetet val, dokumenterat
  som "the load-bearing limitation" i hubben.
- **Tre skills får aldrig sätta visuell riktning:** `minimalist-ui`,
  `industrial-brutalist-ui` och `high-end-visual-design`. Var och en har en hel
  palett hårdkodad — Notions gråskala, `#E61919` som "enda tillåtna accent", tre
  fasta arketyper. Deras färgkoder i ett bygge på nivå 0–2 loggas som
  kontraktsbrott.
- **`DESIGN.md` skrivs bara via `impeccable document` eller `brand-system`.** Fem
  olika skills skriver en fil med det namnet i tre oförenliga format, och en
  prosa-variant fick systemet att utropa "LÅST, ärv systemet" utan att spärra
  någonting alls.
- **Nödstopp:** `DESIGN_HOOKS_DISABLED=1` stänger av hela kedjan.

### Föreslaget — ej beslutat

- **En positiv kvalitetsport — nu införd (2026-09-03):** `verbs/critique.md` betygsätter sju
  dimensioner på pixlar (pass/minor/major) med uppmätta värden och referensmeningen; A/B-test
  03 i `tests/ab/`. Ursprunglig formulering: Diagnosen i
  `plans/2026-07-31-what-actually-made-the-difference.md` säger rakt ut att alla 88
  portar är negativa, alltså formulerade som förbud, och att en platt men helt
  regelriktig sida därför passerar samtliga utan anmärkning. Något som mäter att
  sidan är *bra* saknas. Detta är härlett ur projektets egen analys, inte beslutat.
- **Publicera version 2 och 3 utåt.** Den publika README:n beskriver fortfarande
  version 1 och 2 med tre sajter, medan repot innehåller sju och ett helt annat
  hantverksgolv. Om skyltfönstret ska vara ett skyltfönster behöver det uppdateras
  — men om Anton inte längre bryr sig om den publika sidan är det en icke-fråga.
  Se öppen fråga 2.
- **Rapport som visar om synen faktiskt användes.** `design-vision-track.py` loggar
  numera när en bild verkligen når modellen; det finns ingen sammanställning som
  visar trenden över tid.

## Beroenden till andra projekt

**Vad det här projektet väntar på:**

- Ingenting. Systemet är självständigt och kräver bara att Claude Code är
  installerat.
- De fem uppströmsprojekten (impeccable, taste-skill, design-extract, designpowers,
  stitch-skills) klonas från GitHub. Ändras de kan referenskontrollerna i
  `verify-design-system.py` börja gå fel, men ingenting slutar fungera.

**Vad som väntar på det här projektet:**

- **`super-intelligence` distribuerar det.** Hookfilerna ligger i
  `super-intelligence/hooks/` och `install.mjs`/`upgrade.mjs` kopplar in dem. Ändras
  en hooks filnamn eller signatur här måste installeraren följa med.
- **Varje projekt där Anton designar något.** Hookarna är globala. En regression
  här märks först som att en helt annan sajt får fel färger.
- Två skarpa användningar finns nedskrivna: `alunix-site` (ett scroll-drivet
  uppslag) och `klova-hamnkrog` (en designgranskning, åtta fixar, båda committade).

## Öppna frågor till Anton

1. **Vad är "klart" här?** Är det ett verktyg som bara underhålls så länge du
   designar med AI, eller finns det ett sluttillstånd du siktar på? Utan svar går
   det inte att skriva en milstolpe som inte är påhittad.
2. **Är det publika repot fortfarande ett mål?** Det ligger på GitHub med en
   README skriven för främlingar och en Vercel-demo, men innehållet beskriver ett
   system som är två omarbetningar gammalt. Ska det underhållas som skyltfönster,
   eller är GitHub bara backup nu?
3. ~~Vilken kopia är originalet — repot eller `~/.agents/skills/design/`?~~ **Löst
   2026-09-05:** valvets `.agents/skills/design` är källan, `anti-slop-design/skills/design`
   är spegeln (`scripts/sync-from-live.py`, körs manuellt efter varje live-redigering —
   glömdes inte idag, men är lätt att glömma; värt att göra till en `/conclude`-standardrad).
4. **Ska `hallmark` bort?** Den konkurrerar fortfarande om automatisk aktivering,
   och dess innehåll är redan inflyttat.
5. **Är `impeccable` (skillet, inte referenstexten) laddningsbart i den headless-miljö
   byggarna kör i?** `component-routing.md` pekar flera regler mot `$impeccable <verb>`
   (layout/harden/operate/polish/…), men `impeccable` laddades noll gånger i sex fulla
   r7-rundor per koncept. Om det inte går att ladda där behöver de reglerna peka om mot
   `design` i stället — se `tests/alunix-ab-r7/CHAIN-AUDIT-2026-09-07.md` § 2b.

## Ändringslogg

- 2026-09-06 — claude — r6 underkändes av Anton och blev r7. Fynden: hans webbläsare kör
  reduced motion (Windows-animationer av), så alla sex celler visade sina reservlägen och
  reservlägena var tomma; kedjan läste noll referenser för att SKILL.md gjorde TASTE.md
  villkorad, prompten förbjöd `extract/`, ingen hook nekar i nybyggen, telemetrin ser inte
  vilka filer som lästs och route-gapet är blint för scroll; K3 och K2:s brief var Claudes
  smakfel. Byggt: `design-catalogue/FEEDBACK.md` (Antons domar som regler, F-001–F-009),
  referensgolvet i hookarna (`ref-read`, gate nekar första UI-skrivningen, scroll-route,
  scroll-gap, rm-bild i exit-bar), SKILL.md Step 1b/2b/Motion/Step 5, TASTE § 4.8,
  house-physics, skill-orchestration § 12 (delegerade byggen i rundor, målbildsgrind),
  `scripts/serve.py`, boardens reduced-motion-varning. r7 (`tests/alunix-ab-r7/`): K1 + K2
  om igen med Sonnet i rundor, Higgsfield/Kling-kameraresa för K1 (tak 35 cr), board 4625.
  Utfall 2026-09-07: båda cellerna i slutläge efter sex rundor + kritikertrion, varje runda
  med kedjan bevisat tänd (`tests/alunix-ab-r7/RAPPORT.md`); Antons dom väntar.
- 2026-09-07 — claude — Antons dom på boarden avslöjade att rörelsen fortfarande inte syntes;
  grundorsaken var Windows Animationseffekter fortfarande av, samma villkor som F-001. Anton
  eskalerade till en permanent, global regel: rörelse spelas alltid upp, oavsett webbläsare/
  systeminställning (F-011), ett medvetet, informerat avsteg från tillgänglighet han bekräftade
  efter att avvägningen lades fram. Genomfört genom hela kedjan (`scrollcraft.js/.css`, K1/K2,
  `a11y-audit` globalt) och verifierat i en riktig reduced-motion-webbläsare. En separat, riktig
  bugg hittades samtidigt: `board.py` körde HTTP/1.0 och tappade WebP (samma bugg `serve.py`
  löste för cellerna, aldrig portad till boarden) — fixat. På Antons begäran grävdes sedan hela
  kedjefyrningen igenom på nytt (`CHAIN-AUDIT-2026-09-07.md`): en verklig sessions-scoping-bugg
  i Stop-hooken bevisad (räknar fel session när hook-processen saknar rätt miljövariabel, fix
  föreslagen men inte gjord), två olika orsaker bakom route-gapet särskilda
  (`imagegen-frontend-web` för brett villkor, `"impeccable layout"` fel skillnamn), och
  `Skill(design-catalog)` visade sig aldrig ha kallats — orkestrerarens egen prompt gav
  filvägar direkt i stället för att köra skillets sökning. Nytt öppet fynd (F-012): rörelsen
  spelar nu upp korrekt men "ser hackigt och billigt gjort ut" — orsak oundersökt, uttryckligen
  överlämnad till nästa session.

- 2026-09-05/06 — claude — r6: det isolerade A/B-testet (Claude-native mot kedjan, samma
  frysta prompt, tre nya Alunix-koncept, headless Fable-high-processer, blind board på port 4624).
  Delmål 2 ("route gap = 0") fick sin förklaring: intentklassificerarens negativlista nollade all
  designintention på ett enda ord (`commit`, `skills`) var som helst i briefen, så gaten uteblev för
  hela arm B; fixad i `hooks/design_hook_lib.py` med korpusen 42/42. Djupare: när skillen väl
  laddas läser agenten inga referenser och kör inga procedurskills, så "kedjan på" mätte bara
  SKILL.md-i-kontext plus hookar vid skrivning. Unsplash-API:t är i drift (nyckel, skript, kredit).
  Se `tests/alunix-ab-r6/verdict.md`.

- 2026-09-04/05 — claude — den skarpa designsessionen från "Next Steps" kördes: ett riktigt
  kundprojekt (Alunix, `tests/alunix-concepts-r3/` … `-r5/`) gick igenom hela kedjan flera
  varv (bake-off, Step 5-loopar, kritikeragent, en boardomskrivning). Route gap drev **inte**
  till noll — stop-hooken pekade konsekvent ut `emil-design-eng`, `imagegen-frontend-web` och
  `impeccable layout` som utpekade men olästa genom hela sessionen. Värt att undersöka som
  egen punkt: är det äkta gap eller routrar som pekar på skills som aldrig var relevanta för
  den här sortens bygge (ingen animationsbibliotek-fråga, ingen bildgenerering, inget
  komponentbibliotek)? Se session-loggen för 2026-09-05.

- 2026-09-03 — claude — rework v3: delmål 5–7 klara, positiva porten införd, nya delmål
  9 (pusha super-intelligence + plugin-cache) och 10 (katalogen till Vercel + OAuth) läggs
  under Öppna frågor; se hubben och `tests/ab/`.

- 2026-08-26 — claude — skapad, ur `README.md`, `ROUTER.md`, hubbdokumentet
  `anti-slop-design.md`, `plans/2026-07-31-what-actually-made-the-difference.md`,
  hookfilerna i `.claude/hooks/`, git-historiken, `super-intelligence/install.mjs`
  och `upgrade.mjs` samt en jämförelse mot den installerade skillen i
  `~/.agents/skills/design/`.
