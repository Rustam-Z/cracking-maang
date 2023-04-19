"""
15. 3Sum
https://leetcode.com/problems/3sum/

Problem: Given an array of integers, return all triplets with sum 0. No duplicate triplets!

Constraints?
    The length of array always bigger than 3?
    What if we don't have any triplets?

SOLUTION 1: Sort array then use two pointers (1 index, and last index)
SOLUTION 2: Same as SOLUTION 1 but a bit efficient
"""
from typing import List, Set, Tuple


# O(N^2) time | O(1) space
def solution1(nums: List[int]) -> list[tuple[int, int, int]]:
    nums.sort()
    ans = set()

    for i in range(len(nums)):
        st = i + 1
        sp = len(nums) - 1

        while st < sp:
            if nums[st] + nums[sp] + nums[i] < 0:
                st += 1
            elif nums[st] + nums[sp] + nums[i] > 0:
                sp -= 1
            else:
                tp = (nums[i], nums[st], nums[sp])
                ans.add(tp)
                st += 1
                sp -= 1

    return list(ans)


# O(N^2) time | O(1) space
def solution2(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []

    for i in range(len(nums) - 2):
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            if sum_ == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif sum_ < 0:
                left += 1
            else:
                right -= 1

    return triplets
