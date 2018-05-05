"""
idea:
"""
import time

import math


def main():
    upper_limit = 10**13

    found_nums = []

    for x in range(2, int(math.sqrt(upper_limit))):
        if x % 100000 == 0:
            print('prog:', x)

        p = x
        while p < upper_limit:
            p *= x
            if digit_sum(p) == x:
                found_nums.append(p)

    found_nums.sort()
    print('found {} nums'.format(len(found_nums)))
    print(found_nums)
    if len(found_nums) >= 30:
        print('30th:', found_nums[29])


def digit_sum(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
