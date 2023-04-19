"""
114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list
"""

class Solution:
    def flatten_bad(self, root: Optional[TreeNode]) -> None:
        """
        O(2N) time | O(2N) space, where N is number of nodes.

        Make simple pre-order traversal and save values.
        Loop over saved values, crate nodes, and connect to tree.

        NOTE! Don't forget that if you NODES themselves, be careful because they have left and right children.
        """

        if root is None:
            return None

        values = []

        def dfs(node):
            if node:
                values.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        root.left = None
        curr = root

        for i in values[1:]:
            curr.right = TreeNode(i)
            curr = curr.right

    def flatten_better(self, root: Optional[TreeNode]) -> None:
        """
        O(N) time | O(N) space, here we don't save node values.

        So to reverse the pre-order traversal, we first visit the right child,
        then the left and finally the node itself.
        Because we reach the very last node. And modifying is safe.
        """
        if root is None:
            return None

        prev = None

        def dfs(node):

            if node:
                dfs(node.right)
                dfs(node.left)

                nonlocal prev
                node.right = prev
                node.left = None
                prev = node

        dfs(root)

