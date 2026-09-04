---
title: "Vestris"
url: https://vestris.ai/
source_url: https://vestris.ai/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/7d60cd211483dd41-screenshot.webp
category: product-focused
category2: ""
family: ivy-framed-fintech
dna: "Renaissance still-life vines x real-estate ops dashboard"
register: editorial print
grammar: live surface
lane: "A serif-italic headline in parentheses sits on a sage ground, framed by painted ivy vines crawling in from both edges around a floating product screenshot, then a numbered four-step proof sequence"
mode: persuade
traits: ["sage/cream ground", "painterly ivy-vine illustration framing the hero", "serif-italic parenthetical headline", "YC badge", "floating product UI card", "numbered proof steps", "document-card stack visual", "olive CTA buttons"]
palette: ["#7C8F6E", "#F0ECDD", "#33402B", "#FFFFFF", "#FF6600"]
type: ["Instrument Serif", "Geist"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The headline is set inside literal parenthesis marks — "( The file moves itself
)" — in a serif italic, which does two things at once: it reads as an aside, a
quiet confident claim rather than a shouted one, and the parentheses themselves
become a graphic device the eye tracks. That restraint is unusual for a YC-
backed AI startup, most of which default to bold sans headlines; here the
software claim is dressed in editorial, almost literary type.

Painted ivy vines, rendered in a soft old-master illustration style, crawl in
from both edges of the hero and frame the floating product screenshot at the
centre. It's a strange, memorable pairing — botanical illustration around a
document-automation dashboard — and it works because the vines never touch or
obscure the screenshot itself; they stay in the margins, doing atmosphere while
the UI does proof.

The proof structure below is procedural rather than promotional: four numbered
steps (`01` documents find their file, `02` the next step kicks off, `03`
generate closing docs, `04` title searches complete) each paired with a plain
sentence and, for the visual anchor, a stack of scanned document cards showing
real file types (Purchase Contract, Invoice, HOA Disclosure) routing into an
order. It reads like a systems diagram dressed as a feature list.

## What to borrow (principle)

- **Set a plainly confident claim inside literal parentheses**, in serif italic,
  to lower the temperature of an AI-automation headline without weakening it.
- **Frame a product screenshot with illustration that stays in the margins** —
  vines, borders, ornament — never overlapping the UI itself.
- **Number your proof steps and pair each with one plain sentence**, not a
  paragraph, so the sequence reads as a process rather than a features list.
- **Show real document types moving through the system** (contract, invoice,
  disclosure) rather than abstract icons, when the product's job is document
  handling.

## What to leave

- The old-master ivy illustration is distinctive but sits in tension with the
  otherwise crisp, modern product screenshot — it risks reading as decorative
  rather than integrated if it doesn't recur anywhere else on the page.
- A YC badge this prominent works as credibility shorthand for a narrow
  investor/technical audience but says little to the actual buyer (a title
  company); it may be over-indexed for the wrong reader.

## Signature move

The parenthetical headline: the entire hero claim wrapped in literal `( )`
marks, set in serif italic. It turns a bold software claim into something closer
to a whispered aside — confident without needing volume.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed,
but the captured CSS is nearly empty: the only duration token is an
`instant` (1ms) allow-discrete overflow transition and a generic `transition:
all`, with a single spinner keyframe. This is consistent with a page whose
real content motion (the document-card stack settling into the order, the ivy
vines framing in) is likely driven by inline JS/whileInView animation rather
than CSS, so it isn't visible to static extraction — the "cards animate in"
read stays inferred from the image, not confirmed by the extract.

| token | value | role |
|---|---|---|
| `instant` | 1ms | baseline transition duration (framework default) |

## Brief

Build a sage-and-cream product page for a document-automation platform. Open on
a parenthetical headline in serif italic, small YC/investor badge above it, a
single "meet your assistant" CTA. Frame the hero's floating product screenshot
with painterly botanical illustration entering from both edges, never
overlapping the UI. Below, lay out a numbered four-step process, each step one
plain sentence, paired with a visual of real document types stacking into an
order. Keep buttons olive-filled, sans-serif, fully lowercase.

## Image recipe

Illustrated botanical vine or ivy, painted in a soft old-master still-life
style, muted sage and olive tones with occasional warm highlight, rendered to
frame empty negative space at the centre — the vine reads as a border
ornament, never as the subject.

## Photo search

Unsplash first, Pexels second (illustration, not photography, is primary here).
- "botanical illustration vine ivy vintage"
- "old master still life leaves painting"
- "sage green foliage illustration border"

## Reference lock

Primary reference/direction: Vestris — parenthetical serif-italic headline framed by painterly ivy vines around a floating product screenshot.
Preserve (3-5 traits): headline set inside literal parenthesis marks in serif italic; botanical illustration framing the hero screenshot without ever overlapping the UI; numbered process steps paired with real document-type visuals; sage-and-cream ground with olive-filled CTAs.
Borrow only (1-2): the YC/investor badge above the headline; the document-card stack visual.
Role rules: illustration stays confined to hero margins, never inside a UI screenshot; parenthetical headline device used once per page, not repeated as a section-header pattern; numbered steps capped at one sentence each.
Media strategy: illustration only for the hero frame (no photography); product screenshots are real UI, never mockup placeholders.
Reject: bold, shouted AI-startup headline type in place of the parenthetical serif italic; illustration overlapping or obscuring the product screenshot; abstract icons replacing real document-type visuals in the proof section.
Token commitments: sage `#7C8F6E`, cream `#F0ECDD`, olive-ink `#33402B`, white `#FFFFFF`, badge-orange `#FF6600`; serif italic for the hero headline only, sans for all UI and body copy.
