"""
idea:


"""
import time

import math
import primesieve


def main():
    primes = primesieve.primes(10000)
    square_numbers = [x**2 for x in range(1, 100)]
    odd_composites = {(2*i+1)*(2*j+1) for i in range(1, 1000) for j in range(i, 1000)}

    for prime in primes:
        for square_number in square_numbers:
            x = prime + 2*square_number
            if x in odd_composites:
                odd_composites.remove(x)

    print(min(odd_composites))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
