"""
idea:
"""
import time

import math


def main():
    version2()


def version2():
    limit = 1500001

    found_lengths = set()
    multiples = set()

    for m in range(2, int(math.sqrt(limit))):
        for n in range(1, m):

            if (m + n) % 2 != 1 or gcd(m, n) != 1:
                continue

            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2

            perimeter = a + b + c
            if perimeter > limit:
                break
            tmp_perimeter = perimeter
            while perimeter <= limit:
                if perimeter in found_lengths:
                    multiples.add(perimeter)
                else:
                    found_lengths.add(perimeter)
                perimeter += tmp_perimeter

    diff_set = found_lengths.difference(multiples)

    print(len(found_lengths))
    print(diff_set)

    print('uniqe perimeters found:', len(diff_set))


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def version1():
    limit = 1500000  # 1500001

    squares_ls = [x ** 2 for x in range(1, int(limit / 2))]
    squares_set = set(squares_ls)
    print('squares generated')

    found_lengths = set()
    multiples = set()

    t0 = time.time()
    m = len(squares_ls)
    for i in range(len(squares_ls)):
        if i % 100 == 0:
            print('i: {}, {}%, {}sec'.format(i, round((i / m) * 100, 5), round(time.time() - t0)))

        a = squares_ls[i]
        for j in range(i, len(squares_ls)):
            b = squares_ls[j]
            c = a + b
            if i + j + math.sqrt(c) + 2 > limit:
                break

            if c in squares_set:
                perimeter = i + j + squares_ls.index(c) + 3  # +3 because 3x index offset by 1
                if perimeter in found_lengths:
                    multiples.add(perimeter)
                else:
                    found_lengths.add(perimeter)

    print('finished calc difference...')
    diff_set = found_lengths.difference(multiples)

    print(found_lengths)
    print(diff_set)

    print('uniqe perimeters found:', len(diff_set))

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
