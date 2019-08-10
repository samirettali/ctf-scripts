#!/usr/bin/env python3
from sys import argv
from sys import maxsize
from dijkstra import dijkstra, shortest_path


def read_file(filename):
    graph = {}
    f = open(filename, 'r') 

    for line in f.readlines():
        origin, destination = line.split(' -> ')
        destination = destination.replace('\n', '')
        if origin in graph.keys():
            graph[origin][destination] = maxsize
        else:
            graph[origin] = {destination: maxsize}

    return graph


# def dijkstra(graph, origin):
#     for v in graph:
    
#     location = origin
#     path = location
#     while location != destination:
#         location = graph[destination]
#         path += location
#     return path

def main():
    if len(argv) != 2:
        print('Usage: ./%s <file>' % argv[0])
        exit(1)

    graph = read_file(argv[1])
    dist, pred = dijkstra(graph, start='A')
    print(shortest_path(graph, 'A', 'Z'))
    # print(find_path(graph, 'A', 'Z'))

if __name__ == '__main__':
    main()
