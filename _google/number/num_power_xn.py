"""
Pow(x, n): https://leetcode.com/problems/powx-n/

Problem: Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Constraints:
    - Power can be negative. Ex: 2^-2 = 1/2^2 = 1/4 = 0.25

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
"""


def brute_force(x: float, n: int) -> float:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    result = 1
    for _ in range(abs(n)):
        result *= x

    return result if n >= 0 else 1 / result


def optimized_solution(x: float, n: int) -> float:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    result = 1.0

    if n == 0:
        return result
    elif n < 0:
        x = 1 / x
        n = -n

    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2

    return result


def myPow(x: float, n: int) -> float:
    def helper(x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        result = helper(x, n // 2)
        result = result * result
        return x * result if n % 2 else result

    result = helper(x, abs(n))
    return result if n >= 0 else 1 / result
