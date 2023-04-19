"""
BFS
    - Time: O(n)
    - Space: O(n)

DFS (pre-order, inorder, post-order)
    - Time: O(n)
    - Space: O(d), d = depth
"""

from collections import deque


class TreeNode:
    """
    TreeNode class creates a binary search tree, and traverses the tree using BFS and DFS algorithms.

    insert_nodes(vals: list) - creates binary search tree
    bfs(root: TreeNode) - BFS traversal
    dfs(root: TreeNode) - DFS preorder traversal
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

    def _insert_node(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left._insert_node(val)
            elif val >= self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right._insert_node(val)

    def insert_nodes(self, vals: list):
        for i in vals:
            self._insert_node(i)


class Traverse:
    def bfs(self, root: TreeNode) -> list:
        if root is None:
            return None

        values = []  # CUSTOM
        queue = deque()
        queue.append(root)

        while queue:
            level_values = []  # CUSTOM
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                level_values.append(cur_node.val)  # CUSTOM

                if cur_node.left is not None:
                    queue.append(cur_node.left)

                if cur_node.right is not None:
                    queue.append(cur_node.right)

            values.append(level_values)  # CUSTOM

        return values

    @staticmethod
    def custom_print(val):
        print(val, end=" ")

    def dfs_recursive(self, root: TreeNode, operation=custom_print):
        """
        Inorder DFS traversal recursive algorithm.
        """
        if root:
            self.dfs_recursive(root.left, operation)
            operation(root.val)
            self.dfs_recursive(root.right, operation)


if __name__ == "__main__":
    tree_root = TreeNode(4)
    tree_root.insert_nodes([2, 1, 3, 6, 5, 7])

    traverse = Traverse()

    print("BFS traversal:", traverse.bfs(tree_root))
    print("DFS traversal:")
    traverse.dfs_recursive(tree_root)
