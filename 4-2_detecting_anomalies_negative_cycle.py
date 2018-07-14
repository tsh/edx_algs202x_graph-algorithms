#Uses python3

import sys


def negative_cycle(adj, cost):
    dist = [9999999999999 for _ in range(len(adj))]
    dist[0] = 0

    for _ in range(len(adj) - 1):
        for vert in range(len(adj)):
            for ni in range(len(adj[vert])):
                neighbor = adj[vert][ni]
                nbr_cost = cost[vert][ni]
                if dist[neighbor] > dist[vert] + nbr_cost:
                    dist[neighbor] = dist[vert] + nbr_cost
    # detect negative
    for vert in range(len(adj)):
        for ni in range(len(adj[vert])):
            neighbor = adj[vert][ni]
            nbr_cost = cost[vert][ni]
            if dist[neighbor] > dist[vert] + nbr_cost:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
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
    print(negative_cycle(adj, cost))
