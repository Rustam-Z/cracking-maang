"""
Product of all n elements expect the index value for each index: https://leetcode.com/problems/product-of-array-except-self/

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


def brute_force(nums: List[int]) -> List[int]:
    # Time comp: O(N^2)
    # Space comp: O(N)
    res = []
    for i in range(len(nums)):
        tmp = 1
        for j in range(len(nums)):
            if i != j:
                tmp *= nums[j]
        res.append(tmp)

    return res


def optimized_solution(nums: List[int]) -> List[int]:
    # Time comp: O(N)
    # Space comp: O(N)
    left = [1] * len(nums)
    right = [1] * len(nums)
    res = [1] * len(nums)

    # Left product list.
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    # Right product list.
    for i in range(len(nums) - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # Multiply left and right product lists.
    for i in range(len(nums)):
        res[i] = left[i] * right[i]

    return res


def clean_code_solution(nums: List[int]) -> List[int]:
    # Time comp: O(N)
    # Space comp: O(1)
    res = [1] * len(nums)

    # Left product list.
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]

    # Right product list.
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res
