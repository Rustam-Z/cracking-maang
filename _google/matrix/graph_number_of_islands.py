from typing import List


def number_of_islands(grid: List[List[str]]) -> int:
    """
    https://leetcode.com/problems/number-of-islands/

    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

    Algorithm:
        - DFS
        - Iterate through the grid, if we find a 1, we increment the count and call the dfs function
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
