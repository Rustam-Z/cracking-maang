"""
Given the matrix with 0s and 1s, we need to find largest area with 1 calculated in 4-directions (up, down, left, right)

We need to use the DFS, recursively.

Time: O(R*C)
Space: O(R*C)
"""


class Solution:
    def __init__(self):
        self.seen = set()  # We will not check the pixel which was check before

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                new_area = self.area(grid, r, c)
                max_area = max(max_area, new_area)

        return max_area

    def area(self, grid, r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in self.seen and grid[r][c]):
            return 0
        self.seen.add((r, c))

        return (1 + self.area(grid, r + 1, c) + self.area(grid, r - 1, c) +
                self.area(grid, r, c - 1) + self.area(grid, r, c + 1))
        # We need to add all the previous results, on the code 733, we were coloring in-place, so counter will not
        # work in this problem


# https://support.leetcode.com/hc/en-us/articles/360011834174-I-encountered-Wrong-Answer-Runtime-Error-for-a-specific-test-case-When-I-test-my-code-using-this-test-case-it-produced-the-correct-output-Why-

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

sol = Solution()
print(sol.maxAreaOfIsland(grid))
