"""
Problem: Given array, move zeros to the end of the array, in-place.

Questions:
    - Should we preserve the order of the elements? Yes
"""


def brute_force(array: list) -> None:
    """
    Algorithm:
        - Iterate through the array
        - If the element is zero, pop it and append it to the end of the array
    Complexity:
        Time: O(n^2)
        Space: O(1)
    """

    for i in range(len(array)):
        if array[i] == 0:
            array.pop(i)
            array.append(0)


def another_brute_force(array: list) -> None:
    """
    Algorithm:
        - Create another array
        - Iterate through the array
        - Change values of array with new_array values
    """

    new_array = []
    count_zeros = 0

    for i in range(len(array)):
        if array[i] == 0:
            count_zeros += 1
        else:
            new_array.append(array[i])

    for i in range(count_zeros):
        new_array.append(0)

    for i in range(len(array)):
        array[i] = new_array[i]


def optimized_solution(array: list) -> None:
    """
    Algorithm:
        - Create a variable to keep track of the index of the next non-zero element
        - Iterate through the array
        - If the element is non-zero, swap it with the element at the index
        - Increment the index

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    pos = 0

    for i in range(len(array)):
        if array[i] != 0:
            array[pos], array[i] = array[i], array[pos]
            pos += 1
