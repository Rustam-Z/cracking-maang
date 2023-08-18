"""
4Sum: https://leetcode.com/problems/4sum/

Problem: Given an array nums and target, group 4 integers so that their sum equals to target.

Examples:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    Input: nums = [], target = 0
    Output: []
"""

from typing import List


def brute_force(nums: List[int], target: int) -> List[List[int]]:
    """
    Time: O(n^4)
    Space: O(1)
    """
    result = set()

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            for k in range(j + 1, len(nums) - 1):
                for l in range(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.add((nums[i], nums[j], nums[k], nums[l]))

    return list(result)


def two_pointers_with_set(nums: List[int], target: int) -> List[List[int]]:
    """
    Time: O(n^3)
    Space: O(n)
    """
    nums.sort()
    result = set()

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left = j + 1
            right = len(nums) - 1

            while left < right:
                sum_ = nums[i] + nums[j] + nums[left] + nums[right]

                if sum_ == target:
                    result.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum_ < target:
                    left += 1
                else:
                    right -= 1

    return list(result)
