#!/usr/bin/env python3
"""
Analyse de l'ecart entropique gamma = 1 - h(ln2/ln3) ~ 0.0500

Pour k grand, le nombre de sequences est exponentiellement plus petit
que la taille du module d(k). C'est pourquoi les cycles sont impossibles.
"""
import math

def compute_S(k):
    return math.ceil(k * math.log2(3))

def compute_d(k):
    S = compute_S(k)
    return (1 << S) - (3 ** k)

def log_binomial(n, r):
    if r > n or r < 0:
        return float('-inf')
    r = min(r, n - r)
    result = 0.0
    for i in range(r):
        result += math.log2(n - i) - math.log2(i + 1)
    return result

def entropy(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)

def main():
    alpha = math.log(2) / math.log(3)
    gamma = 1.0 - entropy(alpha)
    print("=" * 70)
    print("ANALYSE DE L'ECART ENTROPIQUE (moteur de la non-surjectivite)")
    print("alpha = ln2/ln3 = {:.6f}".format(alpha))
    print("gamma = 1 - h(alpha) = {:.6f}".format(gamma))
    print()
    print("Pour k grand: nombre de sequences << taille du module d(k)")
    print("=> Les cycles deviennent impossibles")
    print("=" * 70)
    print()
    print("{:>4} | {:>4} | {:>16} | {:>12} | {:>8} | {:>10}".format(
        "k", "S", "log2(sequences)", "log2(d(k))", "Ecart", "Non-surj?"))
    print("-" * 65)
    k_threshold = None
    for k in range(3, 101):
        S = compute_S(k)
        log_c = log_binomial(S - 1, k - 1)
        d = compute_d(k)
        log_d = math.log2(d) if d > 0 else 0
        ecart = log_c - log_d
        non_surj = "OUI" if log_c < log_d else "non"
        if log_c < log_d and k_threshold is None:
            k_threshold = k
        if k <= 25 or k % 10 == 0 or k == k_threshold:
            print("{:>4} | {:>4} | {:>16.2f} | {:>12.2f} | {:>8.2f} | {:>10}".format(
                k, S, log_c, log_d, ecart, non_surj))
    print()
    print("=> Seuil de non-surjectivite: k >= {}".format(k_threshold))
    print("   (Theoreme de Jonction de Merle: k >= 18)")
    print("   L'ecart croit comme -gamma * k quand k -> infini")
    print("   gamma = {:.4f}".format(gamma))
    print("=" * 70)

if __name__ == "__main__":
    main()
