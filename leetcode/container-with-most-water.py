"""
11. Container With Most Water

-------------------------------------------------------------------
Brute Force:
1. Search linearly one by one O(n^2)
2. Area = length of shorter vertical line * distance between lines

class Solution:
    def maxArea(self, height) -> int:
        max = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j-i) * min(height[i], height[j])
                if area > max:
                    max = area
        return max

-----------------------------------------------------------------
Optimized Solution:
height = [1,8,6,2,5,4,8,3,7]

l_side = 0, r_side = 8
max_area = 8 * 1 = 8
l_side += 1

l_side = 1, r_side = 8
max_area = 7 * 7 = 49
r_side -= 1

l_side = 1, r_side = 6
... 
"""

class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        l_side = 0
        r_side = len(height) - 1 # because of indexing starts from 0

        while l_side < r_side:
            max_area = max(max_area, (r_side - l_side) * min(height[l_side], height[r_side])) # width * height
            if height[l_side] < height[r_side]: #
                l_side += 1
            else:
                r_side -= 1

        return max_area

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))