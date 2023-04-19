"""
To lower case
Input: s = "Hello"
Output: "hello"
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        lst = list(s)

        for i in range(len(lst)):
            if ord(lst[i]) >= 65 and ord(lst[i]) <= 90:
                lst[i] = chr(ord(lst[i]) + 32)

        return ''.join(lst)

        # return s.lower() # 75 / 65

