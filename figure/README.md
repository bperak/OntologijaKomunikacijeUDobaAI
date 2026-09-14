# figure/ — figure knjige

Figure su **autorske** (Benedikt Perak), izrađene za predavanje *Elements of Cognition in Complex Language* (IUC Dubrovnik, 11. 9. 2026.) i preuzete u knjigu. Svaka figura ima izvornu skriptu, izvor podataka i datum izrade.

## Popis (stvarna imena datoteka)

| datoteka | sadržaj | poglavlja |
|---|---|---|
| `fig_omlcc_s1.png`, `fig_omlcc_s2.png`, `fig_omlcc_s3.png` | ljestvica šesnaest razina kroz tri domene (materijalna 1–8 / psihološka 9–11 / društvena 12–16), svaka razina s relacijskom shemom; podnožje nosi tvrdnju *mreža → emergentni entitet → mreža sljedeće razine* (Emmeche, Køppe & Stjernfelt 1997) i atribuciju domena Searleu (1995; 2010) | **2**, 3 |
| `fig_omlcc16.png` | cjelovita ljestvica šesnaest razina (jedna slika) | 2 |
| `fig_emotion_network.png` | mreža 125 hrvatskih emocionalnih leksema sa *strah* u središtu (vlastita figura, izrezana) | **6** |
| `fig_strah_usporedba.png`, `fig_strah_vektori.png` | usporedba mrežnog i vektorskog prikaza leksema *strah* | 6, 10 |
| `fig_scale.png` | parametri, FLOP, Chinchilla, sparsnost | 9, 10 |
| `fig_trillion_club.png` | „klub 10¹² parametara" (Thompson 2026 — **procjene**) | 10 |
| `fig_scoreboard.png` | rezultati i stropovi testova (GPQA, HLE) | 10 |
| `fig_context.png` | rast kontekstnog prozora (512 → 10 M) | 10 |
| `fig_horizon.png` | vremenski horizont zadataka (METR 2025) | 10 |
| `fig_agent_hijerarhija.png` | pet slojeva koji pretvaraju model u agenta | **12** |
| `fig_searle.png` | Searleova podjela domena (brute / mental / institutional facts) | 2, 8 |
| `fig_razine.png`, `fig_hijerarhija.png`, `fig_emerg_hijerarhija.png` | prikazi hijerarhije i emergencije razina | 1, 3 |
| `fig_loops.png` | petlje procesiranja / unaprjeđenja konteksta | 11 |
| `fig_voda.png` | radni primjer (materijal → informacija → komunikacija) | 3 |

## Alati i provjera

- vektorski izvori: **SVG → PNG preko `resvg-py`** (`cairosvg` i LibreOffice u ovom okruženju ne rade).
- izvoz iz prezentacije: pptx → PDF → PyMuPDF (render) → **vizualna provjera** (`vision_analyze`): nema rezanog teksta, nema prelijevanja, natpisi odgovaraju tekstu knjige.
- **Pravilo:** ako natpis na slici i tekst knjige ne govore isto, ispravlja se **tekst** (ili se figura ponovno izrađuje) — figura nikad ne smije tvrditi više od onoga što je u tekstu.

## Autorska prava

Tuđe figure se **ne** kopiraju. Ako je figura tuđa, navodi se izvor; inače se izrađuje vlastita figura na temelju podataka, uz citiranje izvora podataka.
