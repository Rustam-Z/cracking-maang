"""
LeetCode: 98, https://leetcode.com/problems/validate-binary-search-tree/

Problem: Given a root of the tree, check if the tree is a valid binary search tree.

Solution:
1. Use In-order traversal to validate BST,
2. In-order traversal is a sorted list of nodes in a BST

Time: O(n), n = number of nodes
Space: O(n)
"""
from typing import Optional

from trees.binary_tree_traversals import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None

        traversed_tree = []

        def inorder_traversal(root, traversed_tree):
            if root:
                # LNR
                inorder_traversal(root.left, traversed_tree)
                traversed_tree.append(root.val)
                inorder_traversal(root.right, traversed_tree)

        inorder_traversal(root, traversed_tree)

        for i in range(1, len(traversed_tree)):
            if traversed_tree[i] <= traversed_tree[i - 1]:
                return False

        return True


class Solution2:
    def isLeave(self, node):
        return not (node.left or node.right)

    def inorder(self, node):
        if not node:
            return []
        if self.isLeave(node):
            return [node.val]
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.inorder(root)
        print(arr)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False
        return True