"""
Task:


"""
import time


def main():

    # list containing (numerator, denominator) for searched numbers
    wanted_nums = []

    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            simplified = -1
            if int(str(numerator)[0]) == int(str(denominator)[1]) and int(str(denominator)[0]) != 0:
                simplified = int(str(numerator)[1]) / int(str(denominator)[0])
            elif str(numerator)[1] == str(denominator)[0] and int(str(denominator)[1]) != 0:
                simplified = int(str(numerator)[0]) / int(str(denominator)[1])

            if simplified == (numerator / denominator):
                wanted_nums.append((numerator, denominator))


    print("wanted nums as (numerator, denominator):", wanted_nums)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
