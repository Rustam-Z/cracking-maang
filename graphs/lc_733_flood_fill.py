"""
Flood fill: https://leetcode.com/problems/flood-fill/

Problem: Need to color 4-dimensionally (up, left, right, down)
"""


def solution(image, sr, sc, newColor):
    """
    Algorithm (DFS = Depth first search, uses the Stack):
    1. Check if the given cell is not the new color and is the original color
    2. If yes, then change the color of the cell to the new color
    3. Then recursively call the function for the up, down, left, right cells

    Time: O(R*C), where R is the number of rows in the given image, and C is the number of columns.
    Space: O(R*C)
    """

    if not image or image[sr][sc] == newColor:
        return image

    number_of_rows, number_of_columns = len(image), len(image[0])

    def dfs(image, row, column, original_color):
        if 0 <= row < number_of_rows and 0 <= column < number_of_columns and image[row][column] == original_color:
            image[row][column] = newColor
            dfs(image, row + 1, column, original_color)
            dfs(image, row - 1, column, original_color)
            dfs(image, row, column + 1, original_color)
            dfs(image, row, column - 1, original_color)

    dfs(image, sr, sc, original_color=image[sr][sc])  # No need to iterate over each cell. Only for image[sr][sc]

    return image


if __name__ == "__main__":
    assert solution(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2) == [[2, 2, 2], [2, 2, 0],
                                                                                        [2, 0, 1]]
    assert solution(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1) == [[0, 0, 0], [0, 1, 1]]
