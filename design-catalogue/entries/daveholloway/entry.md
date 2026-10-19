---
title: "Dave Holloway"
url: https://daveholloway.uk/
source_url: https://daveholloway.uk/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: cobalt-cartoon-pitch-folio
dna: "Freelance designer folio x cartoon self-portrait and football pitch"
register: illustrated dark
grammar: chaptered editorial
lane: "A cobalt-blue folio led by a cartoon self-portrait under a speech-bubble 'HEY!', with a project carousel over a green cycling landscape, service cards like trading cards, a football pitch that rises from a wireframe stadium for the about section, and a guitar that curls in for 'READY TO PLAY?'."
mode: persuade
traits: ["saturated cobalt ground", "illustrated self-portrait", "trading-card service cards", "wireframe stadium resolving into a pitch", "scoreboard-style award ticker", "guitar illustration at the close"]
palette: ["#798F68", "#2C47FF", "#0A0B14", "#5E3681", "#9CAD77", "#6F6F94"]
type: ["Alumni Sans", "Gasoek One"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The folio is a person's hobbies made into structure: the about section is a football pitch with a scoreboard ticker of awards, and the contact is a guitar ('ready to play?'). One cobalt ground holds all of it so the illustrations feel like one sticker book.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Portfolio).

## What to borrow (principle)

- Turn a personal interest into a section device (pitch + scoreboard for awards)
- Present services as collectible cards in a fanned row
- Let a wireframe resolve into the illustrated scene as the transition

## What to leave

- Heavy smoothing on a dense page
- Very small body text in cards

## Signature move

A wireframe stadium that resolves into a football pitch with an award scoreboard.

## Motion

Intro: logo mark on white, then black flash, then the cobalt portrait with 'HEY!' typing in a card (~3 s). Scroll (Lenis, 1 pin, SplitText, WebGL): 'WORK' with a project card carousel over a hilly cycling illustration; 'SERVICES' trading cards fan in; a wireframe stadium draws and zooms into a green pitch; about card with a scrolling scoreboard ticker; the pitch curves away; a guitar fills the frame for 'READY TO PLAY?' set along its curve; contact.

Measured (`motion/probe.json`): GSAP 3.14.2; 1 pinned sections; Lenis; WebGL canvas x15 (three.js); split text; smoothed scroll (median 64 px still travelling after input stops); entry gate: Skip to main content. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a cobalt-blue folio led by a cartoon self-portrait under a speech-bubble 'HEY!', with a project carousel over a green cycling landscape, service cards like trading cards, a football pitch that rises from a wireframe stadium for the about section, and a guitar that curls in for 'READY TO PLAY?'. Type: Alumni Sans, Gasoek One.
Ground and ink from the measured palette (#798F68, #2C47FF, #0A0B14). Motion carries the page through
a wireframe stadium that resolves into a football pitch with an award scoreboard. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat vector illustration (portrait, landscapes, pitch, guitar) in saturated colour

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat vector illustration (portrait, landscapes, pitch, guitar) in saturated colour

## Reference lock

Primary reference/direction: Dave Holloway — A cobalt-blue folio led by a cartoon self-portrait under a speech-bubble 'HEY!', with a project carousel over a green cycling landscape, service cards like trading cards, a football pitch that rises from a wireframe stadium for the about section, and a guitar that curls in for 'READY TO PLAY?'.
Preserve (3-5 traits): saturated cobalt ground; illustrated self-portrait; trading-card service cards; wireframe stadium resolving into a pitch; scoreboard-style award ticker.
Borrow only (1-2): Turn a personal interest into a section device (pitch + scoreboard for awards); Present services as collectible cards in a fanned row
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat vector illustration (portrait, landscapes, pitch, guitar) in saturated colour
Reject: Heavy smoothing on a dense page; Very small body text in cards
Token commitments: palette #798F68, #2C47FF, #0A0B14, #5E3681, #9CAD77, #6F6F94; type Alumni Sans, Gasoek One; engine GSAP + Lenis linked (never vendored).
