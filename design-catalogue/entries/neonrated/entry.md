---
title: "NEON - film distributor"
url: https://www.neonrated.com/
source_url: https://www.neonrated.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: ""
family: film-trailer-hero
dna: "Film distributor x a full-bleed film still with the title, which the capture opened into a trailer"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A film distributor's site: a full-bleed still of a family on a fjord with 'FJORD' in heavy caps and a slide counter; the wheel opened the trailer, so the capture shows the trailer's shots (NEON logo over mountains, interiors, a ferry, a Palme d'Or card) rather than the site's own scroll."
mode: experience
traits: ["full-bleed film still", "heavy title caps", "slide counter", "trailer overlay"]
palette: ["#000000", "#56716F", "#152F36", "#69918F", "#51473E", "#A8AE96"]
type: ["Girott", "Focal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Leading with one still and a title lets the film sell itself.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Antinomy Studio).

## What to borrow (principle)

- One still and one title as the whole hero

## What to leave

- Capture shows the trailer, not the page

## Signature move

'FJORD' in heavy caps over a family on a fjord.

## Motion

Hero slides with a counter; the trailer opens as an overlay player.

Measured (`motion/probe.json`): Lenis; 2 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Reject All, Close, PLAY TRAILER. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a film distributor's site: a full-bleed still of a family on a fjord with 'FJORD' in heavy caps and a slide counter; the wheel opened the trailer, so the capture shows the trailer's shots (NEON logo over mountains, interiors, a ferry, a Palme d'Or card) rather than the site's own scroll. Type: Girott, Focal.
Ground and ink from the measured palette (#000000, #56716F, #152F36). Motion carries the page through
'FJORD' in heavy caps over a family on a fjord. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film stills, trailer

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film stills, trailer

## Reference lock

Primary reference/direction: NEON - film distributor — A film distributor's site: a full-bleed still of a family on a fjord with 'FJORD' in heavy caps and a slide counter; the wheel opened the trailer, so the capture shows the trailer's shots (NEON logo over mountains, interiors, a ferry, a Palme d'Or card) rather than the site's own scroll.
Preserve (3-5 traits): full-bleed film still; heavy title caps; slide counter; trailer overlay.
Borrow only (1-2): One still and one title as the whole hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film stills, trailer
Reject: Capture shows the trailer, not the page
Token commitments: palette #000000, #56716F, #152F36, #69918F, #51473E, #A8AE96; type Girott, Focal; engine GSAP + Lenis linked (never vendored).
