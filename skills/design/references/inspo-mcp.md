# Inspo MCP

`mcp__inspo__*` — `https://inspomcp.dev/api/mcp`, `Nutlope/inspo`, MIT, read-only. An
archive of **2,320 pages across 832 real, shipped sites**: screenshots (desktop +
mobile), palettes, fonts, detected tech, a **fold-for-fold autopsy** per page, a
**`DESIGN.md` per site** (semantic colour roles, type scale, spacing scale, CSS
variables, container width), and **68 reference components** (hero, pricing, nav,
footer, CTA, testimonial, logo-cloud, FAQ, stat, features), each with copyable JSX.

## When

**After the house catalogue, never before it.** `SKILL.md` Step 1b item 5 (catalogue
first) is unchanged. Query Inspo when the catalogue lacks the page's **form** — not
when it lacks a mood or a palette; those are catalogue/lock problems, not Inspo's. It
is the second source, ahead of the user's own URL, 21st.dev and Refero MCP
(`reference-lock.md` § Sources, in order — item 5).

## The workflow and budget

```
get_filters()                          once, cold — every valid enum value
recommend(<form problem>)              the start; never style words
search_screens(<form problem>) ×≤2     phrased as form, budget hard-capped at 2
compare([...])                         triangulation, before the direction locks
get_screen(...) ×3                     the FULL page image, read as an image
get_design_system(primary)             TOKENS — never eyeballed from a picture
find_reference_components + get_reference_jsx   for sections still lacking form
```

- **`recommend`'s brief is the page's form problem, never a style word.** "Live
  client sites as proof, three works' identities on one page with its own identity,
  the business card as a physical object" — not "warm, editorial, paper." A brief
  written as mood returns noise; a brief written as the problem the page has to
  solve returns the layout and the grip in one call.
- **`search_screens` is phrased as form, capped at 2 calls.** *"Client websites shown
  as huge full-bleed screens that dominate the page"* found the reference that
  mattered. The companion query, phrased as an object ("visitkort" / "business
  card"), returned brus — noise — because ranking is **lexical**, not semantic.
  Object and mood queries burn the budget without moving the direction.
- **`compare` triangulates; it never picks a winner.** Run it on 2–4 kept
  candidates *before* the direction locks. Take one move from each reference that
  shares something with the others — never treat `compare` as a filter that
  selects a single "best" reference and discards the rest. A composition that
  rests on one reference alone is the exact failure `compare` exists to catch
  (`sameRegister:false` still means: go find what they share, don't pick one).
- **Open every kept reference with `get_screen` and read the full page image.**
  `get_screen` returns a `full.1440.webp` URL — download it and read it as an
  image, not the thumbnail. The thumbnail shows a 2×2 crop; the grip a page
  actually depends on is often only visible in the full composition (a
  continuous rutverk of cells reads as four squares in a thumbnail and as one
  system in the full page).
- **`get_design_system` on the primary reference is mandatory, not optional, once
  a direction is chosen.** It returns real tokens — hex, radius, weight, tracking,
  a fluid type scale — straight into the spec. Nothing here is guessed or read off
  a screenshot.
- **`find_reference_components` + `get_reference_jsx`** close the loop for any
  section the chosen reference doesn't cover on its own — real, copyable JSX,
  stamped with the macrostructure, theme and state it came from.

## Anti-patterns and limits

- **Ranking is lexical, not embedding-based.** A query has to match the words a
  real page's autopsy uses, not the concept behind them.
- **Object and mood queries return noise.** Query the problem the page's form has
  to solve ("show live client work at full scale"), never a subject ("business
  card") or a vibe ("warm, editorial").
- **The archive has no motion.** Every asset is a static screenshot. Motion
  borrowings come out of the autopsy **text** ("checkerboard pixel-dissolve"),
  never out of the image.
- **`recommend`'s `pick` is a majority vote, not a recommendation.** It names the
  most common macrostructure among the hits and says so itself; the shortlist
  carries the runners-up, and the right answer for this brief is often one of
  those, not the pick.
- **`heroGuidance` and `spacingGuidance` ship with every `recommend` result and are
  requirements, not tips.** Hero composes inside the first view (~1280×800 /
  `100svh`), never spills past the fold. Sections get real block space — production
  sites run 80–160px between sections — and copy stays in a centred, padded column.
  Both get ignored by default; read them as gates.
- **Results are re-read on every later turn.** They don't cost once — they stay in
  context and get re-read each subsequent turn, so an extra search past the budget
  costs more than it finds. Budget: one `recommend`, ≤2 `search_screens`, `get_screen`
  on 3–5 kept references, is a complete study.

## V3e vs V3f: the difference in numbers

V3e and V3f shared the same copy, image bank and models. V3e became a typographic
document — **4.3% image area**, in practice two surfaces — because its `recommend`
brief was a mood, its second search was object-phrased, its references were judged
from thumbnails, and no tokens were fetched. V3f became a composition — **30% image
area**, four flat surfaces plus rastered image cells — because the brief was the
page's form problem, the search was form-phrased, the full-page image was read (not
the thumbnail), `get_design_system` supplied real tokens, and the resulting spec
opened with the grip stated in one sentence before any cell map or constraint.

Same tool, same budget, opposite outcome — the difference was in how each call was
phrased and which artifact got read, not in which calls were made.

Full account, worked example and the nine-antipattern case study this file distills:
`tests/alunix-r8/INSPO-MCP-INSTRUKTION.md` and `tests/alunix-r8/HANDOFF-V3f.md` § 1,
§ 3.1 (anti-slop-design repo).

## The house fork (2026-09-25)

`inspo` in `~/.claude.json` is a local stdio fork, not the hosted endpoint: `~/inspo`, branch
`house`, remote `upstream` = Nutlope/inspo (MIT). It serves upstream's 2,320 pages **plus the 97
house catalogue entries** as `house-<slug>` rows (lexical ranking only; no Together key, no Blob,
no database).

- Rows are generated by `python scripts/inspo_import.py` (anti-slop-design) into
  `~/inspo/packages/db/src/house-screens.json` (gitignored) — rerun after any catalogue change;
  `--check` validates against Inspo's taxonomy, `--selftest` tests the mapping.
- House images resolve to `http://127.0.0.1:4610/design-catalogue/entries/<slug>/…` — start the
  repo's `catalogue` launch config (`python -m http.server 4610` from the repo root) before
  fetching them. Text fields (northstar, autopsy, palette, fonts, DESIGN.md) work without it.
- Upstream updates: `git -C ~/inspo fetch upstream && git -C ~/inspo rebase upstream/main` on
  branch `house` (one commit: the loader in `packages/db/src/seed-source.node.ts`).
- Rollback to hosted: `claude mcp remove inspo -s user && claude mcp add --transport http inspo
  https://inspomcp.dev/api/mcp -s user`.
