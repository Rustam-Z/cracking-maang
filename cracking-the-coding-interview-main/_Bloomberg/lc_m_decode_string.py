"""394. Decode String
https://leetcode.com/problems/decode-string/

Problem: Given the string, decode it.

Example:
    "3[a]2[bc]" -> aaabcbc
    "3[a2[c]]" -> accaccacc

Questions:
    - What is the range for digits?
    - We could have nested string?
    - Letters - only lowercase english?

Solution:
    - Using stack, and push all items when item is not ]
    - When we see ] then we start decoding it and pushing to stack the result
"""


def decodeString(s: str) -> str:
    stack = []

    for i in s:
        if i != ']':
            stack.append(i)
        else:
            buffer = ''
            while stack[-1] != '[':
                buffer = ''.join((stack.pop(), buffer))
            stack.pop()

            # Find integer as it could be 4,5,6 we must calc them
            num = 0
            power = 0
            while stack and stack[-1].isnumeric():
                num = num + int(stack.pop()) * pow(10, power)
                power += 1

            stack.append(num * buffer)
    return ''.join(stack)

