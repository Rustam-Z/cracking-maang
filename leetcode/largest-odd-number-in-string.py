"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) % 2 == 0:
                num = num[:i]
            else:
                return num
        
        return num 
"""

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2:
                return num[:i+1]
        
        return ''
            

# num = "52"
# num = "4206"
num = "35427"
sol = Solution()
print(sol.largestOddNumber(num))