"""80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Problem:
    Modify array in-place such that each unique element appears at most twice, and return the length of array.

Example:
    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7 and nums = [0,0,1,1,2,3,3,_,_]. But don't return the array.

Constraints and questions?
    - Won't we have just 1 item. -> It is guaranteed that at least 2 items.
    - Array is sorted
    - Items are only integers?
"""
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) < 3:
        return len(nums)

    ind = 2  # Pointer from where we need to replace elements
    for i in range(2, len(nums)):
        if nums[i] != nums[ind - 2]:
            nums[ind] = nums[i]
            ind += 1

    return ind

