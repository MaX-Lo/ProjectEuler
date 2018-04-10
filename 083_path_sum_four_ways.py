"""
idea:
"""
import time


def main():
    data = read_file('083_matrix.txt')
    shortest_path(data)


def shortest_path(matrix):
    # All nodes where one way to get there is unknown
    nodes = dict()
    unknown_nodes = dict()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            # a nodes structure is: (x, y) = (weight_to_this_node, distance, visited)
            unknown_nodes[(x, y)] = matrix[y][x]
            nodes[(x, y)] = matrix[y][x]

    start_node = (0, 0), unknown_nodes[(0, 0)]
    unknown_nodes.pop((0, 0))
    # All nodes where one way to get there is known
    unvisited_nodes = dict()
    unvisited_nodes[start_node[0]] = start_node[1]

    visited = dict()

    while len(unvisited_nodes) != 0:
        curr = get_next(unvisited_nodes)
        distance = unvisited_nodes[curr]
        unvisited_nodes.pop(curr)
        #print(curr, distance)
        visited[curr] = distance

        cx, cy = curr
        for candidate in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
            # update unvisited nodes
            if candidate in unvisited_nodes:
                maybe_shorter_distance = distance + nodes[candidate]
                if maybe_shorter_distance < unvisited_nodes[candidate]:
                    unvisited_nodes[candidate] = maybe_shorter_distance
            # add former unknown nodes to unvisited nodes
            if candidate in unknown_nodes:
                unvisited_nodes[candidate] = distance + unknown_nodes[candidate]
                unknown_nodes.pop(candidate)

    print(visited)
    x, y = len(matrix)-1, len(matrix[0])-1
    print('shortes:', visited[(x, y)])


def get_next(nodes):
    min_distance = 100000000
    n = -1, -1
    for node in nodes:
        if nodes[node] < min_distance:
            n = node
            min_distance = nodes[node]
    return n


def print_matrix(matrix):
    for line in matrix:
        print(line)


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_line = [int(num) for num in line.strip().split(',')]
        data_set.append(data_line)
    return data_set


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
