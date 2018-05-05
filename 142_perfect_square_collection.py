"""
idea:
"""
import time

import math


def main():
    limit = 1000

    squares = {x ** 2 for x in range(1, limit)}
    squares_dict = {x: x ** 2 for x in range(1, limit)}

    smallest = 10000000000000000000000000000

    for i in range(1, len(squares_dict)):
        e = squares_dict[i]
        if i % 50 == 0:
            print('prog', i)

        for j in range(i, len(squares_dict)):
            c = squares_dict[j]
            for k in range(j, len(squares_dict)):
                a = squares_dict[k]

                f = a - c
                d = a - e
                b = c - e

                if a % 2 != b % 2 or c % 2 != d % 2:
                    continue

                if not (f > 0 and d > 0 and b > 0):
                    continue

                if f in squares and d in squares and b in squares:
                    x = (a + b) / 2
                    y = (a - b) / 2
                    z = (c - d) / 2
                    if x > 0 and y > 0 and z > 0:
                         print('x y z', x, y, z, 'sum', x+y+z)


def old_approach():
    limit = 100000

    largest_square = limit + (limit - 1)
    squares = {x ** 2 for x in range(1, int(math.sqrt(largest_square)) + 1)}

    smallest = 10000000000000000000000000000

    for z in range(1, limit):
        if z % 500 == 0:
            print('prog', z)

        steps_z = get_steps(z % 10, {x for x in range(0, 10)})
        for y in range(z + 1, limit):
            if y + z not in squares or y - z not in squares:
                continue
            steps_y = get_steps(y, steps_z)
            # print(steps_y)
            # for x in range(y+1, limit):
            #    pass
            x = y + 1 - ((y + 1) % 10)

            while x < limit:
                for i in steps_y:
                    if all_perfect(x + y, y, z, squares):
                        if (x + i) + y + z < smallest:
                            smallest = x + y + z
                        print('x, y, z', x, y, z)
                x += 10

    print('smalles', smallest)

def all_perfect(x, y, z, squares):
    return x+y in squares and x-y in squares and x+z in squares and x-z in squares

def get_steps(digit, possible):
    candidates = []
    for x in possible:
        if (x+digit)%10 in {0, 1, 4, 5, 6, 9} and (x-digit+10)%10 in {0, 1, 4, 5, 6, 9}:
            candidates.append(x)
    return candidates


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
