"""
Task:


"""
import time

import math


def main():

    wanted_nums = []

    for i in range(3, 1000000):
        num_sum = 0
        for digit in str(i):
            num_sum += math.factorial(int(digit))
        if i == num_sum:
            wanted_nums.append(i)

    print(wanted_nums)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
