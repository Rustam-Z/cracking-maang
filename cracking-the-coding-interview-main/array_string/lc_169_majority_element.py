"""
169. Majority Element
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


# Sorting
# O(N*logN) time | O(1) space
def majority_element(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


# Counter
# O(N) time | O(N) space
def majorityElement(nums: list[int]) -> int:
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)


# Special algorithm
# O(N) time | O(1) space
def majorityElement(self, nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
