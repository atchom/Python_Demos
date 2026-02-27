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
