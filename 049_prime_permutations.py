"""
idea:


"""
import time

import itertools

import primesieve


def main():

    primes = set(primesieve.primes(1000, 9999))

    for prime in primes:
        digits = [c for c in str(prime)]
        unfiltered_permutations = tuple_list_to_int_list(list(itertools.permutations(digits)))

        permutations = []
        for perm in unfiltered_permutations:
            if perm in primes:
                permutations.append(perm)

        for perm in permutations:
            if prime < perm:
                diff = perm - prime
                if (perm + diff) in permutations and (perm + diff) in primes:
                    if len({perm, prime, (perm+diff)}) == 3:
                        print(prime, perm, perm+diff)
            elif prime > perm:
                diff = prime - perm
                if (prime + diff) in permutations and (prime + diff) in primes:
                    if len({perm, prime, (prime + diff)}) == 3:
                        print(prime, perm, prime + diff)


def tuple_list_to_int_list(tuple_list):
    int_list = []
    for ele in tuple_list:
        num_str = ''
        for digit in ele:
            num_str += digit
        int_list.append(int(num_str))
    return int_list


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
