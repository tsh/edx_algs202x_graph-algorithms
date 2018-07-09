#Uses python3

import sys


def toposort(adj):
    result = []
    visited = set()

    def dfs(node):
        if node in visited:
            return
        for nbr in adj[node]:
            dfs(nbr)
        visited.add(node)
        result.append(node)

    for v in range(len(adj)):
        if v not in visited:
            dfs(v)

    return result[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

