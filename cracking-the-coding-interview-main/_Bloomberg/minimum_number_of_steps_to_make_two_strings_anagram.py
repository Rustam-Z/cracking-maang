"""1347. Minimum Number of Steps to Make Two Strings Anagram
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

Example:
    Input: s = "bab", t = "aba"
    Output: 1
    Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

"""
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        result = 0
        s_counter = Counter(s)
        t_counter = Counter(t)

        for s_key, s_value in s_counter.items():
            t_value = t_counter.get(s_key)
            if t_value is None:
                result += s_value
            elif s_value > t_value:
                result += s_value - t_value

        return result

