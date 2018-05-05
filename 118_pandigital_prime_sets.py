"""
idea:
"""
import time

import itertools

import primesieve


def main():
    solution()


def solution():
    primes = set(str(x) for x in primesieve.primes(99999999))
    print('got primes')
    masks = get_masks()
    already_found = set()

    count = 0
    for permutation in list(itertools.permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'])):
        # permutation = ('6', '3', '1', '8', '9', '4', '7', '2', '5')
        if is_prime(int(str().join(permutation))):
            count += 1
            print('all primes, perm', permutation, 'long, count', count)

        for mask, multiple in masks:
            i = 0
            all_primes = True
            nums = set()
            for subset_size in mask:
                num = str().join(permutation[i:i+subset_size])
                nums.add(num)
                i += subset_size
                if num not in primes:
                    all_primes = False
                    break

            if all_primes:
                nums = frozenset(nums)
                if nums not in already_found:
                    count += 1
                    already_found.add(nums)
                    print('all primes, perm', permutation, 'mask', mask, 'count', count)

    # ToDo check all 9 digit primes for having each digit exactly once
    print('all:', count)


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def get_masks():
    masks = [
        ([9], 1),
        ([8, 1], 1),
        ([7, 2], 1),
        ([7, 1, 1], 2),
        ([6, 3], 1),
        ([6, 2, 1], 1),
        ([6, 1, 1, 1], 3*2),
        ([5, 4], 1),
        ([5, 3, 1], 1),
        ([5, 2, 2], 2),
        ([5, 2, 1, 1], 2),
        ([5, 1, 1, 1, 1], 4*3*2),
        ([4, 4, 1], 2),
        ([4, 3, 2], 1),
        ([4, 3, 1, 1], 2),
        ([4, 2, 2, 1], 2),
        ([4, 2, 1, 1, 1], 3*2),
        ([4, 1, 1, 1, 1, 1], 5*4*3*2),
        ([3, 3, 3], 3*2),
        ([3, 3, 2, 1], 3*2),
        ([3, 3, 1, 1, 1], 2*3*2),
        ([3, 2, 2, 2], 3*2),
        ([3, 2, 2, 1, 1], 2*2),
        ([3, 2, 1, 1, 1, 1], 4*3*2),
        # [3, 1, 1, 1, 1, 1, 1],
        ([2, 2, 2, 2, 1], 4*3*2),
        ([2, 2, 2, 1, 1, 1], 3*2*3*2),
        # [2, 2, 1, 1, 1, 1, 1],
        # [2, 1, 1, 1, 1, 1, 1, 1],
        # [1, 1, 1, 1, 1, 1, 1, 1, 1] cant be prime
    ]

    # prime number has can't and with a digit thats not prime
    # cant end with 4, 6 or 8
    return masks


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)