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

## Research loop

Three to five angles, not one query:

1. **Broad aesthetic** — the mood in plain language ("warm coastal Nordic hospitality").
2. **Domain / category** — what this business actually is.
3. **Known brand** — a specific strong player in the segment, named.
4. **Register** — the row from `SKILL.md`'s register table this brief lands in.
5. **Anti-reference** — one thing this build should *not* look like, sharpening the
   boundary the same way a rejected direction does in the lock block below.

Then: **capture 3–4 full references as images and read them**, long pages in
viewport-sized slices. Memory returns wrong facts — two market-leading pages
turned out to *centre* their heroes, and one coloured words inside the headline
instead of switching typeface, opposite of what was assumed before the images
were opened.

From the 3–4 captured, pick **one primary** and take **1–2 borrowed details** from
the rest. Nothing else survives into the lock.

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

**A major visual choice with no row here is not shipped.** Not "shipped and
justified after" — the row exists before the choice does.

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
