"""
Climbing Stairs: https://leetcode.com/problems/climbing-stairs/

Problem: How many ways to climb to top.

Constrains:
    Start at index 0 or 1
    Can only climb 1 or 2 steps at a time
    n >= 1

Solution:
    1. Brute Force
        - Recursion
        - Time: O(2^n)
        - Space: O(n)
    2. Recursion with Memoization
        - Time: O(n)
        - Space: O(n)
    3. Dynamic Programming
        - Time: O(n)
        - Space: O(n)
"""


# Brute Force
def brute_force(n):
    """
        0         1
      1  2      1  2  Either I can take 1 or 2 steps
    1 2 1 2   1 2 1 2
    if sum = n then result += 1
    if sum > n then stop
    if sum < n then continue

    Time: O(2^n)
    Space: O(n)

    We are repeating the same calculations. We can use memoization to cache the calculations.
                       0
                    1     2
                2   3    3  4
             3 4   3 4  4 5 4 5
             You see how many 3s we have. We can cache it.s
    """
    def helper(n, sum):
        if sum == n:
            return 1
        if sum > n:
            return 0
        return helper(n, sum+1) + helper(n, sum+2)

    return helper(n, 0)


# Recursion with Memoization
def dp_memoization(n):
    """
    Time: O(n)
    Space: O(n)
    """
    def helper(n, memo):
        if n == 0 or n == 1:
            return 1
        if memo[n] == 0:
            memo[n] = helper(n-1, memo) + helper(n-2, memo)
        return memo[n]

    memo = [0] * (n+1)
    return helper(n, memo)


# Dynamic Programming (Bottom Up)
def dp_bottom_up(n):
    # Edge case
    if n == 0 or n == 1:
        return 1

    # Setup dp array
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]  # We can only take 1 or 2 steps at a time.

    return dp[-1]
