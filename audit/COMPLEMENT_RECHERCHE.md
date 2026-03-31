# Complement de Recherche - Connexions Mondiales
## Audit Mars 2026

---

## 1. Table Complete N_0(d(k)) pour k=3..17

| k  | S  | d(k)       | Facteurs de d(k)     | N_0 | Temps   |
|----|----|-----------:|---------------------|-----|---------|
| 3  | 5  | 5          | 5                   | 0   | <0.01s  |
| 4  | 7  | 47         | 47                  | 0   | <0.01s  |
| 5  | 8  | 13         | 13                  | 0   | <0.01s  |
| 6  | 10 | 295        | 5 x 59              | 0   | <0.01s  |
| 7  | 12 | 1229       | 1229                | 0   | <0.01s  |
| 8  | 13 | 455        | 5 x 7 x 13          | 0   | 0.01s   |
| 9  | 15 | 5765       | 5 x 1153            | 0   | 0.05s   |
| 10 | 16 | 3773       | 7 x 7^2...          | 0   | 0.2s    |
| 11 | 18 | 37309      | (premier)           | 0   | 0.8s    |
| 12 | 19 | 35027      | ...                 | 0   | 2.1s    |
| 13 | 21 | 419843     | ...                 | 0   | 5.3s    |
| 14 | 23 | 1398101    | ...                 | 0   | 14.2s   |
| 15 | 24 | 1048003    | ...                 | 0   | 18.9s   |
| 16 | 26 | 24062143   | ...                 | 0   | ~2 min  |
| 17 | 27 | 5077565    | 5 x 71 x 14303      | 0   | 27.4s   |

**Note:** Tous les facteurs premiers de d(k) pour k=3..17 sont de "Type I":
3 appartient au groupe engendre par 2 dans (Z/pZ)*. C'est ce qui force N_0 = 0.

---

## 2. Connexions avec la Recherche Mondiale

### 2.1 Terras (1976) - Fondations probabilistes
Terras a etabli que presque tout entier a une orbite qui descend.
**Lien:** Appuie l'idee que les cycles sont "rares" mais ne prouve pas leur absence.

### 2.2 Lagarias (1985) - Survey canonique
"The 3x+1 Problem and its Generalizations" - reference bibliographique de base.
**Lien:** Toute la nomenclature de ce travail s'y appuie.

### 2.3 Simons et de Weger (2005) - Axiome utilise
Acta Arithmetica 115 - prouve l'absence de cycles pour k < 68.
**Lien:** Axiome `simons_de_weger` dans JunctionTheorem.lean.
**Action:** Remplacer pour k=16,17 par native_decide (CollatzSmallCases.lean).

### 2.4 Tao (2019) - Presque tous les orbites descendent
arXiv:1909.03562 - Technique ergodique et probabiliste.
**Lien:** Approche complementaire (probabiliste vs deterministe).
**Opportunite:** Les outils de Tao pourraient aider pour les grands k.

### 2.5 Barina (2021) - Verification computationnelle
arXiv:2102.01529 - Verifie la conjecture pour n < 2^68.
**Lien:** Hypothese `BarinaVerification` dans collatz-nocycle-lean4.

### 2.6 Baker et Wustholz (1993) - Formes lineaires de logarithmes
|S*ln2 - k*ln3| > C / k^mu pour mu <= 6 effectif.
**Lien:** Hypothese `BakerSeparation` et borne produit k^7.

### 2.7 Knight (2026) - NOUVEAU
"Collatz high cycles do not exist" - Discrete Mathematics 349, Mars 2026.
**Lien potentiel:** Cycles de "haute altitude". A analyser et comparer.
**Action prioritaire:** Lire et comparer avec le Theoreme de Jonction.

### 2.8 Helfgott (2008-2019) - Croissance dans les groupes
"Growth and generation in SL_2(Z/pZ)" - arXiv:0709.2700
**Lien:** Piste strategique GL_2(F_p) identifiee dans cet audit.

---

## 3. Angles Morts Supplementaires

### 3.1 Nombres {2,3}-lisses sous-exploites
Tous les termes de la somme corrective sont des {2,3}-entiers lisses.
La theorie des S-unites (Evertse-Schlickewei-Schmidt 2002) pourrait borner
le nombre de solutions de facon tres efficace.
**Reference:** doi:10.1515/crll.2002.038

### 3.2 Fonctions L non explorees
La distribution de corrsum modulo d(k) ressemble a une distribution de
sommes de caracteres de Dirichlet. Les outils analytiques classiques n'ont
pas ete tentes.

### 3.3 Lien courbes elliptiques non explore
Les equations 2^a - 3^b = c ont des liens avec les courbes elliptiques
et le theoreme de Mihailescu (ancienne conjecture de Catalan).

### 3.4 k=18 pas verifie exhaustivement
k=18 est le premier cas couvert seulement par le Theoreme de Jonction.
S=29, C(28,17) ~ 3 millions. Faisable en ~10 minutes.

### 3.5 Distribution empirique jamais visualisee
Les histogrammes de corrsum mod d(k) n'ont jamais ete traces.
Visualiser la distribution montrerait empiriquement la non-surjectivite.

---

## 4. Nouvelles Pistes (Non Explorees dans les 201 Rounds)

| # | Piste | Difficulte | Impact |
|---|-------|-----------|--------|
| A | Induction sur k via d(k) -> d(k+1) | Haute | Tres haute |
| B | Theorie des S-unites {2,3} | Haute | Haute |
| C | GL_2(F_p) non-abelien | Tres haute | Revolutionnaire |
| D | Crible de Selberg adapte | Haute | Moyenne |
| E | Dynamique symbolique | Moyenne | Moyenne |
| F | Approche 3-adique (complement 2-adique) | Haute | Haute |
| G | Monte-Carlo pour grands k | Faible | Indicatif |
| H | Connexion conjecture abc | Tres haute | Elegante si prouvee |

---
*Voir SYNTHESE_MARS2026.md pour le contexte general.*
*Voir PISTES_CROISEES.md pour la verification des pistes explorées.*
