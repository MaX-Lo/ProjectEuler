"""
idea:

num of digits in a number:
digit_count = floor(log10(n))+1

i^n = nummer
-> für i <= 9 wird die Zahl mit zunehmenden n zu kurz
-> für i == 10 ist die Zahl immer um 1 zu kurz
-> für i >= 11 wird die Zahl mit zunehmenden n zu lang
"""
import time

import math


def main():
    n_digit_nums = set()
    for base in range(1, 10):
        power = 1
        while True:
            num = base**power
            len_diff = power - digit_count(num)
            if len_diff == 0:
                n_digit_nums.add(num)
            else:
                break
            power += 1

    print(len(n_digit_nums))


def digit_count(num):
    return math.floor(math.log10(num)) + 1


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
