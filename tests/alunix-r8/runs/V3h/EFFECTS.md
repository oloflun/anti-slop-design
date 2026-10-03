# V3g · godkända effekter (skyddade)

Varje effekt nedan har Anton bedömt som bra. En runda får inte ändra dem om briefen inte
uttryckligen säger det, och ingen av dem får bli sämre mätt med `section_probe.py`.
Baslinjen är `shots/section-probe-baseline.json`. Den skrivs när loopfixen är gjord, eftersom
dagens siffror bär loopens kostnad.

| Effekt | Var | Vad som är bra (Antons ord) | Signatur att hålla |
|---|---|---|---|
| Tesrubriken reser sig och står | `#tes`, `.tes-top` pin 0,9 vh + char-rise | "Det första intrycket är digitalt … var bättre" i V3f | p95 i `#tes` ≤ V3f-nivå (33 ms) utan loop; rubriken helt synlig ≥ 40 vh |
| Rubrikerna i allmänhet | alla `headline-40/50` | "rubrikerna blev mycket bättre" (V3f) | står stilla och hela ≥ 40 vh (motion.md läsregel) |
| Kontakten, kortet lämnas över | `#kontakt` | "även kontaktsidan" (V3f) | kortet vänder sig självt vid 0,7; heron speglad |
| Showcase-mekanismen | `#showcase` | "showcasen är bättre", "behåll mekanismen" (V3g R2) | en pin skapad en gång; övertoning mellan steg; räknare + mintspår |
| Övertoning vid casebyte | `activateCase` | ingen hård övergång (V3g R1–R2) | inget scrollY-hopp > baslinjen vid klick |

Underkänt, får inte återkomma: stegrubrik i displayskala och jättesiffra i rutan (F-019);
numerisk scrub och Lenis-standardtempo (F-020); refresh-loop via iframe-omladdning (F-021).
