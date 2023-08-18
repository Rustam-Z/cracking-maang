"""
Problem:
    Given string num representing a non-negative integer num,
    and an integer k, return the smallest possible integer after removing k digits from num.

"""
from typing import List


def brute_force(num: str, k: int) -> str:
    """
    Algorithm:
        - Try all combinations of removing k digits from num and select the smallest one.
        - Use backtracking to try all combinations.

    Time complexity: O(n^k)
    Space complexity: O(n)
    """
    res = []

    def backtrack(start: int, path: List[str]) -> None:
        if len(path) == len(num) - k:
            res.append(int(''.join(path)))
            return

        for i in range(start, len(num)):
            path.append(num[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return min(res)


def greedy_with_stack(num: str, k: int) -> str:
    """
    Algorithm:
        - Use a stack to store the digits.
        - If the current digit is smaller than the top of the stack, pop the stack.
        - If the current digit is larger than the top of the stack, push the current digit to the stack.
        - Remove leading zeros from the stack.
        - Return the stack as a string.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    stack = []
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # while k > 0:
    #     stack.pop()
    #     k -= 1

    # if not stack:
    #     return '0'

    while stack and stack[0] == '0':
        stack.pop(0)

    return ''.join(stack)


if __name__ == '__main__':
    print(brute_force('1432219', 3))
    print(greedy_with_stack('1432219', 3))
    print(brute_force('10', 0))
