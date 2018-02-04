"""
Task:

digit sum of 2^1000
"""
import time


def main():
    start_time = time.time()

    num = 2**1000
    print(num)
    print("digit sum", digit_sum(str(num)))

    print("time:", time.time() - start_time)


def digit_sum(number_string):
    sum = 0
    for char in number_string:
        sum += int(char)
    return sum


if __name__ == '__main__':
    main()
