class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        # word1 = ''.join(word1)
        # word2 = ''.join(word2)

        # word11 = ''
        # word22 = ''

        # for i in word1:
        #     word11 += i

        # for i in word2:
        #     word22 += i

        # if word11 == word22:
        #     return True
        # else:
        #     return False


        return ''.join(word1) == ''.join(word2)


        

sol = Solution()
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(sol.arrayStringsAreEqual(word1, word2))