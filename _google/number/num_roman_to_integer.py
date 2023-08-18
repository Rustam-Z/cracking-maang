"""
Roman to integer: https://leetcode.com/problems/roman-to-integer/
Integer to roman: https://leetcode.com/problems/integer-to-roman/

Problem: Given roman numeral, convert it to an integer.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


def roman_to_integer(s):
    """
    Algorithm:
        - Create a dictionary of roman numerals and their integer values.
        - Iterate through the string and check if the current roman numeral is less than the next one.
        - If yes, then subtract the current roman numeral from the next one.
        - Else, add the current roman numeral to the total.
    Time: O(n)
    Space: O(1)
    """
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i in range(len(s)):
        if i < len(s)-1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:  # Last roman numeral will always be added.
            total -= roman_to_int[s[i]]
        else:
            total += roman_to_int[s[i]]
    return total


def integer_to_roman(num: int) -> str:
    """
    Algorithm:
        - Create a dictionary of roman numerals and their integer values.
        - Create a list of roman numerals in descending order.
        - Iterate through the roman numerals and check if the current roman numeral is less than the number.
        - If yes, then subtract the current roman numeral from the number.
        - Else, add the current roman numeral to the total.
    Time: O(n)
    Space: O(1)
    """
    int_to_roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    roman = ""
    for i in int_to_roman:
        while num >= i:
            roman += int_to_roman[i]
            num -= i
    return roman
