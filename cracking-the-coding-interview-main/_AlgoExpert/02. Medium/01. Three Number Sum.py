"""
Similar to https://leetcode.com/problems/3sum/

Problem: given unsorted array, find all triplets which sum to targetSum.
"""


# O(N^2) time | O(N) space
def solution(array: list, target_sum: int) -> list[tuple]:
    """
    Solution:
    - sort the array
    - use two pointers technique
    """
    result = []  # # If you don't want duplicates use set
    array.sort()  # in-place, O(N*logN)

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target_sum:
                left += 1
                right -= 1
                result.append((array[i], array[left], array[right]))
            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1

    return result


def better_solution(nums: list, target_sum: int) -> list:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target_sum:
                result.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            elif current_sum > target_sum:
                right -= 1

    return result
