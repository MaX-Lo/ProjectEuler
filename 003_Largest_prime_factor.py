"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Idea:
use factorization after Fermat

"""
# FixMe seem not to work for every number e.g. 50 ???

import math

import time


def main():
    print(get_factors(600851475143))


def get_factors(n):
    if n == 10 or n == 5:
        return 5
    if n == 9 or n == 6 or n == 3:
        return 3
    if n == 2 or n == 4 or n == 8:
        return 2

    x = math.ceil(math.sqrt(n))
    r = x * x - n
    while not math.sqrt(r).is_integer():
        r = math.floor(r) + 2 * x + 1
        x = x + 1

    y = math.sqrt(r)
    a = x + y
    b = x - y

    if a != 1 and b != 1:
        greatest_in_a = get_factors(int(a))
        greatest_in_b = get_factors(int(b))
        return greatest_in_a if greatest_in_a > greatest_in_b else greatest_in_b
    elif a != 1 and b == 1:
        return a
    elif a == 1 and b != 1:
        return b


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)