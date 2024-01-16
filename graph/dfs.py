# Adjacency list
def dfs(graph, u, visited):
    visited.add(u)

    for v in graph[u]:
        if v not in visited:
            dfs(graph, v, visited)
