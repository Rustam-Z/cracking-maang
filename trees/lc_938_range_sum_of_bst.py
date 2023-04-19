"""
LeetCode: 938. Range Sum of BST, https://leetcode.com/problems/range-sum-of-bst/

Problem: Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low, high].

Solution:
1. Use DFS
2. Use global variable to store the sum

Time: O(n)
Space: O(1)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        global sum_
        sum_ = 0

        def dfs(root):
            if root is None:
                return None
            else:
                if root.val >= low and root.val <= high:
                    global sum_
                    sum_ += root.val
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return sum_

