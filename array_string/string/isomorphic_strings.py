"""
LeetCode: https://leetcode.com/problems/isomorphic-strings/

Problem: Two strings s and t are isomorphic if the characters in s can be replaced to get t.

Input: s = "egg", t = "add"
Output: true

SOLUTION 1:
    - Use defaultdict(list) and save the position of chars
    - Pros: Python keeps the order of items inserted, good for us

SOLUTION 2:
    - Create a numeric string egg=122, using counter and dictionary

Let's implement solution 1.
Time complexity: O(n), n is the length of the longest string
Space complexity: O(n), m in number of chars (n = distinct chars * indexes where they exist)
"""
from collections import defaultdict


class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_n = self.make_numeric(s)
        t_n = self.make_numeric(t)

        return s_n == t_n

    def make_numeric(self, string):
        arr = list(string)
        str_map = {}
        counter = 1

        for i in range(len(arr)):
            if arr[i] not in str_map:
                str_map[arr[i]] = counter
                counter += 1
            arr[i] = str(str_map[arr[i]])

        return ''.join(arr)


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def create_mapping(string):
            mapping = defaultdict(list)

            for idx, char in enumerate(string):
                mapping[char].append(idx)

            # For optimization purposes
            for key, value in mapping.items():
                mapping[key] = sum(value)

            return list(mapping.values())

        sm = create_mapping(s)
        tm = create_mapping(t)

        return sm == tm
