#Uses python3

import sys
from collections import deque

def bipartite(adj):
    colors = [None] * len(adj)
    colors[0] = True
    q = deque()
    q.append(0)
    while q:
        u = q.popleft()
        for nbr in adj[u]:
            if colors[nbr] is None:
                colors[nbr] = not colors[u]
                q.append(nbr)
            elif colors[nbr] == colors[u]:
                return 0
    return 1

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
    print(bipartite(adj))
