---
title: "Caractère Bois"
url: https://www.caractere-bois.fr
source_url: https://www.caractere-bois.fr
captured: 2026-09-04
origin: raw-url
extract: ok
category: luxury-craft
category2: portfolio
family: oxblood-atelier-blueprint
dna: "Documentary workshop video x oxblood serif wordmark with blueprint line overlays"
register: editorial print
grammar: gallery/catalog
lane: "A sky-blue band carries a huge oxblood serif wordmark over a workshop video, drops into a full-bleed oxblood pull-quote panel, then scatters joinery detail photography annotated with hairline architectural line drawings"
mode: persuade
traits: ["oxblood display serif wordmark", "sky-blue header band", "documentary workshop video hero", "full-bleed oxblood pull-quote panel", "mixed roman/italic serif headlines", "hairline architectural line overlays on photos", "scattered mosaic detail photography", "rounded humanist sans labels"]
palette: ["#EAEAEA", "#9CC4FF", "#540A04", "#F4300F", "#333333", "#C2AF94", "#B28959", "#897A65"]
type: ["PP Migra", "studiofeixensans"]
measured: designlang
kind: reference-style
source: claude
status: ready
raw: raw/d98c20760b023fbe-www-caractere-bois-fr.webp
---

## Why it works

The identity opens on a strong colour clash used deliberately: a sky-blue band
carries the wordmark "CARACTÈRE BOIS" set in an oxblood display serif (PP
Migra) large enough to nearly fill the header, with the brand's leaf-shaped
mark sitting between the two words as a hard-edged full stop. Immediately
below, a documentary video of a craftsman at a workshop table plays without
any text over it — the wordmark has already said the brand's name, so the
footage is left to just show real work happening. The next section commits
harder to the oxblood: a full-bleed dark-red panel with a French pull-quote
set in the same serif, roman and italic mixed within the sentence (much like
Calyx's own display convention) to give emphasis without changing size or
weight. The extract shows a brighter red-orange (`#f4300f`) as the single
most-used colour on the page, ahead of the oxblood itself — the identity
leans on this hotter accent for smaller, higher-frequency marks (links,
hairlines, small UI) while oxblood carries the large panels and the wordmark.

Further down, the page's most specific device appears: photographs of joinery
details — a door handle, a cabinet corner, a window frame — have thin oxblood
architectural line drawings sketched directly onto them, as if a blueprint had
been laid over the finished photograph. It reads as "this is designed before
it's built," turning product photography into evidence of process. The
detail photos themselves are scattered at irregular sizes rather than gridded,
echoing a workshop pin-board rather than a catalogue spread.

Labels and captions drop to a rounded, humanist sans (studiofeixensans),
tracked and small, giving the page the same voice/record split Calyx uses
between serif and mono — serif speaks, sans records.

## What to borrow (principle)

- **Let a bold wordmark on a contrasting flat-colour band stand alone above
  documentary footage** — the footage doesn't need to repeat what the wordmark
  already established.
- **Mix roman and italic within one headline sentence** for emphasis instead of
  changing size, weight or colour — it reads as considered typesetting rather
  than a shouted headline.
- **Overlay thin hand-drawn-style line work directly on product photography**
  to signal "this was designed," not just "this was photographed" — a cheap
  device relative to a full blueprint render, with outsized effect.
- **Scatter detail photography at irregular sizes** rather than a uniform grid
  when the goal is to feel like a workshop or atelier, not a catalogue.

## What to leave

- The sky-blue vs. oxblood header contrast is high-saturation and won't suit
  every craft brand — it works here because the rest of the page is quiet
  enough to absorb one loud opening beat.
- The hairline line-overlay device needs restraint; used on every photo it
  would stop reading as "blueprint annotation" and start reading as clutter.
- The pull-quote panel's italic-mixed-with-roman treatment depends on the
  copy itself being short — it would lose clarity in a longer paragraph.

## Signature move

Thin oxblood architectural line drawings sketched directly onto joinery detail
photographs — an arc, a door-frame outline — turning finished product shots
into something closer to an annotated technical drawing.

## Motion

(from designlang extract) The extract rates overall feel "smooth" with
confirmed scroll-linked behaviour. Three duration steps span 200ms to a full
1000ms, mostly on a plain `ease-in-out` (`ease`) rather than a custom bezier —
restrained, matching the page's quiet, gallery-like pacing. Five named
keyframes are defined, all dialog-pattern: `dialog-fade-in` (opacity 0→1)
plus four directional slide-ins (`dialog-slide-in-right/top/bottom/left`,
each a 100%→0 translate) — almost certainly the mechanism behind a cart/menu
overlay (the "PANIER/MENU" nav buttons noted in Reference lock) rather than
the joinery-detail or pull-quote sections, which appear to rely on plain
opacity/transform transitions instead. (observed in capture) The hero's
looping documentary video is independently confirmed — raw and fresh
captures show two different frames of the same workshop scene — autoplay/loop
video, not inferred.

| kind | tokens |
|---|---|
| durations | sm 200ms · md 400ms · xl 1000ms |
| easing | ease-in-out (`ease`, 1 use) |
| keyframes | `dialog-fade-in` · `dialog-slide-in-{right,top,bottom,left}` |

## Brief

Build a French craft/atelier brand on a high-contrast opening: a bold
oxblood-on-sky-blue (or equivalent complementary pair) wordmark band, followed
immediately by autoplaying documentary video of real workshop work with no
text overlay. Use one serif for all display copy, mixing roman and italic
within a single headline sentence for emphasis rather than varying size or
colour. Commit to one full-bleed dark accent panel for a short pull-quote.
Further down, scatter product/detail photography at irregular sizes rather
than a grid, and overlay a small number of them with thin hand-drawn-style
architectural line work to signal designed intention behind the craft. Keep
labels and captions in a plain rounded sans, small and tracked, separate from
the serif's voice.

## Image recipe

Documentary photograph of [SUBJECT] — a joinery/cabinetry detail (handle,
corner, frame) or interior fit-out — natural or warm interior light, real
material texture (wood grain, brass hardware) in sharp focus, candid framing
as installed rather than staged for catalogue, optionally with a thin
hand-drawn architectural line (arc, outline) overlaid in a single accent
colour to suggest a design sketch beneath the finished piece.

## Photo search

Unsplash first, Pexels second.
- "wood cabinetry detail brass handle"
- "joinery workshop craftsman documentary"
- "interior wood furniture detail natural light"
- "carpentry workshop tools warm light"

## Reference lock

Primary reference/direction: Caractère Bois — oxblood serif wordmark on
sky-blue, documentary workshop video, blueprint-line-overlaid joinery detail
photography.
Preserve (3-5 traits): high-contrast wordmark band (one bold accent colour on
one contrasting flat ground) opening the page; autoplaying documentary
workshop video with no text overlay; one serif carrying all display copy,
mixed roman/italic within a sentence for emphasis; thin hand-drawn-style line
overlays on a minority of detail photographs; scattered irregular-size photo
placement rather than a uniform grid.
Borrow only (1-2): the leaf-shaped logomark as a divider between wordmark
halves; the pill-shaped "PANIER/MENU" nav buttons.
Role rules: line overlays applied to at most a third of any photo set, never
all of them; serif never used for captions/labels, sans never used for
headlines.
Media strategy: photo/video:documentary — real workshop and installed-project
footage/photography only, no staged catalogue product shots.
Reject: a uniform photo grid in place of the scattered mosaic; line overlays
on every image; a second display typeface competing with the serif.
Token commitments: sky `#9CC4FF`, oxblood `#540A03`, oxblood-accent `#AB3E21`,
paper `#EAEAEA`, wood-light `#C2AF94`, wood-mid `#B28959`, wood-deep `#897A65`;
display serif "PP Migra" (roman + italic mixed), labels "studiofeixensans".
