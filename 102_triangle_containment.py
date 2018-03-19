"""
idea:
"""
import time


def main():
    data = read_file('102_triangles.txt')

    count = 0
    #print(contains_origin([-340, 495, -153, -910, 835, -947]))

    for triangle in data:
        print(contains_origin(triangle))
        if contains_origin(triangle):
            count += 1

    print('count:', count)


def contains_origin(points):
    """
    idea: check whether one line is above origin and one line is under
    it if yes the triangle has to contain the origin
    """
    above = False
    under = False

    x1, y1, x2, y2, x3, y3 = points
    t_above, t_under = check_line([x1, y1, x2, y2])
    if t_above:
        above = True
    if t_under:
        under = True
    t_above, t_under = check_line([x1, y1, x3, y3])
    if t_above:
        above = True
    if t_under:
        under = True
    t_above, t_under = check_line([x2, y2, x3, y3])
    if t_above:
        above = True
    if t_under:
        under = True

    return above and under


def check_line(points):
    above = False
    under = False

    if points[0] > points[2]:
        xb, yb = points[0], points[1]
        xs, ys = points[2], points[3]
    else:
        xb, yb = points[2], points[3]
        xs, ys = points[0], points[1]

    if xb >= 0 and xs <= 0:
        m = (yb - ys) / (xb - xs)
        f0 = ys + m * abs(xs)
        if f0 > 0:
            above = True
        elif f0 < 0:
            under = True
        else:
            above = True
            under = True

    return above, under


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        values = [int(x) for x in line.strip().split(',')]
        data_set.append(values)
    return data_set


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
