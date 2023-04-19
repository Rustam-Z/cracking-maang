from typing import List


class TreeNode:
    """
    TreeNode class creates a binary search tree.
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


def build_tree(values: List[int]):
    root_value = values[0]
    root = TreeNode(root_value)
    root.insert_nodes(values[1:])
    return root


if __name__ == "__main__":
    root = build_tree([100, 50, 40, 200])
