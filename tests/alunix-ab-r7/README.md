# Alunix r7 — K1 Skymning och K2 Affischen om igen, Sonnet i rundor, kedjan bevisat tänd

Plan: `~/.claude/plans/jag-vill-att-du-shimmering-sketch.md` (godkänd 2026-09-06). Antons dom på
r6: `design-catalogue/FEEDBACK.md` F-001 till F-009. Målbild v2: `concepts.md`.

## Vad som skiljer från r6

| | r6 | r7 |
|---|---|---|
| Modell | Fable high, headless one-shot | Sonnet high, headless, **rundor** via `--resume` + promptfil |
| Armar | A (Claude-native) mot B (kedjan) | bara kedjan |
| Referenser | prompten förbjöd allt utom två poster | golvet: TASTE + FEEDBACK + reference-lock + posternas filer inkl. `extract/*-DESIGN.md` + scroll-referenserna; hooken nekar UI-skrivning innan dess |
| Runda 1 | bygg allt | bara `BRIEF.md` (referensdigest, auktoritet, lock, grammatik, feeling curve, devices, fingerprint, rm-plan) |
| Material | agenten sökte Unsplash, skrev egen server | fotopaket + Higgsfield-sekvens färdiga i `assets/`, `scripts/serve.py` |
| Granskning | efteråt | orkestreraren läser pixlar i **båda** rörelselägena mellan varje runda |
| Board | blind A/B, 4624 | 4625: motor 1 = r6 B-cellen (före), motor 2 = r7 (efter), reduced-motion-varning |

## Filer

- `concepts.md` — målbild v2 med målbildsgrinden ifylld.
- `PROMPT.md` — runda 1 (placeholders `{{KONCEPT}}`, `{{UT_MAPP}}`, `{{PORT}}`).
- `rounds/<K>-r<n>.md` — orkestrerarens prompt per efterföljande runda.
- `run.py` — tunt skal över r6:s `run.py` (`--model`, `--round`, `--prompt-file`); portar K1 3201, K2 3202.
- `monitor.py` — skal över r6:s monitor med `ref-read`-kategorier; `logs/round-N/`.
- `higgsfield/` — start- och slutbild, testrutor, kostnadslogg.
- `runs/B/K1/assets/push/` — Kling-sekvensen (WebP-rutor + all-intra mp4 + `push-last.webp`).
- `review/<cell>/` — orkestrerarens bilder (`grid-motion.png`, `grid-reduced.png`, `sp-*.png`).
- `RAPPORT.md` — kedjebeviset per runda, Higgsfield-loggen, pixeldomarna.

## Kommandon

```
set ALUNIX_CLAUDE_BIN=%APPDATA%\Claude\claude-code\2.1.260\claude.exe
python tests/alunix-ab-r7/run.py probe B --prompt-file tests/alunix-ab-r7/probe-prompt.md
python tests/alunix-ab-r7/run.py build B K1 K2 --round 1
python tests/alunix-ab-r7/run.py build B K1 --round 2 --prompt-file tests/alunix-ab-r7/rounds/K1-r2.md
python tests/alunix-ab-r7/monitor.py B K1 --round 2
python tests/alunix-ab-r6/review.py B K1 --root tests/alunix-ab-r7 --port 3110
python tests/alunix-ab-r7/run.py board
python ~/.agents/skills/design/scripts/board.py tests/alunix-ab-r7/board --port 4625 --fallback-root .
```
