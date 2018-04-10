"""
idea:
"""
import time

import primesieve


def main():
    wanted_ratio = 15499 / 94744
    #wanted_ratio = 4 / 10

    limit = 1000000
    primes = primesieve.primes(limit)

    for i in range(2, limit):
        if i % 10000 == 0:
            print('progress:', i)

        ratio = get_ratio(i, primes)
        print(ratio)
        if ratio < wanted_ratio:
            print('found: ', i)
            break


def get_ratio(num, primes):
    factors = factorization(num, primes)
    phi = get_phi(factors)
    resilience = phi
    ratio = resilience / (num - 1)
    return ratio


def get_phi(factors):
    phi = 1
    for factor in factors:
        phi *= factor**(factors[factor]-1) * (factor-1)
    return phi


def factorization(n, primes):
    """
    :param n: number to factorize
    :param primes: list with primes
    :return: dictionary with primes that occur (and count of them)
    """
    factors = {}

    # in case n itself is a prime
    if n in primes:
        factors[n] = 1
        return factors

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
