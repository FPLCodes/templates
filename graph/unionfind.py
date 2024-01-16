# Union by size
def find(u, parent):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u], parent)
    return parent[u]


def union(u, v, parent, size):
    u, v = find(u), find(v)
    if u == v:
        return

    if size[u] > size[v]:
        parent[v] = u
        size[u] += size[v]
    else:
        parent[u] = v
        size[v] += size[u]
