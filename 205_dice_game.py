"""
idea:
"""
import time

import math


def main():

    pyramid_chances = []
    cubic_chances = []
    p_count = 0
    c_count = 0

    for i in range(6, 9*4 + 1):
        p = possibilities(9, 4, i)
        p_count += p
        c = possibilities(6, 6, i)
        c_count += c
        pyramid_chances.append(p)
        cubic_chances.append(c)

    print(len(pyramid_chances), len(cubic_chances))
    print(pyramid_chances)
    print(cubic_chances)

    chances = 0
    for c in range(0, 31):
        count = 0
        for p in range(c + 1, 31):
            count += pyramid_chances[p]
        # add chance of having c with cubes and something better with pyramids
        chances += (cubic_chances[c] / c_count) * (count / p_count)
    print(chances)


def possibilities(dices, sides, total):
    """ return number of possibilities to roll with 'dices' dices with
    'sides' sides each a total of 'total' """

    count = 0

    limit = int(math.floor((total - dices) / sides))
    for k in range(limit + 1):
        count += (-1)**k * ncr(dices, k) * ncr(total - 1 - sides * k, dices - 1)
    return int(count)


def ncr(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
