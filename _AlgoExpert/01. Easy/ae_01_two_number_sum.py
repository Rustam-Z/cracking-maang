"""
LeetCode Alternative: https://leetcode.com/problems/two-sum/

Problem: Given an array of integers nums and an integer target,
         return two numbers such that they add up to target.

Input: Array, and target int
Output: two nums

SOLUTION 1:
    - Double for loops
    - Time: O(n^2)
    - Space: O(1)

SOLUTION 2:
    - Sort the array
    - Use left and right pointer (0, len(array) - 1)
    - Check their sum with target:
        - if smaller than target, increment left pointer
        - if larger than target, decrement right pointer
    - Time: O(n*logn), the time spent in sorting
    - Space: O(1)

SOLUTION 3:
    - Use set to save (target - num)
    - Time: O(n)
    - Space: O(n)

SOLUTION 4 (WHEN INDEX NEEDED):
    - x + y = target
    - y = target - x
    - What if we can save "y" in dict?
    - For example: [3, 5, 7] target = 10
    - So, y = 10-3=7 => dict{y : 0}
    - Then during iteration we see presence of 7 inside dict and return
    - Time: O(n), n is the len of array
    - Space: O(n)
"""


# O(n^2) time | O(1) space | #BAD
def two_number_sum_2_loops(nums, target):
    for i in range(len(nums) - 1):
        first_num = nums[i]
        for j in range(i+1, len(nums)):
            second_num = nums[j]
            if first_num + second_num == target:
                return first_num, second_num
    return []


# O(n) time | O(n) space | #NICE
def two_number_sum_set(nums, target):
    set_ = set()
    for num in nums:
        if num in set_:
            return target - num, num
        set_.add(target - num)

    return []


# O(n*logn) time | O(1) space | Here we don't use space but extra time
def two_number_sum_sorting(nums, target):
    nums.sort()
    left, right = 0, len(target) - 1

    while left <= right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return nums[left], nums[right]
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return []


# O(n) time | O(n) space
def two_number_sum_index(nums, target):
    dict_ = {}

    for idx, num in enumerate(nums):
        if num in dict_:
            return dict_[num], idx
        dict_[target - num] = idx

    return []


def check_two_number_sum(func, nums, target, expected):
    actual = func(nums, target)
    print(actual)
    assert actual == expected


if __name__ == "__main__":
    test_data = {
        "TC0": [two_number_sum_set, [2, 7, 11, 15], 9, (2, 7)]
    }

    check_two_number_sum(*test_data["TC0"])
