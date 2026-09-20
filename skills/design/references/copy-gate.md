# Copy gate

**Load whenever a user-facing string is written or changed.** Also available standalone as `design copy-audit <target>`.

Two stages, in order. Stage 1 decides *what the copy has to do*; stage 2 removes the tells that mark it as machine-written.

**Both rulesets apply in every language.** For Swedish — or any non-English copy — resolve the equivalent of each pattern rather than skipping it. The tells transfer: inflated significance, promotional adjectives, negative parallelism, forced triads, and manufactured drama are structural, not lexical. Do not treat any rule as English-only.

## The order, in one line

Pass 0 UX copy → `Skill(copywriting)` → SlopMonster source test (every headline names its
source or is cut) → `Skill(copy-editing)` (seven sweeps with loop-backs) →
`Skill(humanizer)` / `Skill(humanizer-svenska)` per language, both named → the six-step
manual cleanse → `deslop.py --view` per section (English) plus the Swedish twins by hand →
[optional rival-model cleanse, English only, then **re-lint**] → gate 75 sweep +
`preflight_taste.py --copy`.

Stage 1 and stage 2 below are the middle of that sequence, not the whole of it. Pass 0 runs
first because a page whose labels and error states are wrong does not get better by being
persuaded harder.

---

## Pass 0 · UX copy

The interface half, before any marketing pass touches it. Sources: impeccable
`clarify.md` and `ux-writing.md`. `humanizer-svenska` cannot do this job — it edits prose,
and this is about labels, states, and the messages a page shows when something goes wrong.

**Message hierarchy.** For each state, decide in this order: (1) *the one fact the user
needs now*; (2) *the action available next*; (3) *supporting context that changes the
decision*; (4) *the appropriate tone for this moment*. Then say each idea once — *"if the
heading already explains the state, the introduction should add new information or
disappear."*

**Labels are verb + object.** Never `OK`, `Submit`, `Yes/No`, `Click here`. The label
describes what will happen, not the gesture that triggers it:

| Bad | Good | Why |
|---|---|---|
| OK | Save changes | Says what will happen |
| Submit | Create account | Outcome-focused |
| Yes | Delete message | Confirms the action |
| Cancel | Keep editing | Clarifies what "cancel" means |
| Click here | Download PDF | Describes the destination |

For destructive actions, name the object and the consequence, and show the count: "Delete 5
items", not "Delete selected". *"Prefer undo over confirmation when recovery is safe."*
When confirmation is unavoidable, the action is named on both the message and the button.

**Errors answer three questions, in order:** *(1) what failed; (2) why, when known and
useful; (3) how to recover or what alternative remains.* Never expose an internal code as
the primary message, and never promise a cause the system cannot know. Templates:

| Situation | Template |
|---|---|
| Format error | "[Field] needs to be [format]. Example: [example]" |
| Missing required | "Please enter [what's missing]" |
| Permission denied | "You don't have access to [thing]. [What to do instead]" |
| Network error | "We couldn't reach [thing]. Check your connection and [action]." |
| Server error | "Something went wrong on our end. We're looking into it. [Alternative action]" |

Reframe away from blame: *"Please enter a date in MM/DD/YYYY format"*, not *"You entered an
invalid date"*. Treat privacy, payment, deletion, access loss and blocked work seriously —
*"warmth is welcome, jokes are not."*

**Empty states are four different states, not one.** An empty state *"distinguishes first
use, no results, filters, permissions, and failure"*. First use teaches and offers the one
next action; no-results says what was searched for; a filter result says which filter is
hiding things and offers to clear it; a permissions state names who can grant access. One
generic "Nothing here yet" for all four is the failure this pass exists to catch.

**Loading names the real operation** and sets an honest expectation when the wait is
meaningful. "Saving your draft…", not "Loading…". Show determinate progress when it is
available; *"never invent progress."*

**Write for translation.** Complete translatable sentences, never concatenated fragments;
numbers and variables kept structured so translators can reorder them; expansion allowed
for rather than abbreviated away:

| Language | Expansion |
|---|---|
| German | +30 % |
| French | +20 % |
| Finnish | +30–40 % |
| Chinese | −30 % characters, same width |

A CTA that fits at exactly one line in English and breaks at +30 % is a gate 49 failure in
German. Size the affordance for the expansion, or shorten the English label.

**One term per concept.** Delete / Remove / Trash → pick one. Settings / Preferences /
Options → pick one. *"Do not vary words for literary effect in an interface."* Keep a short
glossary when the inconsistency spans more than one surface.

**Plain-word substitutions** are cited, not restated: the 14-row replacement table
(`utilise → use`, `facilitate → help`, `prior to → before`, `commence → start`, …) lives in
`upstream/inclusive/cognitive-accessibility/skills/plain-language-design/SKILL.md`. Read it
there when a line is stuck at the formal register. Its reading benchmarks bind here:
buttons, labels and error messages target grade 4–6, body copy grade 6–8, and any sentence
over 25 words gets flagged.

---

## Stage 1 · `copywriting`

Invoke `Skill(copywriting)`.

**Inputs, gathered first:** page purpose · audience · product/offer · traffic context (where the reader came from and what they already believe).

**Brand voice comes from the derived system.** The CONTENT FUNDAMENTALS section written during [`brand-derivation.md`](brand-derivation.md) — tone, casing, first vs second person, emoji, vibe, with real examples — is the input that makes this stage enforce *this brand's* voice instead of generically good copy. If that section does not exist yet, the gate still runs, but say that the voice is unconstrained.

**Structure.** Above the fold: headline, subheadline, CTA. Then social proof, problem, solution, how it works, objections, final CTA — as the page actually needs, not as a checklist to fill.

**Discrete facts get their own line; a process gets a sentence.** A price, a spec, a date — each is its own bold lead line, not folded into a paragraph with two other facts ("Bottentvätt 450 kr, propelleravdrag 350 kr. Större jobb går till vår partnerverkstad" reads as a wall of facts). What the business *does* for the customer stays a sentence in flowing prose, in its own section, described the way a person would say it out loud ("vi tvättar botten om du bett om det") — not re-listed as another line item once it already has a price above. Splitting a dense multi-fact paragraph into short bold-led micro-paragraphs (one claim, one clarifying sentence, repeat) reads as more scannable and more inviting without losing information; a single paragraph carrying four unrelated facts reads as cold regardless of how correct each fact is. (AB20/AB21, 2026-09-03: two independent briefs, same finding both times — see `tests/ab/{20-copy-hybrid-kajplats,21-copy-hybrid-reglabok}/verdict.md`.)

**Headline formulas** as starting points, not templates to ship: `{Achieve outcome} without {pain point}` · `The {category} for {audience}` · `Never {unpleasant event} again`.

**CTA formula:** `[Action Verb] + [What They Get] + [Qualifier if needed]`. "Start Free Trial" over "Sign Up".

**The five principles:**

1. Simple over complex — no jargon
2. Specific over vague — no buzzwords like "streamline"
3. Active over passive
4. Confident over qualified — remove hedging
5. Honest over sensational — fabricated claims create legal liability

**Prohibited:** exclamation points · weak CTAs ("Submit", "Learn More") · buried value propositions.

**Output contract.** The skill returns page copy organised by section, plus **annotations**
(for each key element: why this choice, which principle it applies) and **2–3 alternatives
for every headline and CTA**, each with its rationale. Copy handed back as a single block
with no annotations and no options has skipped the part that makes it reviewable — ask for
the alternatives rather than accepting the first line.

### CTA rules (mandatory, from `design-taste-frontend` § 4.5)

These are copy decisions with a layout consequence, so they bind here and are re-checked
mechanically at gate 49.

- **No duplicate CTA intent.** *"Two CTAs with the same intent on one page is a Pre-Flight
  Fail."* "Get in touch" + "Contact us" + "Let's talk" + "Start a project" + "Reach out" are
  one intent; pick one label and use it in the nav, the hero and the footer. Same for "Try
  free" / "Get started" / "Sign up free", and "View work" / "See selected work" / "Browse
  projects". **One label per intent, page-wide.**
- **CTA wrap ban.** Button text fits one line at desktop. *"Three words max for primary
  CTAs, ideally 1–2."* Fix by shortening the label first, widening the button second; never
  by constraining `max-width` on a CTA. A wrapped desktop CTA is a fail, not a nuance.
- **Button contrast check.** Verify the label against the fill it actually sits on before
  shipping: white button with white text, a transparent button on the page ground with no
  border, a ghost button over a photograph — all banned. Ghost buttons over imagery get a
  backdrop, a scrim, or a stroke. (Gate 41 measures it; this is where it gets caught while
  the label is still being written.)
- **Form contrast check.** Inputs, placeholder text, focus rings, helper text and error text
  all clear AA against the section ground.

### Density (from `design-taste-frontend` § 4.9)

*"Landing pages live on the first impression, not the full read."*

- **Default shape per section:** headline **≤ 8 words** + sub-paragraph **≤ 25 words** + one
  visual asset **or** one CTA. Anything beyond that is justified by the section's job or cut.
- **No data-dump sections.** A 20-row table or a 30-row list on a marketing page is the
  wrong layout, not long copy: top 3–5 highlights plus a link, or a different page entirely
  if the data *is* the product. Over five items, the fix is a different component, not a
  longer list.
- **Copy self-audit, mandatory before ship.** Re-read *every* visible string — headlines,
  subheads, eyebrows, button labels, body, captions, alt text, footer, error messages — and
  flag any that is grammatically broken, has an unclear referent, reads as cute-but-wrong
  wordplay, or *"reads like an LLM trying to sound thoughtful"* (passive-aggressive
  humility, fake-craftsman labels, mock-poetic micro-meta). Rewrite every flagged string.
  *"If unsure whether a string makes sense, replace it with a plain functional sentence. AI
  generated cute copy is worse than boring copy."*
- **Fake-precise numbers are flagged.** `92 %`, `4.1×`, `48k`, `5.8 mm` either come from
  real data, are explicitly labelled as mock, or are banned. *"Don't fake engineering
  precision the brand doesn't claim."* This is gate 46 at the decimal point.
- **One copy register per page.** Technical mono, editorial prose and marketing punch do not
  mix in one composition unless the brand voice explicitly calls for it.

### The copy test

Refero's litmus test for length, and the one that ends most arguments about a section:
*"If deleting 30 % of copy improves the page → keep deleting. AI over-writes; real
designers edit down."* Run it on the built page, not the draft — the deletion that improves
a page is usually visible only once the type is set. The sibling image, card and brand tests
live in [`slop-test.md`](slop-test.md).

---

## Stage 1b · `copy-editing` — the seven sweeps

Invoke `Skill(copy-editing)`. Seven sequential passes, each on one dimension, because
*"multiple focused passes beat one unfocused review"*:

| # | Sweep | Focus |
|---|---|---|
| 1 | Clarity | Can the reader understand what you're saying? |
| 2 | Voice and tone | Is the copy consistent in how it sounds? |
| 3 | So what | Does every claim answer "why should I care?" |
| 4 | Prove it | Is every claim supported with evidence? |
| 5 | Specificity | Is the copy concrete enough to be compelling? |
| 6 | Heightened emotion | Does the copy make the reader feel something? |
| 7 | Zero risk | Have we removed every barrier to action? |

**The loop-back rule is the whole method.** After sweep N, re-run N−1 down to 1 and confirm
the later edit did not break an earlier one — the skill states it per sweep ("after this
sweep: return to Specificity, Prove It, So What, Voice and Tone, then Clarity"). A single
forward pass through seven headings is not this framework; it is a checklist with the
verification removed. Repeat until a full sweep finds nothing new.

**Two sweeps resolve against rules this system already has, and the resolution is stated
here so the pass does not fight itself:**

- **Sweep 4 (Prove it) has no proof to add.** Discipline 2 and gate 46 forbid inventing a
  metric, a testimonial, a logo count or a case study. The sweep's honest outputs are: a
  softer claim the product can stand behind, `[needs number]`, or a question to the user.
  It never fills the gap.
- **Sweep 6 (Heightened emotion) raises via specificity, not adjectives.** The sweep looks
  for "flat, informational language"; the humanizer bans promotional language outright. This
  system resolves in the humanizer's favour: emotion is added by naming the moment, the
  number, or the loss — the scene, per [`copy.md`](copy.md) § Scenes, not claims — never by
  reaching for "vibrant", "powerful", or an exclamation mark. If a sweep-6 edit reads as a
  bigger adjective, it is a sweep-6 failure, not a humanizer conflict.

**Transitions to avoid (AI tells)**, from `copywriting/references/natural-transitions.md` —
the seven the humanizer's own catalogue does not carry: *"That being said,…"* · *"It's worth
noting that…"* · *"At its core,…"* · *"In today's digital landscape,…"* · *"When it comes to
the realm of…"* · *"This begs the question…"* · *"Let's delve into…"*.

---

## Stage 2 · `humanizer`

Invoke `Skill(humanizer)` in embedded mode — final text only, no ceremony.

**The core constraint:** *"Preserve the information, not the shape."* Every fact survives; structure changes freely. **Never invent facts.** Match the author's voice unless a user-supplied sample overrides the style rules.

33 patterns in four families:

**Content** — inflated significance ("marking a pivotal moment") · undue notability emphasis · superficial "-ing" analyses · promotional language ("vibrant", "nestled") · vague attributions · formulaic "challenges" sections.

**Language** — overused AI vocabulary ("delve", "tapestry", "interplay") · copula avoidance ("serves as" for "is") · negative parallelism ("not only… but") · forced rule-of-three lists · synonym cycling · false ranges · passive voice · em and en dashes.

**Style** — em dashes banned outright (sample-override exception) · excessive boldface · inline-header lists · title-cased headings · emojis · curly quotes replaced with straight quotes.

**Communication** — chatbot artifacts ("I hope this helps") · knowledge-cutoff disclaimers · speculative gap-filling · sycophantic tone · filler phrases · excessive hedging · manufactured drama · aphorism formulas · theatrical rhetorical openers.

**One counterweight worth holding onto:** good human writing has personality. Sterile writing is equally suspect. The goal is copy that reads as written by someone, not copy sanded to neutrality.

### What not to flag — the humanizer's own false-positive list

The skill ships a DETECTION GUIDANCE section, and skipping it is how this stage guts good
prose. *"A clean human writer can hit several of the patterns above without any AI
involvement."* Not reliable indicators on their own:

perfect grammar and consistent style (*"polish does not equal AI"*) · mixed casual and
formal registers · "bland" or "robotic" prose without the specific tells · formal or
academic vocabulary (*"don't flatten 'ostensibly' or 'constituent' just because they sound
brainy"*) · a letter-style opening or closing · a common transition word in isolation
(*"one however is not a tell"*) · curly quotes alone · **em dashes alone** (*"evidence only
when paired with formulaic sales-y rhythm"*) · one short emphatic sentence · "honestly" or
"look" mid-sentence · unsourced claims · correct, complex formatting · **secondhand text**
(*"do not rewrite watched phrases inside quotations, titles, proper names, or examples where
the phrase is being discussed rather than used"*).

**The cluster rule:** *"A single em dash means nothing; em dashes plus rule-of-three plus
vibrant tapestry plus a 'Conclusion' section is a confession."*

**Note the em-dash carve-out does not travel.** The humanizer treats a lone em dash as weak
evidence *of AI authorship*; gate 75 bans the character from visible page text regardless of
who wrote it. Gate 75 wins on the page; the humanizer's rule stands only as a detection
heuristic. Do not cite it to keep a dash.

**Signs of human writing to preserve** (over-editing destroys these): specific, unusual,
hard-to-fabricate detail (*"LLMs round off specifics; humans hoard them"*) · mixed feelings
and unresolved tension · dated, era-bound references · first-person editorial choices the
writer can defend · variety in sentence length · genuine asides, parentheticals and
self-corrections · anything written before ChatGPT's launch.

### The four Swedish patterns with no English twin

`humanizer-svenska` carries sixteen patterns; four of them have no counterpart in the
English catalogue and are therefore invisible to any English-first pass:

- **§ 5 Passiv röst som falsk formalitet** — passive voice used to sound official.
- **§ 6 Nominaliseringsöverdrift** — a verb turned into a noun to sound weightier.
- **§ 7 Anglifieringsimporter** — English constructions carried into Swedish word for word.
- **§ 15 Kopulaundvikande** — *utgör* / *representerar* / *fungerar som* where *är* is meant.

Name them when running the Swedish pass, so the report says which pattern was resolved
rather than "made it sound more Swedish".

### What no humanizer pass may touch

From the cleanse prompt, and binding on every pass in this gate: *"Preserve any HTML tags,
markdown structure and placeholders exactly as they appear."* A humanizer pass rewrites
prose. It does not restructure markup, renumber headings, collapse a list into a paragraph,
or resolve a `[needs number]` placeholder — the placeholder is the finding, and removing it
hides an unearned claim rather than fixing one.

---

## Interaction with the mechanical detector

Five detector rules catch the cheapest cases before this gate runs, and they fire on every UI edit:

`em-dash-overuse` · `marketing-buzzword` · `theater-slop-phrase` · `aphoristic-cadence` · `repeated-container-text`

Treat their findings as already-known. This gate covers what a regex cannot: structure, offer clarity, invented claims, voice.

## Interaction with honest copy

Discipline 2 in the front door and gate 46 bind here and are **not** overridable by stage 1's persuasion goals. If the user did not supply a metric, testimonial, logo, or case-study count, the copy does not get one. A stat-led layout with no stats becomes a different layout, a labelled placeholder, or an honest omission — never an invented number.

When stage 1 wants proof the product cannot supply, say so and offer the placeholder. *"+47% conversion"* invented to fill a proof bar is the single worst failure this gate can have.

---

## `copy-audit` — the standalone verb

Runs both stages over existing copy **without editing**.

1. Extract every user-facing string in scope — visible text, `alt`, `aria-label`, `placeholder`, `title`, button labels, error and empty states, meta title and description.
2. Run both stages against each.
3. Report as a table: **Before · After · Why**, one row per changed string, citing the stage and the specific rule.
4. Flag separately, never auto-fix: any string containing a **claim** — a metric, a customer count, a benchmark, a capability. Those need the user, not a rewrite.
5. Apply only on confirmation. On a live page this is a content change, and it is the user's call.

Scope note: run per surface, not per repo. A whole-codebase sweep produces a table nobody reads.

## 2026-09-03 — SlopMonster folded in (AB11)

**Pass 1b · Where does the line come from?** Before copy-editing, every headline and
lead names its source or is cut: (1) what the trade actually does (a specification beats
three adjectives), (2) what the customer already fears, (3) what the competition will not
say (a refusal positions), (4) a line that arrived already good. A line with no source is
a slogan. Never invent proof: no counts, testimonials or ratings the business has not
earned; write `[needs number]` and move on. (SlopMonster, `references/upstream/slopmonster/references/principles.md`.)

**Mechanical gate for English strings.** After the three passes run
`python ~/.agents/skills/slopmonster/tools/deslop.py <file|--text>` and read the hits.
Vocabulary, constructions, dash cadence and invented proof are fixes; a rule-of-three hit
on a list that is genuinely three things (record · replay · diff) is a judged pass, say so.
The scorer is English-only: it returns a false 5/5 on Swedish copy.

**Run it per section, not per page.** `deslop.py page.html --view hero` scores one element
by id. A whole-page score averages a clean hero against a sloppy footer and tells you
nothing actionable; a per-section score names the section to rewrite. Empty input fails
rather than passing, on purpose — *"a cleanse that times out leaves a zero-byte file, and a
gate that stamps that CLEAN reports slop as clean exactly when the pipeline broke."*

**A plainer word, not a synonym.** *"Replace with a plainer word, not a synonym of the same
word."* `leverage` → `use`, not `utilise`. `elevate` → the verb that actually happens.
Swapping one register-heavy word for another scores the same and reads worse.

**Compound stacking is a punctuation tell.** Four or more hyphenated compound modifiers
inside one sentence (a 220-character window) is a hit. *"One is ordinary English: 'a
25-year warranty'. Four in a sentence is a model reaching for authority it has not earned,
and the giveaway is that they stack in front of one noun: 'our industry-leading,
context-aware, best-in-class, AI-powered platform'."* Real trade copy runs one to three per
hundred words. The fix is to keep the one that carries information and delete the rest.

**Re-lint after every cleanse — score it, don't just read it.** *"A frontier model is very
good at removing tells and quite capable of adding new ones while it does. An unlinted
cleanse is a coin flip."* The linter gets the first and the last word, because it is honest
and the model is persuasive. Ship only at 5/5.

**The six-step manual cleanse**, run after the skills and before the linter (from the
Ridgeline build's own checklist):

1. **Strip the adjectives.** Delete every adjective, read it back, restore only the ones
   whose absence changed the meaning. *"Usually one in five survives."*
2. **Find the number.** Any claim that could carry a number gets one, or gets cut.
   "Long-lasting" becomes "25 years". *(Real numbers only — gate 46.)*
3. **Name the noun.** "Materials" becomes "ice and water shield"; "quality workmanship"
   becomes "six nails per shingle". *"The specific noun is the whole trick."*
4. **Cut the throat-clearing.** Delete the first sentence of each paragraph and check
   whether anything was lost. *"Usually it was a run-up."*
5. **Read it aloud.** Anything you would not say standing in front of the customer comes out.
6. **Verify every claim, and mark the unverified ones *on the page*.** Numbers,
   certifications and warranty terms get checked against reality before publishing.
   *"Anything unverified is marked as a placeholder on the page, not quietly left in."* In
   the upstream build that meant a visible callout naming five wireframe figures as
   unverified rather than shipping them as fact.

**Why the skills run before the linter.** The Jasper receipt closes on it: *"The linter gets
you to 'not machine'. The principles get you to 'good'."* Its own run went 3/5 → 5/5 with
the meaning intact, and the copy was still generic — no numbers, no named pain, no refusals.
A 5/5 score is the floor of this gate, never its result.

**Swedish twins the scorer cannot see** (humanizer-svenska checks these by hand):
`inte bara X — det är Y` · tricolons joined by `och` (`passion, precision och kärlek`) ·
`i hjärtat av` · `kurerar` · `älskad mötesplats` · `sömlöst` · `unik upplevelse` · a lede
that restates the headline.

**Swedish twins of the filler verbs.** `design-taste-frontend` § 9.D bans *"Elevate",
"Seamless", "Unleash", "Next-Gen", "Revolutionize"* and the humanizer adds *delve* and
*tapestry* — *"concrete verbs only"*. The Swedish forms slip past both catalogues and are
banned identically: **lyfta** (as in *lyfta ditt varumärke*) · **sömlös / sömlöst** ·
**nästa generation** · **revolutionera** · **frigöra potentialen** · **väva samman**. Replace
each with the verb that names what actually happens.

**Gate 75 still wins.** SlopMonster tolerates single em-dashes; this system does not.
Zero visible em-dashes, en-dash only in ranges. The optional rival-model cleanse
(`tools/cleanse.sh`, codex) is allowed on English marketing pages only, and its output is
re-read: in AB11 it changed little and appended a summary it was told not to write.

## 2026-09-20 — F-018, the page narrating itself

A section lede that describes the section is slop at any type size, and the size-based
scanner cannot see it. Added to every pass as a standing check.

**The shape**, from the Alunix chapter lede Anton rejected twice: *setup* ("X är en
florist och Y en restaurang") → *disclaimer* ("Ingen av dem finns") → *roadmap* ("Vi går
igenom vad vi valde i dem och varför"). It is recognisable by its cadence, not its
vocabulary — rewriting the words while keeping the three beats reproduces the fault, which
is what happened on the second attempt.

**In pass 0 and in `copywriting`:** never open a section by saying what the section
contains. Write about the business, the work, or the reader's question.

**In `copy-editing`:** flag any sentence whose subject is the page, the section, the
example, or the reader's progress through it ("nedan", "vi går igenom", "det här avsnittet",
"som ni strax ser"). Flag any caveat about the material's status placed before the
material.

**In `humanizer-svenska`:** the cadence survives translation and paraphrase. Read the
three beats, not the words.

**The deletion test, applied last:** cut the lede and read the section. If nothing is lost
but a description of what the reader can already see, ship it cut. A heading standing
alone is a legitimate setting and usually the better one — it is never given a lede to
fill space.
