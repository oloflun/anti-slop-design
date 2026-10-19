---
title: "TheFinch - UI UX Design Agency"
url: https://thefinch.design/
source_url: https://thefinch.design/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: blue-glass-agency-saas
dna: "Indian UX agency x blue glass 3D shapes and a stacking card story"
register: modern clean
grammar: chaptered editorial
lane: "An agency: 'Crafting impactful visuals with AI-led UI UX design agency' on white, a white card that expands into a dark section with a laptop morphing in the middle of 'Outcome-driven UI UX for visionary leaders', question cards floating, blue light lines, 'Hire us' marquee, testimonials, blue glass 3D shapes beside services, and a lead form popup."
mode: persuade
traits: ["card expanding into a dark section", "object in the middle of a headline", "blue glass 3D shapes", "question cards floating", "blue light lines", "promo ticker bar"]
palette: ["#000000", "#FFFFFF", "#07209C", "#7E849C", "#D1D3D9", "#374986"]
type: ["Bw Gradual", "Lexend"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The card that expands from white to dark is a decent chapter change; otherwise conventional.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Expand a card into the next section's background

## What to leave

- Lead popup
- Generic agency sections

## Signature move

A white card expanding into a dark section with a laptop inside the headline.

## Motion

Intro: white hero. Wheel (ScrollSmoother, 4 pins): a card expands to full screen and turns dark; a laptop scales into the gap of the headline; question cards float up; blue lines draw; services slide with glass shapes rotating; the form popup appears.

Measured (`motion/probe.json`): GSAP 3.11.5; 50 ScrollTriggers; 4 pinned sections; ScrollSmoother; WebGL canvas x1 (three.js); 8 video; split text. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an agency: 'Crafting impactful visuals with AI-led UI UX design agency' on white, a white card that expands into a dark section with a laptop morphing in the middle of 'Outcome-driven UI UX for visionary leaders', question cards floating, blue light lines, 'Hire us' marquee, testimonials, blue glass 3D shapes beside services, and a lead form popup. Type: Bw Gradual, Lexend.
Ground and ink from the measured palette (#000000, #FFFFFF, #07209C). Motion carries the page through
a white card expanding into a dark section with a laptop inside the headline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D glass shapes, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D glass shapes, device mockups

## Reference lock

Primary reference/direction: TheFinch - UI UX Design Agency — An agency: 'Crafting impactful visuals with AI-led UI UX design agency' on white, a white card that expands into a dark section with a laptop morphing in the middle of 'Outcome-driven UI UX for visionary leaders', question cards floating, blue light lines, 'Hire us' marquee, testimonials, blue glass 3D shapes beside services, and a lead form popup.
Preserve (3-5 traits): card expanding into a dark section; object in the middle of a headline; blue glass 3D shapes; question cards floating; blue light lines.
Borrow only (1-2): Expand a card into the next section's background
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D glass shapes, device mockups
Reject: Lead popup; Generic agency sections
Token commitments: palette #000000, #FFFFFF, #07209C, #7E849C, #D1D3D9, #374986; type Bw Gradual, Lexend; engine GSAP + Lenis linked (never vendored).
