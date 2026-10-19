---
title: "Telescope - Recommendations by real people"
url: https://telescope.fyi/
source_url: https://telescope.fyi/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "editorial"
family: curator-platform-image-scatter
dna: "Recommendation platform x scattered images converging into words and a portrait"
register: modern clean
grammar: chaptered editorial
lane: "A recommendation app: 'Real recommendations by real people' with small images scattered around, a portrait sliding into the gap between 'by real' and 'people' and expanding to full screen ('Featuring curators from around the world'), a statement with outlined words, product cards, a lime wedge with 'your taste' letters, 'Zoom in with Telescope', full-bleed collections with category words, and 'No algorithms. No ads. No overwhelm.' with images converging into a stack."
mode: persuade
traits: ["image inside the headline gap", "portrait expanding to full screen", "outlined key words", "lime wedge shape", "category words over full-bleed images", "images converging into a stack"]
palette: ["#F5F3EF", "#615247", "#ADA395", "#40372F", "#74685B", "#D5D7D0"]
type: ["Beausite", "CM Geom", "DM Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Images literally gathering into the words make the product (curation) visible; the portrait in the headline gap gives it a human face.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Adrien Vanderpotte, KOKI-KIKO, Louis Paquet).

## What to borrow (principle)

- Put an image in the gap of the headline and expand it
- Gather scattered images into one stack at the end

## What to leave

- Some frames feel busy

## Signature move

A portrait in the gap between 'by real' and 'people' expanding to full screen.

## Motion

Intro: images drift into a scatter around the headline (~2 s). Wheel (Lenis ~85-135 px glide): images converge; a portrait slides into the gap and grows full screen; the statement fills; products slide; the lime wedge sweeps; letters scatter; collections cross-fade under category words; images converge into a stack.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; smoothed scroll (median 144 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a recommendation app: 'Real recommendations by real people' with small images scattered around, a portrait sliding into the gap between 'by real' and 'people' and expanding to full screen ('Featuring curators from around the world'), a statement with outlined words, product cards, a lime wedge with 'your taste' letters, 'Zoom in with Telescope', full-bleed collections with category words, and 'No algorithms. No ads. No overwhelm.' with images converging into a stack. Type: Beausite, CM Geom, DM Mono.
Ground and ink from the measured palette (#F5F3EF, #615247, #ADA395). Motion carries the page through
a portrait in the gap between 'by real' and 'people' expanding to full screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lifestyle and product photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lifestyle and product photography

## Reference lock

Primary reference/direction: Telescope - Recommendations by real people — A recommendation app: 'Real recommendations by real people' with small images scattered around, a portrait sliding into the gap between 'by real' and 'people' and expanding to full screen ('Featuring curators from around the world'), a statement with outlined words, product cards, a lime wedge with 'your taste' letters, 'Zoom in with Telescope', full-bleed collections with category words, and 'No algorithms. No ads. No overwhelm.' with images converging into a stack.
Preserve (3-5 traits): image inside the headline gap; portrait expanding to full screen; outlined key words; lime wedge shape; category words over full-bleed images.
Borrow only (1-2): Put an image in the gap of the headline and expand it; Gather scattered images into one stack at the end
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lifestyle and product photography
Reject: Some frames feel busy
Token commitments: palette #F5F3EF, #615247, #ADA395, #40372F, #74685B, #D5D7D0; type Beausite, CM Geom, DM Mono; engine GSAP + Lenis linked (never vendored).
