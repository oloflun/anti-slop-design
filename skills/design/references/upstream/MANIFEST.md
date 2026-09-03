# Upstream vendor manifest

Reference material vendored byte-identically from upstream repos into this skill.
File contents are never modified after copying. See `INDEX.md` for a per-file listing.

| vendor | repo URL | commit SHA | license | paths copied | date |
|---|---|---|---|---|---|
| interfaces | https://github.com/jakubkrehel/skills | `267330e1adfc66a718fb65fa6918c1f06d0a689e` | MIT (Jakub Krehel) | `skills/better-accessibility/` (whole dir minus `agents/`), `skills/better-ui/`, `skills/better-typography/`, `skills/better-colors/`, `skills/better-layout/`, `skills/better-writing/`, `skills/better-interface/`, `skills/interface-review/`, `skills/variant/`, `skills/break/`, `LICENSE` | 2026-09-03 |
| designpowers | https://github.com/Owl-Listener/designpowers | `cb00757da9d554591fa78d27aa1854d60a05c4f7` | MIT (MC Dean) | `agents/accessibility-reviewer.md`, `agents/design-critic.md`, `agents/heuristic-evaluator.md`, `skills/accessible-content/SKILL.md`, `skills/cognitive-accessibility/SKILL.md`, `skills/adaptive-interfaces/SKILL.md`, `skills/inclusive-personas/SKILL.md`, `skills/verification-before-shipping/SKILL.md`, `skills/design-review/SKILL.md`, `skills/design-debt-tracker/SKILL.md`, `skills/design-taste/SKILL.md`, `skills/using-designpowers/SKILL.md`, `skills/motion-choreography/SKILL.md`, `skills/inspiration-scouting/SKILL.md`, `LICENSE` | 2026-09-03 |
| inclusive | https://github.com/Owl-Listener/inclusive-design-skills | `6e0740f04b2130af60bc57abe3401b91e460e70d` | MIT (MC Dean) | every `*/skills/*/SKILL.md` under `accessibility-decisions/`, `accessible-content/`, `adaptive-interfaces/`, `cognitive-accessibility/`, `inclusive-interaction/`, `inclusive-personas/` (58 files), `README.md`, `LICENSE` | 2026-09-03 |
| designer-skills | https://github.com/Owl-Listener/designer-skills | `20e34c4a587e5eb09fcdf8351fa97b3ad761b31e` | MIT (MC Dean) | `visual-critique/` (whole dir), `design-systems/skills/accessibility-audit/`, `interaction-design/skills/form-design/`, `interaction-design/skills/error-handling-ux/`, `interaction-design/skills/loading-states/`, `interaction-design/skills/onboarding-design/`, `ui-design/skills/dark-mode-design/`, `INDEX.md`, `LICENSE` | 2026-09-03 |
| refero | https://github.com/referodesign/refero_skill | `1d324d5be0492352e2c8702f70a4f9c386c2345f` | MIT (Refero) | `skills/refero-design/` (SKILL.md + `agents/` + `references/`), `LICENSE` | 2026-09-03 |
| scroll-craft | https://github.com/nateherkai/scroll-craft | `677619e74553c006203d9174fe4025f8584a3907` | MIT (Nate Herk) | `plugins/nateherk-design/skills/scroll-craft/` (whole dir), `EXAMPLES.md`, `LICENSE` | 2026-09-03 |
| anthropic | local file (no clone) — `C:/Users/Anton L/.claude/plugins/cache/claude-plugins-official/frontend-design/0120fb83da5d/skills/frontend-design/` | n/a (plugin cache, not a git checkout) | Apache License 2.0 | `SKILL.md`, `LICENSE.txt` | 2026-09-03 |
| slopmonster | https://github.com/ItsssssJack/SlopMonster | `153fab34071d78227b2bd3ec0f26d268c8513ad5` | MIT (Jack Roberts) | whole repo (minus `.git`): `SKILL.md`, `README.md`, `LICENSE`, `.gitignore`, `.github/`, `docs/`, `examples/`, `prompts/`, `references/`, `tools/` | 2026-09-03 |

Notes:
- `refero_skill`'s repo root LICENSE was used since `skills/refero-design/` itself has no LICENSE file.
- `interfaces`' `skills/better-accessibility/` copy excludes its `agents/` subdirectory per instruction; all other `better-*`/`interface-review`/`variant`/`break` dirs were copied whole, including their own `agents/openai.yaml`.
- `anthropic`'s source is a local plugin cache directory, not a git clone, so no commit SHA applies; the plugin cache path itself (containing the short hash `0120fb83da5d`) is the provenance record.
