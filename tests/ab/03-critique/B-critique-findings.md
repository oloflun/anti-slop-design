# Visual critique — Florhuset Majorna ("planted.html")

**Lane:** salt-bleached harbour atelier, editorial print register
**Inputs read:** fold screenshot, full-page slices s00–s05 (all Read into context),
source `planted.html` (HTML comments treated as absent — not used as evidence),
live render inspected in-browser for computed-style measurements (colour, font-size,
padding) cited below. Reference: `house-physics.md`, editorial-print register
(Calyx / Hōrai / Hyperborea invariants + the all-register Structural section).

No `DESIGN.md` exists for this fixture; the lane sentence + house-physics register
table stand in for it per the critique procedure.

---

## 1 · Hierarchy — **major**

**Observation.** The hero's two CTAs, "Beställ bukett" and "Boka bröllopsmöte,"
are rendered with identical computed styles: `background: rgb(193,67,43)`,
`border-color: rgb(193,67,43)`, `font-size: 13px`, `padding: 15px 26px` for both.
Nothing on screen marks one as the default action. Separately, in "Om ateljén,"
the section heading `h2` ("Om ateljén," 28px) sits beside its child label
`h3` ("Öppettider," 25px, weight 500) — a measured size ratio of 1.12×.

**Problem.** Two filled, same-weight, same-color CTAs side by side violate the
"one dominant action, primary filled / secondary ghost" rule directly — a visitor
has no signal for which action the business actually wants first (buy flowers,
which is the site's stated primary activity, vs. book a wedding consult, a
lower-frequency action). The h2/h3 pair falls well under the ≥1.5× differential
the house scale requires between adjacent hierarchy levels — at 1.12× the
section heading and its sub-heading read as near-siblings, flattening the level
that should separate "section" from "sub-topic within section."

**Fix.** Demote "Boka bröllopsmöte" to the register's existing secondary
treatment — the italic underlined text-link pattern already used for the
Bröllop section's own CTA — leaving exactly one filled button in the hero.
For the about section, either drop "Öppettider" to the same kicker + body
pattern used by "Adress" and "Hitta hit" (see Typography, below) or restore a
real size step between the h2 and h3 (e.g. 28px → 18–20px).

## 2 · Composition — **major**

**Observation.** Bröllop → Prenumeration → Ateljékvällar run as three
consecutive sections on a shared cream ground, each built from the identical
anatomy: kicker, h2, one paragraph. No image, ledger, inversion, or grid-break
interrupts the run (confirmed against the full-page slices s02–s03). Measured
`padding-top`/`padding-bottom` across sections: hero 96px, ledger 116px,
Bröllop 84px, Prenumeration 120px, Ateljékvällar 96px, about 116px — four
distinct values with no shared step (84/96/116/120, deltas of 12/20/4).
Within Prenumeration, a filled accent pill ("★ Mest bokade," bold, rounded,
high-contrast) sits directly above a quiet grey underlined text link
("Starta prenumeration →") that is the section's actual conversion action.

**Problem.** Three flat text blocks in a row is the named composition-contract
failure regardless of how good any one of them reads alone — the page goes
visually silent for an entire scroll-and-a-half. The padding drift means
section rhythm reads as improvised rather than deliberate — nothing marks
Prenumeration as more "important" than its 120px vs. Bröllop's 84px, so the
inconsistency has no narrative purpose, only noise. The decorative badge
out-weighs the real CTA beneath it: a squinting reader's eye lands on the
badge, not the link that actually converts.

**Fix.** Break the three-in-a-row run by giving at least one section a
distinct anatomy — an image, a ledger-style stat, or the about-section's photo
pulled forward. Quantize section padding to a defined scale (e.g. 88/112/136px)
so consecutive sections read as one system. Drop the "★ Mest bokade" badge or
shrink it to kicker weight, and raise "Starta prenumeration →" to a treatment
that reads as the loudest thing in the section.

## 3 · Typography — **major**

**Observation.** In the "Om ateljén" info-grid, three parallel, semantically
equal column labels receive three different treatments: "Adress" and
"Hitta hit" use the `.kicker` micro-format (uppercase, letter-spaced, mono),
while "Öppettider" is a full `h3` (25px serif, weight 500) — confirmed by
DOM inspection, not just appearance.

**Problem.** These three labels do the same job (naming a fact about the
atelier) and should share one treatment per the token-compliance rule; instead
the middle column reads as a sub-heading of its own section while its
neighbors read as captions, which breaks the row's scan pattern — a reader's
eye has to re-parse the row instead of reading three parallel facts.

**Fix.** Set all three labels to the kicker format (or promote all three to
the same heading level) so the row reads as one system.

## 4 · Colour — **major**

**Observation.** Photo captions (e.g. "Sensommarbukett, bunden på ateljén
vecka 36") and the ledger's "vas ingår ej" sub-price text render at
`rgb(154,154,154)` / `#9a9a9a` against the `#F6F1E8` cream ground. Measured
contrast ratio: **2.50:1**. Separately, the sold-out marker on "Dahliabukett"
(row 03) is a small filled-accent dot (`.dot-slut`) with `aria-hidden="true"`
and no adjacent text — confirmed via DOM: the status element's `textContent`
is empty and it carries no accessible name.

**Problem.** 2.50:1 is under the 3:1 floor for large/meta text and far under
4.5:1 for body-scale text — these captions and price sub-labels are
functionally illegible for anyone with even mild low-vision, and this is a
named gate, not a matter of taste. The sold-out dot carries state through
colour alone with zero text fallback, sighted or assistive — a colour-blind
visitor or a screen-reader user gets no signal at all that "Dahliabukett" is
unavailable.

**Fix.** Raise caption/meta colour to the `--stone` token (`#5B5850`), already
used elsewhere on the page and legible against cream. Add a visible text
label ("Slutsåld") next to or replacing the dot, and give it (or its parent)
an accessible name if the dot stays as a decorative reinforcement.

## 5 · Affordance — **major**

**Observation.** Same evidence as Hierarchy #1 (identical dual CTAs) and
Colour #4 (colour-only sold-out state), viewed from the controls angle: the
hero offers two default-looking buttons with no primary/secondary
distinction, and the ledger's unavailable-item state has no discoverable
affordance at all — no text, no strikethrough on the price, no disabled
styling on the row.

**Problem.** "Single CTA" and "state never carried by colour alone" are both
named rules under this dimension and both fail on the same evidence already
cited. A user scanning the ledger for what they can actually buy has no way
to tell row 03 is unavailable until they try to act on it.

**Fix.** Same as above: demote the secondary hero CTA; add a text/strike
treatment to the sold-out row (e.g. "Slutsåld" kicker-style label, price
struck through or greyed with a text note, not colour alone).

## 6 · Information density — **minor**

**Observation.** The ledger repeats "vas ingår ej" on all four rows even
though it doesn't vary row to row. Otherwise the page is easy to scan: one
task per section, prices right-aligned and consistently formatted, footer
grouped by function.

**Problem.** The repeated micro-copy is low-value repetition at reading pace —
not harmful, but it's four instances of information that could be said once.

**Fix.** State "vas ingår ej" once, near the section heading or ledger head,
rather than on every row (unless it's meant to vary in the future).

## 7 · Brand consistency — **major**

Compared against the lane sentence ("salt-bleached harbour atelier, editorial
print register") and house-physics' Structural section plus the
Calyx-family editorial-print invariants (the closest documented register
match).

**Observation.** The Structural section requires "exactly ONE saturated
accent, deployed at display scale... and never as fill on a small control."
On this page the accent (`#C1432B`) appears exactly four times, and every
instance is a small-control fill: two hero buttons, the decorative
"Mest bokade" badge, and the sold-out dot. It never appears at display scale —
no giant price, no drop cap, no accent glyph; ledger prices and numerals
render in plain ink, not accent. Separately, the hero photograph (styled
hands cradling a heart-shaped bouquet against a flat pink studio backdrop,
with scattered red beads) is a posed product shot, while the "Om ateljén"
photograph (unstyled red begonias in natural light outside the shopfront) is
documentary. And the page runs three different CTA affordances at once —
filled button (hero), italic underlined text-link (Bröllop), small quiet
underlined text-link (Prenumeration) — without an apparent rule for which
applies where.

**Problem.** The accent's role is inverted from what the register specifies:
it's a small-control colour here, never a display-scale one, which is the
opposite of what makes the "one saturated accent" rule work as a hierarchy
device elsewhere in the house's examples. The hero photo's styled/staged
register reads as generic e-commerce florist photography, which undercuts the
documentary, unpolished "atelier" mood the kicker, ledger, and second photo
establish — the page doesn't commit to one photographic voice. Three CTA
styles with no visible rule reads as inconsistency rather than intentional
range.

**Fix.** Move the accent to at least one true display-scale use (a large
price, a drop cap, a numeral) and reserve it from small-control fills going
forward — use the existing text-link pattern for buttons instead. Replace or
recrop the hero image to match the about-section photo's documentary,
natural-light quality. Settle on one CTA affordance system (most likely the
text-link pattern already used twice) and reserve any filled button for a
single, genuinely primary action if one is kept at all.

---

## Squint test

Blurred, the top-level hierarchy still reads: headline dominant, image
secondary, ledger legible as a price list. Two failures surface specifically
under blur: the hero's two CTAs merge into one undifferentiated red block
(the eye can't tell there are two, let alone which is primary), and the
sold-out dot on row 03 all but disappears — a single 8px dot is not enough
visual weight to carry a state that matters to a buyer. No column in the
page's grids is an empty "hole" — every open column (hero image, about
figure, info-grid cells) carries real weight — so this check passes on the
composition side even where hierarchy and affordance fail.

## Composition contract (three-flat-text-sections)

**Fails.** Bröllop, Prenumeration, and Ateljékvällar — in that literal,
consecutive order — are all kicker + h2 + paragraph on the same cream ground,
with no image, ledger, inversion, or grid-break anywhere in the run. Named
explicitly under Composition above.

---

## Prioritised fix list

**P1 — Critical**
1. **Issue:** Photo captions and ledger sub-price text render at `#9a9a9a` on
   `#F6F1E8` — measured 2.50:1, under the 3:1 AA floor for large/meta text.
   **Dimension:** Colour. **Fix:** Raise to the `--stone` token (`#5B5850`).
2. **Issue:** Sold-out state on "Dahliabukett" is a bare `aria-hidden` colour
   dot with empty text content — no visible or accessible label.
   **Dimension:** Affordance. **Fix:** Add a visible "Slutsåld" text label
   with a real accessible name; don't carry the state on colour alone.
3. **Issue:** Hero's two CTAs ("Beställ bukett" / "Boka bröllopsmöte") share
   identical background, border, size, and padding — no primary/secondary
   distinction for the site's actual default action.
   **Dimension:** Hierarchy / Affordance. **Fix:** Demote the wedding CTA to
   the italic text-link pattern already used in the Bröllop section; keep one
   filled button.

**P2 — Important**
4. **Issue:** Bröllop → Prenumeration → Ateljékvällar are three consecutive
   sections with identical anatomy (kicker + h2 + paragraph, no imagery).
   **Dimension:** Composition. **Fix:** Give at least one a distinct anatomy
   (image, ledger stat, or pull the about photo forward).
5. **Issue:** Section vertical padding measures 96/116/84/120/96/116px across
   hero/ledger/Bröllop/Prenumeration/Ateljékvällar/about — no shared scale.
   **Dimension:** Composition. **Fix:** Quantize to a defined step
   (e.g. 88/112/136px).
6. **Issue:** In the about-section info-grid, "Adress" and "Hitta hit" use
   the kicker micro-format but "Öppettider" is a full h3 — three parallel
   labels, three treatments.
   **Dimension:** Typography. **Fix:** Set all three to the kicker format.
7. **Issue:** "Om ateljén" h2 (28px) and "Öppettider" h3 (25px) measure a
   1.12× size ratio, under the house's ≥1.5× hierarchy-level floor.
   **Dimension:** Hierarchy. **Fix:** Restore a real size step, or fold
   "Öppettider" into the kicker treatment per item 6.
8. **Issue:** The "★ Mest bokade" filled accent pill outweighs the section's
   real conversion action, the quiet underlined "Starta prenumeration →" link.
   **Dimension:** Composition / Affordance. **Fix:** Drop or shrink the
   badge; raise the real CTA's visual weight.
9. **Issue:** The single saturated accent never reaches display scale on this
   page — it appears only as fill on four small controls (2 buttons, badge,
   dot), the opposite of the house's "display scale, never small-control
   fill" rule.
   **Dimension:** Colour / Brand. **Fix:** Give the accent one true
   display-scale use (large price, drop cap, or numeral); move small controls
   to the existing text-link pattern.

**P3 — Polish**
10. **Issue:** The hero photograph (styled hands-and-bouquet product shot on
    a flat pink studio backdrop) reads in a different photographic register
    than the documentary, natural-light photo in "Om ateljén."
    **Dimension:** Brand. **Fix:** Recrop or replace the hero image to match
    the about section's unstyled, documentary quality.
11. **Issue:** "vas ingår ej" repeats identically on all four ledger rows.
    **Dimension:** Density. **Fix:** State it once near the ledger heading.

---

## Assessment

The page's strongest dimension is typography's *scale usage* at the macro
level — the display headline, kicker, and body sizes are drawn from a
disciplined set and the ledger's numeral/name/price columns read cleanly at a
glance. Its weakest dimension is composition: three consecutive
identical-anatomy text sections and a section rhythm with no shared scale
both show up as soon as you scroll past the ledger, and they compound with a
genuine accessibility failure (2.50:1 captions, colour-only sold-out state)
and a hierarchy failure (two identical CTAs) that a reviewer can verify on
the fold screenshot alone, without reading any code.

## Honest reference sentence

This page does not beat the register's own references. Calyx and the other
editorial-print worked examples in house-physics keep the accent strictly at
display scale and never let two CTAs compete for the same weight; this build
inverts the first rule (accent only ever appears as small-control fill) and
breaks the second directly (two identical filled hero buttons). The
three-flat-text run is exactly the failure mode house-physics' structural
section warns against ("at least three distinct section anatomies per
page"), and the measured 2.50:1 caption contrast is a plain AA miss the
references don't carry. Where this build matches the references — kicker
microformat, ledger-not-card-grid pricing, one tonal inversion in the footer —
it matches faithfully; where it deviates, it deviates into defects, not
intentional range.
