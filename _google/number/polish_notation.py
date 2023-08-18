"""
Problem: Given arithmetical expression in polish notation, evaluate the expression.

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Questions to ask:
    - Will we have negative numbers? Float nums?
    - Will we have division to zero?
    - Can we make sure that the expression is valid?
"""


def solution(expression: list) -> int:
    """
    Algorithm:
        - Iterate through the expression
        - If the element is a number, add it to the stack
        - If the element is an operator, pop two elements from the stack, perform the operation and push the result
        - Return the last element in the stack

    Time complexity: O(n)
    Space complexity: O(n)
    """

    stack = []

    for element in expression:
        if element.isdigit():
            stack.append(int(element))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if element == '+':
                result = num2 + num1
            elif element == '-':
                result = num2 - num1
            elif element == '*':
                result = num2 * num1
            else:
                result = num2 / num1

            stack.append(result)

    return stack[-1]


def better_code_solution(expression: list) -> int:
    stack = []

    for element in expression:
        if element.isdigit():
            stack.append(int(element))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            result = eval(f'{num2}{element}{num1}')
            stack.append(result)

    return stack[-1]


if __name__ == '__main__':
    expression = ["2", "1", "+", "3", "*"]
    assert solution(expression) == 9
    assert better_code_solution(expression) == 9

    expression = ["4", "13", "5", "/", "+"]
    print(solution(expression))
    print(better_code_solution(expression))
