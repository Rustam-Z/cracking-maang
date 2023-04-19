"""
LeetCode alternative: https://leetcode.com/problems/move-zeroes/ where target is 0

Problem: given an array and target, place array elements equal to target to the end.
         Do not return anything, all should be in-place.

Solutions:
1. (Trivial solution, not implemented here), sort the array, the target elements will be near each other
"""


# O(N^2) time, because we use pop
def solution1_bad(nums: list, target: int) -> None:
    """
    Iterate over an array, append & pop
    """
    counter = 0
    for _ in range(len(nums)):
        if nums[counter] == target:
            nums.append(target)
            nums.pop(counter)
        else:
            counter += 1


# O(N) time
def solution2_better(nums: list, target: int) -> None:
    """
    Using swap, we need to same the last
    """
    idx = 0  # last index of swap
    for i in range(len(nums)):
        if nums[i] != target:
            nums[idx], nums[i] = nums[i], nums[idx]
            idx += 1


# O(N) time | O(1) space
def solution3_good(nums: list, target: int) -> None:
    """
    Two pointers approach, and swapping.
    One pointer starts in the beginning of array and points to target element.
    Another starts from the end and points to non-target element.
    And we swap them, when pointers point to target and non-target elements.
    """
    start = 0  # target
    end = len(nums) - 1  # non-target

    while start < end:
        while start < end and nums[end] == target:
            end -= 1
        if nums[start] == target:
            nums[start], nums[end] = nums[end], nums[start]
        start += 1


def main():
    func = solution3_good
    test_data = ([4, 1, 3, 2, 2, 2, 4, 2], 2)
    func(*test_data)
    print(test_data[0])


if __name__ == "__main__":
    main()
