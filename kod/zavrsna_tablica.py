#!/usr/bin/env python3
"""zavrsna_tablica.py — konačna tablica stilskog prolaza: prije (kopija) → poslije (sada)."""
import importlib.util
import os
import subprocess

B = "/home/agent/knjiga-emergencija/"
STARO = "/tmp/stil-staro"
spec = importlib.util.spec_from_file_location("cs", B + "kod/check_stil.py")
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)

red = []
for put in cs.datoteke():
    rel = os.path.relpath(put, B)
    stari = os.path.join(STARO, rel[len("rukopis/"):])
    a, b = cs.mjere(stari), cs.mjere(put)
    r = subprocess.run(["python3", "kod/check_stil.py", "--datoteka", put], cwd=B, capture_output=True, text=True).stdout
    red.append([rel.replace("rukopis/", ""), a, b, "✔" if "✔ proza" in r else "⚠"])

zag = ["datoteka", "bold prije", "bold sada", "dugi prije", "dugi sada", "reč. prije", "reč. sada",
       "≤8 prije", "≤8 sada", "niz prije", "niz sada", "upravo prije", "upravo sada", "stanje"]
w = [len(z) for z in zag]
for ime, a, b, st in red:
    vals = [ime, f"{a['bold']:.1f}", f"{b['bold']:.1f}", f"{a['bold_dugi']:.1f}", f"{b['bold_dugi']:.1f}",
            f"{a['rec']:.1f}", f"{b['rec']:.1f}", f"{a['vrlo_kratke']:.1f}", f"{b['vrlo_kratke']:.1f}",
            str(a['niz_dagih']), str(b['niz_dagih']), f"{a['upravo']:.1f}", f"{b['upravo']:.1f}", st]
    for i, v in enumerate(vals):
        w[i] = max(w[i], len(v))
print("  ".join(zag[i].rjust(w[i]) for i in range(len(zag))))
for ime, a, b, st in red:
    vals = [ime, f"{a['bold']:.1f}", f"{b['bold']:.1f}", f"{a['bold_dugi']:.1f}", f"{b['bold_dugi']:.1f}",
            f"{a['rec']:.1f}", f"{b['rec']:.1f}", f"{a['vrlo_kratke']:.1f}", f"{b['vrlo_kratke']:.1f}",
            str(a['niz_dagih']), str(b['niz_dagih']), f"{a['upravo']:.1f}", f"{b['upravo']:.1f}", st]
    print("  ".join(vals[i].rjust(w[i]) for i in range(len(vals))))

wa = sum(a["rijeci"] for _, a, _, _ in red)
wb = sum(b["rijeci"] for _, _, b, _ in red)
print(f"\nUKUPNO riječi proze: prije {wa} → sada {wb}")
for klj, ime in [("bold", "podebljano %"), ("bold_dugi", "dugi masni %"), ("rec", "srednja rečenica"),
                 ("vrlo_kratke", "≤8 riječi %"), ("kratke", "<12 riječi %"), ("duge", ">40 riječi %"),
                 ("upravo", "„upravo“/10k")]:
    va = sum(a[klj] * a["rijeci"] for _, a, _, _ in red) / wa
    vb = sum(b[klj] * b["rijeci"] for _, _, b, _ in red) / wb
    print(f"  {ime:<20} {va:>7.1f} → {vb:>7.1f}")
