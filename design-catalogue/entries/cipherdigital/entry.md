---
title: "Cipher Digital"
url: http://cipherdigital.com/
source_url: http://cipherdigital.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "product-focused"
family: grid-window-datacenter
dna: "Hyperscale data centre developer x construction-grid windows"
register: cinematic dark
grammar: chaptered editorial
lane: "A data-centre developer on charcoal where a thin construction grid spans the page and photographs open as windows inside its cells (a server plate, a site under construction, a desert at dusk), the last one growing to full bleed with capacity figures counting up."
mode: read
traits: ["thin page-wide grid lines", "photos opening as windows in grid cells", "window that grows to full bleed", "counting capacity figures (MW, GW)", "dark charcoal and sand", "lime CTA"]
palette: ["#0C0E10", "#403D3C", "#252423", "#8C7A68"]
type: ["articulat-cf"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The grid is a site plan: images appear as cells being filled in, and the last cell (a desert at dusk, where the next site will be) expands until it is the whole frame. The counters then land over that landscape, so numbers are anchored to a real place.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Elliott Mangham, ONBOX Creative).

## What to borrow (principle)

- Open photographs as windows inside a visible page grid
- Expand the final window to full bleed for the key scene
- Count capacity numbers over the landscape they refer to

## What to leave

- Generic dark corporate hero
- Small light body text

## Signature move

A desert-at-dusk photo that opens in a grid cell and grows to fill the page.

## Motion

Intro: dark frame, a metal plate render with 'Built for Hyperscale.' (~1.5 s). Scroll (Lenis, ~130 px glide, 9 ScrollTriggers, 1 pin, SplitText): grid lines draw across; body text fades; construction photos open as windows and shift cells; the dusk landscape grows from a small window to full bleed; 'Rapidly scaling…' line; 700 MW / 4.4 GW / 207 MW count up; investor block; architectural light-and-shadow close.

Measured (`motion/probe.json`): GSAP 3.14.2; 9 ScrollTriggers; 1 pinned sections; Lenis; 4 video; split text; smoothed scroll (median 121 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a data-centre developer on charcoal where a thin construction grid spans the page and photographs open as windows inside its cells (a server plate, a site under construction, a desert at dusk), the last one growing to full bleed with capacity figures counting up. Type: articulat-cf.
Ground and ink from the measured palette (#0C0E10, #403D3C, #252423). Motion carries the page through
a desert-at-dusk photo that opens in a grid cell and grows to fill the page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — construction and desert landscape photography, dusk light, industrial details

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: construction and desert landscape photography, dusk light, industrial details

## Reference lock

Primary reference/direction: Cipher Digital — A data-centre developer on charcoal where a thin construction grid spans the page and photographs open as windows inside its cells (a server plate, a site under construction, a desert at dusk), the last one growing to full bleed with capacity figures counting up.
Preserve (3-5 traits): thin page-wide grid lines; photos opening as windows in grid cells; window that grows to full bleed; counting capacity figures (MW, GW); dark charcoal and sand.
Borrow only (1-2): Open photographs as windows inside a visible page grid; Expand the final window to full bleed for the key scene
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: construction and desert landscape photography, dusk light, industrial details
Reject: Generic dark corporate hero; Small light body text
Token commitments: palette #0C0E10, #403D3C, #252423, #8C7A68; type articulat-cf; engine GSAP + Lenis linked (never vendored).
