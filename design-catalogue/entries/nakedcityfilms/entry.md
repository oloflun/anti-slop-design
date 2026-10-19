---
title: "Naked City Films"
url: https://nakedcityfilms.com/
source_url: https://nakedcityfilms.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: production-blue-block-reel
dna: "New York production company x electric blue blocks and highlighted italic phrases"
register: cinematic dark
grammar: chaptered editorial
lane: "A production company: a blue block grows on grey, the 'NKD CITY' logo card sits over full-bleed footage, the card shrinks into a light statement with italic serif phrases highlighted in blue, then a navy grid of project stills where hovered titles turn blue, a blue 'What's moving us' block, talent cards and a 'Have a story to tell?' footer with a giant logo."
mode: persuade
traits: ["electric blue as a highlighter", "logo card over full-bleed footage", "italic serif phrases highlighted", "navy project grid", "talent cards with italic tags", "giant split logo footer"]
palette: ["#E7E7E7", "#060615", "#6F6051", "#AFA48E", "#32373C", "#0D0E65"]
type: ["Haas Grotesk Medium", "TRJNDaVinci Medium Trial Italic"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The blue block is the material of the whole site: it is the loader, the logo, the highlight behind phrases and the footer, so every transition is the same blue moving.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: SavoirFaire).

## What to borrow (principle)

- One accent colour used as a physical block that moves
- Highlight italic phrases inside a statement

## What to leave

- Very small project captions
- Grey loading placeholders in frames

## Signature move

An electric blue block that grows into the logo and highlights phrases across the page.

## Motion

Intro: grey with a blue square growing (~1.5 s), then footage behind the logo card. Wheel (ScrollSmoother): the logo card shrinks and the footage slides away; the statement types in with blue highlight boxes sweeping behind italic phrases; the project grid drifts with parallax per column; a blue panel rises for the dispatch section; the footer logo splits across the width.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x1 (three.js); 19 video. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a production company: a blue block grows on grey, the 'NKD CITY' logo card sits over full-bleed footage, the card shrinks into a light statement with italic serif phrases highlighted in blue, then a navy grid of project stills where hovered titles turn blue, a blue 'What's moving us' block, talent cards and a 'Have a story to tell?' footer with a giant logo. Type: Haas Grotesk Medium, TRJNDaVinci Medium Trial Italic.
Ground and ink from the measured palette (#E7E7E7, #060615, #6F6051). Motion carries the page through
an electric blue block that grows into the logo and highlights phrases across the page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial and documentary film stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial and documentary film stills

## Reference lock

Primary reference/direction: Naked City Films — A production company: a blue block grows on grey, the 'NKD CITY' logo card sits over full-bleed footage, the card shrinks into a light statement with italic serif phrases highlighted in blue, then a navy grid of project stills where hovered titles turn blue, a blue 'What's moving us' block, talent cards and a 'Have a story to tell?' footer with a giant logo.
Preserve (3-5 traits): electric blue as a highlighter; logo card over full-bleed footage; italic serif phrases highlighted; navy project grid; talent cards with italic tags.
Borrow only (1-2): One accent colour used as a physical block that moves; Highlight italic phrases inside a statement
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial and documentary film stills
Reject: Very small project captions; Grey loading placeholders in frames
Token commitments: palette #E7E7E7, #060615, #6F6051, #AFA48E, #32373C, #0D0E65; type Haas Grotesk Medium, TRJNDaVinci Medium Trial Italic; engine GSAP + Lenis linked (never vendored).
