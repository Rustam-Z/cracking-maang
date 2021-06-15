"""
TODO:
- Create list of tuples with the indexes of sililar numbers like [(1, 4, 5), (2, 6)]
    - Grouping
    - Values at indexes 1, 4, 5 are the same

- We just need to count the frequency of similar numbers
- Then handshaking formula n(n-1)/2 with loop over each tuple in list
"""

import collections

class Solution:
    def numIdenticalPairs(self, nums) -> int:        
        counter = collections.Counter(nums)
        val = list(counter.values())
        val = [i for i in val if i > 1]
        
        overall = 0
        for n in val:
            overall += n * (n - 1) / 2

        return overall



nums = [1,2,3,1,1,3]

sol = Solution()

print(sol.numIdenticalPairs(nums))