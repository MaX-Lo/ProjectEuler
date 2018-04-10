"""
idea:
"""
import time

import primesieve


def main():
    limit = 1000000
    primes = primesieve.primes(limit+1)

    smallest = 0
    largest_chain = 0

    divisors_dict = dict()
    for i in range(1, limit+1):
        divisors_dict[i] = sum(get_divisors(i, primes))
        if i % 10000 == 0:
            print('progress 1. loop:', int(i/10000), '%')

    for i in range(1, limit + 1):
        length = chain_length(i, divisors_dict, limit)
        if length > largest_chain:
            largest_chain = length
            smallest = i
        if i % 10000 == 0:
            print('progress 2. loop:', int(i/10000), '%')

    print('longest chain: {} by: {}'.format(largest_chain, smallest))
    print_chain(smallest, primes, limit)


def print_chain(num, primes, limit):
    chain = []
    curr = num
    while curr not in chain:
        chain.append(curr)
        if curr > limit:
            return 0
        curr = sum(get_divisors(curr, primes))

    print('--- corresponding chain and min num ---')
    print(chain)
    print(min(chain))


def chain_length(num: int, div_dict: dict, limit):
    chain = set()
    curr = num
    while curr not in chain:
        chain.add(curr)
        if curr > limit or curr == 0:
            return 0

        curr = int(div_dict[curr])
        if curr == num:
            return len(chain)
    return 0


# get a list of all factors for N
# ex: get_factors(10) -> [1,2,5,10]
def get_divisors(n, primelist):
    num = n
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

    if num in factors:
        factors.remove(num)

    return factors


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
