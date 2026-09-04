---
title: "Vistal"
url: https://vistal.webflow.io
source_url: https://vistal.webflow.io
captured: 2026-09-04
origin: raw-url
raw: raw/55902b07b043d210-vistal-webflow-io.webp
extract: ok
category: portfolio
category2: ""
family: floating-house-wordmark
dna: "Floating glass-house dusk photography x giant outline wordmark poster"
register: modern clean
grammar: typographic poster
lane: "A giant white outline wordmark sits over a dusk photograph of a floating glass house, then the page cuts hard to a flat yellow section of centred black type and a fanned stack of project photo cards"
mode: persuade
traits: ["oversized outline wordmark over photo", "dusk architectural photography", "flat saturated yellow second section", "fanned overlapping photo cards", "black pill CTAs", "copyright mark beside wordmark", "small-caps dot-marked section kicker", "centred black sans headline"]
palette: ["#F1D359", "#F8F8F5", "#616059", "#22221D", "#3F3B35", "#131313"]
type: ["Inter"]
measured: designlang
kind: reference-style
source: claude
status: ready
---

## Why it works

The hero repeats this catalogue's photo-through-wordmark device (see Indoek) but in a
single-colour outline treatment against a moody dusk photograph of a floating glass
architecture piece — the wordmark's open counters let the photograph's warm interior
lighting show through the letterforms rather than masking a separate image inside them.
Supporting copy stays minimal: a two-line statement, one short sentence, and a single
pill CTA, all kept to the lower half of the frame so the architecture photograph and the
wordmark share the visual weight evenly.

The page then cuts, with no gradient or transition, from the dusk photograph straight into
a flat, fully saturated yellow section — one of the hardest colour-field breaks in this
set. Centred black sans type states the value proposition plainly, and a fanned stack of
three overlapping project photo cards (each captioned with a project type) sits beneath
it, the cards' white borders and drop shadows reading as physical printed photographs laid
on a yellow desk rather than a browser grid.

The small circled "©" beside the wordmark, echoed exactly in Studio Ag elsewhere in this
set, again turns a legal mark into a piece of the logotype rather than footer boilerplate
— a small but recognisable convention this catalogue is now seeing across unrelated
templates.

## What to borrow (principle)

- **Let a photograph show through an outline wordmark's counters directly**, rather than
  masking a second cropped image inside them — the letterforms and the photo's own
  lighting merge into one object.
- **Use one hard, saturated colour-field cut as the entire transition between hero and
  next chapter.** No gradient needed if the cut itself is confident.
- **Fan overlapping photo cards with visible borders and shadows** to read as physical
  prints rather than a uniform digital grid — effective for portfolio/gallery previews.
- **Fold a copyright or trademark mark into the wordmark's own scale and weight** instead
  of relegating it to a footer line.

## What to leave

- This entry's images are derived from the archived raw capture, not a fresh render — the
  live site did not complete the capture pipeline within budget (background attempt also
  failed), so treat exact copy and layout as approximate.
- A fully saturated flat yellow field this large, directly following a moody dusk
  photograph, is a high-contrast jump that could read as jarring rather than confident
  depending on the surrounding brand tone — worth testing against the specific palette
  before committing.
- The fanned photo-card stack's drop shadows are heavier than anything else on the page,
  introducing a dimensionality (depth, physical stacking) that the rest of the flat-colour
  system doesn't otherwise use.

## Signature move

The photo-lit outline wordmark: rather than a flat white or black outline logotype, the
letterforms are transparent enough (or positioned precisely enough) that the dusk
photograph's own warm interior lighting reads through them, so the wordmark appears to be
glowing from the same light source as the architecture behind it.

## Motion

Motion feel is smooth and the page is scroll-linked. The duration scale is short — just
three steps, 100ms to 300ms — noticeably tighter than the other extracts in this batch, and
easing draws from only two families: a plain `ease-in-out` ("ease", 5 uses) and a gentle
decelerate curve (`ease-out`, `cubic-bezier(0.25, 0.46, 0.45, 0.94)`, 2 uses) — neither is a
spring or overshoot curve. No keyframe animation is logged as in-use at all; a generic
`spin` (360° rotation) sits in the raw stylesheet, presumably for a loading state, but
nothing is recorded as actually applied to page content. The motion here appears to run
entirely on property transitions (opacity, transform, background-color) rather than
keyframe reveals — consistent with the "smooth" feel rating and the extract's soft,
low-key shadow profile. No stagger pattern is recorded (from designlang extract).

| kind | name/family | value |
|---|---|---|
| duration | `xs` | 100ms |
| duration | `sm` | 200ms |
| duration | `md` | 300ms |
| easing | ease-in-out | `ease` |
| easing | ease-out | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` |

## Brief

Build an architecture-studio or property template opening on a giant outline wordmark
positioned over a moody dusk photograph of a distinctive building, so the photograph's own
lighting reads through the wordmark's open counters. Keep supporting hero copy — a two-
line statement, one sentence, one pill CTA — confined to the lower half of the frame.
Cut hard, with no gradient, into a flat, fully saturated accent-colour section carrying a
centred black sans value-proposition headline. Beneath it, fan two or three overlapping
project photo cards with visible white borders and drop shadows, each captioned with a
short project type and description, so they read as physical prints rather than a grid.
Fold any copyright/trademark mark into the wordmark's own visual scale.

## Image recipe

Moody dusk or blue-hour architectural photograph of [SUBJECT] — a distinctive modern
building (glass, timber, floating or waterside structure) — shot with warm interior
lighting visible through glass against a cool dusk exterior, sharp architectural lines,
some natural surroundings (water, greenery) in frame, composed with open sky or water
space at the top for a large outline wordmark to sit over.

## Photo search

Unsplash first, Pexels second.
- "modern glass house dusk lit interior"
- "floating architecture waterside blue hour"
- "contemporary building warm interior lighting dusk"
- "architectural photography glass timber dusk"

## Reference lock

Primary reference/direction: Vistal — dusk architecture photograph glowing through a
giant outline wordmark, hard cut into a flat yellow section with fanned project cards.
Preserve (3-5 traits): a giant outline wordmark positioned so a dusk photograph's own warm
lighting reads through its open counters; minimal hero copy confined to the lower half of
the frame; a hard, ungraded cut from the photographic hero into a flat saturated accent-
colour section; a fanned stack of overlapping, bordered project photo cards reading as
physical prints; a copyright/trademark mark folded into the wordmark's own scale.
Borrow only (1-2): the small dot-marked section kicker ("• ABOUT VISTAL"); the black pill
CTA style with a circular arrow icon.
Role rules: the wordmark is always photo-lit, never a flat solid colour on the homepage
hero; the colour-field cut between hero and next section is always hard, never a
gradient; photo cards always carry a visible border and shadow, never flush/borderless.
Media strategy: photo:unsplash — moody dusk/blue-hour architectural photography with warm
interior light against a cool exterior; never a bright daylight or interior-only shot.
Reject: a flat, non-photo-lit wordmark treatment; a gradient transition between the hero
and the accent-colour section; a flush, borderless photo grid in place of fanned cards;
relegating the copyright mark to a small footer line.
Token commitments: accent-yellow `#F1D359`, paper `#F8F8F5`, ink `#22221D`, ink-soft
`#3F3B35`, stone `#616059`, warm-tan `#887661`; grotesque sans for wordmark and headlines
throughout; wordmark always set large and photo-lit in the hero, black sans centred for
the yellow section's headline.
