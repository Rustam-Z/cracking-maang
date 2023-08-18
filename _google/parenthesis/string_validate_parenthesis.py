"""
20. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/

Problem: Give a string with parentheses, return True if the parentheses are valid, False otherwise.

Examples:
    Input: s = "()[]{}"
    Output: true

    Input: s = "([)]"
    Output: false

Questions and constraints:
    - Can the string be empty?
    - Can the string have other characters?

"""


def brute_force(string: str) -> bool:
    # Time complexity: O(N), where N is the length of the string.
    # Space complexity: O(N)
    stack = []

    for char in string:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False

            element = stack.pop()

            if char == ")" and element != "(":
                return False
            elif char == "}" and element != "{":
                return False
            elif char == "]" and element != "[":
                return False

    return not stack


def brute_force_clean_code(string: str) -> bool:
    stack = []
    opening = "({["
    closing = ")}]"

    for char in string:
        if char in opening:
            stack.append(char)
        else:
            if not stack:
                return False

            element = stack.pop()
            if opening.index(element) != closing.index(char):
                return False

    return False if stack else True
