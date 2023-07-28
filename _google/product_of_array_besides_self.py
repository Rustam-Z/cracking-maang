"""
https://leetcode.com/problems/product-of-array-except-self/

Problem: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Constraints:
    - You must write an algorithm that runs in O(n) time and without using the division operation.

Solution 1: Brute force.
    - 2 loops.
    - Time comp: O(N^2)

Solution 2: Left and right product lists.
    - Time comp: O(N)
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # Multiplication of element before "i" element
        p = 1
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]

        # Multiplication of elements in reverse
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output
