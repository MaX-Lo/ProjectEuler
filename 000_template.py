"""
Task:


"""
import time


def main():
    start_time = time.time()

    print("time:", time.time() - start_time)


if __name__ == '__main__':
    main()


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip())
    return data_set
