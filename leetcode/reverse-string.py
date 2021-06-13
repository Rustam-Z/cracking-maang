'''
#easy

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

TODO:
- Use swap and iterate though list 
    - if len odd then do not swap middle item
    - if len even then Ok

'''
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # return s[::-1]

s = ["h","e","l","l","o"]

sol = Solution()
out = sol.reverseString(s)
print(out)