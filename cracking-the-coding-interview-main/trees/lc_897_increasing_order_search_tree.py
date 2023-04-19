"""
LeetCode: https://leetcode.com/problems/increasing-order-search-tree/

Problem: Given the root of a BST, rearrange so that all elements are in right side only.

Solution:
1. Use in-order traversal
2. Create a new tree, and populate the right side

Time: O(n), where n is the number of nodes in the given tree.
Space: O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    In-Order Traversal with extra memory space.
    """
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right


class Solution2:
    """
    Traversal with Relinking
    """
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right