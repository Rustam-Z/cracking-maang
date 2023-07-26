"""
Dijkstra algorithm is used to find the shortest path from a vertex to all other vertices in a weighted graph.
It is a greedy algorithm.

Algorithm:
    - Visited and unvisited.
    - We will use priority queue, to fetch the vertex with the shortest distance on every iteration. This is how Dijsktra works.
    - We will use a dictionary to store the shortest distance from the start to a vertex.
    - We will use a dictionary to store the previous vertex of a vertex on the shortest path. Not to recalculate the path.
      Ex: path from A to E is A -> B -> C -> D -> E. We will store the previous vertex of E, which is D. Because distance till D is already shortest.

Time complexity: O(E * logV), where E is the number of edges and V is the number of vertices in the graph.
Space complexity: O(V)

https://www.youtube.com/watch?v=pVfj6mxhdMw
"""

import heapq


def dijkstra(graph, start):
    queue = [(0, start)]  # Heap to store the vertex with the shortest distance from the start. Similar to BFS.
    # We need queue, because we need to pop the smallest every time that is not visited. We can also use shortest_dist dict.
    # But it will be slower to select the smallest out of not visited.
    shortest_dist = {start: 0}  # Dictionary to store the shortest distance from the start to a vertex.
    prev = {}  # Children points to parent.
    visited = set()

    while queue:
        dist, vertex = heapq.heappop(queue)  # Pop the vertex with the shortest distance from the queue.

        if vertex in visited:  # If the vertex has been visited, skip it.
            continue

        visited.add(vertex)  # Mark the vertex as visited, look that only parent node is added.

        # For each neighbor of the current vertex.
        for neighbor, weight in graph[vertex]:
            # If the neighbor has not been visited yet...
            if neighbor not in visited:
                # ... calculate the distance from the start to the neighbor.
                new_dist = dist + weight
                # ... if the new distance is shorter than the current shortest distance.
                if neighbor not in shortest_dist or new_dist < shortest_dist[neighbor]:
                    shortest_dist[neighbor] = new_dist  # ... update the shortest distance.
                    prev[neighbor] = vertex  # ... update the previous vertex.
                    heapq.heappush(queue, (new_dist, neighbor))  # add the neighbor to the queue.

    return shortest_dist, prev


if __name__ == "__main__":
    adjacency_list = {
        'A': [('B', 2), ('C', 3)],
        'B': [('D', 1), ('E', 4)],
        'C': [('E', 5)],
        'D': [('E', 2)],
        'E': []
    }
    shortest_dist, prev = dijkstra(adjacency_list, 'A')
    print(shortest_dist)  # {'A': 0, 'B': 2, 'C': 3, 'D': 3, 'E': 5}
    print(prev)  # {'B': 'A', 'C': 'A', 'D': 'B', 'E': 'D'}
