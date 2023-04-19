"""
LeetCode: 102, https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Solution:
1. Use BFS
2. Use queue (deque)

Time: O(n), where n is the number of nodes
Space: O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []

        queue, result_list = [], []
        queue.append(root)

        while queue:
            nodes_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes_values.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result_list.append(nodes_values)

        return result_list
