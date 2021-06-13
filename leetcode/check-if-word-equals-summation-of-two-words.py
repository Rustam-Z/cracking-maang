'''
#easy

TODO:
- .lower() before feeding
- create a dict with letters and index: using zip() and iterate through ascii codes
    - 97 is a, 65 is A, 122 is z
    - ord('a') = 97
    - chr(97) = 'a'
- iterate though each letter in word, and create their numerical using str concat in new vars
- do for all 3 letters
- calculate sum with if / else 
'''


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str):
        firstWord, secondWord, targetWord = firstWord.lower(), secondWord.lower(), targetWord.lower()
        letters = [chr(i) for i in range(97, 123)]
        self.alph_index = dict(zip(letters, range(26)))

        # print(">> letters=", letters)
        # print(">> alph_index=", alph_index)

        firstWord = self.convertToNum(firstWord)
        secondWord = self.convertToNum(secondWord)
        targetWord = self.convertToNum(targetWord)

        # print(firstWord, secondWord, targetWord)

        if firstWord + secondWord == targetWord:
            return True
        else:
            return False

       
    def convertToNum(self, stringRepr):
        numRepr = ''
        for i in stringRepr:
            numRepr += str(self.alph_index[i])
        return int(numRepr)


firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"

sol = Solution()
sol.isSumEqual(firstWord, secondWord, targetWord)
