"""
300. Longest Increasing Subsequence: https://leetcode.com/problems/longest-increasing-subsequence/

Problem: Given an integer array nums, return the length of the longest strictly increasing subsequence.

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""


def dp_brute_force(nums: list) -> int:
    """
    Algorithm:
        - For each element in nums, we have two choices:
            - Take the element and increment the length of the subsequence by 1.
            - Don't take the element and keep the length of the subsequence same.

    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def helper(i: int, prev: int) -> int:
        if i == len(nums):
            return 0

        taken = 0  # Length of longest increasing subsequence if we take nums[i]
        if nums[i] > prev:
            taken = 1 + helper(i + 1, nums[i])

        not_taken = helper(i + 1, prev)  # Length of longest increasing subsequence if we don't take nums[i]

        return max(taken, not_taken)

    return helper(0, float('-inf'))


def dp_memoization(nums: list) -> int:
    """
    Algorithm:
        - For each element in nums, we have two choices:
            - Take the element and increment the length of the subsequence by 1.
            - Don't take the element and keep the length of the subsequence same.
        - We memoize the result of each subproblem to avoid recomputation.

    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    cache = {}  # (i, prev) -> result

    def helper(i: int, prev: int) -> int:
        if i == len(nums):
            return 0

        if (i, prev) in cache:
            return cache[(i, prev)]

        taken = 0
        if nums[i] > prev:
            taken = 1 + helper(i + 1, nums[i])

        not_taken = helper(i + 1, prev)

        cache[(i, prev)] = max(taken, not_taken)

        return cache[(i, prev)]

    return helper(0, float('-inf'))


def dp_tabulation(nums: list) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    dp = [1] * (len(nums) + 1)  # Initialize dp array with 1s, because each element is a subsequence of length 1.

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)
