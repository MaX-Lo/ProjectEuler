"""
idea:
"""
import time


def main():
    # lists containing 4-digit polygonal numbers as strings
    triangles = generate_figurate_nums(1000, 10000, triangle)
    squares = generate_figurate_nums(1000, 10000, square)
    pentagonals = generate_figurate_nums(1000, 10000, pentagonal)
    hexagonals = generate_figurate_nums(1000, 10000, hexagonal)
    heptagonals = generate_figurate_nums(1000, 10000, heptagonal)
    octagonals = generate_figurate_nums(1000, 10000, octagonal)

    # for every number in squares:
    #   - check in other polygonal lists for numbers beginning with
    #     the last two digits of this square number
    #   - repeat that 5 times
    # all in all that should be some recursion algorithm
    lists_to_check_in = [squares, pentagonals, hexagonals, heptagonals, octagonals]
    for current_num in triangles:
        first_num = current_num
        last_two = first_num[-2:]

        for polygonal_list in lists_to_check_in:
            for next_num in polygonal_list:
                first_two = next_num[:2]
                if first_two == last_two:
                    new_to_check_list = list(lists_to_check_in)
                    new_to_check_list.remove(polygonal_list)
                    ist, elements = is_cyclic(first_num, next_num, new_to_check_list)
                    elements = list(elements)
                    elements.insert(0, first_num)
                    if ist:
                        print(elements)
                        print('sum:', sum([int(ele) for ele in elements]))


def is_cyclic(first_num, current_num, lists_to_check_in):

    # recursion termination condition
    if len(lists_to_check_in) == 0:
        last_two = current_num[-2:]
        first_two = first_num[:2]
        cyclic = last_two == first_two
        if cyclic:
            print('cyclic, start num:', first_num)
            return True, [current_num]
        else:
            return False, [current_num]

    # recursive check elements in remaining polygonal lists
    last_two = current_num[-2:]
    for polygonal_list in lists_to_check_in:
        for next_num in polygonal_list:
            first_two = next_num[:2]
            if first_two == last_two:
                new_to_check_list = list(lists_to_check_in)
                new_to_check_list.remove(polygonal_list)
                ist, elements = is_cyclic(first_num, next_num, new_to_check_list)

                if ist:
                    elements.insert(0, current_num)
                    return ist, elements

    return False, []


def triangle(n):
    return n * (n + 1) / 2


def square(n):
    return n**2


def pentagonal(n):
    return n*(3*n-1)/2


def hexagonal(n):
    return n*(2*n-1)


def heptagonal(n):
    return n*(5*n-3)/2


def octagonal(n):
    return n*(3*n-2)


def generate_figurate_nums(n_min, n_max, func):
    nums = []
    n = 0
    i = 1
    while func(i) < n_max:
        n = func(i)
        if n >= n_min: # Todo n_min:
            nums.append(str(int(n)))
        i += 1
    return nums


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)