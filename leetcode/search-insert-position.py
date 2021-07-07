"""

Input: nums = [1,3,5,6], target = 5
Output: 2

"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # returning index if already present
        if(target in nums):
            return nums.index(target)
        else:
			# perfroming binary search to determine the position
            start, mid, end = 0, 0, len(nums) - 1
            while start <= end:
                mid = (start + end)//2
                if(nums[mid] < target):
                    start = mid + 1
                else:
                    end = mid - 1
            return start