"""
Problem: Given num and target. Insert operators to num to get target.

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Solution:
    - Use backtracking to generate all possible combinations of operators.
    - Time complexity: O(4^n * n)
    - Space complexity: O(n)
"""

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        answer = set()

        def dp(idx, total, path, last_number):
            if idx == len(num) and total == target:  # Check if we reached the end, and equaled to target.
                answer.add(path)

            if idx >= len(num):  # Check if we reached the end.
                return

            for i in range(idx, len(num)):
                if len(num[idx:i + 1]) > 1 and num[idx:i + 1][0] == "0":
                    continue

                tmp_number = num[idx:i + 1]

                if last_number == "":
                    dp(i + 1, int(tmp_number), tmp_number, tmp_number)
                else:
                    # addition
                    dp(i + 1, total + int(tmp_number), path + "+" + tmp_number, tmp_number)

                    # subtraction
                    dp(i + 1, total - int(tmp_number), path + "-" + tmp_number, "-" + tmp_number)

                    # multiplication
                    dp(i + 1, total - int(last_number) + (int(last_number) * int(tmp_number)), path + "*" + tmp_number,
                       str(int(tmp_number) * int(last_number)))

        dp(0, -1, "", "")
        return answer
