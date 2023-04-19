"""
LeetCode: -

Problem: Given the root of the tree, return the list of branch sums

        1
       / \
     2    3
    / \   / \
   4   5 6  7
  /\   /
 8 9  10

[15, 16, 18, 10, 11]

SOLUTION 1:
    - DFS
    - Recursively
    - Time: O(N)
    - Space: O(N)
"""


class TreeNode:
    def __init__(self, value=0):
        self.right = None
        self.left = None
        self.val = value


# O(N) time | O(N) space
def branch_sum(root: TreeNode) -> list:
    list_ = []
    sum_init = 0

    def dfs(node: TreeNode, sum_: int) -> None:
        if node:
            sum_ += node.val
            if node.left is None and node.right is None:
                list_.append(sum_)
            dfs(node.left, sum_)
            dfs(node.right, sum_)

    dfs(root, sum_init)
    return list_
