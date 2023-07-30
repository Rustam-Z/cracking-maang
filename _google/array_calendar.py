"""
Given any 3 numbers, and list the permutations of valid dates. For example, giving (2, 7, 29),
the permutations of valid dates would be [(2, 7, 29), (29, 2, 7), (29, 7, 2)], if in (yyyy,mm,dd) format.
If there is no valid permutation, return an empty list. Please implement this function, get_valid_dates(num1, num2, num3).

Hint: Please notice solar/lunar months and leap year issues.

Other examples:
(4, 13, 100) --> [(100, 4, 13)]
(21, 13, 15) --> [ ], no valid permutation
(5,6,7) --> [(5,6,7), (5,7,6), (6,5,7), (6,7,5), (7,5,6), (7,6, 5)]
(6,31,10) --> [(6,10,31), (31,6,10),(31,10,6)]

References:
Solar Months: Jan(1), Mar(3). May(5), Jul(7), Aug(8), Oct(10), Dec(12) --> 31 days
Lunar Months: Apr(4), Jun(6), Sep(9), Nov(11) --> 30 days
"""

from itertools import permutations


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(year, month, day):
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]

    if month == 2:
        if is_leap_year(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    elif month in months_with_31_days:
        return 1 <= day <= 31
    elif month in months_with_30_days:
        return 1 <= day <= 30
    else:
        return False


def get_valid_dates(num1, num2, num3):
    valid_dates = []
    all_permutations = list(permutations([num1, num2, num3]))

    for date in all_permutations:
        year, month, day = date
        if is_valid_date(year, month, day):
            valid_dates.append(date)

    return valid_dates


# Test examples
print(get_valid_dates(2, 7, 29))
print(get_valid_dates(4, 13, 100))
print(get_valid_dates(21, 13, 15))
print(get_valid_dates(5, 6, 7))
print(get_valid_dates(6, 31, 10))
