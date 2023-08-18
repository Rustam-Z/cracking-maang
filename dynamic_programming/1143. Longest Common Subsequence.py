"""
Strings longest common subsequence: https://leetcode.com/problems/longest-common-subsequence/

Problem:
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    A common subsequence of two strings is a subsequence that is common to both strings.

Input: text1 = "abcde", text2 = "ace"
Output: 3

Input: "ezupkr" "ubmrapg"
Output: 2

"""


def brute_force(text1: str, text2: str) -> int:
    """
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def helper(i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            return 1 + helper(i + 1, j + 1)

        return max(helper(i + 1, j), helper(i, j + 1))

    return helper(0, 0)


def memoization(text1: str, text2: str) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    cache = {}  # (i, j) -> result

    def helper(i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):  # Base case
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        if text1[i] == text2[j]:
            result = 1 + helper(i + 1, j + 1)
        else:
            result = max(helper(i + 1, j), helper(i, j + 1))

        cache[(i, j)] = result

        return cache[(i, j)]

    return helper(0, 0)
