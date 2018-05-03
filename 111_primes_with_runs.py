"""
idea:
"""
import time

import primesieve


def main():
    solution()

def solution():
    n = 10
    max_count, nums = get_nums_with_max_digit_count(n)
    res = 0
    for digit in nums:
        res += nums[digit]
    print('wanted sum:', res)


def get_nums_with_max_digit_count(digits):
    # contains max num of repeated digits for every digit
    max_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    nums = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    it = primesieve.Iterator()
    it.skipto(10**(digits - 1))

    prime = it.next_prime()
    upper_limit = 10**digits

    progress = 1
    while prime < upper_limit:
        if progress % 100000 == 0:
            print('curr prime:', prime)
        progress += 1

        digit_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        #digit_count = [0 for _ in range(10)]
        n = prime
        while n:
            r, n = n % 10, n // 10
            digit_count[r] += 1

        for digit in digit_count:
            if digit_count[digit] > max_count[digit]:
                max_count[digit] = digit_count[digit]
                nums[digit] = prime
            elif digit_count[digit] == max_count[digit]:
                nums[digit] += prime

        prime = it.next_prime()

    print(max_count)
    print(nums)
    return max_count, nums


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
