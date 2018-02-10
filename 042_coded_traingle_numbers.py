"""
idea:


"""
import time


def main():
    data = read_file('042_words.txt')

    longest_word = max(len(word) for word in data)
    largest_needed_number = 26 * longest_word

    triangle_nums = set(triangle_numbers(largest_needed_number))

    triangle_word_count = 0
    for word in data:
        if get_word_sum(word) in triangle_nums:
            triangle_word_count += 1

    print("num of triangle words:", triangle_word_count)
    print(triangle_nums)


def triangle_numbers(limit):
    nums = []

    num = -1
    i = 1
    while num < limit:
        num = (i**2 + i) / 2
        nums.append(int(num))
        i += 1

    return nums


def get_word_sum(word):
    word_sum = 0
    for char in word:
        word_sum += ord(char) - 64
    return word_sum


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip().split("\",\""))

    data_set = data_set[0]
    data_set[0] = data_set[0][1:]
    data_set[-1] = data_set[-1][:-1]
    return data_set


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
