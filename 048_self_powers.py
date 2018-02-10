"""
idea:


"""
import time


def main():
    result = 0
    for i in range(1, 1001):
        result += i**i

    res_str = str(result)
    print(res_str[-10:])


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
