"""
Only one possible solution exists!

possible_nums = {}
nums=[2,7,11,15]
target=9

LOOP:
    2
        9-2=7
        possible_nums = {7:0}
    7
        7 found in possible_nums
        return

"""

class Solution(object):
    def twoSum(self, nums, target):
  
        possible_nums = {}
        
        for i in range(len(nums)):
            if nums[i] in possible_nums:
                print(possible_nums)
                return possible_nums[nums[i]], i
            else:    
                possible_nums[target-nums[i]] = i


sol = Solution()
print(sol.twoSum(nums=[2,7,11,15], target=9))