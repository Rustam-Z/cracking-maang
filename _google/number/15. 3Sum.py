"""
3Sum: https://leetcode.com/problems/3sum/

Problem: Given array[int], group 3 integers so that their sum equals to 0.

Examples:
    Input: [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Constraints and questions:
    - Target number?
    - Do we have duplicates? And how to handle them? Should we include them in the result? Or not?
        SOLUTION: If not, we can use set() to remove duplicates.
                  Or, track nums[i] and nums[i + 1]
    - Do we have negative numbers? And how to handle them?
"""
from typing import List


def brute_force(nums: List[int]) -> List[List[int]]:
    """
    Algorithm:
        - Create 3 nested loops, and create all possible combinations.
        - Sort array or even don't sort

    Time complexity: O(n^3)
    Space complexity: O(1)
    """
    if len(nums) < 3:
        return []

    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates.
            continue

        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates.
                continue

            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:  # Skip duplicates.
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result


def two_pointers_with_set(nums: List[int]) -> List[List[int]]:
    result = set()
    nums.sort()

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] < 0:
                left += 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1

    return list(result)


def two_pointers(nums: List[int]) -> List[List[int]]:
    """
    Algorithm:
        - Sort array
        - Iterate through each item in array, and use two pointers to find the other two numbers.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if len(nums) < 3:
        return []

    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates.
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]

            if sum_ < 0:
                left += 1
            elif sum_ > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:  # Skip duplicates.
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # Skip duplicates.
                    right -= 1

                left += 1
                right -= 1

    return result
