"""
idea:
"""
import time

from copy import deepcopy


def main():
    edges = read_file('107_network.txt')
    for y in range(len(edges)):
        for x in range(len(edges[0])):
            if edges[y][x] == '-':
                edges[y][x] = -1
            else:
                edges[y][x] = int(edges[y][x])

    unoptimized_sum = get_edges_sum(edges)

    vertices_count = len(edges[0])

    # contains already visited vertices
    visited = {0}
    # format eg.: (index_x, Y)
    minimal_edges = list()

    # - find next unknown vertex with shortest distance to a already known vertices
    # - add that vertex to visited and deleted all edges from that vertex to visited vertices which haven't the
    #   shortest distance to that vertex
    # - repeat until all vertices have been visited, remaining edges form a minimal network
    while len(visited) < vertices_count:
        start_vertex, nearest_vertex = find_nearest_unvisited_vertex(edges, visited)
        visited.add(nearest_vertex)

        # remove unnecessary edges between visited vertices
        for vertex in range(len(edges)):
            if vertex != start_vertex and vertex in visited:
                edges[nearest_vertex][vertex] = -1
                edges[vertex][nearest_vertex] = -1

    for line in edges:
        print(line)

    optimized_sum = get_edges_sum(edges)
    print('old:', unoptimized_sum, 'new:', optimized_sum, 'diff:', unoptimized_sum - optimized_sum)


def find_nearest_unvisited_vertex(edges, visited):
    minimal_distance = -1
    nearest_start_vtx = -1
    nearest_end_vtx = -1
    for start_vtx in range(len(edges)):
        if start_vtx not in visited:
            continue

        for end_vtx in range(len(edges)):
            distance = edges[start_vtx][end_vtx]
            if end_vtx in visited:
                continue
            if (distance < minimal_distance and distance != -1) or minimal_distance == -1:
                minimal_distance = distance
                nearest_start_vtx = start_vtx
                nearest_end_vtx = end_vtx

    print(nearest_start_vtx, nearest_end_vtx, minimal_distance)
    return nearest_start_vtx, nearest_end_vtx


def get_edges_sum(edges):
    tmp = deepcopy(edges)
    res = 0
    for v1 in range(len(tmp)):
        for v2 in range(len(tmp)):
           if tmp[v1][v2] == -1:
               continue
           else:
               res += tmp[v1][v2]
               tmp[v2][v1] = -1
    return res


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip().split(','))
    return data_set


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:", time.time() - start_time)
