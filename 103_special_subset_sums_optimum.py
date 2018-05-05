"""
idea:

- get a solution near optimum
- check numbers around that solution for optimum solution
"""
import copy
import time

import math

import itertools


def main():
    ist = test([11, 17, 20, 22, 23, 24])
    print(ist)
    solution()


def solution():
    # last = [6, 9, 11, 12, 13]
    last = [11, 18, 19, 20, 22, 25]
    mid = last[len(last)//2]
    n = 7
    nums = [last[x] + mid for x in range(n - 1)]
    nums.insert(0, mid)
    guess_sum = sum(nums)
    best_sum = guess_sum
    best_nums = nums

    max_deviation = 3
    nums = [num - max_deviation for num in nums]

    for i0 in range(nums[0], nums[0]+2*max_deviation):
        for i1 in range(nums[1], nums[1] + 2 * max_deviation):
            if i1 <= i0:
                continue
            for i2 in range(nums[2], nums[2] + 2 * max_deviation):
                if i2 <= i1:
                    continue
                for i3 in range(nums[3], nums[3] + 2 * max_deviation):
                    if i3 <= i2:
                        continue
                    for i4 in range(nums[4], nums[4] + 2 * max_deviation):
                        if i4 <= i3:
                            continue
                        for i5 in range(nums[5], nums[5] + 2 * max_deviation):
                            if i5 <= i4:
                                continue
                            for i6 in range(nums[6], nums[6] + 2 * max_deviation):
                                if i6 <= i5:
                                    continue

                                tmp_sum = i0 + i1 + i2 + i3 + i4 + i5 + i6
                                if tmp_sum < best_sum:
                                    if test([i0, i1, i2, i3, i4, i5, i6]):
                                        best_sum = tmp_sum
                                        best_nums = [i0, i1, i2, i3, i4, i5, i6]

    print('optimum sum:', best_sum)
    print('optimum nums:', best_nums)


def test(nums):
    """ list is sorted ascending"""
    print('nums:', nums)

    # check if a subset with more nums than another subset has also a greater sum
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


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
