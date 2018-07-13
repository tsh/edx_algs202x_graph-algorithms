#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [float('Inf') for _ in range(len(adj))]
    dist[s] = 0
    q = queue.PriorityQueue()
    for v, w in enumerate(dist):
        q.put((w, v))
    while not q.empty():
        wvert, vert = q.get()
        for pos, nbr in enumerate(adj[vert]):
            if dist[nbr] > wvert + cost[vert][pos]:
                dist[nbr] = wvert + cost[vert][pos]
                q.put((wvert + cost[vert][pos], nbr))
    return -1 if dist[t] == float('Inf') else dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
