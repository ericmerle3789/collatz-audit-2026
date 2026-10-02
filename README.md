> **⚠️ Erratum (octobre 2026) — à lire avant le reste de ce dépôt.**
>
> Ce dépôt est conservé tel quel comme trace de mars 2026. Plusieurs de ses affirmations sont fausses :
>
> 1. **Il ne prouve pas l'absence de cycles.** « Cycles de longueur 18+ : impossibles (Théorème de Jonction) » n'est pas démontré : le Théorème de Jonction établit seulement qu'il y a moins de compositions que de résidus modulo d(k) (non-surjectivité), ce qui n'implique pas qu'aucune ne donne le résidu 0. « Tous les cycles : impossibles (sous hypothèses) » est circulaire : sous la vérification de Bařina (tout n < 2⁷¹ atteint 1), l'hypothèse `DerivedLargeKBound` revient à « aucun cycle pour k > 1322 », c'est-à-dire à la conclusion. Le seul contenu non circulaire de cette chaîne est : aucun cycle non trivial avec k ≤ 1322, sous la vérification de Bařina et l'hypothèse de travail `BakerSeparation` (une inégalité de type Baker qui n'est pas un théorème publié sous cette forme).
> 2. **k = 3 à 18 : rien de nouveau.** L'absence de cycle avec k ≤ 68 termes impairs découle déjà de Simons & de Weger (*Acta Arith.* 117, 2005, 51-70), qui excluent tout m-cycle avec m ≤ 68 (et m ≤ k). La mention « première mondiale » est retirée. Le calcul N₀(d(k)) = 0 ne traite que le plus petit S tel que 2^S > 3^k.
> 3. **Lean : rien n'a été vérifié ici.** La CI Lean a échoué à chaque exécution, dans `lakefile.lean`, avant toute preuve. `native_decide` fait confiance au compilateur (axiome `Lean.ofReduceBool`), pas au noyau seul. Les théorèmes de `CollatzSmallCases.lean` portent sur des sommes modulo d(k), pas sur les cycles eux-mêmes. `BakerSeparationProof.lean` et `ContinuedFractionBridge.lean` contiennent des `sorry`, et les fenêtres de fractions continues s'arrêtent à k < 10 590 737. La toolchain v4.14.0 est antérieure au correctif du bug noyau lean4#14576 (v4.32.2, 28 juillet 2026).
> 4. **Chiffres et références erronés.** μ = 5,125 est la mesure d'irrationalité de **ln 3** (Salikhov 2007), pas de log₂3, et n'est pas due à Rhin 1987. « BakerSeparation ⇔ μ(log₂3) ≤ 6 ou 7 » est faux : l'inégalité, posée pour tout k ≥ 2 avec la constante 1, est plus forte qu'une mesure d'irrationalité. Simons & de Weger : volume 117, pas 115. Les tables « Configurations testées » (`results/RESULTATS_PYTHON.md`) et d(k) pour k = 7 à 15 (`audit/COMPLEMENT_RECHERCHE.md`) sont fausses ; les valeurs justes sont dans `results/VERIFICATION_EXHAUSTIVE.txt`. « Tous les facteurs de d(k) sont de Type I pour k = 3..17 » est faux (k = 8, 12, 14, 16).
>
> *Erratum (October 2026), English summary: this repository does not prove that Collatz cycles do not exist. The claim for k ≥ 18 is not proven (non-surjectivity does not imply N₀ = 0); the "all cycles, under hypotheses" claim is circular (given Bařina's verification, the hypothesis `DerivedLargeKBound` amounts to the conclusion for k > 1322). The cases k ≤ 18 were already known (Simons & de Weger, Acta Arith. 117, 2005). The Lean CI never got past `lakefile.lean`; `native_decide` trusts the compiler, not the kernel. μ = 5.125 is Salikhov's measure for ln 3, not for log₂3.*

> **⚠️ Repository frozen 2026-04-22 (not archived on GitHub) — historical audit, March 2026.**
>
> This meta-repository cross-referenced three Collatz research repos during the audit conducted March 2026. After the April 2026 consolidation, the **active project is [collatz-nocycle-lean4](https://github.com/ericmerle3789/collatz-nocycle-lean4)** (its main theorem is affected by the circularity described in the erratum above). Two of the three originally audited repos (`Collatz-Junction-Theorem`, `collatz-cycles-lean`) carry the same archive banner.
>
> Audit artifacts (`audit/SYNTHESE_MARS2026.md`, `audit/COMPLEMENT_RECHERCHE.md`, `audit/PISTES_CROISEES.md`) remain here unchanged for historical reference. The March 2026 state-of-the-art snapshot is thus preserved as-is.
>
> No further maintenance is planned here. Issues or questions → [active repo issue tracker](https://github.com/ericmerle3789/collatz-nocycle-lean4/issues).
>
> — Eric Merle, 2026-04-22

---

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

Ce travail **visait** à exclure tout cycle, en deux étapes : une vérification exhaustive pour les petites valeurs de k (k = nombre de termes impairs du cycle), puis un argument de comptage pour k ≥ 18. **La seconde étape n'est pas une preuve** (voir l'erratum).

### Calcul de cet audit (mars 2026)
N₀(d(k)) = 0 au plus petit S, pour k = 3 à 18 selon `results/VERIFICATION_EXHAUSTIVE.txt` (la CI Python ne vérifie que k ≤ 14). Ce cas était déjà couvert par la littérature. Le fichier Lean correspondant n'a jamais été compilé.

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

| Ce qu'on cherche | Statut réel | Méthode |
|---|---|---|
| Cycles avec k = 3 à 18 termes impairs | Exclus, déjà connu (Simons & de Weger 2005) | Calcul Python au plus petit S (CI : k ≤ 14) |
| k = 16, 17 en Lean | Non vérifié (CI en échec, `native_decide`) | `lean/CollatzSmallCases.lean` |
| Cycles avec k ≥ 18 | **Non démontré** | La non-surjectivité ne suffit pas |
| Tous les cycles « sous hypothèses » | **Circulaire** (`DerivedLargeKBound`) | Seul acquis : k ≤ 1322 sous `BakerSeparation` (hypothèse de travail) + Bařina |

---

## CI/CD (Vérification automatique)

[![Lean](https://github.com/ericmerle3789/collatz-audit-2026/actions/workflows/lean-check.yml/badge.svg)](https://github.com/ericmerle3789/collatz-audit-2026/actions/workflows/lean-check.yml)
[![Python](https://github.com/ericmerle3789/collatz-audit-2026/actions/workflows/python-scripts.yml/badge.svg)](https://github.com/ericmerle3789/collatz-audit-2026/actions/workflows/python-scripts.yml)

---

## Références principales

- Simons & de Weger (2005) - Acta Arithmetica 117 (2005) 51-70
- Tao (2019) - arXiv:1909.03562
- Barina (2021) - arXiv:2102.01529
- Knight (2026) - Discrete Mathematics 349

---
*Audit réalisé avec l'assistance de Claude Sonnet 4.6 (Anthropic)*
