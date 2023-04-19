"""
414. Third Maximum Number
https://leetcode.com/problems/third-maximum-number/

Problem: given list find the 3rd largest element

Solution #1: sort array, take 3rd item, O(N*logN) time
Solution #2: use heap data structure
Solution #3: use 3 variables to keep track of 3 large numbers

"""
import heapq
from typing import List


class Solution1:
    # O(N*logN) time | O(n) for set conversion
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        nums.sort(reverse=True)
        max_ = nums[2]
        return max_


class Solution2:
    # O(N) map to negative | O(1) space
    def thirdMax(self, nums):
        # Building max heap in Python
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)

        count = 3
        ma = nums[0]
        prev = None
        while nums and count:
            temp = heapq.heappop(nums)
            if temp != prev:  # To prevent duplicated number to be added
                count -= 1
                prev = temp

        return -temp if not count else -ma


class Solution3:
    # O(N) to iterate all items | O(1) space
    def thirdMax(self, nums):
        a = b = c = float("-inf")

        for e in nums:
            if e == a or e == b or e == c:
                continue
            elif e >= a:
                c = b
                b = a
                a = e
            elif b <= e < a:
                c = b
                b = e
            elif c <= e < b:
                c = e

        return c if c != float("-inf") else a
