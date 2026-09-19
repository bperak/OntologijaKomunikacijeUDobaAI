#!/usr/bin/env python3
"""check_cisto.py — higijena rukopisa i izvora.

Tri vrste grešaka koje se u ovome projektu stalno vraćaju, a oku su nevidljive:

  1. **ćirilični homoglifi** — „Gricеova" (е ćirilično), „kontekст" (с, т), „Rаčuna" (а).
     Izgledaju kao latinična slova, pretraživanje ih ne nalazi, a u tisku izlaze kao
     drugi znak. Provjeravaju se svi .md i .mmd izvori.
  2. **zaostali markeri skripti** — `<!-- KRAJ-DIJELA-2 -->`, `TODO`, `FIXME`.
     Izuzetak je namjerni marker dijelova dodatka C (`<!-- dio N/4: … -->`), koji
     nastaje pri pisanju u četiri dijela i zato se ne prijavljuje kao zaostatak.
  3. **miješano nazivlje slika** — usporedno „Slika 3.1" i „Figura 3.1" u istome rukopisu;
     potpis i uputa u tekstu moraju rabiti isti naziv (u ovoj knjizi: **Slika**).

Pokretanje: python3 kod/check_cisto.py   (0 = čisto, 1 = ima nalaza)
"""
import glob
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CILJEVI = (glob.glob(os.path.join(ROOT, "rukopis", "**", "*.md"), recursive=True)
           + glob.glob(os.path.join(ROOT, "docs", "*.md"))
           + glob.glob(os.path.join(ROOT, "figure", "izvori", "*.mmd"))
           + [os.path.join(ROOT, "README.md")])
HOMOGLIFI = {"\u0430": "a", "\u0435": "e", "\u043e": "o", "\u0441": "c", "\u0440": "p",
             "\u0443": "y", "\u0445": "x", "\u0442": "t", "\u0456": "i", "\u0410": "A",
             "\u0415": "E", "\u041e": "O", "\u0421": "C", "\u0420": "P", "\u0422": "T"}


def main() -> int:
    nalazi = []
    for p in sorted(CILJEVI):
        if not os.path.isfile(p):
            continue
        ime = os.path.relpath(p, ROOT)
        t = open(p, encoding="utf-8").read()
        for i, ch in enumerate(t):
            if ch in HOMOGLIFI or "\u0400" <= ch <= "\u04FF":
                try:
                    naziv = unicodedata.name(ch)
                except ValueError:
                    naziv = "?"
                nalazi.append(f"{ime}: ćirilični znak {ch!r} ({naziv}) → "
                              f"…{t[max(0, i - 35):i + 25].replace(chr(10), ' ')}…")
        for lab, rx in (("HTML komentar", r"<!--(?!\s*dio\s+\d+/\d+)"),
                        ("marker skripte", r"KRAJ-DIJELA"),
                        ("TODO/FIXME", r"\bTODO\b|\bFIXME\b|\bXXX\b")):
            for m in re.finditer(rx, t):
                nalazi.append(f"{ime}: {lab} → …{t[max(0, m.start() - 40):m.start() + 40]}…")
    # miješano nazivlje slika (samo rukopis)
    slik = fig = 0
    for p in glob.glob(os.path.join(ROOT, "rukopis", "**", "*.md"), recursive=True):
        t = open(p, encoding="utf-8").read()
        slik += len(re.findall(r"\bSlika\b", t))
        fig += len(re.findall(r"\bFigura\b", t))
    print("=== Higijena rukopisa ===")
    print(f"nazivlje slika: Slika ×{slik} | Figura ×{fig}")
    if fig:
        nalazi.append(f"miješano nazivlje: „Figura\" se pojavljuje {fig}× — knjiga rabi „Slika\"")
    if nalazi:
        print(f"\n⚠ nalaza: {len(nalazi)}")
        for n in nalazi:
            print("   -", n)
        return 1
    print("\n✔ nema homoglifa, markera ni miješanog nazivlja")
    return 0


if __name__ == "__main__":
    sys.exit(main())
