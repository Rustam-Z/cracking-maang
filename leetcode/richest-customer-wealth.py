"""
#easy

TODO:
- loop over person with the len(accounts)
- then again loop over bank accs
"""

class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth = [self.sum_main(i) for i in accounts] # just trying to create own sum() func
        max_wealth = max(wealth)
        return max_wealth
    
    def sum_main(self, list_main):
        sum = 0
        for i in range(len(list_main)):
            sum += list_main[i]
        return sum


accounts = [[1,5],[7,3],[3,5]]

sol = Solution()
print(sol.maximumWealth(accounts))