
"""
Task:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
    limit = 1000
    sum_with_intersections = sum_of_multiples(3, limit) + sum_of_multiples(5, limit)
    # numbers that are multiples of 3 and 5 at the same time shouldn't be accounted doubled for
    sum_without_intersections = sum_with_intersections - sum_of_multiples(15, 1000)
    print(sum_without_intersections)


def sum_of_multiples(number, limit):
    sum = 0
    for i in range(number, limit, number):
        sum += i
    return sum


if __name__ == '__main__':
    main()