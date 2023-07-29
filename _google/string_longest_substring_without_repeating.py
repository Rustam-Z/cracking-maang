"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem: Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Solution 1:
    - Use sliding window for substring, and hashmap to store the char and its index.
    - Time complexity: O(N)
    - Space complexity: O(N)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        result = 0

        for end, char in enumerate(s):
            if char not in seen:
                result = max(result, end - start + 1)
            else:
                if seen[char] < start:  # If we have two chars and both in seen. We continue with the front char.
                    # Example: tmmzuxt, t and m in seen. when we see second t, we don't jump to it, but still use 2nd m.
                    result = max(result, end - start + 1)
                else:
                    start = seen[char] + 1

            seen[char] = end

        return result


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("tmmzuxt") == 5
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring(" ") == 1
    assert Solution().lengthOfLongestSubstring("dvdf") == 3
