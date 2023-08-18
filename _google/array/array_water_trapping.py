"""
Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/

Problem: Calculate how much water can be trapped in between the bars.

Constraints: We can put water is BAR - 1 > BAR < BAR + 1

Example:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""


def brute_force(height):
    """
    Algorithm:
        - For each bar, find the maximum height bar on the left and right.
        - The amount of water that can be trapped is min(left_max, right_max) - height.
    Time: O(n^2)
    Space: O(1)
    """
    total_water = 0
    for i in range(len(height)):
        left_max = 0
        right_max = 0
        for j in range(i, -1, -1):
            left_max = max(left_max, height[j])
        for j in range(i, len(height)):
            right_max = max(right_max, height[j])
        total_water += min(left_max, right_max) - height[i]
    return total_water


def optimized_solution(height):
    """
    Algorithm:
        - Use two pointers, one at the beginning and one at the end of the array.
        - Move the pointer with the smaller height inwards.
        - Calculate the area and update the max_area.
    Time: O(n)
    Space: O(1)
    """
    total_water = 0
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    while left < right:
        if height[left] < height[right]:  # Move the pointer with the smaller height inwards.
            if height[left] > left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]
            right -= 1
    return total_water
