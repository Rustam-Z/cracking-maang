"""
55. Jump Game: https://leetcode.com/problems/jump-game/

Problem:
    Given an array of integers, calculate if we can reach the end of array.
    Each index is representing how many max jumps we can perform.
"""


def brute_force_backtracking(nums: list) -> bool:
    """
    Algorithm:
        - Try all possible combinations

    Time complexity: O(2^N)
    Space complexity: O(N)
    """
    def backtrack(start=0):
        if start >= len(nums) - 1:
            return True

        for i in range(start + 1, start + nums[start] + 1):
            if backtrack(i):
                return True

        return False

    return backtrack()


def optimized_solution_greedy_approach(nums: list) -> bool:
    """
    Algorithm:
        - Greedy approach
        - Keep track of the furthest index we can reach
        - If we can reach the end of array, return True
        - If we can't reach the end of array, return False

    Time complexity: O(N)
    Space complexity: O(1)
    """
    furthest_index = 0

    for i in range(len(nums)):
        if i > furthest_index:
            return False

        furthest_index = max(furthest_index, i + nums[i])  # Greedy approach to select max jump

    return True


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    assert brute_force_backtracking(nums) is True

    nums = [3, 2, 1, 0, 4]
    assert brute_force_backtracking(nums) is False
