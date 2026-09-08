---
title: Handoff 2026-09-08 — designkedjan v4
type: handoff
project_slug: anti-slop-design
plan: C:\Users\Anton L\.claude\plans\trots-den-senaste-design-system-federated-raven.md
session_log: session-logs/2026-09-08-session-log.md
updated: 2026-09-08
---

# Handoff — designkedjan v4

Till nästa session i det här projektet. Planen ligger i
`~/.claude/plans/trots-den-senaste-design-system-federated-raven.md` och är godkänd. Det
här dokumentet säger vad av den som faktiskt finns, vad som inte gjordes, och exakt vad som
återstår.

## Kort version

Planen har tretton infrastrukturuppgifter (T1 till T13) och ett test (Alunix r8). **Åtta
uppgifter är klara, två delvis, tre orörda, och testet är inte startat.** Ingenting av det
som byggdes har ännu producerat en designad sida, vilket var hela poängen med övningen.

Två saker att veta innan något annat:

1. **Hookarna är inte i drift.** Allt hook-arbete är korrekt i repot och bevisat med
   fixturer, men sessionerna kör inaktuella kopior. Det är T2 och det blockerar mätningen.
2. **Inget agent-team kördes.** Ingen `/goal`, ingen `/loop`, inga celler, ingen board.

## Vad som INTE gjordes, sagt rakt ut

- **Inget agent-team.** Hela §7 och §8 i planen är orörda. Det finns ingen
  `tests/alunix-r8/`, inga byggare, ingen arkitekt-teammate, ingen board på port 4626.
  Prompterna i §8 är skrivna men aldrig använda.
- **Ingen Alunix-sida byggdes.** Varken V3c, K3 eller K4 existerar.
- **Ingen granskarkvartett kördes**, eftersom det inte fanns något bygge att granska.
- **Ingen Codex-review-agent.** Den fanns aldrig i planen. Codex förekommer på exakt två
  ställen: som en utesluten impeccable-referens (den handlar om native-appar, fel plattform)
  och som reservväg för bildgenerering om Higgsfield-krediterna tar slut. Ingen kodgranskning
  via Codex var planerad och ingen kördes.
- **Ingen bild eller video genererades.** Higgsfield-lagret är installerat, mätt och
  kostnadspreflightat, men inga krediter spenderades. Saldot är oförändrat 73,5.
- **Inget är committat.** 89 spårade filer är ändrade.

## Vad som byggdes

### Mätlagret, som är sessionens tyngdpunkt

| Uppgift | Vad som gjordes | Bevis |
|---|---|---|
| T1 | Eventets sessions-id vinner över ärvd miljövariabel | Hittade den verkliga buggen: id:t läckte från förälderprocessen, så en headless byggare läste fel sessions rader |
| T3 | Referensgolvet kräver mekaniskt katalogval med minst två poster, och att varje vald post lästs färdigt | `tests/hooks/test_reference_floor.py`, fem fall |
| T5 | Fallback-namnet var inte laddbart, bildregeln träffade vendorat material, fem skills saknade rutt | `tests/route_corpus.jsonl`, tjugo fall |
| T6a | F-011 rensad ur kedjans egna filer, cirka trettio mandat i tjugotre filer | grep-verifierad |
| T12 | Varje genereringsanrop loggas med modell, jobb-id och kostnad; grinden nekar utan budgetrad och `get_cost` | `tests/hooks/test_generation_gate.py`, fyra fall |

`verify-design-system.py` går igenom med **191 kontroller mot tidigare 80**. Den kraschade
mitt i körningen redan före sessionen, på en rad som anropade namn `design-stop.py` aldrig
exporterat; siffran "80/80" i hubben var alltså inaktuell.

### Skript, alla bevisade i båda riktningarna

Principen är portad från slopmonster och gäller nu i `gates.md`: **en kontroll som bara kan
avfyra är lika värdelös som en som aldrig gör det.** Varje skript prövas mot en trasig
fixtur som måste falla och mot ett känt-gott bygge som måste hålla tyst.

- `scripts/catalogue/select.py` — deterministiskt referensval ur hela katalogen, skriver
  den `catalogue-select`-rad golvet kräver. `--wildcard` tar in en post utanför kategorin.
- `scripts/catalogue/sweep_raw.py` — omvänt index; katalogen visade sig vara helt svept.
- `scripts/catalogue/drift.py` — enum-, sektions- och extract-validering.
- `skills/design/scripts/motion_probe.py` — bildtid och värdekontinuitet.
- `skills/design/scripts/perf_probe.py` — budgeten, fjorton regelklasser.
- `skills/design/scripts/preflight_taste.py` — taste-skillens mekaniska pre-flight.

### F-012 stängd med mätning

Den öppna frågan var "scrolleffekten renderade som den skulle, men det såg hackigt och
billigt gjort ut". Svaret är **två fel, och F-011 orsakade ingendera**:

| | trasig fixtur | fixad fixtur | V3b i verkligheten |
|---|---|---|---|
| bildtid p95 | 16,7 ms | 16,7 ms | 49,9 ms otrottlad |
| trappsteg | 18 | 0 | 9 till 16 |

Bildfrekvensen är identisk i fixturerna. Skillnaden ligger i värdet, inte i klockan. Motorn
dämpar bara video och pekare; `--sc-p` skrivs 1:1 från rå scrollposition. Dessutom är V3b
genuint tung: 4,9 MB, 19 typsnittsfiler, 17 långa tasks under scroll, och en hero-bild på
1,1 MB **hotlänkad från Unsplash** i strid med kedjans egen regel. Allt står som F-013 i
`design-catalogue/FEEDBACK.md`.

Åtgärden är `skills/design/scripts/scroll/sc-smooth.js`, som publicerar en lerpad `--sc-ps`
bredvid motorns råa värde. Motorn redigeras aldrig.

### Higgsfield

Åtta skills installerade, fyra avstängda efter läsning av innehållet, tre referensfiler
inkopierade med F-011-annotering. Två saker som inte gick att göra som uppdraget löd:

- **MCP:n installerar inga skills.** `sync_agents` går åt andra hållet: den laddar upp
  Antons egna skills och en syntetiserad personlighetsfil till Higgsfields marknadsplats.
  Den körs aldrig av kedjan.
- **Skillsen är CLI-baserade med egen OAuth.** Deras kommandorader kan inte köra mot
  MCP-servern. Upplägget blev: MCP:n kör, skillsen levererar procedur. Skälet är mätbart —
  `get_cost` finns bara på MCP-sidan, och ingen av de åtta skillsen nämner kostnadskontroll.

**Modellkatalogen har flyttat sig sedan r7.** `kling3_0` heter nu `kling3_0_turbo` och tar
bara startbild. För ett klipp med låst start och slut gäller `minimax_h3_max`, och priset är
25 credits för tio sekunder mot r7:s 17,5. Det är därför `models_explore` är obligatoriskt
före första anropet i varje körning.

### Katalogen

`drift.py` rapporterar noll avvikelser och `sweep_raw.py` rent. Åtgärdat: åtta poster med
mode-värde utanför schemat, fyra felnamngivna sektioner, sju exempelsajter som saknade
`## Motion` (skrivna ur sajternas egen kod), tre skräpkataloger, sju extraherade
exempelsajter, och tre dokumentationsfel om vilket serve-kommando och vilka
designlang-flaggor som faktiskt fungerar.

## Vad som återstår, exakt

| Uppgift | Läge | Nästa konkreta steg |
|---|---|---|
| **T2 driftsätt hookarna** | omskriven efter mätning, kräver Anton | Registrera `anti-slop-design` som marketplace och aktivera pluginet; ta bort designhookarna ur super-intelligences publicerade commit |
| **T8 fingerprint-registret** | noll av 29 Alunix-rader | Läs varje cell i `tests/alunix-*` och skriv en rad per koncept i radformatet i `feel-and-fingerprint.md` |
| **T6 portlistorna** | den stora biten, ca hundra namngivna portar | Arbeta §2.4.1 till §2.5.8 i planen rad för rad; varje rad har destination angiven |
| **T10 granskarkontraktet** | tre filer saknar dispositionsord, den fjärde finns inte | Lägg till kontraktet i `~/.claude/agents/design-{critic,heuristics,a11y-reviewer}.md` och skapa `design-perf-reviewer.md` |
| **T7 `scaffold_entry.py`** | enda skriptet som saknas | Skriv det enligt planens §4.3 |
| **T4 arming i r8-harnesset** | ej påbörjad | Kräver att `tests/alunix-r8/` finns |
| **T11 kanonisk DESIGN.md-skrivare** | ej påbörjad | Enligt planens §3.2 |
| **§7 och §8, hela r8-testet** | ej påbörjat | Blockerat av T2 och T8 |

**Ordningen spelar roll.** T2 först, annars mäter r8 ingenting: route-gapet, katalogvalet
och genereringsloggen kommer alla från hookar som inte är i drift. T8 därefter, eftersom
fingerprint-gaten annars inte kan hindra att K3 och K4 liknar något Alunix redan byggt.

## Öppna punkter som inte är uppgifter

- **`/review-animations` kan bara du köra.** Den sätter `disable-model-invocation`, så ingen
  agent kan ladda den. Mot shimen:
  `/review-animations skills/design/scripts/scroll/sc-smooth.js`
- **`sites/calyx.html` bryter mot kedjans egna regler.** Tolv synliga tankstreck mot gate
  75:s nolltolerans, och horisontell överflödning vid 320 px (scrollWidth 384). En uppgift
  är föreslagen för tankstrecken; överflödningen är inte adresserad.
- **Sex beslut i planens §11 är antaganden** tills du säger annat, bland dem kredittaket på
  20 för r8 och att `higgsfield`-CLI:n inte installeras.
- **En öppen fråga till dig i planen:** kortets baksida i V3c listar
  `Design · Utveckling · System` i liggarens ordning. Ditt meddelande skrev "utveckling,
  design, system". Var ordningen avsiktlig?

## Terminalfrågan

Du frågade om jag kan starta lead-sessionen härifrån. **Ja.** Testat och bekräftat: en
interaktiv `claude.exe` startade i ett Windows Terminal-fönster och levde, innan jag stängde
testfönstret igen.

```bash
powershell -NoProfile -Command "Start-Process -FilePath 'wt.exe' -ArgumentList 'cmd','/k','cd /d \"C:\Users\Anton L\anti-slop-design\" && set CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 && claude'"
```

Två saker att veta. `cmd /c start "" wt.exe -d "<sökväg med mellanslag>"` fungerar **inte**;
`wt` kör aldrig kommandot och lämnar inget spår. Och sessionen syns inte i sessionslistan
medan den står tom vid prompten, så för att jag ska kunna mata den med lead-prompten måste
den först ha behandlat en tur. Det kostar tokens och startar arbete, så det valet är ditt.
