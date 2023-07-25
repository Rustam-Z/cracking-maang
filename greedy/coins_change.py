"""
Problem: You have to make a change of an amount using the smallest possible number of coins.
    Available coins are $5 coin, $2 coin, $1 coin.
    There is no limit to the number of each coin you can use.

Input: $18
Output: set of coins that make up $18. {5, 5, 5, 2, 1}

Constraints:
    - No negative integers
    - No floating point numbers
    - No zero
    - No empty string

Solution:
    - Greedy algorithm
    - Sort the coins in descending order.
    - Start from the largest coin.
    - If the amount is greater than or equal to the coin, then add the coin to the change.
    - Subtract the coin from the amount.
    - Repeat the process until the amount is zero.

TIme complexity: O(n), where n is the number of coins.
Space complexity: O(n), where n is the number of coins in change.
"""


def coins_change(amount: int) -> list[int]:
    coins = (5, 2, 1)
    change = []

    while amount > 0:
        for coin in coins:
            if amount >= coin:
                change.append(coin)
                amount -= coin
                break

    return change


def main():
    test_data = 18
    solution = coins_change(amount=test_data)
    print(solution)


if __name__ == "__main__":
    main()
