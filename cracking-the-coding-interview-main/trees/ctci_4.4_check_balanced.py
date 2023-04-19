"""
LeetCode: 110, https://leetcode.com/problems/balanced-binary-tree/

Problem: Given a binary tree, determine if it is height-balanced. Height-balanced = diff. no more than 1.

Solution:
1. Use DFS algorithm to check if tree is balanced.

Time: O(n)
Space: O(1)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.is_difference_less_than_one = True

        def dfs(root):
            l, r = 0, 0
            if root.left:
                l += dfs(root.left)
            if root.right:
                r += dfs(root.right)
            if abs(r - l) > 1:
                self.is_difference_less_than_one = False
            return max(r, l) + 1

        dfs(root)
        return self.is_difference_less_than_one