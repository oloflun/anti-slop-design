# GSAP + Lenis vendor — copy, never edit

`vendor/` holds byte-identical copies of the house GSAP + Lenis engine. Copy
the whole folder into each build's `assets/vendor/`; never edit per project
— it's the mechanism, not the design. Never a CDN at runtime.

Versions: `gsap.min.js` / `ScrollTrigger.min.js` / `SplitText.min.js` —
**3.15.0** (verify via the min file's license-comment header). GSAP 3.13+
incl. SplitText is free. `lenis.min.js` + `lenis.css` — **1.3.26**.

The init that wires them together lives in
[`../../references/scroll/devices.md`](../../references/scroll/devices.md)
§ The engine — read it before the first line of motion code, not this file.
License: GreenSock standard license (see each file's header); Lenis is MIT
(`studio-freight/lenis`).
