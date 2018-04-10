"""
idea:
"""
import time
import copy


def main():

    data = read_file('082_matrix.txt')

    for x in range(len(data[0]) - 2, -1, -1):
        tmp_data = copy.deepcopy(data)
        for y in range(len(data)): # for every number in the current row
            min_sum = 1000000000000000000000000000
            for i in range(0, y+1): # check all nums above current num and the one right of it
                tmp_sum = data[i][x+1]
                for j in range(i, y+1):
                    tmp_sum += data[j][x]
                if tmp_sum < min_sum:
                    min_sum = tmp_sum
            for i in range(len(data)-1, y, -1): # check all nums under it
                tmp_sum = data[i][x + 1]
                for j in range(i, y-1, -1):
                    tmp_sum += data[j][x]
                if tmp_sum < min_sum:
                    min_sum = tmp_sum
            tmp_data[y][x] = min_sum

        data = copy.deepcopy(tmp_data)

    print_matrix(data)
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
