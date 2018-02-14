"""
idea:


"""
import time


def main():
    t = time.time()
    pandigitals = get_pandigital_numbers()
    print("time for generating pandigitals", time.time() - t)

    len_pandigitals = len(pandigitals)
    i = 0
    print("num of pandigital nums:", len_pandigitals)

    wanted_nums = []

    for num in pandigitals:
        i += 1
        if i % 10000 == 0:
            print(i/len_pandigitals)

        num_str = str(num)
        if int(num_str[1:4]) % 2 != 0:
            continue
        if int(num_str[2:5]) % 3 != 0:
            continue
        if int(num_str[3:6]) % 5 != 0:
            continue
        if int(num_str[4:7]) % 7 != 0:
            continue
        if int(num_str[5:8]) % 11 != 0:
            continue
        if int(num_str[6:9]) % 13 != 0:
            continue
        if int(num_str[7:10]) % 17 != 0:
            continue

        wanted_nums.append(num)

    print(wanted_nums)
    print(sum(int(num) for num in wanted_nums))


def get_pandigital_numbers():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # digits = ['0', '1', '2']

    pandigital_numbers = []
    for digit in digits:
        new_num = digit
        new_digits = list(digits)
        new_digits.remove(digit)
        pandigital_numbers.extend(f(new_num, new_digits))
    return pandigital_numbers


def f(num, digits: list):
    if len(digits) == 1:
        return [num+digits[0]]
    else:
        ls = []
        for digit in digits:
            new_digits = list(digits)
            new_digits.remove(digit)
            new_num = num + digit
            ls.extend(f(new_num, new_digits))
        return ls


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)