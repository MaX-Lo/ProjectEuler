"""
Task:


"""
import time

import math


def main():
    start_time = time.time()

    limit = 20

    primes = all_primes(limit)

    ls = []
    phi = {1: 1}
    print("time:", time.time() - start_time)

    for i in range(1, limit):
        if i in primes:
            phi[i] = i - 1
        else:
            a, b = get_2factors(i)
            phi[i] = phi[a] * phi[b]
        print(i, phi[i])

    print("time:", time.time() - start_time)


def get_2factors(n):
    if n % 2 == 0:
        return int(n/2), 2

    a = math.ceil(math.sqrt(n))
    b = a**2 - n
    while not math.sqrt(b).is_integer():
        b += 2*a + 1
        a += 1

    y = math.sqrt(b)
    a = a + y

    return int(a), int(n / a)

def is_square():
    pass


# get a list of all factors for N
# ex: get_factors(10) -> [1,2,5,10]
def get_factors(n, primelist):
    fcount = {}
    for p in primelist:
        if p > n:
            break
        if n % p == 0:
            fcount[p] = 0

        while n % p == 0:
            n /= p
            fcount[p] += 1

    factors = [1]
    for i in fcount:
        level = []
        exp = [i**(x+1) for x in range(fcount[i])]
        for j in exp:
            level.extend([j*x for x in factors])
        factors.extend(level)

    return factors


def all_primes(limit):
    # list containing for every number whether it has been marked already
    numbers = {}
    for x in range(3, limit, 2):
        numbers[x] = False

    primes = [2, 3]

    p = 3
    while p < limit:
        for i in range(p, limit, p):
            numbers[i] = True

        for i in range(p, limit, 2):
            if not numbers[i]:
                p = i
                numbers[i] = True
                primes.append(i)
                break
            else:
                p += 1
    return primes


if __name__ == '__main__':
    main()
