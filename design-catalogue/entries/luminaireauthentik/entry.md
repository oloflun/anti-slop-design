---
title: "Luminaire Authentik - Custom Lighting"
url: https://www.luminaireauthentik.com/
source_url: https://www.luminaireauthentik.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "luxury-craft"
family: lighting-maker-warm-editorial
dna: "Canadian lighting maker x warm interiors and a colour swatch fan"
register: warm photographic
grammar: chaptered editorial
lane: "A lighting manufacturer: a row of lamp photos sliding in on beige, a serif product intro, a two-up of a linear lamp and a terracotta wall, 'Located in the heart of the Eastern Townships', a fan of colour swatch chips under 'Colourful, creative and versatile design', a product grid, a 'Choco & Corten' finish, projects and services."
mode: persuade
traits: ["warm beige and terracotta", "thin serif headings", "colour swatch fan", "lamp product grid", "interior project photos", "promo marquee bar"]
palette: ["#E7E0D3", "#716A61", "#291C15", "#553F33", "#908A81"]
type: ["DM-Sans", "PP-Editorial-New", "Axeptio Source Sans 3"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The swatch fan makes customisation tangible, and the warm palette fits the product.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: LEEROY).

## What to borrow (principle)

- A fan of real colour swatches for a customisable product

## What to leave

- Cookie modal over every frame
- Generic grid

## Signature move

A fan of colour swatch chips under a serif headline.

## Motion

Intro: beige, lamp photos slide in as a row (~1.5 s). Wheel (native): sections fade up; the swatch fan rotates open; product tiles stagger; project images slide.

Measured (`motion/probe.json`): GSAP 3.12.7; 1 video. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a lighting manufacturer: a row of lamp photos sliding in on beige, a serif product intro, a two-up of a linear lamp and a terracotta wall, 'Located in the heart of the Eastern Townships', a fan of colour swatch chips under 'Colourful, creative and versatile design', a product grid, a 'Choco & Corten' finish, projects and services. Type: DM-Sans, PP-Editorial-New, Axeptio Source Sans 3.
Ground and ink from the measured palette (#E7E0D3, #716A61, #291C15). Motion carries the page through
a fan of colour swatch chips under a serif headline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — interior and product photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: interior and product photography

## Reference lock

Primary reference/direction: Luminaire Authentik - Custom Lighting — A lighting manufacturer: a row of lamp photos sliding in on beige, a serif product intro, a two-up of a linear lamp and a terracotta wall, 'Located in the heart of the Eastern Townships', a fan of colour swatch chips under 'Colourful, creative and versatile design', a product grid, a 'Choco & Corten' finish, projects and services.
Preserve (3-5 traits): warm beige and terracotta; thin serif headings; colour swatch fan; lamp product grid; interior project photos.
Borrow only (1-2): A fan of real colour swatches for a customisable product
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: interior and product photography
Reject: Cookie modal over every frame; Generic grid
Token commitments: palette #E7E0D3, #716A61, #291C15, #553F33, #908A81; type DM-Sans, PP-Editorial-New, Axeptio Source Sans 3; engine GSAP + Lenis linked (never vendored).
