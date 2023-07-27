"""
https://leetcode.com/problems/generate-parentheses/description/

Problem: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Solution:
    - We need to use backtracking.
    - So, what this N means? It means how many times we can use ( and ). So, why not use this information?
    - We will use recursion to solve this problem. Use backtracking approach, add closing or opening 1 at a time. It will be like a tree.
    - Add open parenthesis if open_count < N
    - Add closing parenthesis if closed_count < open
    - We start from 0
    - Valid result if open == closed == n.
    - Time complexity: O(2^n)
    - Space complexity: O(2^n)
"""
from typing import List

import pytest as pytest


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []  # List of valid final combinations where open == closed == n

        def backtrack(open_count, closed_count):
            # Base case
            print(">>> stack", stack)

            if open_count == closed_count == n:
                one_combination = "".join(stack)
                print(">>>", one_combination)
                result.append(one_combination)
                return

            if open_count < n:  # We always should start from open.
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()  # Remove the element we have just added.

            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()  # Remove the element we have just added.

        backtrack(0, 0)
        return result


@pytest.mark.parametrize("args,expected", [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (1, ["()"]),
])
def _test_positive(args, expected):
    assert Solution().generateParenthesis(args) == expected


if __name__ == "__main__":
    Solution().generateParenthesis(3)
