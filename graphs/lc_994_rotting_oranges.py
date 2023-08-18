"""
Rotting oranges: https://leetcode.com/problems/rotting-oranges/
https://www.youtube.com/watch?v=y704fEOx0s0&list=LL&index=2

We have array with oranges.

0 = no
1 = fresh
2 = rotten

We need to make the oranges rotten.
"""
from collections import deque
from typing import List


def solution_bfs(grid: List[List[int]]) -> int:
    """
    Algorithm:
        1. Only BFS will work here, because if orange is rotten it makes neighbors rotten at the same time.
        2. Count fresh oranges, if it's not 0 in the end, it means that we can't make all oranges rotten.
        3. Keep track of rotten oranges in the queue. Will be used in BFS.
        4. Iterate over the queue, and make neighbors rotten.

    """
    number_of_rows, number_of_columns = len(grid), len(grid[0])
    fresh_oranges_count = 0  # Count fresh oranges, in the end if it's not 0, it means that we can't make all oranges rotten.
    rotten_oranges_positions = deque()  # Keep track of positions of rotten oranges.

    for r in range(number_of_rows):
        for c in range(number_of_columns):
            if grid[r][c] == 1:
                fresh_oranges_count += 1
            elif grid[r][c] == 2:
                rotten_oranges_positions.append([r, c])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # up, down, right, left
    minutes = 0

    while rotten_oranges_positions and fresh_oranges_count > 0:
        for _ in range(len(rotten_oranges_positions)):  # Iterating over all rotten oranges, for all rotten images, doing simultaneously, +1 time
            r, c = rotten_oranges_positions.popleft()

            # Here we need to go over 4 dimensions.
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < number_of_rows and 0 <= col < number_of_columns and grid[row][col] == 1:
                    grid[row][col] = 2
                    rotten_oranges_positions.append([row, col])
                    fresh_oranges_count -= 1

        minutes += 1

    return minutes if fresh_oranges_count == 0 else -1

