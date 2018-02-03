"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time


def main():
    start = time.time()
    # n=20 > 26.525495767593384, >232792560

    n = 9699690 #2*3*5*7*11*13*17*19
    print(n)
    while not is_devisible(n):
        n += 9699690

    print(time.time()-start)
    print(n)


def is_devisible(n):
    devisible = True
    for i in range(11, 20):
        if n % i != 0:
            devisible = False
    return devisible


if __name__ == '__main__':
    main()