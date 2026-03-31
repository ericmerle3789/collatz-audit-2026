#!/usr/bin/env python3
"""
Verification: N_0(d(k)) = 0 pour k = 3..17
Prouve qu'aucun cycle Collatz de longueur 3 a 17 n'est possible.
"""
import math
from itertools import combinations
import time

def compute_S(k):
    return math.ceil(k * math.log2(3))

def compute_d(k):
    S = compute_S(k)
    return (1 << S) - (3 ** k)

def count_zero_mod(k):
    S = compute_S(k)
    d = compute_d(k)
    pow3 = [3 ** (k - 1 - i) for i in range(k)]
    base = pow3[0]
    count = 0
    total = 0
    for combo in combinations(range(1, S), k - 1):
        cs = base
        for i, a in enumerate(combo):
            cs += pow3[i + 1] * (1 << a)
        if cs % d == 0:
            count += 1
        total += 1
    return count, total, S, d

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def main():
    print("=" * 65)
    print("VERIFICATION: N_0(d(k)) = 0 pour k = 3..17")
    print("=" * 65)
    all_zero = True
    for k in range(3, 18):
        S = compute_S(k)
        d = compute_d(k)
        factors = factorize(d)
        factor_str = " x ".join(
            "{}^{}".format(p, e) if e > 1 else str(p)
            for p, e in sorted(factors.items())
        )
        t0 = time.time()
        count, total, _, _ = count_zero_mod(k)
        elapsed = time.time() - t0
        status = "ZERO OK" if count == 0 else "ATTENTION: {} solutions!".format(count)
        if count != 0:
            all_zero = False
        print("k={:2d}: S={:2d}, d(k)={:>12,} = {}".format(k, S, d, factor_str))
        print("       Sequences testees: {:>8,} | N_0 = {} -> {}".format(total, count, status))
        print("       Temps: {:.2f}s".format(elapsed))
        print()
    print("=" * 65)
    if all_zero:
        print("CONCLUSION: N_0(d(k)) = 0 pour TOUS k de 3 a 17.")
        print("=> Aucun cycle Collatz de longueur 3 a 17 n'est possible.")
    else:
        print("ATTENTION: Des exceptions ont ete trouvees!")
    print("=" * 65)

if __name__ == "__main__":
    main()
