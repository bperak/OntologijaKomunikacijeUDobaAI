"""fig_scoreboard.py — where the scoreboard moved: GPQA and HLE, 2026 (data: Thompson, LifeArchitect.ai Models Table)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

INK = '#1C2B4A'; INK2 = '#334463'; ACC = '#C0502E'; ACC2 = '#0F766E'
MUTED = '#5A6B80'; LINEC = '#D5DDE8'; PAPER = '#FCFBF8'; DEEP = '#8E3A20'

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.edgecolor': LINEC,
                     'axes.labelcolor': INK, 'xtick.color': MUTED, 'ytick.color': INK2,
                     'axes.linewidth': 0.9, 'figure.facecolor': PAPER, 'axes.facecolor': PAPER})

GPQA = [('Claude Mythos Preview', 'Anthropic', 'Apr/2026', 94.5, 'US'),
        ('GPT-5.4', 'OpenAI', 'Mar/2026', 94.4, 'US'),
        ('Gemini 3.1 Pro', 'Google DeepMind', 'Feb/2026', 94.3, 'US'),
        ('Claude Opus 4.7', 'Anthropic', 'Apr/2026', 94.2, 'US'),
        ('Gemini 3 Pro', 'Google DeepMind', 'Nov/2025', 93.8, 'US'),
        ('GPT-5.5', 'OpenAI', 'Apr/2026', 93.6, 'US')]
HLE = [('Claude Mythos Preview', 'Anthropic', 'Apr/2026', 64.7, 'US'),
       ('GPT-5.4', 'OpenAI', 'Mar/2026', 58.7, 'US'),
       ('Muse Spark', 'Meta AI', 'Apr/2026', 58.4, 'US'),
       ('GPT-5.5', 'OpenAI', 'Apr/2026', 57.2, 'US'),
       ('Claude Opus 4.7', 'Anthropic', 'Apr/2026', 54.7, 'US'),
       ('Kimi K2.6', 'Moonshot AI', 'Apr/2026', 54.0, 'CN')]

fig, axes = plt.subplots(1, 2, figsize=(12.6, 3.3), dpi=220, gridspec_kw=dict(wspace=0.42))
fig.subplots_adjust(left=0.155, right=0.99, top=0.80, bottom=0.155)

LABCOL = {'Anthropic': DEEP, 'OpenAI': INK, 'Google DeepMind': ACC2, 'Meta AI': MUTED, 'Moonshot AI': ACC}

def bars(ax, data, ceiling, human, human_label, xmax, title):
    names = [f'{m}\n{l}  ·  {d}' for m, l, d, v, c in data][::-1]
    vals = [v for m, l, d, v, c in data][::-1]
    labs = [l for m, l, d, v, c in data][::-1]
    cols = [LABCOL.get(l, INK) for l in labs]
    ypos = list(range(len(vals)))
    ax.barh(ypos, vals, color=cols, height=0.60, zorder=3)
    for y, v in zip(ypos, vals):
        ax.text(v + xmax * 0.014, y, f'{v:g}', va='center', ha='left', fontsize=8.4,
                color=INK, zorder=4, fontweight='bold')
    ax.set_yticks(ypos)
    ax.set_yticklabels(names, fontsize=8.0, linespacing=1.35)
    ax.axvline(ceiling, color=DEEP, lw=1.2, ls='--', zorder=5)
    ax.text(ceiling + xmax * 0.012, len(vals) - 0.55, f'ceiling ≈ {ceiling:g}%', fontsize=7.3,
            color=DEEP, va='center', ha='left', style='italic', zorder=6)
    ax.axvline(human, color=ACC2, lw=1.5, zorder=5)
    ax.text(human + xmax * 0.012, -0.72, human_label, fontsize=7.3, color=ACC2,
            va='center', ha='left', zorder=6)
    ax.set_xlim(0, xmax)
    ax.set_ylim(-1.0, len(vals) - 0.05)
    ax.set_title(title, fontsize=10, color=INK, pad=6, loc='left')
    ax.grid(axis='x', color=LINEC, lw=0.6, alpha=0.7)
    ax.set_axisbelow(True)
    for sp in ('top', 'right', 'left'):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis='y', length=0)

bars(axes[0], GPQA, 90.0, 34.0, 'human PhD avg = 34', 112,
     'GPQA Diamond — top scores, 2026 (score, ceiling, human reference)')
bars(axes[1], HLE, 25.6, 0.0, 'human average = 0', 78,
     '"Humanity\'s Last Exam" — top scores, 2026 (ceiling ≈ 25.6%)')

fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_scoreboard.png', dpi=220, facecolor=PAPER)
print('fig_scoreboard.png written')
