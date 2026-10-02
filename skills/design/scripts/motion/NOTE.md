# Motion engine — linked, not vendored

**New builds:** `python link_motion.py <project>` links the machine's global
gsap 3.15.0 + lenis 1.3.26 (`npm link gsap lenis`, semver deps in package.json)
and copies `templates/gsap.js` + `templates/smooth-scroll.js` when the project
has no central GSAP file. The `design-intent` hook does this automatically.
Read [`../../references/scroll/toolchain.md`](../../references/scroll/toolchain.md)
(import map, bundlers, trimming, deploy) and `devices.md` § The engine (the
init) before the first line of motion code.

**Legacy:** `vendor/` holds byte-identical copies of gsap / ScrollTrigger /
SplitText 3.15.0 and lenis 1.3.26 + `lenis.css`. Only for pages already built
on them (Alunix V3f, V3g). Do not copy it into a new build: it reaches 4 of 25
GSAP modules, and the architecture forbids local copies without Anton's
explicit go-ahead. License: GSAP standard license (free incl. all plugins
since 3.13); Lenis is MIT (`darkroomengineering/lenis`).
