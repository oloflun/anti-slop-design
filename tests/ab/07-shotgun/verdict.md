# AB07 — Shotgun / bake-off (3 riktningar × 2 motorer, florist-brief)

Board: `tests/ab/07-shotgun/board.json`; celler byggda blint av sex Sonnet-agenter (fold + första sektion).
Motorer: `chain` = craft floor + house-physics; `impeccable` = impeccable SKILL.md + craft-floor.md.

| Riktning | chain | impeccable | Vinnare | Varför (läst i compare/folds.png) |
|---|---|---|---|---|
| A Tryckt katalog (editorial print) | label-rail hero, roman+italic-tvåton, typsatt länk-CTA, ledger börjar under folden | vänster text + höger ramad plansch (default-landningslayout), två knappar, kortkänsla | chain | ledger och typsatt CTA mot kort-reflex |
| B Kall verkstad (modern clean) | petrol-poster, grotesk med ett tegel-ord, ritad stjälk som bryter högerkanten, två riktiga knappar | fog-grund, staplad rubrik i tre storlekar/färger ("VERKSTADEN / PÅ / MARIAPLAN"), platshållarkort | chain | samlad hierarki mot tre konkurrerande vikter |
| C Hamnfoto (warm photographic) | fullbleed Klippan-vatten med varm scrim, serif + italic accentord, knapp + spökländk; foto-ID återanvänt från verifierade sajter | fullbleed **dykare med fiskstim** (ogranskat Unsplash-ID), rubrik korrekt | chain | fel bild = fel sida; kedjans regel om verifierade foton bet |

Fingerprint mellan riktningarna (grammatik · nav · hero-device · palett · typ · CTA-form): A/B skiljer 6/6, A/C 5/6, B/C 5/6 — klarar 3/6.
Human-val (jag, som testets människa): **B-chain** — den enda som lämnar cream-defaulten och ändå håller registret; A-chain är det säkra valet, C-chain kräver ett varmare foto.

**Beslut: IN.** Boarden fungerar (riktningar × motorer, feedback.json), och bake-offen svarar konkret på "är kedjan bevisat bättre" varje gång: 3–0 mot impeccable ensam på den här briefen. Kostnad 6 fold-byggen ≈ 2 fulla byggen; default i kedjan blir 3 riktningar × 2 motorer på page-scope. Modifiering: cellprompten ska kräva foto-ID:n från katalogen/sajterna (verifierade), aldrig fria gissningar; italic/färgat accentord i rubriken (A-chain, C-chain) ska passera gate 89-kontrollen i Step 4.
