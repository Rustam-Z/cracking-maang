"""
Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/

Problem:
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

Examples:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Input: strs = ["dog","racecar","car"]
    Output: ""

"""

from typing import List


def brute_force(strs: List[str]) -> str:
    """
    - Loop through the first string.
    - For each char, loop through the rest of the strings and check if the char is the same.
    - If not, return the result.
    - Time complexity: O(N * M), where N is the length of the first string, M is the length of the list.
    - Space complexity: O(1)
    """

    if not strs:
        return ""

    first_string = strs[0]
    result = ""

    for i in range(len(first_string)):
        char = first_string[i]

        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return result

        result += char

    return result


def clean_code(strs: List[str]) -> str:
    prefix = ""

    if not strs:
        return prefix

    def check_if_equal(word, char, index):
        return True if word[index] == char else False

    smallest_string = min(strs, key=len)
    for idx, char in enumerate(smallest_string):
        if all(check_if_equal(word, char, idx) for word in strs):  # Check all words
            prefix += char
        else:
            break

    return prefix
