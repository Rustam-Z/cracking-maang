"""
https://leetcode.com/problems/two-sum/

Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Questions and constraints:
    - Do we have these 2 number that add up to sum?
    - Are there duplicates?
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}

        for idx, num in enumerate(nums):
            if num in dict_:
                return [dict_[num], idx]

            dict_[target - num] = idx
