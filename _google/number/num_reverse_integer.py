"""
Reverse Integer: https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Constraints:
    - Integer can be negative. -321 = -123

Example 1: 123 -> 321
Example 2: -123 -> -321
Example 3: 120 -> 21
"""


def brute_force_solution(x: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    # Convert integer to string
    x = str(x)

    # Reverse string
    x = x[::-1]

    # Check if negative
    if x[-1] == "-":
        x = "-" + x[:-1]

    # Check if integer is within 32-bit signed integer range
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0

    # Convert back to integer
    x = int(x)

    return x


def optimized_solution(x: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check if negative
    if x < 0:
        x = -x
        is_negative = True
    else:
        is_negative = False

    # Reverse integer
    reversed_integer = 0
    while x > 0:
        reversed_integer = reversed_integer * 10 + x % 10
        x //= 10

    # Check if integer is within 32-bit signed integer range
    if reversed_integer > 2 ** 31 - 1 or reversed_integer < -2 ** 31:
        return 0

    # Check if negative
    if is_negative:
        reversed_integer = -reversed_integer

    return reversed_integer
