"""
idea:


"""
import time


def main():
    pass


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip())
    return data_set


def read_txt_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip().split("\",\""))

    data_set = data_set[0]
    data_set[0] = data_set[0][1:]
    data_set[-1] = data_set[-1][:-1]
    return data_set

