"""
Diagonal Traverse: https://leetcode.com/problems/diagonal-traverse/

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9] CHECK PICTURE!!!

1 2 3
4 5 6
7 8 9

"""


def brute_force(matrix: list[list[int]]) -> list:
    """
    Algorithm:
        - Create a list to store each diagonal.
        - Iterate through each diagonal, and depending on ODD/EVEN, we append to the list.

    Time complexity: O(n*m)
    Space complexity: O(n*m)

    diagonals = get_diagonals(matrix)
    loop over diagonals list and create a new lists with traversed elements. Use boolean to track.
    """

    # Check for empty matrices
    if not matrix or not matrix[0]:
        return []

    def get_diagonals(matrix):
        """
        Get all the diagonals of the matrix.
        """
        diagonals = []

        # Get all the diagonals starting from the first column
        for i in range(len(matrix)):
            diagonal = []
            row, col = i, 0
            while row >= 0 and col < len(matrix[0]):
                diagonal.append(matrix[row][col])
                row -= 1
                col += 1
            diagonals.append(diagonal)

        # Get all the diagonals starting from the last row
        for j in range(1, len(matrix[0])):
            diagonal = []
            row, col = len(matrix) - 1, j
            while row >= 0 and col < len(matrix[0]):
                diagonal.append(matrix[row][col])
                row -= 1
                col += 1
            diagonals.append(diagonal)

        return diagonals

    diagonals = get_diagonals(matrix)  # [[1], [4, 2], [7, 5, 3], [8, 6], [9]]

    output = []
    for i, diagonal in enumerate(diagonals):
        if i % 2 == 0:
            output.extend(diagonal[::-1])
        else:
            output.extend(diagonal)

    return output


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # [1, 4, 2, 3, 5, 7, 8, 6, 9]
    print(brute_force(matrix))
