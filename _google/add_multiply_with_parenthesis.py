"""
You are given a list of tuples, and each tuple contains digits that you can perform either addition ("+") or multiplication ("*") on them.
Multiplication is always performed before addition unless addition(s) have parenthesis around them (i.e. "(1+2+3) * 4").
You are also given a target number. For each tuple return an expression string that evaluates to the target
if there is one and if there is none return "" for that tuple. Return is a list of strings.

Example 1:
list_of_arrays = [[2 3 4], [4, 3, 2]]
target = 20
Output = ["(2 + 3) * 4", "4 * (3 + 2)"]
"""
from functools import cache


def solution(nums, target):
    @cache
    def dp(i, j):
        # i is the starting index of the array
        # j is the ending index of the array

        if i == j:
            return {nums[i]: (str(nums[i]), 0)}

        res = dict()  # {target: (expression, is_addition)}
        for m in range(i, j):
            for a, (b, c) in dp(i, m).items():  # Solving sub-problems
                for d, (e, f) in dp(m + 1, j).items():  # Solving sub-problems
                    res[a + d] = (b + '+' + e, 1)
                    res[a * d] = ('(' * c + b + ')' * c + '*' + '(' * f + e + ')' * f, 0)
        return res

    # Parse the result
    var = dp(0, len(nums) - 1)
    print(var)
    return var.get(target)[0] if var else ''


if __name__ == "__main__":
    solution([2, 3, 4], 20)

