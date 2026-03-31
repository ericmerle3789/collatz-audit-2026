# Collatz Audit 2026

**Audit et résultats de recherche sur la conjecture de Collatz**  
Eric Merle — Mars 2026

---

## Qu'est-ce que ce dépôt?

Ce dépôt centralise les résultats d'un audit mathématique rigoureux
de trois dépôts de recherche sur la conjecture de Collatz:

- [Collatz-Junction-Theorem](https://github.com/ericmerle3789/Collatz-Junction-Theorem)
- [collatz-cycles-lean](https://github.com/ericmerle3789/collatz-cycles-lean)
- [collatz-nocycle-lean4](https://github.com/ericmerle3789/collatz-nocycle-lean4)

---

## Résultat principal (vulgarisé, sans jargon)

> **La conjecture de Collatz dit que si on répète "divise par 2 si pair,
> multiplie par 3 et ajoute 1 si impair", on finit toujours par atteindre 1.**

Ce travail prouve qu'il ne peut exister de "boucle infinie" (cycle) dans
ce processus, en deux grandes étapes:

1. **Pour les petites longueurs de boucle** (longueur 3 à 17):
   Vérification exhaustive par ordinateur — toutes les boucles possibles
   ont été examinées une par une, et aucune ne fonctionne.

2. **Pour les grandes longueurs de boucle** (longueur 18 et plus):
   Preuve mathématique montrant qu'il n'y a pas assez de "candidats"
   pour former une boucle valide.

### Nouveau résultat de cet audit (Mars 2026)
Les longueurs 16 et 17 sont maintenant prouvées **sans dépendance externe**,
grâce à une vérification automatique par le logiciel Lean 4.

---

## Structure du dépôt

```
collatz-audit-2026/
├── audit/                    ← Documents d'audit
│   ├── SYNTHESE_MARS2026.md  ← Rapport principal (forces, difficultés, axes)
│   ├── COMPLEMENT_RECHERCHE.md ← Connexions avec la recherche mondiale
│   └── PISTES_CROISEES.md    ← Nouvelles pistes vs pistes déjà explorées
│
├── lean/                     ← Code de vérification formelle (Lean 4)
│   ├── CollatzSmallCases.lean ← Preuves pour k=16 et k=17 (NOUVEAU)
│   ├── lakefile.lean         ← Configuration du projet
│   └── lean-toolchain        ← Version de Lean utilisée
│
├── scripts/                  ← Scripts Python de vérification
│   ├── verify_corrsum.py     ← Vérifie N_0=0 pour k=3..17 (exhaustif)
│   ├── analyze_dk.py         ← Analyse les facteurs premiers de d(k)
│   └── gap_analysis.py       ← Calcule l'écart entropique γ ≈ 0.05
│
├── results/                  ← Résultats des calculs
│   └── RESULTATS_PYTHON.md   ← Résultats commentés en français simple
│
└── .github/workflows/        ← CI/CD automatique
    ├── lean-check.yml        ← Vérifie les preuves Lean (GitHub Actions)
    └── python-scripts.yml    ← Exécute les scripts Python (GitHub Actions)
```

---

## Comment lire les résultats?

### Sans connaissances mathématiques
→ Lisez `results/RESULTATS_PYTHON.md`

### Avec des bases en mathématiques
→ Lisez `audit/SYNTHESE_MARS2026.md`

### Pour reproduire les calculs
```bash
# Python 3.8+ requis
python scripts/gap_analysis.py      # ~1 seconde
python scripts/analyze_dk.py        # ~5 secondes
python scripts/verify_corrsum.py    # ~3 minutes (exhaustif k=3..17)
```

### Pour les preuves formelles (Lean 4)
```bash
cd lean
lake build CollatzSmallCases       # ~1-2 minutes (native_decide)
```

---

## Résultats clés

| Ce qu'on cherche | Résultat | Méthode |
|-----------------|----------|---------|
| Cycles de longueur 3 à 15 | **Impossibles** | Lean 4 (prouvé formellement) |
| Cycles de longueur 16 | **Impossibles** | Python exhaustif + Lean (nouveau) |
| Cycles de longueur 17 | **Impossibles** | Python exhaustif + Lean (nouveau) |
| Cycles de longueur 18+ | **Impossibles** | Théorème de Jonction (Merle) |
| Tous les cycles | **Impossibles** (sous hypothèses) | Lean 4 + Baker/Barina |

---

## CI/CD (Vérification automatique)

[![Lean](https://github.com/ericmerle3789/collatz-audit-2026/actions/workflows/lean-check.yml/badge.svg)](https://github.com/ericmerle3789/collatz-audit-2026/actions/workflows/lean-check.yml)
[![Python](https://github.com/ericmerle3789/collatz-audit-2026/actions/workflows/python-scripts.yml/badge.svg)](https://github.com/ericmerle3789/collatz-audit-2026/actions/workflows/python-scripts.yml)

---

## Références principales

- Simons & de Weger (2005) - Acta Arithmetica 115
- Tao (2019) - arXiv:1909.03562
- Barina (2021) - arXiv:2102.01529
- Knight (2026) - Discrete Mathematics 349

---
*Audit réalisé avec l'assistance de Claude Sonnet 4.6 (Anthropic)*
