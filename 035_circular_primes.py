"""
Task:


"""
import time

import primesieve as primesieve


def main():
    primes = set(primesieve.primes(1000000))

    wanted_nums = set()

    for prime in primes:
        str_prime = str(prime)
        all_rotations_are_prime = True
        for rotation_num in range(len(str_prime)):
            str_prime = str_prime[1:] + str_prime[0]
            if int(str_prime) not in primes or str_prime in wanted_nums:
                all_rotations_are_prime = False
                break
        if all_rotations_are_prime:
            wanted_nums.add(prime)

    print(wanted_nums)
    print("num of these primes:", len(wanted_nums))


def all_primes(limit):
    # list containing for every number whether it has been marked already
    numbers = {}
    for x in range(3, limit, 2):
        numbers[x] = False

    primes = [2, 3]

    p = 3
    while p < limit:
        for i in range(p, limit, p):
            numbers[i] = True

        for i in range(p, limit, 2):
            if not numbers[i]:
                p = i
                numbers[i] = True
                primes.append(i)
                break
            else:
                p += 1
    return primes


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
