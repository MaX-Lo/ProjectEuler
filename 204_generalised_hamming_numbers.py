"""
idea:
"""
import time

import primesieve


def main():
    limit = 10**9
    hamming_type = 100
    primes = primesieve.primes(hamming_type)

    c = 1 +  count(1, limit, 0, primes, len(primes))
    print('counted:', c)


def count(n, limit, ind,  primes, prime_count):
    """
    :param n: current product
    :param limit: max product
    :param ind: curr index in primes
    :param primes: list of primes
    :param prime_count: len of prime list
    """
    c = 0
    for i in range(ind, prime_count):
        n_tmp = n * primes[i]
        if n_tmp > limit:
            return c
        c += 1
        #print(n_tmp)
        c += count(n_tmp, limit, i, primes, prime_count)
    return c


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)

