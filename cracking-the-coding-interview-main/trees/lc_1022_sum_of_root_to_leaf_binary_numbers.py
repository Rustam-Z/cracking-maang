"""
LeetCode: 1022. Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

Problem: Given binary tree. With zeros and ones, calculate the sum of the binary numbers.

Solution:
1. Use DFS, recursively
2. Use the bit manipulation, left shift which doubles the number, and bitwise OR. last_decimal = (last_decimal << 1) | root.val
3. If root doesn't have left and right. It means we reach the end, and then we add the last_decimal to the sum.

Time: O()
Space: O()
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        global sum_
        sum_ = 0

        last_decimal = 0

        def dfs(root, last_decimal):
            if root is None:
                return None
            else:
                last_decimal = (last_decimal << 1) | root.val

                if not (root.left or root.right):
                    global sum_
                    sum_ += last_decimal

                dfs(root.left, last_decimal)
                dfs(root.right, last_decimal)

        dfs(root, last_decimal)
        return sum_

