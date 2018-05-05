"""
idea:
"""
import copy
import time

import itertools

import math


def main():
    sets = read_file('105_sets.txt')
    res = 0
    for my_set in sets:
        if test(my_set):
            print(my_set, sum(my_set))
            res += sum(my_set)
    print('wanted sum', res)


def test(nums: list):
    """ list is sorted ascending"""
    # check if a subset with more nums than another subset has also a greater sum
    nums.sort()

    for i in range(1, int(math.ceil(len(nums)/2))):
        small_nums_sum = sum(nums[:i+1])
        big_nums_sum = sum(nums[-i:])
        if small_nums_sum <= big_nums_sum:
            return False

    for subset_len in range(2, len(nums)//2 + 1):
        for subset1 in itertools.combinations(nums, subset_len):
            remaining = copy.deepcopy(nums)
            for num in subset1:
                remaining.remove(num)
            s1 = sum(subset1)
            for subset2 in itertools.combinations(remaining, subset_len):
                s2 = sum(subset2)
                if s1 == s2:
                    return False
    return True


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append([int(x) for x in line.strip().split(',')])
    return data_set


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
