"""
idea:
"""
import time

import math


def main():
    t0 = time.time()
    max_num = 3/7

    closest = (0, 1)
    closest_fraction = 0/1

    for denominator in range(3, 1000000):
        if denominator % 10000 == 0:
            print('{}%, {}sec'.format(denominator/10000, round(time.time()-t0), 3))

        start = int(math.floor(denominator * 3/7)) - 1

        numerator = start
        while (numerator+1) / denominator < max_num:
            numerator +=1

        if is_reduced(numerator, denominator) and numerator / denominator > closest_fraction:
            closest_fraction = numerator / denominator
            closest = numerator, denominator
            #print(closest_fraction, closest)

    print('real num:  ', max_num)
    print('best match:', closest_fraction)
    print('final best matching:', closest)


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