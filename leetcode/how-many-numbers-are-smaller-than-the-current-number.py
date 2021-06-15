"""
How Many Numbers Are Smaller Than the Current Number

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

TODO:
- Loop over each element
- Loop again and check how many elements less than its

- We can sort the array
"""

# Brute force solution - needs to be updated
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        overall = []
        for i in nums:
            counter = 0
            for j in range(len(nums)):
                if i > nums[j]:
                    counter += 1
            overall.append(counter)

        return overall




# nums = [8,1,2,2,3]
nums = [6,5,4,8]
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))