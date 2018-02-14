"""
idea:

idee: primfaktoren
"""
import time

import primesieve


def main():
    distinct_factors = 4

    primes = primesieve.primes(1000000)

    consecutive = 0
    current_num = 2
    while consecutive != distinct_factors:
        if current_num % 10000 == 0:
            print("progress:", current_num)

        factors = factorization(current_num, primes)
        if len(factors.keys()) == distinct_factors:
            consecutive += 1
        else:
            consecutive = 0
        current_num += 1

    print("wanted num", current_num-consecutive)


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