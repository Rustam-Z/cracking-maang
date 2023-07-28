"""
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Problem: Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""
from typing import List


def brute_force(word1: List[str], word2: List[str]) -> bool:
    """
    - Concatenate strings and compare
    - Time comp: O(N*K), N is the number of strings in the list and K is the maximum length of a string in it.
    - Space comp: O(N*K)
    """
    return "".join(word1) == "".join(word2)


def two_pointers(word1: List[str], word2: List[str]) -> bool:
    # Compare characters
    # Move pointers
    # Compare characters
    # Move pointers
    # Compare characters
    # Move pointers
    # ...
    # If one pointer is at the end, but the other is not, return False
    # If both pointers are at the end, return True
    i1 = 0  # Pointer for string in word1
    i2 = 0  # Pointer for string in word2
    j1 = 0  # Pointer for character in string in word1
    j2 = 0  # Pointer for character in string in word2

    while i1 < len(word1) and i2 < len(word2):
        if word1[i1][j1] != word2[i2][j2]:  # Check characters are equal or not
            return False

        if j1 == len(word1[i1]) - 1:  # Check if the pointer is at the end of the string, then move to the next string.
            i1 += 1
            j1 = 0
        else:
            j1 += 1

        if j2 == len(word2[i2]) - 1:  # Check if the pointer is at the end of the string, then move to the next string.
            i2 += 1
            j2 = 0
        else:
            j2 += 1

    return i1 == len(word1) and i2 == len(word2)  # Check if both pointers are at the end of the list.
