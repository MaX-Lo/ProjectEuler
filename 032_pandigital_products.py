"""
Task:

idee:

alle möglichen Aufteilungen der Ziffern 1..9 auf 3 Mengen
"""
import time


def main():

    wanted_nums = set()

    for i in range(123456789, 987654322):
        if i % 1000000 == 0:
            print('p:', i)

        if len(set(str(i))) == 9 and '0' not in str(i):
            for len_num1 in range(1, 5):

                for len_num2 in range(1, 6-len_num1):
                    num1 = int(str(i)[:len_num1])
                    num2 = int(str(i)[len_num1:len_num1+len_num2])
                    result = int(str(i)[len_num1+len_num2:])

                    if num1 * num2 == result:
                        print(num1, num2, result)
                        wanted_nums.add(result)

    print(wanted_nums)
    print(sum(wanted_nums))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)