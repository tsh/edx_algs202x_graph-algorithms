#Uses python3

import sys
from collections import deque

def distance(adj, s, t):
    dist = {v: float('Inf') for v in range(len(adj))}
    dist[s] = 0
    q = deque()
    q.append(s)
    while q:
        u = q.popleft()
        for nbr in adj[u]:
            if dist[nbr] == float('Inf'):
                q.append(nbr)
                dist[nbr] = dist[u] + 1
    return -1 if dist[t] == float('Inf') else dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
