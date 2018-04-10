"""
idea:
"""
import time

import math


def main():
    # n = 10000 t: 2.325
    # n = 10000 t: 1.189
    # n = 10000 t: 0.131
    # n = 10000 t: 0.1

    f1 = 1
    f2 = 2
    count = 3
    t0 = time.time()

    while True:
        if count % 5000 == 0:
            print('n =', count, 't:', round(time.time() - t0, 3))

        f1, f2 = f2, f1+f2
        count += 1

        length = int(math.floor(math.log10(f2)))+1
        if count == 541:
            print(f2 % 1000000000, is_pandigital(str(f2 % 1000000000)))
        if length >= 9 and is_pandigital(str(f2 % 1000000000)):
            first_9 = f2 // 10 ** (length - 9)
            if is_pandigital(str(first_9)):
                print(count, f2)
                break


def is_pandigital(num):
    return set(num) == set('123456789')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)