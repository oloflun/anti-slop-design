# Copy

> **Diverges from upstream Hallmark: T6 port (2026-09-09).** This file has been
> extended with material ported from the upstream packages named in the design
> chain's v4 plan, sections 2.1 to 2.5. Every addition is traceable to a source
> file; where a port collided with a rule already in this file, the conflict is
> resolved in the text and the winner is named. Upstream is no longer the bar
> here, and `verify-design-system.py` records the divergence rather than
> treating it as drift.

Words are part of the design. A great layout with stock copy looks generic. Tight copy in an average layout reads as considered.

## Principles

- **Specific verbs.** "Save changes" beats "OK" beats "Submit".
- **Labels describe.** "Email address" beats "Email".
- **Link text stands alone.** "View pricing plans" beats "Click here".
- **Errors are instructions.** Describe what broke, why, how to fix — in that order.
- **Active voice.** "We couldn't find your account" beats "Your account could not be found".
- **Consistency.** Pick one of "Delete" or "Remove". Pick one of "Sign in" or "Log in". Use it everywhere.
- **One name per action, all the way through.** *"An action keeps the same name through the whole flow, so the button that says 'Publish' produces a toast that says 'Published.'"* (`upstream/anthropic/frontend-design/SKILL.md`.) The button, the confirmation, the toast, the empty state and the log entry use one verb. A button labelled "Publish" that reports "Your post is live" has broken the trail the reader was following.
- **Reading age 12–14.** Aim for roughly 6th–8th grade: short sentences, common words, one idea per sentence — *"if a sentence has 'and' in the middle, consider splitting it"* (designpowers `accessible-content` § 1). This is a floor on comprehension, not a ceiling on voice: the tone samples further down all clear it. Jargon is allowed only where the audience demonstrably uses it, and then it gets a plain explanation the first time.

## Buttons

Use the verb for the action the button performs.

Good: `Save changes`, `Create account`, `Send invitation`, `Copy link`, `Open file`.
Bad: `OK`, `Submit`, `Click here`, `Continue` (only as the secondary button of a multi-step flow).

## Error messages

Three parts:

1. **What happened.** Past tense, factual. "That card was declined."
2. **Why, if known.** "Your bank flagged the charge."
3. **What to do.** Imperative. "Try another card, or contact your bank."

Never apologetic for the *user's* input. Don't say "Oops!" on a validation error. A form that won't accept a value should explain the value, not perform embarrassment.

## Empty states

Three beats:

1. One line naming what's empty. "No projects yet."
2. One line on why this matters / what projects are. "Projects group your tasks and team."
3. One button. The single next action. "Create a project".

## Loading

- Short wait: spinner with no text.
- Medium wait (>2s): spinner + "Loading…".
- Long wait (>10s): spinner + progress indication + an honest label — "Compiling (this can take a minute)."

## The six things a piece of copy answers

Refero's universal structure. Any block of page copy answers these, in roughly this order;
*"if copy feels empty, one of these is missing"*
(`upstream/refero/skills/refero-design/references/copywriting.md`):

1. **Context** — where is the reader right now?
2. **Job to be done** — what are they trying to accomplish?
3. **Solution** — what do you offer?
4. **Outcome** — what changes for them?
5. **Conditions** — limits, tradeoffs, requirements.
6. **Next step** — what should they do now?

**Point 5 is the one that gets dropped**, and it is the one that buys the other five their
credibility. "Works with Gmail and Outlook. iCloud is next" is a limit stated out loud, and
it makes the two supported clients believable. A page that lists only capabilities reads as
a brochure; a page that names one honest limit reads as a product someone actually built.
It is also the honest-copy rule from the other direction — see gate 46 and
[`copy-gate.md`](copy-gate.md) § Interaction with honest copy: an unearned proof point is
banned, and a stated constraint is the thing that replaces it.

## Scenes, not claims

*"People remember images, not abstractions."* The scene template is **who + where + what
happens + what changes**.

- Bad: *"A better workflow for teams."*
- Good: *"At 10:03 the PM drops a task. At 10:07 the designer has real references and a draft."*

A claim asserts a property of the product. A scene puts the reader somewhere and lets them
watch the property happen. When a section refuses to get concrete, it is usually because
nobody has decided who the reader is or what minute of their day this is — that is a brief
problem surfacing as a copy problem, and it goes back to the brief rather than getting
another adjective.

## Rhythm

*"Flat rhythm kills attention."* Change sentence length every one to two lines. One
paragraph, one punch.

> Fewer clicks.
> Clearer decisions.
> Less arguing in Slack.

This is the positive form of a rule the [`copy-gate.md`](copy-gate.md) humanizer pass only
states negatively (the AI cadence is even, mid-length, and never varies). Landing a
three-word sentence after a long one is the fastest human signal in the text.

## The sticky-line test

*"Every important page needs at least one line that can be screenshotted, quoted,
remembered."* Patterns that carry it: *"Not another X. Finally Y."* · *"Less noise. More
decisions."* · *"Stop guessing. Start seeing."*

Read the built page and point at the line. If nothing is quotable, nothing sticks, and the
page is a competent brochure. One line per page, not one per section — a page where every
heading is trying to be the sticky line has no sticky line.

## Quotes and testimonials

From `design-taste-frontend` § 4.10:

- **Max 3 lines** of quote body. Never 6. A longer original gets cut — *"a landing-page
  quote is a snippet, not the full review."* At footer-testimonial sizes the cap can
  stretch slightly; the spirit is "fits in a glance".
- **Attribution is name + role + optionally company.** Never a bare first name
  (`- Sarah`). A quote nobody can place is a quote nobody believes.
- **Real typographic quote marks, or none at all.** Not straight ASCII.
- **No dashes inside the quote body** as a design flourish. Attribution uses ` - ` or a
  line break — gate 75, zero tolerance, and it applies inside quotation marks exactly as it
  does outside them.
- A quote the business has not been given is a fabricated testimonial: gate 46, not a
  styling question.

## Headings, labels, alt text

The structural half of copy. All four are content, and all four are read aloud by somebody.
From designpowers `accessible-content`:

- **One H1 per page**, describing the page's purpose. Headings follow H1 → H2 → H3 without
  skipping levels, and are descriptive enough that *"a screen reader user scanning headings
  alone should understand the page structure"*. Never use a heading tag to get big bold
  text — that is what CSS is for.
- **Placeholders are not labels.** They disappear on focus. Every input carries a visible
  label, programmatically associated (`<label for>` or `aria-labelledby`).
- **Format hints go before the input, not after.** "DD/MM/YYYY" above the field, where it
  is read before the reader types, not below it where it is read after they got it wrong.
- **Required state is visible and announced**, not carried by an asterisk alone.
- **Errors are associated with their field** via `aria-describedby`, placed adjacent to it,
  and announced (`aria-live="assertive"` or by moving focus).
- **Alt text is content, not metadata:**

| Image type | Alt text approach |
|---|---|
| Informative | Describe the information the image conveys, not the image |
| Decorative | Empty alt (`alt=""`) — do not describe decoration |
| Functional (button/link) | Describe the action: "Search", not "magnifying glass" |
| Complex (chart, diagram) | Brief alt plus a full description in surrounding text or `<details>` |
| Image of text | Reproduce the full text |

Link text follows the same rule as buttons: *"Read the accessibility guidelines"*, never
"Read more". Where several "Read more" links genuinely must coexist, each one is
distinguished by `aria-label` or by visible text.

## Microcopy bans

- "Click here." Link text must stand alone.
- "Oops!", "Uh oh!", "Something went wrong." Name the thing that broke.
- "Enter your email below." If the input is below, you don't need to say so.
- Exclamation marks in error states.
- Humour in frustration paths (forgot-password, payment-failed, account-locked).
- Stock placeholder names: Jane Doe, John Smith, Lorem Ipsum (unless the page is a lorem-ipsum tool).
- Startup clichés in product copy: Acme, Nexus, Unleash, Seamless, Supercharge, Transform, Elevate, Empower, Delight, Magical.
- Marketing copy that promises a feeling without naming a feature. "Experience the power of ___" is empty.

## Proper typography

- Curly quotes: `"Hello"`, `'word'`.
- Em-dash for interruption: `—` (U+2014). En-dash for ranges: `10–20` (U+2013). Never `--`.
- Ellipsis: `…` (U+2026). Never `...`.
- Apostrophe: `’`. Never the prime `'`.
- Non-breaking space before units: `10 kg`, `5 min` (use `&nbsp;` or U+00A0).

If the text is loaded from a CMS, configure Smart Quotes in the CMS. If it's hard-coded, write it correctly.

---

## Voice and tone

**Voice is who you are. Tone is how you say it right now.** Voice stays constant across the
page; tone adapts to the moment. Ported from designpowers `voice-and-tone`, which supplies
the axis this file's tone samples were missing: the samples show what a voice *sounds*
like, this shows how to *state* one so a second writer can hold it.

**Step 1 — name 3 to 5 voice attributes, each as "this, not that".** The second column is
the load-bearing one; *"the 'not that' column prevents drift"*, because every attribute has
a cheap version the model reaches for first.

| Attribute | This | Not that |
|---|---|---|
| Warm | Friendly, approachable | Sycophantic, emoji-heavy |
| Knowledgeable | Confident, precise | Academic, condescending |
| Direct | Clear, action-oriented | Blunt, cold, robotic |
| Encouraging | Celebrates effort | Patronising, fake-cheerful |

**Step 2 — set tone per context.** One voice, six settings:

| Context | Feel |
|---|---|
| Success | Celebration, warmth, brief |
| Error | Calm, helpful, **no blame** |
| Onboarding | Welcoming, confidence-building |
| Empty state | Inviting, action-oriented |
| Loading | Reassuring, brief |
| Destructive | Clear, calm, reversible |

**Step 3 — write the vocabulary list.** Two columns, always/never, in this product's own
domain words: *water* not *irrigate*, *happy* not *optimal*, *you* not *the user*. The list
is a constraint the copy pass is held to, not a suggestion.

The attributes and the vocabulary belong in `BRIEF.md` alongside the tone the design-context
gate committed to ([`SKILL.md`](../SKILL.md) Step 1), so the copy gate has something
specific to enforce instead of generically good copy. Where the brand-derivation pass has
already written CONTENT FUNDAMENTALS, that is this artifact — extend it, don't write a
second one.

## Voice samples per tone

The skill bends toward distribution-default copy ("Built for the modern team", "Unleash your X", "Where A meets B") unless given non-default voices to imitate. The samples below are *real opening lines* from sites that defy that distribution. **Imitate the kind of specificity** — named places, named dates, named verticals, refusal of metaphor, refusal of the verb — not the wording. The tone column maps to the seven tones the design-context gate (see [`SKILL.md`](../SKILL.md) Step 1) commits the user to.

### Editorial

Three voice patterns: *date-anchored*, *refusal of the verb*, *enumerative*.

- *"Creative direction, design and type for culture since 2003."* — apracticeforeverydaylife.com — date + named verticals
- *"A monthly art publication featuring contributions by some of the most engaged thinkers working today."* — e-flux.com/journal — uses cadence (*monthly*) and a verb (*featuring*) that's specific
- *"A thing well made."* — klim.co.nz — refusal of the verb, treats design as material
- *"Frieze elevates the provocative and brilliant leading voices who shape and challenge today's art world."* — frieze.com — uses *challenge* instead of *empower*
- *"We design everything for everyone."* — pentagram.com — refusal of marketing verbs; democratic claim
- *"Writer + Photographer."* — craigmod.com — three words, two roles, no padding
- *"Type, set with care."* — Hallmark Specimen — three words; the comma is the design
- *"I'm a French design technologist based in London. I make websites and fonts, amongst other physical and digital artefacts."* — mathieutriay.com — named place, named deliverables, "artefacts" signals craft

### Brutalist

Three voice patterns: *flat declarative*, *refusal of metaphor*, *direct address with consequence*.

- *"The product development system for teams and agents."* — linear.app — flat declarative; no flourish, no "powered by AI"
- *"Resend is the email API for developers. Send transactional and marketing emails at scale with a simple, modern API."* — resend.com — names the form factor, the audience, and what it does
- *"Purpose-built for planning and building products. Designed for the AI era."* — linear.app — names the era plainly, no euphemism
- *"WE ARE A STUDIO. WE ARE NOT A PLATFORM."* — Hallmark Meridian (test 04) — defines by refusal, all caps
- *"We design products that last twelve years. We do not design products that need replacing every two."* — concrete number, paired declaration
- *"A toolkit for assembling new worlds from the scraps of the old."* — are.na — second-position copy that breaks template
- *"NO COMPROMISE."* — Hallmark Brutal — two words; the period is the design
- *"We will not put our work behind a chatbot. We will answer the email ourselves."* — declarative refusal, two short sentences

### Soft

Three voice patterns: *poetic restraint*, *passion via enumeration*, *vulnerability with proof*.

- *"It's about time."* — cron.com — pun without winking; restraint
- *"Time is our most precious resource."* — Notion Calendar — opens on the philosophical premise, then gets concrete
- *"Designer for the Web (v. XIX)."* — lynnandtonic.com — version number signals craft-in-progress
- *"Design engineer creating software that makes people feel something."* — rauno.me — emotional outcome over feature list; "feel something" avoids genre cliché
- *"All I want to do is build websites. Typography, motion design, copywriting, performance — the web is an endless medium of opportunity."* — paco.me — passion via enumeration; vulnerability ("scratched the surface")
- *"I craft UI demos that explore the power of the web and help others sharpen their skills."* — jhey.dev — names the verb (*craft*), names the audience (*others*)
- *"Soft, but exact."* — Hallmark Hum — two short adjectives, one comma, full stop
- *"This page is soft because the surface should be soft. The rules underneath are not."* — pairs claim with refusal

### Technical

Three voice patterns: *spec-embedded prose*, *measured language*, *data-first opening*.

- *"The 14-inch MacBook Pro with M5 brings serious speed and advanced on-device AI to the personal, professional, and creative work you do every day."* — apple.com — spec embedded in prose; "serious speed" is measured language
- *"434 total posts. New CSS you feel like you could use today."* — nerdy.dev (Adam Argyle) — data-first; "feel like" suggests genuine utility
- *"$ streampipe parse access.log --filter status=5xx | jq"* — Streampipe (test 02) — open on a real command, not a marketing claim
- *"Open the trace, find the span, fix the regression. No glossary required."* — Tracejam (test 05) — three concrete verbs, then a refusal
- *"From stdin, through the pipe, into your dashboard."* — names the data path; refuses abstraction
- *"23 spans · 4 services · 482 ms."* — Tracejam mockup — data is the headline
- *"Read anything that emits lines. Files, pipes, sockets, kubectl logs."* — names the inputs, refuses generality
- *"Drop-in OTLP. No agent, no sidecar."* — pairs claim with refusal of common alternatives

### Luxury

Three voice patterns: *heritage with specifics*, *refusal as sophistication*, *named scale*.

- *"The world's most acclaimed creative collective, where 23 partners work independently and collaboratively to shape the future of design."* — pentagram.com — heritage (implied longevity), named scale (23 partners)
- *"By appointment."* — atelier-style — refusal as gatekeeping
- *"A study in the senses."* — Hallmark Atelier — single nominal phrase, comma-free
- *"A page should arrive like a person — composed, deliberate, in good clothes."* — Hallmark Atelier — analogy treats the page as social
- *"With pleasure, you are most welcome."* — Hallmark Editorial salutation — formal address
- *"Restraint, repeated, becomes a signature."* — Hallmark Atelier — three commas, four words, philosophical
- *"A studied hand."* — three words; the determiner does the work
- *"A small, opinionated craftsmanship engine that argues with your AI assistant on your behalf — and wins."* — Hallmark Atelier — names the role precisely, embraces the conflict

### Playful

Three voice patterns: *analogy via pop-culture*, *food/sensory metaphor*, *anticipated reaction*.

- *"Playlists, but for ideas."* — are.na — analogy that's also useful
- *"Internet memory palace."* — are.na — three-word noun phrase, structural metaphor
- *"Devouring details. Nourishing novelty. Deploying excellence."* — rauno.me — alliteration; food + tech metaphor
- *"The kind that make you say, 'Wait, how did you do that?'"* — jhey.dev — direct address, anticipates the reader's reaction
- *"Built to ship."* — Hallmark Sport — three words, declarative, with a verb that's a verb
- *"Ready? You are two minutes from shipping."* — Hallmark Sport — a question, then a number
- *"design like print: warm, off-register, intentional."* — Hallmark Riso — lowercase + colon + three modifiers
- *"this is not a page that pretends to be paper. it is a page that remembers paper."* — Riso — refuses the imitation framing

### Austere

Three voice patterns: *extreme abbreviation*, *principle as opening*, *refusal of marketing language*.

- *"Hello."* — Hallmark Coral salutation — one word; the period is the design
- *"This is a page that doesn't try."* — Coral — declares the position openly
- *"Things Become Other Things."* — craigmod.com — three words; treats brand as essay title
- *"Lightness above weightiness, elevate everyone you encounter."* — craigmod.com — principle-first positioning
- *"A quiet skill."* — Hallmark Coral — three words; the article is doing work
- *"Software can be soft and exact at once. That's the trick."* — Hallmark Hum — names the contradiction, names the resolution
- *"One HTML file."* — Anya (test 06) footer — three words; the count is the boast
- *"This page doesn't move."* — names the design decision openly

---

## Four moves that make a line memorable

Removing tells leaves clean, dead copy. These are the moves that put a person back in,
from SlopMonster's § After the tells are gone
(`upstream/slopmonster/references/signs-of-ai-writing.md`) and § 3 and § 5 of its
principles. They are craft moves, not gates: each one is a decision a writer makes, and one
per page is usually the whole difference.

- **Say one thing a model would not risk.** *"An opinion, a preference, a thing that failed.
  Safety is the texture of AI writing."* A page that never states a preference has no
  author. "We do not do overlays. If the roof needs replacing, it gets stripped" is a
  sentence with a cost attached, which is why it reads as true.
- **Refusal as positioning.** *"A refusal positions better than a promise — anyone can
  promise quality, almost nobody publishes the work they turn down."* This is the move the
  [`reference-lock.md`](reference-lock.md) instruction *"borrow the move, never the
  sentence"* points at without naming: the Brutalist and Austere samples above are almost
  all refusals. Name what this business will not do, in its own words.
- **Teach something on the way past.** *"A page that explains how the thing works earns
  trust that a page of claims cannot buy, and it arms the reader to spot a bad competitor —
  a favour they remember."* One mechanism, explained plainly, somewhere in the middle of the
  page. "A roof is seven layers. Most quotes only price two."
- **Keep one rough edge.** A contraction, a fragment, a sentence starting with "And".
  *"One rough edge is texture. Five is sloppy."* Deliberate, and counted.

The mechanical companion to these — strip the adjectives, find the number, name the noun,
cut the throat-clearing, read it aloud, verify and mark on the page — is a pass in
[`copy-gate.md`](copy-gate.md), run after the skills and before the linter. These four are
what that pass leaves room for.

## Banned opening lines (anti-patterns)

These phrases appear across distribution-default LLM copy and reach for none of the specificity above. **Banned outright** — if you find yourself reaching for one, replace it with one of the patterns from the tone above.

| Phrase | Why it fails |
| --- | --- |
| *"Built for the modern team"* | Vague; assumes no specifics; temporal marketing |
| *"Unleash your [X]"* | Hyperbolic; software can't unleash anything |
| *"Where X meets Y"* | False synthesis; creative laziness |
| *"Empower your..."* | Missionary language; avoids concrete benefit |
| *"Reimagine the way you..."* | Suggests dissatisfaction before explaining need |
| *"Supercharge your workflow"* | Energy metaphor without mechanics |
| *"Innovative solutions"* | Meaningless; every product claims innovation |
| *"Seamless integration"* | "Seamless" has no antonym; signals non-specificity |
| *"In today's digital landscape"* | Temporal hand-wave; assumes the reader needs orientation |
| *"Next-generation"* | Implies predecessor inadequacy; offers no differentiation |

If the brief gives you nothing to work with for an opening line, *say so to the user* and ask one question that elicits a specific noun, verb, or place. The user knows their product; the model is not allowed to invent specificity.
