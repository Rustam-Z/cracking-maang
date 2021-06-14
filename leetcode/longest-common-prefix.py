"""
#easy
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        if len(strs)==0:
            return ""
        elif " " in strs:
            return ""
        else:
            for i in range(len(min(strs, key=len))):
                if all(elem[i] == strs[0][i] for elem in strs):
                    prefix = prefix + str(strs[0][i])
                else: 
                    break

            return prefix
