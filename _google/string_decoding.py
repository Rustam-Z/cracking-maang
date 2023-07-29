"""
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
    - Integers can be from 1 to 300.
    - Inner strings inside [] are compound.
    - [] can be nested.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != ']':  # We will push everything except ']'
                stack.append(i)
            else:
                buffer = ''  # Create the string that is inside []
                while stack[-1] != '[':
                    buffer = ''.join((stack.pop(), buffer))
                stack.pop()  # Remove '['

                # Find integer as it could be 4,5,6 we must calc them
                num = 0
                power = 0
                while stack and stack[-1].isnumeric():
                    num = num + int(stack.pop()) * pow(10, power)
                    power += 1

                stack.append(num * buffer)

        return ''.join(stack)
