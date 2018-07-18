#Uses python3
import sys
import math


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

def kruskal():
    pass

def minimum_distance(n, x, y):
    result = 0.
    weights = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            w = distance(x[i], y[i], x[j], y[j])
            weights[i][j] = w
            weights[j][i] = w
    return result


if __name__ == '__main__':
    input = """5
0 0
0 2
1 1
3 0
3 2"""
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(n, x, y)))
