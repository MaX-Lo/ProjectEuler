"""
idea:
"""
import time


def main():
    cubes_str_list = [str(x**3) for x in range(10000)]
    cubes_dict_ls = generate_cubes_dict(cubes_str_list)

    for i in range(len(cubes_str_list)):

        num_of_matching = 0
        cube_dict = cubes_dict_ls[i]

        for cube in cubes_dict_ls:
            if are_cubes_matching(cube_dict, cube):
                num_of_matching += 1

        if num_of_matching == 5:
            print(cubes_str_list[i])


def are_cubes_matching(cube_dict, cube):
    for digit in '0123456789':
        if cube_dict[digit] != cube[digit]:
            return False
    return True


def generate_cubes_dict(cubes):
    """
    generate a list with a dictionary for every cube, these dictionaries contain how many of each character the number contains
    """
    cubes_dict_ls = []
    for cube in cubes:
        cube_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        for digit in cube:
            cube_dict[digit] += 1
        cubes_dict_ls.append(cube_dict)
    return cubes_dict_ls


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)