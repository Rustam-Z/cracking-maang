"""
LeetCode: 538. Convert BST to Greater Tree, https://leetcode.com/problems/convert-bst-to-greater-tree/

Problem: Given the root of BST, change the root.val to sum of bigger elements.

Solution:
1. Use the pre-order traversal but RNL

Time: O(n)
Space: O()
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root
