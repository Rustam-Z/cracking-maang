"""
Problem: Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        """
        If s[r] not in seen, we can keep increasing the window size by moving right pointer

        There are two cases if s[r] in seen:
        case0: s[r] is not inside the current window when seen[s[r]] < l, we can keep increase the window.
        case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
        """
        if s[r] not in seen:
            output = max(output, r - l + 1)
        else:
            if seen[s[r]] < l:
                output = max(output, r - l + 1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r

    return output


def tests():
    input_data = [
        ('abcabcbb', 3),
        ('tmmzuxta', 6),
        ('bbbbb', 1),
        ('pwwkew', 3),
    ]
    for input_s, expected_result in input_data:
        actual_result = lengthOfLongestSubstring(input_s)
        assert actual_result == expected_result
