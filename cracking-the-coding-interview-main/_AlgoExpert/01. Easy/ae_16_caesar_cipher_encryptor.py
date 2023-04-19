"""
https://www.hackerrank.com/challenges/caesar-cipher-1/problem

Place letters in circular alphabetical order after k shifts

Example:
    Input: xyz 2
    Output: zab

CORNER CASES:
    - Should we consider only letters (lower, upper, or both)?
    - Should we consider special chars like /, \, ]?
    - !!!NOTE 65 <= upper <= 90, 95 <= lower <= 122
"""


# O(n) time | O(n) space
def solution1(s, k):
    def getNewLetter(letter, key):
        ascii = ord(letter)
        new_ascii = ascii + key
        if new_ascii <= 122:
            return chr(new_ascii)
        else:
            return chr(96 + new_ascii % 122)

    key = k % 26
    list_ = list(s)

    for idx, char in enumerate(list_):
        list_[idx] = getNewLetter(char, key)

    return ''.join(list_)


print(solution1("abcd", 2))  # cdef
print(solution1("ABCD", 2))  # CDEF
print(solution1("abCD", 2))  # cdEF
print(solution1("xyzXYZ", 2))  # zabZ[\


# O(n) time | O(n) space
def solution2(string, key):
    def getNewLetter(letter, key, alphabet):
        newLetterCode = alphabet.index(letter) + key
        return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]

    newLetters = []

    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)


print(solution2("abcd", 2))  # cdef
print(solution2("ABCD", 2))  # CDEF
print(solution2("abCD", 2))  # cdEF
print(solution2("xyzXYZ", 2))  # zabZ[\
