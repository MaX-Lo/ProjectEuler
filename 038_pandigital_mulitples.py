"""
Task:


"""
import time


def main():

    wanted_nums = []

    for n in range(1, 1000000):
        num_str = ''
        i = 1
        while len(num_str) < 9:
            num_str += str(i * n)
            i += 1
        if len(num_str) == len(set(num_str)) and '0' not in num_str:
            wanted_nums.append(num_str)

    print(wanted_nums)
    print(max(wanted_nums))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
