"""
Number of islands: https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
from typing import List


def dfs_solution(grid: List[List[str]]) -> int:
    """
    Algorithm:
        - We will use DFS to traverse the grid, only if the current cell is 1.
        - During DFS, we will mark the cell as 0, so we don't visit it again. And it means that we create a new island.

    Time complexity: O(m * n)
    Space complexity: O(m * n)
    """
    if not grid:
        return 0

    number_of_rows, number_of_columns = len(grid), len(grid[0])

    def dfs(row, column):
        if 0 <= row < number_of_rows and 0 <= column < number_of_columns and grid[row][column] == "1":
            grid[row][column] = "0"
            dfs(row + 1, column)
            dfs(row, column + 1)
            dfs(row - 1, column)
            dfs(row, column - 1)

    result = 0
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if grid[row][column] == "1":
                dfs(row, column)
                result += 1

    return result


def bfs_solution(grid: List[List[str]]) -> int:
    """
    Algorithm:
        - We will use BFS to traverse the grid, only if the current cell is 1.
        - During BFS, we will mark the cell as 0, so we don't visit it again. And it means that we create a new island.
    """

    if not grid:
        return 0

    number_of_rows, number_of_columns = len(grid), len(grid[0])
    result = 0

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if grid[row][column] == "1":
                result += 1
                grid[row][column] = "0"

                queue = [(row, column)]
                while queue:
                    current_row, current_column = queue.pop(0)
                    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                    for dr, dc in directions:
                        next_row, next_column = current_row + dr, current_column + dc
                        if (0 <= next_row < number_of_rows and 0 <= next_column < number_of_columns
                                and grid[next_row][next_column] == "1"):
                            grid[next_row][next_column] = "0"
                            queue.append((next_row, next_column))

    return result

