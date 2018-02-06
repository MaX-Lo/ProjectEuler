"""
Task:


"""
import time


def main():

    n = 1001

    # i=2  n=i*4=8   sum=9  diagonal points= sum+(sum-i)+(sum-2*i)+(sum-3*i)
    total = 1
    diagonal_sum = 1
    for i in range(2, n, 2):
        total += i*4
        diagonal_sum += total + (total-i) + (total - 2*i) + (total - 3*i)

    print("diagonals sum:", diagonal_sum)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
