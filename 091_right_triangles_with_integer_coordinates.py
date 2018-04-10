"""
idea:
"""
import time

import math


def main():
    limit = 50

    count = 0
    # bottom horizontal and right vertical
    for y1 in range(1, limit + 1):
        print('progress:', y1)
        for x1 in range(0, limit + 1):
            for y2 in range(0, limit + 1):
                for x2 in range(1, limit + 1):
                    # f(x)=m*x+n second point has to be under this line
                    m = -1
                    if x1 != 0:
                        m = y1/x1
                    f = m * x2
                    if y2 >= y1 and x2 <= x1 or f == y2:
                        continue
                    #print(x1, y1, x2, y2, is_right_triangle(x1, y1, x2, y2))
                    if is_right_triangle(x1, y1, x2, y2):
                        count += 1

    print('counted:', count)


def is_right_triangle(x1, y1, x2, y2, x3=0, y3=0):
    a = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    b = math.sqrt(abs(x1-x3)**2 + abs(y1-y3)**2)
    c = math.sqrt(abs(x3-x2)**2 + abs(y3-y2)**2)

    if a > b and a > c:
        hypo = a
        k1 = b
        k2 = c
    elif b > a and b > c:
        hypo = b
        k1 = a
        k2 = c
    else:
        hypo = c
        k1 = a
        k2 = b

    #print(k1**2, '+', k2**2, ' = ', hypo**2)
    if abs(k1**2 + k2**2 - hypo**2) < 0.000000001:
        return True
    else:
        return False


def not_fully_working():
    limit = 5

    count = 0
    # bottom horizontal and right vertical
    for y1 in range(1, limit + 1):
        for x1 in range(y1, limit + 1):
            for y2 in range(0, y1):
                count += 1
    # times 2 because left vertical top horizontal is the same
    print('bottom horizontal and right vertical:', count)
    print('left vertical top horizontal:', count)
    count *= 2

    # bottom horizontal and left vertical
    t = limit ** 2
    count += t
    print('bottom horizontal and left vertical:', t)

    # bottom horizontal, top right angel and left vertical right right angle
    t = limit - 1
    count += t * 2
    print(' bottom horizontal, top right angel and left vertical right right angle: ', t)

    print('counted all together:', count)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
