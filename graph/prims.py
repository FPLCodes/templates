import heapq


def prims(graph, src):
    heap = [(0, src)]
    visited = set()
    total = 0
    while len(visited) != len(graph):
        d, u = heapq.heappop(heap)

        visited.add(u)
        total += d

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(heap, (w, v))

    return total


if __name__ == "__main__":
    graph = {
        "A": [("B", 2), ("C", 3)],
        "B": [("A", 2), ("C", 4), ("D", 1)],
        "C": [("A", 3), ("B", 4), ("D", 2)],
        "D": [("B", 1), ("C", 2)],
    }

    source_node = "A"
    minimum_spanning_tree_cost = prims(graph, source_node)
    print(f"Minimum Spanning Tree Cost: {minimum_spanning_tree_cost}")
