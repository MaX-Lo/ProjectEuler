"""
idea:
"""
import time

import math
import primesieve


def main():
    n = 100000

    primes = set(primesieve.primes(1000000))

    it = primesieve.Iterator()

    # i=2  n=i*4=8   sum=9  diagonal points= sum+(sum-i)+(sum-2*i)+(sum-3*i)
    total = 1
    num_of_primes = 0
    diagonal_nums = 1
    for i in range(2, n, 2):
        total += i * 4
        diagonal_nums += 4
        it.skipto(total-3*i - 1)
        num_of_primes += 1 if it.next_prime() == total-3*i else 0
        it.skipto(total-2*i - 1)
        num_of_primes += 1 if it.next_prime() == total-2*i else 0
        it.skipto(total-i - 1)
        num_of_primes += 1 if it.next_prime() == total-i else 0
        it.skipto(total - 1)
        num_of_primes += 1 if it.next_prime() == total else 0

        ratio = num_of_primes / diagonal_nums
        print('i', i+1, 'ratio', ratio)
        if ratio < 0.1:
            print("i", i+1, 'total', total)
            break


def is_prime(n):
    if n % 2 == 0:
        return False

    a = math.ceil(math.sqrt(n))
    b = a**2 - n
    while not math.sqrt(b).is_integer():
        b += 2*a + 1
        a += 1

    y = math.sqrt(b)
    a = a + y

    if int(a) == 1 or int(n/a) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)