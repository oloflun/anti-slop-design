---
title: "Shelby Kay"
url: https://shelbykay.dev/
source_url: https://shelbykay.dev/
captured: 2026-09-04
origin: refero
extract: ok
category: portfolio
category2: editorial
family: linen-wordmark-botanical
dna: "265px edge-to-edge wordmark x low-opacity botanical greenhouse atmosphere"
register: editorial print
grammar: typographic poster
lane: "A warm linen canvas holds a 265px sage wordmark stretched to the viewport edge over a barely-visible botanical photograph, with a rotated surname running down the right margin and a text-only bottom nav — no button, no shadow, no rounded corner anywhere on the page"
mode: portfolio
traits: ["26x type-scale ratio (265px to 10px)", "two-colour ink system, olive + sage only", "0px radius everywhere, zero elevation", "botanical photography at 10-15% opacity", "rotated 90° side label as running header", "tonal section shifts, cream to tan to taupe"]
palette: ["#393c2a", "#737955", "#efe6d9", "#d6b292", "#afa199", "#7b8785"]
type: ["Ranade", "Switzer"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Shelby Kay.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the
live capture — the second image shows the work-grid page in the same system.
The palette is genuinely two brand colours only: olive ink `#393c2a` for
structure (all text, all borders) and sage `#737955` reserved exclusively for
display headings, used "sparingly — one display element per section maximum."
Everything else (sienna, driftwood, riverstone) is a tonal surface shift, not
a third brand colour, so the system reads as disciplined even though four
warm neutrals are in play.

Typography runs an extreme, stated ratio: Ranade at 265px for the wordmark
against Switzer at 10px for metadata is a 26× scale jump, and the source is
explicit that hierarchy comes from "size alone, never by color or weight
variation within a single element type." Ranade appears only at weight 400 —
"the weight is light but the size is monumental, creating authority through
scale not boldness" — while Switzer's 500-700 range handles every functional
role beneath it.

Zero radius and zero elevation are absolute: the source states cards sit
directly on their section surface "with a hairline border or none at all —
the printed-page metaphor forbids digital lift." Botanical photography is
demoted to a 10-15% opacity atmospheric layer rather than a subject, and
section transitions happen through tonal surface shifts (linen → sienna →
driftwood) rather than hard dividers — the whole page behaves as a sequence of
warm paper stock rather than a stack of digital panels.

## What to borrow (principle)

- **Restrict a workhorse brand colour to display headings only.** Sage
  appearing exclusively on large type (never body, never UI) keeps a second
  brand colour from diluting the olive structural ink.
- **State the type-scale ratio as a number, not a feeling.** A declared 26×
  jump between wordmark and metadata size is a concrete, repeatable rule for
  scale-driven hierarchy.
- **Demote photography to atmosphere at a stated opacity.** 10-15% opacity
  botanical photography reads as ambient texture rather than competing
  content — an explicit percentage is more portable than "subtle."
- **Shift tone instead of adding dividers between sections.** Warm surface
  layering (cream → tan → taupe) can do a divider's job with none of a
  divider's visual noise.
- **Rotate a secondary wordmark fragment to the margin.** Splitting a two-word
  brand name (SHELBY / KAY) across the hero and a rotated side label creates a
  spatial device unique to that one name, not a repeatable pattern.

## What to leave

- A 26× type-scale ratio with zero intermediate steps is an extreme
  commitment — any content that doesn't fit cleanly into "monumental
  wordmark" or "whisper metadata" has nowhere natural to sit.
- Zero border-radius everywhere, including on photography, is a hard
  constraint that will visibly clash with any borrowed component using even a
  subtle rounded corner.
- Sage's 3.7:1 contrast on linen fails body-text readability by the source's
  own admission — the colour is usable only at display scale, which limits
  how much of the page can actually carry the brand's "voice" colour.

## Signature move

The rotated surname running header: "KAY" set in Ranade at 83-158px, rotated
90° counter-clockwise and pinned flush to the right viewport edge — a second
half of the wordmark functioning as a persistent spatial anchor independent of
the horizontal "SHELBY" hero text.

## Motion

(from designlang extract) Feel reads as responsive, and the page is
scroll-linked — correcting the earlier "no motion tokens" read: this is a
Svelte-built site with a genuine, fairly heavily-used transition system. Two
easing families cover most of it — a custom `cubic-bezier(0.76, 0, 0.24, 1)`
(29 uses) and a fast-settling ease-out `cubic-bezier(0.165, 0.84, 0.44, 1)` (72
uses, the dominant curve) — across five duration steps from 100ms up to a slow
1.25s. The one keyframe confirmed firing, `svelte-tz8cmd-fadeIn`, is Svelte's
own generated opacity-fade transition class (1 use) rather than a bespoke
animation — consistent with simple mount/route fades, not choreographed
reveals. (observed in capture) given the explicitly print-metaphor,
zero-elevation register, hover states most plausibly still apply only the
documented underline/border treatment on nav links, riding that same
fast ease-out curve rather than introducing new motion language.

| Token | Value | Easing |
|---|---|---|
| xs | 100ms | ease-out family |
| md | 400ms | ease-out family |
| lg | 500ms | custom `cubic-bezier(0.76, 0, 0.24, 1)` |
| xl | 1.2s | custom `cubic-bezier(0.76, 0, 0.24, 1)` |
| xxl | 1.25s | custom `cubic-bezier(0.76, 0, 0.24, 1)` |

## Brief

Build a botanical-editorial personal portfolio. Canvas is linen `#efe6d9`;
olive ink `#393c2a` carries all text, borders and structural strokes; sage
`#737955` is reserved exclusively for the wordmark and section-anchor display
text, never body or UI. Set the hero wordmark in Ranade weight 400 at up to
265px, stretched edge-to-edge, over a botanical photograph at 10-15% opacity.
Add a rotated 90° secondary wordmark fragment pinned to the right margin at
83-158px. Use Switzer weight 500-700 for absolutely everything else — nav,
metadata, labels — at 10-20px, with a compact editorial voice. Ban border-
radius entirely: cards, images and tags all sit at 0px with no shadow, only a
hairline border or none. Shift section backgrounds through warm tonal layers
(linen → sienna → driftwood → riverstone) instead of hard dividers. Build the
work grid as full-bleed images with a rotated date-stamp in one corner and a
centred two-letter label below — no card chrome. Keep navigation text-only,
positioned at the page edges, with no buttons anywhere on the site.

## Image recipe

Atmospheric botanical photograph of [SUBJECT] — large plants, palm fronds or
dense foliage shot in natural light, processed to an extremely low 10-15%
opacity so it reads as a greenhouse shadow layer rather than a subject, full-
bleed with no border or mask, never the primary focus of any composition.

## Photo search

Unsplash first, Pexels second.
- "palm leaves botanical shadow natural light"
- "dense foliage greenhouse atmosphere"
- "large plant leaves close up soft light"
- "botanical texture low contrast"

## Reference lock

Primary reference/direction: Shelby Kay — linen botanical editorial portfolio,
265px edge-to-edge wordmark, two-colour ink system.
Preserve (3-5 traits): linen `#efe6d9` canvas with olive `#393c2a` structural
ink; sage `#737955` reserved strictly for display type, one element per
section maximum; extreme type-scale ratio (up to 265px wordmark vs. 10px
metadata), hierarchy by size alone; 0px radius and zero elevation on every
element without exception; botanical photography demoted to a 10-15% opacity
atmospheric layer, never a subject.
Borrow only (1-2): the rotated 90° secondary wordmark fragment pinned to the
margin; the rotated date-stamp on work-grid cards.
Role rules: sage never sets body text (fails contrast); no button of any kind
exists — navigation and contact are always plain text; body text never
centres except the section-anchor callout.
Media strategy: photo:unsplash — botanical/foliage photography used only as a
low-opacity atmospheric layer; one desaturated portrait permitted on a
profile page only.
Reject: any border-radius above 0px; drop shadows; sage used for body copy;
filled button backgrounds of any colour; a cool gray outside the Riverstone
token.
Token commitments: bg `#efe6d9`, tone-1 `#d6b292`, tone-2 `#afa199`, tone-3
`#7b8785`, ink `#393c2a`, brand `#737955`; wordmark Ranade 400 at up to
265px/leading 0.9; body Switzer 500-700 at 10-20px/leading 1.2-1.3; radius 0px
universal; base spacing unit 8px, section gap 36-56px.
