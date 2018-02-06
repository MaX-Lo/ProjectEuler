"""
Task:


"""
import time


def main():
    start_time = time.time()

    fa = 1
    fb = 1
    i = 2
    while len(str(fb)) < 1000:
        tmp = fb
        fb = fa + fb
        fa = tmp
        i += 1

    print("{}st fibonacci number has over 1000 digits".format(i))
    print("time:", time.time() - start_time)


if __name__ == '__main__':
    main()
