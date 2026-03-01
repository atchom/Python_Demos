import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# ------------------------------------------------------------
# PALETTE UNHCR
# ------------------------------------------------------------
COULEURS_HCR = {
    'bleu_fonce': '#0033A0',
    'bleu_clair': '#418FDE',
    'blanc': '#FFFFFF',
    'gris_clair': '#F2F2F2',
    'gris_fonce': '#4A4A4A',
    'rouge': '#E74C3C',
    'vert': '#2ECC71',
    'orange': '#F39C12'
}

# ------------------------------------------------------------
# DONNÉES
# ------------------------------------------------------------
periodes = ['Janv-Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Sept-Déc']
flux_journaliers = [35, 17.5, -6.7, 150, 55, 10, 5]

# Données pour la courbe
jours = [0, 90, 120, 150, 180, 210, 240, 365]
pop_jours = [8000, 11200, 11500, 11300, 13100, 14200, 14500, 14750]

# Tableau des périodes
tableau_data = [
    ['Période', 'Événement majeur', 'Impact flux', 'Population'],
    ['Janv–Mars', 'Saison sèche\narrivées modérées', '+30 à +40/j', '8 000 → 11 200'],
    ['Avril', 'Début des pluies\nroutes difficiles', '-50% arrivées', '11 200 → 11 500'],
    ['Mai', 'Nouveaux camps\nau Soudan', 'Départs -200', '11 500 → 11 300'],
    ['Juin', 'Intensification\ndu conflit', '+150/j', '11 300 → 13 100'],
    ['Juillet', 'Capacité\npresque atteinte', 'Arrivées limitées', '13 100 → 14 200'],
    ['Août', 'Saturation\ndu camp', 'Arrivées = départs', '~14 500'],
    ['Sept–Déc', 'Stabilisation', 'Variations faibles', '14 000–15 000']
]

# ------------------------------------------------------------
# CONSTRUCTION DE LA FIGURE AVEC GRIDSPEC
# ------------------------------------------------------------
fig = plt.figure(figsize=(18, 10))
fig.patch.set_facecolor(COULEURS_HCR['blanc'])

# Grille : 2 lignes, 2 colonnes, la première ligne fusionnée
gs = gridspec.GridSpec(2, 2, height_ratios=[1.5, 1], hspace=0.3, wspace=0.25)

# ------------------------------------------------------------
# 1. GRAPHIQUE PRINCIPAL (toute la largeur en haut)
# ------------------------------------------------------------
ax1 = plt.subplot(gs[0, :])
ax1.set_facecolor(COULEURS_HCR['gris_clair'])

# Courbe principale
ax1.plot(jours, pop_jours, color=COULEURS_HCR['bleu_fonce'],
         linewidth=4, marker='o', markersize=12,
         markeredgecolor=COULEURS_HCR['blanc'],
         markeredgewidth=2, markerfacecolor=COULEURS_HCR['bleu_clair'],
         label='Évolution population', zorder=5)

# Zones colorées des périodes
couleurs_periodes = ['#2E7D32', '#4CAF50', '#8BC34A', '#FFC107',
                     '#FF9800', '#F44336', '#9C27B0']
for i, (debut, fin, couleur) in enumerate(zip(jours[:-1], jours[1:], couleurs_periodes)):
    ax1.axvspan(debut, fin, alpha=0.15, color=couleur)
    milieu = (debut + fin) / 2
    ax1.text(milieu, 8000, periodes[i], ha='center', va='bottom',
             color=COULEURS_HCR['bleu_fonce'], fontweight='bold', fontsize=11,
             bbox=dict(facecolor=COULEURS_HCR['blanc'], alpha=0.7, boxstyle='round,pad=0.3'))

# Annotations des valeurs
for jour, pop in zip(jours, pop_jours):
    ax1.annotate(f'{int(pop)}', (jour, pop),
                 xytext=(0, 10), textcoords='offset points',
                 ha='center', color=COULEURS_HCR['blanc'],
                 fontweight='bold', fontsize=11,
                 bbox=dict(facecolor=COULEURS_HCR['bleu_fonce'], alpha=0.8, boxstyle='round,pad=0.2'))

# Lignes de capacité
ax1.axhline(y=15000, color=COULEURS_HCR['rouge'], linestyle='--', linewidth=2.5,
            label='Capacité max (15 000)', alpha=0.8)
ax1.axhline(y=17000, color=COULEURS_HCR['orange'], linestyle=':', linewidth=2,
            label='Extension potentielle', alpha=0.6)

ax1.set_xlabel('Jours', fontsize=14, fontweight='bold', color=COULEURS_HCR['gris_fonce'])
ax1.set_ylabel('Population', fontsize=14, fontweight='bold', color=COULEURS_HCR['gris_fonce'])
ax1.set_title('ÉVOLUTION DE LA POPULATION - CAMP MÉKÉ 2024',
              fontsize=18, fontweight='bold', color=COULEURS_HCR['bleu_fonce'], pad=20)
ax1.set_xlim(-10, 375)
ax1.set_ylim(7000, 18000)
ax1.set_xticks(jours)
ax1.set_xticklabels(['J0\nJanv', 'J90\nMars', 'J120\nAvril', 'J150\nMai',
                     'J180\nJuin', 'J210\nJuil', 'J240\nAoût', 'J365\nDéc'])
ax1.tick_params(colors=COULEURS_HCR['gris_fonce'], labelsize=11)
ax1.grid(True, alpha=0.3, linestyle='--', color='gray')
ax1.legend(loc='upper left', frameon=True, facecolor=COULEURS_HCR['blanc'],
           edgecolor=COULEURS_HCR['bleu_fonce'], labelcolor=COULEURS_HCR['gris_fonce'],
           fontsize=11)

# ------------------------------------------------------------
# 2. GRAPHIQUE DES FLUX JOURNALIERS (bas gauche)
# ------------------------------------------------------------
ax2 = plt.subplot(gs[1, 0])
ax2.set_facecolor(COULEURS_HCR['gris_clair'])

couleurs_barres = [
    COULEURS_HCR['bleu_fonce'],  # Janv-Mars
    COULEURS_HCR['bleu_clair'],  # Avril
    COULEURS_HCR['bleu_fonce'],  # Mai
    COULEURS_HCR['bleu_fonce'],  # Juin
    COULEURS_HCR['bleu_clair'],  # Juillet
    COULEURS_HCR['gris_fonce'],  # Août
    COULEURS_HCR['gris_fonce']   # Sept-Déc
]

bars = ax2.bar(periodes, flux_journaliers, color=couleurs_barres,
               edgecolor=COULEURS_HCR['bleu_fonce'], linewidth=1.5, alpha=0.9)

for bar, val in zip(bars, flux_journaliers):
    height = bar.get_height()
    signe = '+' if val > 0 else ''
    ax2.text(bar.get_x() + bar.get_width()/2.,
             height + 2 if val > 0 else height - 8,
             f'{signe}{val:.1f}/j', ha='center',
             va='bottom' if val > 0 else 'top',
             color=COULEURS_HCR['gris_fonce'], fontweight='bold', fontsize=10)

ax2.axhline(y=0, color=COULEURS_HCR['gris_fonce'], linewidth=1)
ax2.set_xlabel('Période', fontsize=13, fontweight='bold', color=COULEURS_HCR['gris_fonce'])
ax2.set_ylabel('Flux net (personnes/jour)', fontsize=13, fontweight='bold', color=COULEURS_HCR['gris_fonce'])
ax2.set_title('FLUX JOURNALIERS PAR PÉRIODE', fontsize=16, fontweight='bold',
              color=COULEURS_HCR['bleu_fonce'], pad=15)
ax2.tick_params(colors=COULEURS_HCR['gris_fonce'], labelsize=10, rotation=45)
ax2.grid(True, alpha=0.3, linestyle='--', color='gray', axis='y')

# ------------------------------------------------------------
# 3. TABLEAU DES PÉRIODES (bas droite)
# ------------------------------------------------------------
ax3 = plt.subplot(gs[1, 1])
ax3.axis('tight')
ax3.axis('off')
ax3.set_facecolor(COULEURS_HCR['blanc'])

table = ax3.table(cellText=tableau_data, loc='center', cellLoc='center',
                  colWidths=[0.16, 0.25, 0.2, 0.16], bbox=[0, 0, 1, 1])

table.auto_set_font_size(False)
table.set_fontsize(10)

for i in range(len(tableau_data)):
    for j in range(4):
        cell = table[(i, j)]
        if i == 0:
            cell.set_facecolor(COULEURS_HCR['bleu_fonce'])
            cell.set_text_props(color=COULEURS_HCR['blanc'], fontweight='bold')
        else:
            cell.set_facecolor(COULEURS_HCR['gris_clair'] if i % 2 == 0 else COULEURS_HCR['blanc'])
            cell.set_text_props(color=COULEURS_HCR['gris_fonce'])
            if j == 3:
                cell.set_text_props(color=COULEURS_HCR['bleu_fonce'], fontweight='bold')

ax3.set_title('DÉTAIL DES PÉRIODES', fontsize=16, fontweight='bold',
              color=COULEURS_HCR['bleu_fonce'], pad=10)

# ------------------------------------------------------------
# LOGO UNHCR
# ------------------------------------------------------------
fig.text(0.02, 0.98, 'UNHCR', fontsize=24, fontweight='bold',
         color=COULEURS_HCR['bleu_fonce'], transform=fig.transFigure)
fig.text(0.02, 0.955, 'The UN Refugee Agency', fontsize=12,
         color=COULEURS_HCR['bleu_fonce'], transform=fig.transFigure)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()