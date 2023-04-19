"""
LeetCode: 669. Trim a Binary Search Tree, https://leetcode.com/problems/trim-a-binary-search-tree/

Problem: Given BST and a range, trim the tree to the given range. Structure of the tree should remain.

Solution:
1. Use recursion
2. If the node is in the range, assign left and right, then return the node
3. If node.val < min, go to right subtree, else do to left subtree

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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)