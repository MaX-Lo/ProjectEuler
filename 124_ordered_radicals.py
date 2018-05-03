"""
idea:
"""
import operator
import time

import itertools
from functools import reduce

import primesieve


def main():
    limit = 100001

    primes = primesieve.primes(limit)
    rads = dict()
    for i in range(1, limit):
        if i % 10000 == 0:
            print(i)
        factors = list(factorization(i, primes).keys())
        rad = reduce(operator.mul, factors, 1)
        rads[i] = rad

    sorted_rads = sorted(rads.items(), key=operator.itemgetter(1))

    print(sorted_rads[10000-1])


def factorization(n, primes):
    """
    :param n: number to factorize
    :param primes: list with primes
    :return: dictionary with primes that occur (and count of them)
    """
    factors = {}

    while n != 1:
        for prime in primes:
            if n % prime == 0:
                n /= prime
                if prime in factors:
                    factors[prime] += 1
                else:
                    factors[prime] = 1
                break
    return factors


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
