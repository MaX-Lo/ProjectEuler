"""
idea:

17526*10^9 = (n*(n+1))/2 solved by n is:
n = 5920473
"""
import time
import threading

import math


def main():
    g = 1000

    variant1(g)


def get_triangular_nums(g):
    tri_ls = [0, 1, 3]
    num = 3
    n = 3
    while num+n <= g:  # 17526000000000:
        num += n
        n += 1
        tri_ls.append(num)

    return tri_ls


def variant1(g):
    parallel = False # 103sec, 93sec,

    # old 10^8 11,71sec count 25812
    count = 0

    tri_ls = get_triangular_nums(g)
    tri_set = set(tri_ls)
    print("lists created start running... ({}sec)".format(time.time()-start_time))

    fi = 0
    si = 0
    finished = False

    limit = len(tri_ls) - 1
    limit2 = int(math.floor(g/2))

    if not parallel:
        while not finished:
            first = tri_ls[fi]
            if first >= limit2:
                break
            diff = g - first

            while si <= fi:
                second = tri_ls[si]
                third = diff - second
                #print(first, second, third)

                if first > third:
                    break

                if third in tri_set:
                    progress = round(100 - (diff - first)*100/g, 3)
                    if progress * 100000 > 1:
                        print("{}%, {}sec".format(progress, round(time.time()-start_time)))

                    if first == second == third:
                        count += 1
                    elif first == second or first == third or second == third:
                        count += 3
                    else:
                        count += 6
                si += 1

            si = 0
            fi += 1
        print("g:", g, "counted:", count)

    if parallel:
        limit1 = int(math.ceil(limit / 4))
        t1 = threading.Thread(threaded(0, 0, limit1, tri_ls, tri_set, g))
        t1.start()
        limit2 = int(math.ceil(limit * 3 / 4))
        t2 = threading.Thread(threaded(limit1 + 1, 0, limit2, tri_ls, tri_set, g))
        t2.start()
        t3 = threading.Thread(threaded(limit2 + 1, 0, limit, tri_ls, tri_set, g))
        t3.start()


def threaded(fi, si, limit, tri_ls, tri_set, g):
    count = 0
    finished = False

    limit2 = int(math.floor(g/2))
    while not finished:
        first = tri_ls[fi]
        if first >= limit2:
            break
        diff = g - first

        while si <= fi:
            second = tri_ls[si]

            third = diff - second
            if first > third:
                break

            if third in tri_set:
                #print(100 - (diff - first)*100/g, "%")

                if first == second == third:
                    count += 1
                elif first == second or first == third or second == third:
                    count += 3
                else:
                    count += 6
            si += 1

        si = 0
        fi += 1

    print("lim:", limit, "counted:", count)


def variant2():
    g = 1000  # 17526000000000
    count = 0
    # 7,75 and 834

    tris = get_triangular_nums(g)
    print(tris)
    m = len(tris)-1
    limit1 = int(math.ceil(g / 3))
    limit2 = int(math.ceil(g / 3))

    finished = False
    while not finished:
        n = 0
        tmp = tris[m] + tris[n]
        while tmp <= g:
            o = 0
            tmp = tris[m] + tris[n]
            res = tmp
            while res < g:

                res = tmp + tris[o]
                if res > g:
                    break

                if res == g:
                    if m == n == o:
                        count += 1
                    elif m == n or m == o or n == o:
                        count += 3
                    else:
                        count += 6
                o += 1
                if tris[o] > tris[m]:
                    break
            n += 1
            if tris[n] > limit2:
                break

        m -= 1
        if tris[m] < limit1:
            break
    print("counted:", count)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
