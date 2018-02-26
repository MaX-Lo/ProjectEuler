"""
note:
key is 3 characters long

idea:
frequency analysis - schauen, welche Buchstaben haeufig auftauchen und mit realen auftreten der Buchstaben vergleichen
"""
import operator
import time


def main():
    approach2()


def analysis_approach():
    key_length = 3
    data = read_file('059_cipher.txt')
    print('text length:', len(data))
    print('ord of some letters: e', ord('e'), 't', ord('t'), 'a', ord('a'))

    chifre_txt = str().join([chr(i) for i in data])
    # print('chiffre text:', chifre_txt)
    letter_frequencies = frequency_analysis(data, key_length)
    print(letter_frequencies)
    key = []
    english_language_most_occurring = ord('e')
    for ls in letter_frequencies:
        most_occurring = ls[0][0]
        print(ls[:3])
        key_chr = 101 - most_occurring
        key.append(key_chr)

    # decrypt
    print(key)
    plain_txt = []
    i = 0
    for c in data:
        plain_txt.append(chr(c + key[i]))
        i += 1
        i %= key_length

    plain_str = str().join(plain_txt)
    print(plain_str)


def frequency_analysis(txt, key_length=3):
    """for every char in the key check the letter frequency to obtain
    a possible offset from plaintext"""
    occurrences = [dict() for _ in range(key_length)]
    i = 0
    for char in txt:
        if char in occurrences[i]:
            occurrences[i][char] += 1
        else:
            occurrences[i][char] = 1
        i += 1
        i %= key_length
    return [sorted(occurrences[i].items(), key=operator.itemgetter(1), reverse=True) for i in range(key_length)]


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        tmp = [int(x) for x in line.strip().split(',')]
        data_set.extend(tmp)
    return data_set


def approach2():
    key_length = 3
    data = read_file('059_cipher.txt')
    print(data)
    print('text length:', len(data))
    chifre_txt = str().join([chr(i) for i in data])

    i0, i1, i2 = 97, 97, 97
    while True:
        if i2 > 122:
            i2 = 97
            i1 += 1
        if i1 > 122:
            i1 = 97
            i0 += 1
        if i0 > 122:
            break

        key = [i0, i1, i2]

        pos = 0
        found = True
        for i in range(len(data)):
            encrypted_chr = data[i] ^ key[pos]
            i += 1
            i %= 3
            if not( 32 <= encrypted_chr <= 122) and encrypted_chr!=35 and encrypted_chr!=36:
                found = False
                break
            pos += 1
            pos %= 3
        if found:
            print(key)
        i2 += 1

    for i in range(len(data)):
        if i % 3 == 2:
            data[i] = data[i] ^ 100
        elif i % 3 == 1:
            data[i] = data[i] ^ 111
        else:
            data[i] = data[i] ^ 103
    print(str().join(data))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
