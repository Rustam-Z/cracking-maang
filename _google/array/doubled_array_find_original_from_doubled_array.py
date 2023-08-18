"""
Problem:
    An integer array original is transformed into a doubled array changed by appending twice the value
    of every element in original, and then randomly shuffling the resulting array.
    Find that array, or return [] if the array doesn't exist.

Questions:
    1. Negative numbers? Zeros? Will we have duplicates?
    2. What if the array is empty?
    3. Can we sort the array?
    4. Length of the array is even?
    5. can we reuse the same element? NO

Examples:
    Input: [1, 2, 3, 4, 2, 4, 6, 8]
    Output: [1, 2, 3, 4]
"""
from collections import defaultdict


def brute_force(array: list) -> list:
    """
    Algorithm:
        - Sort the array
        - Create a hashmap to track used items.
        - Initially we didn't remove any values. While we iterate, we will use X and X*2. If we find X*2 again them we return [].

    Complexity:
        Time: O(n log n)
        Space: O(n)
    """
    # EDGE CASES
    if len(array) < 2 or len(array) % 2 != 0:
        return []

    array.sort()  # We need sorting because if we have this case [2, 1[ We search for 2 * 2
    original = []

    # Initially we didn't remove any values. While we iterate, we will use X and X*2. If we find X*2 again them we return [].
    visited = defaultdict(int)
    for num in array:
        visited[num] += 1

    for num in array:
        if visited[num] < 1:  # DO IT LATER!!!
            continue

        if visited[num * 2] == 0 or num * 2 not in visited:  # If we already used, or even element doesn't exist.
            return []

        original.append(num)
        visited[num] -= 1
        visited[num * 2] -= 1

    return original



if __name__ == "__main__":
    print(brute_force([1, 2, 3, 4, 2, 4, 6, 8]))
    print(hash_map([1, 2, 3, 4, 2, 4, 6, 8]))
