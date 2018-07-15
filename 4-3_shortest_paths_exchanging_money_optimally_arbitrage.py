#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    reachable[s] = ''
    prev = [None] * len(adj)
    last_relax = None
    # Bellman-Ford
    for _ in range(len(adj) - 1):
        for vert in range(len(adj)):
            for npos in range(len(adj[vert])):
                neighbor = adj[vert][npos]
                weight = cost[vert][npos]
                if distance[neighbor] > distance[vert] + weight:
                    distance[neighbor] = distance[vert] + weight
                    reachable[neighbor] = distance[vert] + weight
                    last_relax = neighbor
                    prev[neighbor] = vert
    # negative cycle
    for _ in range(len(adj)):
        x = prev[last_relax]
    shortest[x] = 0  # cycle start
    y = x
    x = prev[x]
    while y != x:
        shortest[x] = 0
        x = prev[x]


if __name__ == '__main__':
    input = """6 7
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1
1"""
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

