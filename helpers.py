from collections import defaultdict, namedtuple


def process_input(s):
    values = parse(s)
    n, m = values[0]
    edges = values[1:m+1]
    other = values[m+1:]
    adj_list = make_adjacency_list(edges)
    res = namedtuple('Graph', ['vertices', 'edges', 'adjacency_list', 'other'])
    return res(n, m, adj_list, other)


def parse(s):
    s = [tuple(map(int, x.split())) for x in s.split('\n')]
    return s


def make_adjacency_list(items):
    adj = defaultdict(list)
    for u, v in items:
        adj[u].append(v)
    return adj