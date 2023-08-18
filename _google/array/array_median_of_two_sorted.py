"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem: Given two sorted arrays, return the median if they were combined.

Constraints:
    - The overall run time complexity should be O(log (m+n)).
    - Only integers
    - len(nums1) + len(nums2) >= 1, can be even or odd

Solution 1: Brute force
    - Combine two arrays
    - Sort the combined array
    - Return the median
    - Time comp: O((m+n)log(m+n))

Solution 2:
    - Median is the middle num
    - If odd OKAY, 3/2=1.5, means 1 is middle num, we start from 0
    - If even we take two nums, and divide
    - The goal is to use the algorithm used in merge sort. Which combining items. And counting, we just need to reach the mid points. Then time complexity will be log(m+n)

"""


def brute_force(nums1: list, nums2: list) -> float:
    combined_nums = sorted(nums1 + nums2)
    mid_point = len(combined_nums) // 2

    if len(combined_nums) % 2 == 1:
        return combined_nums[mid_point]
    else:
        return (combined_nums[mid_point - 1] + combined_nums[mid_point]) / 2


def find_median_sorted_arrays(nums1: list, nums2: list) -> float:
    """
    Time comp: O(log(m+n))
    Space comp: O(1)
    """
    m, n = len(nums1), len(nums2)
    p1, p2 = 0, 0

    # Get the smaller value between nums1[p1] and nums2[p2].
    def get_min():
        nonlocal p1, p2
        if p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
        elif p1 == m:
            ans = nums2[p2]
            p2 += 1
        else:
            ans = nums1[p1]
            p1 += 1
        return ans

    if (m + n) % 2 == 0:
        for _ in range((m + n) // 2 - 1):
            _ = get_min()
        return (get_min() + get_min()) / 2
    else:
        for _ in range((m + n) // 2):
            _ = get_min()
        return get_min()

