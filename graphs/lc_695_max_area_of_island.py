"""
Max Area of island: https://leetcode.com/problems/max-area-of-island/

Given the matrix with 0s and 1s, we need to find largest area with 1 calculated in 4-directions (up, down, left, right)

We need to use the DFS, recursively.

Time: O(R*C)
Space: O(R*C)
"""


def solution(grid: list[list[int]]) -> int:
    """
    1. Use DFS to traverse the grid, only if the current cell is 1.
    2. During DFS, we will mark the cell as 0, so we don't visit it again.
    """

    if not grid:
        return 0

    number_of_rows, number_of_columns = len(grid), len(grid[0])
    max_area = 0

    def dfs_calculate_area(grid, row, column) -> int:
        if 0 <= row < number_of_rows and 0 <= column < number_of_columns and grid[row][column] == 1:
            grid[row][column] = 0
            return (1 + dfs_calculate_area(grid, row, column + 1) +
                    dfs_calculate_area(grid, row, column - 1) +
                    dfs_calculate_area(grid, row + 1, column) +
                    dfs_calculate_area(grid, row - 1, column))

        return 0

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if grid[row][column] == 1:
                area = dfs_calculate_area(grid, row, column)
                max_area = max(max_area, area)

    return max_area


def solution_with_seen_set(self, grid: list[list[int]]) -> int:
    max_area = 0
    seen = set()  # We will not check the pixel which was check before

    def area(grid, r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c] == 1:
            seen.add((r, c))
            return 1 + area(grid, r + 1, c) + area(grid, r - 1, c) + area(grid, r, c - 1) + area(grid, r, c + 1)
        else:
            return 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            new_area = area(grid, r, c)
            max_area = max(max_area, new_area)

    return max_area


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    print(solution(grid))
