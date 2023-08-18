"""
Given a gird, and there are X and Y in this grid. find the shortest distance between X and Y.

Example 1:

Input:
[[X,0,0],
 [0,Y,0],
 [X,Y,0]]
Output: 1
Example 2:

Input:
[[X,X,0],
 [0,0,Y],
 [Y,0,0]]
Output: 2

Questions:
    - Which directions we can move?
    - Do we have X, Y?
"""

from collections import deque


def bfs(grid):
    q, visited = deque(), set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Insert all Xs into the queue
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                # (position, distance)
                q.append(((i, j), 0))
                visited.add((i, j))

    while q:
        for _ in range(len(q)):
            (row, col), dist = q.popleft()
            if grid[row][col] == 'Y':  # We found Y, we return.
                return dist

            for dir in dirs:
                new_pos = (new_r, new_c) = row + dir[0], col + dir[1]
                if new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]) or new_pos in visited:
                    continue
                q.append((new_pos, dist + 1))
                visited.add(new_pos)

    # Can't reach Y
    return -1


