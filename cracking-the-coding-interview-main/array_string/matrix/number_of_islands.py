"""200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Approach
    - Use DFS algorithm, to check left-right-up-down of the item,
    and mark as 0 the regions which are checked, so that we don't
    want to visit it.
"""


# Time O(M*N) | Space O(1)
def numIslands(grid):
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
