"""
idea:
counted 456 sum 18407904
time: 10939.591751337051
"""
import time

import math
from functools import reduce

import primesieve


def main():
    semi_naive()


def semi_naive():
    limit = 120000
    prime_factor_table = precalculate_prime_factors(limit)

    found = []

    for c in range(3, limit):
        a = 0
        b = c
        while a < c // 2:
            a += 1
            if math.gcd(a, c) != 1:
                continue
            b = c - a
            if math.gcd(b, a) == 1:
                factors = prime_factor_table[c].union(prime_factor_table[a]).union(prime_factor_table[b])
                rad = reduce(lambda x, y: x*y, factors, 1)
                if rad < c:
                    print('c:', c)
                    found.append(c)

    print('counted', len(found), 'sum', sum(found))
    #print(found)


def precalculate_prime_factors(limit):
    """ get a dictionary containing for every integer n < limit a set containing its distinct prime factors """
    lookup_table = dict()
    primes = primesieve.primes(limit)
    for i in range(1, limit):
        n = i
        factors = set()
        for prime in primes:
            if prime > i:
                break
            if i % prime == 0:
                i //= prime
                factors.add(prime)
        lookup_table[n] = factors
    return lookup_table


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
