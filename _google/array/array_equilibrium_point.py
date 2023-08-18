"""
Find pivot index (equilibrium) in array: https://leetcode.com/problems/find-pivot-index/

Problem: Given an array of integers nums, calculate the pivot index of this array.
    Sum of numbers to the left of the index is equal to the sum of numbers to the right of the index.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation: The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11.
    Right sum = nums[4] + nums[5] = 5 + 6 = 11.

"""
from typing import List


def brute_force(nums: List[int]) -> int:
    """
    Algorithm:
        - Iterate over array. For each element, calculate left and right sum.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for i in range(len(nums)):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i + 1:])

        if left_sum == right_sum:
            return i

    return -1


def optimized_solution(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]

    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    for i in range(len(nums)):
        left_sum = prefix_sum[i] - nums[i]
        right_sum = prefix_sum[-1] - prefix_sum[i]

        if left_sum == right_sum:
            return i

    return -1


def best_solution(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """

    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        total_sum -= num
        if left_sum == total_sum:
            return i

        left_sum += num

    return -1
