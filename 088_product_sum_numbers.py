"""
idea:
"""
import time

import itertools
import primesieve


def main():
    max_num = 15000
    primes = primesieve.primes(max_num)
    primefactors = {}
    for num in range(2, max_num):
        primefactors[num] = factorization(num, primes)

    min_prod_nums = set()

    for k in range(2, 12001):
        num = k
        found = False
        while not found:
            primes = primefactors[num].keys()
            count = primefactors[num].values()
            for factors in multiplicative_partitions(primes, count):
                sum_of_needed_ones = k - len(factors)
                res = sum(factors) + sum_of_needed_ones
                if res == num:
                    print('k: {} found: {}'.format(k, num))
                    min_prod_nums.add(num)
                    found = True
                    break
            num += 1

    print('wanted num:', sum(min_prod_nums))


def test_num(num: int, k: int, divisors: dict):
    pass

def exponent_partitions(exponents, min_exponents):
    """Generate all vector partitions of 'exponents', each of whose
    entries is lexicographically at least 'min_exponents'."""
    if all(exponent == 0 for exponent in exponents):
        yield []
    else:
        for vector in itertools.product(*(range(v+1) for v in exponents)):
            if vector >= min_exponents:
                remainder = tuple(x - y for x, y in zip(exponents, vector))
                for partition in exponent_partitions(remainder, vector):
                    yield partition + [vector]


def divisor_from_exponents(primes, exponent_vector):
    """Reconstruct divisor from the list of exponents."""
    divisor = 1
    for p, e in zip(primes, exponent_vector):
        divisor *= p**e
    return divisor


def multiplicative_partitions(primes, exponents):
    """Generate all multiplication partitions of
    product(p**e for p, e in zip(primes, exponents))"""
    if len(exponents) == 0:
        # Corner case for partitions of 1.
        yield []
    else:
        initial_vector = (0,) * (len(exponents) - 1) + (1,)
        for partition in exponent_partitions(exponents, initial_vector):
            yield [divisor_from_exponents(primes, vector) for vector in partition]


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