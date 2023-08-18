"""
https://leetcode.com/problems/01-matrix

01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

Example:
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]

    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
from typing import List


def updateMatrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Algorithm:
        - BFS
        - But we should change 1s to something different, so we can distinguish real 1s with 1s that we added (distances.)

    Time complexity: O(mn)
    Space complexity: O(mn)
    """
    queue = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                queue.append((r, c))
            else:
                matrix[r][c] = "#"  # to save the initial state of 1s, then for up, down, left, right we can

    for r, c in queue:
        for dx, dy in directions:
            row, col = dx + r, dy + c
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == "#":
                matrix[row][col] = matrix[r][c] + 1
                queue.append((row, col))

    return matrix
