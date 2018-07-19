#Uses python3
import sys
import math


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))


def minimum_distance(n, x, y):
    result = 0.
    weights = [[0]*n for _ in range(n)]
    adj = [[] for _ in range(n)]
    for i in range(n):
        adj[i] = list(v for v in range(n) if v != i)
        for j in range(n):
            w = distance(x[i], y[i], x[j], y[j])
            weights[i][j] = w
            weights[j][i] = w

    X = set()
    X.add(0)

    while len(X) != n:
        crossing = set()
        for u in X:
            for v in adj[u]:
                if v not in X:
                    crossing.add((u, v))
        edge = sorted(crossing, key=lambda e: weights[e[0]][e[1]])[0]
        result += weights[edge[0]][edge[1]]
        X.add(edge[1])

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(n, x, y)))
