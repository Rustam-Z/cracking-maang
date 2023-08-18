"""
Rotate image: https://leetcode.com/problems/rotate-image/

Problem:
    Given an image represented by an NxN matrix, rotate this matrix by 90 degrees clockwise.

Questions and clarifications:
    - Matrix is NxN, square matrix?
    - Only numbers?
    - Should it be rotated in place? Or we need to return new one?
    - We need to rotate the matrix 90 degrees clockwise.

NOTE!
    - While rotating the matrix, the inner matrices should be rotated.
      So rotate level by level.

Example:
    Input:
        [1,2,3]
        [4,5,6]
        [7,8,9]
    Output:
        [7,4,1]
        [8,5,2]
        [9,6,3]
"""


def brute_force(matrix: list) -> list:
    """
    Algorithm:
        - Create new matrix
        - Iterate over the matrix and fill the new matrix
        - Return new matrix

    Time complexity: O(N^2)
    Space complexity: O(N^2)

    HOW IT WORKS?
        1 2 3
        4 5 6
        7 8 9

        new_matrix[j[n - i - 1]] = matrix[i][j]

        -- i=0 --
        new_matrix[0][2] = matrix[0][0] = 1
        new_matrix[1][2] = matrix[0][1] = 2
        new_matrix[2][2] = matrix[0][2] = 3
        -- i=1 -- 3 - 1 - 1 = 1
        new_matrix[0][1] = matrix[1][0] = 4
        new_matrix[1][1] = matrix[1][1] = 5
        new_matrix[2][1] = matrix[1][2] = 6

    """
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_matrix[j][n - i - 1] = matrix[i][j]

    return new_matrix


def matrix_transposition_solution(matrix: list) -> list:
    """
    Algorithm:
        - Transpose the matrix
        - Reverse each row

    Time complexity: O(N^2)
    Space complexity: O(1)

    HOW IT WORKS?
        1 2 3
        4 5 6
        7 8 9

        -- Transpose --
        1 4 7
        2 5 8
        3 6 9

        -- Reverse each row --
        7 4 1
        8 5 2
        9 6 3

    """
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert brute_force(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert matrix_transposition_solution(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    assert brute_force(matrix) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    assert matrix_transposition_solution(matrix) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
