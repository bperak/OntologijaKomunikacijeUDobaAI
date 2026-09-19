#!/usr/bin/env python3
"""sadrzaj_build.py — generira sadržaj knjige iz naslova u rukopisu.

Zašto generirano: sadržaj je prvo što se razveže s tekstom kad se poglavlje preimenuje
ili doda odjeljak. Ovdje se čita iz samih datoteka, pa je uvijek točan; u prijelomu se
dodaju brojevi stranica.

    python3 kod/sadrzaj_build.py     →  rukopis/sadrzaj.md
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUK = os.path.join(ROOT, "rukopis")
IZLAZ = os.path.join(RUK, "sadrzaj.md")

# redoslijed dijelova knjige (kako se čita, a ne kako stoji na disku)
PREDGOVOR = ["predgovor.md", "uvod.md"]
POGLAVLJA = [f"poglavlje-{i:02d}.md" for i in range(1, 17)]
DODACI = ["dodaci/dodatak-A-okruzenje.md", "dodaci/dodatak-B-rjecnik.md",
          "dodaci/dodatak-C-rjesenja-vjezbi.md", "dodaci/dodatak-D-predlosci.md",
          "dodaci/dodatak-E-izvori-i-brojke.md", "dodaci/dodatak-F-prigovori-i-odgovori.md",
          "dodaci/dodatak-G-kazalo.md"]
KRAJ = ["zakljucak.md", "studije-slucaja/incidenti-2026.md"]


def naslovi(put, dubine=(1, 2)):
    """Vrati (razina, tekst) za zadane dubine naslova u datoteci."""
    izlaz = []
    if not os.path.exists(put):
        return izlaz
    for redak in open(put, encoding="utf-8"):
        m = re.match(r"^(#{1,3}) (.+?)\s*$", redak)
        if m and len(m.group(1)) in dubine:
            izlaz.append((len(m.group(1)), m.group(2)))
    return izlaz


def main() -> int:
    redci = ["# Sadržaj", "",
             "*Generirano skriptom `kod/sadrzaj_build.py` iz naslova u rukopisu; brojevi stranica "
             "dodaju se u prijelomu.*", ""]
    manjkaju = []
    for skupina, imena, bez_podnaslova in (
            ("", PREDGOVOR, True),
            ("## POGLAVLJA", POGLAVLJA, False),
            ("## DODACI", DODACI, False),
            ("", KRAJ, True)):
        if skupina:
            redci += ["", skupina, ""]
        for ime in imena:
            put = os.path.join(RUK, ime)
            if not os.path.exists(put):
                manjkaju.append(ime)
                continue
            for razina, tekst in naslovi(put, (1,) if bez_podnaslova else (1, 2)):
                if razina == 1:
                    redci.append(f"- **{tekst}**")
                else:
                    redci.append(f"  - {tekst}")
    open(IZLAZ, "w", encoding="utf-8").write("\n".join(redci) + "\n")
    print(f"sadržaj: {IZLAZ} | redaka: {len(redci)}")
    if manjkaju:
        print("  (još ne postoje, preskočeno: " + ", ".join(manjkaju) + ")")
    return 0


if __name__ == "__main__":
    sys.exit(main())
