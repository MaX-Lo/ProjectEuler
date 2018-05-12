"""
idea:
"""
import time

import math

import copy


def main():
    power = 100
    limit = 10**power

    dec = count_decreasing(limit)
    inc = count_increasing(limit)
    repdigits_nums = 9 * (int(math.floor(math.log10(limit) + 1)) - 1) + (power-1)
    print('re', repdigits_nums)

    print('inc:', inc, 'dec', dec, 'rep', repdigits_nums)
    print('non bouncy smaller {}: {}'.format(limit, dec + inc - repdigits_nums))


def count_increasing(limit):
    iterations = int(math.floor(math.log10(limit) + 1)) - 1
    # save possibilities for last powers numbers beginning with the corresponding key
    possibilities = {x: 1 for x in range(1, 10)}
    possibilities[0] = 0  # since 0 isn't positive

    new_possibilities = {}
    for i in range(1, iterations):
        for x in range(10):
            new_possibilities[x] = 0
            for z in range(x, 10):
                new_possibilities[x] += possibilities[z]
        #print(i + 1, new_possibilities)
        possibilities = copy.deepcopy(new_possibilities)

    all_possibilities = get_dict_sum(possibilities)

    return all_possibilities


def get_dict_sum(possibilities):
    res = 0
    for key in possibilities:
        res += possibilities[key]
    return res


def count_decreasing(limit):
    iterations = int(math.floor(math.log10(limit) + 1)) - 1
    # save possibilities for last powers numbers beginning with the corresponding key
    possibilities = {x: 1 for x in range(10)}
    print(1, possibilities)

    all_possibilities = -1 + get_dict_sum(possibilities)
    new_possibilities = {}
    for i in range(1, iterations):
        for x in range(10):
            new_possibilities[x] = 0
            for z in range(x, -1, -1):
                new_possibilities[x] += possibilities[z]
        print(i + 1, new_possibilities)
        possibilities = copy.deepcopy(new_possibilities)
        all_possibilities += get_dict_sum(possibilities)

    print('all:', all_possibilities)
    return all_possibilities


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)