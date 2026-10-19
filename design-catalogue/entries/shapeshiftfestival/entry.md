---
title: "SHAPESHIFT 2026"
url: https://shapeshiftfestival.com/
source_url: https://shapeshiftfestival.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "editorial"
family: pixel-code-tech-festival
dna: "Tech and art festival x pixel blocks and code brackets"
register: modern clean
grammar: chaptered editorial
lane: "A festival site where a QR-like pixel mark forms on grey, the theme ':The Human Algorithm:' is set with code brackets, black sections are broken by grey pixel squares, the lineup appears as photos with neon-green pixel clusters on their corners, and a pixel drawing game closes."
mode: persuade
traits: ["pixel-block mark and transitions", "code brackets around display text (<DATE>, </PLACE>)", "black and pale grey with neon green and yellow", "lineup photos with green pixel clusters", "typing headlines with cursor", "pixel-art drawing tool"]
palette: ["#000000", "#E9E9E9", "#171717", "#B7B8B0", "#565556", "#FAFB1F"]
type: ["Hoves", "Manrope-Regular"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The theme (humans and algorithms) is carried by a single visual unit, the pixel, and by code syntax wrapped around ordinary information (dates and places in tags). Black and grey grounds are broken into pixel squares, so even section changes look computed.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Next DC - Creative Agency).

## What to borrow (principle)

- Wrap plain event info in code syntax as the typographic voice
- Pixel squares as the unit for transitions and photo accents
- Close with a small interactive toy (pixel drawing) that fits the theme

## What to leave

- Cookie panel over every frame
- Lineup cards are small

## Signature move

Event facts written as code tags: <DATE> 24.04 </DATE> <PLACE> SOFIA </PLACE>.

## Motion

Intro: grey with scattered dots that gather into a pixel mark, 'initializing the human element' (~2.5 s). Scroll (Lenis, ~125 px glide, 1 pin, Barba, WebGL): ':The Human Algorithm:' with code-tag info cards; marquee; black manifesto; pixel squares cut the black; lineup [001]–[008] with photos and green pixel clusters; 'TALKS / WORKSHOPS / EXHIBITION / SCREENINGS' list where the active item gets a red band and photo; pixel art; drawing tool; '<DON'T MISS THE EVENT>' typing; partners grid.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; Barba page transitions; WebGL canvas x1; 1 video; smoothed scroll (median 128 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a festival site where a QR-like pixel mark forms on grey, the theme ':The Human Algorithm:' is set with code brackets, black sections are broken by grey pixel squares, the lineup appears as photos with neon-green pixel clusters on their corners, and a pixel drawing game closes. Type: Hoves, Manrope-Regular.
Ground and ink from the measured palette (#000000, #E9E9E9, #171717). Motion carries the page through
event facts written as code tags: <DATE> 24.04 </DATE> <PLACE> SOFIA </PLACE>. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — speaker portraits and art installation photos with pixel overlays

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: speaker portraits and art installation photos with pixel overlays

## Reference lock

Primary reference/direction: SHAPESHIFT 2026 — A festival site where a QR-like pixel mark forms on grey, the theme ':The Human Algorithm:' is set with code brackets, black sections are broken by grey pixel squares, the lineup appears as photos with neon-green pixel clusters on their corners, and a pixel drawing game closes.
Preserve (3-5 traits): pixel-block mark and transitions; code brackets around display text (<DATE>, </PLACE>); black and pale grey with neon green and yellow; lineup photos with green pixel clusters; typing headlines with cursor.
Borrow only (1-2): Wrap plain event info in code syntax as the typographic voice; Pixel squares as the unit for transitions and photo accents
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: speaker portraits and art installation photos with pixel overlays
Reject: Cookie panel over every frame; Lineup cards are small
Token commitments: palette #000000, #E9E9E9, #171717, #B7B8B0, #565556, #FAFB1F; type Hoves, Manrope-Regular; engine GSAP + Lenis linked (never vendored).
