"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

not my solution, but a very short one:

def problem6(r):
    return sum(r)** 2- sum([x** 2 for x in r])
problem6(range(1,101))
"""

def main():
    number = 100

    n1 = sum_of_squares(number)
    n2 = square_of_sum(number)
    print("sum of squares:", n1)
    print("square of sum:", n2)
    print("difference:", n2-n1)


def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum


def square_of_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum*sum


if __name__ == '__main__':
    main()