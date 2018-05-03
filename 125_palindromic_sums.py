"""
idea:
"""
import time

import math


def main():
    solution()


def solution():
    limit = 10**8
    max_square = int(math.sqrt(limit))
    squares = [x**2 for x in range(1, max_square + 1)]

    found_palindroms = set()

    for i in range(1, len(squares)):
        square_sum = squares[-i]
        j = 1

        print('new', square_sum)

        while True:
            if is_palindromic(square_sum) and square_sum != squares[-i]:
                found_palindroms.add(square_sum)

            if (i+j) > len(squares):
                break

            if square_sum + squares[-(i+j)] < limit:
                square_sum += squares[-(i+j)]
            else:
                break

            j += 1

    print('counted {} nums with a sum of {}'.format(len(found_palindroms), sum(found_palindroms)))


def is_palindromic(num):
    n = str(num)
    for i in range(int(math.ceil(math.log10(num))) // 2):
        if n[i] != n[-(i+1)]:
            return False
    return True


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
