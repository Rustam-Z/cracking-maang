"""
Combination Sum: https://leetcode.com/problems/combination-sum/

Problem:
    Given an array of integers and a target integer target,
    return a list of all unique combinations of to make up that target.

Questions and constraints:
    - Integers are distinct? How about duplicates?
    - Can we use the same integer multiple times?
    - Negative integers?
"""


def backtracking_solution(array: list, target: int) -> list:
    """
    # Time complexity: O(N^2)
    # Space complexity: O(N)
    """
    result = []

    def backtrack(target: int, start: int, current: list) -> None:
        if target == 0:
            result.append(current[:])
            return

        for i in range(start, len(array)):
            if array[i] > target:
                continue

            current.append(array[i])
            backtrack(target - array[i], i, current)
            current.pop()

    backtrack(target, 0, [])
    return result


if __name__ == "__main__":
    # Positive test cases
    assert backtracking_solution([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert backtracking_solution([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Edge cases
    assert backtracking_solution([2], 1) == []
    assert backtracking_solution([1], 1) == [[1]]
    assert backtracking_solution([1], 2) == [[1, 1]]
    assert backtracking_solution([], 1) == []

    # Negative test cases: Wrong input

