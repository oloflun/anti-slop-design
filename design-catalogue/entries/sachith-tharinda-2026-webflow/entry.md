---
title: "Sachith Tharinda - Designer, Frontend Developer and Webflow Expert"
url: http://sachith-tharinda-2026.webflow.io/
source_url: http://sachith-tharinda-2026.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: badge-and-scribble-dev-folio
dna: "Webflow developer x hanging ID badge and condensed headline with scribbles"
register: modern clean
grammar: chaptered editorial
lane: "A developer folio: project cards flash through a loader with a counter, 'CODE BY SACHITH', then an ID badge on a lanyard swings down over the intro text, and a huge condensed line 'I craft digital experiences as a designer, frontend developer & Webflow expert' scrolls sideways with purple scribbles and 3D wire objects, a dark globe section, expertise cards and a blurred-project 'Let's work together'."
mode: persuade
traits: ["swinging ID badge on a lanyard", "sideways condensed headline", "hand-drawn purple scribbles", "3D wire objects", "counter loader with flashing project cards", "blurred background CTA"]
palette: ["#FFFFFF", "#000000", "#E4E2E4", "#858485", "#2C2C2C", "#565656"]
type: ["Haffer", "Schabo Condensed", "Fragment Mono", "Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The swinging badge introduces the person physically, and the scribbles make a long horizontal headline feel hand-annotated.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A swinging badge as the personal intro
- Scribble annotations under key words of a moving headline

## What to leave

- Generic expertise cards
- Very long sideways headline

## Signature move

An ID badge swinging on a lanyard over the intro text.

## Motion

Intro: black, project cards flash while a counter rises to 100, then 'CODE BY SACHITH' (~2 s). Wheel (Lenis ~110 px glide, 83 triggers): the badge drops and swings with inertia; the condensed headline slides sideways with scribbles drawing under words and wire objects spinning; the globe section rises; cards stack; the CTA fades over a blurred project. Barba transitions.

Measured (`motion/probe.json`): GSAP 3.14.1; 83 ScrollTriggers; Lenis; Barba page transitions; split text; smoothed scroll (median 116 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a developer folio: project cards flash through a loader with a counter, 'CODE BY SACHITH', then an ID badge on a lanyard swings down over the intro text, and a huge condensed line 'I craft digital experiences as a designer, frontend developer & Webflow expert' scrolls sideways with purple scribbles and 3D wire objects, a dark globe section, expertise cards and a blurred-project 'Let's work together'. Type: Haffer, Schabo Condensed, Fragment Mono, Inter.
Ground and ink from the measured palette (#FFFFFF, #000000, #E4E2E4). Motion carries the page through
an ID badge swinging on a lanyard over the intro text. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait badge, project screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait badge, project screenshots

## Reference lock

Primary reference/direction: Sachith Tharinda - Designer, Frontend Developer and Webflow Expert — A developer folio: project cards flash through a loader with a counter, 'CODE BY SACHITH', then an ID badge on a lanyard swings down over the intro text, and a huge condensed line 'I craft digital experiences as a designer, frontend developer & Webflow expert' scrolls sideways with purple scribbles and 3D wire objects, a dark globe section, expertise cards and a blurred-project 'Let's work together'.
Preserve (3-5 traits): swinging ID badge on a lanyard; sideways condensed headline; hand-drawn purple scribbles; 3D wire objects; counter loader with flashing project cards.
Borrow only (1-2): A swinging badge as the personal intro; Scribble annotations under key words of a moving headline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait badge, project screenshots
Reject: Generic expertise cards; Very long sideways headline
Token commitments: palette #FFFFFF, #000000, #E4E2E4, #858485, #2C2C2C, #565656; type Haffer, Schabo Condensed, Fragment Mono, Inter; engine GSAP + Lenis linked (never vendored).
