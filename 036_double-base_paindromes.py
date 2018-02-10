"""
Task:


"""
import time

import math


def main():
    wanted_nums = []

    for i in range(1000000):
        if is_palindrome(str(i)) and is_palindrome(str(bin(i))[2:]):
            wanted_nums.append(i)

    print(wanted_nums)
    print('sum of wanted nums:', sum(wanted_nums))


def is_palindrome(txt):
    if txt[0] == '0':
        return False

    for i in range(int(math.floor(len(txt)/2))):
        if txt[i] != txt[len(txt)-1-i]:
            return False

    return True


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)