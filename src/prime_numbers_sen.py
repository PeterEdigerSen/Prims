import math


def prime_numbers_sen(n):
    if n == 1:
        return []
    n_small = int(math.sqrt(n + 0.1))
    prims_small = prime_numbers_sen(n_small)
    prims = prims_small.copy()
    for p in range(n_small + 1, n + 1):
        is_dividable = False
        for m in prims_small:
            if p % m == 0:
                is_dividable = True
                break
        if not is_dividable:
            prims.append(p)
    return prims


def n_of_prime_numbers_sen(n):
    return len(prime_numbers_sen(n))
