class Solution:
    def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
        # 43, 87
        '''
        keys = {'type': 0, 'color': 1, 'name': 2}
        ind = keys[ruleKey]
        return sum(1 for item in items if item[ind] == ruleValue)
        '''
        rules = ["type", "color", "name"]
        counter = 0
        for i in range(len(items)):
            if items[i][rules.index(ruleKey)] == ruleValue:
                counter += 1
        return counter


sol = Solution()
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print(sol.countMatches(items, ruleKey, ruleValue))