"""
Problem: Given an array rotate it to right.

Example:
    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]

Questions and Clarifications:
    - Should it be done in-place? Yes
    - What if k is 0?
    - What if k is greater than the length of the array?
    - What if k is negative?
    - What if the array is empty?
    - What if the array contains only one element?

"""


def brute_force(array: list, k: int):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for _ in range(k):
        array.insert(0, array.pop())


def optimized(array: list, k: int):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    k = k % len(array)
    array[:] = array[-k:] + array[:-k]


def best_solution(array: list, k: int):
    """
    Algorithm:
        - Reverse the whole array
        - Reverse the first k elements
        - Reverse the rest of the elements

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    k = k % len(array)
    array.reverse()
    array[:k] = reversed(array[:k])
    array[k:] = reversed(array[k:])

    """
    Same operation can be done while loop
    
    # Rotate the whole array
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
        
    # Rotate the first k elements
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
        
    # Rotate the rest of the elements
    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    """
