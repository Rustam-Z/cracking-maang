"""
HOW:
- jewels make list
- use .count() in stones str to count the indidual elements from jewels
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)

        result = 0
        for i in jewels:
            result += stones.count(i)

        return result



jewels = "aA"
stones = "aAAbbbb"

sol = Solution()
print(sol.numJewelsInStones(jewels, stones))