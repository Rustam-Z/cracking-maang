"""
Merge sorted array.

Questions and assumptions:
    1. Are the arrays sorted?
    2. Are the arrays of the same length?
    3. Are the arrays of the same type?
    4. Arrays don't have any trash inside?
"""


def brute_force(array1: list, array2: list) -> list:
    """
    Algorithm: Brute force method.
        - Merge the two arrays.
        - Sort the merged array.

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    return sorted(array1 + array2)


def optimized_solution(array1: list, array2: list) -> list:
    """
    Algorithm: Two pointers.
        - Similar to merge sort.
    """
    # Create a new array to store the merged array.
    merged_array = [None] * (len(array1) + len(array2))
    i = j = k = 0  # i, j, k are pointers for array1, array2, and merged_array respectively.

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array[k] = array1[i]
            i += 1
        else:
            merged_array[k] = array2[j]
            j += 1
        k += 1

    # When we run out of elements in either ARRAY1 or ARRAY2,
    # pick up the remaining elements and put in A[p..r]
    while i < len(array1):
        merged_array[k] = array1[i]
        i += 1
        k += 1

    while j < len(array2):
        merged_array[k] = array2[j]
        j += 1
        k += 1

    return merged_array


def _merge_if_array1_has_extra_zeros_inplace(array1: list, array2: list) -> None:
    """
    https://leetcode.com/problems/merge-sorted-array/

    Algorithm: Two pointers.
        - Should be inplace. Array 1 has extra zeros at the end. Number of zeros = len(array2).
        - We start from the end.
    """

    i = len(array1) - len(array2) - 1
    j = len(array2) - 1
    k = len(array1) - 1

    while i >= 0 and j >= 0:
        if array1[i] > array2[j]:
            array1[k] = array1[i]
            i -= 1
        else:
            array1[k] = array2[j]
            j -= 1
        k -= 1

    while j >= 0:
        array1[k] = array2[j]
        j -= 1
        k -= 1

