"""
https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

Problem: Given a string s, return the maximum number of occurrences of any substring under the following rules:
    - The number of unique characters in the substring must be less than or equal to maxLetters.
    - The substring size must be between minSize and maxSize inclusive.

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
"""
from collections import defaultdict


def solution(s: str, max_letters: int, min_size: int, max_size: int) -> int:
    # Time complexity: O(N)
    # Space complexity: O(N)

    counts = defaultdict(int)
    answer = 0
    for i in range(len(s) - min_size + 1):
        substring = s[i: i + min_size]
        if len(set(substring)) <= max_letters:
            counts[substring] += 1
            answer = max(answer, counts[substring])

    return answer


if __name__ == "__main__":
    assert solution("aababcaab", 2, 3, 4) == 2
