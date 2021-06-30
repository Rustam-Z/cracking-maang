"""
1. Like sliding window, window size depends on size of s1
2. Check 'i' from s2 is in s1, then do the step 1
3. Use ''.join(sorted(s)) == ''.join(sorted(t))

Check the number of for loop iterations:
s1=cdb, s2=abcd 
abc, bcd 

4   2
5   3

len(s2)-length_s1+1
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1 = len(s1)
        for i in range(len(s2)-length_s1+1):
            if s2[i] not in s1:
                continue
            print(s2[i:i+length_s1])
            check = ''.join(sorted(s2[i:i+length_s1])) == ''.join(sorted(s1))

            if check:
                return True
        return False


sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
# s1 = "ab"
# s2 = "eidboaoo"
print(sol.checkInclusion(s1, s2))