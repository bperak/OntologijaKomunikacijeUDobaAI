# ISPRAVKE — evidencija ispravljenih tvrdnji

Ova datoteka vodi **svaku tvrdnju koja je iznesena javno, a kasnije se pokazala netočnom ili nepotpunom**.
Pravilo knjige: pogreška se ne briše — bilježi se (što je pisalo, što je točno, odakle to znamo, gdje je ispravljeno).
Datum u zagradi = datum provjere na primarnom izvoru.

---

## ISPRAVAK-001 · 14. 9. 2026. · METR-ov vremenski horizont

- **Pisalo je:** METR-ov vremenski horizont za frontier model u veljači 2026. iznosi ~13–14,5 h. (izlaganje IUC Dubrovnik, 11. 9. 2026., slajd 16)
- **Točno je:** prvotna METR-ova procjena za **Claude Opus 4.6** (20. 2. 2026.) bila je **~14,5 h**, ali je METR **3. 3. 2026. ispravio bug** u svom modeliranju i vrijednost spustio na **~12 h**.
- **Uz to:** METR uz graf navodi: *„Measurements above 16 hrs are unreliable with our current task suite."* **Claude Mythos** (ožujak 2026.) ocijenjen je na **16+ h** — što je gornja granica skupa zadataka, a ne novi plato.
- **Izvor:** METR (2025), arXiv:2503.14499 (NeurIPS 2025); METR-ova napomena uz graf (2026.); A. Cotra (METR), *I underestimated AI capabilities (again)*, 3. 3. 2026.
- **Posljedica za tekst:** horizont se navodi kao **~12 h (nakon ispravka, 3. 3. 2026.)**, a svako navođenje brojke iznad 16 h mora nositi napomenu o nepouzdanosti mjerenja.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina G) · `data/fakti.csv` (`metr_horizon_2026`, novi `metr_unreliable_above`)

## ISPRAVAK-002 · 14. 9. 2026. · Strop GPQA

- **Pisalo je:** strop GPQA („nesporno točni" odgovori) ≈ **90 %**. (izlaganje, slajd 17)
- **Točno je:** strop je **~80 %** (zavisi od podskupa); GPQA je **zasićen 11/2025** (Gemini 3 Pro @ 93,8 %), a **Anthropic ga prestaje izvještavati od 6/2026**.
- **Izvor:** A. D. Thompson, *Mapping IQ, MMLU, MMLU-Pro, GPQA, HLE*, LifeArchitect.ai (ažurirano 4. 8. 2026.); Rein et al. (2023), arXiv:2311.12022.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina H) · `data/fakti.csv` (`gpqa_ceiling` = 80, uz novi `mmlu_ceiling` 91 i `mmlu_pro_ceiling` 90 za kontekst)

## ISPRAVAK-003 · 14. 9. 2026. · Strop HLE (nepotpuna tvrdnja)

- **Pisalo je:** strop HLE = **25,6 %**. (izlaganje, slajd 17)
- **Nepotpuno je:** postoje **dva izvora s različitim vrijednostima** — **~51,3 %** (FutureHouse, 7/2025) i **25,6 %** (Alibaba, 2/2026, arXiv:2602.13964v2). HLE je **gotovo zasićen 12/2025** (GPT-5.2 @ 50 %).
- **Izvor:** Thompson (2026), *Mapping*; HLE (2026), *Nature* 649:1139–1146, DOI 10.1038/s41586-025-09962-4.
- **Posljedica za tekst:** nikad se ne navodi jedan strop kao jedini — navode se **oba, s izvorom i datumom**.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina G) · `data/fakti.csv` (`hle_ceiling` = 51.3 + napomena o Alibabi)

---

## Zašto ovo postoji

Knjiga tvrdi da se razine razlučuju **po vrsti dokaza**, a ne po uvjerljivosti izvora. Ako autor ne bilježi vlastite ispravke, tvrdnja o razlučivanju razina nije vjerodostojna. Zato:

1. **Brojka bez datuma i vrste (mjereno / procjena) nije brojka.**
2. **Ako se dvije mjerne vrijednosti razilaze, navode se obje** — čitatelj dobiva stanje spora, ne autorov izbor.
3. **Ispravak se objavljuje, ne skriva.** Ova datoteka je javna.
