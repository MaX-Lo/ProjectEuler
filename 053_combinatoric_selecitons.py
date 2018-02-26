"""
idea:

r = n / 2

"""
import time

import math


def main():
    n = 22

    num_of_values = 0

    while n <= 100:
        r = int(math.floor(n / 2))

        val = nCr(n, r)
        go_further = False
        if val > 1000000:
            num_of_values += 1
            if n % 2 == 1:
                num_of_values += 1

            go_further = True
        step = 1
        while go_further:
            next_val = nCr(n, r-step)
            if next_val > 1000000:
                step += 1
                num_of_values += 2
            else:
                go_further = False

        n += 1

    print("num of values", num_of_values)


def nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
