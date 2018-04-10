"""
idea:
"""
import time

import math
import primesieve


def main():
    max_num = 50000000

    power2 = []
    power3 = []
    power4 = []

    primes = primesieve.primes(math.sqrt(max_num))
    for prime in primes:
        if prime**2 < max_num:
            power2.append(prime**2)
        else:
            break
    for prime in primes:
        if prime**3 < max_num:
            power3.append(prime**3)
        else:
            break
    for prime in primes:
        if prime**4 < max_num:
            power4.append(prime**4)
        else:
            break

    nums = set()
    for p2 in power2:
        for p3 in power3:
            for p4 in power4:
                res = p2 + p3 + p4
                if res < max_num:
                    nums.add(res)

    print('counted:', len(nums))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
