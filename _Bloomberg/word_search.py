"""79. Word Search
https://leetcode.com/problems/word-search/

Problem:
    Given 2D array `board` and `word` string, we have to check if we can form a string in array.

Constraints:
    - `board` contains lowercase and uppercase chars.
    - If `word` is not in board then return False.

Approach:
    - Use DFS algorithm to check up, down, left, right neightbours.
    - We have to mark our character with some special `/` so not to visit it again.
    - Question? Imagine we have neighbours with the same chars that we need?
      Answer: We can handle this case with DFS. We will return just False if board[i][j] != word[k].
    - TIme: O(mn * 4^k), k is the length of the word, m & n are rows and columns.
    - Space: O(k), recursion call stack will have k levels of call.
"""


def exist(board, word):
    def dfs(board, word, i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        tmp, board[i][j] = board[i][j], '/'
        res = dfs(board, word, i+1, j, k+1) or dfs(board, word, i-1, j, k+1) or dfs(board, word, i, j+1, k+1) or dfs(board, word, i, j-1, k+1)
        board[i][j] = tmp
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j, 0):
                return True
    return False
