"""
Problem: Need to color 4-dimensionally (up, left, right, down)

DFS = Depth first search, uses the Stack.

0. We have to use the recursion
1. Edge case, check if list is None or the image pixel is already same color
2. Apply DFS
3. Check if index is out of bounds or current pixel is not the same color

Time: O(n)
Space: O(n)
"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        # Check for the corner cases
        if image is None or image[sr][sc] == newColor:
            return image

        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image

    def fill(self, image, row, column, initial, newColor):
        # Base case, check out of bounds
        if row < 0 or row >= len(image) or column < 0 or column >= len(image[0]) or image[row][
            column] != initial:  # last one checks if the color of pixel is not the same as initial
            return

        image[row][column] = newColor
        self.fill(image, row - 1, column, initial, newColor)  # Up
        self.fill(image, row + 1, column, initial, newColor)  # Down
        self.fill(image, row, column - 1, initial, newColor)  # Left
        self.fill(image, row, column + 1, initial, newColor)  # Right


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 0
sc = 1
newColor = 2

sol = Solution()
print(sol.floodFill(image, sr, sc, newColor))
