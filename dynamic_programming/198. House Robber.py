"""
House robber: if you break two adjacent houses you will fail. Make max profit.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""


def brute_force(houses: list) -> int:
    """
    Algorithm:
        - Try all the combinations of robbing and not robbing the houses.
        - Iterate over the houses
        - For each house, check if the previous house was robbed or not
        - If the previous house was robbed, then the current house cannot be robbed
        - If the previous house was not robbed, then the current house can be robbed or not robbed.
        - Return the maximum profit

    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def helper(index: int, is_robbed: bool) -> int:
        # If we are out of bounds, return 0. This is the base case.
        if index >= len(houses):
            return 0

        if is_robbed is True:
            return helper(index + 1, False)
        else:
            return max(
                houses[index] + helper(index + 1, True),
                helper(index + 1, False)
            )

    return helper(0, False)


def dp_solution(houses: list) -> int:
    """
    Algorithm:
        - Same as brute force, but we use a cache to store the results of the subproblems. DP approach.
        - Iterate over the houses
        - For each house, check if the previous house was robbed or not
        - If the previous house was robbed, then the current house cannot be robbed
        - If the previous house was not robbed, then the current house can be robbed
        - Return the maximum profit

    Time complexity: O(n)
    Space complexity: O(n)
    """

    cache = {}

    def helper(index: int, is_robbed: bool) -> int:
        # If we are out of bounds, return 0. This is the base case.
        if index >= len(houses):
            return 0

        if (index, is_robbed) in cache:
            return cache[(index, is_robbed)]

        if is_robbed is True:
            cache[(index, is_robbed)] = helper(index + 1, False)
        else:
            cache[(index, is_robbed)] = max(
                houses[index] + helper(index + 1, True),
                helper(index + 1, False)
            )

        return cache[(index, is_robbed)]

    return helper(0, False)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    assert brute_force(nums) == 4
    assert dp_solution(nums) == 4

    nums = [2, 7, 9, 3, 1]
    assert brute_force(nums) == 12
    assert dp_solution(nums) == 12
