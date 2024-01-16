# Adjacency list
import heapq


def dijkstra(graph, start, end=None):
    heap = [(0, start)]
    dist = {}
    while heap:
        d, u = heapq.heappop(heap)
        if u in dist:
            continue

        dist[u] = d
        if u == end:
            break
        for v, w in graph[u]:
            if v not in dist:
                heapq.heappush(heap, (d + w, v))

    return dist


if __name__ == "__main__":
    graph = {
        "A": [("B", 5), ("C", 3)],
        "B": [("A", 5), ("C", 2), ("D", 1)],
        "C": [("A", 3), ("B", 2), ("D", 4), ("E", 2)],
        "D": [("B", 1), ("C", 4), ("E", 1)],
        "E": [("C", 2), ("D", 1)],
    }

    start_node = "A"
    end_node = "E"

    result = dijkstra(graph, start_node, end_node)
    print(result)
