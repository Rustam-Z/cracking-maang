"""
Container With Most Water: https://leetcode.com/problems/container-with-most-water/

Problem:
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.

height = [1,8,6,2,5,4,8,3,7]
Output: 49
"""


def brute_force(height):
    """
    Algorithm:
        - Try all possible combinations of lines and find the maximum area out of those.
    Time: O(n^2)
    Space: O(1)
    """
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            new_area = min(height[i], height[j]) * (j-i)  # Calculate area: height * width
            max_area = max(max_area, new_area)
    return max_area


def two_pointer(height):
    """
    Algorithm:
        - Use two pointers, one at the beginning and one at the end of the array.
        - Move the pointer with the smaller height inwards.
        - Calculate the area and update the max_area.
    Time: O(n)
    Space: O(1)
    """
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        new_area = min(height[left], height[right]) * (right-left)  # Calculate area: height * width
        max_area = max(max_area, new_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
