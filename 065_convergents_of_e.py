"""
idea:
"""
import time


def main():

    continued_fraction = [2, 1]
    k = 2
    for i in range(3, 101):
        if i % 3 == 0:
            continued_fraction.append(k)
            k += 2
        else:
            continued_fraction.append(1)

    eval_continued_fraction(continued_fraction)


def eval_continued_fraction(continued_frac):
    """
    evaluate a continued fraction
    expect a list as: [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8] (e.g. for e)
    """

    numerator = 1
    denominator = continued_frac[-1]
    continued_frac.pop(-1)

    for num in reversed(continued_frac):
        numerator += num * denominator
        numerator, denominator = denominator, numerator

    # last exchange was unnecessary therefore reverse it back again
    numerator, denominator = denominator, numerator
    print(numerator, '/', denominator)
    print('numerator digit sum:', get_digit_sum(numerator))


def get_digit_sum(num):
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)
    return digit_sum


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)