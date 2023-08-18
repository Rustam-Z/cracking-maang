"""
https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

Problem: Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed.

Constraints:
    - After you remove, nwe occurrence can be created.

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
"""


def brute_force_python_with_replace(s: str, part: str) -> str:
    """
    - Loop through the string and check if the substring is in the string.
    - If yes, remove it.
    - Remove until there is no more substring.
    - Time complexity: O(N^2)
    - Space complexity: O(N)
    """

    while part in s:
        s = s.replace(part, "")

    return s


def brute_force_python_with_find(s: str, part: str) -> str:
    # Same as previous, but without using Python custom methods such as replace.

    while part in s:
        index = s.find(part)
        s = s[:index] + s[index + len(part):]

    return s


def brute_force(s: str, part: str) -> str:
    # Same as previous, but without using Python custom methods such as replace or find.

    part_len = len(part)
    result = ""

    i = 0
    while i < len(s):
        if s[i:i + part_len] == part:
            i += part_len
        else:
            result += s[i]
            i += 1

    return result


def optimized_solution(s: str, part: str) -> str:
    """
    - Use stack to store the char.
    - If the char is the last char of the part, check if the last len(part) chars in the stack is the same as part.
    - If yes, pop the last len(part) chars.
    - Time complexity: O(N)
    - Space complexity: O(N)
    """
    stack = []
    part_len = len(part)

    for char in s:
        stack.append(char)

        if char == part[-1]:
            if "".join(stack[-part_len:]) == part:
                for _ in range(part_len):
                    stack.pop()

    return "".join(stack)
