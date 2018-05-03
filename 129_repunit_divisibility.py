"""
idea:
"""
import time

import math


def main():
    approach2()
    return
    first = small_nums()
    print('first over million:', first)

    return
    n = 10000
    large_rep = 10**n // 9
    for i in range(1, 100):
        n += 1
        large_rep = large_rep * 10 + 1

        if n % 2 == 0 or n % 5 == 0:
            continue

        res1 = (large_rep // 10) % n
        res3 = (large_rep // 1000) % n
        res9 = (large_rep // 1000000000) % n

        if res1 == 0:
            print('n', n, 'A(n) diff 1', n-1)
        if res3 == 0:
            print('n', n, 'A(n) diff 3', n-3)
        if res9 == 0:
            print('n', n, 'A(n) diff 9', n-9)

def approach2():
    limit = 1000001
    n = limit
    a_n = 0
    while a_n < limit:
        n += 1
        if n % 2 == 0 or n % 5 == 0:
            continue
        a_n = a(n)
    print(n)


def a(n):
    x = 1
    k = 1
    while x != 0:
        x = (x*10 + 1) % n
        k += 1
    return k


def small_nums():
    k_max = 0
    n_max = 0

    for n in range(1000000, 1100000):
        if n % 2 == 0 or n % 5 == 0:
            continue
        k = int(math.floor(math.log10(n))) + 1

        rep = (10 ** k // 9)

        while rep % n != 0:
            rep = rep * 10 + 1
            k += 1
        if k_max < k:
            k_max = k
            n_max = n
            if k_max > 1000000:
                return n_max
        print('n', n, 'A(n)', k, 'diff', n-k)

    return 'not found yet'


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
