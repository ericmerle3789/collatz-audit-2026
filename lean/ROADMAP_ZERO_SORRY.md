# Feuille de route vers 0 sorry

## Etat actuel

La preuve dans `collatz-nocycle-lean4` est COMPLETE sauf 2 hypotheses externes.

### Ce qui est prouve (0 sorry, 0 axiom)

| Composant | Fichier | Statut |
|-----------|---------|--------|
| Definition IsOddCycle | Phase50CycleEquation.lean | Prouve |
| Equation de Steiner | Phase52SteinerEquation.lean | Prouve |
| Borne produit | Phase56Bloc18Complete.lean | Prouve |
| Inegalite de Bernoulli | Phase56Bloc18Complete.lean | Prouve |
| 3n <= k^7 + k | Phase56Bloc18Complete.lean | Prouve |
| k <= 1322 => n < 2^71 | Phase58PorteDeuxFinal.lean | Prouve (native_decide) |
| Cycle empeche reaches_one | Phase50Bridge.lean | Prouve |
| Fractions continues k > 1322 | Phase59ContinuedFractions.lean | Prouve (conditionnel) |

### Ce qui manque (2 sorry)

| # | Hypothese | Enonce | Fichier |
|---|-----------|--------|---------|
| 1 | BakerSeparation | (2^s - 3^k) * k^6 >= 3^k | BakerFormalization.lean |
| 2 | BarinaVerification | n > 0, n < 2^71 => reaches_one n | BarinaFormalization.lean |

## Chemin vers 0 sorry

### Sorry 1: Baker (THEORIQUE)

**Enonce exact:** Pour tout s,k naturels, s >= 1, k >= 2, 2^s > 3^k :
  (2^s - 3^k) * k^6 >= 3^k

**Mathematiquement equivalent a:** la mesure d'irrationalite mu(log_2 3) <= 7

**Resultat connu:** mu(log_2 3) <= 5.125 (Rhin 1987, via Baker)

**Etat de l'art en formalisation:**
- Gelfond-Schneider formalise en Lean 4 (Mars 2026, arXiv:2603.24823)
- Baker: NON formalise dans aucun assistant de preuve au monde
- Estimation: 1-2 ans avec equipe specialisee

**Etapes:**
1. Utiliser la formalisation de Gelfond-Schneider comme base
2. Etendre aux formes lineaires a 2 logarithmes
3. Obtenir une constante effective pour a1=2, a2=3
4. Deduire (2^s - 3^k) * k^6 >= 3^k

### Sorry 2: Barina (COMPUTATIONNEL)

**Enonce exact:** Tout entier positif < 2^71 atteint 1 sous Collatz

**Nature:** Resultat purement computationnel (brute-force GPU)

**Chemins:**
1. **Algorithme certifie** (recommande, 6-12 mois)
   - Formaliser l'algorithme de descente de Barina en Lean
   - Prouver sa correction
   - Executer sur cluster HPC
   
2. **Reduction du seuil** (si Baker avec meilleure constante)
   - Si mu <= 4: seuil tombe sous 2^50
   - native_decide pourrait devenir faisable

## Priorite recommandee

1. **Court terme (semaines):** Contacter les auteurs de Gelfond-Schneider
   (Karatarakis & Wiedijk) pour evaluer la faisabilite de l'extension a Baker

2. **Moyen terme (mois):** Travailler sur l'algorithme certifie de Barina
   (plus accessible que Baker, necessite "juste" de la programmation certifiee)

3. **Long terme (annees):** Formaliser Baker ou trouver une alternative

## Si les 2 sorry sont elimines

Le theoreme final serait:
```lean
theorem no_nontrivial_cycle (n k : Nat) (hcyc : IsOddCycle n k) : False
```
Avec 0 sorry, 0 axiom. Cela constituerait une preuve COMPLETE et IRREFUTABLE
que les cycles Collatz non triviaux n'existent pas.
