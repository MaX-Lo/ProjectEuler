"""
idea:
"""
import time


def main():
    bouncies = 1

    num = 100
    while True:
        num_str = str(num)
        increasing = False
        decreasing = False
        for i in range(len(num_str)-1):
            if num_str[i] < num_str[i+1]:
                increasing = True
            elif num_str[i] > num_str[i+1]:
                decreasing = True

            if increasing and decreasing:
                bouncies += 1
                break
        num += 1

        ratio = bouncies / num

        if ratio == 0.99:
            print('end num', num)
            break

        if num % 1000 == 0:
            print('num', num, 'ratio', ratio)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
