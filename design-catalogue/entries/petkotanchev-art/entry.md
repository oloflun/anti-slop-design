---
title: "Petko Tanchev - Interactive Media Artist"
url: https://petkotanchev.art/
source_url: https://petkotanchev.art/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "institutional"
family: media-artist-dark-gallery
dna: "Bulgarian media artist and scenographer x projection-mapped spectacle photography"
register: cinematic dark
grammar: chaptered editorial
lane: "A media artist's site: a full-bleed night shot of a light show with a giant mapped fish, the name, a manifesto in thin uppercase, a featured project 'Mysteries of Transition' with the golden fish, a vertical 'Gallery' label beside a mosaic of projects, and a long biography interleaved with portraits and installation photos."
mode: read
traits: ["projection-mapped spectacle photography", "thin uppercase manifesto", "vertical rotated section label", "project mosaic", "long biography with images", "cookie bar"]
palette: ["#111317", "#E0E0E0", "#7C756D"]
type: ["SofiaSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The work photographs are spectacular enough to carry a conventional layout; the vertical labels add a gallery feel.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: I-Creativ Studio).

## What to borrow (principle)

- Rotate section labels vertically for a gallery tone

## What to leave

- Cookie bar in every frame
- Long text-heavy biography

## Signature move

A giant projection-mapped golden fish over a night city.

## Motion

Intro: dark for ~1.5 s, the night shot fades in. Wheel (Lenis ~130 px glide): the manifesto slides up line by line; the featured image scales into a card; the mosaic shifts; biography images reveal with a clip.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; WebGL canvas x2; smoothed scroll (median 134 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a media artist's site: a full-bleed night shot of a light show with a giant mapped fish, the name, a manifesto in thin uppercase, a featured project 'Mysteries of Transition' with the golden fish, a vertical 'Gallery' label beside a mosaic of projects, and a long biography interleaved with portraits and installation photos. Type: SofiaSans.
Ground and ink from the measured palette (#111317, #E0E0E0, #7C756D). Motion carries the page through
a giant projection-mapped golden fish over a night city. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — installation and projection mapping photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: installation and projection mapping photography

## Reference lock

Primary reference/direction: Petko Tanchev - Interactive Media Artist — A media artist's site: a full-bleed night shot of a light show with a giant mapped fish, the name, a manifesto in thin uppercase, a featured project 'Mysteries of Transition' with the golden fish, a vertical 'Gallery' label beside a mosaic of projects, and a long biography interleaved with portraits and installation photos.
Preserve (3-5 traits): projection-mapped spectacle photography; thin uppercase manifesto; vertical rotated section label; project mosaic; long biography with images.
Borrow only (1-2): Rotate section labels vertically for a gallery tone
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: installation and projection mapping photography
Reject: Cookie bar in every frame; Long text-heavy biography
Token commitments: palette #111317, #E0E0E0, #7C756D; type SofiaSans; engine GSAP + Lenis linked (never vendored).
