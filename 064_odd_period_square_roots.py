"""
idea:
"""
import time

import math


def main():
    num_with_odd_periods = 0
    for i in range(2, 10001):
        if math.sqrt(i) % 1 == 0:
            continue
        count = continued_fraction(i)
        if count % 2 == 1:
            num_with_odd_periods += 1
        print('rep len for {}: {}'.format(i, count))

    print('count of nums with odd periods:', num_with_odd_periods)


def continued_fraction(num):
    """
    square root of any natural number that is not a perfect square
    e.g. 3, 5, 6, 7... but not 4, or 9
    """
    s = num
    sqrtS = math.sqrt(num)
    a0 = math.floor(sqrtS)

    m = 0
    d = 1
    a = a0
    count = 0
    while True:
        m = d * a - m
        d = (s - m**2) / d
        a = math.floor((a0 + m) / d)

        count += 1

        if a == 2*a0:
            break
    return count


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
