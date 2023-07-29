"""
https://leetcode.com/problems/find-peak-element/

Problem: A peak element is an element that is strictly greater than its neighbors.

Constraints:
    - There is always a peak element in the array.
    - Return any peak element, not necessarily the biggest element.
    - IMPORTANT!!! Ex: [4, 100, 9, 10, 11, 2, 3], peak elements could be 100, 11, 3.

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [1,2,3]
Output: 2

Input: nums = [1,2,3,4]
Output: 3

Input: nums = [4,3,2,1]
Output: 0

"""

from typing import List


def brute_force_python(nums: List[int]) -> int:
    # This is a Pythonic way of doing it.
    # Time complexity: O(n)
    # Space complexity: O(1)
    return nums.index(max(nums))


def brute_force(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    if len(nums) <= 3:
        return nums.index(max(nums))

    max_idx = 0
    for i in range(1, len(nums) - 1):
        tmp = max_idx  # We need to store the index of the biggest element so far.

        if nums[i - 1] < nums[i] > nums[i + 1]:
            tmp = i
        elif i == len(nums) - 2 and nums[i] < nums[i + 1]:  # Handle the last element, ex: [1, 2, 3, 4]
            tmp = i + 1

        # We want to return the biggest element's index.
        if nums[max_idx] < nums[tmp]:
            max_idx = tmp

    return max_idx


def optimized_solution_logN(nums: List[int]) -> int:
    # IMPORTANT!!! Ex: [4, 100, 9, 10, 11, 2, 3], peak elements could be 100, 11, 3. For this reason we can use binary search.
    # Time complexity: O(logN)
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if mid > 0 and nums[mid] < nums[mid-1]:
            high = mid - 1
        elif mid < len(nums) - 1 and nums[mid] < nums[mid+1]:
            low = mid + 1
        else:
            return mid
