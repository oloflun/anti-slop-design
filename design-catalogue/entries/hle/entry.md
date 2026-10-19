---
title: "HLE"
url: https://hle.io/
source_url: https://hle.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: crt-monitor-media-agency
dna: "Music and media talent agency x vintage CRT monitor"
register: modern clean
grammar: filmic one-shot
lane: "A talent agency that types its positioning on black, then zooms out to a vintage white CRT on a grey shelf showing the same text, zooms back into the screen through a 'NO SIGNAL' static frame, and continues inside the screen's grid world with projects and a warping headline."
mode: persuade
traits: ["typed headline with cursor", "3D vintage CRT monitor", "zoom into the screen as the transition", "'NO SIGNAL' static frame", "dark grid world inside the screen", "warping/wobbling headline type"]
palette: ["#101010", "#8B8B8B", "#767676", "#B6B6B6", "#5D5D5D"]
type: ["PPSupplyMonoRegular", "PPSupplySansRegular"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The camera move is the story: the line you just read turns out to be on a little monitor, and the page enters that monitor, through static, into the agency's world. The zoom-through-the-screen gives a single continuous transition from intro to content.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The First The Last).

## What to borrow (principle)

- Reveal that the intro text was on an object, then zoom into that object as the transition
- A 'no signal' static frame as the cut between worlds
- Type the positioning line with a cursor before showing anything

## What to leave

- Small grey UI labels
- Wobbling headline is hard to read

## Signature move

Zooming into a vintage CRT through a 'NO SIGNAL' static frame.

## Motion

Intro: 'Positioned at the axis of talent and content across music' types character by character with a cursor on black (~2 s). Scroll (virtual, ScrollTo, MotionPath, WebGL): pull back to reveal the text on a white CRT on a shelf; camera pushes in until the screen fills the frame; 'NO SIGNAL' blue static; inside, a grid with the line retyped; 'Our projects' cards; 'Helping people get their idea sold' warps letter by letter; contact.

Measured (`motion/probe.json`): GSAP 3.8.0; WebGL canvas x1 (three.js); 1 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the filmic one-shot grammar: a talent agency that types its positioning on black, then zooms out to a vintage white CRT on a grey shelf showing the same text, zooms back into the screen through a 'NO SIGNAL' static frame, and continues inside the screen's grid world with projects and a warping headline. Type: PPSupplyMonoRegular, PPSupplySansRegular.
Ground and ink from the measured palette (#101010, #8B8B8B, #767676). Motion carries the page through
zooming into a vintage CRT through a 'NO SIGNAL' static frame. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D render of retro hardware on a plain grey set

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D render of retro hardware on a plain grey set

## Reference lock

Primary reference/direction: HLE — A talent agency that types its positioning on black, then zooms out to a vintage white CRT on a grey shelf showing the same text, zooms back into the screen through a 'NO SIGNAL' static frame, and continues inside the screen's grid world with projects and a warping headline.
Preserve (3-5 traits): typed headline with cursor; 3D vintage CRT monitor; zoom into the screen as the transition; 'NO SIGNAL' static frame; dark grid world inside the screen.
Borrow only (1-2): Reveal that the intro text was on an object, then zoom into that object as the transition; A 'no signal' static frame as the cut between worlds
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D render of retro hardware on a plain grey set
Reject: Small grey UI labels; Wobbling headline is hard to read
Token commitments: palette #101010, #8B8B8B, #767676, #B6B6B6, #5D5D5D; type PPSupplyMonoRegular, PPSupplySansRegular; engine GSAP + Lenis linked (never vendored).
