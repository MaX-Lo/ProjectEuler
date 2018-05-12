"""
idea:
160626866400
6469693230
"""
import time

import primesieve


def main():
    #advantageous_primes_approach()
    consecutive_primes_approach()


def consecutive_primes_approach():
    max_prime = 1000
    wanted_ratio = 15499 / 94744
    # wanted_ratio = 4 / 10
    primes = primesieve.primes(max_prime)
    prime_factors = {2: 1}
    next_prime_index = 1
    next_prime = 3
    ratio = 1 / (2 - 1)
    phi = 1
    d = 2
    last_d, last_phi = d, phi
    while ratio > wanted_ratio:
        last_d, last_phi = d, phi
        d *= next_prime
        phi *= (next_prime - 1)
        prime_factors[next_prime] = 1
        next_prime_index += 1
        next_prime = primes[next_prime_index]
        ratio = phi / (d-1)
        print('d', d, 'phi', phi, 'ratio', ratio, 'wanted ratio', wanted_ratio)

    # remove last prime which was to much
    prime_factors.pop(primes[next_prime_index-1])

    composite_nums = [[2, 2], [2, 3], [2, 2, 2], [3, 3], [2, 5], [2, 2, 3], [2, 7], [3, 5], [2, 2, 2, 2],
                      [2, 3, 3], [3, 7], [2, 2, 7]]

    multiple = 2
    tmp_d = last_d
    tmp_phi = last_phi
    while tmp_d < d:
        tmp_d = multiple * last_d
        tmp_phi = last_phi
        factors = factorization(multiple, primes)
        for factor in factors:
            tmp_phi = tmp_phi * factor**factors[factor]

        ratio = tmp_phi / (tmp_d - 1)
        if ratio < wanted_ratio:
            break
        multiple += 1

    print('d', d)
    print(prime_factors)

    print('d small', tmp_d, 'multiple', multiple)


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


def advantageous_primes_approach():
    max_prime = 1000
    wanted_ratio = 15499 / 94744
    #wanted_ratio = 4 / 10

    primes = primesieve.primes(max_prime)

    prime_factors = {2: 1}
    next_prime_index = 1
    next_prime = 3
    ratio = 1 / (2 - 1)
    phi = 1
    d = 2
    while ratio > wanted_ratio:
        # test increasing already occurring factors
        increased_existing_factor = False
        for prime in prime_factors:
            if prime**prime_factors[prime]*(prime-1) < next_prime - 1:
                prime_factors[prime] += 1
                d *= prime
                phi *= prime
                increased_existing_factor = True
                break

        if not increased_existing_factor:
            # adding a new factor is better than increasing already occurring, so do it
            prime_factors[next_prime] = 1
            d *= next_prime
            next_prime_index += 1
            # precalculated primes weren't enough
            if len(primes) == next_prime_index:
                print('not enough primes')
                break
            phi *= (next_prime - 1)
            next_prime = primes[next_prime_index]

        ratio = phi / (d-1)
        print('d', d, 'phi', phi, 'ratio', ratio, 'wanted ratio', wanted_ratio)
        print(prime_factors)

    print('d', d)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
