"""
https://leetcode.com/problems/count-primes/

Problem: Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
    Input: n = 0
    Output: 0

Example 3:
    Input: n = 1
    Output: 0
"""


def brute_force(n: int) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    def is_prime(number):
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False

        # We only need to check up to the square root of the number.
        # If the number has a divisor larger than its square root, it must also have a divisor smaller than it.
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    count = 0
    for number in range(n):
        if is_prime(number):
            count += 1

    return count


def sieve_of_eratosthenes(n: int) -> int:
    """
    Time complexity: O(n log log n)
    Space complexity: O(n)
    """

    if n <= 2:
        return 0

    # Create a boolean array "prime[0..n]" and initialize all entries it as true.
    # A value in prime[i] will finally be false if i is Not a prime, else true.
    prime = [True for _ in range(n)]

    # 0 and 1 are not prime numbers.
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            # Update all multiples of i to False.
            for j in range(i * i, n, i):
                prime[j] = False

    return sum(prime)
