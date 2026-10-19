---
title: "A Love Story - branding agency"
url: https://alovehatestory.com/
source_url: https://alovehatestory.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: red-white-condensed-agency
dna: "Italian branding agency x red and white, condensed display with a letter circled, a billboard case and giant numerals"
register: other
grammar: chaptered editorial
lane: "A branding agency: 'A Love Story' with a heart on white, then huge on red, a billboard for a client photographed in a landscape sliding up through the red, manifesto in small Italian, services as condensed titles with one letter in a circle ('Disruptive br(a)nding', 'Corporate we(b)site', 'Advertising 'n (c)onsulting') each with an image that pops up, a project strip, and giant numerals (99, 70, 48) with signatures and ghost words."
mode: persuade
traits: ["condensed display caps", "one letter circled per title", "red and white alternation", "billboard case photo", "giant numerals with signature"]
palette: ["#F8F8F8", "#8EA6C3", "#C8191B", "#7B756E", "#752721"]
type: ["Instrument Serif", "Anton", "Instrument Serif Placeholder", "Anton Placeholder"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Circling one letter in every service name is a tiny, repeatable mark that turns a services list into an identity.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: A Love Story).

## What to borrow (principle)

- Mark one letter per title as a repeatable signature

## What to leave

- Small Italian body copy

## Signature move

'Disruptive br(a)nding' with the a in a circle.

## Motion

Intro: heart and title on white, wipe to red (~2 s). Wheel (Lenis): the billboard slides up; titles reveal by line; images pop; numerals scale.

Measured (`motion/probe.json`): Lenis; split text; smoothed scroll (median 94 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a branding agency: 'A Love Story' with a heart on white, then huge on red, a billboard for a client photographed in a landscape sliding up through the red, manifesto in small Italian, services as condensed titles with one letter in a circle ('Disruptive br(a)nding', 'Corporate we(b)site', 'Advertising 'n (c)onsulting') each with an image that pops up, a project strip, and giant numerals (99, 70, 48) with signatures and ghost words. Type: Instrument Serif, Anton, Instrument Serif Placeholder, Anton Placeholder.
Ground and ink from the measured palette (#F8F8F8, #8EA6C3, #C8191B). Motion carries the page through
'Disruptive br(a)nding' with the a in a circle. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign photography

## Reference lock

Primary reference/direction: A Love Story - branding agency — A branding agency: 'A Love Story' with a heart on white, then huge on red, a billboard for a client photographed in a landscape sliding up through the red, manifesto in small Italian, services as condensed titles with one letter in a circle ('Disruptive br(a)nding', 'Corporate we(b)site', 'Advertising 'n (c)onsulting') each with an image that pops up, a project strip, and giant numerals (99, 70, 48) with signatures and ghost words.
Preserve (3-5 traits): condensed display caps; one letter circled per title; red and white alternation; billboard case photo; giant numerals with signature.
Borrow only (1-2): Mark one letter per title as a repeatable signature
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign photography
Reject: Small Italian body copy
Token commitments: palette #F8F8F8, #8EA6C3, #C8191B, #7B756E, #752721; type Instrument Serif, Anton, Instrument Serif Placeholder, Anton Placeholder; engine GSAP + Lenis linked (never vendored).
