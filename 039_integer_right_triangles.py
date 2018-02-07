"""
idea:


"""
import time

import math


def main():

    p_with_max_solutions = -1
    max_solutions = -1

    for perimeter in range(1, 1001):
        print(perimeter)

        wanted_nums = []
        a = 0
        b_and_c = perimeter
        while b_and_c >= a:
            b_and_c -= 1
            a += 1
            for i in range(b_and_c):
                b = i
                c = b_and_c - i
                if b >= a or c >= a:
                    continue

                if is_right_angle_triangle(a, b, c):
                    wanted_nums.append((a, b, c))

        num_solutions = len(wanted_nums) / 2 # every triplet
        if num_solutions > max_solutions:
            p_with_max_solutions = perimeter
            max_solutions = num_solutions

    print("max solutions num:", max_solutions)
    print("p with max solutions:", p_with_max_solutions)


def is_right_angle_triangle(a, b, c):
    hypothenus = -1
    n1 = -1
    n2 = -1
    if a >= b and a >= c:
        hypothenus, n1, n2 = a, b, c
    elif b >= a and b >= c:
        hypothenus, n1, n2 = b, a, c
    elif c >= a and c >= b:
        hypothenus, n1, n2 = c, a, b

    angle1 = math.degrees(math.asin(n1 / hypothenus))
    angle2 = math.degrees(math.asin(n2 / hypothenus))

    angle_3 = 180 - angle1 - angle2

    return math.fabs(90 - angle_3) < 0.0000001


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)