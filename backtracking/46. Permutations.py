"""
Problem: Given the array of integers, return all permutations with these numbers.
    Input: array of integers.
    Output: array containing all permutations.

Example:
    Input: [1, 2, 3]
    Output: [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
"""
from typing import List


def permute(nums: list[int]) -> list[list[int]]:
    res = []

    # base case
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)

        res.extend(perms)

        nums.append(n)  # As we are removing the n, we have to add it again.

    return res


def permute_2(nums: List[int]) -> List[List[int]]:
    """
    Time complexity: O(n*n!), Given a set of length n, the number of permutations is n!n!n!.
    Space complexity: O(n!)
    """
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()

    ans = []
    backtrack([])
    return ans


if __name__ == "__main__":
    assert permute([1, 2, 3]) == [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]  # Order doesn't matter.
    assert permute_2([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
