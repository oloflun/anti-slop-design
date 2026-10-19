---
title: "Radiance - creative team"
url: https://radiance.family/
source_url: https://radiance.family/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: team-photo-agency-yellow
dna: "Dresden creative team x a team photo that expands and colour panels sliding over each other"
register: other
grammar: chaptered editorial
lane: "An agency: a yellow counter, 'RADIANCE' huge with a grass texture in one letter, 'Meet with our outstanding team' as a card that grows into a full team photo, a yellow ground, 'Recognized by the community' on a black card, bubbles of services, a black panel with budget cards, a pink curved panel 'And this is just a small part of our presentation' and works."
mode: persuade
traits: ["counter loader", "texture inside a letter", "card growing into team photo", "stacked rounded panels", "floating service bubbles", "yellow, black and pink"]
palette: ["#060606", "#F3F4EF", "#B2A588", "#3F3A30"]
type: ["Inter Tight"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The team photo growing from a card is a warm opener; the rest stacks panels.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Grow a small card into the full team photo

## What to leave

- Generic panels

## Signature move

A small card growing into a full photo of the team.

## Motion

Intro: yellow counter (~2 s), the wordmark. Wheel: the black panel rises with a card that grows full screen; panels slide up as rounded sheets; bubbles drift; the pink curve rises; works scroll.

Measured (`motion/probe.json`): GSAP 3.12.5; 5 ScrollTriggers; 2 pinned sections; Lenis; WebGL canvas x2 (three.js); 3 video; smoothed scroll (median 127 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: an agency: a yellow counter, 'RADIANCE' huge with a grass texture in one letter, 'Meet with our outstanding team' as a card that grows into a full team photo, a yellow ground, 'Recognized by the community' on a black card, bubbles of services, a black panel with budget cards, a pink curved panel 'And this is just a small part of our presentation' and works. Type: Inter Tight.
Ground and ink from the measured palette (#060606, #F3F4EF, #B2A588). Motion carries the page through
a small card growing into a full photo of the team. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — team and project photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: team and project photography

## Reference lock

Primary reference/direction: Radiance - creative team — An agency: a yellow counter, 'RADIANCE' huge with a grass texture in one letter, 'Meet with our outstanding team' as a card that grows into a full team photo, a yellow ground, 'Recognized by the community' on a black card, bubbles of services, a black panel with budget cards, a pink curved panel 'And this is just a small part of our presentation' and works.
Preserve (3-5 traits): counter loader; texture inside a letter; card growing into team photo; stacked rounded panels; floating service bubbles.
Borrow only (1-2): Grow a small card into the full team photo
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: team and project photography
Reject: Generic panels
Token commitments: palette #060606, #F3F4EF, #B2A588, #3F3A30; type Inter Tight; engine GSAP + Lenis linked (never vendored).
