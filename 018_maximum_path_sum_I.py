"""
Task:

solution for 018 as well as for 067

idea: build up from down

"""
import time


def main():
    start_time = time.time()

    data = read_file("067_triangle.txt") # "018_data.txt"
    tree = []
    for layer in data:
        tree.append(list(map(int, layer)))

    while len(tree) > 1:
        tree = sum_up_last_layer(tree)

    print("maximum path sum:", tree[0][0])

    print("time:", time.time() - start_time)


def sum_up_last_layer(tree: list):
    depth = len(tree) - 1
    for i in range(depth):
        if tree[depth][i] > tree[depth][i+1]:
            tree[depth-1][i] += tree[depth][i]
        else:
            tree[depth-1][i] += tree[depth][i+1]
    tree.remove(tree[depth])
    return tree


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip().split())
    return data_set


if __name__ == '__main__':
    main()
