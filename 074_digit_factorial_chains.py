"""
idea:
"""
import time

import math


def main():
    t0 = time.time()

    count = 0
    for i in range(1, 1000000):
        if i % 10000 == 0:
            print('{}%, {}sec'.format(i / 10000, round(time.time() - t0), 3))

        if get_chain_len(i) == 60:
            count += 1

    print('wanted num:', count)


def get_chain_len(num):
    chain = set()

    element = num
    while element not in chain:
        chain.add(element)
        tmp = 0
        for digit in str(element):
            tmp += math.factorial(int(digit))
        element = tmp

    return len(chain)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
