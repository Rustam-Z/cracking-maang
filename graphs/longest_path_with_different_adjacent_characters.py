"""2246. Longest Path With Different Adjacent Characters
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/

Approach:
    - Graph DFS algorithm
    - The tree is n-ary, and we need to create a path. Path has its start and end.
    - So we can take only two longest children path. And for this reason we need to keep track of longest and second_longest.
    - We need to keep track of overall result as a global var or smth like this.
        - result = max(result, longest + second_longest + 1)

"""
from collections import defaultdict
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adjacency_list = defaultdict(list)
        for idx, value in enumerate(parent):
            adjacency_list[value].append(idx)

        del adjacency_list[-1]  # We don't have parent of 0

        result = 0

        def dfs(node):
            nonlocal result
            longest = 0
            second_longest = 0

            for child in adjacency_list[node]:
                val = dfs(child)

                if s[node] != s[child]:
                    if val > second_longest:
                        second_longest = val
                    if second_longest > longest:
                        longest, second_longest = second_longest, longest

            result = max(result, longest + second_longest + 1)
            return longest + 1

        dfs(0)
        return result
