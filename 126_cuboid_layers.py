"""
idea:
"""
import time


def main():
    approach_2()


def solution():
    limit = 2000
    wanted_occurences = 1000
    h, b, d = 1, 1, 1

    c_dict = dict()
    ind = 1
    while True:
        b += 1
        if b > d:
            b = 1
            d += 1
        if d > h:
            d = 1
            h += 1

        if ind % 100000 == 0:
            print('ind', ind, 'max', max(c_dict.values()))
        ind += 1


        if get_surface_area((h, b, d)) > limit:
            if b and d == 1: # at this point is clear that no larger cuboids with layers having < limit cuboids exist
                break
            else:
                continue

        # print('h, b, d', h, b, d)

        layer = 1
        cuboids = get_layer_cuboids((h, b, d), layer)
        last_layer_cuboids_half = b*d
        last_layer_cuboids_mid_slice = 0 #2*b + 2*d

        while cuboids < limit:
            cuboids_mid_slice = 2*b + 2*d + (layer-1)*4
            cuboids_half = last_layer_cuboids_half + last_layer_cuboids_mid_slice

            cuboids = h * cuboids_mid_slice + 2 * cuboids_half
            # print('cuboids', cuboids)
            last_layer_cuboids_mid_slice = cuboids_mid_slice
            last_layer_cuboids_half = cuboids_half

            if cuboids in c_dict:
                c_dict[cuboids] += 1
                if c_dict[cuboids] == wanted_occurences:
                    print(c_dict)
            else:
                c_dict[cuboids] = 1

            layer += 1

    print(c_dict)
    print('max occurence count', max(c_dict.values()))


def get_layer_cuboids(cuboid, layer):
    # height, breath, depth
    h, b, d = cuboid
    cuboids = 2 * (b*d)

    for slice_num in range(1, layer):
        cuboids += 2 * (2*b + 2*d + (slice_num-1)*4)

    cuboids += h * (2*b + 2*d + (layer-1)*4)
    return cuboids


def get_surface_area(cuboid):
    # height, breath, depth
    h, b, d = cuboid
    return (h*b*2) + (h*d*2) + (b*d*2)


def approach_2():
    limit = 30000
    wanted_ocurences = 1000

    c_dict = {x: 0 for x in range(1, limit + 1)}

    h, b, d = 1, 1, 1
    while count_cuboids(h, h, h, 1) <= limit:
        b = h
        while count_cuboids(h, b, h, 1) <= limit:
            d = b
            while count_cuboids(h, b, d, 1) <= limit:
                n = 1
                while count_cuboids(h, b, d, n) <= limit:
                    c_dict[count_cuboids(h, b, d, n)] += 1
                    n += 1
                d += 1
            b += 1
        h += 1

    print('max occurence count', max(c_dict.values()))
    print(c_dict)
    thousands = []
    for key in c_dict:
        if c_dict[key] == wanted_ocurences:
            thousands.append(key)
    thousands.sort()
    print(thousands)


def count_cuboids(b, d, h, layer):
    return 2*(b*d + b*h + d*h) + 4*(b+d+h+layer-2) * (layer - 1)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
