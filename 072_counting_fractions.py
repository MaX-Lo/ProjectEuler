"""
idea:
"""
import time

import primesieve


def main():
    primes = primesieve.primes(1000000)
    t0 = time.time()

    count = 0
    for i in range(2, 1000001):
        if i % 1000 == 0:
            print('{}%, {}sec'.format(i / 10000, round(time.time() - t0), 5))
        count += get_phi(factorization(i, primes))

    print('result:', count)


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