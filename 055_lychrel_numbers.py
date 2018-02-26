"""
idea:


"""
import time


def main():
    num_of_not_lychrels = 0

    for n in range(1, 10000):
        steps = 0
        tmp_num = n
        while steps < 50:
            tmp_num = reverse_add(tmp_num)
            if is_palindrome(tmp_num):
                num_of_not_lychrels += 1
                break
            steps += 1
    print('lychrels', 9999 - num_of_not_lychrels)


def reverse_add(x):
    rev_x = int(str(x)[::-1])
    return x + rev_x


def is_palindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
