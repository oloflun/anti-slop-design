---
title: "24/7 Artists - music business platform"
url: https://247artists.com/
source_url: https://247artists.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: music-platform-colour-chapters
dna: "Music career platform x full-colour chapters and scattered tag cards"
register: other
grammar: chaptered editorial
lane: "A music business platform: 'Build your music career step by step' with concert photos popping in, a red 'The music business can be hard. It doesn't have to be...', cream, lime with scattered tag cards ('We help artists grow'), yellow with the Career GPS and streaming calculator UI, purple grid with '24/7' and photos, pricing and dark CTA."
mode: persuade
traits: ["full-colour chapters", "statement split across two screens", "scattered tilted tag cards", "product UI cards", "purple grid", "inline highlighted words"]
palette: ["#FF4438", "#FFF0D1", "#241E25", "#C69092", "#762E2E"]
type: ["Gellix"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each chapter's colour is a beat in the argument (hard, easy, help, simplify, community), so the colour changes carry the story.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let colour changes mark the beats of the pitch

## What to leave

- Cookie bar in frames

## Signature move

'The music business can be hard. It doesn't have to be...' on red.

## Motion

Intro: dark with the headline and photos popping (~2 s). Wheel (Lenis): a red bar grows into the red panel; words slide; each colour panel wipes up; tag cards scatter in; UI cards stack; the grid fills with photos.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 4 video; split text; smoothed scroll (median 148 px still travelling after input stops); entry gate: Decline. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a music business platform: 'Build your music career step by step' with concert photos popping in, a red 'The music business can be hard. It doesn't have to be...', cream, lime with scattered tag cards ('We help artists grow'), yellow with the Career GPS and streaming calculator UI, purple grid with '24/7' and photos, pricing and dark CTA. Type: Gellix.
Ground and ink from the measured palette (#FF4438, #FFF0D1, #241E25). Motion carries the page through
'The music business can be hard. It doesn't have to be...' on red. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — concert photography, product UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: concert photography, product UI

## Reference lock

Primary reference/direction: 24/7 Artists - music business platform — A music business platform: 'Build your music career step by step' with concert photos popping in, a red 'The music business can be hard. It doesn't have to be...', cream, lime with scattered tag cards ('We help artists grow'), yellow with the Career GPS and streaming calculator UI, purple grid with '24/7' and photos, pricing and dark CTA.
Preserve (3-5 traits): full-colour chapters; statement split across two screens; scattered tilted tag cards; product UI cards; purple grid.
Borrow only (1-2): Let colour changes mark the beats of the pitch
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: concert photography, product UI
Reject: Cookie bar in frames
Token commitments: palette #FF4438, #FFF0D1, #241E25, #C69092, #762E2E; type Gellix; engine GSAP + Lenis linked (never vendored).
