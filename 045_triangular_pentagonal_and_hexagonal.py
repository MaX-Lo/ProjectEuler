"""
idea:


"""
import time


def main():
    limit = 100000

    pentagons = {get_pentagonal(n) for n in range(1, int(limit/1.7))}
    hexagons = {get_hexagonal(n) for n in range(1, int(limit / 2))}

    for num in hexagons:
        if num in pentagons:
            print("next tri-pen-hex number", num)


def get_triangle(n):
    return (n**2 + n) / 2


def get_pentagonal(n):
    return n * (3*n - 1) / 2


def get_hexagonal(n):
    return 2*n**2 - n


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
