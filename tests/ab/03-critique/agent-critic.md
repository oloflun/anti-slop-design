# Design critique - Florhuset Majorna (planted.html)

Lane/register sentence given: "salt-bleached harbour atelier, editorial print register."
Reference-lock: none was captured for this build - no competitor/market-leader pages were named, screenshotted, or observed before work started.

All findings below are drawn independently from the rendered CSS/HTML and the six screenshots.

---

## Summary

The bones are competent editorial-print execution - real ledger for prices, kicker microformat, hairline rules, a genuine tonal-inversion footer, a reduced-motion-safe reveal system - but the build fails its own named lane. "Salt-bleached harbour" was never delivered: the palette and photography read as generic warm-cream botanical editorial (the Calyx family already catalogued in house-physics.md), with no cool, weathered, or coastal quality anywhere despite Majorna being a harbour district. On top of that direction miss, the single locked accent is used backwards - confined to small controls and never once reaching display scale - and there is a real accessibility failure (a sold-out state that is invisible to assistive tech, not just low-contrast). This does not hold up as shipped; it needs both a direction correction and several concrete fixes.

---

## Findings, severity-ranked

### 1. Critical - the single accent never reaches display scale (house-physics.md, Structural)
Rule: "Exactly ONE saturated accent, deployed at display scale (drop caps, giant prices, glyphs, a drawn form) and never as fill on a small control."

--accent: #C1432B is used in exactly five places on this page: the two hero .btn-primary fills, the .badge-decorative pill fill, the .dot-slut sold-out dot fill, and the three footer h3 micro-labels (11px). It is never used on a headline, a ledger price, a drop cap, or any other display-scale element - the one place it would have earned its keep (the ledger prices in .ledger-price, which are plain var(--ink)) is exactly where it is absent. The rule is inverted: the accent is small-control-only, the opposite of the spec.
Before: accent used only as button/badge/dot fill. After: move the accent onto one display-scale element (for example the ledger price numerals, or the hero first word) and drop it from the small fills.

### 2. Critical - sold-out state is invisible, not just low-contrast (accessibility; WCAG 1.4.1)
Row 03 in the ledger (Dahliabukett) carries its sold-out state as a span.ledger-status containing only span.dot-slut, and the dot itself is aria-hidden="true". A screen-reader user gets nothing: the row reads identically to an in-stock row. A sighted user gets a red dot with no label explaining what it means (confirmed in planted--s01.png). This is worse than a contrast failure - the information does not exist for assistive tech at all, and even visually there is no adjacent word ("Slutsald") anywhere in the row.
Before: dot only, aria-hidden. After: visible text label ("Slutsald") plus the dot as reinforcement, never the reverse.

### 3. High - two competing primary CTAs in the hero, no hierarchy (structural: "Hierarchy through scale, not decoration"; register: "Buttons barely exist")
planted--s00.png: "BESTALL BUKETT" and "BOKA BROLLOPSMOTE" are both .btn-primary - identical accent fill, identical size, side by side, equal visual weight - for two actions of very different intent (a transaction vs. booking a consultation). A visitor cannot tell which is the default action in the two-second read the pre-emit hierarchy check calls for. This also collides with the editorial-print button physics in house-physics.md ("Buttons barely exist. CTAs are typeset mailtos/links... Hyperborea's one button is a sharp amber rectangle") - this page ships two solid rectangle buttons in the hero alone.
Before: two identical filled buttons. After: one primary action (filled or typeset), the other demoted to a text link.

### 4. High - decorative badge outweighs the real conversion link (structural hierarchy; production-tells gate 84 spirit)
planted--s02.png, Prenumeration section: the star-marked "Mest bokade" badge is a bold, filled, rounded-pill badge - the loudest element in the section. The actual conversion action, "Starta prenumeration ->", is a 14px grey underlined text link buried after two paragraphs of body copy. "Mest bokade" is also an unsourced superlative with no supporting number anywhere on the page - the kind of performative social-proof label gate 84 flags, dressed as a rounded chip the editorial-print register otherwise avoids.
Before: badge louder than CTA. After: either the CTA carries the section visual weight, or drop the unsubstantiated badge.

### 5. Medium - caption-grey fails contrast (slop-test.md gate 40)
--caption-grey: #9A9A9A on --cream: #F6F1E8 computes to approximately 2.5:1 (WCAG relative-luminance check, verified independently). Gate 40 requires 4.5:1 for small text and 3:1 even at the large-text/icon floor - this fails both. It is used on both figcaptions (hero and about-section) - both legible-looking but measurably under floor.
Fix: darken the token until it clears 4.5:1 against cream (--stone at #5B5850 already clears about 6.3:1 - the caption token should sit closer to that family, not a flat unrelated grey).

### 6. Medium - three consecutive sections share one anatomy (house-physics.md: "At least three distinct section anatomies per page")
Brollop, Prenumeration, and Ateljekvallar (planted--s02.png, planted--s03.png top) are all: kicker + h2 + paragraph, single column, no imagery, same cream ground - differing only in whether a link or badge is tacked on. House-physics.md's own closing guidance names this exact failure mode: "If a section is about to become... three same-rhythm text blocks, this file is the list of what to do instead." This build ships precisely the pattern the file warns against, back-to-back.
Fix: give at least one of the three a distinct anatomy - an image, a stat, a full-height rule, a different grid - per "every open column carries weight."

### 7. Medium - inconsistent heading level across three parallel info items (heading-rhythm / semantic consistency)
In "Om ateljen" (planted--s03.png to planted--s04.png), the three-column info grid has "Adress" and "Hitta hit" styled as 10.5px mono kicker paragraphs, but the middle item, "Oppettider," is marked up and styled as a 25px serif h3 - visibly much larger and heavier than its two siblings in the same row. This reads as a markup accident, not a deliberate weight choice: three parallel facts should carry equal typographic treatment.
Fix: make all three either headings or all kicker-labelled paragraphs - pick one, apply to all three.

### 8. Low - en dash used as a range separator in running/footer copy (slop-test.md gate 75)
"Tis-fre 10-18", "Lor 10-15", "Son-man stangt" (opening hours, both in the info grid and repeated in the footer) use an en dash as a separator. Gate 75 is zero-tolerance on em-dash and separator-en-dash anywhere, including body copy and captions, with no carve-out for date/time ranges. This is mechanically detectable and appears in at least two places on the page.
Fix: replace with regular hyphens or spell the range out.

### 9. Low - section padding-block values do not sit on a coherent scale
Across six sections: 96px, 116px, 84px, 120px, 96px, 116px. All are multiples of 4px (so the literal gate-24 grid-snap check passes), but the deltas between them show no legible rhythm or scale relationship - it reads as unplanned rather than a deliberate stagger.
Fix: pick a small step scale (for example 88 / 104 / 120px) and assign padding by section weight, not arbitrarily.

---

## Lane-sentence audit (separate from the numbered gates)

The named direction was "salt-bleached harbour atelier, editorial print register." What shipped is warm cream (#F6F1E8), a dark botanical-green ink (#1E2A1F), and a rust/terracotta accent (#C1432B) - this is, in effect, the "cream botanical atelier" family house-physics.md already catalogues under Calyx (cream oklch(0.965 0.012 88), rust oklch(0.46 0.108 38)), not a distinct "salt-bleached harbour" direction. Nothing on the page is coastal or weathered: the hero photograph is a glossy studio shot of hands holding a bouquet against a bright pink backdrop (planted--s00.png), and the about-section photograph is a bed of red begonias - neither reads as harbour, salt, or bleach in any way, despite Majorna being a genuine Goteborg harbour district a few blocks from the water. There is no cool tone, no grey-driftwood texture, no sea reference anywhere in the palette or imagery direction.

This is a Step 2 (direction-derivation) problem, not a fix being proposed here - the build needs its palette and imagery direction re-derived from "salt-bleached harbour" honestly, rather than defaulting to the warm-cream-editorial attractor that gate 89 exists to catch. Gate 89 does not auto-fail here on its narrow technical text, since a florist's seasonal ledger is plausible editorial-print territory - but the lane sentence asked for something more specific than editorial-print-in-general, and that specificity was dropped.

---

## Verdict: revise

The structural bones (ledger, kicker, hairlines, reveal system, tonal-inversion footer) are sound and worth keeping. But this cannot ship as-is: findings 1-2 are a structural-rule inversion and a real accessibility failure, 3-4 are unresolved hierarchy problems on the two most commercially important elements on the page (the hero CTA and the subscription CTA), and the lane-sentence audit is a named, unresolved Step 2 gap that should be corrected before the palette is treated as final - flagged here, not solved here.
