---
title: "Operator (AI Agent Agency template)"
url: https://oma-operator.framer.website/
source_url: https://oma-operator.framer.website/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/0c9b6b882155bce2-screenshot.webp
category: product-focused
category2: ""
family: dark-agent-console
dna: "SaaS dashboard demo x AI-agency pitch deck"
register: cinematic dark
grammar: live surface
lane: "A misty dark photograph carries the pitch, a glassy dashboard card floats mid-hero as proof, then a bento grid of stats and client quotes closes the case"
mode: persuade
traits: ["dark misty photo ground", "hexagon agent mark", "floating glassmorphic dashboard card", "garbled marquee logo strip", "bento stat/quote grid", "white pill CTAs on dark", "mint micro-accent tag", "placeholder testimonial names"]
palette: ["#0D0F12", "#181B20", "#6E7986", "#F5F4F0", "#9FEFC4"]
type: ["Uncut Sans"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The page sells an invisible product — software agents — by giving them a visible
home. A dark, fogged mountain photograph sits behind everything as atmosphere, and
a single glassy dashboard card (agent list, draft/paused/active counts, a "deploy
agent" button) floats over it mid-hero. The card is doing the actual persuading:
it is the only concrete thing on the page, so the eye lands there before it lands
on the headline.

Everything below the fold is proof, stacked in two densities. A logo marquee runs
first, deliberately distorted (letters skewed, mirrored, overlapping) so it reads
as motion before it reads as names — trust-signal texture rather than trust-signal
content. Underneath, a bento grid mixes hard numbers (`180+ agents deployed`,
`94% average retention`) with quote tiles at the same visual weight, so a stat and
a testimonial are interchangeable units of the same argument.

The dark register does real work: on a near-black ground, the one warm/light
surface (the dashboard card, and later the white bento tiles) reads as the
"place where the product lives," separate from the marketing chrome around it.
That separation is the whole trick of demoing software you can't actually let
someone click.

## What to borrow (principle)

- **Float one real screen over the hero photograph.** A single UI card, partially
  glass, does more convincing than three paragraphs of feature copy.
- **Make the logo strip texture, not proof.** If the "trusted by" names aren't real
  clients, distort or animate them so they read as rhythm, not as a claim.
- **Mix stats and quotes in one grid.** Equal-weight tiles let a hard number and a
  soft testimonial back each other up without a separate "results" section.
- **Reserve one accent for state, not decoration.** A single mint tag or status dot
  is enough to mark "this is live" against an otherwise monochrome dark UI.

## What to leave

- Placeholder testimonial names and companies that read as generated rather than
  sourced (a "Sheldon Cooper, Founder, GrowthLane" is a tell, not a proof point).
- The garbled/broken logo marquee taken further than motion — at rest, several
  logos are illegible, which undercuts the "trusted by" claim it's making.
- Generic AI-agency copy ("Scale your operations without scaling your team") that
  could sit on any agent-building business — the page has no product specifics to
  differentiate it from a template.

## Signature move

The floating dashboard card mid-photograph: a real (if fictional) product screen,
partially transparent, overlapping the hero image and headline rather than sitting
in its own section. It turns an abstract "AI agents" pitch into something with a
UI, before a single feature is described.

## Motion

(from designlang extract) The captured stylesheet is thin: Framer's static CSS
shows only a near-instant `1ms` duration token, a discrete-property overflow
transition, and a generic `background, box-shadow` hover transition — no
scroll-triggered keyframes or eased curves are present in the extracted CSS.
The extract still tags the page's feel as "mixed" with scroll-linked motion
present, consistent with Framer's habit of driving reveals (the card float,
the bento-tile entrances) through inline whileInView props rather than CSS
transitions, so the choreography the capture implies is real but invisible to
static extraction. The one literal keyframe found is a generic 360° loading
spinner, unrelated to content motion.

| token | value | role |
|---|---|---|
| `instant` | 1ms | baseline transition duration (Framer default) |

Feel: mixed · Scroll-linked: yes (per extract) · Easings/keyframes beyond the
spinner: none captured.

## Brief

Build a dark, photographic SaaS-agency page for a product that has no single
screen to show off. Ground everything in a near-black, fog-photograph hero; float
one glassy product card over it as the only concrete proof in the fold. Use a
single geometric sans throughout, white text on dark, one small mint accent for
status/tags. Below the fold, run a continuously scrolling logo strip (real or
stylised) followed by a bento grid mixing 2-3 hard metrics with 2-3 short client
quotes at equal visual weight. Close on a repeat of the primary CTA pair (a
demo/audit button plus a secondary "see results" link).

## Image recipe

Atmospheric landscape or skyline of [SUBJECT], shot at dusk or in fog, desaturated
toward blue-grey, heavy vignette toward the edges so a UI card can float over the
centre without competing for contrast, no visible horizon line, wide negative
space top and bottom for headline and nav.

## Photo search

Unsplash first, Pexels second.
- "misty mountains dark blue moody"
- "foggy landscape aerial desaturated"
- "night skyline haze dark"
- "abstract dark gradient atmosphere"

## Reference lock

Primary reference/direction: Operator — dark AI-agency template, floating dashboard card over a fogged photograph, bento proof grid.
Preserve (3-5 traits): near-black photographic ground with heavy fog/vignette; one glassy product-UI card floating mid-hero as the sole concrete proof; bento grid mixing stat tiles and quote tiles at equal weight; single mint micro-accent reserved for status/tags only.
Borrow only (1-2): the continuously scrolling distorted logo marquee; the paired CTA (primary action + secondary "see results" link).
Role rules: no more than one floating UI card per fold; stat and quote tiles never exceed two tones of emphasis; accent colour never used for body text, only tags/status.
Media strategy: photo:unsplash — atmospheric, low-detail, dark landscape or cityscape only; never a literal "team in an office" stock shot.
Reject: fabricated testimonial names presented as real; logo marquees distorted past legibility even at rest; stacking more than one floating UI card in the same viewport.
Token commitments: bg `#0D0F12`, surface `#181B20`, muted `#6E7986`, paper `#F5F4F0`, accent-mint `#9FEFC4`; display/body a single geometric sans; card corner-radius large (~20px) with low-opacity fill for the glass effect.
