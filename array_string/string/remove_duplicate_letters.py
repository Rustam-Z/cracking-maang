"""
LeetCode: https://leetcode.com/problems/remove-duplicate-letters

Problem:
    Given the string, remove duplicates letters, result should be in the smallest in lexicographical order.
    So that you should not rearrange the array, but remove the items.

Constraints:
    - Only english lower case chars
    - No spaces

Solution:
    - We will be using stack.
    - last_occ = used to capture last occurrence of any character in string
    - We traverse sequentially on the string
    - For each s[i], we check whether it's already in stack or not
    - if it is not in the stack, we need to push it to the stack. But we need to check another condition before pushing.
        - If s[i] is not in the stack (we can check using this in O(1) using a set), and it is smaller than previous
        elements in stack (lexicographically), and those elements are repeating in future (can check with last_occ),
        we need to pop these elements.
    - Now we can push s[i] in stack
    - Finally just join the characters in stack to form the result
    - We are using visited set to check whether s[i] is in stack or not in O(1) time, to improve time complexity

Time: O(N^2)
Space: O(N)

Example:
s = 'bcabc'
last_occ = { a : 2, b : 3, c : 4 }
stack trace:
[]
['b']
['b', 'c']
['a'] (b & c got popped because a < c, a < b and b and c both were gonna repeat in future)
['a' , 'b']
['a', 'b', 'c']
"""


def removeDuplicateLetters(s: str) -> str:
    last_occ = {}
    stack = []
    visited = set()

    # Save the latest index for given char
    for i in range(len(s)):
        last_occ[s[i]] = i

    # Removing duplicates and sorting lexicographically
    for i in range(len(s)):
        if s[i] not in visited:
            while stack and stack[-1] > s[i] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(s[i])
            visited.add(s[i])

        # We don't need else because we check everything in IF. If new item is smaller than some item in
        # stack, then we remove the item from stack. And we also check if we meet the item in the future

    return ''.join(stack)


def tests():
    input_data = [
        ('bcabc', 'abc'),
        ('cbacdcbc', 'acdb'),
    ]
    for input_s, expected_result in input_data:
        actual_result = removeDuplicateLetters(input_s)
        assert actual_result == expected_result
