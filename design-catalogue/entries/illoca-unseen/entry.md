---
title: "Illoca"
url: https://illoca.unseen.co/
source_url: https://illoca.unseen.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: two-tone-3d-workspace-product
dna: "AI architecture tool x two-tone 3D illustration"
register: illustrated dark
grammar: filmic one-shot
lane: "A product page that is one continuous 3D camera move through a two-tone blue-and-sand illustrated studio: from a city window down to an architect's desk, where the sketch on the paper turns into the product's floor plan."
mode: persuade
traits: ["two-colour 3D scene (ultramarine + sand)", "scroll drives a single camera move", "logo-mark preloader", "feature title slides in beside the frame", "sketch-to-plan transformation on the desk", "grotesque headline over the scene"]
palette: ["#E7DDC7", "#0249B0", "#B7B4AD", "#3F5F91", "#87909D"]
type: ["Geist Mono", "F37 Analog", "Graphik Web", "Architect Pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The product (AI that turns sketches into plans) is shown by a camera, not a screenshot: the wheel dollies from the room to the hands to the paper, and the sketch on the desk resolves into a plan. Two flat colours keep a 3D scene graphic, and the whole page is one shot, so every feature arrives as the next thing the camera reaches.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Unseen Studio, Unseen Studio®).

## What to borrow (principle)

- Show a tool's result happening inside a scene rather than as a UI screenshot
- Map the wheel to one continuous camera path; features are stops on it
- Restrict a 3D scene to two flat colours so it reads as illustration

## What to leave

- Virtual scroll with no visible progress
- The scene frame crops the headline on the way in

## Signature move

A scroll-driven camera that travels into the drawing on the architect's desk, where the sketch becomes a floor plan.

## Motion

Intro: logo mark on sand, headline 'Design at the speed of thought' and the scene window rise in (~2.5 s). Scroll (virtual, 6 pinned stages, WebGL): the scene frame grows to fill the page; the camera dollies over the architect's shoulder down to the desk; the frame shifts right as 'Augmented Sketch' slides in on the left; the sketch lines on the paper redraw as a plan with markers. SplitText on headings.

Measured (`motion/probe.json`): GSAP 3.15.0; 6 pinned sections; Lenis; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the filmic one-shot grammar: a product page that is one continuous 3D camera move through a two-tone blue-and-sand illustrated studio: from a city window down to an architect's desk, where the sketch on the paper turns into the product's floor plan. Type: Geist Mono, F37 Analog, Graphik Web, Architect Pro.
Ground and ink from the measured palette (#E7DDC7, #0249B0, #B7B4AD). Motion carries the page through
a scroll-driven camera that travels into the drawing on the architect's desk, where the sketch becomes a floor plan. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — two-tone 3D illustration of the user at work, one saturated hue plus one neutral

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: two-tone 3D illustration of the user at work, one saturated hue plus one neutral

## Reference lock

Primary reference/direction: Illoca — A product page that is one continuous 3D camera move through a two-tone blue-and-sand illustrated studio: from a city window down to an architect's desk, where the sketch on the paper turns into the product's floor plan.
Preserve (3-5 traits): two-colour 3D scene (ultramarine + sand); scroll drives a single camera move; logo-mark preloader; feature title slides in beside the frame; sketch-to-plan transformation on the desk.
Borrow only (1-2): Show a tool's result happening inside a scene rather than as a UI screenshot; Map the wheel to one continuous camera path; features are stops on it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: two-tone 3D illustration of the user at work, one saturated hue plus one neutral
Reject: Virtual scroll with no visible progress; The scene frame crops the headline on the way in
Token commitments: palette #E7DDC7, #0249B0, #B7B4AD, #3F5F91, #87909D; type Geist Mono, F37 Analog, Graphik Web, Architect Pro; engine GSAP + Lenis linked (never vendored).
