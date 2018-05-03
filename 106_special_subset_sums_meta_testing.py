"""
idea:
"""
import copy
import time

import itertools

import math


def main():
    sets = [
        [1],  # 1
        [1, 2],  # 2
        [2, 3, 4],  # 3
        [3, 5, 6, 7],  # 4
        [6, 9, 11, 12, 13],  # 5
        [11, 18, 19, 20, 22, 24],  # 6
        [47, 44, 42, 27, 41, 40, 37],  # 7
        [81, 88, 75, 42, 87, 84, 86, 65],  # 8
        [157, 150, 164, 119, 79, 159, 161, 139, 158],  # 9
        [354, 370, 362, 384, 359, 324, 360, 180, 350, 270],  # 10
        [673, 465, 569, 603, 629, 592, 584, 300, 601, 599, 600],  # 11
        [1211, 1212, 1287, 605, 1208, 1189, 1060, 1216, 1243, 1200, 908, 1210]  # 12
    ]
    i = 1
    for my_set in sets:
        count = test(my_set)
        print(i, ' len needs tests:', count)
        i += 1


def test(nums: list):
    """ list is sorted ascending"""
    # check if a subset with more nums than another subset has also a greater sum
    nums.sort()

    count = 0

    for subset_len in range(2, len(nums)//2 + 1):
        for subset1 in itertools.combinations(nums, subset_len):
            remaining = copy.deepcopy(nums)
            for num in subset1:
                remaining.remove(num)
            for subset2 in itertools.combinations(remaining, subset_len):
                l1 = list(subset1)
                l1.sort()
                l2 = list(subset2)
                l2.sort()

                l1_ascending = False
                l1_descending = False
                for i in range(len(l1)):
                    if l1[i] < l2[i]:
                        if l1_ascending:
                            count += 1
                            break
                        l1_descending = True
                    elif l1[i] > l2[i]:
                        if l1_descending:
                            count += 1
                            break
                        l1_ascending = True
    return count / 2


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
