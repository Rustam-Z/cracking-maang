class Solution:
    def replaceDigits(self, s: str) -> str:
        result_s = ''
        
        for i in range(len(s)):
            if i % 2 != 0: # number
                result_s += self.shift(s[i-1], s[i])
            else:
                result_s += s[i]
        return result_s
    
    def shift(self, ch, digit):
        new_ch = ord(ch) + int(digit)
        
        return chr(new_ch)
        