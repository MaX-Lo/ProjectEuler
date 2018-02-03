"""
Task:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time

# FixMe inefficient solution for larger numbers


def main():
    start_time = time.time()

    a = 1
    b = 2
    c = 3

    while not (a**2 + b**2 == c**2 and a+b+c == 1000):
        if b == c:
            c += 1
            a = 1
            b = 2
        elif a == b:
            b += 1
            a = 1
        a += 1

    print("{}*{}*{}={}".format(a, b, c, a*b*c))
    print("time:", time.time() - start_time)


if __name__ == '__main__':
    main()
