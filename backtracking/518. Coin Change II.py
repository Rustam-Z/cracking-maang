"""
Coin change: https://leetcode.com/problems/coin-change-ii/

Problem:
    You are given an integer array coins representing coins of different denominations
    and an integer amount representing a total amount of money.
    Find the number of combinations that make up that amount.
    If not possible, return 0.

Examples:
    Input: amount = 5, coins = [1,2,5]
    Output: 4

    Input: amount = 3, coins = [2]
    Output: 0
"""


def backtracking_solution(amount: int, coins: list) -> int:
    """
    Algorithm:
        - Try all combination of numbers.

    Time complexity: O(n^k)
    Space complexity: O(n^k)
    """
    output = []

    def backtrack(curr_sum=0, curr_comb=[]):
        if curr_sum == amount:
            output.append(curr_comb[:])
            return

        for coin in coins:
            if curr_sum + coin > amount:
                continue
            curr_comb.append(coin)
            backtrack(curr_sum + coin, curr_comb)
            curr_comb.pop()

    backtrack()
    return output  # [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [1, 2, 2], [2, 1, 1, 1], [2, 1, 2], [2, 2, 1], [5]]


if __name__ == "__main__":
    print(backtracking_solution(5, [1, 2, 5]))
