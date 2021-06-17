class Solution:
    def restoreString(self, s: str, indices) -> str:
        # overall = ""
        # for i in indices:
        #     overall += s[i]
        # return overall

        # result = [s[i] for i in indices]
        # return ''.join(result)

        new_s = [''] * len(s)
        for counter, i in enumerate(indices):
            new_s[i] = s[counter]
        return ''.join(new_s)
        
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

sol = Solution()
print(sol.restoreString(s, indices))