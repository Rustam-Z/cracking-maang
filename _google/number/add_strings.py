"""
Add strings.
Numbers are strings.
"""


def addStrings(num1: str, num2: str) -> str:
    def str2int(num):
        int_ = 0
        for i in num:
            int_ = int_ * 10 + ord(i) - ord('0')  # Or create a dict like "0": 0, "1":1 ....
        return int_

    res = str(str2int(num1) + str2int(num2))
    return res
