"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

Problem: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""


def brute_force(haystack: str, needle: str) -> int:
    # Time complexity: O(N * H), where N is the length of needle, H is the length of haystack.
    # Space complexity: O(1)
    N, H = len(needle), len(haystack)

    for i in range(H - N + 1):
        for j in range(N):
            if needle[j] != haystack[i + j]:
                break
            if j == N - 1:
                return i

    return -1


def strStr(haystack: str, needle: str) -> int:
    """
    - Keep a pointer to the needle.
    - Time
    """
    if not needle:
        return 0

    if len(needle) > len(haystack):
        return -1

    needle_ptr = 0
    i = 0
    while i < len(haystack):
        item_value = haystack[i]
        if item_value == needle[needle_ptr]:
            needle_ptr += 1

            if needle_ptr == len(needle):
                return i - len(needle) + 1
        else:
            if needle_ptr != 0:
                i -= needle_ptr
            needle_ptr = 0

        i += 1


def strStr2(haystack: str, needle: str) -> int:
    start = 0
    end = len(needle)

    if needle == "":
        return 0

    while end <= len(haystack):
        if haystack[start:end] == needle:
            return start
        else:
            start = start+1
            end = end+1

    return -1


if __name__ == "__main__":
    assert strStr("sadbutsad", "sad") == 0
    assert strStr("sadbutsad", "sad1") == -1
    assert strStr("sadbutsad", "sadbut") == 0
    assert strStr("sadbutsad", "sadbut1") == -1
