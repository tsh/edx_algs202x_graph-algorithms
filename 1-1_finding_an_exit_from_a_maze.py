from helpers import process_input


def has_exit(adj_list, frm, to):
    s = []
    visited = set()
    s.extend(adj_list[frm])
    while s:
        v = s.pop()
        if v == to:
            return 1
        if v in visited:
            continue
        s.extend(adj_list[v])
        visited.add(v)
    return 0

if __name__ == '__main__':
    inp = process_input("""4 4
1 2
3 2
4 3
1 4
1 4""") # 1
    print(has_exit(inp.adjacency_list, inp.other[0][0], inp.other[0][1]))