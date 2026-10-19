---
title: "Rectangles - design's group chat"
url: https://rectangles.fm/
source_url: https://rectangles.fm/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: paper-scrapbook-podcast
dna: "Design podcast x a scrapbook of polaroids, records, envelopes and sticky notes"
register: other
grammar: chaptered editorial
lane: "A podcast and newsletter site on black: 'Where designers get unstuck' with a paper-clipped card and a polaroid of the host, 'Livestreams' as polaroids of guests sliding over vinyl records with handwritten names, 'Newsletters' as envelopes with stamps and headline cards ('Jony Ive + Ferrari = ?'), 'Takeaways' as a binder of punched pages, 'From our community' as sticky notes with highlighter, 'A note from Chris' as a folded letter, and a persistent 'Design's group chat' sign-up card."
mode: read
traits: ["polaroids and vinyl", "envelopes with stamps", "punched binder pages", "sticky notes with highlighter", "handwritten names", "black ground with paper objects"]
palette: ["#0D0D0D", "#D4D2CA", "#A29889", "#E9E8E1", "#3C3B36"]
type: ["Forma DJR Display Regular", "Forma DJR Display Bold", "Perfume Sans 1", "Forma DJR Display Regular Placeholder"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Every section is a different paper object, so the content is sorted by material: records for shows, envelopes for mail, notes for the community.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Ashwin Pradeep Kumar).

## What to borrow (principle)

- Give each content type its own paper object

## What to leave

- Persistent sign-up card overlaps

## Signature move

Guest polaroids sliding over vinyl records with handwritten names.

## Motion

Intro: the clipped card drops in. Wheel: polaroids slide and rotate over records; envelopes stack and tilt; binder pages turn; sticky notes peel in; the letter unfolds.

Measured (`motion/probe.json`): GSAP 3.14.1; 1 ScrollTriggers; 1 pinned sections; Lenis; WebGL canvas x1; smoothed scroll (median 153 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a podcast and newsletter site on black: 'Where designers get unstuck' with a paper-clipped card and a polaroid of the host, 'Livestreams' as polaroids of guests sliding over vinyl records with handwritten names, 'Newsletters' as envelopes with stamps and headline cards ('Jony Ive + Ferrari = ?'), 'Takeaways' as a binder of punched pages, 'From our community' as sticky notes with highlighter, 'A note from Chris' as a folded letter, and a persistent 'Design's group chat' sign-up card. Type: Forma DJR Display Regular, Forma DJR Display Bold, Perfume Sans 1, Forma DJR Display Regular Placeholder.
Ground and ink from the measured palette (#0D0D0D, #D4D2CA, #A29889). Motion carries the page through
guest polaroids sliding over vinyl records with handwritten names. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — photography, paper objects

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: photography, paper objects

## Reference lock

Primary reference/direction: Rectangles - design's group chat — A podcast and newsletter site on black: 'Where designers get unstuck' with a paper-clipped card and a polaroid of the host, 'Livestreams' as polaroids of guests sliding over vinyl records with handwritten names, 'Newsletters' as envelopes with stamps and headline cards ('Jony Ive + Ferrari = ?'), 'Takeaways' as a binder of punched pages, 'From our community' as sticky notes with highlighter, 'A note from Chris' as a folded letter, and a persistent 'Design's group chat' sign-up card.
Preserve (3-5 traits): polaroids and vinyl; envelopes with stamps; punched binder pages; sticky notes with highlighter; handwritten names.
Borrow only (1-2): Give each content type its own paper object
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: photography, paper objects
Reject: Persistent sign-up card overlaps
Token commitments: palette #0D0D0D, #D4D2CA, #A29889, #E9E8E1, #3C3B36; type Forma DJR Display Regular, Forma DJR Display Bold, Perfume Sans 1, Forma DJR Display Regular Placeholder; engine GSAP + Lenis linked (never vendored).
