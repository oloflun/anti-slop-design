---
title: "NURA (planner template)"
url: https://nura-ai.framer.website/
source_url: https://nura-ai.framer.website/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/3ec3c18c594acd2e-screenshot.webp
category: product-focused
category2: ""
family: meadow-planner
dna: "Lifestyle photography x task-planner app pitch"
register: warm photographic
grammar: none
lane: "Full-bleed lifestyle photography of a woman in a flower field carries the entire pitch for a task planner that never shows its own interface, closing on a bare stat strip"
mode: persuade
traits: ["full-bleed lifestyle photography", "roman + italic serif headline pairing", "pill CTA on photo", "zero product screenshots", "light grey feature panel", "second flower-field photo mid-page", "bare inline stat strip", "generic planner copy"]
palette: ["#A9C9DE", "#E8A9C0", "#6B8F5A", "#FFFFFF", "#1A1A1A", "#F5F5F3"]
type: ["Inter Display", "Instrument Serif"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The page borrows wholesale from wellness/lifestyle-app photography: a full-bleed
portrait of a woman in a flower field, warm sunlight, soft focus, with the
headline set directly onto it in white — roman weight for most of the sentence,
italic serif for the emotional word ("a *better plan*"). That's a legible,
low-effort way to signal "calm, human, aspirational" for a task-planning tool
without building any product-specific imagery.

Below the fold, a light grey panel restates the pitch in plain prose ("You don't
need more tasks — you need a clear direction") next to a second, closer crop of
the same photographic subject. The repetition of the model across two hero-style
images, with no interface shown between them, is the page's most telling choice —
this is a productivity product whose entire visual argument is a lifestyle photo
shoot, not a demonstration of the thing it does.

A bare inline stat strip at the bottom ("Tasks organized in 2.4s // 8 tasks
organized / Priorities ranked automatically") gestures at product proof without
ever showing the product. It's the visual language of a SaaS landing page grafted
onto a wellness photo shoot, and the seam between the two is visible.

## What to borrow (principle)

- **Pair a roman headline with one italic-serif word** for warmth without
  switching to a full serif system — it's a lightweight way to add an emotional
  register to an otherwise plain sans headline.
- **Use a bare, unboxed stat strip** as a lightweight proof device when you don't
  want a full metrics dashboard.

## What to leave

- Selling a software product entirely through lifestyle photography, with no
  screenshot, mockup, or UI shown anywhere on the page — a planner app's core
  claim (that it organizes your day) is never demonstrated, only asserted.
- Repeating the same photographic subject across two hero-scale images reads as
  a stock-photo budget of one shoot, not a considered art direction.
- The bare stat strip has no visual container or hierarchy, so it reads as an
  afterthought rather than proof.

## Signature move

The photograph-only pitch: two full-bleed lifestyle shots of the same subject
carrying the entire emotional argument for a productivity tool, with the product
itself never shown. It's a shortcut that works for tone and fails for
credibility — the reviewer's honest tell that this is a template, not a shipped
product.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed,
though the captured CSS is thin — a single `400ms` duration token and one
custom ease (`cubic-bezier(0.44,0,0.56,1)`, a near-symmetric ease-in-out) drive
link/underline colour transitions; the only keyframe is a generic loading
spinner, unrelated to content. That's consistent with a photography-only page:
there's little UI to animate, so what little motion exists is confined to
text-link state changes rather than any scroll-triggered reveal of the hero
or stat strip.

| token | value | role |
|---|---|---|
| `md` | 400ms | link/underline colour transitions |
| custom | `cubic-bezier(0.44,0,0.56,1)` | only easing found (2 uses) |

## Brief

If borrowing this direction, treat the photography as tone-setting only — pair it
with at least one real product screenshot before asking a visitor to trust a
planning tool. Open on a full-bleed lifestyle photograph with a roman + one-word
italic-serif headline in white, a single pill CTA. Follow with a light grey
feature panel pairing plain-prose copy against a second, tighter crop of the same
photographic world. Close with an inline, unboxed stat strip — but back it with
an actual screenshot earlier in the scroll, which this reference omits.

## Image recipe

A person in [SUBJECT] — a flower field, golden hour, soft warm light, shallow
depth of field, genuine unposed expression — shot documentary-style, no visible
product or device, colour graded warm and slightly hazy.

## Photo search

Unsplash first, Pexels second.
- "woman flower field golden hour candid"
- "sun flare portrait outdoor warm"
- "wildflower meadow lifestyle photography"

## Reference lock

Primary reference/direction: NURA — lifestyle-photography-only pitch for a task planner, no product screenshot shown.
Preserve (3-5 traits): full-bleed warm lifestyle photography as the primary visual device; roman headline with one italic-serif emotional word; single pill CTA set directly on the photograph; bare, unboxed stat strip as a lightweight proof device.
Borrow only (1-2): the light grey plain-prose feature panel; the repeated photographic subject across two hero-scale images.
Role rules: never claim organizational/product proof without showing the product at least once; italic serif reserved for one word per headline only.
Media strategy: photo:unsplash — warm, candid lifestyle photography only; must be paired with at least one real UI screenshot elsewhere on the page to avoid an all-photography pitch.
Reject: shipping a software marketing page with zero product screenshots; an unboxed stat strip with no supporting visual proof nearby.
Token commitments: sky `#A9C9DE`, blossom `#E8A9C0`, foliage `#6B8F5A`, white `#FFFFFF`, ink `#1A1A1A`, panel-grey `#F5F5F3`; sans for headline body, italic serif for one emphasis word only.
