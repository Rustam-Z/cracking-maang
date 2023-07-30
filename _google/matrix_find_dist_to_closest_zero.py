"""
https://leetcode.com/problems/01-matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

"""
from typing import List


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:

    queue = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = "#"  # to save the initial state of 1s, then for up, down, left, right we can

    for r, c in queue:
        for dx, dy in directions:
            row, col = dx + r, dy + c
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] == "#":
                mat[row][col] = mat[r][c] + 1
                queue.append((row, col))

    return mat
