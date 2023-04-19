class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        """
        if target in nums:
            return nums.index(target)
        else:
            left, right = 0, len(nums) - 1

            while right >= left:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

