class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))

"""
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false


sorted() returns a list, so I use ''.join() to make string.
"""