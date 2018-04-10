"""
idea:
"""
import time


def main():
    romans = read_file('089_roman.txt')
    old_length = 0
    new_length = 0
    for num in romans:
        old_length += len(num)
        latin = roman_to_latin(num)
        new_roman = latin_to_roman(latin)
        new_length += len(new_roman)

    print('old:', old_length, 'new:', new_length, 'diff:', old_length - new_length)


def latin_to_roman(num):
    used_D = False
    used_L = False
    used_V = False

    roman = []

    while num - 1000 >= 0:
        roman.append('M')
        num -= 1000

    if num - 900 >= 0:
        roman.append('CM')
        num -= 900

    if num >= 500:
        roman.append('D')
        used_D = True
        num -= 500

    if num >= 400 and not used_D:
        roman.append('CD')
        num -= 400

    while num >= 100:
        roman.append('C')
        num -= 100

    if num >= 90:
        roman.append('XC')
        num -= 90

    if num >= 50:
        roman.append('L')
        used_L = True
        num -= 50

    if num >= 40 and not used_L:
        roman.append('XL')
        num -= 40

    while num >= 10:
        roman.append('X')
        num -= 10

    if num >= 9:
        roman.append('IX')
        num -= 9

    if num >= 5:
        roman.append('V')
        used_V = True
        num -= 5

    if num >= 4 and not used_V:
        roman.append('IV')
        num -= 4

    while num >= 1:
        roman.append('I')
        num -= 1

    return ''.join(roman)


def roman_to_latin(roman):
    nums = []
    for digit in roman:
        nums.append(rom_digit_to_num(digit))

    res = 0
    for i in range(len(nums)):
        if i < len(nums) - 1 and nums[i] < nums[i+1]:
            res -= nums[i]
        else:
            res += nums[i]

    return res


def rom_digit_to_num(rom_digit):
    if rom_digit == 'I':
        return 1
    elif rom_digit == 'V':
        return 5
    elif rom_digit == 'X':
        return 10
    elif rom_digit == 'L':
        return 50
    elif rom_digit == 'C':
        return 100
    elif rom_digit == 'D':
        return 500
    elif rom_digit == "M":
        return 1000


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip())
    return data_set


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
