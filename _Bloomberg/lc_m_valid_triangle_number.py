"""611. Valid Triangle Number
https://leetcode.com/problems/valid-triangle-number/

Problem: Given the array, count how many triangles can be constructed.
"""
from typing import List


def triangleNumber(nums: List[int]) -> int:
    nums.sort()
    L = len(nums)
    result = 0

    # c < a + b
    for i in range(L - 1, 1, -1):
        start = 0
        end = i - 1
        c = nums[i]

        while start < end:
            a = nums[start]
            b = nums[end]
            if a + b > c:
                result += end - start
                end -= 1
            else:
                start += 1

    return result
