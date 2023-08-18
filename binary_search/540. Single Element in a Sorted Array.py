"""
Problem: Given array in which each element is repeated twice except one element. Find that element.
"""


# Solution 1: Using XOR
# Time Complexity: O(n)
# Space Complexity: O(1)
def singleNonDuplicate(nums):
    res = 0
    for i in nums:
        res ^= i
    return res

# Solution 2: Using Binary Search
# Time Complexity: O(logn)
# Space Complexity: O(1)
def singleNonDuplicate2(nums):
    start = 0
    end = len(nums) - 2
    while end >= start:
        mid = (end + start) // 2
        if nums[mid] == nums[mid ^ 1]:
            start = mid + 1
        else:
            end = mid - 1
    return nums[start]
