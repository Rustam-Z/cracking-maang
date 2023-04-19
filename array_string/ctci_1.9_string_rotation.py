"""
Leetcode alternative: 796. Rotate String

Problem: Given some string s and some goal string. Check if s can become goal after rotations.

Input: s = "abcde", goal = "cdeab"
Output: true

Time: O(N^2), where N is the length of S.
Space: O(N), the space used building S+S.
"""
import pytest


def rotate(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    combined_goal = ''.join([goal, goal])
    if s in combined_goal:
        return True
    return False


# Test cases
test_cases = [
    [("abcde", "cdeab"), True],  # TCP1: Rotate left by one
    [("abcde", "abcde"), True],  # TCP2: Rotate by zero
    [("", ""), True],  # TCP3: Empty strings

    [("de", "abcde"), False],  # TCN1: Lengthes are not the same, length of s is longer than goal
    [("abcde", "abced"), False],  # TCN2: Cannot be created with rotation
    [("abcde", "abcdef"), False],  # TCN3: Length of goal is longer than s

    [("", "a"), False],  # TCN4: Length, and empty string
    [("a", ""), False],  # TCN5: Length, and empty string
    [(" ", "abcde"), False],  # TCN6: Length, and s with space
    [("abcde", " "), False],  # TCN7: Length, and goal with space
]
test_cases_raising_errors = [
    [(21, 12), TypeError],  # TCN8: Data type should be string
    [("21", 12), TypeError],  # TCN9: Data type should be string
    [(21, "21"), TypeError],  # TCN10: Data type should be string
]

@pytest.mark.parametrize("test_input, expected", test_cases)
def test_rotate(test_input, expected):
    assert rotate(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize("test_input, expected", test_cases_raising_errors)
def test_rotate_raises_errors(test_input, expected):
    with pytest.raises(TypeError):
        rotate(test_input[0], test_input[1])
