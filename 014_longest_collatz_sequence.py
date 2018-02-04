"""
Task:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
"""
import time


def main():
    start_time = time.time()

    max_length = -1
    max_starting_number = -1
    for n in range(1, 1000000):
        starting_number = n
        length = 1
        while n != 1:
            length += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
        if length > max_length:
            max_starting_number = starting_number
            max_length = length
        print(starting_number)

    print("starting number:", max_starting_number)
    print("chain length:", max_length)

    print("time:", time.time() - start_time)


if __name__ == '__main__':
    main()
