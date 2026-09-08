# The lift — what replaces "just run polish"

`impeccable polish` is a *last* pass and says so: it "preserves the incumbent visual
world" and "does not add animation merely to make polish visible". Pointed at a whole
page that is merely competent, it returns a slightly tidier competent page. Every other
impeccable command ends by handing off to polish; polish is the handoff target, not the
procedure.

The lift is the procedure. Each pass is a named skill invocation, in an order the
upstream references themselves prescribe, with a mechanical gate between passes.

## The sequence

| # | Pass | Invocation | Output |
|---|---|---|---|
| 1 | Read-only review | [`verbs/review.md`](verbs/review.md) — slop audit + `Skill(a11y-audit)` + [`verbs/critique.md`](verbs/critique.md) + `Skill(review-animations)` | One ranked table, ≤ 15 rows, Block or Approve |
| 2 | The quartet, in parallel | `design-critic`, `design-heuristics`, `design-a11y-reviewer`, `design-perf-reviewer` | Four reports on the shared contract below |
| 3 | Where motion belongs | `Skill(find-animation-opportunities)` + `Skill(animation-vocabulary)` | ≤ 5 proposals with exact values **and a Rejected list** |
| 4 | Fix plans | `improve-animations`' PLAN-TEMPLATE per finding | `plans/NNN-slug.md`: Problem / Target / Conventions / Steps / Boundaries / Verification incl. a feel-check |
| 5 | Fix passes, one per round | (a) `impeccable layout` → (b) `impeccable typeset` → (c) `impeccable colorize` *only if* the critique says flat or grey → (d) `Skill(animate)` + `Skill(emil-design-eng)` → (e) `impeccable delight` *only if* the brief carries a delight thesis → (f) the copy gate → (g) `impeccable harden` → (h) `impeccable optimize` against the probe reports → (i) `impeccable polish` **last** | One commit per pass, screenshots after each |
| 6 | Mechanical gate after every pass | `detect.mjs --json`, `preflight_taste.py`, `scroll_verify.py`, `perf_probe.py`, `motion_probe.py`, `contrast_over_media.py` | All green before the next pass |
| 7 | Round again | Back to 1 | Stop when a whole pass finds nothing material **and the critic writes "beats" for each locked reference** |

Cap: six rounds per cell. Then stop and hand Anton a table of what is still open, rather
than iterating quietly forever.

## Triage order inside a round

From `impeccable/reference/polish.md`: **broken → states → flow and hierarchy → visual →
code.** A colour decision taken before a broken state is fixed is a decision taken about
the wrong page. Within "visual", most material first: a fix that changes what the page
*is* outranks one that changes how it is finished.

## The reviewer contract

All four reviewers return the same shape, borrowed from impeccable's finish-reviewer:

1. First line, one disposition word: `recapture` · `rebuild` · `fix` · `ship`.
2. Then exactly five sections:
   - **persistence** — did the previous round's fixes survive?
   - **fidelity** — against the target picture, screen by screen (F-007).
   - **ceiling** — what each locked reference still does better, one line per reference.
   - **material_fixes** — at most 8, most material first, each with a target value or a
     reference image, never "make it nicer".
   - **keep** — what must not be touched.

The critic's ceiling section carries the honest sentence **per locked reference**:
"beats garden-eight on X, loses to mattis-studio on Y". A single lump verdict hides which
reference is actually beating you.

Reconciliation when they disagree: **accessibility > performance > usability > brief >
personas > escalate**. Performance sits above usability because a page that drops frames
cannot be judged on usability at all.

Every finding is verified against the pixels by whoever merges the reports. A reviewer
report is a claim, not a fact.

## When a pass is skipped

`bolder`, `quieter` and `distill` run **only** when pass 1 or 2 says a named section is
flat, loud or overloaded. `colorize` runs only on a flatness finding. `delight` runs only
when the brief declares a delight thesis. Skipping is the default; running one without a
finding behind it is how a page drifts away from its own direction.

## Not part of the lift

- `impeccable live` — needs a dev server and an overlay; it is Anton's own manual
  iteration after delivery, not a chain step.
- `impeccable onboard` / `extract` — Operate surfaces and design-system maintenance.
- `impeccable document` — runs *after* ship, from the built code, never before.
- `prototype` — the bake-off already has `board.py`.
- The gstack quartet (`design-review`, `design-shotgun`, `design-html`,
  `design-consultation`) — a parallel pipeline. Pick one lane per project; what is worth
  borrowing from it is already ported into `verbs/review.md`.

## Stopping

Two conditions, both required: a full pass 1–2 that finds nothing material, and the
critic writing "beats" for every locked reference. "Stands up beside them" is not the
bar. If you cannot say it yet, the page is not finished — and if you have said it six
times without it becoming true, the concept is what needs changing, not the polish.
