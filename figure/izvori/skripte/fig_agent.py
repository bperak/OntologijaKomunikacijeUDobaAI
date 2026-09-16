#!/usr/bin/env python3
"""Levels of organisation WITH the language model as a candidate new agent (for the proposition slide)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

INK='#1C2B4A'; INK2='#334463'; ACC='#C0502E'; ACC2='#0F766E'; SOFT='#EEF2F8'; MUTED='#5A6B80'; LINEC='#D5DDE8'

fig, ax = plt.subplots(figsize=(7.4, 3.55), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 62); ax.axis('off')

def box(x, y, w, h, fc=SOFT, ec=None, ls='solid', z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=2.0",
                                fc=fc, ec=(ec or 'none'), lw=1.4, ls=ls, zorder=z))
def txt(x, y, s, fs=9.5, c=INK, bold=False, ha='center', style='normal'):
    ax.text(x, y, s, ha=ha, va='center', fontsize=fs, color=c, fontweight=('bold' if bold else 'normal'), style=style, zorder=3, linespacing=1.3)
def arrow(x1, y1, x2, y2, color=LINEC, lw=1.8, ls='solid'):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=13, color=color, lw=lw, ls=ls, zorder=1))

txt(50, 59.5, 'Levels of organisation — and a candidate new agent in the system', fs=11, c=ACC, bold=True)

levels = [
    ('PHYSICAL', 'parts: atoms, energy states', MUTED),
    ('CHEMICAL', 'emergent: liquidity, solvent properties', INK2),
    ('BIOLOGICAL', 'emergent: life, metabolism', INK2),
    ('SOCIAL / COGNITIVE', 'emergent: meaning, norms, shared intentionality', ACC2),
    ('LANGUAGE MODEL (candidate)', 'an agent — a new entity: collaborator to humans, competitor for resources', ACC),
]
y = 6.0
h = 8.6
for name, note, col in levels:
    highlight = name.startswith('LANGUAGE MODEL')
    box(7, y, 86, h, fc=('white' if highlight else SOFT), ec=(ACC if highlight else LINEC), ls=('dashed' if highlight else 'solid'))
    txt(50, y + h*0.66, name, fs=(10.5 if highlight else 10), c=(ACC if highlight else INK), bold=True)
    txt(50, y + h*0.26, note, fs=8.4, c=MUTED, style='italic')
    y += h + 1.9
arrow(3.2, 7.0, 3.2, 55.0, color=LINEC, lw=2)
txt(50, 1.4, 'each level: new entities with properties their parts lack — the model enters as a participant, not as a copy of us',
    fs=9, c=INK2)
fig.tight_layout(); fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_agent_hijerarhija.png',
                                facecolor='white', bbox_inches='tight', pad_inches=0.07)
print('saved fig_agent_hijerarhija.png')
