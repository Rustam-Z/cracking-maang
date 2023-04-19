"""
https://www.youtube.com/watch?v=pVfj6mxhdMw

Time: O(E + V log V), where E is the number of edges and V is the number of vertices in the graph.
Space: O(V)
"""


import heapq


def dijkstra(graph, start):
    # create a priority queue and add the starting vertex
    queue = [(0, start)]
    # create a dictionary to store the shortest distance from the start to a vertex
    shortest_dist = {start: 0}
    # create a dictionary to store the previous vertex of a vertex on the shortest path
    prev = {}
    # create a set to store visited vertices
    visited = set()

    while queue:
        # pop the vertex with the shortest distance from the queue
        dist, vertex = heapq.heappop(queue)
        # if the vertex has already been visited, continue
        if vertex in visited:
            continue
        # mark the vertex as visited
        visited.add(vertex)
        # for each neighbor of the current vertex
        for neighbor, weight in graph[vertex]:
            # if the neighbor has not been visited yet
            if neighbor not in visited:
                # calculate the distance from the start to the neighbor
                new_dist = dist + weight
                # if the new distance is shorter than the current shortest distance
                if neighbor not in shortest_dist or new_dist < shortest_dist[neighbor]:
                    # update the shortest distance
                    shortest_dist[neighbor] = new_dist
                    # update the previous vertex
                    prev[neighbor] = vertex
                    # add the neighbor to the queue
                    heapq.heappush(queue, (new_dist, neighbor))

    return shortest_dist, prev


# example usage
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('E', 5)],
    'D': [('E', 2)],
    'E': []
}
shortest_dist, prev = dijkstra(graph, 'A')
print(shortest_dist)  # {'A': 0, 'B': 2, 'C': 3, 'D': 3, 'E': 5}
print(prev)  # {'B': 'A', 'C': 'A', 'D': 'B', 'E': 'D'}
