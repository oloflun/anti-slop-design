# Heuristic evaluation — Alunix, run B/K1

URL: http://127.0.0.1:3201/tests/alunix-ab-r7/runs/B/K1/index.html
Source: `tests/alunix-ab-r7/runs/B/K1/` (index.html, script.js, scrollcraft.js, style.css, scrollcraft.css)
Method: Playwright (Chromium), desktop viewport 1440x900, motion build and prefers-reduced-motion build, both scripted and screenshotted. No files edited.

## Summary

The page communicates what Alunix sells and gets a visitor to the price list and the contact address cleanly in both the motion build and the reduced-motion build -- that core path works. But the signature set-piece's "live, clickable" iframe is a broken affordance in the motion build (every pixel of it is covered by an invisible decoy image, so no mouse click ever reaches it) and a scroll trap in the reduced-motion build (the mouse wheel is fully captured by the embedded site, and page-scroll stops dead). A keyboard-only visitor tabbing from the header skips the entire middle of the page -- camera push-in, the demo iframe, all three proof rows, and the whole price list -- landing on the footer contact link on the third Tab press. These are usability failures independent of any contrast/ARIA finding a11y review would raise on the same elements.

## Heuristic findings

| # | Heuristic | Verdict | Key finding |
|---|---|---|---|
| 1 | Visibility of system status | Caution | Global progress bar gives scroll-position feedback, but nothing signals why the wheel briefly stops responding when it is captured by the reduced-motion iframe (see Critical #1) |
| 2 | Match between system and real world | Pass | "Fonstret ar Horai" caption + topbar label ("Exempelsida: Horai...") correctly frame the metaphor; Swedish price list reads like a real quote sheet |
| 3 | User control and freedom | Fail | Reduced-motion iframe captures the wheel (page scroll delta 0 across 6 wheel ticks placed over it); motion build's pinned scene has no skip control and needs roughly 2.7 screens of scroll to clear |
| 4 | Consistency and standards | Fail | The two builds fail in opposite ways on the same feature: motion build's "clickable" frame is unclickable (blocked by a stacked decoy), reduced-motion's is clickable but traps scroll. Visitors who reduce motion get a functionally different, not just visually calmer, page |
| 5 | Error prevention | Caution | No destructive actions on the page (mailto + price list only), so little surface for this heuristic; the one candidate error (dead-end click on the frame) produces no feedback at all, not even a cursor change |
| 6 | Recognition rather than recall | Pass | Site names ("Calyx, Horai, Hyperborea") are repeated at hero and at each proof row; price list rows are self-contained, no scrolling back needed to compare |
| 7 | Flexibility and efficiency of use | Fail | No way to jump straight to the price list or contact for a returning visitor; Tab-only navigation ironically "skips" to the end (see Critical #2) but does so by omission, not as an intentional shortcut |
| 8 | Aesthetic and minimalist design | Caution | Horai's own "RESERVATIONS" button and Alunix's "kontakt@alunix.se" pill occupy the same top-right corner simultaneously during the pinned scene, competing for the same visual slot |
| 9 | Help users recognize, diagnose, and recover from errors | Fail | Clicking the visibly-styled RESERVATIONS button, HORAI logo, or book.horai.se link during the pinned window does nothing -- no cursor affordance, no console warning, no visual response |
| 10 | Help and documentation | N/A | Marketing single-pager; not applicable |

## Cognitive walkthrough -- "Understand offer, see proof, reach price list, find contact"

### Path A: scrolling visitor, motion build (primary persona)

1. Land on hero. Will the user try to achieve the right effect? Yes -- headline "Er hemsida ar nutidens visitkort" plus subhead states the offer plainly. Will they notice what to do next? Yes, the page fills the viewport with no visible chrome inviting a click, so scrolling is the obvious next action. Pass.
2. Scroll through the camera push-in (about 2.3 screens of scroll). Will they associate scrolling with progress? The thin top progress bar ticks up, so yes. But there is no content payoff for roughly the first screen and a half beyond the hero fade, just city imagery, so a visitor unsure whether the page is "loading" or simply long has only the progress bar as reassurance, and it is a 2px line easy to miss. Uncertain.
3. Window resolves into the live Horai frame; topbar shows "Exempelsida: Horai, Asian fusion-koncept"; a "RESERVATIONS" button is visible. Will the user try to interact with it, given it visually presents as a real, live website? Very likely, given the button styling and layout. Do they notice the correct action is available? They perceive an action that is not actually available: every click in this entire scroll window lands on an invisible image, not the iframe. Confirmed with Playwright: document.elementFromPoint at viewport center returns IMG.exit-frame at every sampled progress value from 0.50 to 0.71, because .exit-frame-wrap (z-index 3, opacity 0 until 0.70) sits in front of .reveal-frame-slot iframe (z-index 2) for the iframe's entire visible lifetime. Clicking produces zero feedback. Fail, Critical.
4. Proof rows (Design / Utveckling / System), each naming an example site. Will they recognize this as evidence for the claims above? Yes, images plus site names read clearly, and the Horai still visible in row 2 echoes the frame they just could not click. Pass, but the near-miss from step 3 has already taught the visitor that images on this page which look like buttons are not clickable, which will make them hesitate before clicking anything else, including the real mailto link later.
5. Price list ("Alla har ratt till bra design"). Three rows, tiered pricing, hairlines animate in per-row on scroll. Clear, scannable, no ambiguity about what is included. Pass.
6. Contact ("kontakt@alunix.se" at the very bottom, and mirrored in the persistent header the whole time). The header contact link is visible and legible (light text, drop-shadow for contrast) from the very first frame of the page, so a visitor who wants to skip straight to contacting Alunix never actually needs to reach the footer. Pass, this is the strongest part of the flow.

### Path B: keyboard-only visitor (Tab, no mouse-wheel scrolling)

1. Page loads, focus is on body. First Tab goes to topbar__mark (logo, jumps to #top). Second Tab goes to topbar__contact (mailto). Both fine, expected order.
2. Third Tab jumps directly to the landing-mailto link and the page scrolls from scrollY 0 to scrollY 6775 in one jump (measured directly). The camera push-in, the "live" demo iframe, all three proof rows, and the entire price list are skipped -- none of that content has a focusable element, and the one focusable element inside the pinned scene (the iframe) is visibility:hidden outside its narrow 22-percent-of-500vh window, so it is never in the tab order when the page is at rest. A keyboard-only visitor cannot reach the price list at all via Tab; they would have to already know to use PageDown or arrow keys instead. Fail, Critical, since "reaches the price list" is one of the four things this walkthrough is explicitly testing, and it fails outright for this input method.
3. If a user instead scrolls into the pinned window first and only then presses Tab, focus does successfully land on the iframe's three internal links (Horai logo, RESERVATIONS, book.horai.se, confirmed via iframe.contentDocument, 3 focusable elements) and later cycles correctly through mark, contact, landing-mailto. So keyboard support exists for the iframe, but only for a visitor who is already scrolled to the right part of the page, which the Tab key itself will never take them to.

### Path C: reduced-motion visitor

1. Hero, then a static "window" formed on a still photo ("fonstret ar Horai"), a clean substitute for the camera move, message received without any motion. Pass.
2. Directly below, a second section holds the actual live iframe, captioned "Exempelsida: Horai, Asian fusion-koncept." This is genuinely clickable this time (elementFromPoint returns the IFRAME itself here) -- the reduced-motion build does not have the exit-frame-wrap stacking bug, since that element only exists in the motion build's markup. Pass on affordance.
3. But scrolling past it is where control breaks. With the cursor positioned over the iframe (a realistic position, it is the widest element on the page) and 6 wheel ticks sent, the parent page's scrollY did not move at all, while the iframe's internal scrollY advanced to 1800px -- the visitor is now reading Horai's own "Cooking is a conversation..." quote section, not Alunix's page. The only way out is to move the mouse off the iframe's bounding box and scroll again, which nothing on the page tells them to do. Fail, Critical.
4. Once past it, by luck or by moving the pointer, proof rows, price list, and contact are all plain scrolling content with no further traps.

## Findings by severity

### Critical

1. [H3, H9] The motion build's "live, clickable" iframe cannot be clicked at all. .exit-frame-wrap (z-index 3) sits in front of .reveal-frame-slot iframe (z-index 2) for the iframe's entire visible window (p 0.50 to 0.71); its opacity:0 in that range does not remove it from hit-testing (no pointer-events:none, no visibility:hidden), so document.elementFromPoint returns the invisible .exit-frame image at every sampled point, not the iframe -- confirmed at p = 0.50, 0.52, 0.55, 0.58, 0.60, 0.63, 0.66, 0.68, 0.70. Screenshot: heur-motion-03-iframe-live-p60.png (shows a fully-rendered RESERVATIONS button that is not actually reachable by any click). Fix: add pointer-events:none to .exit-frame-wrap for as long as --xfade2 is 0, or gate it with the same sigAct.live-and-frameVisible check script.js already applies to the iframe's own visibility.

2. [H3, H4] Reduced-motion build's iframe captures the mouse wheel; parent page scroll stops dead. With the pointer over .rm-frame-slot iframe and 6 wheel events (300px each) dispatched, page scrollY delta was 0 while the iframe's internal scrollY reached 1800px. Screenshots: heur2-rm-frame-centered.png (before) then heur2-rm-frame-after-wheel.png (after -- visitor is now inside Horai's own quote section, Alunix's page appears to have stalled). Fix: constrain the iframe so it never has internal scroll room within the visible frame (fixed-height sandboxed preview), or replace wheel-scrollable embedding with a static screenshot plus an "open example" link that opens the real site in a new tab.

3. [H3, H7] Keyboard-only (Tab) navigation skips the entire body of the page. From scrollY 0, three Tab presses go topbar mark, then topbar contact, then straight to the landing mailto link, jumping scrollY from 0 to 6775 in one step. The pinned camera scene, the demo iframe, all three proof rows, and the full price list have no focusable elements reachable from page load, because the iframe is visibility:hidden outside its narrow scroll window. A keyboard-only visitor never sees the proof or the price list via Tab. Fix: either make the iframe programmatically reachable regardless of scroll position (with a tabindex/focus-management pattern that also scrolls it into view, matching the existing focusin handler already used elsewhere in scrollcraft.js), or provide an always-tabbable link to the proof and price-list sections early in the DOM.

### Major

4. [H4, H8] Two top-right calls-to-action collide during the pinned scene. Alunix's own kontakt@alunix.se pill (fixed header, z-index 80) and Horai's embedded RESERVATIONS button occupy the same corner simultaneously once the iframe is live, reading as visual clutter and creating a moment where it is unclear which top-right item belongs to Alunix versus the demo site. Screenshot: heur-motion-11-topbar-during-scene.png. Fix: scrim or mask the iframe's own header chrome, or coordinate with the demo builds so their nav avoids the exact coordinates Alunix's fixed header occupies.

5. [H1] No progress or "why did scrolling stop" cue when the reduced-motion iframe captures the wheel. Immediately after Critical #2, a visitor has no on-screen indication that further scrolling requires moving the pointer off the frame first -- from their point of view the page has simply frozen. Fix: detect sustained wheel input inside the iframe's bounding box without matching page-level scroll progress, and surface a short "scroll to continue" hint.

### Minor

6. [H7] No way to skip the roughly 2.3-screen camera push-in for a repeat visitor. Not unreasonable for a one-time hero moment, but there is no accelerator (for example a "skip intro" affordance once a visitor has already seen it once, tracked in sessionStorage). Fix: low priority; consider only if analytics show high bounce during the push-in.

## What works well

- The reduced-motion build tells the same story as the motion build at every checkpoint (hero, window, proof, price list, contact) with no missing content -- the "fewer and gentler, not zero" principle documented in scrollcraft.js is honored structurally, not just claimed.
- The persistent header keeps kontakt@alunix.se legible and clickable from the very first frame through to the last (verified display, opacity and visibility all resolve to visible with opacity 1 at both hero and landing), so the fastest possible path to contact never requires scrolling at all -- a real strength for a visitor who just wants to email them.
- The price list is unambiguous: three rows, per-row hairline draws in on scroll as a subtle progress cue, tabular numerals keep prices aligned, and "Pris vid forfragan" for the custom tier avoids implying a fixed number that does not exist.
- Site names are repeated at the hero and again at each individual proof row, so a visitor never has to scroll back up to remember which example matches which service.
- The global scroll progress bar gives page-wide orientation feedback that most single-page scroll sites skip entirely.

## Recommendation

Revise. The narrative and default (non-interactive) reading path are solid in both builds, but the page's one interactive promise, a live clickable window into an example site, is broken in both builds, in two different and equally severe ways (unreachable by mouse in motion, scroll-trapping in reduced-motion), and the keyboard path additionally fails the walkthrough's own success criteria outright (price list unreachable via Tab). These are mechanical, well-isolated fixes (a pointer-events rule, a scroll-capture guard, a focus-management gap) rather than a redesign, so revise-and-reverify rather than rethink.
