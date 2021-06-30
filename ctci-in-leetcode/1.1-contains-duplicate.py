class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        char_set = {}
        for i in nums:
            if char_set.get(i): # Already found this char in string
                return True 
            char_set[i] = True # True means, found one time
        return False

