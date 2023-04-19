"""1209. Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Problem: Remove substrings consisting from K adjacent chars .

Example:
    Input: "deeedbbcccbdaaadd" and 3
    Output: "dd"

Questions?
    String:
        - how to handle lower and upper cases?
        - will we have empty string?
        - ASCII, Unicode with special chars?
        - the length of string
        - will have too many removals?
        - string is mutable or immutable?
    Int:
        - how to handle 0, 1?
        - positive and negative number?

Edge cases:
    - After removing the new substring of K adjacent nums can be created.

The best solution:
    - Use the stack data structure, push to stack [char, quantity]
    - if quantity == k, pop from stack
"""


def removeDuplicates(s: str, k: int) -> str:
    stack = []

    for c in s:
        if stack and stack[-1][0] == c:  # check if stack is not empty
            stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])

    return ''.join(char * count for char, count in stack)
