#!/usr/bin/env python3
"""kazalo_build.py — generira kazalo pojmova i imena za knjigu.

Zašto ovako
-----------
Kazalo se ne piše ručno, jer bi se ručno i pokvarilo: čim se poglavlje promijeni,
kazalo zastari. Ovdje se gradi iz dvaju izvora koji su ionako pod provjerom:

  * POJMOVI  ← `pojmovnik/koncepti.csv` (registar pojmova za sve tri knjige)
  * IMENA    ← `referencije/REFERENCE_BASE.md` (jedini dopušteni izvor citata)

Svaki se pojam i svako prezime traže u rukopisu, a bilježe se **odjeljci** u kojima
se pojavljuju (npr. 7.5, 14.6) — ne brojevi stranica, jer se paginacija određuje tek
u prijelomu. Uz svaki se pojam ispisuje i broj pojavljivanja, da se vidi je li pojam
nositelj ili samo spomenut.

Pokretanje: python3 kod/kazalo_build.py
Izlaz:      rukopis/dodaci/dodatak-G-kazalo.md
"""
import csv
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUK = os.path.join(ROOT, "rukopis")
POJMOVI = os.path.join(ROOT, "pojmovnik", "koncepti.csv")
REF = os.path.join(ROOT, "referencije", "REFERENCE_BASE.md")
IZLAZ = os.path.join(RUK, "dodaci", "dodatak-G-kazalo.md")

# dodatak i predgovor ne ulaze u kazalo (kazalo pokazuje gdje se pojam razrađuje)
PRESKOCI = ("predgovor", "zakljucak", "uvod")


def bez_dijakritika(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def poglavlja():
    """Vrati [(oznaka, tekst)] za sve dijelove rukopisa, s brojevima odjeljaka."""
    izlaz = []
    for korijen, _, datoteke in os.walk(RUK):
        for d in sorted(datoteke):
            if not d.endswith(".md"):
                continue
            if any(p in d for p in PRESKOCI) and "dodaci" not in korijen:
                continue
            put = os.path.join(korijen, d)
            izlaz.append((os.path.relpath(put, RUK), open(put, encoding="utf-8").read()))
    return izlaz


def odjeljci_pojma(tekst: str, pojam: str):
    """Vrati (sorted set odjeljaka, broj pojavljivanja) za pojam u jednom tekstu."""
    # traži pojam kao riječ (dopuštajući hrvatske nastavke i padeže)
    uzorak = re.compile(r"(?<!\w)" + re.escape(pojam).rstrip("aeiou") + r"\w{0,4}", re.I)
    trenutni, nadeni = None, set()
    broj = 0
    for redak in tekst.splitlines():
        naslov = re.match(r"^#{2,3} (\d+\.\d+|\d+\.\d+\.\d+)", redak)
        if naslov:
            trenutni = naslov.group(1)
        if uzorak.search(redak):
            broj += len(uzorak.findall(redak))
            if trenutni:
                nadeni.add(trenutni)
    return sorted(nadeni, key=lambda x: [int(y) for y in x.split(".")]), broj


def main() -> int:
    if not os.path.exists(POJMOVI):
        print(f"nema registra pojmova: {POJMOVI}")
        return 1
    rukopis = poglavlja()
    # 1) pojmovi iz registra
    with open(POJMOVI, encoding="utf-8") as fh:
        sirovi = [r for r in csv.DictReader(fh) if r.get("pojam")]
    # Registar pokriva SVE TRI knjige, pa se isti pojam pojavljuje i po tri puta.
    # Za kazalo ove knjige uzima se jedan zapis po pojmu; prednost ima zapis koji
    # pripada ovoj knjizi, a pojam se ionako bilježi prema pojavljivanjima u rukopisu.
    koncepti, videni = [], set()
    for r in sorted(sirovi, key=lambda x: 0 if "razine" in (x.get("knjiga") or "").lower() else 1):
        kljuc = bez_dijakritika(r["pojam"].strip().lower())
        if kljuc in videni:
            continue
        videni.add(kljuc)
        koncepti.append(r)

    redci_pojmovi = []
    for k in koncepti:
        pojam = k["pojam"].strip()
        mjesta = {}
        ukupno = 0
        for ime, tekst in rukopis:
            odj, broj = odjeljci_pojma(tekst, pojam)
            if odj:
                mjesta[ime] = odj
                ukupno += broj
        if ukupno:
            redci_pojmovi.append((pojam, ukupno, mjesta))

    # 2) imena iz baze referenci (prezime + godina)
    baza = open(REF, encoding="utf-8").read()
    imena = {}
    for m in re.finditer(r"^- \*\*([A-ZŠĐČĆŽ][^*]{2,60}?)\s*\((\d{4}[a-z]?)\)", baza, re.M):
        autor = m.group(1).strip().rstrip(",.")
        prvo = re.split(r",| i | &", autor)[0].strip()
        if len(prvo) < 3 or not prvo[0].isupper():
            continue
        imena.setdefault(prvo, set()).add(m.group(2))

    redci_imena = []
    for prezime, godine in sorted(imena.items()):
        mjesta, ukupno = {}, 0
        jezgra = bez_dijakritika(prezime)[:5]
        for ime, tekst in rukopis:
            if jezgra.lower() not in bez_dijakritika(tekst).lower():
                continue
            odj, broj = odjeljci_pojma(tekst, prezime)
            if odj:
                mjesta[ime] = odj
                ukupno += broj
        if ukupno:
            redci_imena.append((prezime, sorted(godine), ukupno, mjesta))

    # 3) zapis
    def popis(mjesta, dvije=False):
        dijelovi = []
        for ime, odj in sorted(mjesta.items()):
            tag = ime.replace("poglavlje-", "pogl. ").replace(".md", "").replace(
                "dodaci/dodatak-", "dodatak ")
            if dvije and odj:
                dijelovi.append(f"**{tag}** ({', '.join(odj)})")
            else:
                dijelovi.append(f"**{tag}**")
        return " · ".join(dijelovi)

    def popis_imena(mjesta):
        """Imena: poglavlja s odjeljcima, ali najviše osam odjeljaka po poglavlju."""
        dijelovi = []
        for ime, odj in sorted(mjesta.items()):
            tag = ime.replace("poglavlje-", "pogl. ").replace(".md", "").replace(
                "dodaci/dodatak-", "dodatak ")
            if not odj:
                dijelovi.append(f"**{tag}**")
                continue
            isjecak = ", ".join(odj[:8]) + ("…" if len(odj) > 8 else "")
            dijelovi.append(f"**{tag}** ({isjecak})")
        return " · ".join(dijelovi)

    os.makedirs(os.path.dirname(IZLAZ), exist_ok=True)
    with open(IZLAZ, "w", encoding="utf-8") as fh:
        fh.write("# Dodatak G — Kazalo pojmova i imena\n\n")
        fh.write("Kazalo je **generirano** iz registra pojmova (`pojmovnik/koncepti.csv`) i baze "
                 "referenci (`referencije/REFERENCE_BASE.md`), pa se ne može razilaziti s tekstom. "
                 "Uz pojmove se navode **odjeljci** u kojima se pojavljuju (npr. 7.5, 14.6) i broj "
                 "pojavljivanja; uz imena se navode poglavlja s odjeljcima (najviše osam po poglavlju, "
                 "puni popis daje skripta). Brojevi stranica dodaju se u prijelomu.\n\n")
        fh.write(f"*Pojmova: {len(redci_pojmovi)} · imena i izvora: {len(redci_imena)} · "
                 f"izrađeno skriptom `kod/kazalo_build.py`.*\n\n---\n\n")
        fh.write("## G.1 Pojmovi\n\n")
        for pojam, ukupno, mjesta in sorted(redci_pojmovi, key=lambda x: bez_dijakritika(x[0].lower())):
            fh.write(f"- **{pojam}** ({ukupno}×) — {popis(mjesta, dvije=True)}\n")
        fh.write("\n## G.2 Imena i izvori\n\n")
        for prezime, godine, ukupno, mjesta in sorted(redci_imena, key=lambda x: bez_dijakritika(x[0].lower())):
            fh.write(f"- **{prezime}** ({', '.join(godine)}) ({ukupno}×) — {popis_imena(mjesta)}\n")
    print(f"kazalo: {IZLAZ}")
    print(f"  pojmova s pojavljivanjima: {len(redci_pojmovi)} | imena: {len(redci_imena)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
