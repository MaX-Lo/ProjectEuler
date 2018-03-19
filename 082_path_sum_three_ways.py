"""
idea:
"""
import time
import copy


def main():

    data = read_file('082_matrix.txt')

    for x in range(len(data[0]) - 2, -1, -1):
        tmp_data = copy.deepcopy(data)
        for y in range(len(data)):
            if y == 0:
                tmp_data[y][x] += min(data[y][x+1], data[y+1][x]+data[y+1][x+1])
            elif y == len(data)-1:
                tmp_data[y][x] += min(data[y-1][x]+data[y-1][x+1], data[y][x+1])
            elif y == 1:
                tmp_data[y][x] += min(data[y-1][x]+data[y-1][x+1], data[y][x+1], data[y+1][x]+data[y+1][x+1], data[y+1][x]+data[y+2][x]+data[y+2][x+1])
            elif y == len(data)-2:
                tmp_data[y][x] += min(data[y-1][x]+data[y-1][x+1], data[y-1][x]+data[y-2][x]+data[y-2][x+1], data[y][x+1], data[y+1][x]+data[y+1][x+1])
            else:
                tmp_data[y][x] += min(data[y-1][x]+data[y-1][x+1], data[y-1][x]+data[y-2][x]+data[y-2][x+1], data[y][x+1], data[y+1][x]+data[y+1][x+1], data[y+1][x]+data[y+2][x]+data[y+2][x+1])

        data = copy.deepcopy(tmp_data)

    print_matrix(tmp_data)
    first_row = []
    for line in data:
        first_row.append(line[0])
    print('shortest path sum:', min(first_row))


def print_matrix(matrix):
    for line in matrix:
        print(line)


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_line = [int(num) for num in line.strip().split(',')]
        data_set.append(data_line)
    return data_set


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
