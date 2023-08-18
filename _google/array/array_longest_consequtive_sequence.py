"""
Problem:
    Given an array of integers nums, return the length of the longest consecutive elements sequence.

    NOTE! Consecutive elements sequence is a sequence of elements that appears in ascending order.
          NOT NECESSARILY ADJACENT IN THE ARRAY.

Questions:
    - Array is sorted? No
    - How to handle duplicates?
    -
"""


def brute_force(array: list) -> int:
    """
    Algorithm:
        - Sort the array
        - Iterate through the array
            - If the current element is equal to the next element
                - Increment the counter
            - Else
                - Reset the counter

    Complexity:
        Time: O(nlogn)
        Space: O(1)
    """
    if not array:
        return 0

    array.sort()
    max_length = 1
    current_length = 1

    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            current_length += 1
        else:
            current_length = 1

        max_length = max(max_length, current_length)

    return max_length


def optimized_solution(array: list) -> int:
    """
    Algorithm:
        - Create a set of the array
        - Iterate through the array
            - If the current element - 1 is not in the set
                - Increment the counter
                - While the current element + 1 is in the set
                    - Increment the counter
                - Update the max_length
    """
    if not array:
        return 0

    array_set = set(array)
    max_length = 1

    for num in array:
        if num - 1 not in array_set:  # This is the first element of the sequence.
                                      # If it is in set then it is not the first element.
            current_length = 1

            while num + 1 in array_set:
                current_length += 1
                num += 1

            max_length = max(max_length, current_length)

    return max_length

