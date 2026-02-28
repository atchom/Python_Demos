## 🌍 Contexte : planifier l’eau dans un camp de réfugiés

Le HCR doit planifier la quantité d’eau à fournir chaque jour dans un camp.
- Besoin minimum : **20 L d’eau par personne et par jour**
- Population initiale : $P_0$ = 8\,000 personnes
- Chaque jour, il arrive en moyenne **50 nouvelles personnes** (arrivées régulières)

On modélise la population par un **modèle linéaire** :

$$
P(t) = P_0 + a t \qquad\text{équivaut à}\qquad f(x) = a x + b
$$

où :

- $P(t)$ = population au jour t
- $P_0$ = 8000
- La quantité d’eau nécessaire au jour t est :

$$
  E(t)=20⋅P(t)
$$

On veut :

1. La population et le besoin en eau sur 30 jours  
2. Visualiser l’évolution
## Code Python
<div style="background-color: #0d1117; padding: 20px; border-radius: 10px; color: #e6edf3; font-family: monospace;">

  ```python
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
P0 = 8000      # population initiale
a = 50         # arrivées par jour
eau_par_personne = 20  # L/jour/personne
jours = 30

# Jours
t = np.arange(0, jours+1)

# Population chaque jour (modèle linéaire)
P = P0 + a * t

# Besoin en eau chaque jour
E = eau_par_personne * P   # en litres

# Affichage de quelques valeurs
print("Population au jour 30 :", P[-1], "personnes")
print("Besoin en eau au jour 30 :", E[-1], "litres")

# Visualisation
plt.figure(figsize=(12,5))

# Population
plt.subplot(1,2,1)
plt.plot(t, P, marker='o', color='navy')
plt.title("Évolution de la population du camp")
plt.xlabel("Jour")
plt.ylabel("Population")

# Besoin en eau
plt.subplot(1,2,2)
plt.plot(t, E, marker='o', color='teal')
plt.title("Besoin en eau quotidien")
plt.xlabel("Jour")
plt.ylabel("Eau (litres)")

plt.tight_layout()
plt.show()
```
</div>

# 🏕️ Scénario opérationnel 2024 – Camp de Réfugiés de Méké (Éthiopie)

## 🌍 Contexte général

Le camp de Méké, situé dans la région du Tigré en Éthiopie, accueille des populations fuyant les conflits armés, l’insécurité alimentaire et les épisodes de sécheresse. L’année 2024 a été marquée par une forte variabilité des arrivées, des contraintes logistiques importantes et une pression croissante sur les ressources en eau.

Ce document présente une synthèse complète du scénario 2024 : évolution de la population, besoins en eau, incidents critiques, décisions opérationnelles et enseignements clés.

---

## 📊 Synthèse visuelle du scénario 2024

La visualisation ci‑dessous regroupe :

- les arrivées hebdomadaires,
- la comparaison des scénarios d’afflux (bas, moyen, haut),
- l’évolution du besoin en eau quotidien,
- les indicateurs clés à 30, 60 et 90 jours.

<p align="center">
  
<img width="1990" height="1403" alt="image" src="https://github.com/user-attachments/assets/88b0da17-1586-4350-9fa9-e1ce489e7c73" />
</p>

---

## 🧭 Situation initiale (Janvier – Jour 0)

- **Population initiale :** 8 000 personnes  
- **Capacité maximale du camp :** 15 000 personnes  
- **Sources d’eau disponibles :**
  - 3 camions‑citernes (20 000 L chacun)
  - 2 puits opérationnels  
- **Contexte :** saison sèche, routes praticables, flux modéré d’arrivées

---

## 📈 Évolution de la population sur l’année

| Période      | Événement majeur                               | Impact sur les flux | Population estimée |
|--------------|--------------------------------------------------|----------------------|---------------------|
| Janv–Mars    | Saison sèche, arrivées modérées                 | +30 à +40/jour       | 8 000 → 11 200      |
| Avril        | Début des pluies, routes difficiles             | -50% d’arrivées      | 11 200 → 11 500     |
| Mai          | Ouverture de nouveaux camps au Soudan           | Départs volontaires  | 11 500 → 11 300     |
| Juin         | Intensification du conflit                      | +150/jour            | 11 300 → 13 100     |
| Juillet      | Capacité presque atteinte                       | Arrivées limitées    | 13 100 → 14 200     |
| Août         | Saturation du camp                              | Arrivées = départs   | ~14 500             |
| Sept–Déc     | Stabilisation                                   | Variations faibles   | 14 000–15 000       |

---

## ⚠️ Incidents et contraintes opérationnelles

- **Février :** Panne d’un camion‑citerne → rationnement à **15 L/personne/jour**  
- **Juin :** Afflux massif → saturation des tentes et points d’eau  
- **Août :** Risque d’épidémie lié au manque d’hygiène  
- **Octobre :** Forage d’un nouveau puits pour augmenter la capacité d’eau  

---

## 🔢 Indicateurs clés

| Indicateur | Valeur |
|------------|--------|
| Population maximale atteinte | **14 800 personnes** (Septembre) |
| Besoin en eau maximal | **296 000 L/jour** |
| Capacité réelle maximale | **280 000 L/jour** |
| Volume total annuel distribué | **≈ 92 millions de litres** |
| Déficit critique observé | **16 000 L/jour** au pic |

---

## 🛠️ Décisions prises par le HCR

- ✔️ **Février :** Réparation d’urgence du camion (48 h)  
- ✔️ **Mai :** Campagne d’information pour limiter les départs  
- ✔️ **Juin :** Activation du protocole d’urgence (rationnement à 15 L/jour)  
- ✔️ **Août :** Forage d’un 3ᵉ puits (financement d’urgence)  
- ✔️ **Octobre :** Extension du camp (+2 000 places)  

---

## 📚 Leçons apprises

- Anticiper les **vagues saisonnières** d’arrivées.  
- Maintenir une **marge de sécurité de 30%** sur les capacités d’eau.  
- Suivre **quotidiennement** la population réelle.  
- Diversifier les **sources d’eau** (puits, camions, stations mobiles).  

---

## 🧩 Conclusion

Le scénario 2024 du camp de Méké illustre la nécessité d’une planification flexible, basée sur des données fiables et capable d’absorber des variations rapides des flux de population. La gestion de l’eau reste un pilier critique de la réponse humanitaire, nécessitant anticipation, redondance et capacité d’adaptation.


