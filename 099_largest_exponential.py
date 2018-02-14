"""
idea:


"""
import time

import math


def main2():
    data = read_file('099_base_exp.txt')

    max_res = 1
    largest_line = -1

    line_count = 1

    for num, exp in data:
        print("line count:", line_count)
        res = exp*math.log(num)
        if res > max_res:
            max_res = res
            largest_line = line_count
        line_count += 1

    print("largest line", largest_line)


def main():
    # estimation_approach()
    data = read_file('099_base_exp.txt')

    largest_num = 1
    largest_exp = 1
    largest_line = -1

    line_count = 1
    for num, exp in data:
        print("line count:", line_count)
        if compare_nums(num, exp, largest_num, largest_exp):
            print(num, exp, "old", largest_num, largest_exp)
            largest_num = num
            largest_exp = exp
            largest_line = line_count

        line_count += 1

    print("largest line", largest_line)
    print(largest_num, largest_exp)


def compare_nums(num1, exp1, num2, exp2):
    tmp1 = num1
    tmp2 = num2
    while exp1 > 1 or exp2 > 1:
        if tmp1 < tmp2 and exp1 == 1:
            return False
        elif tmp2 < tmp1 and exp2 == 1:
            return True

        if exp1 > 1 and tmp2 >= 1:
            tmp1 *= num1
            exp1 -= 1
        if exp2 > 1 and tmp1 >= 1:
            tmp2 *= num2
            exp2 -= 1

        if tmp1 >= 100000000 or tmp2 >= 100000000:
            tmp1 /= 1000000
            tmp2 /= 1000000

        #print("exp1", exp1, "exp2", exp2, "n1", tmp1, "n2", tmp2)
    return tmp1 > tmp2


def estimation_approach():
    data = read_file('099_base_exp.txt')

    max_estimation = -1
    num_with_max_estimation = -1
    line_num = 1
    for num, exp in data:
        estimation = estimate_digits(num, exp)
        if estimation > max_estimation:
            max_estimation = estimation
            num_with_max_estimation = line_num
            print(max_estimation)
        line_num += 1

    print("line num:", num_with_max_estimation)


def estimate_digits(num: int, exp: int):
    first_hundred_exp = num**3000

    averagely_new_digits = (len(str(first_hundred_exp)) - len(str(num))) / 2999

    digit_estimation = len(str(num)) + averagely_new_digits * (exp-1)

    return digit_estimation


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        x, y = line.strip().split(',')
        data_set.append((int(x), int(y)))
    return data_set


if __name__ == '__main__':
    start_time = time.time()
    main2()
    print("time:", time.time() - start_time)