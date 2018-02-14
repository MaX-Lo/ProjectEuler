"""
idea:

first num has to be one because if it is larger e.g. 2
than 2x6=12 has at at least one more digit
"""
import time

import itertools


def main():
    num = 1
    while True:
        if str(num)[0] != '1':
            num += 10**(len(str(num))-1)*8

        if num % 5000 == 0:
            print("progress:", num)

        if has_equal_digits(num):
            break
        else:
            num += 1
    print(num)


def has_equal_digits(num):
    num_str = str(num)
    num_perms = get_permutation_list(num_str)

    for i in range(2, 7):
        num2 = i * num
        num2_str = str(num2)

        if len(num_str) != len(num2_str):
            return False
        if num2 not in num_perms:
            return False
    return True


def get_permutation_list(num):
    digits = [c for c in str(num)]
    permutations = list(itertools.permutations(digits))

    int_list = []
    for ele in permutations:
        num_str = ''
        for digit in ele:
            num_str += digit
        int_list.append(int(num_str))
    return int_list


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
