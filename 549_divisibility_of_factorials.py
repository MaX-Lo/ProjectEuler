"""
idea:
"""
import time
from sympy.ntheory import factorint
import math
import primesieve


def main():
    limit = 10**8
    primes = primesieve.primes(limit)
    primes_s = set(primes)

    # key: (prime^power), value: s(prime^power)
    cache = dict()
    for prime in primes:
        power = 1
        while prime ** power < limit:
            fac = prime
            k = prime
            while fac % prime**power != 0:
                k += prime
                fac *= k
            cache[(prime, power)] = k
            power += 1
    print('finished building cache')

    # approach with calculating factorization for every single number
    res = 0
    time0 = time.time()
    for i in range(2, limit+1):
        if i % 1000000 == 0:
            print('prog', i, round(time.time() - time0, 2), 'sec')

        if i in primes_s:
            res += i
        else:
            tmp = s(i, primes, cache)
            res += tmp
    print('result', res)


def s(n, primes, cache):
    factors = factorint(n)
    #factors = factorization(n, primes)
    return max([cache[(factor, factors[factor])] for factor in factors])


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
                #print(n)
                n //= prime
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
