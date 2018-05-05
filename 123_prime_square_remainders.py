"""
idea:
"""
import time

import primesieve


def main():
    primes = primesieve.primes(1000000)

    max_remainder = 0
    max_n = 0

    n = 21033
    remainder = f(n + 1, primes[n])
    print('n', n + 1, 'prime', primes[n], 'num', remainder)


    for n in range(21000, len(primes)):
        remainder = f(n + 1, primes[n])
        if remainder > max_remainder:
            max_n = n + 1
            max_remainder = remainder
            print('n', n + 1, 'prime', primes[n], 'num', max_remainder)


def f(n, pn):
    return ((pn - 1)**n + (pn + 1)**n) % (pn**2)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
