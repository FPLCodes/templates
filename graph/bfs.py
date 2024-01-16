from collections import deque


# Adjacency list
def bfs(graph, src):
    q = deque([src])
    visited = set()
    while q:
        u = q.popleft()
        visited.add(u)

        for v in graph[u]:
            if v not in visited:
                q.append(v)
