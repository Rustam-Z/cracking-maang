"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
https://www.youtube.com/watch?v=zx5Sw9130L0

Problem: Given array with heights of histogram bars, find the largest rectangle area.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""


def largestRectangleArea(heights):
    stack = []  # Store the index of the bar
    max_area = 0

    for i in range(len(heights)):
        # If current bar is lower than the bar on top of stack, then calculate area of rectangle.
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        # If current bar is higher than the bar on top of stack, push it to stack.
        stack.append(i)

    # Calculate area for the remaining bars in stack.
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

