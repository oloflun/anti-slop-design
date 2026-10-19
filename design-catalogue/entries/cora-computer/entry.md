---
title: "Cora - AI email assistant"
url: https://cora.computer/
source_url: https://cora.computer/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: painted-sky-to-field-saas
dna: "Email assistant x a painted journey from sky to golden fields with UI floating in it"
register: warm photographic
grammar: filmic one-shot
lane: "A product page painted like a landscape: 'Give Cora your inbox. Take back your life.' over a tablet UI among clouds, the page descends through sky and treetops ('Cora screens your email', 'Cora drafts responses in your voice') with UI windows floating, an envelope opens and cards fly out, the view lands on golden hills and a path ('Today's brief'), then 'Cora learns you inside and out', pricing in the grass and a dusk FAQ."
mode: persuade
traits: ["painted landscape as the page", "descent from sky to field", "UI windows floating in the scene", "envelope opening with cards", "serif headlines", "time of day changing"]
palette: ["#1689C1", "#FFFFFF", "#215369", "#BFCFD8", "#66ABCD"]
type: ["signifier", "switzer"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The scroll is a descent from sky to earth, with the product's screens placed in the landscape, so a SaaS pitch becomes a walk.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Place the product's UI inside a painted world the scroll descends through

## What to leave

- Pricing and FAQ break the painting

## Signature move

An envelope opening in the sky with brief cards flying out.

## Motion

Intro: the sky hero. Wheel (Lenis): clouds part and the view sinks; UI windows slide in and tilt; the envelope opens and cards fan; the hills rise; the light turns golden then dusk.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 1 video; smoothed scroll (median 120 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the filmic one-shot grammar: a product page painted like a landscape: 'Give Cora your inbox. Take back your life.' over a tablet UI among clouds, the page descends through sky and treetops ('Cora screens your email', 'Cora drafts responses in your voice') with UI windows floating, an envelope opens and cards fly out, the view lands on golden hills and a path ('Today's brief'), then 'Cora learns you inside and out', pricing in the grass and a dusk FAQ. Type: signifier, switzer.
Ground and ink from the measured palette (#1689C1, #FFFFFF, #215369). Motion carries the page through
an envelope opening in the sky with brief cards flying out. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — painted illustration, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: painted illustration, UI

## Reference lock

Primary reference/direction: Cora - AI email assistant — A product page painted like a landscape: 'Give Cora your inbox. Take back your life.' over a tablet UI among clouds, the page descends through sky and treetops ('Cora screens your email', 'Cora drafts responses in your voice') with UI windows floating, an envelope opens and cards fly out, the view lands on golden hills and a path ('Today's brief'), then 'Cora learns you inside and out', pricing in the grass and a dusk FAQ.
Preserve (3-5 traits): painted landscape as the page; descent from sky to field; UI windows floating in the scene; envelope opening with cards; serif headlines.
Borrow only (1-2): Place the product's UI inside a painted world the scroll descends through
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: painted illustration, UI
Reject: Pricing and FAQ break the painting
Token commitments: palette #1689C1, #FFFFFF, #215369, #BFCFD8, #66ABCD; type signifier, switzer; engine GSAP + Lenis linked (never vendored).
