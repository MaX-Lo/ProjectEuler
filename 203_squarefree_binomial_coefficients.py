"""
idea:
"""
import time

import copy

import math

import primesieve


def main():

    nums = distinct_num_in_pascal_triangle(51)
    max_prime = int(math.sqrt(max(nums)))
    prime_sqs = [prime**2 for prime in primesieve.primes(max_prime)]

    found = set()
    for num in nums:
        squarefree = True
        for prime_sq in prime_sqs:
            if prime_sq > num:
                break
            if num % prime_sq == 0:
                squarefree = False
                break
        if squarefree:
            found.add(num)

    print('counted:', len(found), 'sum', sum(found))


def distinct_num_in_pascal_triangle(num_of_rows):
    nums = set()
    nums.add(1)
    last_row = [1]
    for i in range(1, num_of_rows):
        row = [1]
        for j in range(len(last_row)-1):
            row.append(last_row[j] + last_row[j+1])
            nums.add(last_row[j] + last_row[j+1])
        row.append(1)
        last_row = copy.deepcopy(row)
    return nums


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
