"""
Coin change: https://leetcode.com/problems/coin-change

Problem: Given array of coins, and amount. Find the minimum number of coins to make up that amount.
If not possible to create that amount, return -1.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Solution 1 (DP Memoization + Backtracking):
    - We can't use greedy approach because it doesn't work for all cases. [1,3,4,5] and amount = 7. Then greedy approach will return 5 + 1 + 1, but the correct answer is 4 + 3.
    - We can use dynamic programming (memoization, to cache calculations, 4, 3 in 7) + backtracking (we try all options).
    - Every time we will create a tree. And the children will mean the remaining amount.
    Example: [1,3,4,5]
           amount = 7
           /  |  \  \
          1   3  4   5
         6   4   3    2
         6 because 7 - 1 = 6
        4 because 7 - 3 = 4
        3 because 7 - 4 = 3
        2 because 7 - 5 = 2
        Then we continue with the children. We 1, 3, 4, 5 again. Till we reach 0. It means we reach the end.
        And we update the depth. If the depth is less than the previous depth, we update it.

Solution 2 (DP bottom up + Backtracking):
    - Similar logic that is in Solution 1.
    - But we will use button up approach. We will start from 0 and go till amount.
"""
from typing import List


def coinChangeBottomUp(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)  # We will store the minimum number of coins to make up that amount.
    dp[0] = 0  # We need 0 coins to make up 0 amount.

    for a in range(1, amount + 1):  # We will go from 1 to amount.
        for c in coins:  # We will try all coins.
            if a - c >= 0:  # If the remaining amount is greater than 0, we will try to update the dp.
                dp[a] = min(dp[a], dp[a - c] + 1)  # We will update the dp with the minimum number of coins.

    return dp[amount] if dp[amount] != float('inf') else -1  # If we can't make up the amount, we will return -1.


if __name__ == "__main__":
    assert coinChangeBottomUp([1, 2, 5], 11) == 3
