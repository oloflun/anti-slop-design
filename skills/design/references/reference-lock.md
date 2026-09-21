# Reference lock

**Load in Step 1b, for every tier.** Refero's research-first method, adapted to this
skill's four-tier gate (`SKILL.md` Step 2): Tier 0 locked · Tier 1 derive · Tier 2
reference · Tier 3 invent. The lock is not a Tier-2-only artifact — every tier states
one before Step 2 runs, because every tier is a claim about where the direction comes
from, and an unstated claim is how Tier 1 gets skipped in favour of invention.

| | |
|---|---|
| **Reads** | The brief, Step 1 pre-flight findings, Step 2 tier evidence (`DESIGN.md`, brand assets, user URL/screenshot, or nothing), the design catalog, 21st.dev for tech/SaaS shots, Refero MCP when configured. |
| **Does** | Runs the research loop below, captures references as read images (never from memory), fills the reference-lock block and decision ledger, checks the build against anti-averaging and token/media-role preservation. |
| **Writes** | Nothing persisted by default — the lock is stated in-session, out loud, before Step 2 and Step 4. When the system is being locked to a portable file, its fields feed [`design-md.md`](design-md.md). |
| **Human checks** | Whether the named primary reference is actually the dominant voice in the build, not a label pasted over an averaged result — the one judgment this file cannot automate. |

---

## What changes per tier

The loop is identical; only what plays the role of "the reference" changes.

- **Tier 0 — locked.** Reconstructed, not invented: read `DESIGN.md` and what's
  already built from it, and write down what "preserve" means. Primary = the
  locked system itself.
- **Tier 1 — derive.** Primary = the brand evidence (logo, wordmark, hex, deployed
  site, `tailwind.config` colours). Borrowed details may come from competitor or
  category references; they extend the language, never re-set it.
- **Tier 2 — reference.** Primary = the user-supplied URL or screenshot. Refero's
  native case; the fields map straight across.
- **Tier 3 — invent.** Primary = the invented world's own bible
  ([`invention.md`](invention.md)) — locking against it stops the second component
  from drifting into a different invented world than the first.

At every tier, a major visual choice with no source in the lock is not shipped.

---

## A brief is not a build target

Refero states the rule this file exists to enforce, in one sentence: *"**A brief is not a
build target.** Before implementation, lock either a user-provided visual source, an
existing product/design-system target, a selected generated mockup, or an explicit
reference-locked direction approved for direct build."*

This is the sentence that closes the skip route. When the direction feels obvious and the
signature act is being built straight from the brief, the visual target still gets named
first — one line saying what this is being built *toward* and what must not drift:

```text
Build target: [existing UI / user screenshot / URL capture / selected mockup / approved reference lock]
What must not drift: [canvas, typography, accent roles, layout, media, density]
```

If no target exists and the visual direction is material, explore options or get one
reference-locked direction approved. A build whose only stated source is the brief is a
build with no source at all.

## Research loop

Six angles, not one query:

1. **Broad aesthetic** — the mood in plain language ("warm coastal Nordic hospitality").
2. **Domain / category** — what this business actually is.
3. **Known brand** — a specific strong player in the segment, named.
4. **Register** — the row from `SKILL.md`'s register table this brief lands in.
5. **Anti-reference** — one thing this build should *not* look like, sharpening the
   boundary the same way a rejected direction does in the lock block below.
6. **Cross-domain wildcard** — one reference from *outside* the category, chosen for a
   quality rather than a subject. *"A banking app can be inspired by a meditation app's
   calm."* Upstream's map:

   | This brief's domain | Look at |
   |---|---|
   | Healthcare | Meditation apps (calm), fitness apps (motivation), journaling (reflection) |
   | Finance | Productivity tools (clarity), weather apps (data viz), news apps (hierarchy) |
   | Education | Games (engagement), music apps (progression), social apps (community) |
   | E-commerce | Editorial sites (storytelling), gallery apps (browsing), travel (discovery) |
   | Enterprise | Consumer apps (polish), design tools (power + clarity), docs (wayfinding) |

   *"Don't force connections — but don't limit yourself to competitors either."* Competitors
   solve the same problem the same way, which is precisely how a category default becomes
   invisible. `select.py --wildcard` is the catalogue-side version of this angle.

**Quality over quantity: *"5 excellent references beat 20 mediocre ones."*** A wall of
screenshots is not research; it is deferred judgment. Curate down before capturing.

Then: **capture 3–4 full references as images and read them**, long pages in
viewport-sized slices. Memory returns wrong facts — two market-leading pages
turned out to *centre* their heroes, and one coloured words inside the headline
instead of switching typeface, opposite of what was assumed before the images
were opened.

**Every captured reference carries two lines, not one:**

```text
What to take: [the specific element or quality to learn from]
What to leave: [what does not apply here]
```

*"This prevents wholesale copying."* A reference with no lesson is decoration, and a
reference with only a "take" line is the one that quietly becomes the whole build. The
"leave" line is also what makes the primary/borrowed split below enforceable rather than
declarative.

**Extract more than colour and type.** From each reference, read out: layout system,
section rhythm and composition · card, button and surface treatments · borders, shadows,
radius · elevation and depth rules · imagery, graphic and illustration treatment · media
asset strategy (real asset, generated, code-native primitive, product screenshot, or
placeholder) · do and don't rules · **one memorable visual move to adapt**. A lock that
carries a palette and a typeface and nothing structural is why a build "referenced" a page
it looks nothing like.

**Give each source a bounded job.** *"Primary style: overall mood, density, and structure.
Secondary styles: specific borrowed details. User context: adapt everything to the product,
audience, and task."* A source with no job is a source that gets averaged.

From the 3–4 captured, pick **one primary** and take **1–2 borrowed details** from
the rest. Nothing else survives into the lock.

**Flag accessibility failures in the references themselves.** *"A beautiful reference with
2:1 contrast ratios is not inspiration — it's a cautionary tale."* Name it when you capture
it, so the trait does not travel into the lock as craft.

### Sources, in order

1. **The design catalog** — `~/anti-slop-design/design-catalogue/`,
   `python scripts/query.py --family … --register … --grammar …`. Query by the
   register named in `SKILL.md`'s table, not by vibe.
2. **User-supplied URL or screenshot** — Tier 2's native input; also valid at any
   tier as a borrowed-detail source.
3. **21st.dev** for tech/SaaS product shots — browse, screenshot, study the
   treatment; borrow the principle and rebuild it in the locked tokens, never paste
   a component with its own palette into a Tier 0–2 build.
4. **Refero MCP**, if configured — `refero_search_styles` → `refero_get_style`.
   Optional. State plainly when it is not configured rather than silently skipping
   it; do not treat its absence as license to skip the research loop itself.

### When the results are weak

Sparse or generic results are a query problem before they are a source problem. Climb this
ladder before concluding the catalogue has nothing (Refero `mcp-tools.md` § If Results Are
Weak):

1. **Broaden the query.**
2. **Remove extra adjectives or constraints.** Two adjectives and a register is usually one
   adjective too many.
3. **Search adjacent categories.**
4. **Try a known-product or best-brand query.** Name a specific strong player instead of
   describing a type.
5. **Inspect later pages.** The first page of any index is the most averaged part of it.

Only after all five is "no usable reference in this register" a finding — and then it is
stated in the lock, not silently converted into invention.

### Transcribe the category's live headlines

Before writing a word of copy, read the **five best live pages in the category and quote
their headlines verbatim** into the lock. *"The bar is what the reader has already seen, not
what sounds nice in isolation"* (`upstream/slopmonster/references/sources.md`). Five lines,
copied exactly, with the source named. They belong here rather than in
[`copy-gate.md`](copy-gate.md) because they are a *reference* capture: the same discipline
as the four screenshots, applied to language, and read before the copy pass rather than
during it.

## The reference-lock block

Verbatim fields, filled before any code:

```text
Primary reference/direction: [one dominant source, named]
Preserve: [3-5 traits that must survive: canvas, type, accent, layout, density, media]
Borrow only: [1-2 specific secondary details]
Role rules: [source token/component meanings to preserve — CTA-only, code-only, decorative-only]
Media strategy: [photo:unsplash | photo:pexels | product surface | drawn system | generated | placeholder]
Reject: [defaults/averages that would collapse the direction]
Token commitments: [canvas, type, accent, radius, border/shadow, imagery — each with its role]
```

**Media strategy is an enum, not prose.** Pick exactly one value per media slot so
drift is visible at a glance: a hero declared `photo:unsplash` that quietly becomes
a CSS gradient is a caught regression; a hero declared "some kind of photo" is not.

## Decision ledger

Every entry in the lock traces back through this table:

| Decision | Source | Source rule/role | Why |
|---|---|---|---|
| [palette / type / layout / media choice] | [reference / catalog query / brand asset / craft rule] | [token or component role to preserve] | [reason specific to this brief] |
| **Memorable detail** | [the reference the move was adapted from] | [what the move does on this page] | [why *this* brief earns it] |

**A major visual choice with no row here is not shipped.** Not "shipped and
justified after" — the row exists before the choice does.

**The `Memorable detail` row is mandatory, and the rule applies to it too.** Refero's
requirement is unambiguous: *"Create at least one memorable detail: a visual move,
interaction, layout choice, or copy detail users would remember."* No row, not shipped —
including for the signature act itself, which is the row most often left blank on the
grounds that it is obvious. An example of a filled row from upstream's own worked case:
*"Memorable detail | 'Operational value' strip showing saved hours/cost by plan | Brief +
analytics product context | Metric strip as evidence, not decoration | Makes pricing feel
tied to outcome."*

## The asset lock

Written **before** anyone starts searching or generating — Step 5b has a pipeline but no
spec upstream of it, and an asset sourced without a spec is an asset chosen by whatever the
search returned. One block per media slot:

```text
Asset role: [hero image / texture / illustration / thumbnail / cutout]
Slot: [dimensions / aspect ratio / location on the page]
Art direction: [source, palette, subject, rendering, crop, density]
Avoid: [wrong palette, extra text, brand drift, generic placeholders]
```

The `Avoid` line is the one that earns its keep: it is the reject field applied to a single
asset, and it is what a QA pass compares the delivered frame against.
*"Generated assets must be placed into the implementation before handoff or documented as
blocked"* — never quietly downgraded to a gradient. That downgrade is the media-role drift
this file's next section already bans, caught one step earlier.

---

## Anti-averaging

Choose a dominant direction. Secondary references contribute narrow, named details;
they do not get to soften the primary one. The failure mode is specific: a dark
workbench reference, an acid-yellow document site, and a serif editorial page do not
average into a warm cream canvas with muted clay accents — **dark + acid + serif is
not cream + orange + polite serif.** Dark → cream, saturated → muted clay, sharp →
rounded, distinctive layout → generic hero-and-sections: each swap is the
intersection eating the direction, not synthesis.

Run these against the lock before shipping — ported from `anti-ai-slop.md`:

- **Identity test.** If the first viewport could belong to any other company,
  branding lost to averaging. Add the one detail that makes this unmistakably *this*
  brand's build.
- **Editorial test.** If swapping the logo for a coffee shop, boutique hotel, or
  literary magazine still makes the hero feel plausible, the build has drifted into
  generic calm-editorial slop regardless of what the lock says on paper.
- **Screenshot test.** Would this pass next to real products in the named
  register, or does it read as the safe middle every other page also landed on?

A lock that names a dominant primary and still fails these three was averaged during
implementation, not during research — check the built page against the lock's
"Reject" line specifically.

## Token-role and media-role preservation

**Token-role preservation.** A source's role for a colour, radius, shadow, or
component is part of the token, not separable from it. A CTA-only accent used as a
section background, a code-only syntax colour promoted to UI chrome, or a decorative
gradient turned into a core surface are all role drift. Preserve the role or drop
the token — never repurpose it to make a layout "work."

**Media-role preservation.** An image-led reference never collapses to text-only
because the image was hard to produce. If the real asset genuinely is not
available, the placeholder must be honest, not silent:

```text
Placeholder — [slot name]
Aspect: [ratio, e.g. 16:9 desktop / 4:3 mobile]
Art direction: [subject, lighting, crop the real asset will match]
Alt: [describes the intended real subject, not "placeholder image"]
```

A placeholder with no aspect ratio, no art direction, and generic alt text is the
same failure as no image at all — it just fails one render cycle later.

---

## Three persona sketches

`SKILL.md` Step 5 pass 12 and [`verbs/review.md`](verbs/review.md) § 4 both resolve ties
with "named personas". Nothing in the chain created any, so the tie-break pointed at an
artifact that did not exist. It does now, and it is three lines in `BRIEF.md` — not the
per-project persona documents upstream files away, which is a research deliverable this
chain has no room for.

Select and write **three**, following upstream's proportions (*"2–3 primary users, 1–2 edge
case users, 1 stress case user"*), compressed to one line each:

```text
Primary: [who they are] · [device and connection] · [what they came to do]
Edge:    [who sits at the margin] · [the ability or context that puts them there] · [what breaks first]
Stress:  [the same job under a named difficult circumstance] · [what they cannot afford to lose]
```

**The conditions are situational, not only permanent.** Upstream's spectrum is explicit that
*"bright sunlight, noisy environment, one hand occupied, driving, multitasking, emotional
distress, unfamiliar language, slow connection"* belong beside vision, hearing, motor and
cognitive conditions. A stress persona on a Swedish harbour-restaurant page is a person on a
phone, outdoors, in sun, deciding where to eat in the next ten minutes — and that persona
decides more layout questions than any abstract one.

**Write the intersections down.** *"A sighted user in bright sunlight has similar needs to a
low-vision user. A stressed parent holding a baby has similar motor constraints to someone
with limited hand mobility. A non-native speaker has similar needs to someone with a
cognitive processing difference."* Each intersection is a universal-design opportunity: one
fix that pays twice.

**Then ask the one question that makes the set honest:** *"Which persona makes you most
uncomfortable?"* — *"that one probably needs the most attention."* Ask it of the brief, and
of the user when there is a user to ask. Discomfort is the signal that a persona was
included for completeness and is about to be designed around rather than for.

Sketches that read as cardboard cutouts have failed. The check is upstream's own: *"do these
feel like real people, or cardboard cutouts?"*

## Feeding Step 2 and Step 5

**Into Step 2.** At **Tier 2**, the lock *is* the direction — its primary reference
sets the token commitments directly. At **Tiers 0–1**, the lock is the **quality
bar** the locked or derived system has to clear: the locked tokens still win on
value, but the captured references are what "as good as" means, concretely.

**Into Step 5 visual QA.** Carry the lock's fields straight into the QA pass:

```text
Source truth: [the reference lock, or the DESIGN.md it fed]
Implementation evidence: [local screenshot, deployed URL screenshot, captured app state]
Viewport/state: [desktop/mobile, route, theme, interaction state]
```

Classify findings P0–P3 (broken/unreadable · major drift from the lock · moderate
mismatch or missing state · post-handoff polish). **No handoff with an open P0, P1,
or P2.** A P3 may ship with the finding named; P0–P2 block.

## Worked example — Skärgårdskrogen (Swedish harbour restaurant, warm photographic)

A harbourside restaurant on the Bohuslän coast. Register: **warm photographic**
(`SKILL.md` register table — harbour restaurant, guesthouse, tourism, family
business), with `klova/` as this skill's own in-repo worked example for the
register (`house-physics.md`).

**Research loop:**

1. Broad aesthetic — "warm coastal Nordic hospitality."
2. Domain/category — harbourside seafood dining, Bohuslän archipelago.
3. Known brand — a west-coast Swedish harbour restaurant with a photograph-led site.
4. Register — warm photographic, per the table above; cross-check against `klova/`.
5. Anti-reference — the editorial-print register (`calyx.html`): its apparatus on a
   family harbour restaurant reads as pretension, not craft.

Four captured and read: `klova/` itself, two competitor harbour-restaurant sites,
and `calyx.html` as the anti-reference boundary check.

**Reference-lock block:**

```text
Primary reference/direction: klova/ — centred logo lockup over full-bleed harbour photography, no rail, no kicker, no edition marker.
Preserve: centred logo lockup with no rail; full-bleed hero photograph with generous framing air on secondary images; one real outlined button sized to be pressed; warm serif display at conversational (not oversized-drop-cap) scale; dark-navy footer as the page's one tonal inversion.
Borrow only: dotted carousel indicator for the food gallery (competitor B — klova/ has no gallery, so this is a genuinely new need, not a style import); 12px rounded image corners (competitor B).
Role rules: the outlined button is CTA-only, never a secondary link style; the navy footer tone is inversion-only, never a section background elsewhere on the page.
Media strategy: photo:unsplash, sourced and vendored per photo-sources.md until real restaurant photography is supplied; hero 16:9 desktop / 4:3 mobile, framed with 24-48px air — never full-bleed-with-type-over, the editorial-print move this build explicitly rejects.
Reject: kicker microformat, grain film, ledger pricing, edition markers, italic serif drop caps — all editorial-print apparatus a family harbour restaurant cannot plausibly publish.
Token commitments: warm ivory canvas; near-black ink; one terracotta accent used only on the button and one wordmark word (never as fill); slate captions with a separate, measured value for the dark footer ground.
```

**Decision ledger:**

| Decision | Source | Source rule/role | Why |
|---|---|---|---|
| Warm photographic, not editorial print | `SKILL.md` register table + anti-reference read of `calyx.html` | register selects apparatus | Family-run harbour restaurant, not a publishing entity |
| Centred logo lockup, no rail | `klova/` (primary) | layout role: identity-first hero | The photograph is the primary hire, not editorial structure |
| Real outlined button | `klova/` (primary) | CTA-only | Warm-photographic register expects a pressable button, unlike print/cinematic typeset links |
| Dotted carousel for gallery | Competitor B (borrowed) | gallery navigation only | `klova/` had no gallery; licensed as one named borrowed detail, not a wholesale style import |
| One terracotta accent, display-scale only | `house-physics.md` structural rule | accent role: CTA + display, never fill | Prevents the accent diluting into a second colour system |

A rejected direction here would average `klova/`'s warm photographic register with
`calyx.html`'s editorial apparatus into a soft-cream page with a restrained kicker
and a half-outlined button that is neither a typeset link nor a real one — the
dark+acid+serif-vs-cream+orange+polite-serif failure, in miniature.

## Two additions from the 2026-09-03 A/B run (AB05)

- **A colour-swapped word in a headline is a gate-89 signal even without a serif.** "Se *exakt* vad som ändrades" with *exakt* in the accent is the same reflex as the italic word swap; use it only when a locked reference does it and the word carries the claim.
- **Token commitments name the anatomy of every priced or listed surface.** Write `pricing: ledger (hairline rows, display numerals)` or `features: label-rail`, so the lock carries house physics into Step 4 instead of falling back to bordered cards.
