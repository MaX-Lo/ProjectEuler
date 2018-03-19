"""
idea:
"""
import time

from decimal import getcontext, Decimal

import math


def main():
    getcontext().prec = 103

    res = 0
    for i in range(1, 101):
        if math.sqrt(i) % 1 == 0:
            continue

        num = Decimal.sqrt(Decimal(i))
        digital_sum = int(str(num)[0]) + digit_sum(str(num)[2:-3])
        res += digital_sum
        print(i, digital_sum)

    print('wanted sum:', res)


def digit_sum(num):
    res = 0
    #print(len(num))
    for c in num:
        res += int(c)
    return res


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)