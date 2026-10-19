---
title: "Trevor Noah - comedian, author, host"
url: https://www.trevornoah.com/
source_url: https://www.trevornoah.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: torn-paper-collage-persona
dna: "Entertainer's site x torn-paper collage of his head and floating props"
register: other
grammar: chaptered editorial
lane: "A personal site on navy: a pink counter, 'Trevor Noah' with his head torn open as a paper collage spilling a mic, a YouTube player and books, 'Finding the extraordinary in the ordinary' with a pink word, 'Media on the screen' with a player and cut-outs, torn paper edges tearing across between sections, 'About this guy' with his face and thought bubbles, 'A curious human intrigued by the world around him', a dates table 'Where's Trevor?', a quote, 'Books on the page' with books floating."
mode: persuade
traits: ["torn paper edges between sections", "collage cut-outs floating", "pink accent words", "navy ground", "thought-bubble props", "dates table"]
palette: ["#1D243F", "#BA9080", "#DBD3CE", "#765B5A"]
type: ["Die Grotesk C", "Die Grotesk B", "Die Grotesk D"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Torn paper is the transition and the hero's idea at once: the page tears open the way his head does.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: OFF+BRAND).

## What to borrow (principle)

- Use one physical material (torn paper) as every section transition

## What to leave

- Cookie panel in every frame

## Signature move

Trevor Noah's head torn open as a paper collage spilling a mic and a YouTube player.

## Motion

Intro: pink counter 0 to 100 (~2 s). Wheel (Lenis): the head collage parts; props float with parallax; a torn edge tears across to reveal the next section; cut-outs drift in; books float up.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); smoothed scroll (median 128 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a personal site on navy: a pink counter, 'Trevor Noah' with his head torn open as a paper collage spilling a mic, a YouTube player and books, 'Finding the extraordinary in the ordinary' with a pink word, 'Media on the screen' with a player and cut-outs, torn paper edges tearing across between sections, 'About this guy' with his face and thought bubbles, 'A curious human intrigued by the world around him', a dates table 'Where's Trevor?', a quote, 'Books on the page' with books floating. Type: Die Grotesk C, Die Grotesk B, Die Grotesk D.
Ground and ink from the measured palette (#1D243F, #BA9080, #DBD3CE). Motion carries the page through
trevor Noah's head torn open as a paper collage spilling a mic and a YouTube player. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — photo collage, cut-outs

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: photo collage, cut-outs

## Reference lock

Primary reference/direction: Trevor Noah - comedian, author, host — A personal site on navy: a pink counter, 'Trevor Noah' with his head torn open as a paper collage spilling a mic, a YouTube player and books, 'Finding the extraordinary in the ordinary' with a pink word, 'Media on the screen' with a player and cut-outs, torn paper edges tearing across between sections, 'About this guy' with his face and thought bubbles, 'A curious human intrigued by the world around him', a dates table 'Where's Trevor?', a quote, 'Books on the page' with books floating.
Preserve (3-5 traits): torn paper edges between sections; collage cut-outs floating; pink accent words; navy ground; thought-bubble props.
Borrow only (1-2): Use one physical material (torn paper) as every section transition
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: photo collage, cut-outs
Reject: Cookie panel in every frame
Token commitments: palette #1D243F, #BA9080, #DBD3CE, #765B5A; type Die Grotesk C, Die Grotesk B, Die Grotesk D; engine GSAP + Lenis linked (never vendored).
