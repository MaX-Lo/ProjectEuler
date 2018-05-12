"""
idea:
"""
import copy
import time

import primesieve


def main():
    limit = 200

    print(primesieve.primes(200))

    prime_combinations = [[1]]
    for prime in primesieve.primes(17):
        prime_combinations.extend(get_prime_exponents(prime))
    primes = primesieve.primes(200)

    print('finished building masks')

    answer = 0
    for n in range(1, limit+1):
        min_steps = 1000000000000
        for org_combination in prime_combinations:
            combination = copy.deepcopy(org_combination)
            curr_exp = combination[-1]
            steps = len(combination) - 1
            if curr_exp > n:
                continue
            while curr_exp < n:
                for i in range(len(combination)-1, -1, -1):
                    if curr_exp + combination[i] <= n:
                        curr_exp += combination[i]
                        combination.append(curr_exp)
                        steps += 1
                        break

            if steps < min_steps:
                if n in primes:
                    prime_combinations.append(combination)
                print(combination)
                min_steps = steps
        print('min steps for', n, ':', min_steps)
        answer += min_steps

    print('sum', answer)
    print("that isnt the answer, but close to it. (real answer is 1582)")


def get_prime_exponents(prime):
    """ return a list with all ways the given prime can be generated
        e.g. for prime=5 it's x^1, x^2, x^4, x^5 or x^1, x^2, x^3, x^5
    """
    exponents = [1]
    found_combinations = f(exponents, prime)
    min_len = min(map(len, found_combinations))
    shortest = list(filter(lambda combination: len(combination) == min_len, found_combinations))
    return shortest


def f(exponents: list, prime: int):
    found_combinations = []
    for i in range(len(exponents)):
        tmp_exponents = copy.deepcopy(exponents)
        new_exp_candidat = exponents[-1] + exponents[i]
        tmp_exponents.append(new_exp_candidat)
        if new_exp_candidat < prime:
            found_combinations.extend(f(copy.deepcopy(tmp_exponents), prime))
        elif new_exp_candidat == prime:
            found_combinations.append(copy.deepcopy(tmp_exponents))
        else:
            continue
    return found_combinations


def count_exponentiation_steps(n):
    steps = 0
    # starting with 'binary' exponentiation check whether exponentiation
    # with 3, 5, 7... needs less steps
    max_prime = n // 2
    primes = primesieve.primes(max_prime)

    # ToDo generic generation of masks
    masks = [
        [1, 2],
        [1, 2, 3],
        [1, 2, 4, 5], [1, 2, 3, 5],
        [1, 2, 4, 6], [1, 2, 3, 6],
        [1, 2, 4, 6, 7], [1, 2, 3, 6, 7], [1, 2, 3, 5, 7],
        [1, 2, 4, 8, 9], [1, 2, 3, 6, 9], [1, 2, 4, 5, 9],
        [1, 2, 4, 8, 10, 11], [1, 2, 3, 6, 9, 11], [1, 2, 4, 5, 10, 11], [1, 2, 3, 5, 10, 11], [1, 2, 4, 6, 7, 11]
    ]

    for prime in primes:
        exponents = [1]
        while exponents[-1] < prime:
            for i in range(len(exponents)-1, -1, -1):
                if exponents[-1] + exponents[i] <= prime:
                    exponents.append(exponents[-1] + exponents[i])
                    break
        print('prime', prime, exponents)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
