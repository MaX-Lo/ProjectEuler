"""
idea:
"""
import time

import primesieve


def main():
    limit = 10**7

    divisors = {x: 0 for x in range(1, limit)}
    prog = 1
    for i in range(1, limit):
        if i % prog == 0:
            print(i / limit * 100, '%')
            if i > 10:
                prog = 100
                if i > 1000:
                    prog = 1000
                    if i > 10000:
                        prog = 100000
        for j in range(i, limit, i):
            divisors[j] += 1

    found = set()
    count = 0
    for x in range(1, limit-1):
        #print(x+1, divisors[x+1])
        if divisors[x] == divisors[x+1]:
            found.add(x)
            found.add(x+1)
            count += 1

    print('counted', count)
    print('found', len(found))


def approach1():
    limit = 10 ** 7
    primes = set(primesieve.primes(limit))

    found = set()
    n = 1
    np1 = 1
    for i in range(3, limit):
        if i % 10000 == 0:
            print(i / limit * 100, '%, found', len(found))
        n, np1 = np1, count_divisors(factorization(i, primes))
        if n == np1:
            found.add(i)
            found.add(i - 1)
    print('found', len(found))


def count_divisors(factors):
    divisors = 1
    for factor in factors:
        occurrences_of_factor = factors[factor]
        divisors *= (occurrences_of_factor + 1)
    return divisors


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
