"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Problem: find the shortest path from top left to bottom right in a binary matrix. Use only 0s.

Constraints:
    - Use 8 directions to traverse the matrix. (To right, to left, to top, to bottom, and diagonals)

Solution:
    - Use BFS to find the shortest path.
    - Time complexity: O(N^2)
    - Space complexity: O(N^2)
"""
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Check if the start/end cell is blocked.
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # Create a queue for BFS and enqueue the start cell
        q = deque([(0, 0, 1)])  # r, c, path_length
        visited = {0, 0}
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while q:
            r, c, length = q.popleft()

            # Checking for bounds, and if value is 0
            if min(r, c) < 0 or max(r, c) >= n or grid[r][c]:
                continue

            # Check if the goal has been reached.
            if r == n - 1 and c == n - 1:  # The first (r,c) collections that reaches this code, will be already the smallest.
                return length

            # Explore adjacent grids.
            for dr, dc in directions:
                if (r + dr, c + dc) not in visited:
                    q.append((r + dr, c + dc, length + 1))
                    visited.add((r + dr, c + dc))  # grid[r + dr][c + dc] = 1

        return -1
