"""
https://leetcode.com/problems/kth-largest-element-in-an-array

Problem: Given unsorted array, return the kth largest element in the array.
"""
import heapq


def brute_force(nums: list[int], k: int) -> int:
    # Sort the array in descending order, and use index.
    # Time complexity: O(NlogN), Space complexity: O(1)
    nums.sort(reverse=True)
    return nums[k - 1]


def with_heap(nums: list[int], k: int) -> int:
    # Time complexity: O(NlogK), Space complexity: O(K)
    heap = []
    for num in nums:
        heapq.heappush(heap, num)  # Time complexity: O(logK)
        if len(heap) > k:
            heapq.heappop(heap)

    return heapq.heappop(heap)
