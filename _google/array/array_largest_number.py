"""
Largest Number: https://leetcode.com/problems/largest-number/

Problem: Given a list of non-negative integers nums, arrange them such that they form the largest number.

Examples:
    Input: nums = [10,2]
    Output: "210"

    Input: nums = [3,30,34,5,9]
    Output: "9534330"

    Input: nums = [1]
    Output: "1"

Questions and constraints:
    - Can we have negative numbers?
    - Can we have duplicates?
    - Can we have 0? What to do with array of 0s?
"""

from typing import List


def brute_force(nums: List[int]) -> str:
    """
    Algorithm:
        - Convert all numbers to string.
        - Sort the array of strings in reverse order. Then join them.

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    nums = list(map(str, nums))
    nums.sort(reverse=True)
    return ''.join(nums)


def bucketing_custom_sort(nums: List[int]) -> str:
    """
    Algorithm:
        1. Divide into buckets by starting digit, 9 should come first, then 8, 7, ...
        2. Inner bucket sorting, similar to radix sort, sort by 2nd 3rd digits.
           It is NOT like string sorting in Python because in Python 3 comes before 34, but 343 is bigger.
        3. Join all buckets.
        4. Disadvantage: Difficult to implement inner bucket sorting.
    """
    ...


def working_solution_swapping(nums: List[int]) -> str:
    """
    Algorithm:
        1. Convert all nums to string.
        2. Compare string a + b and b + a. And swap by places.
        3. Join all nums.

    Example:
        1, 10, 19, 190, 192, 45, 99
        HOW IT WORKS?
        110 or 101 -> 110
        11019 or 19110 -> 19110
        1911045 or 4519110 -> 4519110
        451911099 or 994519110 -> 994519110 SO WE GOT THE MAX NUM

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    nums = list(map(str, nums))  # converting to string

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] > nums[j] + nums[i]:  # comparing xy and yx
                continue
            else:
                nums[i], nums[j] = nums[j], nums[i]  # swap

    result = ''.join(nums)  # joining list

    return '0' if result[0] == '0' else result


def python_solution(nums: List[int]) -> str:
    """
    Algorithm:
        1. Convert all nums to string.
        2. Sort by comparing a + b and b + a.
        3. Join all nums.

    Example:
        1, 10, 19, 190, 192, 45, 99
        HOW IT WORKS?
        110 or 101 -> 110
        11019 or 19110 -> 19110
        1911045 or 4519110 -> 4519110
        451911099 or 994519110 -> 994519110 SO WE GOT THE MAX NUM

    Time complexity: O(n log n)
    Space complexity: O(1)
    """

    class LargerNumKey(str):
        def __lt__(x, y):
            return x + y > y + x

    str_nums = map(str, nums)  # Not necessary to make list.
    largest_num = ''.join(sorted(str_nums, key=LargerNumKey))  # We can use cmp_to_key() from functools.
    return '0' if largest_num[0] == '0' else largest_num


if __name__ == "__main__":
    assert working_solution_swapping([10, 2]) == "210"
    assert working_solution_swapping([3, 30, 34, 5, 9]) == "9534330"
    assert working_solution_swapping([1]) == "1"
    assert working_solution_swapping([0]) == "0"
    assert working_solution_swapping([0, 0]) == "0"
