"""
Smallest Difference

Leetcode: https://leetcode.com/problems/minimum-absolute-difference/

Problem: given two unsorted arrays, return the smallest difference between arrays elements.

Input: [-1, 3, 10, 5, 28, 20], [17, 15, 26, 135, 32]
Result: [26, 28] because difference is 2
"""


# O() time | O() space
def solution(array1: list, array2: list) -> list:
    array1.sort()
    array2.sort()

    ptr1, ptr2 = 0, 0
    min_diff = float('inf')
    smallest_pairs = []

    while ptr1 < len(array1) and ptr2 < len(array2):
        first_num = array1[ptr1]
        second_num = array2[ptr2]
        curr_diff = abs(first_num - second_num)

        if curr_diff < min_diff:
            min_diff = curr_diff
            smallest_pairs = [first_num, second_num]

        if first_num < second_num:
            ptr1 += 1
        elif first_num > second_num:
            ptr2 += 1
        else:
            break

    return smallest_pairs


def test_solution():
    input_data = ([-1, 3, 10, 5, 28, 20], [17, 15, 26, 135, 32])
    actual_result = solution(*input_data)
    expected_result = [28, 26]
    assert actual_result == expected_result
