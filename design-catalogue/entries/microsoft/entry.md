---
title: "Windows 11 - Microsoft"
url: https://www.microsoft.com/en-us/windows
source_url: https://www.microsoft.com/en-us/windows
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: os-glass-window-sky
dna: "Operating system x a glass Windows logo in a sky that opens into app windows"
register: modern clean
grammar: filmic one-shot
lane: "A product page: 'It starts on Windows' over a blue sky with a glass four-pane logo, the logo panes flying apart and becoming app windows (Snap layouts, a document, Copilot in Excel, a Forza game) as the sky shifts from blue to pink to night, a single pane shrinking into the logo again, 'The Windows difference', 'Say hello to security' with a smiley, PC cards, stories and FAQ."
mode: persuade
traits: ["glass logo in a sky", "logo panes becoming app windows", "sky colour shifting per section", "caption card bottom left", "dark lower sections"]
palette: ["#172133", "#77A8D9", "#37405C", "#4187C9", "#9096C6", "#5D5C84"]
type: []
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The logo literally becomes the windows of the product, so the brand mark and the product demo are one object.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: OFF+BRAND).

## What to borrow (principle)

- Break the logo into panes that become the product's UI

## What to leave

- Conventional lower half
- Cookie banner

## Signature move

Glass Windows logo panes flying apart into app windows in a sky.

## Motion

Intro: the sky with the glass logo. Wheel (Lenis, pinned): panes drift apart and turn into windows; content swaps on each; the sky shifts blue to pink to night; one pane collapses back into the logo; lower sections fade up.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1; 9 video; smoothed scroll (median 137 px still travelling after input stops); entry gate: Reject, Discover Windows. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the filmic one-shot grammar: a product page: 'It starts on Windows' over a blue sky with a glass four-pane logo, the logo panes flying apart and becoming app windows (Snap layouts, a document, Copilot in Excel, a Forza game) as the sky shifts from blue to pink to night, a single pane shrinking into the logo again, 'The Windows difference', 'Say hello to security' with a smiley, PC cards, stories and FAQ. Type: read from the captures.
Ground and ink from the measured palette (#172133, #77A8D9, #37405C). Motion carries the page through
glass Windows logo panes flying apart into app windows in a sky. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D glass, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D glass, UI

## Reference lock

Primary reference/direction: Windows 11 - Microsoft — A product page: 'It starts on Windows' over a blue sky with a glass four-pane logo, the logo panes flying apart and becoming app windows (Snap layouts, a document, Copilot in Excel, a Forza game) as the sky shifts from blue to pink to night, a single pane shrinking into the logo again, 'The Windows difference', 'Say hello to security' with a smiley, PC cards, stories and FAQ.
Preserve (3-5 traits): glass logo in a sky; logo panes becoming app windows; sky colour shifting per section; caption card bottom left; dark lower sections.
Borrow only (1-2): Break the logo into panes that become the product's UI
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D glass, UI
Reject: Conventional lower half; Cookie banner
Token commitments: palette #172133, #77A8D9, #37405C, #4187C9, #9096C6, #5D5C84; type -; engine GSAP + Lenis linked (never vendored).
