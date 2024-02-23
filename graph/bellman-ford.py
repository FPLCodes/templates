def bellman_ford(n, edges, src):
    dist = [float("Inf")] * n
    dist[src] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            return "Graph contains negative weight cycle"

    return dist
