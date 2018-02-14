"""
idea:

check iterative for a certain chain length
"""
import time
import primesieve


def main():
    primes = primesieve.primes(999999)
    print("nums to test:", len(primes))

    max_chain_length = -1
    prime_with_max_chain_length = -1

    for i in range(2, len(primes)):
        prime = get_prime_with_given_chain_length(i, primes)
        if prime != -1:
            max_chain_length = i
            prime_with_max_chain_length = prime
            print("prime with chain length:", i, prime_with_max_chain_length)

    print("max chain len", max_chain_length, "prime", prime_with_max_chain_length)


def get_prime_with_given_chain_length(length, primes):
    prime_set = set(primes)

    prime_sum = sum(primes[x] for x in range(0, length))
    if prime_sum in prime_set:
        return prime_sum

    for i in range(length, len(primes)):
        prime_sum = prime_sum - primes[i-length] + primes[i]
        if prime_sum in prime_set:
            return prime_sum

    return -1


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
