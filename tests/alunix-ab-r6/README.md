# Alunix r6 — isolerat A/B-test, Claude-native design mot vår kedja

Plan: `~/.claude/plans/jag-vill-att-du-shimmering-sketch.md` (godkänd 2026-09-05).

## Frysta filer

| Fil | sha256 |
|---|---|
| `PROMPT.md` | `7acb190c6b537e1764caa0de4349c415528036bafe63c316527812355f0ccd76` |
| `concepts.md` | `9dc97e1390e05ba7aedd48c23551571a27bb2fb425597040002e43e587680557` |

`run.py` kontrollerar hashen av `PROMPT.md` före varje `build` och skriver den i `logs/*.meta.json`.
Prompten är identisk för båda armarna; bara `{{KONCEPT}}`, `{{UT_MAPP}}`, `{{PORT}}` fylls i per cell.

## Armar

| Arm | Vad agenten har | Hur det åstadkoms (per process) |
|---|---|---|
| **A** Claude-native | Anthropics officiella `frontend-design` (plugin-cachen `claude-plugins-official/frontend-design/9a881c919fa4`) som system-prompt. Inga skills, inga hookar, inga plugins. | `--setting-sources project`, `--disable-slash-commands`, `--append-system-prompt <SKILL.md-kroppen>`, env `CLAUDE_HOOKS_DISABLED=1` |
| **B** vår kedja | Skillen `design` (live, `~/.agents/skills/design`) + repots aktuella åtta hookar + kritikeragenterna. | `--plugin-dir <repo>`, `--settings {"enabledPlugins":{"super-intelligence@super-intelligence":false}}` (så att den gamla cachekopian inte kör dubbelt) |

Gemensamt: `claude -p --model claude-fable-5-1 --effort high --output-format stream-json --verbose
--include-hook-events --dangerously-skip-permissions --session-id <uuid> --no-chrome`, cwd = repo-roten,
`UNSPLASH_*` ur `~/.secrets/.env` i miljön. Portar K1 3101, K2 3102, K3 3103.

## Två avvikelser från planen, upptäckta av proven

- **Binären.** npm-CLI:n på PATH (2.1.241) avvisar `claude-fable-5-1` (kräver ≥ 2.1.251). `run.py`
  läser `ALUNIX_CLAUDE_BIN`; alla körningar gjordes med skrivbordsappens
  `%APPDATA%\Claude\claude-code\2.1.260\claude.exe`. npm-installationen rördes inte.
- **Plugin-skalet.** Repots `.claude-plugin/plugin.json` har `"defaultEnabled": false`, vilket gör att
  `--plugin-dir <repo>` laddar ingenting (prov B, första försöket: pluginlistan saknade
  `anti-slop-design`, inga kedjehookar). `run.py` bygger `tests/alunix-ab-r6/plugin-b/` (manifestet
  utan flaggan + junctions till repots `hooks/` och `agents/`, gitignorerat) och pekar arm B dit.
  Prov B2 (`probes/B2.jsonl`) visar därefter `Skill(design)` som första anrop, route-hookar efter
  varje Write/Edit, stop-hooken som blockerar utan läst bild, och 13 ledgerrader.

## Avbrott och avvikelser under körningen

- **Användningsgränsen** slog till tre gånger (A-K2 efter 71 varv, B-K1 efter 23 varv, och de fem
  kritikeragenterna direkt). `run.py build <arm> <K> --resume` fortsätter cellen i samma session
  med samma flaggor (loggen appenderas, föregående meta sparas som `.meta.N.json`).
- **Gaten uteblev i arm B** (`NEGATIVE_GUARD`, se verdict § 2). Fixad efter arm B; B-K1 kördes om,
  det första bygget ligger kvar som `runs/B/K1-nogate/` med egen logg och review.
- **Kritikertrion kördes inte.** Fem `design-critic`-agenter startades och dog på 429 utan att
  leverera; de togs inte om eftersom de konkurrerar om samma kvot som byggena. Granskningen är
  Claudes egen pixelläsning (`review.py`, `scroll_verify.py`, `a11y_scan.py`) plus agenternas
  egna anteckningar.
- **Binären och plugin-skalet**, se ovan.

## Ordning

1. Unsplash verifierat (2026-09-05: HTTP 200, gräns 50/h = demo-läge). Max 12 anrop per cell.
2. `run.py probe A` → `probes/A.jsonl`: inga skills, inga hook-händelser, ledgern orörd.
3. `run.py build A` → `runs/A/K*/`, `logs/A-K*.jsonl`; `git status` ren utanför; `monitor.py A`.
4. `run.py probe B` → gate + `Skill(design)` + hook-sökvägar under `anti-slop-design/hooks/`.
5. `run.py build B` → `runs/B/K*/`; `monitor.py B`; `monitor.py summary`.
6. `run.py board` → `board/` (blind: motor 1/2 slumpad per koncept i `board/mapping.json`),
   `python ~/.agents/skills/design/scripts/board.py tests/alunix-ab-r6/board --port 4624 --fallback-root .`
   (launch.json: `alunix-board-r6`). Tangenter: siffra = koncept, `p` = par, `x` = helskärm, `f` = betyg.
7. `verdict.md` (Claude, pixlar) → Antons omdöme på boarden → `run.py reveal`.

## Bevakning

`monitor/<arm>-<K>.md` per cell och `monitor/summary.md`: modell/effort, varv, verktyg per namn,
varje Skill-anrop i ordning, hook-händelser och deras källa (repo/cache/ingen), lästa
kedjereferenser under `~/.agents/skills/`, lästa bilder, Unsplash-anrop, skrivningar utanför
egen mapp, subagenter, ledgerrader per session.
