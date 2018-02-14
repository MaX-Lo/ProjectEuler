"""
idea:


"""
import time


def main():
    max_digit_sum = 0
    for a in range(1, 100):
        print("progress", a)
        for b in range(1, 100):
            digit_sum = get_digit_sum(a**b)
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
                print("tmp max:", max_digit_sum)
    print("max digit sum:", max_digit_sum)


def get_digit_sum(num):
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)
    return digit_sum


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
