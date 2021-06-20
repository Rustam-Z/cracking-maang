# class Solution:
#     def createTargetArray(self, nums, index):
#         target = []
#         for i, j in zip(nums, index):
#             target.insert(j, i)
#         return target

class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for i in range(0,len(nums)):
            target.insert(index[i],nums[i])
        return target
        
                
sol = Solution()
nums = [0,1,2,3,4]
nums = [1,2,3,4,0]
index = [0,1,2,3,0]
print(sol.createTargetArray(nums, index))