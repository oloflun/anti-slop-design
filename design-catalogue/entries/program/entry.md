---
title: "Program Studio"
url: https://program.studio/
source_url: https://program.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: barcelona-desktop-collage-studio
dna: "Barcelona technical studio x desktop of draggable objects"
register: modern clean
grammar: live surface
lane: "A grey desktop of a studio where everything is a draggable object: a tilted statement in a red selection box, project cards, sticky notes, a weather widget, a phone icon, accordion cards for each process step, and a giant toggle switch, all drifting into place as you scroll."
mode: persuade
traits: ["grid-paper ground with a red selection box", "everything as a draggable card or widget", "Times New Roman as the only face", "giant UI toggle and phone icon", "process accordion cards", "playful local widgets (weather, map)"]
palette: ["#E0E0E0", "#BFBFBF", "#FBE25E", "#816453", "#7EB4DB", "#9FC8E8"]
type: ["Times New Roman"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The studio builds interactive systems, so the page is one: a tilted headline in a selection box like a design tool, then widgets, cards and notes laid on a grey desk that drift and can be moved. The single serif (Times New Roman) keeps a technical page oddly literary.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Program Studio, SMLXL).

## What to borrow (principle)

- Present the studio as a desktop of manipulable objects
- A selection box with handles around the headline to signal 'tool'
- Local widgets (weather, map) as warm proof of place

## What to leave

- Cookie dialog in the opening frames
- Busy: many objects compete at once

## Signature move

A tilted headline inside a red selection box with handles, like an object in a design tool.

## Motion

Intro: grid paper, a tilted statement and project photos rotate into place, then the red selection box draws around the headline (~2 s). Scroll (Lenis, ~120 px glide, Barba, Draggable, WebGL x2): project cards drift at different depths; 'View All Projects' pill; sticky notes ('try drawing Cuphead'); process accordion cards open one by one; dot circle; phone number in a pill; giant toggle; product cards; weather widget and 'Pro' sticker close.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; Barba page transitions; WebGL canvas x2 (three.js); 10 video; split text; smoothed scroll (median 123 px still travelling after input stops); entry gate: Deny. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the live surface grammar: a grey desktop of a studio where everything is a draggable object: a tilted statement in a red selection box, project cards, sticky notes, a weather widget, a phone icon, accordion cards for each process step, and a giant toggle switch, all drifting into place as you scroll. Type: Times New Roman.
Ground and ink from the measured palette (#E0E0E0, #BFBFBF, #FBE25E). Motion carries the page through
a tilted headline inside a red selection box with handles, like an object in a design tool. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — client project visuals as cards, UI widgets, sticky notes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: client project visuals as cards, UI widgets, sticky notes

## Reference lock

Primary reference/direction: Program Studio — A grey desktop of a studio where everything is a draggable object: a tilted statement in a red selection box, project cards, sticky notes, a weather widget, a phone icon, accordion cards for each process step, and a giant toggle switch, all drifting into place as you scroll.
Preserve (3-5 traits): grid-paper ground with a red selection box; everything as a draggable card or widget; Times New Roman as the only face; giant UI toggle and phone icon; process accordion cards.
Borrow only (1-2): Present the studio as a desktop of manipulable objects; A selection box with handles around the headline to signal 'tool'
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: client project visuals as cards, UI widgets, sticky notes
Reject: Cookie dialog in the opening frames; Busy: many objects compete at once
Token commitments: palette #E0E0E0, #BFBFBF, #FBE25E, #816453, #7EB4DB, #9FC8E8; type Times New Roman; engine GSAP + Lenis linked (never vendored).
