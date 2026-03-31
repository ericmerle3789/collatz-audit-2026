#!/usr/bin/env python3
"""
Analyse des facteurs premiers de d(k) = 2^S - 3^k
Type I : 3 est une puissance de 2 modulo p => favorable
Type II: 3 n'est pas une puissance de 2 mod p => obstacle
"""
import math

def compute_S(k):
    return math.ceil(k * math.log2(3))

def compute_d(k):
    S = compute_S(k)
    return (1 << S) - (3 ** k)

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

def is_type_I(p):
    if p <= 3:
        return True
    current = 1
    for _ in range(1, p):
        current = (current * 2) % p
        if current == 3:
            return True
        if current == 1:
            break
    return False

def multiplicative_order(a, n):
    if math.gcd(a, n) != 1:
        return None
    order = 1
    current = a % n
    while current != 1:
        current = (current * a) % n
        order += 1
    return order

def main():
    print("=" * 70)
    print("ANALYSE: Type I/II des facteurs premiers de d(k)")
    print("Type I : 3 est une puissance de 2 modulo p (favorable)")
    print("Type II: 3 N'est PAS une puissance de 2 mod p (obstacle)")
    print("=" * 70)
    for k in range(3, 26):
        S = compute_S(k)
        d = compute_d(k)
        factors = factorize(d)
        primes = sorted(factors.keys())
        info = []
        has_type_II = False
        for p in primes:
            t = "I " if is_type_I(p) else "II"
            if not is_type_I(p):
                has_type_II = True
            ord2 = multiplicative_order(2, p) if p > 2 else 1
            info.append("p={}(T{},ord2={})".format(p, t, ord2))
        marker = " <-- TYPE II!" if has_type_II else ""
        print("k={:2d}: S={:2d}, d={:>15,}".format(k, S, d))
        print("       {}{}".format(' | '.join(info), marker))
        print()
    print("Si tous les facteurs sont Type I => N_0 = 0 est attendu")

if __name__ == "__main__":
    main()
