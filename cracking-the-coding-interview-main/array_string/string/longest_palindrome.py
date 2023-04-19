"""
LeetCode Alternative: https://leetcode.com/problems/longest-palindrome

Problem: 409. Longest Palindrome

Input: "abccccdd", and one longest palindrome that can be built is "dccaccd"
Output: 7, Number of letters

SOLUTION 1:
    - Count the number of occurrences of each char
    - We could accept only one char with odd number of occurances
    - Time: O(n)
    - Space: O(1), because Alphabet chars len is fixed
"""
import collections


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans