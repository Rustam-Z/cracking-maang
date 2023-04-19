"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
24 = 2*3*4
12 = 1*3*4
...
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        output = []

        # Multiplication of numbers before i
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]

        p = 1

        # Multiplication of elements in reverse
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output
