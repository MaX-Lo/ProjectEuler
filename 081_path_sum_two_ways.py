"""
idea:
"""
import time


def main():
    data = read_file('081_matrix.txt')
    matrix_size = len(data)

    matrix = data
    for i in range(matrix_size):
        matrix[i].append(1000000)
    matrix.append([1000000 for x in range(matrix_size+1)])

    print('before modifying:')
    print_matrix(matrix)

    for index_sum in range((matrix_size-1)*2 - 1, -1, -1):
        x = index_sum
        y = 0
        while y <= matrix_size-1 and x >= 0:
            if x > matrix_size-1:
                x -= 1
                y += 1
                continue

            # print('index sum:', index_sum, x, y)
            data[x][y] += min(data[x][y+1], data[x+1][y])
            x -= 1
            y += 1
        # print('---')

    print('after modifying:')
    print_matrix(matrix)
    print('minimal path', data[0][0])


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