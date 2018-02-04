"""
Task:


"""
import time


def main():
    start_time = time.time()

    numbers = read_file("013_numbers.txt")

    sum = 0
    for num in numbers:
        sum += int(num)

    print("full sum:", sum)

    print("time:", time.time() - start_time)


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip())
    return data_set


if __name__ == '__main__':
    main()
