# Accessibility audit — Klova Bokning signup + dashboard (`B-with/index.html`)

## 0 · Scope + coverage

Target: `C:/Users/Anton L/anti-slop-design/tests/ab/02-a11y/B-with/index.html`, source built for this audit, no other file inspected. Build was blind one-shot (no screenshots taken at any point). Review method: mechanical scripts against the live default view (`#signup`, step 1), plus a full source read of markup/CSS/JS for both the signup and dashboard views and the booking modal — no interactive browser session beyond the three scripts.

| Domain | Coverage |
| --- | --- |
| Mechanical (axe, keyboard walk, reflow) | **Verified** — ran against the rendered `#signup` step-1 view (the page's default state; `a11y_scan.py`/`tab_walk.py` don't execute app JS to navigate hash state, so `#dashboard` and the booking modal were not scanned live) |
| Signup flow (all 3 steps), summary step, validation logic | **Verified from source** — markup/ARIA/JS logic read directly, not runtime-executed |
| Dashboard, KPI row, bookings table, "Ny bokning" modal | **Verified from source** — not exercised by the mechanical scripts (see above); markup/ARIA/JS read directly |
| Rendered contrast | **Not runtime-measured** (`contrast.py`/`contrast_over_media.py` not run per task scope) — computed by hand from the declared token hex values using the WCAG relative-luminance formula; reported as computed, not pixel-measured |
| Screen-reader announcement, actual tab order, computed focus styles | **Inferred** from source + `tab_walk.py`'s simulated walk of the default view only; not confirmed with a real screen reader |
| Table→card collapse under `display:block` at ≤640px | **Inferred** — known CSS/AT interaction, not confirmed in a live browser at that breakpoint (see Finding 5) |

## 1 · Mechanical pass — before / after

| Script | Before | After |
| --- | --- | --- |
| `a11y_scan.py` (axe-core, desktop+mobile merged) | 0 violations, 42 passes, 0 incomplete | 0 violations, 42 passes, 0 incomplete |
| `tab_walk.py` (--max 200) | 6 stops, **1 issue**: `offscreen` — skip link's focused position lands off-viewport (`top: -48`) | 6 stops, **0 issues** — skip link focused position now `top: 12`, `inViewport: true` |
| `reflow.py` | `overflow320: []`, `overflowZoom200: []`, `hiddenUnderReducedMotion: 0` | same — `overflow320: []`, `overflowZoom200: []`, `hiddenUnderReducedMotion: 0` |

**CARL note:** the project's `tests/a11y/broken.html` fixture (used to confirm these three scripts actually catch a known-bad page before trusting a clean run) does not exist yet in this project and was out of scope to create under this task's "read nothing else" instruction. The clean `a11y_scan.py`/`reflow.py` results above should be read as "no violations these scripts are built to catch," not as an independently re-verified clean bill — flagging per the skill's own rule rather than silently upgrading confidence.

axe-core only evaluates the DOM state at load (`#signup`, step 1) since it doesn't execute the page's own hash-router JS to reach the dashboard or open the modal — those were audited from source in passes 2–7 below, not mechanically scanned.

## 2–7 · Findings

| Severity | Location | Before | After | Why | WCAG | Who |
| --- | --- | --- | --- | --- | --- | --- |
| **HIGH** | Skip link (`.skip-link`) | Position transitioned from `top: -3rem` to `top: var(--space-3)` on `:focus-visible`; `tab_walk.py` measured the focused element still off-viewport (`top: -48`) | Transition removed — position change is instant on focus | A skip link's entire purpose is to be usable the instant it receives focus. A tool measuring it off-viewport right after focus is a credible signal that a keyboard user's first Tab press doesn't reliably land on a visible target — this is the archetypal WCAG 2.4.1 failure pattern (a skip link that "doesn't work" for at least one input cycle) | 2.4.1 Bypass Blocks (A) | Keyboard-only users, screen-reader users navigating by Tab |
| **HIGH** | `#new-booking-form` submit handler (Tid, Gäst, Antal gäster) | On an invalid submit, the handler only called `.focus()` on the first empty required field — no `aria-invalid`, no error text, no visible state change | Rewrote to use the same `setFieldError()` pattern as the signup wizard: sets `aria-invalid="true"`, replaces the field's helper text with a plain-language error, and clears it once the field is valid | A keyboard or screen-reader user who submits an incomplete booking gets silent refocus with zero explanation of what happened or what to fix — this is exactly the "error names no way to recover" escalation trigger, and it left both sighted users (no visual error state at all) and AT users (no announced reason) equally stranded | 3.3.1 Error Identification (A), 3.3.3 Error Suggestion (AA) | Keyboard users, screen-reader users, and — since there was no visual error either — sighted users who click but don't notice which field emptied |
| MAJOR | Bookings table (`table.bookings`) mobile collapse, ≤ 40rem | `display: block` applied to `table/tbody/tr/td` at narrow widths (the standard "table → card" technique) strips the browsers' implicit table/row/cell/columnheader roles in most engines, even though the visual `data-label::before` text keeps the pairing legible on screen | Added explicit `role="table"` (table), `role="rowgroup"` (thead/tbody), `role="row"` (every `<tr>`, static and JS-added), `role="columnheader"` (`<th>`), `role="cell"` (every `<td>`, static and JS-added) via a small `ensureTableRoles()` init pass plus inline roles on dynamically inserted rows | Content stays reachable and the data-label pairing survives visually and in the flat accessibility-tree text, but screen-reader *table navigation commands* (jump to next cell/row, announce column header on cell move) depend on the table/row/cell role chain, which `display: block` silently removes in most browsers — a real, well-documented CSS/AT interaction, not a hypothetical | 1.3.1 Info and Relationships (A) | Screen-reader users on a phone-width viewport who rely on table navigation rather than linear reading |
| MINOR | Password-visibility toggle (`.field-toggle`) | Hit target 47×36 CSS px — under the 44×44 recommended touch target (passes the WCAG 2.5.8 AA floor of 24×24, but not the project's own interaction standard) | Added a `::before` hit-area expansion (`inset: -5px`) so the clickable region is ≥ 44×44 while the visible chip is unchanged | A 36px-tall control next to a 44px input is a common mis-tap source on touch, especially since this sits directly beside the password field it's meant to help with | 2.5.8 Target Size (Minimum) (AA) — passes; deviates from the interaction-and-states.md 44×44 recommendation | Touch and low-precision-pointer users (tremor, one-handed phone use) |
| MINOR | Modal close button (`.btn-icon`, the × in "Ny bokning") | Hit target 40×40 CSS px — meets the "reasonable desktop target" floor but under 44×44, and the modal is reachable on the 390px mobile viewport too | Added a `::before` hit-area expansion (`inset: -2px`) bringing it to 44×44 | Same touch-target rationale as above, on a control that's the only visible way to dismiss the modal besides Escape/backdrop-click | 2.5.8 Target Size (Minimum) (AA) — passes; deviates from the 44×44 recommendation | Touch users on the 390px viewport |
| MINOR | Modal sizing (`dialog.modal`, `.modal__body`) | `max-height` used `vh` (`85vh`, `60vh`) | Switched to `dvh` (`85dvh`, `60dvh`) | `vh` doesn't account for mobile browser chrome (address bar) showing/hiding, which can clip or misjudge the modal's available height on phones; `dvh` tracks the actual visible viewport. Explicitly banned by the project's own responsive reference for anything that interacts with mobile chrome | 1.4.10 Reflow (AA) — defensive, not a confirmed failure | Mobile Safari/Chrome users opening "Ny bokning" |
| MINOR | Consent checkbox `<label>` (step 3) | `<label class="checkbox-field" for="consent" id="consent-label">` both wrapped the checkbox **and** carried a redundant `for="consent"` pointing at the same id | Removed the redundant `for` attribute; the wrap alone is a sufficient explicit association | Not a failure (browsers resolve the duplicate association fine), but redundant markup is exactly the kind of "almost right" pattern the audit should catch before it's copied elsewhere in the codebase | — (code-quality, not a WCAG citation) | n/a — hygiene, not a barrier |
| MINOR | Final-submit navigation (signup step 3 → dashboard) | `location.hash = "#dashboard"` was set **and** `showView("dashboard")` was called directly, so the `hashchange` listener fired a moment later and ran `showView` a second time — double-focusing (and, on some screen readers, potentially double-announcing) the dashboard `<h1>` | Removed the direct call; the `hashchange` listener is now the single path that shows the view and moves focus | Minor extraneous cognitive load (COGA) — a screen-reader user landing on the dashboard could hear "Dashboard" announced twice for one action, which reads as a glitch rather than a confirmation | — (COGA / extraneous load, not a specific WCAG SC) | Screen-reader users completing signup |
| MINOR (fixed proactively) | Modal backdrop (`dialog.modal::backdrop`) | Semi-transparent overlay only, no branch for `prefers-reduced-transparency` | Added `@media (prefers-reduced-transparency: reduce) { ::backdrop { background: var(--color-ink); } }` | Low actual impact — no legible text sits on the translucent layer itself, it only dims the page behind an opaque modal card — but the adaptive pass calls for respecting this preference wherever a translucent surface exists, and the fix was one line | 1.4.11 Non-text Contrast (AA), adjacent | Users with `prefers-reduced-transparency` set (vestibular/visual sensitivity to blur or see-through layers) |

### Confirmed correct (checked, not a finding)

- Both views (`#signup`, `#dashboard`) each carry exactly one `<h1>`; the inactive view uses the native `hidden` attribute, so axe and any AT correctly see only one at a time, including with JS disabled (dashboard is `hidden` in the static markup too).
- Status is never color-only: each badge's **word** differs (`Bekräftad`/`Väntar`/`Avbokad`), independent of the decorative colored dot; passes the greyscale test as-is.
- Error text replaces (never duplicates) helper text in the same slot with a reserved `min-height: 1lh`, matching the no-layout-shift rule.
- Focus rings use `:focus-visible`, 2px, with a hand-computed ≥3:1 contrast pair in both contexts that matter (ink-on-ground ≈15:1; ink-on-accent ≈3.15:1, clearing the ≥3:1 floor for a non-text UI element).
- The signup wizard never disables its submit/"Fortsätt" buttons; validation runs on submit, focuses the first invalid field, and never clears what the user typed.
- Password value is never redisplayed in the step-3 summary (shown as "Angivet", not the literal value).
- `<dialog>` is used natively for the modal (native focus trap, `::backdrop`, Escape-to-close), centered explicitly per the interaction reference's pinning pattern; first focus on open goes to the first field (`Tid`), not the close button; focus returns to the "Ny bokning" trigger on close.
- `tab_walk.py`'s reported accessible names include the literal `*` character (e.g. `"E-postadress\n*"`) because the script's own name-extraction is a simplified `innerText`-style approximation, not the spec's accessible-name algorithm. The asterisk is marked `aria-hidden="true"` in the source, and `a11y_scan.py` (axe-core, which does implement the accname algorithm) reported no name-related violations — so the actual computed accessible name a screen reader announces is `"E-postadress"`, not `"E-postadress *"`. Noted here for transparency rather than silently treated as a pass.

## 8 · Verdict

**Approve**, conditional on the fixes above (all applied in this round — see the after-column and the clean re-run in §1). No `HIGH` finding remains unresolved.

## Legal map

All findings above map to WCAG 2.2 AA success criteria (2.4.1, 3.3.1, 3.3.3, 1.3.1, 2.5.8, 1.4.10, 1.4.11). WCAG 2.2 AA is the baseline EAA/EN 301 549 reference since June 2025; ADA and Section 508 case law both reference WCAG. No jurisdiction-specific gap identified beyond the standard AA mapping.

## SEO flag

The MAJOR table-semantics finding (Finding 3) is SEO-relevant: `role="table"/"row"/"cell"` restores the same structural signal search crawlers use to parse tabular data, which `display: block` alone would have obscured for crawlers as much as for screen readers. Heading hierarchy, alt text, and `lang="sv"` were all checked and are correct — no additional SEO-relevant findings.

## Deferred / accessibility debt

Nothing deferred. All findings identified in this audit were fixed in the single edit round described above; none required the user's explicit debt acknowledgement.

## Testing-pyramid note

This audit covers the automated layer (`a11y_scan.py`, `tab_walk.py`, `reflow.py`) and a manual expert source-read (POUR/COGA/content/adaptive/interaction/persona passes) — roughly the first two of the pyramid's three layers. It does not include testing with actual disabled users (the pyramid's remaining ~20%), which is recommended before this surface ships to real users.
