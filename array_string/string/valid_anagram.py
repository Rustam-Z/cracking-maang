"""
https://leetcode.com/problems/valid-anagram/

Input: s = "anagram", t = "nagaram"
Output: true
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        match = [0] * 128

        for i in s:
            index = ord(i)
            match[index] += 1

        for i in t:
            index = ord(i)
            match[index] -= 1
            if match[index] < 0:
                return False

        return True