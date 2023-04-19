"""
75. Sort Colors
https://leetcode.com/problems/sort-colors/

Problem: Given an array with 0, 1 and 2, sort them in-place.

Constants?
    Will we have all 3 colors always?

SOLUTION 1: use list sort() method, O(N*logN) time, O(1) space, or any other sorting
SOLUTION 2: append 2 in the end, insert 0 in beginning, O(N^2) time, O(1) space
SOLUTION 3: use Counter and change the values of array via slicing, O(N) time, O(1) space
SOLUTION 4: use swapping, O(N) time, O(1) space
"""


# O(N^2) time | O(1) space
def solution2(nums: list[int]) -> None:
    end = len(nums)
    i = 0
    while i < end:
        num = nums[i]
        if nums[i] == 2:
            nums.pop(i)
            nums.append(2)
            end -= 1
        elif nums[i] == 0:
            nums.pop(i)
            nums.insert(0, 0)
            i += 1
        else:
            i += 1


# O(N) time | O(1) space
def solution3(nums: list[int]) -> None:
    counts = collections.Counter(nums)
    one = counts.get(0, 0)
    two = counts.get(1, 0)
    three = counts.get(2, 0)
    nums[:one] = [0] * one
    nums[one:two] = [1] * two
    nums[one + two:] = [2] * three


# O(N) time, O(1) space
def solution4(nums: list) -> None:
    n = len(nums)

    # Handing the constraint
    if n == 2 and nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
        return None

    low, mid, high = 0, 0, n - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low, mid = low + 1, mid + 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
