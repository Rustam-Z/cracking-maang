"""
LeetCode: https://leetcode.com/problems/is-subsequence/

Problem: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

Input: s = "abc", t = "ahbgdc"
Output: true

SOLUTION 1:
    - Use the pointer in s
    - Use pointer in t
    - Loop over s and
        - if t[i] == s[i] move both pointers
        - if not equal move t's pointer
    - We return True when we reached the end of s string

Time: O(max(t, s))
Space: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if len(s) > len(t):
            return False

        s_ptr = 0

        for char in t:
            if s[s_ptr] == char:
                s_ptr += 1

                if s_ptr == len(s):
                    return True

        return False

