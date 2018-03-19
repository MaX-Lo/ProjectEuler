"""
idea:
https://www.wikiwand.com/en/Faro_shuffle
"""
import time

import itertools


def main():
    print(2**60)
    # factorisation of 2^60 - 1
    factors = [3, 3, 5, 5, 7, 11, 13, 31, 41, 61, 151, 331, 1321]
    #factors = [3, 5, 17]

    to_test = []
    for i in range(1, len(factors)+1):
        nums = list(itertools.combinations(factors, i))
        for num in nums:
           to_test.append(product(num))

    to_test.sort()
    print(to_test)

    to_test = set(to_test)
    print(len(to_test))

    v2(to_test)


def product(nums):
    p = 1
    for num in nums:
        p *= num
    return p


def v2(to_test):
    count = 0
    for num in to_test:
        c = get_count(num)
        if c == 60:
            count += num + 1
            print(num, count)
    print('some of...:', count)


def get_count(n):
    res = 2
    count = 1
    while res != 1:
        res = res * 2 % n
        count += 1
        if count > 60:
            return 61
    return count


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


def v1():
    count = 0
    for i in range(2, 100000000000, 2):
        c = s(i)
        if c == 8:
            count += i
            print(i, count)
        #print('s({})={}'.format(i, c))
    print('some of...:', count)


def s(n):

    deck = [x for x in range(n)]
    left = deck[:int(n/2)]
    right = deck[int(n/2):]
    deck = shuffle(left, right)

    count = 1
    while not is_sorted(deck):
        left = deck[:int(n / 2)]
        right = deck[int(n / 2):]
        deck = shuffle(left, right)
        count += 1

    return count


def shuffle(left, right):
    deck = []
    for i in range(len(left)):
        deck.append(left[i])
        deck.append(right[i])
    return deck


def is_sorted(deck):
    satisfied = True
    for i in range(len(deck)):
        if not (deck[i] == i):
            satisfied = False
    return satisfied


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
