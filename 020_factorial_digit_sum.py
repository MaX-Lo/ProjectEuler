"""
Task:

factorial digit sum of 100!
"""
import time

import math


def main():
    start_time = time.time()

    num = math.factorial(100)
    print(num)
    print("digit sum", digit_sum(str(num)))

    print("time:", time.time() - start_time)


def digit_sum(number_string):
    sum = 0
    for char in number_string:
        sum += int(char)
    return sum


if __name__ == '__main__':
    main()
