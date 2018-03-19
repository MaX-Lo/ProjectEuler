"""
idea:
"""
import time

import math


def main():

    best_width = 0
    best_height = 0
    best_diff = 2000000

    width = 1
    height = 1
    arrangements = 0
    while arrangements < 2000000:
        width += 1
        arrangements = count_all_arrangements(width, height)
        diff = abs(2000000-arrangements)
        if diff < best_diff:
            best_diff = diff
            best_width = width
            best_height = height

    running = True
    while running:
        if arrangements < 2000000:
            height += 1
            width += 1
        elif arrangements > 2000000:
            width -= 1

        if height > width:
            break

        arrangements = count_all_arrangements(width, height)
        diff = abs(2000000 - arrangements)
        if diff < best_diff:
            best_diff = diff
            best_width = width
            best_height = height
            print('closest diff: {}, {} x {}'.format(best_diff, best_width, best_height))

    print('closest diff: {}, {} x {}'.format(best_diff, best_width, best_height))


def count_all_arrangements(width, height):
    possibilities = 0
    for i in range(1, width + 1):
        for j in range(1, height + 1):
            possibilities += count_arrangements(width, height, i, j)
    return possibilities


def count_arrangements(width, height, sub_w, sub_h):
    """ on how many ways can a sub_w times sub_h rectangle be
    placed in an rectangle of width times height"""

    width_times = width - sub_w + 1
    height_times = height - sub_h + 1

    return width_times * height_times


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
