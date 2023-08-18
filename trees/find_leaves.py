"""
Problem: Given a binary tree, find leaves, remove leaves, and repeat until the tree is empty.

Example:
      1
     / \
    2   3
  / \
4   5

4 5 3
2
1
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode) -> list[list]:
    """
    Algorithm:
        - While the tree is not empty:
            - Find all leaves of the tree.
            - Remove all leaves from the tree.
            - Add the leaves to the result.
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    def find_leaves(root: TreeNode) -> list[int]:
        """
        Algorithm:
            - If root is None, return []
            - If root is a leaf, return [root.val]
            - Otherwise, return the union of the leaves of the left and right subtrees.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        return find_leaves(root.left) + find_leaves(root.right)

    def remove_leaves(root: TreeNode) -> Optional[TreeNode]:
        """
        Algorithm:
            - If root is None, return None
            - If root is a leaf, return None
            - Otherwise, remove the leaves of the left and right subtrees.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return None

        if not root.left and not root.right:
            return None

        root.left = remove_leaves(root.left)
        root.right = remove_leaves(root.right)

        return root

    result = []
    while root:
        leaves = find_leaves(root)
        result.append(leaves)
        root = remove_leaves(root)

    return result


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(solution(root))
