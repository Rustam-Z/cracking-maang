"""
LeetCode: 257. Binary Tree Paths, https://leetcode.com/problems/binary-tree-paths/

Problem: Given the tree, find all paths till the leaf nodes of the tree.

Solution:
1. Use the DFS

Time: O(n), n = number of the nodes
Space: O(l), l = number of the leaf nodes
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.traversals = []

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        string = ""

        def traversal(root, string):
            if root:
                string += str(root.val) + "->"
                if not (root.left or root.right):
                    result.append(string[:-2])

                traversal(root.right, string)
                traversal(root.left, string)

        traversal(root, string)
        return result
