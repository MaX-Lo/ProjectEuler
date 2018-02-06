"""
Task:


"""
import time


def main():
    start_time = time.time()

    data = read_file("022_names.txt")
    print(letter_to_int('A'))

    data.sort()
    print(data)

    score = 0
    i = 1
    for word in data:
        word_score = 0
        for character in word:
            word_score += letter_to_int(character)
        score += word_score * i
        i += 1

    print("score:", score)
    print("time:", time.time() - start_time)


def letter_to_int(character):
    return ord(character) - 64


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
    main()