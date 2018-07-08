#Uses python3

import sys


def check_cycle(node, visited, on_stack, graph):
    visited.add(node)
    on_stack.add(node)

    for nbr in graph[node]:
        if nbr not in visited:
            if check_cycle(nbr, visited, on_stack, graph):
                return 1
        if nbr in on_stack:
            return 1
    on_stack.remove(node)
    return 0


def acyclic(adj):
    visited = set()
    on_stack = set()
    for node in range(len(adj)):
        if node not in visited:
            if check_cycle(node, visited, on_stack, adj):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
