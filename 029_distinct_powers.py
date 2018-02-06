"""
Task:


"""
import time


def main():

    terms = set()

    for a in range(2, 101):
        for b in range(2, 101):
            terms.add(a**b)

    print("terms in sequence:", len(terms))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
