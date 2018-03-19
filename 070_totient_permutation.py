"""
idea:
"""
import time

import math
import primesieve


def main():
    limit = 10000000

    # check for all primes up to limit if their phi(prime) is a permutation of the corresponding prime
    # useful since afterwards only combinations of primes smaller limit/2 must be tested and the less
    # prime factors the better
    minimum, n_with_minimum = test_p_for_permutation(limit)
    primes = primesieve.primes(limit)
    t0 = time.time()
    print('after prime testing:')
    print("minimum:", minimum, "corresponding n:", n_with_minimum)

    nums = primesieve.primes(int(limit/2))
    print('number list generated, len:', len(nums))

    count = 0
    stop_limit = int(math.sqrt(limit))
    for i in range(len(nums)):
        # it's actually enough to stop after the num reached sqrt(limit)
        if nums[i] > stop_limit:
            break

        factors = {nums[i]: 1}
        product = nums[i]

        if product > limit:
            break

        phi = get_phi(factors)
        n = get_n(factors)
        if n / phi < minimum and is_permutation(n, phi):
            minimum = n / phi
            n_with_minimum = n

        count += 1
        tmp_min, tmp_n, count = f(factors, product, i, nums, limit, count)
        if tmp_min < minimum:
            print("tmp minimum and n", tmp_min, tmp_n)
            minimum = tmp_min
            n_with_minimum = tmp_n

    print('minimum:', minimum)
    print('corresponding n:', n_with_minimum)


def f(factors, product, start_index, nums, limit, count):
    minimum = 10000000
    n_with_minimum = -1
    for j in range(start_index, len(nums)):
        tmp_factors = dict(factors)
        tmp_product = product * nums[j]
        if tmp_product > limit:
            break

        if nums[j] in tmp_factors:
            tmp_factors[nums[j]] += 1
        else:
            tmp_factors[nums[j]] = 1

        phi = get_phi(tmp_factors)
        n = get_n(tmp_factors)

        if n / phi < minimum and is_permutation(n, phi):
            tmp_min = n / phi
            tmp_n = n
            if tmp_min < minimum:
                minimum = tmp_min
                n_with_minimum = tmp_n

        count += 1
        if count % 100000 == 0:
            print(count)

        tmp_min, tmp_n, count = f(tmp_factors, tmp_product, j, nums, limit, count)
        if tmp_min < minimum:
            minimum = tmp_min
            n_with_minimum = tmp_n

    return minimum, n_with_minimum, count


def test_p_for_permutation(limit):
    minimum = 1000000
    p_with_minimum = -1

    for p in primesieve.primes(limit):
        phi = p-1
        if p / phi < minimum and is_permutation(p, phi):
            minimum = p / phi
            p_with_minimum = p

    return minimum, p_with_minimum


def is_permutation(num1, num2):
    """
    return True if num1 is a permutation of num2
    else False
    """
    digit_count1 = count_digits(num1)
    digit_count2 = count_digits(num2)
    for digit in '0123456789':
        if digit_count1[digit] != digit_count2[digit]:
            return False
    return True


def count_digits(num):
    """
    create a dict with occurrences count of digits in the given num
    """
    counter_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for digit in str(num):
        counter_dict[digit] += 1
    return counter_dict


def get_n(factors):
    result = 1
    for factor in factors:
        result *= factor**factors[factor]
    return result


def get_phi(factors):
    phi = 1
    for factor in factors:
        phi *= factor**(factors[factor]-1) * (factor-1)
    return phi


def factorization(n, primes):
    """
    :param n: number to factorize
    :param primes: list with primes
    :return: dictionary with primes that occur (and count of them)
    """
    factors = {}

    # in case n itself is a prime
    if n in primes:
        factors[n] = 1
        return factors

    while n != 1:
        for prime in primes:
            if n % prime == 0:
                n /= prime
                if prime in factors:
                    factors[prime] += 1
                else:
                    factors[prime] = 1
                break
    return factors


def old():
    pass
    # for i in range(2, 10000000):
    #     if i % 1000 == 0:
    #         print('{}%, {}sec'.format(i / 100000, round(time.time() - t0, 5)))
    #
    #     phi = get_phi(factorization(i, primes))
    #     if i / phi < minimum:
    #         if is_permutation(i, phi):
    #             minimum = i/phi
    #             n_with_minimum = i


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
