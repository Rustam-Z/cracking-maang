"""
LeetCode: 1631. Path With Minimum Effort, https://leetcode.com/problems/path-with-minimum-effort/

Problem: Find the minimum effort path from the top-left to the bottom-right of a given 2D plane.

Solution:
1. Use the Dijkstra's algorithm to find the minimum effort path.
2. Use a priority queue to store the nodes with the minimum effort.
3. Use a visited set to store the visited nodes.
4. Use a dictionary to store the effort of each node.

Time: O(n^2)
Space: O(n^2)
"""
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        min_heap = [(0, (0, 0))]
        res = 0

        while min_heap:
            w, (r, c) = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            res = max(res, w)
            if (r, c) == (rows - 1, cols - 1):
                break
            ds = (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)
            for dr, dc in ds:
                if dr < 0 or dr >= rows or dc < 0 or dc >= cols:
                    continue
                if (dr, dc) in visited:
                    continue
                diff = abs(heights[r][c] - heights[dr][dc])
                heapq.heappush(min_heap, (diff, (dr, dc)))

        return res








