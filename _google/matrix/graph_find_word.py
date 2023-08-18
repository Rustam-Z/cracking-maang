"""
Find word in matrix. Search word in matrix. https://leetcode.com/problems/word-search/

Problem: Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
    are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Constraints and questions:
    - Only horizontal and vertical directions?
    - Strings?
    - Matrix is square? No.
"""
from typing import List


def solution(board: List[List[str]], word: str) -> bool:
    """
    Algorithm:
        - Apply DFS to search for the word. Use 2 loops.
        - In DFS we need to check if we found char, if yes we need to mark it as visited, and check 4 neighbors.
            - If we found the word, return True.
            - If we didn't find the word, return False.
            - We need to check if we are out of bounds.
            - After we perform all operation with the char, we need to mark it as unvisited.
              Because if we didn't find the word, we need to check other paths grid[i][j].

    Time Complexity: O(n^2 * 4^n)
    Space Complexity: O(n^2)
    """

    # Check if word has been found.
    number_of_rows, number_of_columns = len(board), len(board[0])

    def search(row, column, i) -> bool:
        """
        i = index of char in word we want to find
        Time Complexity: O(4^n)
        """

        # Check if word has been found.
        if i == len(word):  # Not len(word) - 1, because we need to change the last word too
            return True

        # Check if out of bounds.
        if not (0 <= row < number_of_rows) or not (0 <= column < number_of_columns):
            return False

        # Check if we found correct letter.
        if board[row][column] != word[i]:
            return False

        # Mark as visited.
        board[row][column] = "#"

        # Search 4 neighbours.
        is_found = (search(row + 1, column, i + 1) or
                    search(row - 1, column, i + 1) or
                    search(row, column + 1, i + 1) or
                    search(row, column - 1, i + 1))

        # Mark as unvisited. Because if we didn't find then we need to try other combination also.
        board[row][column] = word[i]

        return is_found

    # Try using every cell as start point.
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            is_found = search(row, column, i=0)  # We always start from beginning.
            if is_found is True:
                return True

    return False
