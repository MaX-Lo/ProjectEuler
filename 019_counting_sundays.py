"""
Task:

171 instead of 173 since start is 1901 and end 2001
"""
import time


def main():
    start_time = time.time()

    num_of_sundays = 0

    year = 1900
    month = 1
    days_since_1900 = 1

    while year < 2001:
        print(days_since_1900 % 7)
        if days_since_1900 % 7 == 0:
            num_of_sundays += 1

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            days_since_1900 += 31
        elif month == 2:
            if year % 100 == 0 and year % 400 != 0:
                days_since_1900 += 28
            elif year % 4 == 0:
                days_since_1900 += 29
            else:
                days_since_1900 += 28
        else:
            days_since_1900 += 30
        month += 1

        if month > 12:
            month = 1
            year += 1

    print("sundays:", num_of_sundays)

    print("time:", time.time() - start_time)


if __name__ == '__main__':
    main()

