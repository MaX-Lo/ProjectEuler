"""
idea:
"""
import time

import math

import sys


def main():
    sys.setrecursionlimit(1500)

    count = 0
    for depth in range(1, 1000):
        # res = 1 + iterate(depth)
        num, denum = iterate(depth)
        # 1 + last
        num += denum
        if num_of_digits(num) > num_of_digits(denum):
            count += 1
    print(count)


def num_of_digits(num):
    return int(math.floor(math.log10(num))+1)


def iterate(depth):
    if depth == 1:
        # special case (don't see the same formula here)
        return 1, 2
    if depth == 2:
        # 1 / (2 + 1/2) (the last term in brackets)
        return 2, 5
    else:
        # 1 / (2 + last), where last is iterate(depth-1)
        num, denum = iterate(depth - 1)
        # 2 + last
        num += 2*denum
        # 1 / (2 + last)
        num, denum = denum, num
        return num, denum


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)