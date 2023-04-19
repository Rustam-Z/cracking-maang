"""
Depth First Search
    - Starts at any node and plunges a depth first into a graph (like a snake), until it cannot go any further
    - At point it can't go any further it backtracks and continues

Application of DFS Algorithm
    - For finding the path
    - To test if the graph is bipartite
    - For finding the strongly connected components of a graph
    - For detecting cycles in a graph

Time complexity: O(V+E), number vertices and edges
Space complexity: O(V)

https://www.youtube.com/watch?v=7fujbpJ0LB4
https://www.programiz.com/dsa/graph-dfs
"""
import pytest

traversal = []


def dfs_version1(graph, node, visited=None):
    if visited is None:
        visited = set()  # Or even you can use an array of booleans.

    # Mark the current node as visited
    visited.add(node)
    traversal.append(node)

    # Recursion for all the vertices adjacent to this vertex
    for child in graph[node]:
        if child not in visited:
            dfs_version1(graph, child, visited)


def dfs_version2(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        # print(node, end=" ")
        traversal.append(node)
        visited.add(node)

        for neighbour in graph[node]:  # graph[node] - visited
            dfs_version2(graph, neighbour, visited)


def test_dfs_version1():
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': [],
    }
    expected_result = ['5', '3', '2', '4', '8', '7']

    traversal.clear()
    dfs_version1(graph, '5')
    assert expected_result == traversal


def test_dfs_version2():
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': [],
    }
    expected_result = ['5', '3', '2', '4', '8', '7']

    traversal.clear()
    dfs_version2(graph, '5')
    assert expected_result == traversal
