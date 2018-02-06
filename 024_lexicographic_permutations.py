"""
Task:


"""
import time

import math


def main():
    start_time = time.time()

    solution()

    print("time:", time.time() - start_time)

def solution():
    perm_num = 1000000
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    #perm_num = 5
    #nums = [0, 1, 2]

    permutation = []
    while len(nums) >= 1:
        fac = math.factorial(len(nums)-1)
        x = 0
        if perm_num % fac != 0:
            x = int(math.floor(perm_num / fac))
            perm_num = perm_num - x * fac
        else:
            x = int(perm_num / fac) - 1
            perm_num = perm_num - x * fac

        permutation.append(nums[x])
        # print(permutation, "perm num", perm_num, "fac", fac, nums, nums[x])
        nums.remove(nums[x])

    print(permutation)

def generate(nums, counter):
    for i in range(len(nums)):
        nnums = nums[1:]
        print(nums[0], nums, nnums, "counter", counter)
        if len(nnums) > 1:
            counter = generate(nnums, i)
        else:
            return counter + 1
    return counter


if __name__ == '__main__':
    main()
