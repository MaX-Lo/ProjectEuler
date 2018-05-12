"""
idea:
1) alle Anagram-Paare herausfinden
2) fuer jedes Paar aller Ersetzungen (0..9) testen

2 neu) statt alle Ersetzungen zu testen:
        - Liste mit allen Quadratzahlen bis zur Länge des längsten Wortes
        - nur die entsprechenden Quadratzahlen bei der 2. Zahl testen
"""
import time

import math


def main():
    largest = 0

    data = read_file('098_words.txt')
    print("max len", max([len(x) for x in data]))
    print(data)

    # generate a dictionary with lists of squares for every length up to max_square (1000000000000)
    # e.g.: {1: [1, 4, 9], 2: [16, 25, 36, 49, 64, 81], ...}
    squares = generate_square_dict(1000000000000)

    # create dict with letter count for every word
    data_occurrences = []
    for word in data:
        t = word, count_character_occurrences(word)
        data_occurrences.append(t)

    # find all anagramic pairs
    pairs = []
    for i in range(len(data_occurrences)):
        word1, occurrences1 = data_occurrences[i]
        for j in range(i+1, len(data_occurrences)):
            word2, occurrences2 = data_occurrences[j]
            if occurrences1 == occurrences2:
                pairs.append((word1, word2)) #, occurrences1))
    print("pairs:", pairs)

    for word1, word2 in pairs:
        for square in squares[len(word1)]:

            if not is_isomorphism(word1, str(square)):
                continue
            #print('is iso:', word1, str(square), is_isomorphism(word1, str(square)))

            sqr_str = str(square)
            mapping = dict()
            for i in range(len(word1)):
                mapping[word1[i]] = sqr_str[i]

            tmp2 = word2
            for letter in mapping:
                tmp2 = tmp2.replace(letter, mapping[letter])

            num = int(tmp2)
            # catch leading zeroes resulting in shorter strings
            if len(str(num)) != len(sqr_str):
                continue

            if math.sqrt(num) % 1 == 0:
                print('found:', word1, word2, 'with values:', square, num)
                larger = max(math.sqrt(square), num)
                if larger > largest:
                    largest = larger

    # for word1, word2, occurrences in pairs:
    #     print('current pair:', word1)
    #     tmp_largest = is_square_anagram(word1, word2, occurrences)
    #     if tmp_largest > largest:
    #         largest = tmp_largest

    print("largest found:", largest)


def is_isomorphism(str1, str2):
    """
    return true if a mapping (isomorphism) exists
    e.g. 12334, hello is true because 1->h, 2->e, 3->l, 4->o
    """
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        for j in range(i+1, len(str2)):
            if str1[j] == c1 and str2[j] != c2:
                return False
    for i in range(len(str2)):
        c2 = str2[i]
        c1 = str1[i]
        for j in range(i+1, len(str1)):
            if str2[j] == c2 and str1[j] != c1:
                return False
    return True


def generate_square_dict(max_square):
    # create empty dict with lists
    squares = dict()
    for i in range(1, len(str(max_square)) + 1):
        squares[i] = list()

    x = 1
    while x ** 2 <= max_square:
        sqr = x ** 2
        squares[len(str(sqr))].append(sqr)
        x += 1
    return squares


def is_square_anagram(word1: str, word2: str, occurrences: dict):
    largest = 0

    length = len(set(word1))

    replace_pattern = 10 ** (length-1)

    while len(str(replace_pattern)) == length:
        if len(set(str(replace_pattern))) < length:
            replace_pattern += 1
            continue
        replace_str = str(replace_pattern)

        k = 0
        t1 = word1
        t2 = word2
        for letter in occurrences:
            t1 = t1.replace(letter, replace_str[k])
            t2 = t2.replace(letter, replace_str[k])
            k += 1

        num1 = int(t1)
        num2 = int(t2)

        # catch case with leading zero
        if len(str(num1)) != len(str(num2)):
            replace_pattern += 1
            continue

        if is_square_num(num1) and is_square_num(num2):
            s1 = math.sqrt(num1)
            s2 = math.sqrt(num2)
            if max(s1, s2) > largest:
                largest = max(s1, s2)
        replace_pattern += 1

    print('largest:', largest)
    return int(largest)


square_nums = set(x**2 for x in range(10000000))
def is_square_num(num):
    return num in square_nums or math.sqrt(num) % 1 == 0


def count_character_occurrences(word):
    occurrences = dict()
    for c in word:
        if c not in occurrences:
            occurrences[c] = 1
        else:
            occurrences[c] += 1
    return occurrences


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.replace("\"", "").split(','))
    return data_set[0]


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
