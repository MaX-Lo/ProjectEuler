"""
idea:
"""
import time

import math


def main():
    t0 = time.time()

    count = 0

    for denominator in range(2, 12001):
        if denominator % 100 == 0:
            print('{}%, {}sec'.format(denominator/100, round(time.time()-t0), 3))

        start = int(math.floor(denominator * 1/3)) - 1

        numerator = start
        while numerator / denominator < 0.5:
            if numerator / denominator > 1/3 and is_reduced(numerator, denominator):
                count += 1
            numerator += 1

    print('fractions between:', count)


def is_reduced(numerator, denominator):
    return computeHCF(numerator, denominator) == 1


def computeHCF(x, y):
    # This function implements the Euclidian algorithm to find H.C.F. of two numbers
    while y:
        x, y = y, x % y

    return x

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)