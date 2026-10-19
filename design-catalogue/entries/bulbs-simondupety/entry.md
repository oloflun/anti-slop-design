---
title: "Bulbs by Simon Dupety"
url: https://bulbs.simondupety.com/
source_url: https://bulbs.simondupety.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: "portfolio"
family: gallery-white-object-catalogue
dna: "Ceramic lamp catalogue x white-cube gallery"
register: editorial print
grammar: gallery/catalog
lane: "A white-cube catalogue where single photographs of ceramic lamps and flowers fold up out of the page like cards on a hinge, one object per scroll beat, with tiny serif captions and a price-list link."
mode: read
traits: ["white ground, object photography only", "images that fold up on a 3D hinge as they enter", "tiny serif captions in caps", "click to enable sound", "price list as the single action", "stacked small-format image pairs"]
palette: ["#FFFFFF", "#E1DDDA", "#C7AF86", "#AE875A", "#4F3925", "#EBD9A8"]
type: ["Special Gothic", "Big Caslon FB"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The page behaves like a gallery wall: nothing but white, one object at a time, small labels. The motion is the only flourish and it is physical, each photograph rotates up from a hinge at its base as if a card is being stood up on a table, so the objects arrive with weight rather than fading in.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Joffrey Spitzer).

## What to borrow (principle)

- Bring images in on a 3D hinge (rotateX from the base) so they stand up rather than fade
- One object per scroll beat with generous white so the catalogue reads as an exhibition
- Captions at caption size in a serif, never a heading

## What to leave

- Heavy smoothing (~220 px still travelling) makes the page feel floaty
- Very small text throughout

## Signature move

Photographs that stand up off the page on a hinge as they scroll in.

## Motion

Intro: a small stack of thumbnails assembles at centre, the first image grows (~1.5 s), 'click to enable sound'. Scroll (Lenis, very soft, ~220 px glide; Taxi transitions; heavy SplitText for captions): each image rotates up from a bottom hinge in perspective and settles flat, the previous one tilts away at the top; caption lines reveal per word; the close stacks images in a fanned pile beside the credits.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); split text; smoothed scroll (median 221 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the gallery/catalog grammar: a white-cube catalogue where single photographs of ceramic lamps and flowers fold up out of the page like cards on a hinge, one object per scroll beat, with tiny serif captions and a price-list link. Type: Special Gothic, Big Caslon FB.
Ground and ink from the measured palette (#FFFFFF, #E1DDDA, #C7AF86). Motion carries the page through
photographs that stand up off the page on a hinge as they scroll in. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — single ceramic or glass object, soft daylight, white plinth or wall, lots of air

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: single ceramic or glass object, soft daylight, white plinth or wall, lots of air

## Reference lock

Primary reference/direction: Bulbs by Simon Dupety — A white-cube catalogue where single photographs of ceramic lamps and flowers fold up out of the page like cards on a hinge, one object per scroll beat, with tiny serif captions and a price-list link.
Preserve (3-5 traits): white ground, object photography only; images that fold up on a 3D hinge as they enter; tiny serif captions in caps; click to enable sound; price list as the single action.
Borrow only (1-2): Bring images in on a 3D hinge (rotateX from the base) so they stand up rather than fade; One object per scroll beat with generous white so the catalogue reads as an exhibition
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: single ceramic or glass object, soft daylight, white plinth or wall, lots of air
Reject: Heavy smoothing (~220 px still travelling) makes the page feel floaty; Very small text throughout
Token commitments: palette #FFFFFF, #E1DDDA, #C7AF86, #AE875A, #4F3925, #EBD9A8; type Special Gothic, Big Caslon FB; engine GSAP + Lenis linked (never vendored).
