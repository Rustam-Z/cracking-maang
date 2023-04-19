"""
LeetCode: 724. Find Pivot Index

Problem: Given an array of integers nums, calculate the pivot index of this array.
         Pivot index = sum all left and right items are equal

Input: nums = [1,7,3,6,5,6]
Output: 3 (index)

Solution:
    - Calculate overall sum
    - Using a for loop, checking if left sum == (overall_sum - left sum - current_item_in_a_loop_
    - Don't forget to increment the left sum.

Time: O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0

        for i, x in enumerate(nums):
            if left_sum == (S - left_sum - x):
                return i
            left_sum += x

        return -1


if __name__ == "__main__":
    test_data = [1, 7, 3, 6, 5, 6]

    s = Solution()
    print(s.pivotIndex(test_data))
