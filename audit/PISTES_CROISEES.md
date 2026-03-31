# Pistes Croisees - Verification et Nouveautes
## Audit Mars 2026

Ce document verifie lesquelles des pistes proposees ont deja ete explorees
dans les 201 rounds de recherche (RESEARCH_MAP.md), et identifie
ce qui est genuinement nouveau.

---

## 1. Status des Pistes

### Deja explorees (Rounds 1-201)

| Piste | Rounds | Resultat |
|-------|--------|---------|
| Verification exhaustive N_0 pour k <= 15 | Rounds 1-50 | Confirme, Lean prouve |
| Theoreme de jonction (non-surjectivite) | Rounds 51-100 | Prouve en Lean |
| Borne de Baker (mu = 6) | Rounds 101-150 | Formalise (hypothese) |
| Fractions continues de log2(3) | Rounds 151-180 | Formalise (hypothese) |
| Verification Barina 2^68 | Round 175 | Comme axiome |
| Sommes de Hardy-Littlewood | Rounds 160-190 | ECHEC (V_SQRT_CANCEL faux) |

### Explorees mais abandonnees a tort

| Piste | Pourquoi abandonnee | Pourquoi reprendre |
|-------|--------------------|--------------------|
| k=16 exhaustif | Suppose couvert par Simons-de Weger | Prouvable SANS axiome |
| k=17 exhaustif | Idem | **NOUVEAU**: N_0=0 confirme en 27.4s |

### Genuinement nouvelles (pas dans les 201 rounds)

| Piste | Description | Reference |
|-------|-------------|-----------|
| S-unites {2,3} | Theorie d'Evertse-Schmidt | 2002, J. Reine Angew. Math. |
| GL_2(F_p) | Contourner l'obstruction abelienne | Helfgott arXiv:0709.2700 |
| Induction sur k | Relation d(k) -> d(k+1) | Original |
| Connexion abc | Baker via conjecture abc | Masser-Oesterlé 1985 |
| Knight (2026) | Cycles de haute altitude | Discrete Math. 349 |
| Crible de Selberg | Comptage des k-cycles | Selberg 1947 |
| Dynamique symbolique | Encoding Collatz en mots | Sofic shifts |
| Approche 3-adique | Complementer Simons-de Weger | Simons-de Weger 2005 |

---

## 2. Analyse Detaillee des 8 Pistes Nouvelles

### Piste 1: S-unites {2,3}
Les termes de corrsum sont tous de la forme 3^a x 2^b (entiers {2,3}-lisses).
Le theoreme d'Evertse-Schlickewei-Schmidt (2002) borne le nombre de solutions
non-degenerees d'equations lineaires sur les S-unites.
**Application:** Montrer que corrSum(A) ≡ 0 (mod d(k)) a peu de solutions.
**arXiv/DOI:** doi:10.1515/crll.2002.038

### Piste 2: GL_2(F_p) non-abelien
L'obstruction principale: 3 n'appartient pas au groupe <2> pour les primes Type II.
**Idee:** Plonger le probleme dans GL_2(F_p) (matrices 2x2 sur F_p).
Ce groupe non-abelien contient <2> comme sous-groupe strict avec structure plus riche.
**Reference:** Helfgott (2008), arXiv:0709.2700

### Piste 3: Induction sur k
**Idee centrale:** Si N_0(d(k)) = 0, peut-on deduire N_0(d(k+1)) = 0?
Les compositions de taille k et k+1 ont des liens structurels.
Si une telle relation existe, une seule preuve de base + induction couvre tous k.

### Piste 4: Conjecture abc
abc affirme: max(|a|,|b|,|c|) < rad(abc)^{1+epsilon} pour a+b=c.
Avec a=2^S, b=-3^k, c=d(k): donne d(k) > 2^{S*(1-epsilon)}.
Plus propre que Baker mais abc non prouvee.

### Piste 5: Knight (2026)
"Collatz high cycles do not exist" - Discrete Mathematics 349, Mars 2026.
A verifier si ce papier couvre les memes k que le Theoreme de Jonction.
**Action:** Acceder au papier et comparer hypotheses et conclusions.

### Piste 6: Crible de Selberg
Utiliser un crible analytique pour borner le nombre de k-cycles candidats.
Analogie avec la preuve par crible de la rarete des nombres premiers jumeaux.

### Piste 7: Dynamique symbolique
Representer l'orbite de Collatz comme un mot infini sur {0,1}.
Les outils d'entropie topologique (Lind et Marcus 1995) formalisent
l'ecart gamma ~ 0.05 de facon tres precise.

### Piste 8: Approche 3-adique
Simons-de Weger utilise les logarithmes 2-adiques.
Une approche 3-adique symetrique pourrait donner des bornes complementaires
et couvrir des cas manquants.

---

## 3. Pistes "Ressuscitables"

### 3.1 Verification exhaustive k=18
k=18: S=29, C(28,17) ~ 3 millions de sequences.
Temps estime: ~10 minutes en Python.
**Cette piste devrait etre reprise.**

### 3.2 Distribution empirique de corrsum mod d(k)
Histogrammes jamais traces. Visualisation facile en Python.
Confirmerait empiriquement la non-surjectivite.

### 3.3 Estimation Monte-Carlo pour k=18..25
Pour k > 18, exhaustivite impossible mais Monte-Carlo peut estimer N_0.
Si N_0 ~ 0 sur 10^6 echantillons aleatoires: fort indice confirmatoire.

---

## 4. References arXiv Recommandees

1. Tao (2019) - arXiv:1909.03562
2. Helfgott (2008) - arXiv:0709.2700  
3. Evertse et al. (2002) - DOI:10.1515/crll.2002.038
4. Simons-de Weger (2005) - Acta Arithmetica 115
5. Baker-Wustholz (1993) - J. Reine Angew. Math.
6. Barina (2021) - arXiv:2102.01529
7. Knight (2026) - Discrete Mathematics 349

---
*Voir SYNTHESE_MARS2026.md pour le contexte general.*
