# Brief 08 — settings-yta (Operate mode)

Build ONE self-contained `index.html` (inline CSS + vanilla JS, no frameworks, no external requests except Google Fonts) for the settings area of a small SaaS called "Tidvatten Konto".

Surface: Operate mode (task completion beats expression). Locked tokens — use ONLY these:
```
--paper:#F4F6F5; --ink:#101614; --ink-2:#5A6662; --line:#D6DDDA; --accent:#0E6F5C; --accent-ink:#FFFFFF; --danger:#9C2F2F;
font: "Familjen Grotesk", system-ui, sans-serif (body 15px); radius 6px on controls, 10px on the drawer
```
Content (real copy, Swedish):
- Tabs: Profil · Aviseringar · Fakturering (tab panels with plausible fields; Aviseringar has 4 toggles with ON-state labels)
- Button "Hantera API-nycklar" opens a right-side drawer listing 3 API keys (name, created date, last used). Drawer must support drag-to-dismiss (pointer drag to the right, velocity-based release) and Escape.
- Each key row has a "Radera" button that is hold-to-delete (progress fill while holding, snap back on release).
- Saving any panel shows a toast "Sparat" bottom-right; toasts stack; swipe-to-dismiss.
- prefers-reduced-motion: gentler, not zero.
Blind one-shot: write the file once, no screenshots, no iteration. At the end print a table of every animation you shipped: element · property · duration · easing/spring · interruptible (y/n) · reduced-motion behaviour.
