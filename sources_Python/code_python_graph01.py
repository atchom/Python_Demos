import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from matplotlib.patches import Circle
import matplotlib.patches as mpatches

# Désactiver tout thème sombre
plt.rcParams.update(plt.rcParamsDefault)
import matplotlib as mpl
mpl.rcParams['figure.facecolor'] = 'white'
mpl.rcParams['axes.facecolor'] = 'white'
mpl.rcParams['savefig.facecolor'] = 'white'
mpl.rcParams['figure.edgecolor'] = 'white'
mpl.rcParams['axes.edgecolor'] = '#0033A0'
mpl.rcParams['axes.labelcolor'] = '#0033A0'
mpl.rcParams['xtick.color'] = '#0033A0'
mpl.rcParams['ytick.color'] = '#0033A0'
mpl.rcParams['text.color'] = '#0033A0'

# Données du dataset
data = """Semaine;Arrivees;Evenement;Periode;Population_estimee;Besoin_eau_L_jour;Source_principale
1;217;;Jan-Mar;8217;164340;2 puits + camion-citerne
2;245;;Jan-Mar;8462;169240;2 puits + camion-citerne
3;210;;Jan-Mar;8672;173440;2 puits + camion-citerne
4;238;;Jan-Mar;8910;178200;2 puits + camion-citerne
5;233;;Jan-Mar;9143;182860;2 puits + camion-citerne
6;266;Panne camion rationnement 15L;Jan-Mar;9409;141135;2 puits + camion-citerne (panne)
7;258;;Jan-Mar;9667;193340;2 puits + camion-citerne
8;249;;Jan-Mar;9916;198320;2 puits + camion-citerne
9;238;;Jan-Mar;10154;203080;2 puits + camion-citerne
10;230;;Jan-Mar;10384;207680;2 puits + camion-citerne
11;252;;Jan-Mar;10636;212720;2 puits + camion-citerne
12;200;;Jan-Mar;10836;216720;2 puits + camion-citerne
1;112;;Avril;10948;218960;2 puits + camion-citerne
2;100;;Avril;11048;220960;2 puits + camion-citerne
1;200;Departs volontaires;Mai;10848;216960;2 puits + camion-citerne
1;45;;Mai;10893;217860;2 puits + camion-citerne
2;48;;Mai;10941;218820;2 puits + camion-citerne
2;33;;Mai;10974;219480;2 puits + camion-citerne
2;1050;Afflux massif;Juin;12024;240480;2 puits + camion-citerne
2;1050;Protocole urgence 15L;Juin;13074;196110;2 puits + camion-citerne
2;228;;Juin;13302;266040;2 puits + camion-citerne
2;30;Capacite presque atteinte;Juillet;13332;266640;2 puits + camion-citerne
2;25;Capacite presque atteinte;Juillet;13357;267140;2 puits + camion-citerne
2;20;Capacite presque atteinte;Juillet;13377;267540;2 puits + camion-citerne
3;22;Capacite presque atteinte;Juillet;13399;267980;2 puits + camion-citerne
3;25;Saturation arrivees=departs;Aout;13424;268480;3 forage + camion-citerne
3;30;Nouveau puits fore;Aout;13454;269080;3 forage + camion-citerne
3;28;;Aout;13482;269640;3 forage + camion-citerne
3;26;;Aout;13508;270160;3 forage + camion-citerne
3;24;;Aout;13532;270640;3 forage + camion-citerne
3;18;;Sept-Dec;13550;271000;3 forage + camion-citerne
3;15;Stabilisation;Sept-Dec;13565;271300;3 forage + camion-citerne
3;20;Stabilisation;Sept-Dec;13585;271700;3 forage + camion-citerne
4;18;Stabilisation;Sept-Dec;13603;272060;3 forage + camion-citerne
4;15;Stabilisation;Sept-Dec;13618;272360;3 forage + camion-citerne
4;12;Stabilisation;Sept-Dec;13630;272600;3 forage + camion-citerne
4;10;Stabilisation;Sept-Dec;13640;272800;3 forage + camion-citerne
4;15;Stabilisation;Sept-Dec;13655;273100;3 forage + camion-citerne
4;20;Stabilisation;Sept-Dec;13675;273500;3 forage + camion-citerne
4;18;Stabilisation;Sept-Dec;13693;273860;3 forage + camion-citerne
4;22;Stabilisation;Sept-Dec;13715;274300;3 forage + camion-citerne"""

df = pd.read_csv(StringIO(data), sep=';')

# Couleurs UNHCR
UNHCR_BLUE = '#0033A0'
UNHCR_LIGHT_BLUE = '#4B8AC8'
UNHCR_RED = '#E4002B'
UNHCR_GREY = '#666666'
WHITE = '#FFFFFF'

# Traitement des données
periode_order = ['Jan-Mar', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Sept-Dec']
df['Periode'] = pd.Categorical(df['Periode'], categories=periode_order, ordered=True)

# Arrivées TOTALES par période
arrivees_par_periode = df.groupby('Periode', observed=True)['Arrivees'].sum()
population_par_periode = df.groupby('Periode', observed=True)['Population_estimee'].mean().round()
besoin_par_periode = df.groupby('Periode', observed=True)['Besoin_eau_L_jour'].mean() / 1000
seuil_saturation = 13300

# Sources d'eau
df['Source_principale_propre'] = df['Source_principale'].replace({
    '2 puits + camion-citerne (panne)': '2 puits + camion-citerne'
})
sources = df['Source_principale_propre'].value_counts()
sources.index = ['2 puits +\ncamion-citerne', '3 forage +\ncamion-citerne']

# CRÉATION DE LA FIGURE
fig = plt.figure(figsize=(22, 14), facecolor=WHITE)
fig.patch.set_facecolor(WHITE)

# Logo et titre (descendus pour éviter la coupure)
fig.text(0.05, 0.95, 'UNHCR', fontsize=34, fontweight='bold', color=UNHCR_BLUE)
fig.text(0.05, 0.925, 'The UN Refugee Agency', fontsize=16, style='italic', color=UNHCR_GREY)
fig.text(0.5, 0.95, 'CAMP DE RÉFUGIÉS MÉKÉ (ÉTHIOPIE) - SCÉNARIO 2024', 
         fontsize=20, fontweight='bold', color=UNHCR_BLUE, ha='center')

# 1. GRAPHIQUE ARRIVÉES MENSUELLES
ax1 = plt.subplot(2, 3, (1, 2))
ax1.set_facecolor(WHITE)
x_pos = np.arange(len(arrivees_par_periode))

# Barres des arrivées
bars = ax1.bar(x_pos, arrivees_par_periode.values, color=UNHCR_BLUE, width=0.6)

# Valeurs sur les barres : TOUTES placées AU-DESSUS en bleu
offset_label = 20  # décalage vers le haut
for bar, val in zip(bars, arrivees_par_periode.values):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + offset_label,
             f'{int(val)}', ha='center', fontweight='bold', fontsize=12,
             color=UNHCR_BLUE)

# Population
ax1b = ax1.twinx()
pop_values = population_par_periode.values / 1000

# Ligne de population
ax1b.plot(x_pos, pop_values, color=UNHCR_GREY, linewidth=2.5, marker='o',
          markersize=12, markeredgecolor=WHITE, markeredgewidth=2.5,
          label='Population (milliers)')

# Colorier les points selon le seuil
for i, (x, pop) in enumerate(zip(x_pos, pop_values)):
    color = UNHCR_RED if pop > seuil_saturation/1000 else UNHCR_LIGHT_BLUE
    ax1b.plot(x, pop, 'o', markersize=12, color=color,
              markeredgecolor=WHITE, markeredgewidth=2.5)
    # Étiquettes population (décalage réduit)
    y_offset = 0.15
    ax1b.text(x, pop + y_offset, f'{pop:.1f}k', ha='center', fontweight='bold', fontsize=11,
              color=UNHCR_RED if pop > seuil_saturation/1000 else UNHCR_BLUE)

# Ajustement des limites pour laisser de l'espace en haut
ax1.set_ylim(0, max(arrivees_par_periode) * 1.15)  # laisse de la place pour les étiquettes au-dessus
ax1b.set_ylim(8, 15)  # marge supérieure à 15

# Configuration
ax1.set_xticks(x_pos)
ax1.set_xticklabels(arrivees_par_periode.index, fontweight='bold', fontsize=13, color=UNHCR_BLUE)
ax1.set_ylabel('Arrivées (totaux par période)', fontweight='bold', fontsize=13, color=UNHCR_BLUE, labelpad=15)
ax1b.set_ylabel('Population (milliers)', fontweight='bold', fontsize=13, color=UNHCR_BLUE, labelpad=15)
ax1.set_title('ARRIVÉES MENSUELLES PAR PÉRIODE', fontweight='bold', fontsize=16, color=UNHCR_BLUE, pad=20)

# Seuil de saturation
seuil_line = ax1b.axhline(y=seuil_saturation/1000, color=UNHCR_RED, linestyle='--', linewidth=2.5)
ax1b.text(len(x_pos)-0.5, seuil_saturation/1000 + 0.3, 'Seuil saturation',
          color=UNHCR_RED, ha='right', fontweight='bold', fontsize=12)

# Légende pour la population (déplacée en zone neutre)
from matplotlib.lines import Line2D
legend_elements_pop = [
    Line2D([0], [0], color=UNHCR_GREY, linewidth=2.5, label='Population'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=UNHCR_LIGHT_BLUE,
           markersize=10, label='Sous seuil', markeredgecolor=WHITE),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=UNHCR_RED,
           markersize=10, label='Au-dessus seuil', markeredgecolor=WHITE),
    Line2D([0], [0], color=UNHCR_RED, linestyle='--', linewidth=2, label='Seuil saturation')
]
# Correction : remplacer transform par bbox_transform
ax1b.legend(handles=legend_elements_pop, loc='center', bbox_to_anchor=(5.8, 12.3),
            bbox_transform=ax1b.transData, fontsize=11, frameon=True,
            facecolor=WHITE, edgecolor=UNHCR_BLUE)

# Annotations des événements
annotations = [
    ('Jan-Mar', 300, 'Panne camion\nrationnement 15L'),
    ('Juin', 1800, 'Afflux massif\nprotocole urgence'),
    ('Aout', 60, 'Nouveau puits\nforé'),
    ('Sept-Dec', 40, 'Stabilisation')
]

for periode, y, texte in annotations:
    if periode in arrivees_par_periode.index:
        idx = list(arrivees_par_periode.index).index(periode)
        ax1.annotate(texte, xy=(idx, y), xytext=(idx, y+200), ha='center', fontsize=10,
                    arrowprops=dict(arrowstyle='->', color=UNHCR_RED, lw=2),
                    bbox=dict(boxstyle='round', facecolor=WHITE, edgecolor=UNHCR_RED, alpha=0.95),
                    color=UNHCR_RED, fontweight='bold')

# 2. CAMEMBERT
ax2 = plt.subplot(2, 3, 3)
ax2.set_facecolor(WHITE)
ax2.set_aspect('equal')

wedges, texts, autotexts = ax2.pie(sources.values,
                                     labels=None,
                                     autopct='%1.1f%%',
                                     startangle=90,
                                     colors=[UNHCR_BLUE, UNHCR_LIGHT_BLUE],
                                     wedgeprops={'edgecolor': WHITE, 'linewidth': 2},
                                     textprops={'fontsize': 14, 'fontweight': 'bold'},
                                     pctdistance=0.8)

for autotext in autotexts:
    autotext.set_color(WHITE)
    autotext.set_fontweight('bold')
    autotext.set_fontsize(14)

# Cercle central
centre_circle = Circle((0, 0), 0.65, fc=WHITE, linewidth=0)
ax2.add_artist(centre_circle)
ax2.text(0, 0, 'SOURCES\nD\'EAU', ha='center', va='center',
         fontsize=14, fontweight='bold', color=UNHCR_BLUE, linespacing=1.2)

# Légendes
legend_elements = [
    mpatches.Patch(color=UNHCR_BLUE, label='2 puits +\ncamion-citerne'),
    mpatches.Patch(color=UNHCR_LIGHT_BLUE, label='3 forage +\ncamion-citerne')
]
ax2.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.15),
           fontsize=12, frameon=True, facecolor=WHITE, edgecolor=UNHCR_BLUE,
           handlelength=1.5, handleheight=1.5)

ax2.set_title('SOURCES PRINCIPALES D\'EAU', fontweight='bold', fontsize=16, color=UNHCR_BLUE, pad=30)

# 3. BESOIN EN EAU
ax3 = plt.subplot(2, 3, 4)
ax3.set_facecolor(WHITE)

bars2 = ax3.bar(x_pos, besoin_par_periode.values, color=UNHCR_LIGHT_BLUE, width=0.6)

for bar, val in zip(bars2, besoin_par_periode.values):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2, height + 8,
             f'{int(val)}', ha='center', fontweight='bold', fontsize=12, color=UNHCR_BLUE)

# Seuil critique
seuil_critique = 200
ax3.axhline(y=seuil_critique, color=UNHCR_RED, linestyle='--', linewidth=2.5, label='Seuil critique')
ax3.text(len(x_pos)-0.5, seuil_critique + 12, 'Seuil critique\n200k L/jour',
         color=UNHCR_RED, ha='right', fontweight='bold', fontsize=10,
         bbox=dict(boxstyle='round', facecolor=WHITE, edgecolor=UNHCR_RED, alpha=0.9))

ax3.set_xticks(x_pos)
ax3.set_xticklabels(besoin_par_periode.index, rotation=45, ha='right',
                    fontweight='bold', fontsize=12, color=UNHCR_BLUE)
ax3.set_ylabel('Eau (milliers L/jour)', fontweight='bold', fontsize=13, color=UNHCR_BLUE, labelpad=15)
ax3.set_title('BESOIN EN EAU QUOTIDIEN MOYEN', fontweight='bold', fontsize=16, color=UNHCR_BLUE, pad=20)
ax3.set_ylim(0, 350)
ax3.grid(axis='y', alpha=0.2, color=UNHCR_GREY, linestyle='--')

# 4. TABLEAU DES STATISTIQUES
ax4 = plt.subplot(2, 3, (5, 6))
ax4.axis('off')
ax4.set_facecolor(WHITE)

# Calculs précis
pop_max = df['Population_estimee'].max()
pop_fin = df['Population_estimee'].iloc[-1]
besoin_max = df['Besoin_eau_L_jour'].max()
total_arrivees = df['Arrivees'].sum()

stats_data = [
    ['INDICATEUR', 'VALEUR'],
    ['Population maximale', f"{pop_max:,} personnes"],
    ['Seuil de saturation', f"{seuil_saturation:,} personnes"],
    ['Périodes au-dessus du seuil', 'Juillet, Août, Sept-Déc'],
    ['Besoin en eau maximal', f"{besoin_max:,} L/jour"],
    ['Total arrivées annuelles', f"{total_arrivees:,} personnes"],
    ['Population fin période', f"{pop_fin:,} personnes"],
    ['Source principale', '2 puits + camion (61%) / 3 forages (39%)']
]

# Tableau
table = ax4.table(cellText=stats_data, loc='center', cellLoc='left',
                  colWidths=[0.4, 0.5], bbox=[0.05, 0.15, 0.9, 0.7])

table.auto_set_font_size(False)
table.set_fontsize(14)

for i in range(len(stats_data)):
    for j in range(2):
        cell = table[(i, j)]
        cell.set_edgecolor(UNHCR_GREY)
        cell.set_linewidth(1.5)
        cell.set_height(0.1)
        if i == 0:
            cell.set_facecolor(UNHCR_BLUE)
            cell.set_text_props(weight='bold', color=WHITE, ha='center', fontsize=15)
        else:
            cell.set_facecolor(WHITE)
            cell.set_text_props(color=UNHCR_BLUE, fontsize=13)
            if j == 0:
                cell.set_text_props(weight='bold')

ax4.text(0.5, 0.95, 'STATISTIQUES CLÉS - CAMP MÉKÉ 2024',
         transform=ax4.transAxes, ha='center', fontsize=18,
         fontweight='bold', color=UNHCR_BLUE)

plt.tight_layout()
plt.subplots_adjust(top=0.9, bottom=0.08, hspace=0.3, wspace=0.3)
plt.show()

print("\n" + "="*60)
print("RÉSUMÉ DES DONNÉES - CAMP MÉKÉ 2024")
print("="*60)
print(f"Population maximale: {pop_max:,} personnes")
print(f"Population fin de période: {pop_fin:,} personnes")
print(f"Seuil de saturation: {seuil_saturation:,} personnes")
print(f"Besoin en eau maximal: {besoin_max:,} L/jour")
print(f"Total des arrivées: {total_arrivees:,} personnes")
print("="*60)