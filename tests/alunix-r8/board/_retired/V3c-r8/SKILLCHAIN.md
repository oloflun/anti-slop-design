# Skill-kedjan per agent, V3c, hela r9

Sammanställd av lead 2026-09-17 ur `tests/alunix-r8/skillchain.py`s rundrapporter
(`SKILLCHAIN-r3.md` till `-r10.md`) och leadsessionens subagent-transkript.

## Byggaren, per runda

Byggaren kör headless i **en** session (`1d136b3f`) som återupptas varje runda med
`--resume`, så ledgerns tal (`ref-read`, `route`, `vision`) är **kumulativa**: de växer
över rundorna och nollställs aldrig. `Skill`-kolumnen är däremot per runda, läst ur
rundans egen stream-json-logg.

| Runda | Modell | Skill-anrop i rundan | route: emitterade / starka / gap | gate-deny | vision (kum.) |
|---|---|---|---|---|---|
| R3 | Opus | emil-design-eng → copywriting → copy-editing → humanizer-svenska → review-animations → a11y-audit | 96 emitterade, 4 starka, gap 0 | 0 | 85 |
| R4 | Sonnet | review-animations | 115 emitterade, 4 starka, gap 0 | 0 | 117 |
| R5 | Sonnet | design → animate → emil-design-eng → find-animation-opportunities | 159 emitterade, 4 starka, gap 0 | 0 | 140 |
| R6 | Sonnet | design | 212 emitterade, 4 starka, gap 0 | 0 | 157 |
| R7 | Sonnet | design → animate → emil-design-eng → a11y-audit | 241 emitterade, 4 starka, gap 0 | 0 | 173 |
| R8 | Sonnet | design → animate → emil-design-eng → a11y-audit | 268 emitterade, 4 starka, gap 0 | 0 | 190 |
| R9 | Sonnet | design → animate → emil-design-eng → a11y-audit | 326 emitterade, 4 starka, gap 0 | 0 | 201 |
| R10 | Sonnet | design → animate → emil-design-eng | 332 emitterade, 4 starka, gap 0 | 0 | 206 |
| R12 | Sonnet | design | 347 emitterade, 4 starka, gap 0 | 1 | 218 |

**Gapet är 0 i varje runda.** Fyra starka hantverksroutes (kod-matchade) emitterades
genomgående och var laddade i samma session. Noll `gate-deny`, noll trap.

## Subagenter (leadens session, delad ledger F-014)

En `Agent`-subagent ärver leadens `CLAUDE_CODE_SESSION_ID`, så ledgern kan inte skilja
dem åt. `Skill`-kolumnen kommer ur varje subagents eget transkript; ledgerrader
attribueras inte per subagent här eftersom flera kördes parallellt.

| Agent | Typ / modell | Skill-anrop | verktygsanrop | fönster |
|---|---|---|---|---|
| Copy-gaten V3c, fem pass | `general-purpose` / opus `aeb86e` | copywriting → copy-editing → humanizer-svenska | 86 | 2026-09-17T20:13 – 2026-09-17T20:31 |
| Fable-arkitekt helhetsloop runda 5 | `general-purpose` / fable `3204c2` | design | 2 | 2026-09-17T17:04 – 2026-09-17T17:04 |
| Design process-act plan for V3c | `Plan` / sonnet `0a3551` | (inga) | 31 | 2026-09-15T14:54 – 2026-09-15T15:02 |
| Fable-arkitekt helhetsloop runda 3 | `general-purpose` / fable `859aba` | design | 235 | 2026-09-17T07:27 – 2026-09-17T11:51 |
| design-perf-reviewer R5 V3c | `design-perf-reviewer` / None `989090` | (inga) | 66 | 2026-09-15T21:39 – 2026-09-15T22:27 |
| design-a11y-reviewer R5 V3c | `design-a11y-reviewer` / None `f2774b` | (inga) | 66 | 2026-09-15T21:39 – 2026-09-15T22:06 |
| Fable-arkitekt helhetsloop runda 4 | `general-purpose` / fable `81406c` | design | 209 | 2026-09-17T13:31 – 2026-09-17T16:30 |
| design-critic R5 V3c | `design-critic` / None `1a5fc1` | (inga) | 36 | 2026-09-15T21:39 – 2026-09-15T21:47 |
| design-heuristics R5 V3c | `design-heuristics` / None `2fc877` | (inga) | 36 | 2026-09-15T21:39 – 2026-09-15T21:50 |
| Fable-arkitekt helhetsloop runda 2 | `general-purpose` / fable `6fe6eb` | design | 259 | 2026-09-17T02:12 – 2026-09-17T06:32 |
| Look up agent teams docs | `claude-code-guide` / None `0e9929` | (inga) | 5 | 2026-09-15T15:35 – 2026-09-15T15:36 |
| Explore skill-chain ledger mechanics | `Explore` / sonnet `db8b7a` | (inga) | 30 | 2026-09-15T14:48 – 2026-09-15T14:51 |
| Fable-arkitekt fas A + plan 010 | `general-purpose` / fable `cf348e` | design → design-catalog → improve-animations | 358 | 2026-09-15T16:42 – 2026-09-16T20:40 |
| Opus-arkitekt helhetsloop runda 5 | `general-purpose` / opus `33dfc9` | design | 192 | 2026-09-17T18:30 – 2026-09-17T20:28 |
| codex-review Astra R5 V3c | `codex-review` / None `2d2bd1` | (inga) | 43 | 2026-09-15T21:40 – 2026-09-15T22:03 |
| Fable-arkitekt helhetsloop runda 1 | `general-purpose` / fable `11d1bc` | design | 222 | 2026-09-16T21:45 – 2026-09-17T01:22 |

## Leadens egen session

Kedjans Stop-hook rapporterade genomgående **`UNLOADED STRONG ROUTES = 1`** för
leadsessionen: `review-animations` routade på riktig kod (mina pixelskript och
rörelsemätningar) men laddades aldrig som skill hos mig. Det är korrekt mätt och
redovisas som leadens egen lucka: rörelsegranskningen kördes i stället av byggaren
(R4, `Skill(review-animations)`) och av perf-granskaren, inte av mig.

## Vad mätningen visar

1. **Headless byggare får en mätbar kedja.** Varje runda laddade `Skill(design)` och
   de skills rundprompten namngav; `animate`, `emil-design-eng`, `a11y-audit` och
   `find-animation-opportunities` syns i transkriptet, inte bara i ledgern.
2. **Subagenter syns bara i sina transkript.** Arkitekten laddade `design` i varje
   runda; granskarna laddade sina egna procedurer. Ledgern ensam hade visat dem som
   leadens rader.
3. **Route-gapet är noll hos byggaren och ett hos lead.** Skillnaden är att byggaren
   får en rundprompt som namnger skills, medan lead orkestrerar och mäter.
