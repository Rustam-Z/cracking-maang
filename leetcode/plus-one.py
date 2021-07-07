"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

9
[1, 0]

9, 9
[1, 0, 0]
"""

class Solution:
    def plusOne(self, digits):
        strings = [str(integer) for integer in digits] # change elements to string data type
        a_string = "".join(strings) # joining them into one string
        an_integer = int(a_string) + 1 # adding +1
        return list(str(an_integer)) # returning the list again
        
sol = Solution()
digits = [9, 9]
print(sol.plusOne(digits))