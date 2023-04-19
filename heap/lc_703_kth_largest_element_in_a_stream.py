""" 
703. Kth Largest Element in a Stream

Problem: Given an array of nums, and array of operations, every time after pushing to array return the Kth largest element.

Solution:
1. Use Heap data structure, apply heapify() in init
2. Tricky moment here is that you need to make the size of heaped array equal to K, so that you will not spend lots of time making the heappush to take a lot of time.
3. Then use heappush(), and again change the len

Time: O(n*logn)
Space: O(n)
"""
import heapq
from heapq import heapify
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(self.nums)
        
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
