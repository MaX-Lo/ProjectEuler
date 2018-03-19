"""
idea:
"""
import time

import math


def main():
    v1()


def v1():
    squares = set(x**2 for x in range(1000000))
    print('max sqr', max(squares))
    t0 = time.time()

    x, y, z = 1, 1, 1
    count = 0
    prog = 0
    while True:
        if x > y:
            x = 1
            y += 1
        if y > z:
            y = 1
            z += 1

        if is_shortest_int(x, y, z, squares):
            count += 1

        if count > 1000000:
            break

        x += 1
        prog += 1
        if prog % 1000000 == 0:
            print('progress:', prog, 'count:', count, 'time:', time.time() - t0)

    print(x, y, z)
    print('counted:', count)
    print('wanted M:', max(x, y, z))


def is_shortest_int(x, y, z, squares):
    l1 = x**2 + (y+z)**2
    l2 = y**2 + (x+z)**2
    l3 = z**2 + (x+y)**2
    lmin = min(l1, l2, l3)
    return lmin in squares


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
