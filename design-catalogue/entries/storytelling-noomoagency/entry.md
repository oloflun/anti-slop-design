---
title: "Noomo — The Power of Digital Storytelling"
url: https://storytelling.noomoagency.com/
source_url: https://storytelling.noomoagency.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: iridescent-phoenix-story
dna: "Immersive agency manifesto x iridescent phoenix"
register: illustrated dark
grammar: filmic one-shot
lane: "A manifesto page that follows a phoenix: iridescent wings over a pastel halo as italic words (narrative, Light, Spirit) swell through, then the scene turns deep blue where a single flame-feather floats beside short principles, and ends with the phoenix in fire."
mode: experience
traits: ["iridescent 3D phoenix wings", "pastel halo ground turning to deep navy then amber", "italic serif words swelling", "single feather as a flame", "short principle lines"]
palette: ["#AFC6EE", "#9287E6", "#D2E1EF"]
type: ["TheSeasons", "TTNeoris"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

One creature carries the argument through three colour worlds (pastel dawn, blue night, fire), and single italic words swell across the screen between short sentences, so the manifesto reads like a title sequence.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Noomo Agency).

## What to borrow (principle)

- Carry a manifesto with one creature/object through changing colour worlds
- Swell single italic words across the screen as chapter beats

## What to leave

- Thin italic over bright halos is hard to read
- 38,000 px for a short text

## Signature move

An iridescent phoenix whose wings sweep through italic words, ending in fire.

## Motion

Intro: pastel lilac, a small mark morphs (~3 s), then 'The power of digital storytelling' with huge italic 'storytelling' over feathers. Scroll (ScrollSmoother, SplitText, WebGL): wings sweep around lines that set word by word; 'narrative', 'Light', 'Spirit', 'Soul' swell and fade; dark navy with a single burning feather beside principles; ice crystals with icons; phoenix in fire over 'Storytelling is what you see, feel, hear, interact with'; contact.

Measured (`motion/probe.json`): GSAP 3.13.0; ScrollSmoother; WebGL canvas x1 (three.js); split text; entry gate: x. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the filmic one-shot grammar: a manifesto page that follows a phoenix: iridescent wings over a pastel halo as italic words (narrative, Light, Spirit) swell through, then the scene turns deep blue where a single flame-feather floats beside short principles, and ends with the phoenix in fire. Type: TheSeasons, TTNeoris.
Ground and ink from the measured palette (#AFC6EE, #9287E6, #D2E1EF). Motion carries the page through
an iridescent phoenix whose wings sweep through italic words, ending in fire. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — iridescent 3D feathers and creature renders, halo light

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: iridescent 3D feathers and creature renders, halo light

## Reference lock

Primary reference/direction: Noomo — The Power of Digital Storytelling — A manifesto page that follows a phoenix: iridescent wings over a pastel halo as italic words (narrative, Light, Spirit) swell through, then the scene turns deep blue where a single flame-feather floats beside short principles, and ends with the phoenix in fire.
Preserve (3-5 traits): iridescent 3D phoenix wings; pastel halo ground turning to deep navy then amber; italic serif words swelling; single feather as a flame; short principle lines.
Borrow only (1-2): Carry a manifesto with one creature/object through changing colour worlds; Swell single italic words across the screen as chapter beats
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: iridescent 3D feathers and creature renders, halo light
Reject: Thin italic over bright halos is hard to read; 38,000 px for a short text
Token commitments: palette #AFC6EE, #9287E6, #D2E1EF; type TheSeasons, TTNeoris; engine GSAP + Lenis linked (never vendored).
