"""
idea:
"""
import time

import primesieve


def main():
    limit = 10**8
    primes = primesieve.primes(limit//2)

    count = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i]*primes[j] >= limit:
                break
            count += 1
    print('counted:', count)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
