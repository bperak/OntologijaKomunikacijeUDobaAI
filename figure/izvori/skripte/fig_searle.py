#!/usr/bin/env python3
"""Searle's emergent levels + the Chinese Room challenge, with the model as a dashed candidate agent."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

INK='#1C2B4A'; INK2='#334463'; ACC='#C0502E'; ACC2='#0F766E'; SOFT='#EEF2F8'; MUTED='#5A6B80'; LINEC='#D5DDE8'

fig, ax = plt.subplots(figsize=(7.3, 3.6), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 66); ax.axis('off')

def box(x, y, w, h, fc=SOFT, ec=None, ls='solid', z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=2.0",
                                fc=fc, ec=(ec or 'none'), lw=1.4, ls=ls, zorder=z))
def txt(x, y, s, fs=9.0, c=INK, bold=False, style='normal', ha='center'):
    ax.text(x, y, s, ha=ha, va='center', fontsize=fs, color=c, fontweight=('bold' if bold else 'normal'), style=style, zorder=3, linespacing=1.25)
def arrow(x1, y1, x2, y2, color=LINEC, lw=1.8):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=13, color=color, lw=lw, zorder=1))

txt(50, 63.5, 'Searle’s emergent systems', fs=11, c=ACC, bold=True)

levels = [
    ('CHEMICAL · PHYSICAL', 'microstructure (parts)', MUTED),
    ('BIOLOGICAL', '', INK2),
    ('CONSCIOUSNESS', 'higher-level system feature — like liquidity of water', INK2),
    ('INTENTIONALITY', 'intrinsic (biological) vs derived (computational)', INK2),
    ('SOCIAL REALITY / INSTITUTIONS', 'emergent from collective intentionality; language = the basic social institution', ACC2),
]
y = 10.5; h = 9.0
for name, note, col in levels:
    box(6, y, 88, h, fc=SOFT, ec=LINEC)
    txt(50, y + h*0.68, name, fs=(10 if name.startswith('SOCIAL') else 9.5), c=col, bold=True)
    if note:
        txt(50, y + h*0.24, note, fs=7.8, c=MUTED, style='italic')
    y += h + 1.6
arrow(2.8, 11.0, 2.8, 57.0, color=LINEC, lw=2)
txt(50, 6.4, 'higher levels: system features caused by the microstructure — Searle’s “causally emergent”',
    fs=8.6, c=INK2)
box(6, 1.0, 88, 3.6, fc='white', ec=ACC, ls='dashed')
txt(50, 2.8, '?   the model — a causal agent at system level, or only a derived system?', fs=8.4, c=ACC, bold=True)
fig.tight_layout(); fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_searle.png',
                                facecolor='white', bbox_inches='tight', pad_inches=0.07)
print('saved fig_searle.png')
