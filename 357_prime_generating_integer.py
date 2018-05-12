"""
idea:
"""
import math

import primesieve
import time


def main():

    primes = primesieve.primes(10 ** 8)
    primes_set = set(primes)
    print('all p-1 len', len(primes))

    nums_to_test = []
    for prime in primes:
        n = prime - 1
        # every n is even because n is a prime - 1 and has therefore 2 as divisor
        if 2 + (n // 2) in primes_set:
            # if n's digit sum is divisible by 3 than is 3 a divisor of n
            could_be = True
            if digit_sum(n) % 3 == 0:
                if not (3 + (n // 3) in primes_set):
                    could_be = False
            if n % 10 == 0 or n % 10 == 5:
                if not (5 + (n // 5) in primes_set):
                    could_be = False
            if could_be:
                nums_to_test.append(n)

    print('new len', len(nums_to_test))

    found = []
    for n in nums_to_test:
        if is_prime_generating(n, primes_set):
            found.append(n)
            print(n)
    print('counted', len(found), 'sum', sum(found))
    print(found)


def is_prime_generating(n, prime_set):
    return all((n % d != 0 or (d + n // d) in prime_set) for d in range(2, int(math.sqrt(n)) + 1))


def digit_sum(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def factorization(n, primelist):
    fcount = {}
    for p in primelist:
        if p > n:
            break
        if n % p == 0:
            fcount[p] = 0

        while n % p == 0:
            n /= p
            fcount[p] += 1
    return fcount


# get a list of all factors for N
# ex: get_factors(10) -> [1,2,5,10]
def get_divisors(n, fcount):
    num = n
    factors = [1]
    for i in fcount:
        level = []
        exp = [i**(x+1) for x in range(fcount[i])]
        for j in exp:
            print('it', [j*x for x in factors])
            level.extend([j*x for x in factors])
        factors.extend(level)

    if num in factors:
        factors.remove(num)

    return factors



if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
