class Solution:
    def groupAnagrams(self, strs):
        d = {}    
        for s in strs:
            sorted_s = ''.join(sorted(s))
            temp = d.get(sorted_s, [])
            print(">",temp)
            temp.append(s)
            print(">>>",temp)
            d[sorted_s] = temp

        print(d)
        return [d[k] for k in d]

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))