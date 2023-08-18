"""
Min Cost Climbing Stairs: https://leetcode.com/problems/min-cost-climbing-stairs/

Problem: Given array with costs. Find min cost to reach the top of the stairs.

Constraints:
    You can either climb 1 or 2 steps.
    We can't do greedy approach. Only brute force is solution.

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1. Pay 15 and climb two steps to reach the top. The total cost is 15.

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

from typing import List


def brute_force(cost: List[int]) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def helper(i: int) -> int:  # We will try all options.5е6пи
        if i >= len(cost):
            return 0

        return min(helper(i + 1), helper(i + 2)) + cost[i]

    return min(helper(0), helper(1))


def dp_memoization(cost: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def helper(i: int) -> int:
        if i >= len(cost):
            return 0

        if dp[i] != -1:
            return dp[i]

        dp[i] = min(helper(i + 1), helper(i + 2)) + cost[i]
        return dp[i]

    dp = [-1] * len(cost)
    return min(helper(0), helper(1))
