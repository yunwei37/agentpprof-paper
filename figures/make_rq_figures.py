#!/usr/bin/env python3
"""Generate RQ1 and RQ3 figures for the AgentPProf paper."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 10,
    'font.family': 'serif',
    'figure.figsize': (3.5, 2.5),
    'axes.grid': True,
    'grid.alpha': 0.3,
})

BLUE = '#2196F3'
RED = '#E57373'
GRAY = '#9E9E9E'


def make_rq1_separation():
    labels = ['No semantic\ntags', 'Session\ntag only', 'Prompt\ntag only', 'Session\n+ Prompt']
    mixed = [90.4, 84.4, 36.7, 0.0]
    residual = [44.7, 33.4, 7.5, 0.0]
    stacks = [11967, 15027, 24703, 26829]

    x = np.arange(len(labels))
    width = 0.28

    fig, ax1 = plt.subplots(figsize=(3.5, 2.5))

    b1 = ax1.bar(x - width/2, mixed, width, label='Mixed weight %',
                 color=RED, alpha=0.85, edgecolor='white')
    b2 = ax1.bar(x + width/2, residual, width, label='Residual %',
                 color='#FFAB91', alpha=0.85, edgecolor='white')

    ax1.set_ylabel('Percentage (%)', fontsize=8)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=7)
    ax1.set_ylim(0, 115)
    ax1.spines['top'].set_visible(False)

    for i, m in enumerate(mixed):
        if m > 5:
            ax1.text(i - width/2, m + 1.5, f'{m:.1f}', ha='center', va='bottom',
                     fontsize=6, color=RED, fontweight='bold')
    for i, r in enumerate(residual):
        if r > 5:
            ax1.text(i + width/2, r + 1.5, f'{r:.1f}', ha='center', va='bottom',
                     fontsize=6, color='#E64A19', fontweight='bold')

    ax2 = ax1.twinx()
    ax2.plot(x, [s/1000 for s in stacks], 's-', color=BLUE, linewidth=1.5,
             markersize=4, label='Unique stacks (k)', zorder=5)
    ax2.set_ylabel('Unique stacks (k)', fontsize=8)
    ax2.set_ylim(0, 35)
    ax2.spines['top'].set_visible(False)

    for i, s in enumerate(stacks):
        ax2.text(i, s/1000 + 1.0, f'{s/1000:.1f}k', ha='center', va='bottom',
                 fontsize=6, color=BLUE, fontweight='bold')

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    fig.legend(h1 + h2, l1 + l2, fontsize=6.5,
               loc='upper center', bbox_to_anchor=(0.5, 1.02),
               ncol=3, framealpha=0.9, columnspacing=0.8)

    plt.tight_layout()
    plt.savefig('fig-rq1-separation.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig-rq1-separation.png', bbox_inches='tight', dpi=300)
    print('Wrote fig-rq1-separation.pdf/png')


def make_rq3_vmeasure():
    datasets = ['mind2web', 'webshop', 'swe-agent', 'weblinx',
                'agenttrek', 'gui-odyssey', 'android', 'toolbench', 'api-bank']
    vmeasure =    [1.000, 1.000, 0.926, 0.872, 0.862, 0.811, 0.716, 0.134, 0.000]
    boundary_f1 = [1.000, 1.000, 0.962, 0.860, None,  0.842, 0.727, 0.353, None]
    ops =         [774,   2504,  496,   500,   200,   7868,  9,     866,   48]

    x = np.arange(len(datasets))
    width = 0.35

    fig, ax = plt.subplots(figsize=(3.5, 2.8))

    vm_colors = [BLUE if v >= 0.7 else GRAY for v in vmeasure]
    bf_colors = ['#81D4FA' if (b is not None and b >= 0.7) else '#BDBDBD'
                 for b in boundary_f1]

    ax.bar(x - width/2, vmeasure, width, color=vm_colors, alpha=0.85,
           edgecolor='white', label='V-measure')

    bf_vals = [b if b is not None else 0 for b in boundary_f1]
    ax.bar(x + width/2, bf_vals, width, color=bf_colors, alpha=0.85,
           edgecolor='white', label='Boundary F1')
    for i, b in enumerate(boundary_f1):
        if b is None:
            ax.text(i + width/2, 0.02, '---', ha='center', va='bottom',
                    fontsize=5, color=GRAY)

    ax.axhline(y=0.7, color=RED, linestyle='--', linewidth=1.0, label='Threshold (0.7)')
    ax.set_ylabel('Score')
    ax.set_xticks(x)
    ax.set_xticklabels(datasets, fontsize=6, rotation=40, ha='right')
    ax.set_ylim(0, 1.18)
    ax.legend(fontsize=6, loc='upper right', framealpha=0.9, ncol=1)

    for i, v in enumerate(vmeasure):
        if v > 0.05:
            ax.text(i - width/2, v + 0.02, f'{v:.2f}', ha='center', va='bottom',
                    fontsize=5, color='#1565C0')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('fig-rq3-vmeasure.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig-rq3-vmeasure.png', bbox_inches='tight', dpi=300)
    print('Wrote fig-rq3-vmeasure.pdf/png')


if __name__ == '__main__':
    make_rq1_separation()
    make_rq3_vmeasure()
