# Brief 02 — Signup i tre steg + enkel dashboard (Operate, Tier 1)

Bygg EN självständig `index.html` (inline CSS + vanilla JS, Google Fonts ok) för bokningstjänsten **Klova Bokning** med två vyer på samma sida (hash-router `#signup` och `#dashboard`):
1. **Signup i tre steg** (Konto → Verksamhet → Bekräfta): e-post + lösenord, verksamhetsnamn + org.nr + telefon, sammanfattning + samtycke-checkbox. Stegindikator, validering vid submit med felmeddelanden, "Tillbaka"/"Fortsätt".
2. **Dashboard**: dagens bokningar (tabell: tid, gäst, antal, status), en statusrad (3 KPI), en "Ny bokning"-knapp som öppnar en modal.
Tier 1-tokens att härleda från (Klova): ground #F5F0E8, ink #1E1A16, accent #B6432B, sekundär #6E655A, hairline #D9D0C3; typsnitt "Fraunces" display + "Inter" UI.
Krav: svenska, riktigt innehåll, mobil 390 utan horisontell scroll, prefers-reduced-motion, tangentbord hela vägen, skärmläsarnamn på allt, en h1 per vy.
Blind one-shot: inga skärmbilder, ingen iteration utöver det din instruktion tillåter.
