"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number

Problem: Old phones keypad contain letters for each number. 2 = abc, 3 = def, 4 = ghi, 5 = jkl, 6 = mno, 7 = pqrs, 8 = tuv, 9 = wxyz.
Given string with nums, return all possible combinations of letters that the number could represent.

Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Questions and constraints:
    - 0 <= digits.length <= 4
    - digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


def brute_force(digits: str) -> List[str]:
    """
    Time: O(4^n * n)
    Space: O(n)
    """
    if not digits:
        return []

    keypad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []
    for digit in digits:
        # If there is no result yet, add all chars from keypad. This will be the first iteration.
        if not result:
            result = [char for char in keypad[digit]]
        else:
            # If it is not the first iteration, add all chars from keypad to each word in result.
            temp = []
            for char in keypad[digit]:
                for word in result:
                    temp.append(word + char)
            result = temp

    return result


def backtracking(digits: str) -> List[str]:
    """
    Time: O(4^n * n)
    Space: O(n)
    """
    n = len(digits)
    result = []

    keypad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(index, curr):
        """
        Backtracking solution, will be tree like solution:

        index = the index of the current digit we are looking at. index in digits.
        curr = the current string we are building.

        For example:
            23
                   a        b         c
                 d e f    d e f      d e f
        """
        if index >= n:
            result.append(curr)
            return

        for j in keypad[digits[index]]:
            backtrack(index + 1, curr + j)

    if digits:
        backtrack(0, "")

    return result


if __name__ == "__main__":
    print(brute_force("23"))  # ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
    print(backtracking("23"))  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
