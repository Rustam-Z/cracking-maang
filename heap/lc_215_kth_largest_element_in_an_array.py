"""
215. Kth Largest Element in an Array

Using Heap

When you insert, you must do heapify()

"""

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        size = 0  # size of the heap

        for num in nums:
            heapq.heappush(heap, num)
            size += 1

            # When the size is bigger than k, then we need to pop the element.
            if size > k:
                heapq.heappop(heap)
                size -= 1

        # Now the min heap is of size k, so the top element will be the kth largest element
        return heapq.heappop(heap)


nums = [1, 4, 5, 2, 9, 7]
k = 2
sol = Solution()
print(sol.findKthLargest(nums, k))