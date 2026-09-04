---
title: "Mattis Studio (agency template)"
url: https://mattis.framer.website/
source_url: https://mattis.framer.website/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/bd32f41ebcc487db-screenshot-upload.webp
category: portfolio
category2: ""
family: grid-boxed-console-agency
dna: "Software changelog framing x design/dev agency pitch"
register: cinematic dark
grammar: split stage
lane: "A black hero framed like a software console — version tag, live clock, slot counter — opens the page, then a single orange full-bleed block states the studio's thesis beside a fashion photograph, closing on plain grey display type"
mode: persuade
traits: ["grid-boxed console-style hero framing", "version-number tag", "live local-time clock", "availability slot counter", "founder signature overlay", "bold orange full-bleed thesis block", "fashion-editorial photography", "oversized flat-colour headline blocks", "condensed bold sans display"]
palette: ["#0B0B0B", "#F04E23", "#FFFFFF", "#E7E5E1", "#1C1C1C"]
type: ["Geist"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The hero borrows interface language from software, not marketing: a
`(EST. 2019 — VERSION 1.0.4)` tag, a corner-marked grid frame around the
wordmark card, a live local-time readout, and an availability counter
("Slots for APR: |||||  2 left"). None of this is a real product — it's an
agency's own homepage — but framing the studio itself as a versioned, in-stock
piece of software borrows urgency and precision language from a different
category entirely.

A founder photo and signature sit inside the same framed card as the wordmark,
which personalises what would otherwise be a purely systemic, cold hero. It's a
small human anchor inside a page that otherwise leans hard on grid lines,
timestamps and version numbers.

The page then commits fully to one flat, saturated orange for an entire
full-bleed section — a bold three-word thesis ("STRATEGY BEFORE PIXELS.") set
in huge condensed type beside a black-and-white fashion-editorial photograph
and a single stat ("12+ Industries"). The colour block does more branding work
in one screen than a logo could, simply by being the loudest, most confident
thing on the page.

## What to borrow (principle)

- **Frame your own homepage like a software product**, with a version tag, a
  live clock, and an availability counter, to borrow precision and urgency
  language from a different category.
- **Put a founder photo and signature inside the hero's framed card**, not in a
  separate "about" section, to personalise an otherwise systemic layout.
- **Commit an entire section to one flat saturated colour** for your core thesis
  statement — it reads as more confident than a colour used sparingly.
- **Pair a black-and-white editorial photograph against a saturated colour
  block** rather than a colour photograph, so the photo and the colour don't
  compete.

## What to leave

- A "slots left this month" counter is a scarcity device borrowed from
  consumer/booking products; for a design agency it can read as a gimmick
  unless the scarcity is genuinely real and updated.
- The console-style hero (version tag, clock, grid frame) is dense with small
  metadata that risks distracting from the actual value proposition on first
  glance — it rewards a second look more than a first one.

## Signature move

The versioned, grid-framed hero card: the studio's name and pitch live inside a
bordered card with corner marks (like a UI component being inspected),
carrying a version number, a founder signature, and a live clock — treating the
agency's own brand as a piece of software with a release history.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed,
though the captured CSS is thin: a `200ms` custom ease
(`cubic-bezier(0.44,0,0.56,1)`, a near-symmetric ease-in-out, 15 uses) drives
link/underline colour changes, plus the framework's `1ms` allow-discrete
overflow transition. The one keyframe present is a generic loading spinner —
no clock-tick or card-select animation was captured, so that read from the
image stays inferred rather than confirmed.

| token | value | role |
|---|---|---|
| `instant` | 1ms | framework overflow transition |
| `sm` | 200ms | link/underline colour changes |
| custom | `cubic-bezier(0.44,0,0.56,1)` | only family found (15 uses) |

## Brief

Build a dark, systems-minded agency homepage. Frame the hero as a bordered card
with corner marks, a version tag, a live local-time clock, and an availability
counter, with the founder's photo and signature inside the same card. Set the
studio name in a large bold wordmark within that frame. Immediately after,
commit one full-bleed section to a single flat saturated colour carrying a
three-to-five-word thesis statement in huge condensed type, paired with one
black-and-white editorial photograph and a single stat. Close on plain,
oversized display type stating what the studio actually builds.

## Image recipe

Black-and-white editorial fashion photograph of [SUBJECT], studio-lit, high
contrast, one figure in three-quarter or profile pose against a plain
background, shot to read as confident and slightly detached rather than warm
or candid.

## Photo search

Unsplash first, Pexels second.
- "black and white fashion editorial studio"
- "monochrome portrait high contrast studio"
- "editorial fashion photography plain background"

## Reference lock

Primary reference/direction: Mattis Studio — versioned software-style hero card with a founder signature, breaking into one flat-colour thesis block with black-and-white editorial photography.
Preserve (3-5 traits): hero framed as a bordered, corner-marked card carrying a version tag and live clock; founder photo and signature placed inside that same card, not a separate section; one full-bleed section committed entirely to a single flat saturated colour for the core thesis; black-and-white (not colour) photography paired against the saturated colour block.
Borrow only (1-2): the "slots left this month" availability counter, used only if genuinely accurate; the single stat paired with the thesis block.
Role rules: only one saturated flat-colour section per page; photography stays black-and-white wherever it meets a saturated colour block; version/clock metadata stays confined to the hero card, never repeated elsewhere.
Media strategy: photo:unsplash — black-and-white editorial/fashion photography only where paired with the saturated colour block; no colour photography elsewhere on the page.
Reject: a fabricated scarcity counter that doesn't reflect real availability; colour photography competing against the flat saturated section; a hero card with no personal/human element.
Token commitments: black `#0B0B0B`, orange `#F04E23`, white `#FFFFFF`, grey `#E7E5E1`, dark-grey `#1C1C1C`; condensed bold sans for all display type.
