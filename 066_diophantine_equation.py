"""
idea:
http://www.numbertheory.org/php/patzpos.html
or better:
https://www.wikiwand.com/en/Pell's_equation#/Fundamental_solution_via_continued_fractions

x^2 - D * y^2 = 1
"""
import time

import math


def main():

    max_x = 0
    d_with_max_x = 0

    for d in range(2, 1000):
        # continue if d is square
        if math.sqrt(d) % 1 == 0:
            continue

        i = 1
        found = False
        while not found:
            fraction_list = continued_fraction(d, i)
            x, y = eval_continued_fraction(fraction_list)
            if x**2 == 1 + d * y**2:
                print('found d {}, x {}, y {}'.format(d, x, y))
                if max_x < x:
                    max_x = x
                    d_with_max_x = d
                found = True
            i += 1

    print('d with max x:', d_with_max_x)


def eval_continued_fraction(continued_frac):
    """
    evaluate a continued fraction
    expect a list as: [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8] (e.g. for e)
    """

    numerator = 1
    denominator = continued_frac[-1]
    continued_frac.pop(-1)

    for num in reversed(continued_frac):
        numerator += num * denominator
        numerator, denominator = denominator, numerator

    # last exchange was unnecessary therefore reverse it back again
    numerator, denominator = denominator, numerator
    return numerator, denominator


def continued_fraction(num, precision):
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
    count = 1
    fraction = [a0]
    while True:
        if count >= precision:
            break
        m = d * a - m
        d = (s - m**2) / d
        a = math.floor((a0 + m) / d)
        fraction.append(a)
        count += 1
    return fraction


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
