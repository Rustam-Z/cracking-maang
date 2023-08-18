"""
62. Unique Paths: https://leetcode.com/problems/unique-paths/

Problem:
    - A robot is located at the top-left corner of a m x n grid.
    - The robot can only move either down or right at any point in time.
    - Find unique paths to reach the bottom-right corner of the grid.

Questions and constraints:
    - Matrix is square or can be any shape?
    - We can move only down and right?
"""


def backtracking_solution(m: int, n: int) -> int:
    """
    Algorithm:
        - We can move only down and right.
        - We try to move down and right until we reach the bottom-right corner.
        - We can use backtracking to solve this problem. Try all possible paths.

    Time complexity: O(2^(m+n))
    Space complexity: O(m+n)
    """
    def backtrack(row: int, col: int) -> int:
        if row == m - 1 and col == n - 1:
            return 1

        # Check if we are out of bounds. If we are, return 0.
        if row >= m or col >= n:
            return 0

        return backtrack(row + 1, col) + backtrack(row, col + 1)

    return backtrack(0, 0)


def optimized_solution(m: int, n: int) -> int:
    """
    Algorithm:
        - Use dynamic programming to solve this problem.
        - We can use a matrix to store the number of unique paths to reach each cell.
        - We can fill the first row and first column with 1.
        - We can fill the rest of the matrix by adding the number of unique paths from the top and left cell.

    How it works:
        1 1 1 1 1
        1 0 0 0 0
        1 0 0 0 0

        matrix[1][1] = matrix[0][1] + matrix[1][0]
        matrix[1][2] = matrix[0][2] + matrix[1][1]
        matrix[1][3] = matrix[0][3] + matrix[1][2]
        matrix[1][4] = matrix[0][4] + matrix[1][3]
        matrix[2][1] = matrix[1][1] + matrix[2][0]
        matrix[2][2] = matrix[1][2] + matrix[2][1]

    Time complexity: O(m*n)
    Space complexity: O(m*n)
    """
    dp = [[0] * n for _ in range(m)]

    # Fill the first column with 1
    for i in range(m):
        dp[i][0] = 1

    # Fill the first row with 1
    for j in range(n):
        dp[0][j] = 1

    # Fill the rest of the matrix
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Return the last element of the matrix
    return dp[-1][-1]
