"""
Problem: Given the array of integers, return all permutations with these numbers.
    Input: array of integers.
    Output: array containing all permutations.

Example:
    Input: [1, 2, 3]
    Output: [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
"""
from typing import List


def solution(nums: List[int]) -> List[List[int]]:
    """
    Algorithm:
        - Use backtracking to generate all permutations.
        - Base case: if length is equal to nums length, append to RESULT.
        - For each number in nums, if it is not in current, append it to current and backtrack.

    Time complexity: O(n*n!), Given a set of length n, the number of permutations is n!n!n!.
    Space complexity: O(n!)
    """
    ans = []

    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()

    backtrack([])
    return ans


if __name__ == "__main__":
    assert solution([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
