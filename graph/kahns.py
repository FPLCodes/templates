from collections import deque
from collections import defaultdict


# Adjacency list
def kahns(graph, incoming, src):
    q = deque([src])
    visited = set()
    order = []
    while q:
        u = q.popleft()
        visited.add(u)
        order.append(u)

        for v in graph[u]:
            if v not in visited:
                incoming[v] -= 1
                if not incoming[v]:
                    q.append(v)

    return order


if __name__ == "__main__":
    # Example graph
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    incoming = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            incoming[v] += 1

    src = "A"
    order = kahns(graph, incoming, src)
    print("Topological Order:", order)
