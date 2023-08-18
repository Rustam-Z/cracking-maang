"""
Problem: Longest string chain.
https://leetcode.com/problems/longest-string-chain/

Questions to ask:
    - Only english lowercase letters? YES

"abc" is a predecessor of "abac"
"""


def brute_force(words: list) -> int:
    """
    Algorithm:
        - Sort the words by length
        - For each word, check if it's a predecessor of any other word
            "abc" is a predecessor of "abac"
        - If it is, add it to the chain
        - Return the longest chain

    Complexity:
        - Time: O(n^2)
        - Space: O(1)
    """
    def is_predecessor(word1, word2):
        """
        Use set to check if word1 is a predecessor of word2.
        """
        if len(word1) + 1 != len(word2):
            return False
        word1_set = set(word1)
        word2_set = set(word2)
        return word1_set == word2_set - set(word1)

    words.sort(key=len)
    longest_chain = 0
    for i in range(len(words)):
        chain = 0
        for j in range(i + 1, len(words)):
            if is_predecessor(words[i], words[j]):
                chain += 1
        longest_chain = max(longest_chain, chain)
    return longest_chain


def dynamic_programming(words: list) -> int:
    """
    Algorithm:
        - Sort the words by length
        - For each word, check if it's a predecessor of any other word
            "abc" is a predecessor of "abac"
        - If it is, add it to the chain
        - Return the longest chain

    Complexity:
        - Time: O(n^2)
        - Space: O(1)
    """

    words.sort(key=len)

    d = {}
    longest_chain = -float('inf')
    for word in words:
        d[word] = 1
        for i in range(len(word)):
            s = word[:i] + word[i + 1:]
            if s in d:
                d[word] = max(d[word], d[s] + 1)
        longest_chain = max(longest_chain, d[word])

    return longest_chain