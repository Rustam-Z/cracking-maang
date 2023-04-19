"""797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/

Given the array showing the edges of DAGs. Create all paths.

Example:
    graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
"""

from collections import deque
from typing import List


# BFS Solution
def allPathsSourceTargetBFS(graph: List[List[int]]) -> List[List[int]]:
    result = []
    dq = deque([(0, [0])])
    target = len(graph) - 1
    while dq:
        cur, route = dq.popleft()
        if cur == target:
            result.append(route)
        else:
            for node in graph[cur]:
                dq.append((node, route + [node]))
    return result


# DFS Solution
def allPathsSourceTargetDFS(graph: List[List[int]]) -> List[List[int]]:
    result = []
    stack = [(0, [0])]
    target = len(graph) - 1
    while stack:
        cur, route = stack.pop()
        if cur == target:
            result.append(route)
        else:
            for node in graph[cur]:
                stack.append((node, route + [node]))
    return result


def main():
    test_data = [[1, 2], [3], [3], []]
    result = allPathsSourceTargetDFS(test_data)
    print(result)


if __name__ == "__main__":
    main()
