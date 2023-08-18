"""
Problem:
    - You are given an array prices where prices[i] is the price of a given stock on the ith day.
    - Maximize profit by selling on a day after buying on a day.

Questions:
    - Can I buy and sell on the same day? No
    - Can I buy and sell on different days? Yes
    - Can I buy and sell multiple times? No
"""


def brute_force(prices: list) -> int:
    """
    Algorithm:
        - Iterate through the array
        - For each element, iterate through the rest of the array

    Time: O(n^2)
    Space: O(1)
    """
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


def optimized_solution(prices: list) -> int:
    """
    Algorithm:
        - Iterate through the array
        - Keep track of the minimum price and maximum profit
        - If the current price is less than the minimum price, update the minimum price

    Time: O(n)
    Space: O(1)
    """
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


def two_pointers_solution(prices):
    left, right = 0, 1
    max_price = 0

    while right < len(prices):
        if prices[left] < prices[right]:  # found time to sell
            curr_price = prices[right] - prices[left]
            max_price = max(max_price, curr_price)

        else:  # l > r, found new min
            left = right

        right += 1

    return max_price
