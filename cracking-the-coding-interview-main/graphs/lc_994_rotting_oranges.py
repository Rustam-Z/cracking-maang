"""
https://www.youtube.com/watch?v=y704fEOx0s0&list=LL&index=2

We have array with oranges

0 = no
1 = fresh
2 = rotten

We need to make the oranges rotten

O(n*m) time & space, row*column
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # fresh
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r, c])  # Save the coordinates for rotten

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # up, down, right, left
        while queue and fresh > 0:

            for i in range(len(queue)):  # Iterating over all rotten oranges, for all rotten images, doing
                # simultaneously, +1 time
                r, c = queue.pop(0)

                # Here we need to go over 4 dimensions
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if not (0 <= row < rows and 0 <= col < cols and grid[row][col] == 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1

