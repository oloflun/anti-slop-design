---
title: "Orix-Studio (creative agency template)"
url: https://orixstudio.framer.website/
source_url: https://orixstudio.framer.website/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/a8af586a53d30f63-screenshot.webp
category: portfolio
category2: ""
family: silhouette-runway-agency
dna: "Fashion-runway silhouette photography x agency service list"
register: cinematic dark
grammar: split stage
lane: "A misty silhouette photograph of walking figures carries a left-aligned service list and a giant circular-registered wordmark, then drops hard to a plain white stats-and-work section"
mode: persuade
traits: ["misty silhouette photography", "left-aligned arrowed service list", "giant wordmark with registered-trademark mark", "dark-to-white hard section break", "plain stat trio", "small work thumbnail grid", "generic agency copy"]
palette: ["#2E3A3E", "#C9754A", "#FFFFFF", "#171A1B", "#E8C9C4"]
type: ["Inter Display", "Instrument Sans"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The hero photograph is a row of silhouetted figures walking through fog or
mist, lit by a warm rim light along the horizon — closer to a fashion-runway
or editorial-film still than a typical agency stock photo. It sets a cinematic,
faintly mysterious tone before a single word of copy is read, which is a
stronger opening move than the generic "team high-fiving" imagery most agency
templates default to.

Service labels (`WEBSITE DESIGN`, `WEB DEVELOPMENT`, `BRANDING`, `MARKETING
DESIGN`) run down the left edge with small arrows, functioning as both
navigation-flavoured decoration and an implicit capability list, while the
studio's wordmark sits giant at the bottom of the photograph with a circled ®
mark for extra weight. It's a lot of visual authority claimed before any actual
work is shown.

The page then breaks hard from cinematic dark to plain white for the "About
Us" and "Work" sections — three bare stats (`120+ Projects Delivered`, `98%
Client Satisfaction Rate`, `15+ Industries Served`) and a small thumbnail grid
of mockup-style work. The contrast is deliberate structurally (mood, then
proof) but the two halves don't share any visual language — no colour, texture
or type-weight carries over — so the page reads as two different sites stapled
together.

## What to preserve

- **Open on cinematic, editorial-style photography** rather than generic office
  or team stock imagery, even for a conventional service business.
- **Run a short service list down one edge of the hero** as implicit
  navigation/capability signage, arrows included, without needing a full nav
  bar.
- **Claim visual authority with scale** — a giant wordmark, a registered-mark
  symbol — before the portfolio has to prove it.

## What to leave

- The hard, uncarried-over break from dark cinematic hero to plain white body
  makes the page feel like two templates spliced together — at minimum, one
  typographic or colour thread should survive the transition.
- Three bare stat numbers with no visual anchor (no thumbnail, no chart) read as
  unverifiable filler, especially directly after a hero this visually
  confident.
- The work-grid thumbnails (a poster mockup, a business-card mockup) are
  generic placeholder-style renders rather than real client work, undercutting
  the sophistication the hero promised.

## Signature move

The mist-lit silhouette walk: a row of backlit figures mid-stride, photographed
through fog with warm rim light along the horizon, used as the entire hero
image with no other visual element competing for attention except the
overlaid wordmark.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed,
but the captured CSS is minimal — no duration tokens, no easing families, and
the only keyframe present is a generic loading spinner; the visible rules are
just a bare `transition: all` and a `background, box-shadow` hover state.
That thinness is consistent with the dark-to-white hard cut this entry
already flags: whatever drives the section break and the service-list
hover/underline states is most likely inline whileInView motion the static
extract can't see, not a captured CSS transition.

## Brief

If borrowing this direction, close the gap between hero and body rather than
letting them read as two separate pages. Open on cinematic, fog-lit silhouette
or editorial photography with a left-edge service list and a giant wordmark
overlaid. Carry at least one colour or type choice from the hero into the body
(the warm rim-light tone, or the condensed display face) so the transition from
dark to light reads as one system. Anchor every stat with a real project
thumbnail rather than a bare number, and replace mockup-style work images with
actual client output before shipping.

## Image recipe

Silhouetted figures walking through [SUBJECT] — mist or fog, backlit by a warm
low sun or rim light along the horizon, wide shot with generous negative space
above for headline/nav, desaturated except for the warm rim-light glow.

## Photo search

Unsplash first, Pexels second.
- "silhouette figures walking fog backlit"
- "people walking mist warm light editorial"
- "runway silhouette rim light dramatic"

## Reference lock

Primary reference/direction: Orix-Studio — cinematic fog-silhouette hero with a left-edge service list, breaking hard to a plain white proof section.
Preserve (3-5 traits): cinematic, backlit silhouette photography for the hero rather than generic office stock; left-edge service list with arrow marks as implicit capability signage; giant wordmark with a registered-mark symbol overlaid on the hero photograph.
Borrow only (1-2): the three-stat trio format; the small work-thumbnail grid layout.
Role rules: at least one visual element (colour, type weight, or motif) must carry from the dark hero into the white body section; every stat must be paired with a real, specific piece of evidence, never left bare.
Media strategy: photo:unsplash — cinematic, backlit, editorial-style photography only for the hero; real client work (not mockup placeholders) for the portfolio grid.
Reject: an unbridged hard cut from dark hero to unrelated white body; bare stat numbers with no supporting evidence; generic mockup renders standing in for real client work.
Token commitments: dark-teal `#2E3A3E`, rim-orange `#C9754A`, white `#FFFFFF`, near-black `#171A1B`, work-tile-peach `#E8C9C4`; bold condensed sans for the wordmark, plain sans for body and stats.
