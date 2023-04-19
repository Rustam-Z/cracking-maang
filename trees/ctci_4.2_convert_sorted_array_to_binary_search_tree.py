"""
LeetCode: 108, https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Problem: Covert a sorted array to BST (binary search tree) 

Solution: 
1. Recursive solution, create a sub tree for each element in the array

Time: O(n)
Space: O(1)
"""

from typing import List, Optional
from binary_tree_traversals import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def rec(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            
            root.left = rec(start, mid - 1)
            root.right = rec(mid + 1, end)
        
            return root
        
        return rec(0, len(nums) - 1)
