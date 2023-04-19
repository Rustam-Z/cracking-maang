"""
LeetCode Alternative: https://leetcode.com/problems/is-subsequence/

Problem: Given two arrays, return true if second array is a subsequence of first array, or false otherwise.

Input: Two arrays
Output: True/False

SOLUTION 1:
    - Traverse both arrays (arrIndex) and sequenceIndex
    - Increment sequenceIndex when sequenceIndex char and arrIndex char are the same
    - Continue while loop until one sequence finishes first
    - Time: O(n)
    - Space: O(1)
"""


def validate_subsequence(array, sequence):
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(array) or seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(sequence)


def validate_subsequence_solution_2(array, sequence):
    if not sequence:
        return True
    if len(sequence) > len(array):
        return False

    seq_idx = 0
    for char in array:
        if sequence[seq_idx] == char:
            seq_idx += 1
            if seq_idx == len(sequence):
                return True
    return False


def check_validate_subsequence(func, data, expected):
    actual = func(*data)
    print(actual, expected)
    assert actual == expected


if __name__ == "__main__":
    test_data = {
        "TC0": {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [1, 6, -1, 10],
            "expected": True,
        }
    }
    data = test_data["TC0"]['array'], test_data["TC0"]['sequence']
    expected = test_data["TC0"]['expected']
    funcs = validate_subsequence, validate_subsequence_solution_2

    for func in funcs:
        check_validate_subsequence(validate_subsequence, data, expected)
