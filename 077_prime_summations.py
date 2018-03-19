"""
idea:
"""
import time

import primesieve


def main():
    v2()


def v2():
    primes = primesieve.primes(1000)
    print()
    i = 2
    while count2(i, 0, 0, primes) <= 5000:
        i +=1
    print('count:', count2(i, 0, 0, primes))
    print('i:', i)


def count2(num, subtotal, curr_prime_ind, primes):
    possibilities = 0
    for i in range(curr_prime_ind, len(primes)):
        res = subtotal + primes[i]
        if res < num:
            possibilities += count2(num, res, i, primes)
        elif res == num:
            possibilities += 1
        elif res > num:
            return possibilities
    return possibilities


def count_possibilities(num):
    possibilities = 0

    nums = [2 for _ in range(int(num/2))]
    res = sum(nums)
    primes = get_prime_dict(num)

    curr = 3
    added = 0
    while True:
        while res + curr > num:
            res -= curr
            nums.pop(-1)
        res += curr
        nums.append(curr)
        added += 1
        curr = primes[curr]


def get_prime_dict(limit):
    """
    return dictionary with prime as key and next prime as value
    e.g {2: 3, 3: 5, 5: 7, 7: 11, ...}
    """
    it = primesieve.Iterator()
    prime = it.next_prime()

    primes = dict()
    while prime < limit:
        nxt_prime = it.next_prime()
        primes[prime] = nxt_prime
        prime = nxt_prime
    return primes


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
