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
    labels = ['No labels', 'Session\nonly', 'Prompt\nonly', 'Session\n+ Prompt']
    mixed = [90.4, 84.4, 36.7, 0.0]
    separated = [9.6, 15.6, 63.3, 100.0]

    x = np.arange(len(labels))
    width = 0.55

    fig, ax = plt.subplots(figsize=(3.5, 2.2))
    ax.bar(x, mixed, width, label='Mixed', color=RED, alpha=0.85, edgecolor='white')
    ax.bar(x, separated, width, bottom=mixed, label='Separated', color=BLUE, alpha=0.85, edgecolor='white')

    ax.set_ylabel('Weight (%)')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylim(0, 105)
    ax.legend(fontsize=8, loc='upper right', framealpha=0.9)

    for i, (m, s) in enumerate(zip(mixed, separated)):
        if m > 10:
            ax.text(i, m / 2, f'{m:.1f}%', ha='center', va='center', fontsize=7, color='white', fontweight='bold')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('fig-rq1-separation.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig-rq1-separation.png', bbox_inches='tight', dpi=300)
    print('Wrote fig-rq1-separation.pdf/png')


def make_rq3_vmeasure():
    datasets = ['mind2web', 'webshop', 'swe-agent', 'weblinx',
                'agenttrek', 'gui-odyssey', 'android', 'toolbench', 'api-bank']
    vmeasure = [1.000, 1.000, 0.926, 0.872, 0.862, 0.811, 0.716, 0.134, 0.000]

    colors = [BLUE if v >= 0.7 else GRAY for v in vmeasure]

    fig, ax = plt.subplots(figsize=(3.5, 2.2))
    x = np.arange(len(datasets))
    bars = ax.bar(x, vmeasure, 0.6, color=colors, alpha=0.85, edgecolor='white')

    ax.axhline(y=0.7, color=RED, linestyle='--', linewidth=1.2, label='Threshold (0.7)')
    ax.set_ylabel('V-measure')
    ax.set_xticks(x)
    ax.set_xticklabels(datasets, fontsize=6.5, rotation=35, ha='right')
    ax.set_ylim(0, 1.12)
    ax.legend(fontsize=7, loc='upper right', framealpha=0.9)

    for i, v in enumerate(vmeasure):
        if v > 0.05:
            ax.text(i, v + 0.02, f'{v:.2f}', ha='center', va='bottom', fontsize=6)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('fig-rq3-vmeasure.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('fig-rq3-vmeasure.png', bbox_inches='tight', dpi=300)
    print('Wrote fig-rq3-vmeasure.pdf/png')


if __name__ == '__main__':
    make_rq1_separation()
    make_rq3_vmeasure()
