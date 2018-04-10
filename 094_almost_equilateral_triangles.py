"""
idea:
"""
import time

import math


def main():
    max_perimeter = 1000000000
    perimeter_sum = 16 + 50 + 196 + 722

    a1 = 5
    a2 = 65
    perimeter = 0
    while perimeter < max_perimeter:
        a_tmp = 14*a2-a1-4
        a1 = a2
        a2 = a_tmp
        perimeter = 3 * a_tmp + 1
        if perimeter < max_perimeter:
            perimeter_sum += perimeter

    a1 = 17
    a2 = 241
    perimeter = 0
    while perimeter < max_perimeter:
        a_tmp = 14 * a2 - a1 + 4
        a1 = a2
        a2 = a_tmp
        perimeter = 3 * a_tmp - 1
        if perimeter < max_perimeter:
            perimeter_sum += perimeter

    print('sum:', perimeter_sum)


def old2():
    max_perimeter = 1000000000
    max_side_length = max_perimeter // 3 + 1
    print(max_side_length)

    perimeter_sum = 0
    for b in range(3, max_side_length):
        if b % 100000 == 0:
            print('progress:', round(((b-1)*2 + b) / 1000000, 2), 'Mio, sum:', perimeter_sum)

        small_height_sqr = get_height(b-1, b)
        small_height = math.sqrt(small_height_sqr)
        if small_height % 1 == 0 and small_height**2 == small_height_sqr:
            if b % 2 == small_height % 2:
                print('found:', b, b-1, b-1)
                perimeter_sum += b + 2 * (b-1)

        big_height_sqr = get_height(b + 1, b)
        big_height = math.sqrt(big_height_sqr)
        if big_height % 1 == 0 and big_height**2 == big_height_sqr:
            if b % 2 == big_height % 2:
                print('found:', b, b + 1, b + 1)
                perimeter_sum += b + 2 * (b+1)

    # small_height_sqr = get_height(max_side_length - 1, max_side_length)
    # small_height = math.sqrt(small_height_sqr)
    # if small_height % 1 == 0:
    #     if max_side_length % 2 == small_height % 2:
    #         print('found:', max_side_length, max_side_length - 1, max_side_length - 1)
    #         perimeter_sum += max_side_length + 2 * (max_side_length - 1)

    print('sum:', perimeter_sum)


def get_height(a, b):
    return 4 * a**2 - b**2


def old():
    max_perimeter = 110  # 1000000000
    max_side_length = max_perimeter // 3 + 1

    perimeter_sum = 0
    for i in range(2, max_side_length):
        if i % 100000 == 0:
            print('progress:', i/1000000, 'Mio, sum:', perimeter_sum)
        if is_high_p_int(i):
            perimeter_sum += i + 2*(i+1)
            print(i, i+1)
        if is_low_p_int(i):
            print(i, i-1)
            perimeter_sum += i + 2*(i-1)
        #print(i, is_high_p_int(i), is_low_p_int(i))

    if is_low_p_int(max_side_length):
        perimeter_sum += max_side_length + 2 * (max_side_length - 1)

    print('wanted sum:', perimeter_sum)

def is_high_p_int(b):
    hsqr = (b+1)**2 - (b**2 / 4)
    h = math.sqrt(hsqr)
    print(b, hsqr, h)
    if hsqr % 2 == 1:
        return False
    elif h % 1 == 0:
        return True
    else:
        return False


def is_low_p_int(b):
    hsqr = (b-1)**2 - (b**2 / 4)
    h = math.sqrt(hsqr)

    if hsqr % 2 == 1:
        return False
    elif abs(h % 1) == 0:
        return True
    else:
        return False


def get_areas(a):
    ap = ((a+1)/2)**2 * (a**2 - (a+1)**2/4)
    am = ((a-1)/2)**2 * (a**2 - (a-1)**2/4)
    return ap, am


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)