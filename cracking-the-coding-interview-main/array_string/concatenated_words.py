"""472. Concatenated Words
https://leetcode.com/problems/concatenated-words/description/

Example:
    Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Approach:
    Create a set of words
    For each work check if it is created using concatenation. We will create a function which will check for this.
    The function will go thorough the word and divide into two parts. And check if we have two parts in set.
        If we don't have the second part we use RECURSION to check if the parts are in set again.

"""
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        concatenated_words = []

        for word in words:
            if self.is_concatenated(word, words_set):
                concatenated_words.append(word)

        return concatenated_words

    def is_concatenated(self, word: str, words_set: set) -> bool:
        for i in range(1, len(word)):
            prefix_word = word[:i]
            suffix_word = word[i:]
            if prefix_word in words_set and (suffix_word in words_set or self.is_concatenated(suffix_word, words_set)):
                return True
        return False
