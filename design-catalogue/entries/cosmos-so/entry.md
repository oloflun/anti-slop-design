---
title: "Cosmos - your space for inspiration"
url: https://www.cosmos.so/
source_url: https://www.cosmos.so/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "editorial"
family: scattered-cards-to-masonry
dna: "Visual bookmarking app x warm white, collected images scattering as small tilted cards around the headline, then a dense masonry of the users' saves"
register: modern clean
grammar: gallery/catalog
lane: "An inspiration-saving app: 'Your space for inspiration' centred on warm white, small tilted image cards bursting outward from behind the headline, a grey skeleton grid loading into collections and a masonry of saved images (posters, sculpture, photography, type specimens), then the masonry blurring behind a pill 'Sign up for Cosmos' and a huge 'COSMOS' wordmark at the foot."
mode: persuade
traits: ["image cards scattering from behind the headline", "masonry of real saves", "blur behind the closing call to action", "huge wordmark footer"]
palette: ["#FFFFFF", "#61413C", "#B6ABA1", "#E6E3E0"]
type: ["cosmosOracle"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The product's content is the hero image: the scattered saves become the masonry, so the page shows what using it looks like.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Unseen Studio®).

## What to borrow (principle)

- Burst the product's own content out of the headline and settle it into the grid

## What to leave

- Skeleton loading frame

## Signature move

Tilted image cards scattering outward behind 'Your space for inspiration'.

## Motion

Intro: headline holds (~1 s), cards burst outward. Wheel: cards settle into the grid; masonry columns parallax at different speeds; the grid blurs as the call to action rises.

Measured (`motion/probe.json`): 1 video; entry gate: Explore. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: an inspiration-saving app: 'Your space for inspiration' centred on warm white, small tilted image cards bursting outward from behind the headline, a grey skeleton grid loading into collections and a masonry of saved images (posters, sculpture, photography, type specimens), then the masonry blurring behind a pill 'Sign up for Cosmos' and a huge 'COSMOS' wordmark at the foot. Type: cosmosOracle.
Ground and ink from the measured palette (#FFFFFF, #61413C, #B6ABA1). Motion carries the page through
tilted image cards scattering outward behind 'Your space for inspiration'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — user-saved imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: user-saved imagery

## Reference lock

Primary reference/direction: Cosmos - your space for inspiration — An inspiration-saving app: 'Your space for inspiration' centred on warm white, small tilted image cards bursting outward from behind the headline, a grey skeleton grid loading into collections and a masonry of saved images (posters, sculpture, photography, type specimens), then the masonry blurring behind a pill 'Sign up for Cosmos' and a huge 'COSMOS' wordmark at the foot.
Preserve (3-5 traits): image cards scattering from behind the headline; masonry of real saves; blur behind the closing call to action; huge wordmark footer.
Borrow only (1-2): Burst the product's own content out of the headline and settle it into the grid
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: user-saved imagery
Reject: Skeleton loading frame
Token commitments: palette #FFFFFF, #61413C, #B6ABA1, #E6E3E0; type cosmosOracle; engine GSAP + Lenis linked (never vendored).
