"""
abccba - palindrome
abcdcba - palindrome too
dbcasf - not palindrome
"""


# BAD, O(N) time | O(N) space
def solution1(string):
    """
    Create a new reversed string and compare with input.
    1. Traverse from the end till start, and create a new string. String concatenation is O(N^2) time complexity.
    1.1. But, if you create an array instead of string, and convert to string in the end. Time complexity will be O(N).
    2. Use reversed() which return generator. And use string join() method.
    """
    new = ''.join(reversed(string))
    return new == string


# BAD, O(N) time | O(N) or O(1) space
def solution2(string, i=0):
    """
    Using recursion.

    TO DISCUSS:
    - But sometimes recursion can be done O(1), when compiler replaces the current field in memory with next function call.
      It is called Tail recursive function.
    """
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return solution2(string, i + 1)
    # OR
    # return True if i >= j else string[i] == string[j] and solution2(string, i + 1)


# GOOD, O(N) time, O(1) space
def solution3(string):
    """
    Two points solution.
    """
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        right -= 1
        left += 1
    return True
