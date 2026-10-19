---
title: "Inertia Studios - CGI, Animation and Design"
url: https://www.weareinertia.com/
source_url: https://www.weareinertia.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "consumer-brand"
family: cgi-studio-letter-window
dna: "London CGI studio x wordmark letters as windows onto renders"
register: modern clean
grammar: chaptered editorial
lane: "A CGI studio on white: a black intro, then 'INERTIA STUDIOS' with a render showing through a letter cut-out; scrolling swaps the render inside one giant letter (I, U, T) before a 'Featured projects / Case studies' marquee, an offset grid of product CGI, a centred manifesto, client logos, 3D billboard showreel, an Ideas in Motion news list and a contact block."
mode: persuade
traits: ["single giant letter as a window onto renders", "swiss sans uppercase on white", "marquee section label", "offset two-column project grid", "anamorphic billboard renders", "corner bracket arrow CTA"]
palette: ["#FFFFFF", "#101516", "#93877A", "#86AFAA", "#556D6F", "#473B34"]
type: ["Neue"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Putting each render inside one letter of the name makes the studio's work and its brand the same object, and the white page lets saturated CGI do all the colour.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Okey Studio).

## What to borrow (principle)

- Use a letter of the wordmark as the mask for the work
- Keep the page white and let renders bring the colour

## What to leave

- Very small nav and metadata
- Generic news list

## Signature move

Product renders seen through a single giant letter of the studio name.

## Motion

Intro: black, 'INERTIA STUDIOS' and a tagline fade in grey, then the page flips to white with the wordmark split around a render (~2 s). Wheel (ScrollSmoother, 1 pin): the hero pins while the render inside the letter mask changes from shoes to an abstract blob to a blue device to moss; the mask then opens to a full-width marquee; project tiles drift at different speeds; the billboard reel scales up; the contact block arrives with a drawn corner bracket.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; ScrollSmoother; 6 video. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a CGI studio on white: a black intro, then 'INERTIA STUDIOS' with a render showing through a letter cut-out; scrolling swaps the render inside one giant letter (I, U, T) before a 'Featured projects / Case studies' marquee, an offset grid of product CGI, a centred manifesto, client logos, 3D billboard showreel, an Ideas in Motion news list and a contact block. Type: Neue.
Ground and ink from the measured palette (#FFFFFF, #101516, #93877A). Motion carries the page through
product renders seen through a single giant letter of the studio name. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product CGI, anamorphic billboard renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product CGI, anamorphic billboard renders

## Reference lock

Primary reference/direction: Inertia Studios - CGI, Animation and Design — A CGI studio on white: a black intro, then 'INERTIA STUDIOS' with a render showing through a letter cut-out; scrolling swaps the render inside one giant letter (I, U, T) before a 'Featured projects / Case studies' marquee, an offset grid of product CGI, a centred manifesto, client logos, 3D billboard showreel, an Ideas in Motion news list and a contact block.
Preserve (3-5 traits): single giant letter as a window onto renders; swiss sans uppercase on white; marquee section label; offset two-column project grid; anamorphic billboard renders.
Borrow only (1-2): Use a letter of the wordmark as the mask for the work; Keep the page white and let renders bring the colour
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product CGI, anamorphic billboard renders
Reject: Very small nav and metadata; Generic news list
Token commitments: palette #FFFFFF, #101516, #93877A, #86AFAA, #556D6F, #473B34; type Neue; engine GSAP + Lenis linked (never vendored).
