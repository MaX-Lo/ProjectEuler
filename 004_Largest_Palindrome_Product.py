"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


def main():
    print(get_biggest_palindrom())


def get_biggest_palindrom():
    biggest_palindrom = -1
    # assuming a palindrome is guaranteed found between 999x999 and 900x900
    for i in range(999, 900, -1):
        print("progress:", 1000-i, "%")
        for j in range(999, 900, -1):
            if is_palindrome(i*j):
                if i*j > biggest_palindrom:
                    biggest_palindrom = i*j
                else:
                    break
    return biggest_palindrom


def is_palindrome(number):
    text = str(number)
    while len(text) > 1:
        if text[0] == text[-1]:
            text = text[1:-1]
        else:
            return False
    return True


if __name__ == '__main__':
    main()