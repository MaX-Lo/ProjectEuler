"""
Task:


"""
import time


def main():
    start_time = time.time()

    digit_sum = 0

    for i in range(1, 10):
        digit_sum += digit_word_len(i)
    sum_of_1_to_9 = digit_sum

    for i in range(10, 20):
        digit_sum += teen_word_len(i)

    for i in range(20, 100):
        tenth = i // 10 * 10
        digit = i % 10
        digit_sum += ten_word_len(tenth) + digit_word_len(digit)

    one_to_ninetynine_sum = digit_sum

    digit_sum = one_to_ninetynine_sum * 10 + 100 * sum_of_1_to_9 + 900 * len("hundred") + (900-9) * len("and") + len("onethousand")

    print(digit_sum)
    print("time:", time.time() - start_time)


def ten_word_len(tenth):
    """ word length for 20, 30, 40, ..., 90"""
    if tenth == 20:  # twenty
        return 6
    elif tenth == 30:  # thirty
        return 6
    elif tenth == 40:  # forty
        return 5
    elif tenth == 50:  # fifty
        return 5
    elif tenth == 60:  # sixty
        return 5
    elif tenth == 70:  # seventy
        return 7
    elif tenth == 80:  # eighty
        return 6
    elif tenth == 90:  # ninety
        return 6


def teen_word_len(teen):
    if teen == 10:
        return len("ten")
    elif teen == 11:
        return len("eleven")
    elif teen == 12:
        return len("twelve")
    elif teen == 13:
        return len("thirteen")
    elif teen == 14:
        return len("fourteen")
    elif teen == 15:
        return len("fifteen")
    elif teen == 16:
        return len("sixteen")
    elif teen == 17:
        return len("seventeen")
    elif teen == 18:
        return len("eighteen")
    elif teen == 19:
        return len("nineteen")


def digit_word_len(digit):
    if digit == 0:
        return 0
    elif digit == 1:  # one
        return 3
    elif digit == 2:  # two
        return 3
    elif digit == 3:  # three
        return 5
    elif digit == 4:  # four
        return 4
    elif digit == 5:  # five
        return 4
    elif digit == 6:  # six
        return 3
    elif digit == 7:  # seven
        return 5
    elif digit == 8:  # eight
        return 5
    elif digit == 9:  # nine
        return 4


if __name__ == '__main__':
    main()
