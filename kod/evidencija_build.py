#!/usr/bin/env python3
"""evidencija_build.py — generira Dodatak E (izvori, podaci i provjera brojki).

Zašto generirano, a ne napisano
-------------------------------
Pravilo knjige je da svaka brojka ima zapis u `data/fakti.csv`, s izvorom, datumom i
vrstom. Dodatak E je zato **pogled na tu evidenciju** — tablica koja se sama obnavlja
kad se evidencija promijeni. Da se piše ručno, prva bi se ispravka brojke razvezala s
popisom i dodatak bi počeo lagati; ovako se obnavlja jednom naredbom:

    python3 kod/evidencija_build.py

Izlaz: rukopis/dodaci/dodatak-E-izvori-i-brojke.md
"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVID = os.path.join(ROOT, "data", "fakti.csv")
IZLAZ = os.path.join(ROOT, "rukopis", "dodaci", "dodatak-E-izvori-i-brojke.md")

# brojke koje su ispravljene nakon provjere (vidi docs/ISPRAVKE.md) — vode se izrijekom
ISPRAVLJENE = {
    "metr_horizon_2026": "ISPRAVAK-001: METR je 3. 3. 2026. ispravio bug u modeliranju; "
                         "prvotna procjena 14,5 h spuštena je na ~12 h (vrijednosti iznad 16 h "
                         "nepouzdane su sa sadašnjim skupom zadataka — zapis `metr_unreliable_above`).",
    "hle_ceiling": "ISPRAVAK-002: rezultat HLE navodi se s OBA izvora (51,3 % FutureHouse 7/2025; "
                   "25,6 % Alibaba 2/2026, arXiv:2602.13964v2) — nijedan se ne navodi kao jedini točan.",
    "gpqa_ceiling": "ISPRAVAK-003: skala je zasićena (11/2025 Gemini 3 Pro 93,8 %), pa se ~80 % "
                    "prikazuje kao povijesna vrijednost, ne kao trenutni strop; u izlaganju je bilo "
                    "navedeno 90 %.",
}


def ucitaj():
    redci, komentari = [], []
    with open(EVID, encoding="utf-8") as fh:
        for red in fh:
            red = red.rstrip("\n")
            if not red.strip():
                continue
            if red.startswith("#"):
                komentari.append(red.lstrip("# ").strip())
                continue
            redci.append(red)
    zag = redci[0].split(",")
    tijelo = []
    for r in redci[1:]:
        # polja mogu sadržavati zareze unutar navodnika — koristi csv čitač
        for d in csv.reader([r]):
            tijelo.append(dict(zip(zag, d)))
    return komentari, tijelo


def main() -> int:
    komentari, zapisi = ucitaj()
    po_vrsti = {}
    for z in zapisi:
        vrsta = (z.get("vrsta") or "").split(" ")[0].strip()
        po_vrsti.setdefault(vrsta, []).append(z)

    def tablica(vrsta):
        redovi = ["| brojka | jedinica | izvor | datum | gdje se pojavljuje | napomena |",
                  "|---|---|---|---|---|---|"]
        for z in sorted(po_vrsti.get(vrsta, []), key=lambda x: (x.get("izvor") or "")):
            nap = (z.get("napomena") or "").replace("\n", " ")
            redovi.append(f"| {z.get('brojka')} | {z.get('jedinica')} | {z.get('izvor')} | "
                          f"{z.get('datum_izvora')} | `{z.get('pojavljuje_se_u')}` | {nap} |")
        return "\n".join(redovi)

    os.makedirs(os.path.dirname(IZLAZ), exist_ok=True)
    with open(IZLAZ, "w", encoding="utf-8") as fh:
        fh.write("# Dodatak E — Izvori, podaci i provjera brojki\n\n")
        fh.write("Ovaj dodatak nije popis literature — literatura je u `referencije/REFERENCE_BASE.md`. "
                 "Ovo je **evidencija brojki**: svaka brojka koja se u knjizi pojavljuje ima ovdje svoj "
                 "redak, s izvorom, datumom i **vrstom**. Pravilo je iz 4.5: *brojka bez izvora, datuma i "
                 "vrste nije brojka*, i provjerava se automatski (`kod/check_fakti.py --strict`). "
                 "Tablica se generira iz `data/fakti.csv` skriptom `kod/evidencija_build.py`.\n\n")
        fh.write(f"**Stanje (generirano):** zapisa {len(zapisi)} · "
                 + " · ".join(f"{v}: {len(p)}" for v, p in sorted(po_vrsti.items())) + ".\n\n---\n\n")
        fh.write("## E.1 Zašto je vrsta brojke dio tvrdnje\n\n")
        fh.write("- **mjereno** — vrijednost je očitana s izvora ili izmjerena u vlastitom postavu; smije "
                 "nositi tvrdnju.\n- **procjena** — vrijednost je procijenjena (modelom, ekstrapolacijom ili "
                 "autorovom procjenom); nikad se ne prikazuje kao mjerenje i uvijek se navodi uz datum i "
                 "metodu procjene.\n- **izvedeno** — vrijednost je izračunata iz drugih brojki u ovoj "
                 "evidenciji; uz nju se navodi iz čega je izvedena.\n\n")
        fh.write("Uz svaku se brojku bilježi i **datum izvora**, jer se predmet knjige mijenja brže od "
                 "knjige: brojka bez datuma ne može se ni provjeriti ni ispraviti.\n\n")
        fh.write("## E.2 Brojke — mjereno\n\n" + tablica("mjereno") + "\n\n")
        fh.write("## E.3 Brojke — procjena\n\n" + tablica("procjena") + "\n\n")
        fh.write("## E.4 Brojke — izvedeno\n\n" + tablica("izvedeno") + "\n\n")
        fh.write("## E.5 Ispravljene brojke\n\n")
        fh.write("Popis ispravaka vodi se u `docs/ISPRAVKE.md`. Tri brojke koje su mijenjane nakon "
                 "provjere jesu:\n\n")
        pronadeno = 0
        for z in zapisi:
            bilj = ISPRAVLJENE.get(z.get("id"))
            if bilj:
                pronadeno += 1
                fh.write(f"- **{z.get('id')}** ({z.get('brojka')} {z.get('jedinica')}) — {bilj}\n")
        if not pronadeno:
            fh.write("*(nijedan zapis iz ove evidencije nije mijenjan)*\n")
        fh.write("\n## E.6 Kako se brojka provjerava\n\n")
        fh.write("```bash\npython3 kod/check_fakti.py --strict   # svaka brojka u tekstu ↔ evidencija\n```\n\n")
        fh.write("Alat traži brojke s jedinicom u rukopisu i provjerava da za svaku postoji zapis; "
                 "prijavljuje i dvostruke identifikatore te vrste koje nisu dopuštene. Kada nalaz "
                 "postoji, ispravlja se **tekst ili evidencija** — nikad oboje napola.\n\n")
        fh.write("## E.7 Izvori podataka korišteni u knjizi\n\n")
        izvori = sorted({(z.get("izvor") or "").strip() for z in zapisi if z.get("izvor")})
        for i in izvori:
            fh.write(f"- {i}\n")
        fh.write("\n" + "\n".join(f"> {k}" for k in komentari) + "\n")
    print(f"dodatak E: {IZLAZ}")
    print(f"  zapisa: {len(zapisi)} | " + " | ".join(f"{v}: {len(p)}" for v, p in sorted(po_vrsti.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
