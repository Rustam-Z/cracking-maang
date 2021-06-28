class Solution:
    def increasingTriplet(self, nums) -> bool:
#         nums_set = []
#         flag = False
#         for i in range(len(nums)-2):
#             nums_set = [i, i+1, i+2]
            
#             if nums_set[1] > nums[0] and nums[1] < nums[2]:
#                 flag = True
         
#         return flag
        smallest = second_smallest = float('inf')
        for num in nums:
            if num < smallest:
                smallest = num
            if smallest < num < second_smallest:
                second_smallest = num
            if num > second_smallest:
                return True
        return False
        