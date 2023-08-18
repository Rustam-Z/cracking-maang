"""
78. Subsets: https://leetcode.com/problems/subsets/

Problem: Given an integer array nums of unique elements, return all possible subsets (the power set).

Example:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Questions and clarifications:
    - Should we create all possible subsets? Or define a max size?
    - What if the array is empty?
"""


def brute_force(nums: list) -> list:
    # Time complexity: O(N * 2^N)
    # Space complexity: O(N * 2^N)

    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [num])

    return subsets


def backtracking(nums: list) -> list:
    # Time complexity: O(N * 2^N)
    # Space complexity: O(N * 2^N)
    output = []

    def backtrack(curr, start):
        output.append(curr[:])

        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()

    backtrack([], 0)
    return output


if __name__ == "__main__":

    # Positive cases.
    assert brute_force([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    # Edge cases.
    assert brute_force([1]) == [[], [1]]
    assert brute_force([]) == [[]]
