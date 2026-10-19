---
title: "Childless - Wege zur Lebensfreude"
url: https://www.childless.ch/
source_url: https://www.childless.ch/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: quiet-serif-counselling
dna: "Counselling for unfulfilled wish for children x thin serif and soft forest photography"
register: warm photographic
grammar: chaptered editorial
lane: "A counselling practice in German: a small logo loader, 'Unerfüllter Kinderwunsch' in thin serif over a misty forest with birds, the founder's story in centred serif lines, three offering cards over hills, testimonials, a full-bleed tree canopy with offer cards rising over it, FAQ and a contact with a portrait."
mode: read
traits: ["thin serif type", "misty forest photography", "centred serif statements", "offer cards over landscape", "cards rising over a canopy photo", "quiet off-white ground"]
palette: ["#FDFDFD", "#31352C", "#E8E6E1", "#9B998D"]
type: ["Abcwhyte", "Merchant"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Restraint suits the subject: soft nature images and calm serif lines, with gentle card movement and nothing loud.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Keep motion gentle and slow for a sensitive subject

## What to leave

- Very small card text

## Signature move

Birds over a misty forest under 'Unerfüllter Kinderwunsch'.

## Motion

Intro: white with a logo that sharpens (~1.5 s). Wheel (8 triggers): the photo scales to full width; statements fade up; cards rise; on the canopy, offer cards slide up one over another.

Measured (`motion/probe.json`): GSAP 3.12.7; 8 ScrollTriggers; 1 pinned sections; Lenis; Swup page transitions; smoothed scroll (median 138 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a counselling practice in German: a small logo loader, 'Unerfüllter Kinderwunsch' in thin serif over a misty forest with birds, the founder's story in centred serif lines, three offering cards over hills, testimonials, a full-bleed tree canopy with offer cards rising over it, FAQ and a contact with a portrait. Type: Abcwhyte, Merchant.
Ground and ink from the measured palette (#FDFDFD, #31352C, #E8E6E1). Motion carries the page through
birds over a misty forest under 'Unerfüllter Kinderwunsch'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — nature photography, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: nature photography, portrait

## Reference lock

Primary reference/direction: Childless - Wege zur Lebensfreude — A counselling practice in German: a small logo loader, 'Unerfüllter Kinderwunsch' in thin serif over a misty forest with birds, the founder's story in centred serif lines, three offering cards over hills, testimonials, a full-bleed tree canopy with offer cards rising over it, FAQ and a contact with a portrait.
Preserve (3-5 traits): thin serif type; misty forest photography; centred serif statements; offer cards over landscape; cards rising over a canopy photo.
Borrow only (1-2): Keep motion gentle and slow for a sensitive subject
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: nature photography, portrait
Reject: Very small card text
Token commitments: palette #FDFDFD, #31352C, #E8E6E1, #9B998D; type Abcwhyte, Merchant; engine GSAP + Lenis linked (never vendored).
