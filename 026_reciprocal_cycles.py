"""
Task:

http://www.mathblog.dk/project-euler-26-find-the-value-of-d-1000-for-which-1d-contains-the-longest-recurring-cycle/
"""
import time


def main():
    cycle_len = 0
    num = 0

    for i in range(1000, 1, -1):
        if cycle_len >= i:
            break

        remainders = [0 for _ in range(i)]
        value = 1
        pos = 0

        while remainders[value] == 0 and value != 0:
            remainders[value] = pos
            value *= 10
            value %= i
            pos += 1

        if pos - remainders[value] > cycle_len:
            num = i
            cycle_len = pos - remainders[value]

    print("cycle len:", cycle_len)
    print("num:", num)


def get_cycle_lenght(numerator, denominator):
    x = numerator * 9
    z = x
    cycle_length = 1
    while z % denominator:
        z = z * 10 + x
        cycle_length += 1
    return cycle_length


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)

