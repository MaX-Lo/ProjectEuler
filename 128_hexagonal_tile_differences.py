"""
idea:
"""
import time

import primesieve


def main():
    old_approach()
    new_approach()


def new_approach():
    limit = 2000
    found_tiles = [1]

    layer = 1
    layer_start_num = 2
    layer_size = 6

    old_t1 = 1
    while len(found_tiles) < limit:
        if layer % 1000 == 0:
            print('layer', layer, 'found', len(found_tiles), 'num', layer_start_num)
        if is_prime(layer_start_num - 1 - old_t1) and \
                is_prime(layer_start_num + 1 - old_t1) and \
                is_prime(layer_start_num + layer_size - 1 - old_t1):
            found_tiles.append(old_t1)

        old_layer_end_num = layer_start_num + layer_size - 1
        if is_prime(old_layer_end_num - old_t1) and \
                is_prime(old_layer_end_num - layer_start_num) and \
                is_prime(layer_start_num + layer_size*2 + 6 - 2 - old_layer_end_num):
            found_tiles.append(old_layer_end_num)
        old_t1 = layer_start_num

        layer_start_num += layer_size
        layer_size += 6
        layer += 1

    print(found_tiles)
    print('2000th', found_tiles[1999])


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def old_approach():
    #  43, 0,53
    #  80, 5.2sec
    # 168, 63
    limit = 10000

    primes = set(primesieve.primes(limit))
    tiles = {(0, 0): 1}

    n = 2
    x, y = 0, -1
    layer = 1
    while n < limit:
        for _ in range(layer):
            tiles[(x, y)] = n
            x, y = x - 1, y + 1
            n += 1
        for _ in range(layer):
            tiles[(x, y)] = n
            x, y = x, y + 1
            n += 1
        for _ in range(layer):
            tiles[(x, y)] = n
            x, y = x + 1, y
            n += 1
        for _ in range(layer):
            tiles[(x, y)] = n
            x, y = x + 1, y - 1
            n += 1
        for _ in range(layer):
            tiles[(x, y)] = n
            x, y = x, y - 1
            n += 1
        for _ in range(layer):
            tiles[(x, y)] = n
            x, y = x - 1, y
            n += 1

        x, y = x, y - 1
        layer += 1

    max_layer = layer - 1
    solutions = [1]
    x, y = 0, -1
    for layer in range(1, max_layer): # outermost layer can't get testet
        for _ in range(layer):
            c = count_prime_diff_neighbours(x, y, tiles, primes)
            if c == 3:
                solutions.append(tiles[x, y])
            x, y = x - 1, y + 1
        for _ in range(layer):
            c = count_prime_diff_neighbours(x, y, tiles, primes)
            if c == 3:
                solutions.append(tiles[x, y])
            x, y = x, y + 1
        for _ in range(layer):
            c = count_prime_diff_neighbours(x, y, tiles, primes)
            if c == 3:
                solutions.append(tiles[x, y])
            x, y = x + 1, y
        for _ in range(layer):
            c = count_prime_diff_neighbours(x, y, tiles, primes)
            if c == 3:
                solutions.append(tiles[x, y])
            x, y = x + 1, y - 1
        for _ in range(layer):
            c = count_prime_diff_neighbours(x, y, tiles, primes)
            if c == 3:
                solutions.append(tiles[x, y])
            x, y = x, y - 1
        for _ in range(layer):
            c = count_prime_diff_neighbours(x, y, tiles, primes)
            if c == 3:
                solutions.append(tiles[x, y])
            x, y = x - 1, y

        x, y = x, y - 1

    print('solutions', solutions)
    print('sol count', len(solutions))


def count_prime_diff_neighbours(x, y, tiles: dict, primes: set):
    count = 0
    if abs(tiles[x, y] - tiles[x - 1, y]) in primes:
        count += 1
    if abs(tiles[x, y] - tiles[x + 1, y]) in primes:
        count += 1
    if abs(tiles[x, y] - tiles[x, y - 1]) in primes:
        count += 1
    if abs(tiles[x, y] - tiles[x, y + 1]) in primes:
        count += 1
    if abs(tiles[x, y] - tiles[x - 1, y + 1]) in primes:
        count += 1
    if abs(tiles[x, y] - tiles[x + 1, y - 1]) in primes:
        count += 1
    return count


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
