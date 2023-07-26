"""
Breadth First Search
    - Starts at any node and explores ALL neighbours first, before moving to the next level of neighbours.

Application of BFS Algorithm
    - The Shortest path on unweighted graph

Time complexity: O(V+E), number vertices and edges
Space complexity: O(V)

https://www.youtube.com/watch?v=oDqjPvD54Ss
https://www.programiz.com/dsa/graph-bfs

"""
from collections import deque


def bfs(graph: dict, start_node: str) -> list:
    traversal = []

    visited = {start_node}  # Set for visited nodes.
    queue = deque([start_node])  # Queue for nodes to visit.

    while queue:
        node = queue.popleft()
        traversal.append(node)  # CUSTOM
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


def test_bfs():
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    expected_result = ['5', '3', '7', '2', '4', '8']
    actual_result = bfs(graph, '5')
    print(actual_result)
    assert actual_result == expected_result
