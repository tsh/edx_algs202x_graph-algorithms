#Uses python3

import sys

sys.setrecursionlimit(200000)


def transpose(graph):
    gr = [list() for _ in range(len(graph))]
    for v in range(len(graph)):
        for nbr in graph[v]:
            gr[nbr].append(v)
    return gr


def dfs(v, visited, graph):
    visited.add(v)
    for nbr in graph[v]:
        if nbr not in visited:
            dfs(nbr, visited, graph)


def dfs_stack(v, visited, stack, graph):
    visited.add(v)
    for nbr in graph[v]:
        if nbr not in visited:
            dfs_stack(nbr, visited, stack, graph)
    stack.append(v)


def number_of_strongly_connected_components(adj):
    result = 0
    visited = set()
    stack = []
    for v in range(len(adj)):
        if v not in visited:
            dfs_stack(v, visited, stack, adj)

    tg = transpose(adj)
    tvisited = set()
    while stack:
        vert = stack.pop()
        if vert not in tvisited:
            dfs(vert, tvisited, tg)
            result += 1
    return result

if __name__ == '__main__':
    input = """4 4
1 2
4 1
2 3
3 1"""
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
