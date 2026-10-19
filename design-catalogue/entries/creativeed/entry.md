---
title: "Creative Ed"
url: https://www.creativeed.dev/
source_url: https://www.creativeed.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: comic-collage-dev-folio
dna: "Creative developer folio x comic book collage"
register: illustrated dark
grammar: chaptered editorial
lane: "A developer folio that loads with a cartoon avatar counting to 100, then breaks into comic-panel diagonals in red and black, purple project cards pinned like notes, a sage 'Bloom & Philosophy' desk with terminal windows, and a draw-something contact form."
mode: persuade
traits: ["avatar count-up loader", "diagonal comic panels in red and black", "sticker labels (ARTIST BY SOUL / CODER BY TRADE)", "pinned paper project cards on purple", "desktop-window props", "draw-on-canvas contact form"]
palette: ["#1A191C", "#A955F6", "#CA2424", "#F9F0BB", "#BFB396", "#432841"]
type: ["Caveat", "Lexend Mega", "Staatliches", "Playfair Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Every section is a different material (comic panels, pinned notes, a desk with windows, a sketchbook form), held together by the avatar character and a sticker typography. The diagonal panel cuts at the start make the transition from loader to hero feel like a page being torn open.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Ed).

## What to borrow (principle)

- Diagonal panel cuts as the hero transition, like comic frames
- A draw-on-canvas contact form as a playful close
- Sticker-label typography for the self-description

## What to leave

- Four different worlds on one page; the systems don't share a palette
- Small handwriting-style text

## Signature move

Diagonal comic panels slicing in red and black as the avatar's loader finishes.

## Motion

Intro: avatar and a serif counter 08 → 87 → 100 (~2.5 s), then the white ground is cut by diagonal red/black/yellow panels sliding past. Scroll (scrollY with ScrollTrigger, Draggable): sticker labels stack in; panels shift diagonally; purple section where project cards drop in pinned; sage section with draggable desktop windows and a growing vine; contact form with a drawing palette.

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x1. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a developer folio that loads with a cartoon avatar counting to 100, then breaks into comic-panel diagonals in red and black, purple project cards pinned like notes, a sage 'Bloom & Philosophy' desk with terminal windows, and a draw-something contact form. Type: Caveat, Lexend Mega, Staatliches, Playfair Display.
Ground and ink from the measured palette (#1A191C, #A955F6, #CA2424). Motion carries the page through
diagonal comic panels slicing in red and black as the avatar's loader finishes. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — illustrated avatar, comic panels, paper props

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: illustrated avatar, comic panels, paper props

## Reference lock

Primary reference/direction: Creative Ed — A developer folio that loads with a cartoon avatar counting to 100, then breaks into comic-panel diagonals in red and black, purple project cards pinned like notes, a sage 'Bloom & Philosophy' desk with terminal windows, and a draw-something contact form.
Preserve (3-5 traits): avatar count-up loader; diagonal comic panels in red and black; sticker labels (ARTIST BY SOUL / CODER BY TRADE); pinned paper project cards on purple; desktop-window props.
Borrow only (1-2): Diagonal panel cuts as the hero transition, like comic frames; A draw-on-canvas contact form as a playful close
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: illustrated avatar, comic panels, paper props
Reject: Four different worlds on one page; the systems don't share a palette; Small handwriting-style text
Token commitments: palette #1A191C, #A955F6, #CA2424, #F9F0BB, #BFB396, #432841; type Caveat, Lexend Mega, Staatliches, Playfair Display; engine GSAP + Lenis linked (never vendored).
