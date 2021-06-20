class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_s = ''
        max_length = 0
        for i in s:
            idx = new_s.find(i) # 0 here
            if idx > -1:
                print("Inner")
                max_length = max(max_length, len(new_s))
                print(max_length)
                new_s += i
                print(new_s)
                new_s = new_s[idx+1:]
                print(new_s)
            else:
                print("outer")
                new_s += i
                print(new_s)
            max_length = max(max_length, len(new_s))
        return max_length



sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))