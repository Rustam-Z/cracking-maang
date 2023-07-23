"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Solution: https://www.youtube.com/watch?v=13m9ZCB8gjw
    - Recursively search for the nodes in the left and right subtrees.
    - If we found both nodes in the left and right subtrees, return the root.
    - If we found only one node in the left or right subtree, return that node.
    - If we didn't find any of the nodes in the left or right subtree, return False.
    - We will check ALL nodes in the tree, so the time complexity is O(N). It is kind of going from top
      to bottom. And from bottom to top.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    # O(N) time | O(N) space
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case for recursion, we reached the end of the tree.
        if not root:
            return False

        # If we found at 1 of the nodes, return it.
        if root == p or root == q:
            return root

        # Recursively search for the nodes in the left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If we found both nodes in the left and right subtrees, return the root.
        if left and right:
            return root

        # We didn't find any of the nodes in the left or right subtree, return False.
        if left is False and right is False:
            return False

        # If we found only one node in the left or right subtree, return that node.
        return left or right


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(17)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    """
    The tree looks like this:
                    3
                   / \
                  5   1
                 / \ / \
                6  2 0  8
               /  / \
              17 7   4
    """

    p = root.left.left
    q = root.left.right.left

    print(Solution().lowestCommonAncestor(root, p, q).val)
