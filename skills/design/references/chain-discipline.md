# Chain discipline

**Resident. Not routed.** This file loads with `SKILL.md` and is read by every
builder, every reviewer and every orchestrator in this chain, on every job.
It is the one document that is about *us* rather than about the page.

It exists because of a five-day run (Alunix V3d, 2026-09-15 → 09-20) that spent
**37 build rounds on 10 orders**, cost $24 for the last round alone, and ended
with the owner's verdict:

> *"resten av ändringarna motsvarade inte riktigt heller mina förväntningar även
> om de utfördes på papper."*
> — Anton, 2026-09-20

Nothing in that run failed for lack of craft. Every ordered point was built and
rendered. It failed because **the chain lied to itself five times and believed
each lie** — and every lie became a build round before anyone caught it. The
rules below are those five lies and their fixes, plus the four method changes
that came out of the same run.

**The rule everything else serves:** *a measurement you have not proven against
a known-broken case is not a measurement, it is a guess with a number on it.*

---

## 1 · Measurement

### M1 · Register every custom property before you read it

`getPropertyValue('--tx')` on an **unregistered** custom property returns the
token stream — `clamp(0,calc((0.3214 - 0.2258) / 0.1613),1)` — not a number.
`parseFloat` on that is `NaN`, and `NaN` silently compares as `0` in every filter
and every `if`.

**What it cost:** the `--slit-p` filter was inert through round 18 *and* through
two of Astra's review passes without anyone noticing. It then convinced the lead
that a colour draw had not started when `--tx` was in fact `0.59`, and that
false reading was written up as a finding before it was caught.

**The rule.** Every numeric custom property that any script, probe or reviewer
reads must be declared:

```css
@property --tx     { syntax: '<number>'; inherits: true; initial-value: 0; }
@property --slit-p { syntax: '<number>'; inherits: true; initial-value: 0; }
```

Declare it when the property is created, not when a measurement fails. If you
are reading a property that is not declared, **that is the finding** — declare
it first, then measure.

**The check that proves the check:** run `parseFloat(getComputedStyle(el)
.getPropertyValue('--tx'))` against the *current, undeclared* state first. It
must return `NaN`. A version of this check that returns a number against both a
declared and an undeclared property is measuring nothing.

### M2 · Never judge an act in a preview mode

A `?preview=<name>` mode is a convenience that lands the page at a scroll
position. It is **not** evidence that the act renders correctly at that
position, and it drifts silently the moment the act's scroll window changes.

**What it cost:** when plan 067 recomputed the act's window from hard-coded
numbers to calculated ones, every preview mode kept aiming at the old window. At
`tes-till-ritning-3` the sheet sat **1329 px below the viewport**. Every review
that had used the preview modes since — Astra's included — had been judging the
wrong scroll position.

**The rule.** Before you judge an act from a preview mode, prove the mode lands
where it claims: read the element's bounding box against the viewport in that
mode and assert the overlap you expect. Failing that, **measure in real wheel
scroll** — `mouse.wheel`, 20 px steps, both directions — and say in your report
which method you used.

### M3 · Every geometric check proves itself against a broken variant first

Run each structural check **against a deliberately broken build** before you run
it against the real one. A check that returns green against both a broken and a
correct page measures nothing, and it will do so quietly, forever.

**What it cost:** it has happened three times in this project. Astra discarded
two of her own probe versions in r21 for exactly this reason, and rebuilt her
column probe in r22 after a false negative.

**The rule.** Every check ships with its injected fault, named in the report:
*"`.chapter-plate{clip-path:none;height:+900px}` → N hits, clean build → 0."*
A check reported without its broken-case value is not evidence and may not be
cited as one.

---

## 2 · Verification

### V1 · A review surface never caches

**What it cost:** `board.py` sent only `Last-Modified`, no cache headers. Chrome
applied heuristic freshness and served a previous round without revalidating.
The owner reviewed stale code **at least twice**, concluded nothing had been
built, and had to ask *"är det ens något gjort?"* — a reasonable conclusion from
what he was actually looking at.

Fixed in `scripts/board.py` (`Cache-Control: no-store, must-revalidate`). The
rule outlives the fix: **any surface a human uses to judge work must be
uncacheable, and must say so in a header, not in a hope.**

If you are ever handed a review surface and cannot state its cache behaviour,
assume it is lying to you until you have force-reloaded it once.

### V2 · Verify in the render, not in the bytes

**What it cost:** the lead grepped the served cell over HTTP, found the change,
and reported *"ändringarna finns"* — while the owner was looking at a page that
did not have it. Bytes on a server prove nothing about what a browser paints.

**The rule.** "It is in the file" is not a verification. "It is in the response
body" is not a verification. The verification is **a rendered image of the page
the human will actually open**, read as an image, by the person making the claim.
When the two disagree, the render wins, and the discrepancy is itself the finding.

---

## 3 · Orchestration

### O1 · Run Codex directly, never through a wrapper agent

`Agent(codex-review)` cost **305,000 Opus tokens per round**. Inside that, the
actual Codex call was **one request, 24 images in, 6.3 kB of text out** — billed
to the OpenAI quota, not to ours. The other ~300k was an Opus subagent
re-doing the measurement work before asking the question.

**The rule.** Drive `codex exec` from the shell. `scripts/astra.py` takes a
prompt file, a screenshot glob and an output path, and reads the answer back.
Screenshots come from a capture script; the prompt comes from you; the verdict
costs almost nothing.

**What you must NOT drop along with the wrapper.** The wrapper verified every
Codex finding against the file and the pixels before releasing it. In r21, three
of Codex's four findings fell to that check. **The verification step is
mandatory and it is now yours.** A Codex verdict is a draft, never a finding.

`astra.py` refuses two failure modes by construction and both matter: an empty
response is an **error**, not "no findings"; and more than ~28 images produces
sludge, so the selection must be narrowed rather than padded.

### O2 · A plan that is not on disk does not exist

**What it cost:** an architect subagent reported a complete plan **three times**
without being able to save it, and said so only when asked for the files
directly. A builder was nearly dispatched against a plan that was never written.

**The rule.** `subagent_type: Plan` is read-only. Before any builder is
dispatched, **`Read` the plan file from disk and confirm it is the plan you
think it is.** A plan reported in a message is a draft. The artifact is the file.

Same rule for reference baselines, målbilder and captured screenshots: if the
path cannot be opened right now, it is not an input.

---

## 4 · Review

### R1 · Aesthetic review is a sanctioned mode

This is the single largest method gain in the run, and it was nearly lost.

`agents/codex-review.md` was written for code and measurements. In r23 it was
instead given the mandate *"varför är detta fult, och vad skulle göra det
vackert"*, with the customer's rejection treated as correct by definition and the
reviewer instructed to find **what it had missed**. The result was the best
review in the project's history. Astra wrote, in plain terms:

> *"Jag mätte att den klippta rektangeln äger 44 % av viewporten och kallade det
> 'en hel yta som förändras'. Jag mätte formens area och tog den för närvaro."*

...and then produced a direction a builder could draw from, rather than a defect
list.

**The rule.** When the owner rejects work that passed every gate, the failure is
not in the gates — it is that no one was asked the aesthetic question. Dispatch
Astra in **`mode: aesthetic`**, with these framings:

- The customer has already judged it and the customer is right by definition.
  Your job is not to defend the work; it is to find what you failed to see.
- Name *why* it is ugly in the terms of form — area, weight, rhythm, contrast,
  what owns the viewport — not in adjectives.
- Weight the answer in `fidelity` and `ceiling`. An aesthetic pass whose output
  is a defect list has failed at its one job.

**What this does not license.** An aesthetic pass may not re-choose the palette,
the type or the direction — that is still a Step 2 decision and still a
gate-order violation. It judges how well the *committed* direction is executed,
and where the execution reads as empty. The distinction is exact: **"this is
badly executed against its own intent" is a finding; "it would look better as
something else" is not.**

### R2 · A rule in prose needs a mechanical test

**What it cost:** F-018 (*the page never narrates itself*) was written into
`FEEDBACK.md`, `anti-patterns.md`, `gates.md`, `copy-gate.md` and
`production-tells.md` — and then broken by the very next sentence the chain
delivered:

> *"Vi har ingen husstil. Formen kommer ur verksamheten, och därför valde vi de
> två projekt som ligger längst ifrån varandra."*

New words, same posture. The sentence explains **the page's own selection** to
the reader; nobody asked why those two examples are on the page. It passed the
scanner because the rule was written for microtext and this was set in body size.

**The rule.** Every copy rule that names a *shape* rather than a word gets a
mechanical check, or it will be broken by the next fluent paragraph. F-018's
check is `scripts/self_reference_scan.py`: it flags every sentence whose subject
is the page, the section, the example or the selection. Run it on the rendered
copy, and run it against the sentence above first — it must flag it.

A prose rule with no test is a preference, and preferences lose to fluency.

---

## 5 · The round ladder

The five rules above stop the chain lying. This one stops the spiral.

**37 rounds for 10 orders** was not a speed problem. It was that **no round was
ever allowed to finish before the next one started.** Round 23 built nine ordered
points and never ran its own § Verification; the nine were then judged
"executed on paper" and the level not reached, which is the only verdict possible
when nobody checked.

**The ladder, in order, no skipping:**

1. **Plan on disk** (O2). Read it before dispatching.
2. **Build one round.**
3. **Verify that round completely** — its own plan's § Verification, all of it,
   not the parts that fit the remaining budget. Disk space, quota and time are
   not verification exemptions; if they run out, the round is **incomplete**, and
   that is what gets reported.
4. **Only then** does the next round start.

**A round may not be retro-fitted.** If round N's verification reveals a fault,
the fix is round N+1 — never a silent edit folded into round N+2's build.

**And the reporting rule that follows from all of it:** a round whose images
nobody has looked at has not been verified, whatever the log says. Do not report
a build as done on the strength of a green exit code. The builder reporting
"grinden grön" while the lead's own reading found a new fault is not a rare
event — it happened in r20 and r22 of this run.

---

## 6 · Where these rules are enforced

| Rule | Written into | Mechanised by |
|---|---|---|
| M1 register properties | this file | the `@property` block; check returns `NaN` on undeclared |
| M2 preview modes | this file | bounding-box assertion, or wheel scroll |
| M3 broken-variant first | this file · `design-verify` | every probe ships its injected fault |
| V1 no caching | this file | `scripts/board.py` `Cache-Control` |
| V2 render not bytes | this file · `agents/design-critic.md` | the review contract's `recapture` disposition |
| O1 Codex direct | this file · `agents/codex-review.md` | `scripts/astra.py` |
| O2 plan on disk | this file | `Read` the file before dispatch |
| R1 aesthetic mode | this file · `agents/codex-review.md` | `mode: aesthetic` in the dispatch |
| R2 rule needs a test | this file · `copy-gate.md` | `scripts/self_reference_scan.py` |

**The one-line version, if you keep only one:** *the customer's rejection is
evidence, the chain's own measurement is a claim, and an unverified round is not
finished — it is unfinished, and says so.*
