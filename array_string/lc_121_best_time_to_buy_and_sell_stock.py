"""
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem: 121. Best Time to Buy and Sell Stock

Input: Array of stock prices
Output: Max profit as int

SOLUTION 1:
    - Left and right pointers, 0 and 1
    - Move left to the position of right when prices[left] < prices[right]
    - Update profit when new max is seen
    - Time: O(n)
    - Space: O(1)
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current = prices[right] - prices[left]
                profit = max(profit, current)
            else:
                left = right

            right += 1

        return profit


