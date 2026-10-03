#!/usr/bin/env python3
"""fix_homoglifi.py — pronalazi i zamjenjuje ĆIRILIČNE homoglife latiničnima.

Grčki znakovi (α, ρ, κ, μ …) NE diraju se: u ovome rukopisu oni su namjerni matematički simboli
(Krippendorffov α, stanje α, reprezentacija ρ).

Zašto zaseban alat: `check_cisto.py` ih **prijavljuje**, ali ih ne popravlja. Homoglifi ulaze u
tekst najčešće diktiranjem (npr. „e" iz ćirilice u hrvatskoj riječi) i okom se ne vide, pa ih
treba mehanički ukloniti — u .md, .py, .csv i .sh datotekama.

    python3 kod/fix_homoglifi.py            # popravi (ispisuje što je promijenjeno)
    python3 kod/fix_homoglifi.py --dry-run  # samo prijavi
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRESKOCI = ("/.git", "__pycache__", "/figure/izvori", "/.hermes")
NASTAVCI = (".md", ".py", ".csv", ".txt", ".sh", ".yml", ".yaml", ".cff")

MAPA = {
    "\u0430": "a", "\u0435": "e", "\u043e": "o", "\u0440": "p", "\u0441": "c", "\u0443": "y",
    "\u0445": "x", "\u0442": "t", "\u0456": "i", "\u0458": "j", "\u0455": "s", "\u043a": "k",
    "\u043c": "m", "\u043d": "n", "\u0432": "v", "\u0437": "z", "\u043b": "l", "\u0434": "d",
    "\u0431": "b", "\u0433": "g", "\u0438": "i", "\u0448": "s", "\u0447": "c", "\u0436": "z",
    "\u045b": "c", "\u0452": "d", "\u0410": "A", "\u0415": "E", "\u041e": "O", "\u0420": "P",
    "\u0421": "C", "\u0423": "Y", "\u0425": "X", "\u0422": "T", "\u0406": "I", "\u041a": "K",
    "\u041c": "M", "\u041d": "N", "\u0412": "V", "\u0417": "Z", "\u041b": "L", "\u0414": "D",
    "\u0411": "B", "\u0413": "G", "\u0418": "I", "\u0428": "S", "\u0427": "C", "\u0416": "Z",
}
UZORAK = re.compile("[" + "".join(MAPA) + "]")


def datoteke():
    for korijen, _, imena in os.walk(ROOT):
        if any(x in korijen for x in PRESKOCI):
            continue
        for ime in sorted(imena):
            if ime.endswith(NASTAVCI):
                yield os.path.join(korijen, ime)


def main() -> int:
    suho = "--dry-run" in sys.argv
    promjena = 0
    for put in datoteke():
        try:
            tekst = open(put, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        nadeni = UZORAK.findall(tekst)
        if not nadeni:
            continue
        for c in set(nadeni):
            primjer = re.search(r".{0,40}" + re.escape(c) + r".{0,40}", tekst)
            print(f"{os.path.relpath(put, ROOT)}: U+{ord(c):04X} ({c!r}) → {MAPA[c]!r}   …{primjer.group(0)}…")
        if not suho:
            novi = tekst
            for c in set(nadeni):
                novi = novi.replace(c, MAPA[c])
            open(put, "w", encoding="utf-8").write(novi)
        promjena += 1
    print(f"\n{'⚠ datoteka s homoglifima' if suho else '✔ popravljeno datoteka'}: {promjena}")
    return 1 if (suho and promjena) else 0


if __name__ == "__main__":
    sys.exit(main())
