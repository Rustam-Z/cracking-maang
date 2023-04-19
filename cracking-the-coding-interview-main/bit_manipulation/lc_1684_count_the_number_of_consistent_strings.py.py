"""
LeetCode: https://leetcode.com/problems/count-the-number-of-consistent-strings/
1684. Count the Number of Consistent Strings

Problem: Given the string allowed, and words list. Count the number of words in the list, which only consist from allowed string.

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Solution:
1.
2.
3.

Time: O()
Space: O()
"""

from typing import List

ORD_A = ord('a')


def encode(s: str) -> int:
    output = 0
    for e in s:
        output |= 1 << (ord(e) - ORD_A)
    return output


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_encoded = encode(allowed)
        return sum(allowed_encoded & w_encoded == w_encoded for w_encoded in map(encode, words))


if __name__ == "__main__":
    s = Solution()
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    # print(s.countConsistentStrings(allowed, words))

    print(encode("aa"))
