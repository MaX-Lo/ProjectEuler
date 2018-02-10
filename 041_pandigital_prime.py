"""
idea:

largest pandigital number is 987.654.321
"""
import time
import primesieve


def main():

    largest = -1
    for i in range(9, 1, -1):
        print("progress", i)
        i_largest = largest_pandigital(i)
        if i_largest > largest:
            largest = i_largest

    print("largest:", largest)


def largest_pandigital(length):
    """
    :param length: length of number e.g 12345 has length 5
    """

    largest = -1

    it = primesieve.Iterator()
    it.skipto(10**(length-1))
    prime = it.next_prime()

    num = '987654321'
    max_num = int(num[9 - length:])
    i = 0
    while prime < max_num:
        i += 1
        if i % 1000000 == 0:
            print(prime)

        prime_str = str(prime)
        if len(set(prime_str)) == len(prime_str) and is_pandigital(prime_str):

            if prime > largest:
                largest = prime
        prime = it.next_prime()

    print("largest:", largest if largest != -1 else "none found!")
    return largest


def is_pandigital(num_str):
    for i in '123456789'[:len(num_str)]:
        if i not in num_str:
            return False
    return True


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)