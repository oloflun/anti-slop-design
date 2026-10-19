---
title: "GRAPHICHUNTERS - sports design studio"
url: https://www.graphichunters.com/
source_url: https://www.graphichunters.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "consumer-brand"
family: sports-design-studio-condensed
dna: "Sports-only design studio x a crosshair loader and portraits flying around 'Our lineup'"
register: modern clean
grammar: chaptered editorial
lane: "A design studio working only in sports: a wordmark with a crosshair that targets letters, a glowing ball on black, 'We are the creative design studio' in heavy condensed caps with a green jersey between the words, Topps and Borussia Dortmund cases, a services list, 'First Class' and 'Grounded' over a halftone basketball photo, 'Our lineup' with team portraits flying around the title like trading cards, and 'Behind the hunt'."
mode: persuade
traits: ["crosshair loader", "heavy condensed caps", "jersey between words", "halftone sports photo", "team portraits flying around a title", "sticker 'Join us' badge"]
palette: ["#F1F1F1", "#242021", "#989D93", "#0B0A0B", "#D8DFD3", "#453D3D"]
type: ["Bolgarus Beta", "Denton Condensed", "Plaid S Mono", "Neue Haas Grotesk Display Pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The crosshair (hunters) and the lineup of portraits around the title borrow sports language (targeting, team sheet) for an agency page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fly portraits around the title like a team lineup

## What to leave

- Small labels

## Signature move

Team portraits flying around 'OUR LINEUP' like trading cards.

## Motion

Intro: white, a crosshair moves across the wordmark and letters drop out (~2 s). Wheel (Lenis): the ball rotates; condensed lines slide in around the jersey; cases scale; services list highlights; the halftone photo scales; portraits fly in from all sides around the pinned title.

Measured (`motion/probe.json`): GSAP 3.12.5; 25 ScrollTriggers; Lenis; Barba page transitions; smoothed scroll (median 143 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a design studio working only in sports: a wordmark with a crosshair that targets letters, a glowing ball on black, 'We are the creative design studio' in heavy condensed caps with a green jersey between the words, Topps and Borussia Dortmund cases, a services list, 'First Class' and 'Grounded' over a halftone basketball photo, 'Our lineup' with team portraits flying around the title like trading cards, and 'Behind the hunt'. Type: Bolgarus Beta, Denton Condensed, Plaid S Mono, Neue Haas Grotesk Display Pro.
Ground and ink from the measured palette (#F1F1F1, #242021, #989D93). Motion carries the page through
team portraits flying around 'OUR LINEUP' like trading cards. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — sports photography and design work

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: sports photography and design work

## Reference lock

Primary reference/direction: GRAPHICHUNTERS - sports design studio — A design studio working only in sports: a wordmark with a crosshair that targets letters, a glowing ball on black, 'We are the creative design studio' in heavy condensed caps with a green jersey between the words, Topps and Borussia Dortmund cases, a services list, 'First Class' and 'Grounded' over a halftone basketball photo, 'Our lineup' with team portraits flying around the title like trading cards, and 'Behind the hunt'.
Preserve (3-5 traits): crosshair loader; heavy condensed caps; jersey between words; halftone sports photo; team portraits flying around a title.
Borrow only (1-2): Fly portraits around the title like a team lineup
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: sports photography and design work
Reject: Small labels
Token commitments: palette #F1F1F1, #242021, #989D93, #0B0A0B, #D8DFD3, #453D3D; type Bolgarus Beta, Denton Condensed, Plaid S Mono, Neue Haas Grotesk Display Pro; engine GSAP + Lenis linked (never vendored).
