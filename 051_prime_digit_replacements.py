"""
idea:

iterative check all primes beginning with 1 digit primes than 2, 3, 4 ...
end all combinations e.g for 3-digit primes exchanging 1 digit at all possible position
than 2-digit... (in general up to n-1, where n is number of digits)
"""
import time

import primesieve


def main():

    max_sequence_len = -1
    max_num = -1

    i = 10
    while max_sequence_len < 9:
        primes = primesieve.primes(i, i*10-1)
        i *= 10
        max_sequence_len, max_num = test_primes(primes)
        print("max sequence len:", max_sequence_len)
        print("corresponding num:", max_num)


def test_primes(primes):
    prime_len = len(str(primes[0]))
    print("testing {} digit long numbers".format(prime_len))

    prime_set = set(primes)

    max_prime_counter = -1
    max_prime_counter_num = -1

    num_of_bin_numbers = 2**prime_len

    max_progress = len(primes)
    count = 0
    for num in range(1, num_of_bin_numbers-1):
        count += 1
        if count % 10 == 0:
            print(count/max_progress * 100)

        digits_to_replace = str(bin(num)[2:])

        if len(digits_to_replace) < prime_len:
            digits_to_replace = (prime_len-len(digits_to_replace))*'0' + digits_to_replace

        for prime in primes:
            prime_counter = 0
            smalles_num_in_sequence = -1
            for i in range(0, 10):

                prime_replaced = [char for char in str(prime)]
                dig_pos = 0
                for char in digits_to_replace:
                    if char == '1':
                        prime_replaced[dig_pos] = str(i)
                    dig_pos += 1

                new_number = int(''.join(prime_replaced))
                if new_number in prime_set:
                    if prime_counter == 0:
                        smalles_num_in_sequence = new_number
                    prime_counter += 1

            if max_prime_counter < prime_counter:
                max_prime_counter = prime_counter
                max_prime_counter_num = smalles_num_in_sequence

    #print("smalles num", max_prime_counter_num)
    #print("sequence length", max_prime_counter)

    return max_prime_counter, max_prime_counter_num


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
