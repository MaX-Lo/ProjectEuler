"""
idea:
"""
import time


def main():
    limit = 10**6

    inner_layer = 8
    count = 0
    while inner_layer <= limit:
        curr_layer = inner_layer
        used_tiles = inner_layer
        while used_tiles <= limit:
            count += 1
            curr_layer += 8
            used_tiles += curr_layer
        inner_layer += 4
    print('counted:', count)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
