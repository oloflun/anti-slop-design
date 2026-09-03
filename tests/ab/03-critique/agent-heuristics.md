# Heuristic evaluation -- Florhuset Majorna (planted.html)

**Scope note:** This is a single static local HTML file (planted.html) with only in-page anchor links (#buketter, #brollop, #prenumeration, #ateljekvallar, #om) plus two href="#" footer placeholders and one mailto: link. There is no sub-page structure to discover, and none was attempted -- sitemap/robots.txt discovery does not apply to a local static fixture. All findings below are based on the rendered HTML/CSS/JS in this one file and the seven screenshots supplied (planted--s00 through s05, --fold, --full). **All seven screenshots are the same desktop-width (~1440px) viewport, scrolled to different points** -- no phone-width screenshot was provided. Findings for the first-time-visitor-on-a-phone persona are therefore partly inferred from the CSS (media max-width:820px rules, flex-wrap nav, single-column grids) rather than visually confirmed, and are flagged as such below.

HTML comments in the source were treated as absent per instructions; all findings come from rendered behavior, not the planted-defect annotations.

## Summary

The page reads cleanly and the ledger/info-grid patterns support quick scanning, but the two key conversion tasks are not equally supported: booking a wedding meeting works (a real mailto: action exists, if easy to miss), while ordering a bouquet has no completion path at all -- the primary hero button leads to a static price list with no order, contact, or add-to-cart affordance anywhere near it. Combined with a color-only sold-out indicator and two co-equal hero CTAs with no default action, a first-time visitor on either device can get most of the way through the funnel and then simply have nowhere to go.

## Heuristic findings

| # | Heuristic | Verdict | Key finding |
|---|---|---|---|
| 1 | Visibility of system status | Fail | No ordering feedback exists anywhere (nothing to click); sold-out state has no visible status text, only a color dot; no current-section indication in nav while scrolling |
| 2 | Match between system and real world | Caution | CTA labels match intent well (Bestall bukett, Boka brollopsmote), but Boka implies scheduling while the mechanism is only a plain email link |
| 3 | User control and freedom | Caution | No sticky header or back-to-top; once scrolled past the hero, returning to either CTA means a full manual scroll |
| 4 | Consistency and standards | Fail | Two hero buttons share identical primary styling with no default action; the About section three parallel info items (Adress/Oppettider/Hitta hit) mix two different label treatments |
| 5 | Error prevention | Fail | Clicking the primary order CTA sets an expectation (purchase) the page cannot fulfill; sold-out item is not flagged in text, so a visitor could pursue an unavailable item |
| 6 | Recognition rather than recall | Pass | Ledger keeps name, description, and price together in one scannable row; vas ingar ej repeated consistently avoids surprises |
| 7 | Flexibility and efficiency of use | Fail | No shortcut exists to actually transact -- no phone/email link repeated near the ledger for people who already know what they want |
| 8 | Aesthetic and minimalist design | Caution | Generally uncluttered, but three consecutive sections (Brollop/Prenumeration/Ateljekvallar) share identical anatomy and padding drifts inconsistently (96/116/84/120px) |
| 9 | Help recognize/diagnose/recover from errors | Fail | mailto: link has no fallback if no mail client is configured; footer href="#" links look actionable but do nothing |
| 10 | Help and documentation | Caution | No delivery cost/lead-time/FAQ near the ordering CTA for a first-time visitor who has basic questions before committing |

## Cognitive walkthrough results

### Task A -- First-time visitor on a phone, wants to order a bouquet
1. Right goal formed? Yes -- hero headline and lede (Vi binder det som ar i sasong...) set up order a bouquet as the obvious next step.
2. Notice correct action? Yes, but with hesitation -- Bestall bukett sits next to an equally weighted Boka brollopsmote button (same fill, same size), so nothing signals which is the default/primary action for a visitor who has not decided yet.
3. Associate action with effect? Tap Bestall bukett -> jumps to #buketter, a static ledger of four items with prices. No button, link, phone number, or select affordance exists on or near any row.
4. See that progress was made? No -- critical failure. The visitor has reached a price list and can go no further on this page. There is no order form, no per-item action, and no contact prompt anywhere in or near the ledger. They would have to independently guess to scroll to the footer for a phone number or email, with nothing in the ledger section pointing them there.

### Task B -- First-time visitor on a phone, wants to book a wedding meeting
1. Right goal formed? Yes.
2. Notice correct action? Yes -- Boka brollopsmote is a clearly labeled hero button.
3. Associate action with effect? Tap -> jumps to #brollop, a paragraph ending in an italic, underlined mailto: link (Skriv till oss om ert datum) embedded mid-sentence. The visual language shifts from a filled button to plain body-style text, so the actionable step requires reading the whole paragraph rather than spotting an obvious next button.
4. See that progress was made? Partially -- if the phone has a mail client configured, tapping opens a pre-addressed email (real progress). If not (increasingly common with webmail-only phone setups), nothing visibly happens and there is no adjacent phone number or web form as fallback -- the visitor is stranded with no diagnostic cue about what went wrong.

### Task C -- Returning customer on desktop, wants to reorder a bouquet by name
1. Right goal formed? Yes, uses header nav BUKETTER directly -- efficient path for a repeat visitor (heuristic 6 pass).
2. Notice correct action? Yes, nav label is unambiguous.
3. Associate action with effect? Scrolls to the ledger, finds the item by name and price quickly.
4. See that progress was made? No -- same critical gap as Task A. Even a confident, returning customer who knows exactly what they want cannot complete a purchase in-page; they must already know from a prior visit that phone/email in the footer is the real channel, since nothing here confirms it.

### Task D -- Returning customer on desktop, checks whether Dahliabukett is available
1. Right goal formed? Yes, scans the ledger for the item.
2. Notice correct action? N/A -- there is no action, only a status to read.
3. Associate the visual cue with meaning? Weak -- the row shows an 8px red dot with aria-hidden=true and no text anywhere near it. The same accent red is also used for the primary CTA buttons and the Mest bokade badge elsewhere on the page, so red carries at least three different meanings (call-to-action, positive social proof, and unavailability) with no other distinguishing cue. A visitor skimming for prices could plausibly miss the dot entirely, or misread it as decorative.
4. See that progress was made? No -- the visitor gets no confirmation either way and would only learn the item is sold out after contacting the shop, i.e., after the task should have already been resolved.

## Findings by severity

### Critical
1. No mechanism to complete a bouquet order anywhere on the page. The primary hero CTA (Bestall bukett) leads only to a static ledger with zero order/contact affordance per item or for the section as a whole. (Heuristics 1, 5, 7) -- Fix: add a per-item or section-level order action (mailto/tel/form) directly in or immediately below the ledger.
2. Sold-out status is conveyed by color alone, via a small aria-hidden dot reusing the same accent red as the CTA buttons and the Mest bokade badge, with no text label anywhere nearby. (Heuristics 1, 9) -- Fix: add a visible Slutsald text label, remove aria-hidden, and use a color/shape distinct from the CTA red.
3. Two hero CTAs render as identical, equally weighted primary buttons (Bestall bukett / Boka brollopsmote), giving no signal about which is the default action for an undecided visitor. (Heuristic 4) -- Fix: pick one as visually primary (filled) and demote the other to a secondary treatment (outline/text).

### Major
4. The real conversion link in the subscription section is visually quieter than a decorative element beside it -- Starta prenumeration is a small grey underlined text link, while the non-actionable Mest bokade badge above it uses the loud filled-accent treatment. (Heuristics 4, 8) -- Fix: swap the weighting so the actual CTA is the loudest element in the section.
5. The wedding-meeting CTA is a mid-paragraph mailto: link with no fallback if the device has no configured mail client, and no phone number placed next to it. (Heuristics 2, 9) -- Fix: present it as a standalone button/link with a phone-number fallback alongside.
6. No sticky header or back-to-top control on a long single-page layout -- once a visitor scrolls to Om ateljen or the footer, returning to either ordering CTA requires a full manual scroll back up. (Heuristic 3) -- Fix: sticky header, or repeat a CTA near the page bottom.
7. Footer Nyhetsbrev and Instagram links point to href="#" -- they look clickable but do nothing, a false affordance for a first-time visitor trying to follow up later. (Heuristics 5, 9) -- Fix: link to real destinations or remove until ready.

### Minor
8. Caption/meta text reads faintly against the cream ground (image captions, vas ingar ej notes) -- easy to miss on a quick scan even though legible on close reading; the precise contrast measurement is a11y territory, but the practical effect is that price fine print and photo captions can go unnoticed during normal scanning speed. (Heuristic 8)
9. Three consecutive sections (Brollop / Prenumeration / Ateljekvallar) share identical anatomy -- kicker plus heading plus paragraph, same cream ground, no imagery -- so a visitor scrolling specifically for the wedding section can scroll past it without it registering as a distinct, actionable module. (Heuristics 6, 8) -- Fix: vary at least one section with imagery, a ground-tone shift, or a different layout.
10. Section vertical padding drifts with no shared scale (96/116/84/120px) -- does not block a task, but undercuts the predictable rhythm that helps a scrolling visitor sense new topic. (Heuristic 4)
11. Inconsistent label treatment across three parallel info items in the About section -- Adress and Hitta hit use the small kicker style, Oppettider uses a heavier h3 -- a small scan-consistency wrinkle for equivalent facts. (Heuristic 4)
12. Nav relies on flex-wrap rather than a collapse pattern for five items at narrow widths -- plausible readability/height risk on a phone, but this could not be visually confirmed since no phone-width screenshot was captured; recommend verifying at roughly 375-420px before relying on this evaluation for the mobile persona. (Heuristic 8, discovery limit)

## What works well
- The ledger keeps name, description, and price aligned in one consistent, scannable row pattern -- strong recognition-over-recall for comparing options.
- Vas ingar ej is repeated consistently under every price, avoiding a late surprise about what is included.
- Reduced-motion is handled correctly: the CSS media query neutralizes the scroll-reveal animation, and the JS includes a load-timeout failsafe that reveals content even if IntersectionObserver never fires -- a genuine fail-toward-visible safety net.
- Om ateljen answers the practical questions a first-time visitor planning a pickup actually has (address, hours, transit stop, bike parking) in one glanceable grid.
- Copy throughout is concrete and specific (named growers, real week numbers, named neighborhoods for delivery) rather than generic marketing language, which builds the kind of trust a visitor needs before committing to an order.

## Recommendation

Revise. The information architecture, tone, and scannable ledger pattern are sound and do not need rebuilding, but the page currently cannot complete its own stated key task (ordering a bouquet) and undersells its secondary task (booking a wedding meeting) through low-contrast CTA styling and a buried link. These are fixable within the existing structure, not a sign the structure itself is wrong.
