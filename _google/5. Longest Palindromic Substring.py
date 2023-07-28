"""
https://leetcode.com/problems/longest-palindromic-substring/

Problem: Given a string s, return the longest palindromic substring in s.
    Palindrome is a word that reads the same backward as forward.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Solution 1: Brute force.
    - Try all possible substrings.
    - Time comp: O(N^3)
    - Space comp: O(1)

Solution 2: Dynamic programming.
    - Time comp: O(N^2)
    - Space comp: O(1)
"""


def brute_force(s):
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            if len(m) >= j - i:  # To reduce time
                break  # Because starts from the end
            elif s[i:j] == s[i:j][::-1]:  # O = n^3
                m = s[i:j]
                break
    return m


def dynamic_programming_expanding_from_center(s: str) -> str:
    res = ""
    res_len = 0

    for i in range(len(s)):
        # odd length
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res_len:
                res = s[left: right + 1]
                res_len = right - left + 1
            left -= 1
            right += 1

        # even length
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > res_len:
                res = s[left: right + 1]
                res_len = right - left + 1
            left -= 1
            right += 1

    return res
