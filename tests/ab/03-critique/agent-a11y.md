# Accessibility Audit: Florhuset Majorna (planted.html)

**Audited:** `file:///C:/Users/Anton L/anti-slop-design/tests/ab/03-critique/planted.html` (also served locally at `http://localhost:3055/` for the two scripts that require a running origin). 2026-09-03.
**Scope:** Whole page — single-page site (header/nav, hero, säsongens buketter ledger, bröllop, prenumeration, ateljékvällar, om ateljén, footer). Source HTML comments were treated as absent throughout; no finding below relies on reading one.
**Register / lane:** Salt-bleached harbour atelier, editorial print register.

## Coverage

| Pass | Evidence inspected | Result |
| --- | --- | --- |
| 0 Scope | Live DOM via Chromium (Playwright), not a screenshot-only review — keyboard, focus, contrast and reflow findings below are **verified**, not inferred | Verified |
| 1 Mechanical | `a11y_scan.py`, `tab_walk.py`, `reflow.py` ran clean against the live page; `contrast.py` ran against a local static copy on port 3055 (the script hardcodes that origin); `contrast_over_media.py` ran but its selector list (`h1, header nav a, header a, section p, section a[href='#meny']`) does not match anything on this page's markup, so it returned no rows — **not applicable as authored to this fixture**, see Pass 2 for how the affected strings were checked instead. CARL check (`tests/a11y/broken.html`) was **not run**: the fixture does not exist in this project and this agent is read-only, so it cannot be created here — flagging rather than silently trusting a clean pass. | 3 mechanical findings, 1 domain (CARL) not verified |
| 2 POUR | Full markup/CSS read + axe-core + contrast.py + manual relative-luminance check for the two strings the media-detection heuristic misclassified | 6 findings / Clear otherwise |
| 3 Cognitive (COGA) | Hero CTAs, prenumeration CTA hierarchy, ateljékvällar task path, wayfinding across the info-grid | 3 findings |
| 4 Content | Alt text, heading structure, link text, reading level, address/hours block | 1 finding (heading/label inconsistency); alt text, reading level and link text are clean |
| 5 Adaptive | `prefers-reduced-motion` (CSS + JS gate), reflow at 320px/200% zoom, `rem` vs `px` usage, colour independence (greyscale reasoning) | 1 finding (px usage); motion and reflow are clean |
| 6 Interaction | Tab order and focus-indicator presence (`tab_walk.py`, 11 stops, 0 issues), focus-ring contrast per background, hit-area sizing from measured rects | 2 findings |
| 7 Personas | 6 personas, 5 key tasks each, barrier matrix below | See below |

`Clear` means inspected with no actionable finding. `Not reviewed`/`Not verified` is stated plainly above rather than folded into a pass.

## Summary

The page is legible, keyboard-reachable end to end, and gets prefers-reduced-motion right in both CSS and JS — genuinely well built on that front. But four contrast pairs (two body-copy pairs, one footer-label pair, and the keyboard focus ring itself in the footer) fall under the WCAG AA floor, and the sold-out marker on the Dahlia bouquet carries its entire meaning in an `aria-hidden` red dot with no text anywhere near it — a colorblind or screen-reader user has no way to learn that item is unavailable before trying to order it. Those four are escalation triggers and block ship as-is.

## Findings

| Severity | Location | Before | After | Why | WCAG | Who |
| --- | --- | --- | --- | --- | --- | --- |
| HIGH | `.dot-slut`, planted.html:96 (CSS), :222 (markup, "Dahliabukett" row) | `<span class="dot-slut" aria-hidden="true"></span>` — a solid 8px dot, hidden from assistive tech, no text anywhere in the row | Add a visible text label in the row (e.g. "Slutsåld") alongside the dot; keep the dot `aria-hidden` if it stays purely decorative once the text exists | Sold-out state is carried by colour alone, and the one visual cue is additionally removed from the accessibility tree entirely — a colorblind, low-vision or screen-reader user gets zero signal before trying to order an unavailable item. Same accent red also means "primary action" elsewhere on the page, so even a sighted user has no reason to read this dot as a warning. `[escalation trigger]` | WCAG 1.4.1 Use of Color (A) | Colorblind users (~1 in 12 men), screen-reader users, low-vision/glare situational users |
| HIGH | `.hero figcaption` (:77) and `.about-section figcaption` (:124), both using `--caption-grey` (:28) | `color:#9A9A9A` on the page's actual cream background `#F6F1E8` — measured **2.50:1** (computed from the CSS custom-property values; `contrast_over_media.py`'s hardcoded selector list doesn't cover `figcaption`, and `contrast.py`'s media heuristic false-positives these as "over photo" because the caption sits in the same `<figure>` as the image, not actually over its pixels) | Move `--caption-grey` toward `--stone` (`#5B5850`, ≈6.3:1 on cream) or another value ≥4.5:1 at this size, then re-measure | Caption text is 11px — never "large text" — so the 4.5:1 AA floor applies, and it fails by a wide margin at both locations that use this token. `[escalation trigger]` | WCAG 1.4.3 Contrast (Minimum) (AA) | Low-vision users, older users, anyone in bright ambient light |
| HIGH | `footer h3` (:135, color) on `footer` (:133, background) — "Kontakt", "Besök oss", "Följ oss" | `color:var(--accent)` `#C1432B` on `background:var(--ink)` `#1E2A1F` — measured **2.92:1** (contrast.py; independently confirmed by axe-core's `color-contrast` rule on all three nodes) | Use a lighter tonal value for this context (cream or a lightened rust both clear 4.5:1 on ink), re-measure | 11px labels fall well under the 4.5:1 AA floor. `[escalation trigger]` | WCAG 1.4.3 Contrast (Minimum) (AA) | Low-vision users reading the footer |
| HIGH | `:focus-visible` (:48) applied to footer links ("Instagram", "Nyhetsbrev") on `footer` background | The focus ring uses `outline:2px solid var(--accent)` — the identical accent-on-ink pair from the row above, 2.92:1 | Add a footer-scoped override, e.g. `footer :focus-visible{outline-color:var(--cream)}` (≈13:1 on ink) | The keyboard focus ring itself is a contrast pair subject to the 3:1 UI-component floor; it inherits the same failing pair as the footer headings in this one context, even though it passes cleanly (≈4.5:1) everywhere else on the cream ground. `tab_walk.py` only checks that an outline exists, not its contrast, so this doesn't show up as an automated "issue" — found by tracing the token through both contexts. `[escalation trigger]` | WCAG 1.4.11 Non-text Contrast / 2.4.13 Focus Appearance (AA) | Keyboard users, low-vision users tracking focus position |
| MEDIUM | Whole document — no `<main>` anywhere in the body (axe-core `landmark-one-main`, `region`, both "moderate") | Header → hero → four content sections → footer, with no landmark beyond `<header>`, `<nav>`, `<footer>` | Wrap the hero-through-about content in `<main id="main">`; add a skip link (`<a class="skip-link" href="#main">Hoppa till innehåll</a>`) as the first focusable element | Assistive-tech users can't jump straight to page content and have no bypass past the header nav | WCAG 1.3.1 Info and Relationships, 2.4.1 Bypass Blocks (A) | Screen-reader and switch-access users, every visit |
| MEDIUM | `.info-grid` in `#om`, :277–288 — Adress / Öppettider / Hitta hit | "Öppettider" is a real `<h3>` (:282); "Adress" (:278) and "Hitta hit" (:286) use `<p class="kicker">` for the same visual role | Make all three the same level — three `<h3>`s, or three non-heading labels, pick one | A screen-reader user scanning by heading loses two of three parallel facts that the third exposes as a heading | WCAG 1.3.1 Info and Relationships (A) | Screen-reader users comparing the three info blocks |
| MEDIUM | `.cta-quiet`, "Starta prenumeration →", :255 | `href="#"` — the subscription flow's only call to action targets nothing; activating it (any input method) does nothing observable | Point it at a real destination, or a `mailto:` fallback matching the `#brollop` section's own pattern | This is the sole path to the subscription task named in the brief; everyone who tries it gets silent, unexplained failure — worse for screen-reader/keyboard users, who get no differentiating feedback that nothing happened | No direct SC — content/completeness gap adjacent to 2.4.4 (link text itself is fine, the destination isn't) | All visitors attempting to subscribe |
| MEDIUM | Header `nav a` (:55 CSS, :161–167 markup) — Buketter, Bröllop, Prenumeration, Ateljékvällar, Om ateljén | Measured hit-area height **17px** (`tab_walk.py`, desktop 1440×900) with ~21–23px horizontal gaps between adjacent links and no vertical padding | Add `padding-block` to nav links (reuse the existing spacing scale) so each clears 24×24 CSS px outright | Measured directly, not inferred: the smallest dimension sits under the WCAG 2.5.8 floor, and the gap is too close to the 24px spacing-exception threshold to rely on. Not re-measured at the 390px mobile viewport where `flex-wrap:wrap` changes the layout — flagged as not verified there | WCAG 2.5.8 Target Size (Minimum) (AA) | Motor-impaired and situational (one-handed, in-motion) pointer users, most acute on touch |
| MEDIUM (COGA) | `.hero .ctas`, :181–184 — "Beställ bukett" / "Boka bröllopsmöte" | Both links share the identical `.btn-primary` fill, weight and colour, with no visual default | Keep one filled/primary, demote the other to the page's own `.btn-text` style (cheapest-fix ladder: reuse, don't invent) | Violates "one primary action per screen" — forces every visitor to resolve which action the page wants before acting, right at the point meant to convert | No direct SC — COGA / cognitive-load principle | First-time visitors, users under time pressure, situational (interrupted, one-handed) users |
| LOW (COGA/content) | `#ateljekvallar`, :260–266 | Heading + one paragraph, no link, no contact method — despite stating "Max tio platser" (implying a capacity to reserve against) | Add a real action (mailto or anchor to a contact point), matching `#brollop`'s pattern | No primary action exists for this task at all — cognitive walkthrough fails outright ("will the user see a way to make progress?" → no) | No direct SC — content completeness | All visitors interested in ateljékvällar; not accessibility-specific, flagged for completeness |
| LOW | `.about-section h2` (:126, 28px) vs `.about-section h3` (:127, 25px), `#om` | Two adjacent heading levels sit within 1.15× of each other | Widen the ratio, reusing the existing type scale from the hero/ledger sections rather than a new size | DOM nesting is correct (h2→h3, no skipped level) but the visual hierarchy nearly flattens, weakening the "scan by heading" cue for low-vision/skimming users | No direct SC — visual hierarchy | Low-vision users and anyone skimming rather than reading in full |
| LOW | Page-wide `font-size` declarations outside the headings' `clamp(...rem...)` rules — e.g. body :36, `.kicker` :44, `.lede` :75, `.ledger-desc` :91, `.ledger-price small` :94, `.about-section h3` :127, `.info-block p` :129, `footer p/a` :136, `nav a` :55, `.btn-primary` :61–62, `.cta-quiet` :116 | Nearly every body/UI-text size is hardcoded in `px`; headings already use `rem` correctly inside their `clamp()` calls | Extend the same `rem` pattern to body copy, labels and buttons | A user with a custom OS/browser base font size (not zoom) gets no benefit outside headings. WCAG 1.4.4 Resize Text itself is satisfied — `reflow.py` confirms clean reflow at 200% zoom — so this is an adaptive-pass best-practice gap, not a hard failure | No direct SC (1.4.4 met via zoom) — adaptive/`rem` principle | Users with a custom base font-size preference, common for low vision, who don't additionally zoom |

One row per root cause; every location a systemic issue reaches is listed in that row.

## Persona walkthrough

| Persona | Condition type | Key task | Result | Barrier (if any) |
| --- | --- | --- | --- | --- |
| Screen-reader user (blind, NVDA) | Permanent | Boka bröllopsmöte | Works | Reaches the mailto link fine; landmark gaps (finding 5) add extra listening to get there |
| Screen-reader user (blind, NVDA) | Permanent | Notice Dahliabukett is sold out before ordering | Fails | `aria-hidden` dot, no text (finding 1) |
| Colorblind user (deuteranopia) | Permanent | Notice Dahliabukett is sold out | Fails | Same red dot reads as "just another accent mark" with no colour-independent cue (finding 1) |
| Keyboard-only user (temporary wrist injury) | Temporary | Tab to footer social/newsletter links | Works with friction | Ring present but under 3:1 against the ink background (finding 4) |
| Keyboard-only user (temporary wrist injury) | Temporary | Starta prenumeration | Fails | Dead `href="#"` (finding 7) — silent no-op with no differentiating feedback for a non-visual user |
| Low-vision user, 200% browser zoom | Permanent | Read either figure's caption | Fails | 2.50:1 contrast (finding 2), independent of zoom level |
| Low-vision user, 200% browser zoom | Permanent | Reflow / read the whole page | Works | `reflow.py` confirms no overflow at 200% zoom or 320px width |
| Parent, one hand on a phone, bright sunlight | Situational | Beställ bukett vs. Boka bröllopsmöte — pick one, fast | Works with friction | No default action between the two identical CTAs (finding 9) adds a decision under time pressure |
| Parent, one hand on a phone, bright sunlight | Situational | Boka ateljékväll | Fails | No CTA exists for this task at all (finding 10) — universal gap, not persona-specific, but compounds under time pressure |

A task that fails for any persona is listed as a finding above regardless of how it looks for the rest.

## What works well

- `prefers-reduced-motion` is handled correctly on both layers: the CSS fails toward visible (`opacity:1; transform:none; transition:none`) and the JS gate checks the same media query before ever registering the `IntersectionObserver`, rather than relying on CSS alone to neutralise a scroll-triggered reveal. `reflow.py` confirms 0 elements left `opacity:0` under reduced motion.
- Both photographs carry specific, meaningful alt text ("Nybunden sensommarbukett med dahlior och flox…", "Blomsterhinkar med säsongens snittblommor…") rather than generic or filename-derived text.
- `<html lang="sv">` matches the actual page language throughout.
- No overflow at 320px width or 200% zoom (`reflow.py`, clean on both checks).
- Every interactive element is keyboard-reachable in visual reading order with a visible focus indicator present (`tab_walk.py`: 11/11 stops, 0 issues) — the contrast of that indicator in one context is the only gap (finding 4).
- Reading level throughout is plain, concrete Swedish with short sentences — no jargon, no lorem, no invented numbers, consistent with the brief.

## Legal map

| Framework | Status | Notes |
| --- | --- | --- |
| WCAG 2.2 AA | Gaps: 1.4.1, 1.4.3 (×2 pairs), 1.4.11/2.4.13, 1.3.1 (×2), 2.5.8 | 4 of these are escalation-trigger HIGHs |
| EAA / EN 301 549 | In scope, gaps mirror WCAG | Aligned with WCAG 2.1 AA plus additional requirements not separately triggered here |
| ADA (US) | Risk noted | Case law references WCAG 2.1 AA; the colour-only status indicator and contrast pairs are the kind of finding that shows up in ADA web-accessibility litigation |
| Section 508 (US gov) | Not applicable (Swedish commercial site) | Noted for completeness only |

## SEO-relevant findings

Missing `<main>` landmark and the heading/label inconsistency in the info-grid (findings 5 and 6) are SEO-relevant — the same structural signals crawlers and screen readers both depend on. Alt text, `lang`, link text and reflow are otherwise clean, so no additional SEO flags there.

## Deferred to accessibility debt

This agent is read-only and did not write to `.impeccable/a11y-debt.md` (no such file exists yet in this project). The following should be appended there, pending the user's explicit acknowledgement of accepting any of it as debt rather than fixing now:

- All MEDIUM and LOW findings above, if not fixed in this round — deadlines per the project's standard triage (major: 30 days, minor: 90 days).
- Mobile (390px) hit-area re-measurement for the header nav (finding 8's mobile caveat) — not verified in this pass, only the desktop viewport was measured.
- The CARL fixture (`tests/a11y/broken.html`) does not exist in this project. Per the audit procedure it should be created and run through `a11y_scan.py`/`tab_walk.py`/`reflow.py`/`contrast.py` once, to confirm each script actually catches a known-broken page, before any future clean run from these scripts is trusted at face value. This agent could not create it (read-only).

None of the above has been acknowledged by the user yet — treat as proposed debt, not logged debt.

## Verdict

**Block** — four HIGH findings remain (sold-out state carried by colour alone and hidden from assistive tech; two failing text-contrast pairs; the footer's own focus-ring contrast). Do not ship until those four are fixed. The MEDIUM/LOW findings stay in the table as work to do; none of them individually blocks on their own.
